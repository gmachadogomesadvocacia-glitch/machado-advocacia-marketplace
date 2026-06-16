#!/usr/bin/env python3
"""
Hook UserPromptSubmit do plugin Civel Adv-OS.

Logica (ativacao automatica por contexto):
1. Le o prompt via stdin (JSON padrao Claude Code hooks).
2. Detecta bypass explicito: flags `--no-revisao`, `--quick`, `--no-r1r4`, `/revisao off`.
3. Detecta GATILHO de DOMINIO via keywords (3 niveis):
   - Gatilho 1: prompt contem palavras do dominio civil/processo civil
   - Gatilho 2: keywords fortes do dominio
   - Gatilho 3: comandos `/start-civel`, `/civel-master`, etc.
4. Se gatilho dispara:
   - Verifica se `civel/cowork-state.json` existe no path atual
   - SIM: injeta protocolo Revisao Tecnica R1-R4 + aponta para skill `civel-master`
   - NAO: sugere `/start-civel` ao usuario (mas nao bloqueia)
5. Se ha bypass: reafirma em stdout que o bypass foi aceito (transparencia).
6. Se nao eh tarefa do dominio: silencio (exit 0 sem output).

Tambem respeita state.json: se `revisao_tecnica.enabled = false`, nunca injeta R1-R4.

Stdlib only.
"""

from __future__ import annotations

import io
import json
import os
import re
import sys
from pathlib import Path

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

SCRIPT_DIR = Path(__file__).resolve().parent
PLUGIN_ROOT = SCRIPT_DIR.parent.parent
sys.path.insert(0, str(PLUGIN_ROOT / "scripts"))

import importlib.util
spec = importlib.util.spec_from_file_location("hook_utils", PLUGIN_ROOT / "scripts" / "hook-utils.py")
hook_utils = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hook_utils)


# NOTA: os nomes TRIGGER_MEDICO / DOMAIN_KEYWORDS / CONSUM_KEYWORDS_GENERAL /
# _is_medico sao internos (herdados do engine portado) e nao tem efeito de
# dominio — aqui carregam o lexico do DIREITO CIVIL E PROCESSO CIVIL. Mantidos
# para preservar a logica do hook.

# Gatilho 1: frases fortes do dominio civil/processo civil (case insensitive)
TRIGGER_MEDICO = [
    r"\bdireito\s+civil\b", r"\bprocesso\s+civil\b",
    r"\bresponsabilidade\s+civil\b", r"\bato\s+il[íi]cito\b",
    r"\bdano\s+moral\b", r"\bdano\s+material\b", r"\bdano\s+est[ée]tico\b",
    r"\bdano\s+emergente\b", r"\blucro\s+cessante\b", r"\bnexo\s+causal\b",
    r"\bresponsabilidade\s+objetiva\b", r"\bindeniza[çc][ãa]o\b",
    r"\brepara[çc][ãa]o\b", r"\bacidente\s+de\s+tr[âa]nsito\b",
    r"\bDPVAT\b", r"\ba[çc][ãa]o\s+de\s+regresso\b",
    r"\bresponsabilidade\s+civil\s+do\s+estado\b",
    r"\binadimplemento\b", r"\bclausula\s+penal\b", r"\bcl[áa]usula\s+penal\b",
    r"\brevis[ãa]o\s+contratual\b", r"\bvicio\s+redibit[óo]rio\b",
    r"\bv[íi]cio\s+redibit[óo]rio\b", r"\bevic[çc][ãa]o\b",
    r"\bneg[óo]cio\s+jur[íi]dico\b", r"\bfraude\s+contra\s+credores\b",
    r"\ba[çc][ãa]o\s+de\s+cobran[çc]a\b", r"\ba[çc][ãa]o\s+monit[óo]ria\b",
    r"\bexecu[çc][ãa]o\s+de\s+t[íi]tulo\s+extrajudicial\b",
    r"\bbusca\s+e\s+apreens[ãa]o\b", r"\baliena[çc][ãa]o\s+fiduci[áa]ria\b",
    r"\bDL\s*911\b", r"\btutela\s+provis[óo]ria\b",
    r"\btutela\s+de\s+urg[êe]ncia\b", r"\btutela\s+de\s+evid[êe]ncia\b",
    r"\bconsigna[çc][ãa]o\s+em\s+pagamento\b",
    r"\bc[óo]digo\s+civil\b", r"\bc[óo]digo\s+de\s+processo\s+civil\b",
]

