#!/usr/bin/env python3
"""
Hook UserPromptSubmit do plugin Usucapiao Adv-OS.

Logica (ativacao automatica por contexto):
1. Le o prompt via stdin (JSON padrao Claude Code hooks).
2. Detecta bypass explicito: flags `--no-revisao`, `--quick`, `--no-r1r4`, `/revisao off`.
3. Detecta GATILHO de DOMINIO via keywords (3 niveis):
   - Gatilho 1: prompt contem palavras do dominio do usucapiao (judicial/extrajudicial)
   - Gatilho 2: keywords fortes do dominio
   - Gatilho 3: comandos `/start-usucapiao`, `/usucapiao-master`, etc.
4. Se gatilho dispara:
   - Verifica se `usucapiao/cowork-state.json` existe no path atual
   - SIM: injeta protocolo Revisao Tecnica R1-R4 + aponta para skill `usucapiao-master`
   - NAO: sugere `/start-usucapiao` ao usuario (mas nao bloqueia)
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
# lexico de USUCAPIAO (judicial e extrajudicial). Mantidos para preservar a
# logica do hook.

# Gatilho 1: frases fortes do dominio do usucapiao (case insensitive)
TRIGGER_MEDICO = [
    r"\busucapi[ãa]o\b", r"\busucapir\b", r"\busucapiente\b",
    r"\bprescri[çc][ãa]o\s+aquisitiva\b",
    r"\bposse\s+ad\s+usucapionem\b",
    r"\bposse\s+mansa\s+e\s+pac[íi]fica\b",
    r"\banimus\s+domini\b",
    r"\busucapi[ãa]o\s+extraordin[áa]ria\b", r"\busucapi[ãa]o\s+ordin[áa]ria\b",
    r"\busucapi[ãa]o\s+especial\s+urbana\b", r"\busucapi[ãa]o\s+especial\s+rural\b",
    r"\busucapi[ãa]o\s+familiar\b", r"\busucapi[ãa]o\s+coletiva\b",
    r"\busucapi[ãa]o\s+extrajudicial\b", r"\busucapi[ãa]o\s+administrativa\b",
    r"\bart\.?\s*1\.?238\b", r"\bart\.?\s*1\.?242\b",
    r"\bart\.?\s*1\.?240\b", r"\bart\.?\s*1\.?239\b",
    r"\b216-?A\b", r"\bart\.?\s*1\.?071\b",
]

# Gatilho 2: keywords fortes dos eixos do usucapiao
DOMAIN_KEYWORDS = [
    # Posse e requisitos
    r"\bposse\b", r"\bpossuidor\b", r"\bpossess[óo]ria\b",
    r"\bjusto\s+t[íi]tulo\b", r"\bboa-?f[ée]\b",
    r"\bposse\s+mansa\b", r"\bposse\s+ininterrupta\b",
    r"\batos\s+possess[óo]rios\b", r"\bbenfeitorias\b",
    r"\bIPTU\b", r"\bITR\b",
    # Modalidades / fundamentos
    r"\bmodalidade\s+de\s+usucapi[ãa]o\b",
    r"\bart\.?\s*183\b", r"\bart\.?\s*191\b",
    r"\bart\.?\s*1\.?240-?A\b", r"\bEstatuto\s+da\s+Cidade\b", r"\bart\.?\s*10\b",
    r"\b250\s*m[²2]\b", r"\b50\s*hectares\b", r"\bmetragem\b",
    # Extrajudicial / cartorio
    r"\bcart[óo]rio\b", r"\bata\s+notarial\b",
    r"\bplanta\s+e\s+memorial\b", r"\bmemorial\s+descritivo\b",
    r"\bART\b", r"\bgeorreferenciamento\b",
    r"\banu[êe]ncia\s+(dos\s+)?confrontantes\b", r"\banu[êe]ncia\b",
    r"\bRegistro\s+de\s+Im[óo]veis\b", r"\bmatr[íi]cula\b",
    r"\bProvimento\s+CNJ\b", r"\bLei\s+6\.?015\b",
    # Confrontantes / partes / citacao
    r"\bconfrontante\b", r"\boponente\b", r"\bvizinho\s+confinante\b",
    r"\br[ée]us\s+incertos\b", r"\bedital\b",
    r"\bcita[çc][ãa]o\s+por\s+edital\b",
    r"\bart\.?\s*246\b", r"\bart\.?\s*259\b",
    # Imovel / bem
    r"\b[áa]rea\s+urbana\b", r"\b[áa]rea\s+rural\b",
    r"\bim[óo]vel\s+sem\s+registro\b", r"\bim[óo]vel\s+sem\s+matr[íi]cula\b",
    r"\bbem\s+p[úu]blico\b", r"\bterra\s+devoluta\b",
    r"\bregulariza[çc][ãa]o\s+fundi[áa]ria\b",
    # Foro / competencia
    r"\bfor[oa]\s+(da\s+)?situa[çc][ãa]o\s+do\s+im[óo]vel\b", r"\brei\s+sitae\b",
    r"\bart\.?\s*47\b",
    # Entes a citar
    r"\bUni[ãa]o\b", r"\bMunic[íi]pio\b", r"\bFazenda\s+P[úu]blica\b",
    # Legislacao / sumulas chave
    r"\bC[óo]digo\s+Civil\b", r"\bS[úu]mula\s+340\b", r"\bS[úu]mula\s+237\b",
    r"\bS[úu]mula\s+11\s+do\s+STJ\b",
]

# Gatilho 3: commands prefixados do plugin
PLUGIN_COMMANDS = [
    "/start-usucapiao",
    "/usucapiao-master",
    "/triagem",
    "/caso-usucapiao",
    "/judicial",
    "/extrajudicial",
    "/contestacao",
    "/posse",
]

# Keywords gerais (fallback — protocolo cauteloso quando casa generico)
CONSUM_KEYWORDS_GENERAL = [
    r"\bposse\b", r"\bim[óo]vel\b", r"\bterreno\b", r"\blote\b",
    r"\bpropriedade\b", r"\bmatr[íi]cula\b", r"\bregistro\b",
    r"\bconfrontante\b", r"\bcart[óo]rio\b", r"\bregulariza[çc][ãa]o\b",
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
    """Verifica se existe `usucapiao/cowork-state.json` no path."""
    if cowork is None:
        return False
    return (cowork / "usucapiao" / "cowork-state.json").exists()


def _revisao_tecnica_enabled(cowork: Path | None) -> bool:
    """Le state.json e verifica revisao_tecnica.enabled. Default true se ausente."""
    if cowork is None:
        return True
    sf = cowork / "usucapiao" / "cowork-state.json"
    if not sf.exists():
        return True
    try:
        state = json.loads(sf.read_text(encoding="utf-8"))
        return bool(state.get("revisao_tecnica", {}).get("enabled", True))
    except Exception:
        return True


def _resolve_cowork() -> Path | None:
    """Resolve COWORK root via env USU_COWORK_PATH ou cwd ancestral."""
    env = os.environ.get("USU_COWORK_PATH") or os.environ.get("COWORK_PATH")
    if env:
        p = Path(env)
        if (p / "usucapiao" / "cowork-state.json").exists():
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
            f"[usucapiao-adv-os] Bypass detectado ({bypass}). "
            "Pecas, requerimentos, pareceres e estrategias serao entregues SEM a "
            "Revisao Tecnica R1-R4. Use por sua conta e risco.\n"
        )
        return 0

    # Caso 2: tarefa do dominio + plugin configurado
    if is_medico and _has_medico_state(cowork):
        if not _revisao_tecnica_enabled(cowork):
            sys.stdout.write(
                "[usucapiao-adv-os] Demanda de usucapiao detectada. "
                "Revisao Tecnica DESATIVADA na configuracao. Aciono apenas a cadeia de skills.\n"
                "Acionar skill: usucapiao-master.\n"
            )
        else:
            sys.stdout.write(
                "[usucapiao-adv-os] Demanda de usucapiao detectada. Plugin ativado.\n"
                "\n"
                "PROTOCOLO AUTOMATICO:\n"
                "1. Acionar skill `usucapiao-master` (Tier 0 - sempre ativa)\n"
                "2. Aplicar Hierarquia das 4 Camadas (1-Proibicoes, 2-Protocolos, 3-Estilo, 4-Skills)\n"
                "3. Verificar as Proibicoes Absolutas, com atencao especial:\n"
                "   - P1: Selo de Validacao de Norma Vigente (CC + CPC + Lei 6.015 + Provimento CNJ) antes de qualquer producao\n"
                "   - Coerencia de polo: usucapiente (autor/requerente) x confrontante/oponente - nunca redigir contra o cliente\n"
                "   - Bem PUBLICO nao e usucapivel (Sumula 340 STF; CF art. 183 §3 / 191 par. unico) - confirmar dominialidade do imovel\n"
                "   - Provar a posse ad usucapionem: tempo + animus domini + mansa/pacifica/ininterrupta + (justo titulo/boa-fe se ordinaria)\n"
                "   - Nunca inventar jurisprudencia, norma, Tema, numero de Provimento ou PA\n"
                "   - Sigilo OAB + LGPD: dados do cliente NUNCA no plugin (pasta caso local)\n"
                "4. Acionar os Protocolos da Camada 2 conforme demanda\n"
                "   (P1 Selo de Validacao de Norma Vigente, P2 Integridade Documental, P3 Memoria de Caso,\n"
                "    P4 Cruzamento Judicial-Extrajudicial, P5 Localizacao/Rito - foro da situacao do imovel/RI da circunscricao, P6 Revisao R1-R4)\n"
                "5. Antes de entregar: Revisao Tecnica R1->R2->R3->R4 (skill `revisao-final-usucapiao`)\n"
                "\n"
                "Bypass disponivel: `--no-revisao`, `--quick`, `/revisao off`.\n"
            )
        return 0

    # Caso 3: tarefa do dominio mas plugin NAO configurado
    if is_medico and not _has_medico_state(cowork):
        sys.stdout.write(
            "[usucapiao-adv-os] Detectei demanda de usucapiao, mas o plugin "
            "ainda nao foi configurado neste diretorio.\n"
            "\n"
            "RECOMENDACAO: rode /start-usucapiao para configurar (~5 min).\n"
            "Vou criar uma pasta `usucapiao/` aqui com a identidade do "
            "advogado/escritorio, OAB, cidade/UF, frentes (judicial / extrajudicial / "
            "defesa de confrontante / consultivo de regularizacao), "
            "tom de voz e configuracao das skills.\n"
            "\n"
            "Caso queira prosseguir SEM configurar, trabalho em modo fallback generico "
            "(persona neutra, qualidade reduzida). Apenas avise.\n"
        )
        return 0

    # Caso 4: tarefa do dominio geral - protocolo cauteloso
    if is_medico_other:
        sys.stdout.write(
            "[usucapiao-adv-os] Tarefa de usucapiao/imobiliario detectada (sem frente especifica). "
            "Aplique protocolo padrao:\n"
            "1. Questionamento previo (sem suposicoes silenciosas - exigir dado real do caso: "
            "via judicial x extrajudicial, modalidade, situacao do imovel, tempo de posse, confrontantes).\n"
            "2. Apresentar estrutura + premissas antes de redigir peca/requerimento/parecer.\n"
            "3. Aguardar confirmacao do advogado-operador.\n"
            "4. Antes de entregar: executar Revisao Tecnica R1-R4 se aplicavel.\n"
            "Bypass: `--no-revisao`, `--quick`, `/revisao off`.\n"
        )
        return 0

    # Caso default: nao e tarefa do dominio - silencio
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
