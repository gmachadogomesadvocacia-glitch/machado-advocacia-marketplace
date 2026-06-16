#!/usr/bin/env python3
"""
Hook UserPromptSubmit do plugin Previdenciario Adv-OS.

Logica (ativacao automatica por contexto):
1. Le o prompt via stdin (JSON padrao Claude Code hooks).
2. Detecta bypass explicito: flags `--no-revisao`, `--quick`, `--no-r1r4`, `/revisao off`.
3. Detecta GATILHO de DOMINIO via keywords (3 niveis):
   - Gatilho 1: prompt contem palavras do dominio previdenciario
   - Gatilho 2: keywords fortes do dominio
   - Gatilho 3: comandos `/start-previdenciario`, `/previdenciario-master`, etc.
4. Se gatilho dispara:
   - Verifica se `previdenciario/cowork-state.json` existe no path atual
   - SIM: injeta protocolo Revisao Tecnica R1-R4 + aponta para skill `previdenciario-master`
   - NAO: sugere `/start-previdenciario` ao usuario (mas nao bloqueia)
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


# NOTA: os nomes TRIGGER_MEDICO / DOMAIN_KEYWORDS / _is_medico sao internos
# (herdados do engine portado) e nao tem efeito de dominio — aqui carregam o
# lexico do DIREITO PREVIDENCIARIO. Mantidos para preservar a logica do hook.

# Gatilho 1: frases fortes do dominio previdenciario (case insensitive)
TRIGGER_MEDICO = [
    r"\bdireito\s+previdenci[áa]rio\b",
    r"\bprevid[êe]ncia\s+social\b",
    r"\bINSS\b", r"\bRGPS\b", r"\bRPPS\b",
    r"\baposentadoria\s+por\s+idade\b",
    r"\baposentadoria\s+por\s+tempo\s+de\s+contribui[çc][ãa]o\b",
    r"\baposentadoria\s+especial\b",
    r"\baposentadoria\s+por\s+invalidez\b", r"\baposentadoria\s+por\s+incapacidade\b",
    r"\baux[íi]lio-?doen[çc]a\b", r"\bincapacidade\s+tempor[áa]ria\b",
    r"\baux[íi]lio-?acidente\b",
    r"\bBPC\b", r"\bLOAS\b",
    r"\bpens[ãa]o\s+por\s+morte\b",
    r"\bsal[áa]rio-?maternidade\b",
    r"\bbeneficio\s+previdenci[áa]rio\b", r"\bbenef[íi]cio\s+previdenci[áa]rio\b",
    r"\brevis[ãa]o\s+da\s+vida\s+toda\b",
    r"\bEC\s*103\b", r"\bEmenda\s+Constitucional\s+103\b",
]

# Gatilho 2: keywords fortes das frentes previdenciarias
DOMAIN_KEYWORDS = [
    # Cadastro contributivo / base de calculo
    r"\bCNIS\b", r"\bcar[êe]ncia\b", r"\bqualidade\s+de\s+segurado\b",
    r"\bsal[áa]rio\s+de\s+benef[íi]cio\b", r"\bsal[áa]rio\s+de\s+contribui[çc][ãa]o\b",
    r"\btempo\s+de\s+contribui[çc][ãa]o\b", r"\bPBC\b", r"\bNIT\b", r"\bPIS\b",
    r"\bfator\s+previdenci[áa]rio\b", r"\bperiodo\s+b[áa]sico\s+de\s+c[áa]lculo\b",
    r"\bcontribuinte\s+individual\b", r"\bsegurado\s+facultativo\b",
    r"\bsegurado\s+especial\b", r"\btrabalhador\s+rural\b", r"\bMEI\b",
    # Datas e siglas de beneficio
    r"\bDER\b", r"\bDIB\b", r"\bDCB\b", r"\bDIP\b",
    r"\bRMI\b", r"\bRMA\b", r"\bNB\b", r"\bn[úu]mero\s+do\s+benef[íi]cio\b",
    r"\bB31\b", r"\bB32\b", r"\bB41\b", r"\bB42\b", r"\bB91\b", r"\bB94\b", r"\bB87\b",
    r"\bcarta\s+de\s+concess[ãa]o\b", r"\bcarta\s+de\s+indeferimento\b",
    r"\bindeferimento\s+administrativo\b",
    # Aposentadoria especial / agentes nocivos
    r"\bPPP\b", r"\bLTCAT\b", r"\bagente\s+nocivo\b", r"\bru[íi]do\b",
    r"\binsalubridade\b", r"\baposentadoria\s+por\s+exposi[çc][ãa]o\b",
    r"\bEPI\s+eficaz\b", r"\bTema\s+555\b", r"\bTema\s+709\b",
    # Acidentario / incapacidade
    r"\bNTEP\b", r"\bFAP\b", r"\bCAT\b", r"\bRAT\b",
    r"\bnexo\s+t[ée]cnico\s+epidemiol[óo]gico\b", r"\bdoen[çc]a\s+ocupacional\b",
    r"\bacidente\s+de\s+trabalho\b", r"\bauxilio-?acidente\b",
    r"\bperic[íi]a\s+m[ée]dica\b", r"\bper[íi]cia\s+previdenci[áa]ria\b",
    r"\bjunta\s+m[ée]dica\b",
    # Esfera administrativa / recursal
    r"\bCRPS\b", r"\bconselho\s+de\s+recursos\b", r"\bjunta\s+de\s+recursos\b",
    r"\bC[âa]mara\s+de\s+Julgamento\b", r"\brecurso\s+administrativo\b",
    r"\bMeu\s+INSS\b", r"\brequerimento\s+administrativo\b",
    # Esfera judicial / competencia
    r"\bJEF\b", r"\bjuizado\s+especial\s+federal\b", r"\bTNU\b",
    r"\bTurma\s+Nacional\s+de\s+Uniformiza[çc][ãa]o\b",
    r"\bjusti[çc]a\s+federal\b", r"\bvara\s+previdenci[áa]ria\b",
    # Calculo / revisao
    r"\brevis[ãa]o\s+de\s+benef[íi]cio\b", r"\brevisional\s+de\s+RMI\b",
    r"\bTema\s+1102\b", r"\bTema\s+999\b", r"\bbur[íi]cio\b",
    r"\bdesaposenta[çc][ãa]o\b", r"\bteto\s+previdenci[áa]rio\b",
    r"\batrasados\b", r"\bparcelas\s+vencidas\b",
    # RPPS / servidor publico
    r"\bservidor\s+p[úu]blico\b", r"\baposentadoria\s+estatut[áa]ria\b",
    r"\bpens[ãa]o\s+estatut[áa]ria\b", r"\babono\s+de\s+perman[êe]ncia\b",
    r"\bregra\s+de\s+transi[çc][ãa]o\b", r"\bped[áa]gio\b", r"\bparidade\b",
    # Previdencia complementar
    r"\bprevid[êe]ncia\s+complementar\b", r"\bPGBL\b", r"\bVGBL\b",
    r"\bfundo\s+de\s+pens[ãa]o\b", r"\bentidade\s+fechada\b",
    # Planejamento / consultivo PJ
    r"\bplanejamento\s+previdenci[áa]rio\b", r"\bcontribui[çc][ãa]o\s+previdenci[áa]ria\b",
    r"\bpro\s*labore\b", r"\bcontribui[çc][ãa]o\s+patronal\b",
    # Acumulacao / dependentes
    r"\bacumula[çc][ãa]o\s+de\s+benef[íi]cios\b", r"\bdependente\b",
    r"\buni[ãa]o\s+est[áa]vel\b", r"\bdepend[êe]ncia\s+econ[ôo]mica\b",
    # Legislacao / sumulas / temas chave
    r"\bLei\s+8\.213\b", r"\bLei\s+8\.212\b", r"\bLei\s+8\.742\b",
    r"\bDecreto\s+3\.048\b", r"\bart\.?\s*103\b",
    r"\bS[úu]mula\s+\d+\s+TNU\b", r"\bdecad[êe]ncia\s+decenal\b",
    r"\bprescri[çc][ãa]o\s+quinquenal\b",
]

# Gatilho 3: commands prefixados do plugin
PLUGIN_COMMANDS = [
    "/start-previdenciario",
    "/previdenciario-master",
    "/triagem",
    "/caso-previdenciario",
    "/status-previdenciario",
    "/suprema-corte-previdenciaria",
    "/jurisprudencia-estrategica",
    "/calculos-previdenciarios",
    "/triagem-dogmatica",
    "/analise-cnis",
    "/recursos-previdenciarios",
    "/peticao-inicial-prev",
    "/administrativo-inss-crps",
]

# Keywords gerais (fallback — protocolo cauteloso quando casa generico)
CONSUM_KEYWORDS_GENERAL = [
    r"\bsegurado\b", r"\bbenef[íi]cio\b", r"\baposentadoria\b",
    r"\bpens[ãa]o\b", r"\bcontribui[çc][ãa]o\b", r"\bprevid[êe]ncia\b",
    r"\bINSS\b", r"\bsal[áa]rio\b", r"\bper[íi]cia\b",
    r"\bafastamento\b", r"\bincapacidade\b", r"\brequerimento\b",
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
    """Verifica se existe `previdenciario/cowork-state.json` no path."""
    if cowork is None:
        return False
    return (cowork / "previdenciario" / "cowork-state.json").exists()


def _revisao_tecnica_enabled(cowork: Path | None) -> bool:
    """Le state.json e verifica revisao_tecnica.enabled. Default true se ausente."""
    if cowork is None:
        return True
    sf = cowork / "previdenciario" / "cowork-state.json"
    if not sf.exists():
        return True
    try:
        state = json.loads(sf.read_text(encoding="utf-8"))
        return bool(state.get("revisao_tecnica", {}).get("enabled", True))
    except Exception:
        return True


def _resolve_cowork() -> Path | None:
    """Resolve COWORK root via env PREV_COWORK_PATH ou cwd ancestral."""
    env = os.environ.get("PREV_COWORK_PATH") or os.environ.get("COWORK_PATH")
    if env:
        p = Path(env)
        if (p / "previdenciario" / "cowork-state.json").exists():
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
            f"[previdenciario-adv-os] Bypass detectado ({bypass}). "
            "Pecas, pareceres e estrategias serao entregues SEM a "
            "Revisao Tecnica R1-R4. Use por sua conta e risco.\n"
        )
        return 0

    # Caso 2: tarefa do dominio + plugin configurado
    if is_medico and _has_medico_state(cowork):
        if not _revisao_tecnica_enabled(cowork):
            sys.stdout.write(
                "[previdenciario-adv-os] Demanda juridico-previdenciaria detectada. "
                "Revisao Tecnica DESATIVADA na configuracao. Aciono apenas a cadeia de skills.\n"
                "Acionar skill: previdenciario-master.\n"
            )
        else:
            sys.stdout.write(
                "[previdenciario-adv-os] Demanda juridico-previdenciaria detectada. Plugin ativado.\n"
                "\n"
                "PROTOCOLO AUTOMATICO:\n"
                "1. Acionar skill `previdenciario-master` (Tier 0 - sempre ativa)\n"
                "2. Aplicar Hierarquia das 4 Camadas (1-Proibicoes, 2-Protocolos, 3-Estilo/FIRAC, 4-Skills)\n"
                "3. Verificar as Proibicoes Absolutas, com atencao especial:\n"
                "   - Validacao de vigencia da norma (EC 103 + marco temporal) antes de qualquer producao\n"
                "   - Nunca aplicar a EC 103/2019 retroativamente: conferir filiacao e regra de transicao na DER\n"
                "   - Nunca confundir RGPS com RPPS (regimes distintos)\n"
                "   - Nunca omitir decadencia decenal (art. 103 Lei 8.213) em pedido de revisao\n"
                "   - Coerencia de tese e de polo (segurado/dependente x INSS) - nunca redigir contra o cliente\n"
                "   - Dados sensiveis do segurado NUNCA no plugin (sigilo OAB + LGPD art. 11; pasta caso local)\n"
                "4. Acionar os Protocolos da Camada 2 conforme demanda\n"
                "   (Triagem Trilateral, Validacao de norma vigente, Localizacao/Foro,\n"
                "    Memoria de Calculo, Suprema Corte R1-R4)\n"
                "5. Antes de entregar: Revisao Tecnica R1->R2->R3->R4 (skill `suprema-corte-previdenciaria`)\n"
                "\n"
                "Bypass disponivel: `--no-revisao`, `--quick`, `/revisao off`.\n"
            )
        return 0

    # Caso 3: tarefa do dominio mas plugin NAO configurado
    if is_medico and not _has_medico_state(cowork):
        sys.stdout.write(
            "[previdenciario-adv-os] Detectei demanda juridico-previdenciaria, mas o plugin "
            "ainda nao foi configurado neste diretorio.\n"
            "\n"
            "RECOMENDACAO: rode /start-previdenciario para configurar (~5 min).\n"
            "Vou criar uma pasta `previdenciario/` aqui com a identidade do "
            "advogado/escritorio, OAB, cidade/UF, area de foco (RGPS / RPPS / "
            "complementar / consultivo), tom de voz e configuracao das skills.\n"
            "\n"
            "Caso queira prosseguir SEM configurar, trabalho em modo fallback generico "
            "(persona neutra, qualidade reduzida). Apenas avise.\n"
        )
        return 0

    # Caso 4: tarefa do dominio geral - protocolo cauteloso
    if is_medico_other:
        sys.stdout.write(
            "[previdenciario-adv-os] Tarefa juridico-previdenciaria detectada (sem frente especifica). "
            "Aplique protocolo padrao:\n"
            "1. Questionamento previo (sem suposicoes silenciosas - exigir dado real do caso: "
            "regime, especie/NB, DER, CNIS).\n"
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