# Gatilho 2: keywords fortes do dominio civil/processo civil
DOMAIN_KEYWORDS = [
    # Responsabilidade civil / indenizatorias
    r"\bresponsabilidade\s+civil\b", r"\bato\s+il[íi]cito\b",
    r"\bdano\s+moral\b", r"\bdano\s+material\b", r"\bdano\s+est[ée]tico\b",
    r"\bdano\s+emergente\b", r"\blucro\s+cessante\b", r"\bnexo\s+causal\b",
    r"\bculpa\b", r"\bdolo\b", r"\bresponsabilidade\s+objetiva\b",
    r"\bindeniza[çc][ãa]o\b", r"\brepara[çc][ãa]o\b", r"\bquantum\b",
    r"\bacidente\s+de\s+tr[âa]nsito\b", r"\bDPVAT\b", r"\bregresso\b",
    r"\bseguradora\b", r"\bresponsabilidade\s+civil\s+do\s+estado\b",
    r"\bfazenda\s+p[úu]blica\b",
    # Contratos e obrigacoes
    r"\bcontrato\b", r"\bobriga[çc][ãa]o\b", r"\binadimplemento\b", r"\bmora\b",
    r"\bcl[áa]usula\s+penal\b", r"\bdistrato\b", r"\brescis[ãa]o\b",
    r"\brevis[ãa]o\s+contratual\b", r"\bpresta[çc][ãa]o\s+de\s+servi[çc]o\b",
    r"\bm[úu]tuo\b", r"\bcomodato\b", r"\bmandato\b", r"\bdoa[çc][ãa]o\b",
    r"\bfian[çc]a\b", r"\bv[íi]cio\s+redibit[óo]rio\b", r"\bevic[çc][ãa]o\b",
    # Negocio juridico / vicios do consentimento
    r"\bneg[óo]cio\s+jur[íi]dico\b", r"\bvicio\s+do\s+consentimento\b",
    r"\bv[íi]cio\s+do\s+consentimento\b", r"\bcoa[çc][ãa]o\b", r"\bles[ãa]o\b",
    r"\bestado\s+de\s+perigo\b", r"\bsimula[çc][ãa]o\b",
    r"\bfraude\s+contra\s+credores\b", r"\banula[çc][ãa]o\b", r"\bnulidade\b",
    # Cobranca e execucao
    r"\ba[çc][ãa]o\s+de\s+cobran[çc]a\b", r"\ba[çc][ãa]o\s+monit[óo]ria\b",
    r"\bexecu[çc][ãa]o\s+de\s+t[íi]tulo\s+extrajudicial\b",
    r"\bt[íi]tulo\s+extrajudicial\b", r"\bcheque\b", r"\bnota\s+promiss[óo]ria\b",
    r"\bduplicata\b", r"\bbusca\s+e\s+apreens[ãa]o\b",
    r"\baliena[çc][ãa]o\s+fiduci[áa]ria\b", r"\bDL\s*911\b",
    # Obrigacoes e tutelas
    r"\bobriga[çc][ãa]o\s+de\s+fazer\b", r"\bobriga[çc][ãa]o\s+de\s+n[ãa]o\s+fazer\b",
    r"\bobriga[çc][ãa]o\s+de\s+dar\b", r"\btutela\s+provis[óo]ria\b",
    r"\btutela\s+de\s+urg[êe]ncia\b", r"\btutela\s+de\s+evid[êe]ncia\b",
    r"\bliminar\b", r"\bconsigna[çc][ãa]o\s+em\s+pagamento\b",
    # Prescricao / decadencia
    r"\bprescri[çc][ãa]o\b", r"\bdecad[êe]ncia\b",
    # Codigos
    r"\bc[óo]digo\s+civil\b", r"\bCC\b", r"\bc[óo]digo\s+de\s+processo\s+civil\b", r"\bCPC\b",
    # Sujeitos
    r"\bautor\b", r"\br[ée]u\b", r"\bcredor\b", r"\bdevedor\b",
    r"\bcontesta[çc][ãa]o\b", r"\bjuros\s+de\s+mora\b", r"\bcorre[çc][ãa]o\s+monet[áa]ria\b",
]

# Gatilho 3: commands prefixados do plugin
PLUGIN_COMMANDS = [
    "/start-civel",
    "/civel-master",
    "/triagem",
    "/caso-civel",
    "/responsabilidade-civil",
    "/contrato",
    "/cobranca",
    "/monitoria",
    "/execucao-titulo",
    "/busca-apreensao",
    "/tutela-urgencia",
    "/consignacao",
    "/parecer-civel",
]

