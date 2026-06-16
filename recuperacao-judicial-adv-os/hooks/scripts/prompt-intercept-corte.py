#!/usr/bin/env python3
"""
Hook UserPromptSubmit do plugin Recuperacao Judicial Adv-OS.

Logica (ativacao automatica por contexto):
1. Le o prompt via stdin (JSON padrao Claude Code hooks).
2. Detecta bypass explicito: flags `--no-revisao`, `--quick`, `--no-r1r4`, `/revisao off`.
3. Detecta GATILHO de DOMINIO via keywords (3 niveis):
   - Gatilho 1: prompt contem frases fortes do dominio de RJ/falencia
   - Gatilho 2: keywords fortes do dominio
   - Gatilho 3: comandos `/rj-master`, `/triagem`, etc.
4. Se gatilho dispara:
   - Verifica se `recuperacao-judicial/cowork-state.json` existe no path atual
   - SIM: injeta protocolo Revisao Tecnica R1-R4 + aponta para skill `rj-master`
   - NAO: sugere `/start-rj` ao usuario (mas nao bloqueia)
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
# lexico de RECUPERACAO JUDICIAL e FALENCIA. Mantidos para preservar a logica do hook.

# Gatilho 1: frases fortes do dominio de RJ/falencia (case insensitive)
TRIGGER_MEDICO = [
    r"\brecupera[çc][ãa]o\s+judicial\b",
    r"\brecupera[çc][ãa]o\s+extrajudicial\b",
    r"\bfal[êe]ncia\b",
    r"\binsolv[êe]ncia\b",
    r"\bLFRJ\b",
    r"\bLei\s+11\.?101\b", r"\bLei\s+14\.?112\b",
    r"\bhabilita[çc][ãa]o\s+de\s+cr[ée]dito\b",
    r"\bhabilita[çc][ãa]o\s+retardat[áa]ria\b",
    r"\bdiverg[êe]ncia\b",
    r"\bimpugna[çc][ãa]o\s+de\s+cr[ée]dito\b",
    r"\bquadro\s+geral\s+de\s+credores\b", r"\bQGC\b",
    r"\bassembleia\s+geral\s+de\s+credores\b", r"\bAGC\b",
    r"\bplano\s+de\s+recupera[çc][ãa]o\b",
    r"\badministrador\s+judicial\b",
    r"\bstay\s+period\b",
    r"\bcram\s+down\b",
    r"\bcredor\s+trabalhista\b",
]

# Gatilho 2: keywords fortes dos eixos de RJ/falencia
DOMAIN_KEYWORDS = [
    # Vias de habilitacao e prazos
    r"\bdiverg[êe]ncia\s+administrativa\b", r"\bart\.?\s*7[ºo]?\s*§?\s*1[ºo]?\b",
    r"\bimpugna[çc][ãa]o\s+judicial\b", r"\bart\.?\s*8[ºo]?\b",
    r"\bretardat[áa]ria\b", r"\bart\.?\s*10\b",
    r"\breserva\b", r"\bart\.?\s*6[ºo]?\s*§?\s*2[ºo]?\b",
    r"\bedital\s+de\s+credores\b", r"\brelacao\s+de\s+credores\b",
    # Classes de credores
    r"\bclasse\s+de\s+credores\b", r"\bclasse\s+I\b", r"\bclasse\s+II\b",
    r"\bclasse\s+III\b", r"\bclasse\s+IV\b",
    r"\bcredor\s+quirograf[áa]rio\b", r"\bgarantia\s+real\b",
    r"\bME\/EPP\b", r"\bmicroempresa\b",
    # Concursalidade e fato gerador
    r"\bconcursal\b", r"\bextraconcursal\b", r"\bfato\s+gerador\b",
    r"\bcr[ée]dito\s+concursal\b", r"\bcr[ée]dito\s+extraconcursal\b",
    r"\bperiodo\s+suspeito\b", r"\bato\s+revog[áa]vel\b",
    # Credito trabalhista em RJ
    r"\bteto\s+de\s+150\s+sal[áa]rios\b", r"\b150\s+SM\b", r"\bart\.?\s*83,?\s*I\b",
    r"\bcertid[ãa]o\s+de\s+cr[ée]dito\s+trabalhista\b", r"\bCH\b",
    r"\bcruzamento\s+JT\b", r"\bJustica\s+do\s+Trabalho\s+x?\s*RJ\b",
    r"\bsentenca\s+da\s+JT\b", r"\breclamat[óo]ria\b",
    r"\bverbas\s+rescis[óo]rias\b", r"\bFGTS\b", r"\bhonor[áa]rios\s+sucumbenciais\b",
    # Prescricao
    r"\bprescri[çc][ãa]o\s+intercorrente\b", r"\bprescri[çc][ãa]o\s+bienal\b",
    r"\bprescri[çc][ãa]o\s+da\s+habilita[çc][ãa]o\b",
    # Procedimento e orgaos do processo
    r"\bvara\s+empresarial\b", r"\bvara\s+falimentar\b", r"\bjuizo\s+universal\b",
    r"\bcomit[êe]\s+de\s+credores\b", r"\bgestor\s+judicial\b",
    r"\bsuspens[ãa]o\s+das\s+execu[çc][õo]es\b", r"\bsuspens[ãa]o\s+das\s+a[çc][õo]es\b",
    r"\bconvola[çc][ãa]o\s+em\s+fal[êe]ncia\b", r"\bdecreta[çc][ãa]o\s+de\s+fal[êe]ncia\b",
    # Plano e votacao
    r"\bnovacao\b", r"\bcram\s+down\b", r"\bquorum\b", r"\bdeagio\b", r"\bdes[áa]gio\b",
    r"\bcarencia\b", r"\bperdao\s+de\s+d[íi]vida\b",
    r"\blaudo\s+economico\b", r"\bviabilidade\s+economica\b",
    # Requisitos e documentos
    r"\bart\.?\s*48\b", r"\bart\.?\s*51\b", r"\bart\.?\s*53\b",
    r"\bdemonstra[çc][õo]es\s+contabeis\b", r"\bbalanco\s+patrimonial\b",
    # Grupo economico
    r"\bconsolida[çc][ãa]o\s+processual\b", r"\bconsolida[çc][ãa]o\s+substancial\b",
    r"\bgrupo\s+econ[ôo]mico\b",
    # Extrajudicial e falencia
    r"\bart\.?\s*161\b", r"\bhomologa[çc][ãa]o\s+de\s+plano\b",
    r"\bpedido\s+de\s+fal[êe]ncia\b", r"\bautofal[êe]ncia\b",
    r"\bcredor\s+extraconcursal\b", r"\bordem\s+de\s+pagamento\b", r"\bart\.?\s*83\b",
    r"\bart\.?\s*84\b", r"\bart\.?\s*67\b",
    # Conceitos / coobrigados
    r"\bcoobrigado\b", r"\bgarantidor\b", r"\baval(ista)?\b",
    r"\bdebenturista\b", r"\bcr[ée]dito\s+disputado\b",
    # Legislacao / sumulas / temas chave
    r"\bLei\s+11\.?101\b", r"\bLei\s+14\.?112\b",
    r"\bS[úu]mula\s+480\b", r"\bS[úu]mula\s+581\b",
    r"\bTema\s+1\.?051\b", r"\bIAC\s+13\b",
]

# Gatilho 3: commands prefixados do plugin
PLUGIN_COMMANDS = [
    "/rj-master",
    "/start-rj",
    "/triagem",
    "/caso-rj",
    "/credor-trabalhista",
    "/habilitacao",
    "/viabilidade",
    "/plano",
]

# Keywords gerais (fallback — protocolo cauteloso quando casa generico)
CONSUM_KEYWORDS_GENERAL = [
    r"\bcredor\b", r"\bdevedor\b", r"\brecuperanda\b",
    r"\bcr[ée]dito\b", r"\bhabilitar\b", r"\bcredores\b",
    r"\bempresa\s+em\s+crise\b", r"\bcrise\s+empresarial\b",
    r"\bplano\b", r"\bassembleia\b", r"\bcredor\b",
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
    """Verifica se existe `recuperacao-judicial/cowork-state.json` no path."""
    if cowork is None:
        return False
    return (cowork / "recuperacao-judicial" / "cowork-state.json").exists()


def _revisao_tecnica_enabled(cowork: Path | None) -> bool:
    """Le state.json e verifica revisao_tecnica.enabled. Default true se ausente."""
    if cowork is None:
        return True
    sf = cowork / "recuperacao-judicial" / "cowork-state.json"
    if not sf.exists():
        return True
    try:
        state = json.loads(sf.read_text(encoding="utf-8"))
        return bool(state.get("revisao_tecnica", {}).get("enabled", True))
    except Exception:
        return True


def _resolve_cowork() -> Path | None:
    """Resolve COWORK root via env RJ_COWORK_PATH ou cwd ancestral."""
    env = os.environ.get("RJ_COWORK_PATH") or os.environ.get("COWORK_PATH")
    if env:
        p = Path(env)
        if (p / "recuperacao-judicial" / "cowork-state.json").exists():
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
            f"[recuperacao-judicial-adv-os] Bypass detectado ({bypass}). "
            "Pecas, pareceres e estrategias serao entregues SEM a "
            "Revisao Tecnica R1-R4. Use por sua conta e risco.\n"
        )
        return 0

    # Caso 2: tarefa do dominio + plugin configurado
    if is_medico and _has_medico_state(cowork):
        if not _revisao_tecnica_enabled(cowork):
            sys.stdout.write(
                "[recuperacao-judicial-adv-os] Demanda de recuperacao judicial/falencia detectada. "
                "Revisao Tecnica DESATIVADA na configuracao. Aciono apenas a cadeia de skills.\n"
                "Acionar skill: rj-master.\n"
            )
        else:
            sys.stdout.write(
                "[recuperacao-judicial-adv-os] Demanda de recuperacao judicial/falencia detectada. Plugin ativado.\n"
                "\n"
                "PROTOCOLO AUTOMATICO:\n"
                "1. Acionar skill `rj-master` (Tier 0 - sempre ativa)\n"
                "2. Aplicar Hierarquia das 4 Camadas (1-Proibicoes, 2-Protocolos, 3-FIRAC/Estilo, 4-Skills)\n"
                "3. Verificar as Proibicoes Absolutas, com atencao especial:\n"
                "   - P1: Validacao de Norma Vigente (L11.101/2005 + L14.112/2020) antes de qualquer producao\n"
                "   - Coerencia de polo: credor x devedor-recuperando x administrador judicial - nunca redigir contra o cliente\n"
                "   - Classe e fato gerador: cravar a classe (I/II/III/IV) e a concursalidade pelo fato gerador\n"
                "   - Credito trabalhista (Classe I): aplicar o teto de 150 SM (art. 83, I); excedente em Classe III\n"
                "   - Dados do cliente NUNCA no plugin (sigilo OAB + LGPD; pasta de caso local)\n"
                "4. Acionar os Protocolos da Camada 2 conforme demanda\n"
                "   (P1 Validacao de Norma Vigente, P2 Integridade Documental, P3 Memoria de Caso,\n"
                "    P4 Mapeamento de Credores, P5 Localizacao/Vara, P6 Revisao R1-R4,\n"
                "    P8 Cruzamento Justica do Trabalho x RJ quando houver origem trabalhista)\n"
                "5. Antes de entregar: Revisao Tecnica R1->R2->R3->R4 (skill `revisao-final-rj`)\n"
                "\n"
                "Bypass disponivel: `--no-revisao`, `--quick`, `/revisao off`.\n"
            )
        return 0

    # Caso 3: tarefa do dominio mas plugin NAO configurado
    if is_medico and not _has_medico_state(cowork):
        sys.stdout.write(
            "[recuperacao-judicial-adv-os] Detectei demanda de recuperacao judicial/falencia, mas o plugin "
            "ainda nao foi configurado neste diretorio.\n"
            "\n"
            "RECOMENDACAO: rode /start-rj para configurar (~5 min).\n"
            "Vou criar uma pasta `recuperacao-judicial/` aqui com a identidade do "
            "advogado/escritorio, OAB, cidade/UF, area de foco (credor / credor-trabalhista / "
            "devedor-recuperando / administrador judicial), tom de voz e configuracao das skills.\n"
            "\n"
            "Caso queira prosseguir SEM configurar, trabalho em modo fallback generico "
            "(persona neutra, qualidade reduzida). Apenas avise.\n"
        )
        return 0

    # Caso 4: tarefa do dominio geral - protocolo cauteloso
    if is_medico_other:
        sys.stdout.write(
            "[recuperacao-judicial-adv-os] Tarefa de recuperacao judicial/falencia detectada (sem frente especifica). "
            "Aplique protocolo padrao:\n"
            "1. Questionamento previo (sem suposicoes silenciosas - exigir dado real do caso, "
            "em especial o POLO: credor / devedor-recuperando / administrador judicial).\n"
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
