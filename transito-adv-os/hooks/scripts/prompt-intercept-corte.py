#!/usr/bin/env python3
"""
Hook UserPromptSubmit do plugin Transito Adv-OS.

Logica (ativacao automatica por contexto):
1. Le o prompt via stdin (JSON padrao Claude Code hooks).
2. Detecta bypass explicito: flags `--no-revisao`, `--quick`, `--no-r1r4`, `/revisao off`.
3. Detecta GATILHO de DOMINIO via keywords (3 niveis):
   - Gatilho 1: prompt contem palavras do dominio de transito
   - Gatilho 2: keywords fortes do dominio
   - Gatilho 3: comandos `/start-transito`, `/transito-master`, etc.
4. Se gatilho dispara:
   - Verifica se `transito/cowork-state.json` existe no path atual
   - SIM: injeta protocolo Revisao Tecnica R1-R4 + aponta para skill `transito-master`
   - NAO: sugere `/start-transito` ao usuario (mas nao bloqueia)
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
# dominio — aqui carregam o lexico do DIREITO DE TRANSITO. Mantidos para
# preservar a logica do hook.

# Gatilho 1: frases fortes do dominio de transito (case insensitive)
TRIGGER_MEDICO = [
    r"\bdireito\s+de\s+tr[âa]nsito\b", r"\binfra[çc][ãa]o\s+de\s+tr[âa]nsito\b",
    r"\bauto\s+de\s+infra[çc][ãa]o\b", r"\bAIT\b",
    r"\bnotifica[çc][ãa]o\s+de\s+autua[çc][ãa]o\b",
    r"\bnotifica[çc][ãa]o\s+da\s+autua[çc][ãa]o\b",
    r"\bnotifica[çc][ãa]o\s+de\s+penalidade\b",
    r"\bnotifica[çc][ãa]o\s+da\s+penalidade\b",
    r"\bdefesa\s+pr[ée]via\b", r"\bdefesa\s+da\s+autua[çc][ãa]o\b",
    r"\brecurso\s+(?:a\s+)?JARI\b", r"\bJARI\b", r"\bCETRAN\b",
    r"\bCONTRANDIFE\b", r"\bCONTRAN\b", r"\bDETRAN\b",
    r"\borg[ãa]o\s+autuador\b", r"\bCTB\b",
    r"\bc[óo]digo\s+de\s+tr[âa]nsito\b", r"\bLei\s*9\.?503\b", r"\bLei\s*14\.?071\b",
    r"\bpontua[çc][ãa]o\b", r"\bpontos\s+na\s+CNH\b",
    r"\bsuspens[ãa]o\s+do\s+direito\s+de\s+dirigir\b",
    r"\bcassa[çc][ãa]o\s+da\s+CNH\b", r"\binfra[çc][ãa]o\s+autossuspensiva\b",
    r"\bindica[çc][ãa]o\s+do\s+condutor\b",
    r"\bidentifica[çc][ãa]o\s+do\s+condutor\b",
    r"\bdupla\s+notifica[çc][ãa]o\b", r"\ba[çc][ãa]o\s+anulat[óo]ria\b",
    r"\bmandado\s+de\s+seguran[çc]a\b",
]

# Gatilho 2: keywords fortes do dominio de transito
DOMAIN_KEYWORDS = [
    # Autuacao e processo administrativo
    r"\bmulta\b", r"\binfra[çc][ãa]o\s+de\s+tr[âa]nsito\b",
    r"\bauto\s+de\s+infra[çc][ãa]o\b", r"\bAIT\b",
    r"\bnotifica[çc][ãa]o\s+de\s+autua[çc][ãa]o\b", r"\bNA\b",
    r"\bnotifica[çc][ãa]o\s+de\s+penalidade\b", r"\bNP\b",
    r"\bdefesa\s+pr[ée]via\b", r"\bdefesa\s+da\s+autua[çc][ãa]o\b",
    r"\brecurso\b", r"\bJARI\b", r"\bCETRAN\b", r"\bCONTRANDIFE\b",
    r"\bCONTRAN\b", r"\bDETRAN\b", r"\borg[ãa]o\s+autuador\b",
    # Normas
    r"\bCTB\b", r"\bc[óo]digo\s+de\s+tr[âa]nsito\b",
    r"\bLei\s*9\.?503\b", r"\bLei\s*14\.?071\b",
    # Pontuacao / CNH / habilitacao
    r"\bpontua[çc][ãa]o\b", r"\bpontos\s+na\s+CNH\b", r"\bcarteira\b",
    r"\bhabilita[çc][ãa]o\b", r"\bCNH\b",
    r"\bsuspens[ãa]o\s+do\s+direito\s+de\s+dirigir\b",
    r"\bcassa[çc][ãa]o\s+da\s+CNH\b", r"\breabilita[çc][ãa]o\b",
    r"\binfra[çc][ãa]o\s+autossuspensiva\b",
    # Classificacao da infracao
    r"\binfra[çc][ãa]o\s+leve\b", r"\binfra[çc][ãa]o\s+m[ée]dia\b",
    r"\binfra[çc][ãa]o\s+grave\b", r"\binfra[çc][ãa]o\s+grav[íi]ssima\b",
    r"\bmultiplicador\b",
    # Sujeitos
    r"\bcondutor\b", r"\bpropriet[áa]rio\s+do\s+ve[íi]culo\b",
    r"\bindica[çc][ãa]o\s+do\s+condutor\b",
    r"\bidentifica[çc][ãa]o\s+do\s+condutor\b",
    # Vicios do auto
    r"\bradar\b", r"\bequipamento\b", r"\bafer[íi][çc][ãa]o\b",
    r"\bINMETRO\b", r"\bsinaliza[çc][ãa]o\b", r"\bvelocidade\b",
    r"\bavan[çc]o\s+de\s+sinal\b", r"\bestacionamento\b", r"\bzona\s+azul\b",
    r"\bdupla\s+notifica[çc][ãa]o\b",
    # Lei seca / embriaguez (interface criminal art. 306; administrativo art. 165)
    r"\blei\s+seca\b", r"\bembriaguez\b",
    # Veiculo
    r"\btr[âa]nsito\b", r"\bve[íi]culo\b", r"\bplaca\b", r"\bRENAVAM\b",
    # Via judicial
    r"\ba[çc][ãa]o\s+anulat[óo]ria\b", r"\bmandado\s+de\s+seguran[çc]a\b",
    # Sumulas / prazos / prescricao
    r"\bsum(?:ula)?\.?\s*312\b", r"\bsum(?:ula)?\.?\s*127\b",
    r"\bprescri[çc][ãa]o\b", r"\bdecad[êe]ncia\s+administrativa\b",
    r"\bampla\s+defesa\b", r"\bprazo\s+de\s+30\s+dias\b",
]

# Gatilho 3: commands prefixados do plugin
PLUGIN_COMMANDS = [
    "/start-transito",
    "/transito-master",
    "/triagem",
    "/caso-transito",
    "/defesa-previa",
    "/defesa-autuacao",
    "/recurso-jari",
    "/recurso-cetran",
    "/indicacao-condutor",
    "/anulatoria",
    "/mandado-seguranca",
    "/analise-auto",
    "/parecer-transito",
]

# Keywords gerais (fallback — protocolo cauteloso quando casa generico)
CONSUM_KEYWORDS_GENERAL = [
    r"\bmulta\b", r"\binfra[çc][ãa]o\b", r"\btr[âa]nsito\b", r"\bve[íi]culo\b",
    r"\bCNH\b", r"\bcarteira\b", r"\bhabilita[çc][ãa]o\b", r"\bpontos\b",
    r"\bpontua[çc][ãa]o\b", r"\bdefesa\b", r"\brecurso\b", r"\bcondutor\b",
    r"\bDETRAN\b", r"\bautua[çc][ãa]o\b",
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
    """Verifica se existe `transito/cowork-state.json` no path."""
    if cowork is None:
        return False
    return (cowork / "transito" / "cowork-state.json").exists()


def _revisao_tecnica_enabled(cowork: Path | None) -> bool:
    """Le state.json e verifica revisao_tecnica.enabled. Default true se ausente."""
    if cowork is None:
        return True
    sf = cowork / "transito" / "cowork-state.json"
    if not sf.exists():
        return True
    try:
        state = json.loads(sf.read_text(encoding="utf-8"))
        return bool(state.get("revisao_tecnica", {}).get("enabled", True))
    except Exception:
        return True


def _resolve_cowork() -> Path | None:
    """Resolve COWORK root via env TRAN_COWORK_PATH ou cwd ancestral."""
    env = os.environ.get("TRAN_COWORK_PATH") or os.environ.get("COWORK_PATH")
    if env:
        p = Path(env)
        if (p / "transito" / "cowork-state.json").exists():
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
            f"[transito-adv-os] Bypass detectado ({bypass}). "
            "Pecas, pareceres e estrategias serao entregues SEM a "
            "Revisao Tecnica R1-R4. Use por sua conta e risco.\n"
        )
        return 0

    # Caso 2: tarefa do dominio + plugin configurado
    if is_medico and _has_medico_state(cowork):
        if not _revisao_tecnica_enabled(cowork):
            sys.stdout.write(
                "[transito-adv-os] Demanda de transito detectada. "
                "Revisao Tecnica DESATIVADA na configuracao. Aciono apenas a cadeia de skills.\n"
                "Acionar skill: transito-master.\n"
            )
        else:
            sys.stdout.write(
                "[transito-adv-os] Demanda de transito detectada. Plugin ativado.\n"
                "\n"
                "PROTOCOLO AUTOMATICO:\n"
                "1. Acionar skill `transito-master` (Tier 0 - sempre ativa)\n"
                "2. Aplicar Hierarquia das 4 Camadas (1-Proibicoes, 2-Protocolos, 3-Estilo, 4-Skills)\n"
                "3. Verificar as Proibicoes Absolutas, com atencao especial:\n"
                "   - SELO DE VALIDACAO LEGAL PREVIA (P1, triagem-transito): validar CTB (Lei 9.503/97)\n"
                "        + Lei 14.071/2020 + Resolucoes CONTRAN vigentes na data da infracao + sumulas\n"
                "        confirmadas, antes de qualquer producao\n"
                "   - NORMA VIGENTE NA INFRACAO: aplicar a norma vigente na data do fato (tempus regit\n"
                "        actum) - atencao as mudancas da Lei 14.071/2020 (pontuacao, validade da CNH)\n"
                "   - PRAZOS ADMINISTRATIVOS PRECLUSIVOS: defesa previa, JARI, CETRAN tem prazos fatais\n"
                "        (em regra 30 dias da notificacao) - nao perder\n"
                "   - DUPLA NOTIFICACAO: a ausencia de notificacao da autuacao E da penalidade gera\n"
                "        nulidade (Sum. 312 STJ; CTB 280-281)\n"
                "   - ETICO: NUNCA orientar fraude de pontuacao ou indicacao falsa do condutor (e crime\n"
                "        - art. 299 CP); defesa legitima != fraude\n"
                "   - Coerencia de polo: defesa do condutor/proprietario (o Estado autua) - nunca\n"
                "        redigir contra o cliente\n"
                "   - INTERFACES: crime de transito (embriaguez art. 306, homicidio/lesao culposa\n"
                "        302/303 CTB) -> plugin criminal; reparacao civil/DPVAT -> plugin civel\n"
                "4. Acionar os Protocolos da Camada 2 conforme demanda\n"
                "   (P1 Selo de Validacao Legal Previa, P2 Integridade Documental - auto/NA/NP/fotos,\n"
                "    P3 Memoria de Caso, P4 Cruzamento Auto-Infracao-Penalidade-Pontuacao,\n"
                "    P5 Esfera/Orgao Autuador/Instancia/Foro, P6 Revisao R1-R4)\n"
                "5. Antes de entregar: Revisao Tecnica R1->R2->R3->R4 (skill `revisao-final-transito`)\n"
                "\n"
                "Bypass disponivel: `--no-revisao`, `--quick`, `/revisao off`.\n"
            )
        return 0

    # Caso 3: tarefa do dominio mas plugin NAO configurado
    if is_medico and not _has_medico_state(cowork):
        sys.stdout.write(
            "[transito-adv-os] Detectei demanda de transito, mas o plugin "
            "ainda nao foi configurado neste diretorio.\n"
            "\n"
            "RECOMENDACAO: rode /start-transito para configurar (~5 min).\n"
            "Vou criar uma pasta `transito/` aqui com a identidade do "
            "advogado/escritorio, OAB, cidade/UF, frentes de atuacao "
            "(Administrativo - defesa/autuacao, JARI, CETRAN / CNH-Habilitacao - "
            "suspensao, cassacao, indicacao / Judicial - anulatoria, MS / "
            "Analise - vicios do auto), tom de voz e configuracao das skills.\n"
            "\n"
            "Caso queira prosseguir SEM configurar, trabalho em modo fallback generico "
            "(persona neutra, qualidade reduzida). Apenas avise.\n"
        )
        return 0

    # Caso 4: tarefa do dominio geral - protocolo cauteloso
    if is_medico_other:
        sys.stdout.write(
            "[transito-adv-os] Tarefa de transito detectada (sem frente especifica). "
            "Aplique protocolo padrao:\n"
            "1. Questionamento previo (sem suposicoes silenciosas - exigir dado real do caso:\n"
            "   dados do auto (AIT, codigo da infracao, data/local, placa/RENAVAM, orgao autuador),\n"
            "   eixo (administrativo / CNH-habilitacao / judicial / analise do auto), polo\n"
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