# Keywords gerais (fallback — protocolo cauteloso quando casa generico)
CONSUM_KEYWORDS_GENERAL = [
    r"\bcivil\b", r"\bcontrato\b", r"\bindeniza[çc][ãa]o\b", r"\bdano\b",
    r"\bcobran[çc]a\b", r"\bd[íi]vida\b", r"\bd[ée]bito\b",
    r"\bautor\b", r"\br[ée]u\b", r"\bcredor\b", r"\bdevedor\b",
    r"\bobriga[çc][ãa]o\b", r"\bprescri[çc][ãa]o\b", r"\bprocesso\s+civil\b",
]

BYPASS_TOKENS = [
    "--no-revisao",
    "--no-r1r4",
    "--quick",
    "/revisao off",
    "/revisao-off",
]


def _load_input() -> dict:
    raw = sys.stdin.read().strip()
    if not raw:
        return {}
    try:
        return json.loads(raw)
    except Exception:
        return {}


def _matches_any(text: str, patterns: list[str]) -> bool:
    for pat in patterns:
        if re.search(pat, text, re.IGNORECASE):
            return True
    return False


def _is_medico(prompt: str) -> bool:
    """Detecta se o prompt e do dominio (gatilhos 1, 2 ou 3)."""
    if _matches_any(prompt, TRIGGER_MEDICO):
        return True
    if _matches_any(prompt, DOMAIN_KEYWORDS):
        return True
    low = prompt.lower()
    for cmd in PLUGIN_COMMANDS:
        if cmd.lower() in low:
            return True
    return False


def _is_medico_general(prompt: str) -> bool:
    """Detecta tarefa do dominio em geral (sem keyword forte)."""
    return _matches_any(prompt, CONSUM_KEYWORDS_GENERAL)


def _has_bypass(prompt: str) -> str | None:
    low = prompt.lower()
    for token in BYPASS_TOKENS:
        if token in low:
            return token
    return None


def _has_medico_state(cowork: Path | None) -> bool:
    """Verifica se existe `civel/cowork-state.json` no path."""
    if cowork is None:
        return False
    return (cowork / "civel" / "cowork-state.json").exists()


def _revisao_tecnica_enabled(cowork: Path | None) -> bool:
    """Le state.json e verifica revisao_tecnica.enabled. Default true se ausente."""
    if cowork is None:
        return True
    sf = cowork / "civel" / "cowork-state.json"
    if not sf.exists():
        return True
    try:
        state = json.loads(sf.read_text(encoding="utf-8"))
        return bool(state.get("revisao_tecnica", {}).get("enabled", True))
    except Exception:
        return True


def _resolve_cowork() -> Path | None:
    """Resolve COWORK root via env CIV_COWORK_PATH ou cwd ancestral."""
    env = os.environ.get("CIV_COWORK_PATH") or os.environ.get("COWORK_PATH")
    if env:
        p = Path(env)
        if (p / "civel" / "cowork-state.json").exists():
            return p
    return hook_utils.find_cowork(Path.cwd())


