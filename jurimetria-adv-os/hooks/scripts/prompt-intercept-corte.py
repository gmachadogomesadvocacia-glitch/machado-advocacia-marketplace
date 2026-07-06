#!/usr/bin/env python3
"""
Hook UserPromptSubmit do plugin Jurimetria Adv-OS.

Logica (ativacao automatica por contexto):
1. Le o prompt via stdin (JSON padrao Claude Code hooks).
2. Detecta bypass explicito: flags `--no-revisao`, `--quick`, `--no-r1r4`, `/revisao off`.
3. Detecta GATILHO de DOMINIO via keywords (3 niveis):
   - Gatilho 1: frases fortes de jurimetria/estatistica processual
   - Gatilho 2: keywords do dominio (DataJud, taxa de exito, duracao media...)
   - Gatilho 3: comandos `/start-jurimetria`, `/coletar-acervo`, etc.
4. Se gatilho dispara:
   - Verifica se `jurimetria/cowork-state.json` existe no path atual
   - SIM: injeta protocolo (Proibicoes Estatisticas + Revisao R1-R4) + skill `jurimetria-master`
   - NAO: sugere `/start-jurimetria` ao usuario (mas nao bloqueia)
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


# Gatilho 1: frases fortes do dominio jurimetrico (case insensitive)
TRIGGER_FORTE = [
    r"\bjurimetria\b", r"\bjurim[ée]trico[as]?\b",
    r"\bestat[íi]stica\s+(processual|do\s+acervo|judicial)\b",
    r"\btaxa\s+de\s+[êe]xito\b",
    r"\bbenchmark\s+(processual|do\s+tribunal|jurimetrico)\b",
    r"\bDataJud\b",
    r"\bdura[çc][ãa]o\s+m[ée]dia\s+(do\s+processo|dos\s+processos)\b",
    r"\btempo\s+m[ée]dio\s+de\s+tramita[çc][ãa]o\b",
    r"\bquantum\s+m[ée]dio\b",
]

# Gatilho 2: keywords do dominio
DOMAIN_KEYWORDS = [
    r"\bquantos?\s+(casos|processos|a[çc][õo]es)\b",
    r"\bquanto\s+tempo\s+(demora|leva|dura)\b",
    r"\bchance\s+de\s+(ganhar|[êe]xito|sucesso)\b",
    r"\bprobabilidade\s+de\b",
    r"\bhist[óo]rico\s+do\s+(escrit[óo]rio|acervo)\b",
    r"\bportf[óo]lio\s+de\s+casos\b",
    r"\bvaras?\s+mais\s+(r[áa]pidas?|lentas?)\b",
    r"\bm[ée]dia\s+de\s+(condena[çc][ãa]o|indeniza[çc][ãa]o|acordo)\b",
    r"\bfaixa\s+de\s+(quantum|condena[çc][ãa]o|indeniza[çc][ãa]o)\b",
    r"\bbloco\s+jurim[ée]trico\b",
    r"\bandamentos?\s+do\s+processo\b",
    r"\bclasse\s+CNJ\b", r"\bassunto\s+CNJ\b",
    r"\bviabilidade\s+(do\s+caso|da\s+a[çc][ãa]o|da\s+demanda)\b",
    r"\bproposta\s+de\s+honor[áa]rios?\s+com\s+dados\b",
    r"\brelat[óo]rio\s+(do\s+acervo|de\s+casos|gerencial)\b",
    r"\b(encerrar|arquivar)\s+(o\s+|este\s+)?caso\b",
]

# Gatilho 3: commands prefixados do plugin
PLUGIN_COMMANDS = [
    "/start-jurimetria",
    "/jurimetria-master",
    "/status-jurimetria",
    "/triagem-jurimetrica",
    "/coletar-acervo",
    "/consulta-processo",
    "/benchmark-jurimetrico",
    "/quantum-jurimetrico",
    "/tempo-processual",
    "/viabilidade-jurimetrica",
    "/instrumentar-caso",
    "/encerrar-caso",
    "/revisao-final-jurimetria",
]

# Keywords gerais (fallback — protocolo cauteloso quando casa generico)
KEYWORDS_GENERAL = [
    r"\bestat[íi]stica\b", r"\bm[ée]dia\b", r"\bmediana\b",
    r"\bamostra\b", r"\bpercentual\b", r"\btend[êe]ncia\b",
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


def _is_dominio(prompt: str) -> bool:
    """Detecta se o prompt e do dominio (gatilhos 1, 2 ou 3)."""
    if _matches_any(prompt, TRIGGER_FORTE):
        return True
    if _matches_any(prompt, DOMAIN_KEYWORDS):
        return True
    low = prompt.lower()
    for cmd in PLUGIN_COMMANDS:
        if cmd.lower() in low:
            return True
    return False


def _is_dominio_general(prompt: str) -> bool:
    """Detecta tarefa estatistica em geral (sem keyword forte)."""
    return _matches_any(prompt, KEYWORDS_GENERAL)


def _has_bypass(prompt: str) -> str | None:
    low = prompt.lower()
    for token in BYPASS_TOKENS:
        if token in low:
            return token
    return None


def _has_state(cowork: Path | None) -> bool:
    if cowork is None:
        return False
    return (cowork / "jurimetria" / "cowork-state.json").exists()


def _revisao_tecnica_enabled(cowork: Path | None) -> bool:
    if cowork is None:
        return True
    sf = cowork / "jurimetria" / "cowork-state.json"
    if not sf.exists():
        return True
    try:
        state = json.loads(sf.read_text(encoding="utf-8"))
        return bool(state.get("revisao_tecnica", {}).get("enabled", True))
    except Exception:
        return True


def _resolve_cowork() -> Path | None:
    env = os.environ.get("JURI_COWORK_PATH") or os.environ.get("COWORK_PATH")
    if env:
        p = Path(env)
        if (p / "jurimetria" / "cowork-state.json").exists():
            return p
    return hook_utils.find_cowork(Path.cwd())


def main() -> int:
    payload = _load_input()
    prompt = payload.get("prompt") or payload.get("user_prompt") or ""
    if not isinstance(prompt, str) or not prompt.strip():
        return 0

    cowork = _resolve_cowork()
    bypass = _has_bypass(prompt)

    is_dom = _is_dominio(prompt)
    is_dom_other = _is_dominio_general(prompt) and not is_dom

    # Caso 1: bypass explicito
    if bypass and (is_dom or is_dom_other):
        sys.stdout.write(
            f"[jurimetria-adv-os] Bypass detectado ({bypass}). "
            "Analises e relatorios serao entregues SEM a Revisao R1-R4. "
            "As Proibicoes Estatisticas (Camada 1) continuam valendo — elas nao tem bypass.\n"
        )
        return 0

    # Caso 2: tarefa do dominio + plugin configurado
    if is_dom and _has_state(cowork):
        if not _revisao_tecnica_enabled(cowork):
            sys.stdout.write(
                "[jurimetria-adv-os] Demanda jurimetrica detectada. "
                "Revisao Tecnica DESATIVADA na configuracao. Aciono apenas a cadeia de skills.\n"
                "Acionar skill: jurimetria-master.\n"
            )
        else:
            sys.stdout.write(
                "[jurimetria-adv-os] Demanda jurimetrica detectada. Plugin ativado.\n"
                "\n"
                "PROTOCOLO AUTOMATICO:\n"
                "1. Acionar skill `jurimetria-master` (Tier 0 - sempre ativa)\n"
                "2. Aplicar Hierarquia das 4 Camadas (1-Proibicoes Estatisticas, 2-Protocolos, 3-Estilo, 4-Skills)\n"
                "3. Verificar as Proibicoes Estatisticas, com atencao especial:\n"
                "   - PE-01: nenhum numero sem N + metodo + fonte + data\n"
                "   - PE-02/03: descritivo != preditivo; NUNCA prometer resultado ou 'X% de chance de ganhar' (veda OAB)\n"
                "   - PE-04: N < 5 -> so leitura qualitativa, sem media/taxa\n"
                "   - PE-07: DataJud so tem capa+movimentos — quantum vem do CASO.md/jurisprudencia\n"
                "   - PE-06: PII/nome de cliente NUNCA em agregado ou relatorio que sai do escritorio\n"
                "4. Acionar os Protocolos da Camada 2 conforme demanda\n"
                "   (P1 Proveniencia dos Dados, P2 Instrumentacao do CASO.md, P3 Freio de N-minimo,\n"
                "    P4 Harmonizacao CNJ, P5 Sigilo/LGPD, P6 Revisao R1-R4)\n"
                "5. Antes de entregar: Revisao R1->R2->R3->R4 (skill `revisao-final-jurimetria`)\n"
                "\n"
                "Bypass disponivel (so da revisao): `--no-revisao`, `--quick`, `/revisao off`.\n"
            )
        return 0

    # Caso 3: tarefa do dominio mas plugin NAO configurado
    if is_dom and not _has_state(cowork):
        sys.stdout.write(
            "[jurimetria-adv-os] Detectei demanda jurimetrica, mas o plugin "
            "ainda nao foi configurado neste diretorio.\n"
            "\n"
            "RECOMENDACAO: rode /start-jurimetria para configurar (~5 min).\n"
            "Vou criar uma pasta `jurimetria/` aqui com a identidade do escritorio, "
            "a raiz do acervo (CASE_ROOT com os CASO.md) e as preferencias de relatorio.\n"
            "\n"
            "Caso queira prosseguir SEM configurar, trabalho em modo fallback generico "
            "(sem acervo apontado; as Proibicoes Estatisticas continuam valendo). Apenas avise.\n"
        )
        return 0

    # Caso 4: tarefa estatistica geral - protocolo cauteloso
    if is_dom_other:
        sys.stdout.write(
            "[jurimetria-adv-os] Tarefa com numeros/estatistica detectada (sem frente especifica). "
            "Se envolver dados processuais, aplique os freios:\n"
            "1. Nenhum numero sem N + metodo + fonte + data (PE-01).\n"
            "2. Descritivo != preditivo; nunca promessa de resultado (PE-02/03).\n"
            "3. N pequeno -> leitura qualitativa (PE-04).\n"
        )
        return 0

    # Caso default: nao e tarefa do dominio - silencio
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
