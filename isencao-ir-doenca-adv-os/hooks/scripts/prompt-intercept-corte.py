#!/usr/bin/env python3
"""
Hook UserPromptSubmit do plugin Isencao IR Doenca Adv-OS.

Logica (ativacao automatica por contexto):
1. Le o prompt via stdin (JSON padrao Claude Code hooks).
2. Detecta bypass explicito: flags `--no-revisao`, `--quick`, `--no-r1r4`, `/revisao off`.
3. Detecta GATILHO de DOMINIO via keywords (3 niveis):
   - Gatilho 1: prompt contem frases fortes do dominio de isencao de IR por doenca grave
   - Gatilho 2: keywords fortes do dominio
   - Gatilho 3: comandos `/start-isencao-ir`, `/isencao-ir-master`, etc.
4. Se gatilho dispara:
   - Verifica se `isencao-ir/cowork-state.json` existe no path atual
   - SIM: injeta protocolo Revisao Tecnica R1-R4 + aponta para skill `isencao-ir-master`
   - NAO: sugere `/start-isencao-ir` ao usuario (mas nao bloqueia)
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
# lexico da ISENCAO DE IRPF POR DOENCA GRAVE. Mantidos para preservar a logica
# do hook.

# Gatilho 1: frases fortes do dominio de isencao de IR por doenca grave (case insensitive)
TRIGGER_MEDICO = [
    r"\bisen[çc][ãa]o\s+de\s+imposto\s+de\s+renda\b",
    r"\bisen[çc][ãa]o\s+de\s+IR\b", r"\bisen[çc][ãa]o\s+do\s+IRPF\b",
    r"\bisen[çc][ãa]o\s+por\s+doen[çc]a\s+grave\b",
    r"\bIRPF\b",
    r"\bart\.?\s*6[ºo]?,?\s*XIV\b", r"\bLei\s+7\.713\b",
    r"\bdoen[çc]a\s+grave\b",
    r"\bproventos\s+de\s+aposentadoria\b",
    r"\bretifica[çc][ãa]o\s+da\s+DIRPF\b",
    r"\bS[úu]mula\s+598\b", r"\bS[úu]mula\s+627\b",
    r"\brepeti[çc][ãa]o\s+de\s+ind[ée]bito\b",
]

# Gatilho 2: keywords fortes dos eixos da isencao de IR por doenca grave
DOMAIN_KEYWORDS = [
    # Doencas da lista do art. 6, XIV
    r"\bneoplasia\s+maligna\b", r"\bc[âa]ncer\b",
    r"\bcardiopatia\s+grave\b", r"\bcegueira\b",
    r"\bdoen[çc]a\s+de\s+parkinson\b", r"\besclerose\s+m[úu]ltipla\b",
    r"\bnefropatia\s+grave\b", r"\bhepatopatia\s+grave\b",
    r"\bAIDS\b", r"\bSIDA\b", r"\bhansen[íi]ase\b",
    r"\bparalisia\s+irrevers[íi]vel\s+e\s+incapacitante\b",
    r"\bespondiloartrose\s+anquilosante\b", r"\bfibrose\s+c[íi]stica\b",
    r"\bdoen[çc]a\s+de\s+paget\b", r"\bosteite\s+deformante\b",
    r"\bcontamina[çc][ãa]o\s+por\s+radia[çc][ãa]o\b",
    r"\baliena[çc][ãa]o\s+mental\b", r"\btuberculose\s+ativa\b",
    # Tipo de provento isento
    r"\bproventos\s+de\s+aposentadoria\b", r"\bpens[ãa]o\b",
    r"\breforma\b", r"\baposentadoria\s+por\s+invalidez\b",
    # Restituicao / indebito
    r"\brestitui[çc][ãa]o\s+de\s+ind[ée]bito\b", r"\bretifica[çc][ãa]o\s+da\s+DIRPF\b",
    r"\bdeclara[çc][ãa]o\s+de\s+ajuste\b", r"\binforme\s+de\s+rendimentos\b",
    r"\bimposto\s+retido\s+na\s+fonte\b", r"\bIRRF\b",
    r"\breten[çc][ãa]o\s+indevida\b", r"\bIR\s+retido\b",
    # Fontes pagadoras
    r"\bINSS\b", r"\bRPPS\b", r"\bfundo\s+de\s+pens[ãa]o\b",
    r"\bprevid[êe]ncia\s+complementar\b", r"\bfonte\s+pagadora\b",
    r"\bRGPS\b", r"\baposentadoria\s+do\s+servidor\b",
    # Receita / esfera administrativa
    r"\bReceita\s+Federal\b", r"\be-?CAC\b", r"\bIN\s+RFB\s+1\.?500\b",
    r"\brequerimento\s+de\s+isen[çc][ãa]o\b",
    # Prova / laudo
    r"\blaudo\s+m[ée]dico\b", r"\blaudo\s+pericial\b",
    r"\bservi[çc]o\s+m[ée]dico\s+oficial\b", r"\bCID\b",
    r"\bdata\s+do\s+diagn[óo]stico\b",
    # Sumulas / Temas / via
    r"\bS[úu]mula\s+598\b", r"\bS[úu]mula\s+627\b", r"\bTema\s+1\.?037\b",
    r"\bmandado\s+de\s+seguran[çc]a\b",
    r"\ba[çc][ãa]o\s+declarat[óo]ria\b",
    r"\bisen[çc][ãa]o\s+tribut[áa]ria\b",
    r"\bprescri[çc][ãa]o\s+quinquenal\b", r"\bCTN\s+art\.?\s*168\b",
    # Conceitos chave
    r"\bcontribuinte\b", r"\bFazenda\s+Nacional\b",
    r"\bvara\s+federal\b", r"\bjuizado\s+especial\s+federal\b", r"\bJEF\b",
]

# Gatilho 3: commands prefixados do plugin
PLUGIN_COMMANDS = [
    "/start-isencao-ir",
    "/isencao-ir-master",
    "/triagem",
    "/caso-isencao-ir",
    "/requerimento",
    "/acao-judicial",
    "/mandado-seguranca",
    "/calculos",
    "/revisao-final-isencao-ir",
    "/status-isencao-ir",
]

# Keywords gerais (fallback — protocolo cauteloso quando casa generico)
CONSUM_KEYWORDS_GENERAL = [
    r"\bcontribuinte\b", r"\baposentado\b", r"\baposentadoria\b",
    r"\bpensionista\b", r"\bpens[ãa]o\b", r"\bimposto\s+de\s+renda\b",
    r"\bIR\b", r"\bRestitui[çc][ãa]o\b", r"\bReceita\b",
    r"\bproventos\b", r"\bdeclara[çc][ãa]o\b", r"\bisen[çc][ãa]o\b",
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
    """Verifica se existe `isencao-ir/cowork-state.json` no path."""
    if cowork is None:
        return False
    return (cowork / "isencao-ir" / "cowork-state.json").exists()


def _revisao_tecnica_enabled(cowork: Path | None) -> bool:
    """Le state.json e verifica revisao_tecnica.enabled. Default true se ausente."""
    if cowork is None:
        return True
    sf = cowork / "isencao-ir" / "cowork-state.json"
    if not sf.exists():
        return True
    try:
        state = json.loads(sf.read_text(encoding="utf-8"))
        return bool(state.get("revisao_tecnica", {}).get("enabled", True))
    except Exception:
        return True


def _resolve_cowork() -> Path | None:
    """Resolve COWORK root via env ISIR_COWORK_PATH ou cwd ancestral."""
    env = os.environ.get("ISIR_COWORK_PATH") or os.environ.get("COWORK_PATH")
    if env:
        p = Path(env)
        if (p / "isencao-ir" / "cowork-state.json").exists():
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
            f"[isencao-ir-doenca-adv-os] Bypass detectado ({bypass}). "
            "Pecas, pareceres e estrategias serao entregues SEM a "
            "Revisao Tecnica R1-R4. Use por sua conta e risco.\n"
        )
        return 0

    # Caso 2: tarefa do dominio + plugin configurado
    if is_medico and _has_medico_state(cowork):
        if not _revisao_tecnica_enabled(cowork):
            sys.stdout.write(
                "[isencao-ir-doenca-adv-os] Demanda de isencao de IRPF por doenca grave detectada. "
                "Revisao Tecnica DESATIVADA na configuracao. Aciono apenas a cadeia de skills.\n"
                "Acionar skill: isencao-ir-master.\n"
            )
        else:
            sys.stdout.write(
                "[isencao-ir-doenca-adv-os] Demanda de isencao de IRPF por doenca grave detectada. Plugin ativado.\n"
                "\n"
                "PROTOCOLO AUTOMATICO:\n"
                "1. Acionar skill `isencao-ir-master` (Tier 0 - sempre ativa)\n"
                "2. Aplicar Hierarquia das 4 Camadas (1-Proibicoes, 2-Protocolos, 3-Estilo, 4-Skills)\n"
                "3. Verificar as Proibicoes Absolutas, com atencao especial:\n"
                "   - P1: Selo de Validacao de Norma Vigente antes de qualquer producao\n"
                "         (Lei 7.713/88 art. 6 XIV + IN RFB 1500 + Sumulas 598/627 STJ)\n"
                "   - NUNCA opinar sobre conduta clinica ou diagnostico - o laudo e do medico;\n"
                "     dados de saude sao SENSIVEIS (LGPD art. 11 + sigilo)\n"
                "   - So afirmar isencao sobre PROVENTOS de aposentadoria/pensao/reforma;\n"
                "     a isencao NAO se estende a rendimentos de ATIVO (Sumula 627 STJ)\n"
                "   - Coerencia de polo: contribuinte/beneficiario x Fazenda/fonte pagadora -\n"
                "     nunca redigir contra o cliente\n"
                "   - Restituicao limitada aos ultimos 5 anos (prescricao quinquenal - CTN art. 168)\n"
                "   - Dados do cliente NUNCA no plugin (sigilo OAB + LGPD; pasta caso local)\n"
                "4. Acionar os Protocolos da Camada 2 conforme demanda\n"
                "   (P1 Selo de Validacao de Norma, P2 Integridade, P3 Memoria de Caso,\n"
                "    P4 Cruzamento Judicial-Administrativo, P5 Localizacao/Rito, P6 Revisao R1-R4)\n"
                "5. Antes de entregar: Revisao Tecnica R1->R2->R3->R4 (skill `revisao-final-isencao-ir`)\n"
                "\n"
                "Bypass disponivel: `--no-revisao`, `--quick`, `/revisao off`.\n"
            )
        return 0

    # Caso 3: tarefa do dominio mas plugin NAO configurado
    if is_medico and not _has_medico_state(cowork):
        sys.stdout.write(
            "[isencao-ir-doenca-adv-os] Detectei demanda de isencao de IRPF por doenca grave, mas o plugin "
            "ainda nao foi configurado neste diretorio.\n"
            "\n"
            "RECOMENDACAO: rode /start-isencao-ir para configurar (~5 min).\n"
            "Vou criar uma pasta `isencao-ir/` aqui com a identidade do "
            "advogado/escritorio, OAB, cidade/UF, area de foco, "
            "tom de voz e configuracao das skills.\n"
            "\n"
            "Caso queira prosseguir SEM configurar, trabalho em modo fallback generico "
            "(persona neutra, qualidade reduzida). Apenas avise.\n"
        )
        return 0

    # Caso 4: tarefa do dominio geral - protocolo cauteloso
    if is_medico_other:
        sys.stdout.write(
            "[isencao-ir-doenca-adv-os] Tarefa tributaria/previdenciaria detectada (sem frente especifica). "
            "Aplique protocolo padrao:\n"
            "1. Questionamento previo (sem suposicoes silenciosas - exigir dado real do caso:\n"
            "   doenca da lista do art. 6 XIV, data do laudo, fonte pagadora, tipo de provento).\n"
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