def main() -> int:
    payload = _load_input()
    prompt = payload.get("prompt") or payload.get("user_prompt") or ""
    if not isinstance(prompt, str) or not prompt.strip():
        return 0

    cowork = _resolve_cowork()
    bypass = _has_bypass(prompt)

    is_medico = _is_medico(prompt)
    is_medico_other = _is_medico_general(prompt) and not is_medico

    # Caso 1: bypass explicito
    if bypass and (is_medico or is_medico_other):
        sys.stdout.write(
            f"[civel-adv-os] Bypass detectado ({bypass}). "
            "Pecas, pareceres e estrategias serao entregues SEM a "
            "Revisao Tecnica R1-R4. Use por sua conta e risco.\n"
        )
        return 0

    # Caso 2: tarefa do dominio + plugin configurado
    if is_medico and _has_medico_state(cowork):
        if not _revisao_tecnica_enabled(cowork):
            sys.stdout.write(
                "[civel-adv-os] Demanda civel/processual civel detectada. "
                "Revisao Tecnica DESATIVADA na configuracao. Aciono apenas a cadeia de skills.\n"
                "Acionar skill: civel-master.\n"
            )
        else:
            sys.stdout.write(
                "[civel-adv-os] Demanda civel/processual civel detectada. Plugin ativado.\n"
                "\n"
                "PROTOCOLO AUTOMATICO:\n"
                "1. Acionar skill `civel-master` (Tier 0 - sempre ativa)\n"
                "2. Aplicar Hierarquia das 4 Camadas (1-Proibicoes, 2-Protocolos, 3-Estilo, 4-Skills)\n"
                "3. Verificar as Proibicoes Absolutas, com atencao especial:\n"
                "   - P1: Selo de Validacao Legal Previa (validar CC/CPC vigentes + sumulas STF/STJ\n"
                "        confirmadas) antes de qualquer producao; conferir a norma vigente ao\n"
                "        fato/contrato (CC/2002 x institutos anteriores)\n"
                "   - PRESCRICAO x DECADENCIA: distinguir e aplicar os prazos certos (CC 205 - geral\n"
                "     10 anos; CC 206 - especiais; termo inicial)\n"
                "   - LIQUIDACAO DO DANO E JUROS: dano emergente x lucro cessante; juros de mora\n"
                "     (termo inicial - Sum. 54 STJ responsabilidade extracontratual desde o evento;\n"
                "     Sum. 362 STJ dano moral desde o arbitramento); correcao monetaria; nao inventar indices\n"
                "   - RESPONSABILIDADE CONTRATUAL x EXTRACONTRATUAL: nao confundir os regimes\n"
                "     (culpa, onus da prova, prazos)\n"
                "   - Coerencia de polo: autor (credor/lesado/demandante) x reu (devedor/causador do\n"
                "     dano/demandado) - nunca redigir contra o cliente\n"
                "   - INTERFACES: consumo / familia / imovel / penal / fiscal / trabalho / INSS NAO se\n"
                "     redige aqui - rotear ao plugin respectivo\n"
                "4. Acionar os Protocolos da Camada 2 conforme demanda\n"
                "   (P1 Selo de Validacao Legal Previa, P2 Integridade Documental,\n"
                "    P3 Memoria de Caso, P4 Cruzamento Relacao Juridica-Pretensao-Execucao,\n"
                "    P5 Localizacao/Rito/Foro/Competencia, P6 Revisao R1-R4)\n"
                "5. Antes de entregar: Revisao Tecnica R1->R2->R3->R4 (skill `revisao-final-civel`)\n"
                "\n"
                "Bypass disponivel: `--no-revisao`, `--quick`, `/revisao off`.\n"
            )
        return 0

    # Caso 3: tarefa do dominio mas plugin NAO configurado
    if is_medico and not _has_medico_state(cowork):
        sys.stdout.write(
            "[civel-adv-os] Detectei demanda civel/processual civel, mas o plugin "
            "ainda nao foi configurado neste diretorio.\n"
            "\n"
            "RECOMENDACAO: rode /start-civel para configurar (~5 min).\n"
            "Vou criar uma pasta `civel/` aqui com a identidade do "
            "advogado/escritorio, OAB, cidade/UF, frentes de atuacao "
            "(responsabilidade civil & indenizatorias / contratos & obrigacoes / "
            "cobranca & execucao / obrigacoes & tutelas), tom de voz e configuracao das skills.\n"
            "\n"
            "Caso queira prosseguir SEM configurar, trabalho em modo fallback generico "
            "(persona neutra, qualidade reduzida). Apenas avise.\n"
        )
        return 0

    # Caso 4: tarefa do dominio geral - protocolo cauteloso
    if is_medico_other:
        sys.stdout.write(
            "[civel-adv-os] Tarefa civel/processual civel detectada (sem frente especifica). "
            "Aplique protocolo padrao:\n"
            "1. Questionamento previo (sem suposicoes silenciosas - exigir dado real do caso:\n"
            "   relacao juridica/fato, frente (responsabilidade civil / contratos / cobranca-execucao /\n"
            "   tutelas), polo, valor/quantum pretendido,\n"
            "   datas - fato/contrato/inadimplemento/citacao).\n"
            "2. Apresentar estrutura + premissas antes de redigir peca/parecer.\n"
            "3. Aguardar confirmacao do advogado-operador.\n"
            "4. Antes de entregar: executar Revisao Tecnica R1-R4 se aplicavel.\n"
            "Bypass: `--no-revisao`, `--quick`, `/revisao off`.\n"
        )
        return 0

    # Caso default: nao e tarefa do dominio - silencio
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
