#!/usr/bin/env python3
"""
Hook UserPromptSubmit do plugin Criminal Adv-OS.

Logica (ativacao automatica por contexto):
1. Le o prompt via stdin (JSON padrao Claude Code hooks).
2. Detecta bypass explicito: flags `--no-revisao`, `--quick`, `--no-r1r4`, `/revisao off`.
3. Detecta GATILHO de DOMINIO via keywords (3 niveis):
   - Gatilho 1: prompt contem palavras do dominio penal/processo penal
   - Gatilho 2: keywords fortes do dominio
   - Gatilho 3: comandos `/start-criminal`, `/criminal-master`, etc.
4. Se gatilho dispara:
   - Verifica se `criminal/cowork-state.json` existe no path atual
   - SIM: injeta protocolo Revisao Tecnica R1-R4 + aponta para skill `criminal-master`
   - NAO: sugere `/start-criminal` ao usuario (mas nao bloqueia)
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
# dominio — aqui carregam o lexico do DIREITO PENAL E PROCESSO PENAL. Mantidos
# para preservar a logica do hook.

# Gatilho 1: frases fortes do dominio penal/processo penal (case insensitive)
TRIGGER_MEDICO = [
    r"\bdireito\s+penal\b", r"\bprocesso\s+penal\b",
    r"\binqu[ée]rito\s+policial\b", r"\ba[çc][ãa]o\s+penal\b",
    r"\bpris[ãa]o\s+em\s+flagrante\b", r"\bpris[ãa]o\s+preventiva\b",
    r"\bpris[ãa]o\s+tempor[áa]ria\b", r"\brelaxamento\s+de\s+pris[ãa]o\b",
    r"\bliberdade\s+provis[óo]ria\b", r"\baudi[êe]ncia\s+de\s+cust[óo]dia\b",
    r"\bden[úu]ncia\b", r"\bqueixa-?crime\b",
    r"\bresposta\s+[àa]\s+acusa[çc][ãa]o\b", r"\balega[çc][õo]es\s+finais\b",
    r"\babsolvi[çc][ãa]o\s+sum[áa]ria\b", r"\bsenten[çc]a\s+penal\b",
    r"\btribunal\s+do\s+j[úu]ri\b", r"\bdosimetria\b",
    r"\bhabeas\s+corpus\b", r"\bexecu[çc][ãa]o\s+penal\b",
    r"\bprogress[ãa]o\s+de\s+regime\b", r"\blivramento\s+condicional\b",
    r"\bANPP\b", r"\bacordo\s+de\s+n[ãa]o\s+persecu[çc][ãa]o\b",
    r"\blei\s+de\s+drogas\b", r"\blei\s+11\.?343\b",
    r"\bmaria\s+da\s+penha\b", r"\blei\s+11\.?340\b",
]

# Gatilho 2: keywords fortes do dominio penal/processo penal
DOMAIN_KEYWORDS = [
    # Investigacao / inquerito / prisao cautelar
    r"\bcrime\b", r"\bdelito\b", r"\bpenal\b", r"\binqu[ée]rito\b",
    r"\binvestiga[çc][ãa]o\b", r"\bflagrante\b", r"\bauto\s+de\s+pris[ãa]o\s+em\s+flagrante\b",
    r"\bpris[ãa]o\s+preventiva\b", r"\bpris[ãa]o\s+tempor[áa]ria\b",
    r"\brelaxamento\s+de\s+pris[ãa]o\b", r"\bliberdade\s+provis[óo]ria\b",
    r"\baudi[êe]ncia\s+de\s+cust[óo]dia\b", r"\bfian[çc]a\b",
    r"\bmedidas\s+cautelares\b",
    # Acao penal
    r"\bden[úu]ncia\b", r"\bqueixa-?crime\b", r"\ba[çc][ãa]o\s+penal\b",
    r"\bresposta\s+[àa]\s+acusa[çc][ãa]o\b", r"\binstru[çc][ãa]o\s+criminal\b",
    r"\balega[çc][õo]es\s+finais\b", r"\bmemoriais\b",
    r"\babsolvi[çc][ãa]o\b", r"\bcondena[çc][ãa]o\b", r"\bsenten[çc]a\s+penal\b",
    # Tribunal do Juri
    r"\btribunal\s+do\s+j[úu]ri\b", r"\bpron[úu]ncia\b", r"\bimpron[úu]ncia\b",
    r"\bdesclassifica[çc][ãa]o\b", r"\bplen[áa]rio\b", r"\bquesitos\b",
    # Dosimetria / pena / prescricao
    r"\bdosimetria\b", r"\bpena\b", r"\bregime\s+(?:fechado|semiaberto|aberto)\b",
    r"\bprescri[çc][ãa]o\b", r"\bdecad[êe]ncia\b", r"\bdetra[çc][ãa]o\b",
    # Recursos
    r"\brecurso\b", r"\bapela[çc][ãa]o\b", r"\brecurso\s+em\s+sentido\s+estrito\b",
    r"\bRESE\b", r"\bembargos\b", r"\bhabeas\s+corpus\b", r"\bHC\b", r"\bRHC\b",
    r"\brevis[ãa]o\s+criminal\b",
    # Execucao penal (LEP)
    r"\bexecu[çc][ãa]o\s+penal\b", r"\bLEP\b", r"\bprogress[ãa]o\s+de\s+regime\b",
    r"\blivramento\s+condicional\b", r"\bremi[çc][ãa]o\b", r"\bfalta\s+grave\b",
    r"\bsa[íi]da\s+tempor[áa]ria\b",
    # Acordos despenalizadores
    r"\bANPP\b", r"\bacordo\s+de\s+n[ãa]o\s+persecu[çc][ãa]o\b",
    r"\btransa[çc][ãa]o\s+penal\b", r"\bsuspens[ãa]o\s+condicional\s+do\s+processo\b",
    r"\bsursis\b", r"\blei\s+9\.?099\b", r"\bJECrim\b",
    # Leis especiais
    r"\blei\s+de\s+drogas\b", r"\blei\s+11\.?343\b",
    r"\bmaria\s+da\s+penha\b", r"\blei\s+11\.?340\b", r"\bviol[êe]ncia\s+dom[ée]stica\b",
    # Codigos
    r"\bc[óo]digo\s+penal\b", r"\bCP\b", r"\bc[óo]digo\s+de\s+processo\s+penal\b", r"\bCPP\b",
    # Sujeitos
    r"\br[ée]u\b", r"\bacusado\b", r"\binvestigado\b", r"\bsentenciado\b",
    r"\bv[íi]tima\b", r"\bofendido\b", r"\bassistente\s+de\s+acusa[çc][ãa]o\b",
    r"\bminist[ée]rio\s+p[úu]blico\b", r"\bantecedentes\b", r"\breincid[êe]ncia\b",
]

# Gatilho 3: commands prefixados do plugin
PLUGIN_COMMANDS = [
    "/start-criminal",
    "/criminal-master",
    "/triagem",
    "/caso-criminal",
    "/flagrante",
    "/relaxamento",
    "/liberdade-provisoria",
    "/resposta-acusacao",
    "/memoriais",
    "/habeas-corpus",
    "/dosimetria",
    "/execucao-penal",
    "/anpp",
]

# Keywords gerais (fallback — protocolo cauteloso quando casa generico)
CONSUM_KEYWORDS_GENERAL = [
    r"\bcrime\b", r"\bdelito\b", r"\bpenal\b", r"\bpris[ãa]o\b",
    r"\br[ée]u\b", r"\bacusado\b", r"\binvestigado\b", r"\bv[íi]tima\b",
    r"\bpena\b", r"\bdefesa\s+criminal\b", r"\bdelegacia\b", r"\bdepoimento\b",
    r"\bdenuncia\b", r"\bprocesso\s+criminal\b",
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
    """Verifica se existe `criminal/cowork-state.json` no path."""
    if cowork is None:
        return False
    return (cowork / "criminal" / "cowork-state.json").exists()


def _revisao_tecnica_enabled(cowork: Path | None) -> bool:
    """Le state.json e verifica revisao_tecnica.enabled. Default true se ausente."""
    if cowork is None:
        return True
    sf = cowork / "criminal" / "cowork-state.json"
    if not sf.exists():
        return True
    try:
        state = json.loads(sf.read_text(encoding="utf-8"))
        return bool(state.get("revisao_tecnica", {}).get("enabled", True))
    except Exception:
        return True


def _resolve_cowork() -> Path | None:
    """Resolve COWORK root via env CRIM_COWORK_PATH ou cwd ancestral."""
    env = os.environ.get("CRIM_COWORK_PATH") or os.environ.get("COWORK_PATH")
    if env:
        p = Path(env)
        if (p / "criminal" / "cowork-state.json").exists():
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
            f"[criminal-adv-os] Bypass detectado ({bypass}). "
            "Pecas, pareceres e estrategias serao entregues SEM a "
            "Revisao Tecnica R1-R4. Use por sua conta e risco.\n"
        )
        return 0

    # Caso 2: tarefa do dominio + plugin configurado
    if is_medico and _has_medico_state(cowork):
        if not _revisao_tecnica_enabled(cowork):
            sys.stdout.write(
                "[criminal-adv-os] Demanda penal/processual penal detectada. "
                "Revisao Tecnica DESATIVADA na configuracao. Aciono apenas a cadeia de skills.\n"
                "Acionar skill: criminal-master.\n"
            )
        else:
            sys.stdout.write(
                "[criminal-adv-os] Demanda penal/processual penal detectada. Plugin ativado.\n"
                "\n"
                "PROTOCOLO AUTOMATICO:\n"
                "1. Acionar skill `criminal-master` (Tier 0 - sempre ativa)\n"
                "2. Aplicar Hierarquia das 4 Camadas (1-Proibicoes, 2-Protocolos, 3-Estilo, 4-Skills)\n"
                "3. Verificar as Proibicoes Absolutas, com atencao especial:\n"
                "   - P1: Selo de Validacao Legal Previa (validar CP/CPP/LEP/leis especiais vigentes\n"
                "        + sumulas STF/STJ e vinculantes confirmadas) antes de qualquer producao\n"
                "   - LEI PENAL NO TEMPO: aplicar a lei vigente ao FATO, salvo lei posterior mais\n"
                "     benefica, que retroage (CF 5 XL; CP 2) - irretroatividade da lei mais gravosa\n"
                "   - Coerencia de polo: defesa (investigado/reu/sentenciado) x assistencia de\n"
                "     acusacao (vitima/ofendido) - nunca redigir contra o cliente\n"
                "   - PRESCRICAO PENAL: distinguir pretensao punitiva x executoria; calcular pela\n"
                "     pena (abstrato/concreto) - CP 109/110\n"
                "   - DOSIMETRIA: metodo trifasico do art. 68 CP (circunstancias judiciais art. 59\n"
                "     -> agravantes/atenuantes -> causas de aumento/diminuicao); nao inventar fracoes\n"
                "   - ETICO-PENAL: a defesa e tecnica e ampla, mas NUNCA orientar a pratica de crime,\n"
                "     destruicao/ocultacao de prova, fuga ou coacao de testemunha; sigilo reforcado\n"
                "4. Acionar os Protocolos da Camada 2 conforme demanda\n"
                "   (P1 Selo de Validacao Legal Previa, P2 Integridade Documental,\n"
                "    P3 Memoria de Caso, P4 Cruzamento Investigacao-Acao Penal-Execucao,\n"
                "    P5 Localizacao/Rito/Foro/Competencia, P6 Revisao R1-R4)\n"
                "5. Antes de entregar: Revisao Tecnica R1->R2->R3->R4 (skill `revisao-final-criminal`)\n"
                "\n"
                "Bypass disponivel: `--no-revisao`, `--quick`, `/revisao off`.\n"
            )
        return 0

    # Caso 3: tarefa do dominio mas plugin NAO configurado
    if is_medico and not _has_medico_state(cowork):
        sys.stdout.write(
            "[criminal-adv-os] Detectei demanda penal/processual penal, mas o plugin "
            "ainda nao foi configurado neste diretorio.\n"
            "\n"
            "RECOMENDACAO: rode /start-criminal para configurar (~5 min).\n"
            "Vou criar uma pasta `criminal/` aqui com a identidade do "
            "advogado/escritorio, OAB, cidade/UF, frentes de atuacao "
            "(investigacao/inquerito / acao penal / Tribunal do Juri / recursos / execucao penal / "
            "acordos despenalizadores), tom de voz e configuracao das skills.\n"
            "\n"
            "Caso queira prosseguir SEM configurar, trabalho em modo fallback generico "
            "(persona neutra, qualidade reduzida). Apenas avise.\n"
        )
        return 0

    # Caso 4: tarefa do dominio geral - protocolo cauteloso
    if is_medico_other:
        sys.stdout.write(
            "[criminal-adv-os] Tarefa penal/processual penal detectada (sem frente especifica). "
            "Aplique protocolo padrao:\n"
            "1. Questionamento previo (sem suposicoes silenciosas - exigir dado real do caso:\n"
            "   crime/tipificacao, fase (inquerito/acao penal/execucao), polo, situacao prisional,\n"
            "   datas - fato/flagrante/denuncia/sentenca).\n"
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
