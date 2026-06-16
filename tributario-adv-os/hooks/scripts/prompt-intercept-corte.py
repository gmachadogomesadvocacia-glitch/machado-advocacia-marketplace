#!/usr/bin/env python3
"""
Hook UserPromptSubmit do plugin Tributario Adv-OS.

Logica (ativacao automatica por contexto):
1. Le o prompt via stdin (JSON padrao Claude Code hooks).
2. Detecta bypass explicito: flags `--no-revisao`, `--quick`, `--no-r1r4`, `/revisao off`.
3. Detecta GATILHO de DOMINIO via keywords (3 niveis):
   - Gatilho 1: prompt contem palavras do dominio tributario
   - Gatilho 2: keywords fortes do dominio
   - Gatilho 3: comandos `/start-tributario`, `/tributario-master`, etc.
4. Se gatilho dispara:
   - Verifica se `tributario/cowork-state.json` existe no path atual
   - SIM: injeta protocolo Revisao Tecnica R1-R4 + aponta para skill `tributario-master`
   - NAO: sugere `/start-tributario` ao usuario (mas nao bloqueia)
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
# dominio — aqui carregam o lexico do DIREITO TRIBUTARIO. Mantidos para
# preservar a logica do hook.

# Gatilho 1: frases fortes do dominio tributario (case insensitive)
TRIGGER_MEDICO = [
    r"\bdireito\s+tribut[áa]rio\b",
    r"\bauto\s+de\s+infra[çc][ãa]o\b",
    r"\ban[uú]lat[óo]ria\s+(?:fiscal|tribut[áa]ria)?\b",
    r"\bexecu[çc][ãa]o\s+fiscal\b",
    r"\bembargos\s+[àa]\s+execu[çc][ãa]o\s+fiscal\b",
    r"\bexce[çc][ãa]o\s+de\s+pr[ée]-?executividade\b",
    r"\bcertid[ãa]o\s+de\s+d[íi]vida\s+ativa\b", r"\bCDA\b",
    r"\brepeti[çc][ãa]o\s+de\s+ind[ée]bito\b",
    r"\bplanejamento\s+tribut[áa]rio\b",
    r"\btransa[çc][ãa]o\s+tribut[áa]ria\b",
    r"\breforma\s+tribut[áa]ria\b",
    r"\brecurso\s+ao\s+CARF\b", r"\bimpugna[çc][ãa]o\s+(?:ao\s+)?(?:auto|lan[çc]amento)\b",
]

# Gatilho 2: keywords fortes do dominio tributario
DOMAIN_KEYWORDS = [
    # Conceitos centrais
    r"\btributo\b", r"\bfisco\b", r"\bfazenda\s+p[úu]blica\b", r"\bfazenda\s+nacional\b",
    r"\breceita\s+federal\b", r"\bsujeito\s+passivo\b", r"\bcontribuinte\b",
    r"\bfato\s+gerador\b", r"\bbase\s+de\s+c[áa]lculo\b", r"\bal[íi]quota\b",
    r"\blan[çc]amento\b", r"\bobriga[çc][ãa]o\s+tribut[áa]ria\b",
    r"\bcr[ée]dito\s+tribut[áa]rio\b", r"\bredirecionamento\b",
    r"\bresponsabilidade\s+tribut[áa]ria\b", r"\bart\.?\s*135\s+(?:do\s+)?CTN\b",
    # Decadencia / prescricao
    r"\bdecad[êe]ncia\b", r"\bprescri[çc][ãa]o\s+(?:intercorrente|tribut[áa]ria)?\b",
    r"\bart\.?\s*173\b", r"\bart\.?\s*174\b", r"\bCTN\b",
    # Contencioso administrativo
    r"\bCARF\b", r"\bTIT\b", r"\bconselho\s+de\s+contribuintes\b",
    r"\bimpugna[çc][ãa]o\b", r"\bPAF\b", r"\bprocesso\s+administrativo\s+fiscal\b",
    r"\bDecreto\s+70\.?235\b", r"\bDec\.?\s*70\.?235\b",
    # Contencioso judicial
    r"\bmandado\s+de\s+seguran[çc]a\b", r"\ba[çc][ãa]o\s+an[uú]lat[óo]ria\b",
    r"\ba[çc][ãa]o\s+declarat[óo]ria\b", r"\ba[çc][ãa]o\s+de\s+consigna[çc][ãa]o\b",
    r"\bLEF\b", r"\bLei\s+6\.?830\b", r"\bcompensa[çc][ãa]o\s+tribut[áa]ria\b",
    r"\brestitui[çc][ãa]o\s+(?:de\s+)?tribut[áa]ri[ao]?\b",
    # Tributos federais
    r"\bIRPJ\b", r"\bIRPF\b", r"\bIR\b", r"\bIPI\b", r"\bPIS\b", r"\bCOFINS\b",
    r"\bCSLL\b", r"\bIOF\b", r"\bITR\b", r"\bcontribui[çc][ãa]o\s+previdenci[áa]ria\b",
    # Tributos estaduais e municipais
    r"\bICMS\b", r"\bIPVA\b", r"\bITCMD\b", r"\bISS\b", r"\bISSQN\b",
    r"\bIPTU\b", r"\bITBI\b",
    # Regimes / programas
    r"\bSimples\s+Nacional\b", r"\bLucro\s+Real\b", r"\bLucro\s+Presumido\b",
    r"\bparcelamento\b", r"\bREFIS\b", r"\bPERT\b",
    # Reforma tributaria
    r"\bCBS\b", r"\bIBS\b", r"\bEC\s*132\b", r"\bLC\s*214\b",
    r"\bimposto\s+seletivo\b", r"\bIVA\s+dual\b",
    # Planejamento / elisao / evasao
    r"\belis[ãa]o\b", r"\bevas[ãa]o\b", r"\bsonega[çc][ãa]o\b",
    r"\bplanejamento\s+sucess[óo]rio\s+tribut[áa]rio\b",
    # Sumulas / temas chave
    r"\bS[úu]mula\s+435\b", r"\bS[úu]mula\s+393\b",
    r"\bcr[ée]dito\s+pr[êe]mio\b", r"\btema\s+repetitivo\b",
]

# Gatilho 3: commands prefixados do plugin
PLUGIN_COMMANDS = [
    "/start-tributario",
    "/tributario-master",
    "/triagem",
    "/caso-tributario",
    "/impugnacao",
    "/recurso-carf",
    "/execucao-fiscal",
    "/anulatoria",
    "/mandado-seguranca",
    "/repeticao",
    "/planejamento",
]

# Keywords gerais (fallback — protocolo cauteloso quando casa generico)
CONSUM_KEYWORDS_GENERAL = [
    r"\btribut[áa]ri[ao]\b", r"\bimposto\b", r"\btaxa\b", r"\bcontribui[çc][ãa]o\b",
    r"\bd[íi]vida\s+ativa\b", r"\bfazenda\b", r"\bfisco\b", r"\bcontribuinte\b",
    r"\bd[ée]bito\s+fiscal\b", r"\bcobran[çc]a\s+fiscal\b", r"\bnotifica[çc][ãa]o\s+fiscal\b",
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
    """Verifica se existe `tributario/cowork-state.json` no path."""
    if cowork is None:
        return False
    return (cowork / "tributario" / "cowork-state.json").exists()


def _revisao_tecnica_enabled(cowork: Path | None) -> bool:
    """Le state.json e verifica revisao_tecnica.enabled. Default true se ausente."""
    if cowork is None:
        return True
    sf = cowork / "tributario" / "cowork-state.json"
    if not sf.exists():
        return True
    try:
        state = json.loads(sf.read_text(encoding="utf-8"))
        return bool(state.get("revisao_tecnica", {}).get("enabled", True))
    except Exception:
        return True


def _resolve_cowork() -> Path | None:
    """Resolve COWORK root via env TRIB_COWORK_PATH ou cwd ancestral."""
    env = os.environ.get("TRIB_COWORK_PATH") or os.environ.get("COWORK_PATH")
    if env:
        p = Path(env)
        if (p / "tributario" / "cowork-state.json").exists():
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
            f"[tributario-adv-os] Bypass detectado ({bypass}). "
            "Pecas, pareceres e estrategias serao entregues SEM a "
            "Revisao Tecnica R1-R4. Use por sua conta e risco.\n"
        )
        return 0

    # Caso 2: tarefa do dominio + plugin configurado
    if is_medico and _has_medico_state(cowork):
        if not _revisao_tecnica_enabled(cowork):
            sys.stdout.write(
                "[tributario-adv-os] Demanda juridico-tributaria detectada. "
                "Revisao Tecnica DESATIVADA na configuracao. Aciono apenas a cadeia de skills.\n"
                "Acionar skill: tributario-master.\n"
            )
        else:
            sys.stdout.write(
                "[tributario-adv-os] Demanda juridico-tributaria detectada. Plugin ativado.\n"
                "\n"
                "PROTOCOLO AUTOMATICO:\n"
                "1. Acionar skill `tributario-master` (Tier 0 - sempre ativa)\n"
                "2. Aplicar Hierarquia das 4 Camadas (1-Proibicoes, 2-Protocolos, 3-Estilo, 4-Skills)\n"
                "3. Verificar as Proibicoes Absolutas, com atencao especial:\n"
                "   - P1: Selo de Validacao de Norma Vigente (CTN + lei do tributo) antes de qualquer producao\n"
                "        -> aplicar a NORMA VIGENTE NO FATO GERADOR; atencao a transicao da Reforma EC 132/LC 214\n"
                "   - Coerencia de polo: contribuinte (defesa) x Fazenda - nunca redigir contra o cliente\n"
                "   - Decadencia (art. 173 CTN) x prescricao (art. 174 CTN) - nunca confundir os marcos\n"
                "   - Nunca confundir elisao licita com evasao/sonegacao (Lei 8.137/90)\n"
                "   - Sigilo fiscal + LGPD: dados do cliente NUNCA no plugin; pasta de caso local\n"
                "4. Acionar os Protocolos da Camada 2 conforme demanda\n"
                "   (P1 Selo de Validacao de Norma Vigente, P2 Integridade Documental,\n"
                "    P3 Memoria de Caso, P4 Cruzamento Administrativo-Judicial,\n"
                "    P5 Localizacao/Rito/Orgao competente, P6 Revisao R1-R4)\n"
                "5. Antes de entregar: Revisao Tecnica R1->R2->R3->R4 (skill `revisao-final-tributaria`)\n"
                "\n"
                "Bypass disponivel: `--no-revisao`, `--quick`, `/revisao off`.\n"
            )
        return 0

    # Caso 3: tarefa do dominio mas plugin NAO configurado
    if is_medico and not _has_medico_state(cowork):
        sys.stdout.write(
            "[tributario-adv-os] Detectei demanda juridico-tributaria, mas o plugin "
            "ainda nao foi configurado neste diretorio.\n"
            "\n"
            "RECOMENDACAO: rode /start-tributario para configurar (~5 min).\n"
            "Vou criar uma pasta `tributario/` aqui com a identidade do "
            "advogado/escritorio, OAB, cidade/UF, frentes de atuacao "
            "(administrativa/judicial/consultiva), tom de voz "
            "e configuracao das skills.\n"
            "\n"
            "Caso queira prosseguir SEM configurar, trabalho em modo fallback generico "
            "(persona neutra, qualidade reduzida). Apenas avise.\n"
        )
        return 0

    # Caso 4: tarefa do dominio geral - protocolo cauteloso
    if is_medico_other:
        sys.stdout.write(
            "[tributario-adv-os] Tarefa juridico-tributaria detectada (sem frente especifica). "
            "Aplique protocolo padrao:\n"
            "1. Questionamento previo (sem suposicoes silenciosas - exigir dado real do caso:\n"
            "   tributo, fato gerador com DATA, polo, esfera, valor do debito/credito).\n"
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
