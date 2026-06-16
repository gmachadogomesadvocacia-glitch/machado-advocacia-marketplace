#!/usr/bin/env python3
"""
Hook UserPromptSubmit do plugin Consumidor Adv-OS.

Logica (ativacao automatica por contexto):
1. Le o prompt via stdin (JSON padrao Claude Code hooks).
2. Detecta bypass explicito: flags `--no-revisao`, `--quick`, `--no-r1r4`, `/revisao off`.
3. Detecta GATILHO de DOMINIO via keywords (3 niveis):
   - Gatilho 1: prompt contem palavras do dominio do consumidor
   - Gatilho 2: keywords fortes do dominio
   - Gatilho 3: comandos `/start-consumidor`, `/consumidor-master`, etc.
4. Se gatilho dispara:
   - Verifica se `consumidor/cowork-state.json` existe no path atual
   - SIM: injeta protocolo Revisao Tecnica R1-R4 + aponta para skill `consumidor-master`
   - NAO: sugere `/start-consumidor` ao usuario (mas nao bloqueia)
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
# lexico do DIREITO DO CONSUMIDOR. Mantidos para preservar a logica do hook.

# Gatilho 1: frases fortes do dominio do consumidor/bancario (case insensitive)
TRIGGER_MEDICO = [
    r"\bdireito\s+do\s+consumidor\b",
    r"\brela[çc][ãa]o\s+de\s+consumo\b",
    r"\bc[óo]digo\s+de\s+defesa\s+do\s+consumidor\b",
    r"\bCDC\b",
    r"\brevisional\s+banc[áa]ria?\b", r"\ba[çc][ãa]o\s+revisional\b",
    r"\bnegativa[çc][ãa]o\s+indevida\b",
    r"\bbusca\s+e\s+apreens[ãa]o\b",
    r"\brepeti[çc][ãa]o\s+de\s+ind[ée]bito\b",
    r"\bcl[áa]usula\s+abusiva\b",
    r"\bsuperendividamento\b",
    r"\bv[íi]cio\s+do\s+produto\b", r"\bv[íi]cio\s+oculto\b",
    r"\bpublicidade\s+engan[oa]sa\b",
]

# Gatilho 2: keywords fortes dos eixos do consumo
DOMAIN_KEYWORDS = [
    # Bancario / financeiro
    r"\bjuros\s+abusivos\b", r"\bcapitaliza[çc][ãa]o\b", r"\banatocismo\b",
    r"\btarifa\s+banc[áa]ria\b", r"\bc[ée]dula\s+de\s+cr[ée]dito\b",
    r"\bfinanciamento\b", r"\baliena[çc][ãa]o\s+fiduci[áa]ria\b",
    r"\bconsignado\b", r"\bcart[ãa]o\s+de\s+cr[ée]dito\b", r"\brotativo\b",
    r"\btaxa\s+m[ée]dia\b", r"\bCET\b", r"\bspread\b", r"\bcontrato\s+de\s+ades[ãa]o\b",
    r"\bpurga[çc][ãa]o\s+da\s+mora\b", r"\bempr[ée]stimo\b",
    # Negativacao / cadastros
    r"\bSPC\b", r"\bSerasa\b", r"\bSCPC\b",
    r"\binscri[çc][ãa]o\s+indevida\b", r"\bcadastro\s+de\s+inadimplentes\b",
    r"\bprotesto\s+indevido\b", r"\bS[úu]mula\s+385\b",
    # Telecom
    r"\bANATEL\b", r"\btelefonia\b", r"\bbanda\s+larga\b",
    r"\bfideliza[çc][ãa]o\b", r"\bportabilidade\b",
    # Servicos essenciais
    r"\bcorte\s+de\s+energia\b", r"\bconta\s+de\s+luz\b", r"\bconta\s+de\s+[áa]gua\b",
    r"\brecupera[çc][ãa]o\s+de\s+consumo\b", r"\breliga[çc][ãa]o\b",
    # Aereo
    r"\bANAC\b", r"\bvoo\s+cancelado\b", r"\bvoo\s+atrasado\b", r"\boverbooking\b",
    r"\bextravio\s+de\s+bagagem\b", r"\bconven[çc][ãa]o\s+de\s+montreal\b", r"\bno-?show\b",
    # Produto / servico
    r"\bgarantia\s+legal\b", r"\bgarantia\s+contratual\b", r"\brecall\b",
    r"\bfato\s+do\s+produto\b", r"\bfato\s+do\s+servi[çc]o\b", r"\bdefeito\b",
    r"\bassist[êe]ncia\s+t[ée]cnica\b", r"\bv[íi]cio\s+aparente\b",
    # E-commerce / digital
    r"\bdireito\s+de\s+arrependimento\b", r"\bcompra\s+online\b",
    r"\bmarketplace\b", r"\bestorno\b", r"\bchargeback\b", r"\bgolpe\b",
    # Publicidade / praticas
    r"\bpublicidade\s+abusiva\b", r"\bpropaganda\s+engan[oa]sa\b",
    r"\boferta\b", r"\bvenda\s+casada\b", r"\bpr[áa]tica\s+abusiva\b",
    # Cobranca / indebito
    r"\bcobran[çc]a\s+indevida\b", r"\brestitui[çc][ãa]o\s+em\s+dobro\b",
    r"\bd[ée]bito\s+indevido\b", r"\bdesconto\s+indevido\b",
    # Superendividamento
    r"\bm[íi]nimo\s+existencial\b", r"\brepactua[çc][ãa]o\s+de\s+d[íi]vidas\b",
    r"\bplano\s+de\s+pagamento\b",
    # Esfera administrativa / orgaos
    r"\bPROCON\b", r"\bconsumidor\.gov\b", r"\bBACEN\b", r"\bBanco\s+Central\b",
    # Conceitos CDC
    r"\binvers[ãa]o\s+do\s+[ôo]nus\b", r"\bhipossufici[êe]ncia\b",
    r"\bvulnerabilidade\b", r"\bdano\s+moral\b", r"\bfornecedor\b",
    # Consumo imobiliario
    r"\bdistrato\b", r"\batraso\s+de\s+obra\b", r"\bincorpora[çc][ãa]o\b",
    # Legislacao / sumulas / temas chave
    r"\bLei\s+8\.078\b", r"\bLei\s+14\.181\b", r"\bLei\s+9\.099\b",
    r"\bjuizado\s+especial\b", r"\bJEC\b",
    r"\bS[úu]mula\s+297\b", r"\bS[úu]mula\s+479\b", r"\bS[úu]mula\s+530\b",
    r"\bS[úu]mula\s+539\b", r"\bTema\s+929\b",
]

# Gatilho 3: commands prefixados do plugin
PLUGIN_COMMANDS = [
    "/start-consumidor",
    "/consumidor-master",
    "/triagem-consumidor",
    "/caso-consumidor",
    "/status-consumidor",
    "/revisao-final-consumidor",
    "/jurisprudencia-consumidor",
    "/calculos-consumidor",
    "/bancario",
    "/contratual",
    "/servicos-regulados",
    "/produto",
    "/superendividamento",
    "/defesa-fornecedor",
]

# Keywords gerais (fallback — protocolo cauteloso quando casa generico)
CONSUM_KEYWORDS_GENERAL = [
    r"\bconsumidor\b", r"\bfornecedor\b",
    r"\bbanco\b", r"\bfinanceira\b", r"\bloja\b", r"\boperadora\b",
    r"\bfatura\b", r"\bcobran[çc]a\b", r"\bcontrato\b",
    r"\bcompra\b", r"\bd[íi]vida\b", r"\bcart[ãa]o\b",
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
    """Verifica se existe `consumidor/cowork-state.json` no path."""
    if cowork is None:
        return False
    return (cowork / "consumidor" / "cowork-state.json").exists()


def _revisao_tecnica_enabled(cowork: Path | None) -> bool:
    """Le state.json e verifica revisao_tecnica.enabled. Default true se ausente."""
    if cowork is None:
        return True
    sf = cowork / "consumidor" / "cowork-state.json"
    if not sf.exists():
        return True
    try:
        state = json.loads(sf.read_text(encoding="utf-8"))
        return bool(state.get("revisao_tecnica", {}).get("enabled", True))
    except Exception:
        return True


def _resolve_cowork() -> Path | None:
    """Resolve COWORK root via env CONSUM_COWORK_PATH ou cwd ancestral."""
    env = os.environ.get("CONSUM_COWORK_PATH") or os.environ.get("COWORK_PATH")
    if env:
        p = Path(env)
        if (p / "consumidor" / "cowork-state.json").exists():
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
            f"[consumidor-adv-os] Bypass detectado ({bypass}). "
            "Pecas, pareceres e estrategias serao entregues SEM a "
            "Revisao Tecnica R1-R4. Use por sua conta e risco.\n"
        )
        return 0

    # Caso 2: tarefa do dominio + plugin configurado
    if is_medico and _has_medico_state(cowork):
        if not _revisao_tecnica_enabled(cowork):
            sys.stdout.write(
                "[consumidor-adv-os] Demanda juridico-consumerista detectada. "
                "Revisao Tecnica DESATIVADA na configuracao. Aciono apenas a cadeia de skills.\n"
                "Acionar skill: consumidor-master.\n"
            )
        else:
            sys.stdout.write(
                "[consumidor-adv-os] Demanda juridico-consumerista detectada. Plugin ativado.\n"
                "\n"
                "PROTOCOLO AUTOMATICO:\n"
                "1. Acionar skill `consumidor-master` (Tier 0 - sempre ativa)\n"
                "2. Aplicar Hierarquia das 4 Camadas (1-Proibicoes, 2-Protocolos, 3-Estilo, 4-Skills)\n"
                "3. Verificar as Proibicoes Absolutas, com atencao especial:\n"
                "   - P1: Selo de Validacao Legal Previa antes de qualquer producao\n"
                "   - PA-04: so afirmar relacao de consumo com destinatario final + vulnerabilidade\n"
                "   - PA-05: coerencia de polo (consumidor x fornecedor) - nunca redigir contra o cliente\n"
                "   - PA-06/07: dobro so com engano injustificavel (art. 42); negativacao checa Sumula 385\n"
                "   - PA-21: dados do cliente NUNCA no plugin (sigilo OAB + LGPD; pasta caso local)\n"
                "4. Acionar os Protocolos da Camada 2 conforme demanda\n"
                "   (P1 Selo de Validacao Legal, P2 Integridade, P3 Memoria de Caso,\n"
                "    P4 Cruzamento Judicial-Administrativo, P5 Localizacao/Rito, P6 Revisao R1-R4)\n"
                "5. Antes de entregar: Revisao Tecnica R1->R2->R3->R4 (skill `revisao-final-consumidor`)\n"
                "\n"
                "Bypass disponivel: `--no-revisao`, `--quick`, `/revisao off`.\n"
            )
        return 0

    # Caso 3: tarefa do dominio mas plugin NAO configurado
    if is_medico and not _has_medico_state(cowork):
        sys.stdout.write(
            "[consumidor-adv-os] Detectei demanda juridico-consumerista, mas o plugin "
            "ainda nao foi configurado neste diretorio.\n"
            "\n"
            "RECOMENDACAO: rode /start-consumidor para configurar (~5 min).\n"
            "Vou criar uma pasta `consumidor/` aqui com a identidade do "
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
            "[consumidor-adv-os] Tarefa juridico-consumerista detectada (sem frente especifica). "
            "Aplique protocolo padrao:\n"
            "1. Questionamento previo (sem suposicoes silenciosas - exigir dado real do caso).\n"
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
