#!/usr/bin/env python3
"""
Hook UserPromptSubmit do plugin Imobiliario Adv-OS.

Logica (ativacao automatica por contexto):
1. Le o prompt via stdin (JSON padrao Claude Code hooks).
2. Detecta bypass explicito: flags `--no-revisao`, `--quick`, `--no-r1r4`, `/revisao off`.
3. Detecta GATILHO de DOMINIO via keywords (3 niveis):
   - Gatilho 1: prompt contem palavras do dominio imobiliario/locacao
   - Gatilho 2: keywords fortes do dominio
   - Gatilho 3: comandos `/start-imobiliario`, `/imobiliario-master`, etc.
4. Se gatilho dispara:
   - Verifica se `imobiliario/cowork-state.json` existe no path atual
   - SIM: injeta protocolo Revisao Tecnica R1-R4 + aponta para skill `imobiliario-master`
   - NAO: sugere `/start-imobiliario` ao usuario (mas nao bloqueia)
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
# dominio — aqui carregam o lexico do DIREITO IMOBILIARIO E LOCACAO. Mantidos
# para preservar a logica do hook.

# Gatilho 1: frases fortes do dominio imobiliario/locacao (case insensitive)
TRIGGER_MEDICO = [
    r"\bdireito\s+imobili[áa]rio\b",
    r"\blei\s+do\s+inquilinato\b", r"\blei\s+8\.?245\b",
    r"\ba[çc][ãa]o\s+de\s+despejo\b", r"\bden[úu]ncia\s+vazia\b",
    r"\brevisional\s+de\s+aluguel\b", r"\ba[çc][ãa]o\s+renovat[óo]ria\b",
    r"\bpurga[çc][ãa]o\s+da\s+mora\b",
    r"\bconsigna[çc][ãa]o\s+de\s+aluguel\b",
    r"\bpromessa\s+de\s+compra\s+e\s+venda\b", r"\bcompromisso\s+de\s+compra\s+e\s+venda\b",
    r"\badjudica[çc][ãa]o\s+compuls[óo]ria\b",
    r"\ba[çc][ãa]o\s+possess[óo]ria\b", r"\breintegra[çc][ãa]o\s+de\s+posse\b",
    r"\bmanuten[çc][ãa]o\s+de\s+posse\b", r"\binterdito\s+proibit[óo]rio\b",
    r"\baliena[çc][ãa]o\s+fiduci[áa]ria\b", r"\blei\s+9\.?514\b",
    r"\bcondom[íi]nio\s+edil[íi]cio\b",
]

# Gatilho 2: keywords fortes do dominio imobiliario/locacao
DOMAIN_KEYWORDS = [
    # Locacao
    r"\bloca[çc][ãa]o\b", r"\blocador\b", r"\blocat[áa]rio\b", r"\binquilino\b",
    r"\baluguel\b", r"\bdespejo\b", r"\bden[úu]ncia\s+vazia\b",
    r"\bpurga[çc][ãa]o\s+da\s+mora\b", r"\brevisional\b", r"\brenovat[óo]ria\b",
    r"\bfundo\s+de\s+com[ée]rcio\b",
    r"\bfiador\b", r"\bfian[çc]a\b", r"\bcau[çc][ãa]o\b", r"\bseguro-?fian[çc]a\b",
    # Contratos imobiliarios
    r"\bcompra\s+e\s+venda\b", r"\bpromessa\s+de\s+compra\b", r"\bcompromisso\b",
    r"\barras\b", r"\bsinal\b", r"\bdistrato\b", r"\bres(?:c|s)is[ãa]o\s+contratual\b",
    r"\blei\s+13\.?786\b", r"\bv[íi]cio\s+redibit[óo]rio\b", r"\bevic[çc][ãa]o\b",
    # Direitos reais e posse
    r"\badjudica[çc][ãa]o\s+compuls[óo]ria\b", r"\bescritura\b", r"\boutorga\b",
    r"\bposse\b", r"\bpropriedade\b", r"\bdom[íi]nio\b",
    r"\ba[çc][ãa]o\s+possess[óo]ria\b", r"\breintegra[çc][ãa]o\s+de\s+posse\b",
    r"\bmanuten[çc][ãa]o\s+de\s+posse\b", r"\binterdito\s+proibit[óo]rio\b",
    r"\besbulho\b", r"\bturba[çc][ãa]o\b",
    r"\bdireito\s+de\s+vizinhan[çc]a\b",
    # Condominio
    r"\bcondom[íi]nio\b", r"\bcota\s+condominial\b", r"\btaxa\s+de\s+condom[íi]nio\b",
    r"\bconven[çc][ãa]o\s+de\s+condom[íi]nio\b",
    # Alienacao fiduciaria / garantias reais
    r"\baliena[çc][ãa]o\s+fiduci[áa]ria\b", r"\bfiduciante\b", r"\bcredor\s+fiduci[áa]rio\b",
    r"\bconsolida[çc][ãa]o\s+da\s+propriedade\b", r"\bleil[ãa]o\s+extrajudicial\b",
    r"\bhipoteca\b", r"\bSFH\b", r"\bSFI\b",
    # Incorporacao e registro
    r"\bincorpora[çc][ãa]o\s+imobili[áa]ria\b", r"\blei\s+4\.?591\b",
    r"\bmatr[íi]cula\b", r"\bregistro\s+de\s+im[óo]veis\b", r"\blei\s+6\.?015\b",
    r"\bcertid[ãa]o\b", r"\b[ôo]nus\b", r"\bdue\s+diligence\b",
    # Tributos do imovel (interface)
    r"\bIPTU\b", r"\bITBI\b",
    # Leis nucleo
    r"\bLei\s+8\.?245\b", r"\bLei\s+9\.?514\b", r"\bLei\s+13\.?786\b",
]

# Gatilho 3: commands prefixados do plugin
PLUGIN_COMMANDS = [
    "/start-imobiliario",
    "/imobiliario-master",
    "/triagem",
    "/caso-imobiliario",
    "/despejo",
    "/revisional",
    "/renovatoria",
    "/possessoria",
    "/compra-e-venda",
    "/adjudicacao",
    "/alienacao-fiduciaria",
]

# Keywords gerais (fallback — protocolo cauteloso quando casa generico)
CONSUM_KEYWORDS_GENERAL = [
    r"\bim[óo]vel\b", r"\bim[óo]veis\b", r"\baluguel\b", r"\bloca[çc][ãa]o\b",
    r"\bpropriedade\b", r"\bposse\b", r"\bcondom[íi]nio\b", r"\bcontrato\s+imobili[áa]rio\b",
    r"\bcompra\s+e\s+venda\b", r"\bterreno\b", r"\bapartamento\b", r"\bcasa\b",
    r"\bescritura\b", r"\bmatr[íi]cula\b",
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
    """Verifica se existe `imobiliario/cowork-state.json` no path."""
    if cowork is None:
        return False
    return (cowork / "imobiliario" / "cowork-state.json").exists()


def _revisao_tecnica_enabled(cowork: Path | None) -> bool:
    """Le state.json e verifica revisao_tecnica.enabled. Default true se ausente."""
    if cowork is None:
        return True
    sf = cowork / "imobiliario" / "cowork-state.json"
    if not sf.exists():
        return True
    try:
        state = json.loads(sf.read_text(encoding="utf-8"))
        return bool(state.get("revisao_tecnica", {}).get("enabled", True))
    except Exception:
        return True


def _resolve_cowork() -> Path | None:
    """Resolve COWORK root via env IMOB_COWORK_PATH ou cwd ancestral."""
    env = os.environ.get("IMOB_COWORK_PATH") or os.environ.get("COWORK_PATH")
    if env:
        p = Path(env)
        if (p / "imobiliario" / "cowork-state.json").exists():
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
            f"[imobiliario-adv-os] Bypass detectado ({bypass}). "
            "Pecas, pareceres e estrategias serao entregues SEM a "
            "Revisao Tecnica R1-R4. Use por sua conta e risco.\n"
        )
        return 0

    # Caso 2: tarefa do dominio + plugin configurado
    if is_medico and _has_medico_state(cowork):
        if not _revisao_tecnica_enabled(cowork):
            sys.stdout.write(
                "[imobiliario-adv-os] Demanda juridico-imobiliaria detectada. "
                "Revisao Tecnica DESATIVADA na configuracao. Aciono apenas a cadeia de skills.\n"
                "Acionar skill: imobiliario-master.\n"
            )
        else:
            sys.stdout.write(
                "[imobiliario-adv-os] Demanda juridico-imobiliaria detectada. Plugin ativado.\n"
                "\n"
                "PROTOCOLO AUTOMATICO:\n"
                "1. Acionar skill `imobiliario-master` (Tier 0 - sempre ativa)\n"
                "2. Aplicar Hierarquia das 4 Camadas (1-Proibicoes, 2-Protocolos, 3-Estilo, 4-Skills)\n"
                "3. Verificar as Proibicoes Absolutas, com atencao especial:\n"
                "   - P1: Selo de Validacao Legal Previa (validar Lei 8.245/CC/Lei 9.514/Lei 13.786\n"
                "        vigentes no contrato/fato + sumulas confirmadas) antes de qualquer producao\n"
                "   - Coerencia de polo: locador x locatario / comprador x vendedor / possuidor x\n"
                "     esbulhador / condominio x condomino / fiduciante x credor fiduciario -\n"
                "     nunca redigir contra o cliente\n"
                "   - POSSE x PROPRIEDADE x DOMINIO: a possessoria discute posse, nao titulo\n"
                "     dominial - nao cumular indevidamente\n"
                "   - GARANTIA LOCATICIA: vedada a cumulacao de garantias (art. 37, paragrafo unico,\n"
                "     Lei 8.245 - so uma modalidade: caucao, fianca, seguro-fianca ou cessao fiduciaria)\n"
                "   - PRAZO DECADENCIAL DA RENOVATORIA: a acao renovatoria deve ser ajuizada entre\n"
                "     1 ano e 6 meses antes do fim do contrato (art. 51, paragrafo 5, Lei 8.245)\n"
                "   - Sigilo + LGPD: dados do cliente e do imovel protegidos; pasta de caso local\n"
                "4. Acionar os Protocolos da Camada 2 conforme demanda\n"
                "   (P1 Selo de Validacao Legal Previa, P2 Integridade Documental,\n"
                "    P3 Memoria de Caso, P4 Cruzamento Extrajudicial-Judicial,\n"
                "    P5 Localizacao/Rito/Foro competente, P6 Revisao R1-R4)\n"
                "5. Antes de entregar: Revisao Tecnica R1->R2->R3->R4 (skill `revisao-final-imobiliaria`)\n"
                "\n"
                "Bypass disponivel: `--no-revisao`, `--quick`, `/revisao off`.\n"
            )
        return 0

    # Caso 3: tarefa do dominio mas plugin NAO configurado
    if is_medico and not _has_medico_state(cowork):
        sys.stdout.write(
            "[imobiliario-adv-os] Detectei demanda juridico-imobiliaria, mas o plugin "
            "ainda nao foi configurado neste diretorio.\n"
            "\n"
            "RECOMENDACAO: rode /start-imobiliario para configurar (~5 min).\n"
            "Vou criar uma pasta `imobiliario/` aqui com a identidade do "
            "advogado/escritorio, OAB, cidade/UF, frentes de atuacao "
            "(locacao / contratos imobiliarios / direitos reais e posse / consultivo), tom de voz "
            "e configuracao das skills.\n"
            "\n"
            "Caso queira prosseguir SEM configurar, trabalho em modo fallback generico "
            "(persona neutra, qualidade reduzida). Apenas avise.\n"
        )
        return 0

    # Caso 4: tarefa do dominio geral - protocolo cauteloso
    if is_medico_other:
        sys.stdout.write(
            "[imobiliario-adv-os] Tarefa juridico-imobiliaria detectada (sem frente especifica). "
            "Aplique protocolo padrao:\n"
            "1. Questionamento previo (sem suposicoes silenciosas - exigir dado real do caso:\n"
            "   tipo de imovel e matricula/endereco, contrato (tipo e data), polo, valor).\n"
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
