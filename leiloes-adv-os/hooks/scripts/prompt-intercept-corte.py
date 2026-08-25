#!/usr/bin/env python3
"""
Hook UserPromptSubmit do plugin Leiloes Adv-OS.

Logica (ativacao automatica por contexto):
1. Le o prompt via stdin (JSON padrao Claude Code hooks).
2. Detecta bypass explicito: flags `--no-revisao`, `--quick`, `--no-r1r4`, `/revisao off`.
3. Detecta GATILHO de DOMINIO via keywords (3 niveis):
   - Gatilho 1: prompt contem palavras do dominio de leiloes
   - Gatilho 2: keywords fortes do dominio
   - Gatilho 3: comandos `/start-leiloes`, `/leiloes-master`, etc.
4. Se gatilho dispara:
   - Verifica se `leiloes/cowork-state.json` existe no path atual
   - SIM: injeta protocolo Revisao Tecnica R1-R4 + aponta para skill `leiloes-master`
   - NAO: sugere `/start-leiloes` ao usuario (mas nao bloqueia)
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
# dominio — aqui carregam o lexico do DIREITO DOS LEILOES E DA ARREMATACAO. Mantidos para
# preservar a logica do hook.

# Gatilho 1: frases fortes do dominio de leiloes (case insensitive)
TRIGGER_MEDICO = [
    r"\bleil[ãa]o\s+judicial\b", r"\bleil[ãa]o\s+extrajudicial\b",
    r"\bhasta\s+p[úu]blica\b", r"\bedital\s+de\s+leil[ãa]o\b",
    r"\barremata[çc][ãa]o\b", r"\barrematante\b", r"\barrematar\b",
    r"\barrematei\b", r"\barrematou\b",
    r"\bcarta\s+de\s+arremata[çc][ãa]o\b", r"\bauto\s+de\s+arremata[çc][ãa]o\b",
    r"\bimiss[ãa]o\s+na\s+posse\b", r"\bpre[çc]o\s+vil\b",
    r"\bcomiss[ãa]o\s+do\s+leiloeiro\b", r"\bleiloeiro\b",
    r"\bconsolida[çc][ãa]o\s+da\s+propriedade\b",
    r"\bsegundo\s+leil[ãa]o\b", r"\bprimeiro\s+leil[ãa]o\b",
    r"\bLei\s*9\.?514\b", r"\bLei\s*14\.?711\b",
    r"\btema\s*1\.?134\b", r"\btema\s*1\.?288\b",
]

# Gatilho 2: keywords fortes do dominio de leiloes
DOMAIN_KEYWORDS = [
    # Leilao e arrematacao
    r"\bleil[ãa]o\b", r"\bleil[õo]es\b", r"\bhasta\s+p[úu]blica\b",
    r"\barremata[çc][ãa]o\b", r"\barrematante\b", r"\barrematar\b",
    r"\blance\b", r"\blote\b", r"\bedital\b", r"\bleiloeiro\b",
    # Documentos do ato
    r"\bauto\s+de\s+arremata[çc][ãa]o\b", r"\bcarta\s+de\s+arremata[çc][ãa]o\b",
    r"\blaudo\s+de\s+avalia[çc][ãa]o\b", r"\bmatr[íi]cula\b",
    r"\bcertid[ãa]o\s+de\s+[õo]nus\b",
    # Institutos
    r"\bpre[çc]o\s+vil\b", r"\badjudica[çc][ãa]o\b", r"\bremi[çc][ãa]o\b",
    r"\bexpropria[çc][ãa]o\b", r"\bpenhora\b",
    r"\bimiss[ãa]o\s+na\s+posse\b", r"\bdesocupa[çc][ãa]o\b",
    r"\bevic[çc][ãa]o\b", r"\bpropter\s+rem\b", r"\bsub-?roga[çc][ãa]o\b",
    # Via fiduciaria
    r"\baliena[çc][ãa]o\s+fiduci[áa]ria\b", r"\bfiduciante\b",
    r"\bfiduci[áa]rio\b", r"\bconsolida[çc][ãa]o\s+da\s+propriedade\b",
    r"\bpurga[çc][ãa]o\s+da\s+mora\b", r"\bLei\s*9\.?514\b",
    r"\bLei\s*14\.?711\b",
    # Ritos
    r"\bLei\s*6\.?830\b", r"\bexecu[çc][ãa]o\s+fiscal\b",
    r"\bCLT\s*888\b", r"\bResolu[çc][ãa]o\s+CNJ\s*236\b",
    # Onus e debitos
    r"\bIPTU\b", r"\bITBI\b", r"\bcota\s+condominial\b",
    r"\bd[íi]vida\s+condominial\b", r"\bhipoteca\b", r"\b[õo]nus\s+real\b",
    r"\bgravame\b",
    # Teses
    r"\btema\s*1\.?134\b", r"\btema\s*1\.?288\b", r"\btema\s*886\b",
]

# Gatilho 3: commands prefixados do plugin
PLUGIN_COMMANDS = [
    "/start-leiloes",
    "/status-leiloes",
    "/leiloes-master",
    "/triagem",
    "/caso-leiloes",
    "/due-diligence",
    "/edital",
    "/imissao",
    "/defesa-arrematacao",
    "/invalidacao",
    "/fiduciario",
    "/desocupacao",
    "/revisao-final",
]

# Keywords gerais (fallback — protocolo cauteloso quando casa generico)
CONSUM_KEYWORDS_GENERAL = [
    r"\bleil[ãa]o\b", r"\barremat", r"\blance\b", r"\bedital\b",
    r"\blote\b", r"\bleiloeiro\b", r"\bhasta\b",
    r"\bimiss[ãa]o\b", r"\bmatr[íi]cula\b", r"\b[õo]nus\b",
    r"\bfiduci", r"\bpenhora\b",
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
    """Verifica se existe `leiloes/cowork-state.json` no path."""
    if cowork is None:
        return False
    return (cowork / "leiloes" / "cowork-state.json").exists()


def _revisao_tecnica_enabled(cowork: Path | None) -> bool:
    """Le state.json e verifica revisao_tecnica.enabled. Default true se ausente."""
    if cowork is None:
        return True
    sf = cowork / "leiloes" / "cowork-state.json"
    if not sf.exists():
        return True
    try:
        state = json.loads(sf.read_text(encoding="utf-8"))
        return bool(state.get("revisao_tecnica", {}).get("enabled", True))
    except Exception:
        return True


def _resolve_cowork() -> Path | None:
    """Resolve COWORK root via env LEIL_COWORK_PATH ou cwd ancestral."""
    env = os.environ.get("LEIL_COWORK_PATH") or os.environ.get("COWORK_PATH")
    if env:
        p = Path(env)
        if (p / "leiloes" / "cowork-state.json").exists():
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
            f"[leiloes-adv-os] Bypass detectado ({bypass}). "
            "Pecas, pareceres e estrategias serao entregues SEM a "
            "Revisao Tecnica R1-R4. Use por sua conta e risco.\n"
        )
        return 0

    # Caso 2: tarefa do dominio + plugin configurado
    if is_medico and _has_medico_state(cowork):
        if not _revisao_tecnica_enabled(cowork):
            sys.stdout.write(
                "[leiloes-adv-os] Demanda de leilao/arrematacao detectada. "
                "Revisao Tecnica DESATIVADA na configuracao. Aciono apenas a cadeia de skills.\n"
                "Acionar skill: leiloes-master.\n"
            )
        else:
            sys.stdout.write(
                "[leiloes-adv-os] Demanda de leilao/arrematacao detectada. Plugin ativado.\n"
                "\n"
                "PROTOCOLO AUTOMATICO:\n"
                "1. Acionar skill `leiloes-master` (Tier 0 - sempre ativa)\n"
                "2. Aplicar Hierarquia das 4 Camadas (1-Proibicoes, 2-Protocolos, 3-Estilo, 4-Skills)\n"
                "3. Verificar as Proibicoes Absolutas, com atencao especial:\n"
                "   - SELO DE VALIDACAO DE NORMA VIGENTE (P1, triagem-leiloes): validar CPC 879-908\n"
                "        ou Lei 9.514/97 na redacao da Lei 14.711/2023, conforme a via, antes de produzir\n"
                "   - POLO (PA-12): o plugin so atua por quem COMPRA (arrematante ou pretendente).\n"
                "        Executado, devedor fiduciante, exequente e credor fiduciario -> ROTEAR\n"
                "   - PA-05: leilao judicial e leilao fiduciario NAO sao o mesmo regime (preco vil e\n"
                "        do CPC; o fiduciario tem referencial proprio no art. 27, § 2º, da Lei 9.514)\n"
                "   - PA-06: nunca afirmar que a arrematacao extingue todo onus. Tributos sub-rogam no\n"
                "        preco (CTN 130, par. unico; Tema 1.134, MODULADO por data do edital), mas\n"
                "        CONDOMINIO e zona cinzenta (CC 1.345 x CPC 908, § 1º; Tema 886 em revisao)\n"
                "   - PRAZO DE 10 DIAS (CPC 903, §§ 2º e 5º): invalidacao, e desistencia do arrematante\n"
                "        por onus nao mencionado no edital (art. 886, VI). Cravar a data-limite SEMPRE\n"
                "   - RITO: CPC, execucao fiscal (LEF 22-23) e trabalhista (CLT 888) tem prazos e\n"
                "        exigencias DIFERENTES (sinal de 20% e pagamento em 24h no trabalhista)\n"
                "   - PA-07: nunca prometer resultado, rentabilidade ou lucro ao investidor\n"
                "   - PA-08/PA-09: nunca orientar autotutela contra ocupante nem afirmar desocupacao\n"
                "        automatica; PA-10: conferir os impedidos de arrematar (CPC 890, inclusive\n"
                "        os ADVOGADOS das partes)\n"
                "   - INTERFACES: executado/exequente -> civel, tributario ou trabalhista; devedor\n"
                "        fiduciante -> imobiliario; UPI e falencia -> recuperacao-judicial\n"
                "4. Acionar os Protocolos da Camada 2 conforme demanda\n"
                "   (P1 Selo de Validacao de Norma Vigente, P2 Integridade Documental - edital/matricula/auto,\n"
                "    P3 Memoria de Caso, P4 Cruzamento Edital-Matricula-Autos,\n"
                "    P5 Via/Rito/Juizo do leilao, P6 Revisao R1-R4)\n"
                "5. Antes de entregar: Revisao Tecnica R1->R2->R3->R4 (skill `revisao-final-leiloes`)\n"
                "\n"
                "Bypass disponivel: `--no-revisao`, `--quick`, `/revisao off`.\n"
            )
        return 0

    # Caso 3: tarefa do dominio mas plugin NAO configurado
    if is_medico and not _has_medico_state(cowork):
        sys.stdout.write(
            "[leiloes-adv-os] Detectei demanda de leilao/arrematacao, mas o plugin "
            "ainda nao foi configurado neste diretorio.\n"
            "\n"
            "RECOMENDACAO: rode /start-leiloes para configurar (~5 min).\n"
            "Vou criar uma pasta `leiloes/` aqui com a identidade do "
            "advogado/escritorio, OAB, cidade/UF, frentes de atuacao "
            "(due diligence pre-lance / imissao na posse / defesa da arrematacao / "
            "invalidacao e eviccao / leilao fiduciario / desocupacao), "
            "tom de voz e configuracao das skills.\n"
            "\n"
            "Caso queira prosseguir SEM configurar, trabalho em modo fallback generico "
            "(persona neutra, qualidade reduzida). Apenas avise.\n"
        )
        return 0

    # Caso 4: tarefa do dominio geral - protocolo cauteloso
    if is_medico_other:
        sys.stdout.write(
            "[leiloes-adv-os] Tarefa de leilao/arrematacao detectada (sem frente especifica). "
            "Aplique protocolo padrao:\n"
            "1. Questionamento previo (sem suposicoes silenciosas - exigir dado real do caso:\n"
            "   dados do auto (AIT, codigo da infracao, data/local, placa/RENAVAM, orgao autuador),\n"
            "   via (judicial / fiduciario), rito, fase, polo\n"
            "   (condutor / proprietario / indicacao do real condutor), fase do processo\n"
            "   administrativo, datas das notificacoes (NA/NP)).\n"
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
