#!/usr/bin/env python3
"""
Hook UserPromptSubmit do plugin Familia e Sucessoes Adv-OS.

Logica (ativacao automatica por contexto):
1. Le o prompt via stdin (JSON padrao Claude Code hooks).
2. Detecta bypass explicito: flags `--no-revisao`, `--quick`, `--no-r1r4`, `/revisao off`.
3. Detecta GATILHO de DOMINIO via keywords (3 niveis):
   - Gatilho 1: prompt contem palavras fortes do dominio de familia/sucessoes
   - Gatilho 2: keywords fortes do dominio
   - Gatilho 3: comandos `/start-familia`, `/familia-master`, etc.
4. Se gatilho dispara:
   - Verifica se `familia/cowork-state.json` existe no path atual
   - SIM: injeta protocolo Revisao Tecnica R1-R4 + aponta para skill `familia-master`
   - NAO: sugere `/start-familia` ao usuario (mas nao bloqueia)
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
# lexico do DIREITO DE FAMILIA E SUCESSOES. Mantidos para preservar a logica do hook.

# Gatilho 1: frases fortes do dominio de familia/sucessoes (case insensitive)
TRIGGER_MEDICO = [
    r"\bdireito\s+de\s+fam[íi]lia\b",
    r"\bdireito\s+das\s+sucess[õo]es\b",
    r"\bdiv[óo]rcio\b", r"\bseparac[ãa]o\s+(judicial|de\s+corpos|de\s+fato)\b",
    r"\bdissolu[çc][ãa]o\s+de\s+uni[ãa]o\s+est[áa]vel\b", r"\buni[ãa]o\s+est[áa]vel\b",
    r"\bguarda\s+(compartilhada|unilateral|de\s+filho)\b",
    r"\bpens[ãa]o\s+aliment[íi]cia\b", r"\balimentos\s+(gravid|provis[óo]rios|definitivos)\b",
    r"\bregime\s+de\s+bens\b",
    r"\bpartilha\s+de\s+bens\b", r"\bmea[çc][ãa]o\b",
    r"\binvent[áa]rio\b", r"\barrolamento\s+(sumario|comum)?\b",
    r"\bheran[çc]a\b", r"\bespólio\b", r"\bsucess[ãa]o\s+(legitima|testament[áa]ria)\b",
    r"\btestamento\b", r"\bleg[íi]tima\b", r"\bcola[çc][ãa]o\b", r"\bsonegados?\b",
    r"\binterdi[çc][ãa]o\b", r"\bcuratela\b", r"\btomada\s+de\s+decis[ãa]o\s+apoiada\b",
    r"\baliena[çc][ãa]o\s+parental\b",
    r"\bplanejamento\s+sucess[óo]rio\b", r"\bholding\s+familiar\b",
    r"\breconhecimento\s+de\s+paternidade\b", r"\binvestiga[çc][ãa]o\s+de\s+paternidade\b",
]

# Gatilho 2: keywords fortes das frentes de familia e sucessoes
DOMAIN_KEYWORDS = [
    # Casamento / dissolucao
    r"\bcasamento\b", r"\bnubentes?\b", r"\bcônjuge\b", r"\bconvivente\b",
    r"\bcomunh[ãa]o\s+parcial\b", r"\bcomunh[ãa]o\s+universal\b",
    r"\bsepara[çc][ãa]o\s+total\b", r"\bparticipa[çc][ãa]o\s+final\s+nos\s+aquestos\b",
    r"\bpacto\s+antenupcial\b", r"\baquestos?\b",
    # Filhos / convivencia
    r"\bguarda\b", r"\bvisita[çc][ãa]o?\b", r"\bconviv[êe]ncia\s+familiar\b",
    r"\bregula[çc][ãa]o\s+de\s+visitas\b", r"\bmelhor\s+interesse\s+da\s+crian[çc]a\b",
    r"\bbusca\s+e\s+apreens[ãa]o\s+de\s+menor\b", r"\bECA\b",
    r"\bestatuto\s+da\s+crian[çc]a\b", r"\boitiva\s+da\s+crian[çc]a\b",
    r"\bestudo\s+psicossocial\b", r"\bconselho\s+tutelar\b",
    # Alimentos
    r"\balimentos\b", r"\bbin[ôo]mio\s+(necessidade|possibilidade)\b",
    r"\bexonera[çc][ãa]o\s+de\s+alimentos\b", r"\brevis[ãa]o\s+de\s+alimentos\b",
    r"\bofferta\s+de\s+alimentos\b", r"\bpris[ãa]o\s+(civil|do\s+devedor\s+de\s+alimentos)\b",
    r"\bdesconto\s+em\s+folha\b", r"\brito\s+da\s+penhora\b",
    # Patrimonio / partilha
    r"\bpartilha\b", r"\bsobrepartilha\b", r"\bbem\s+(comum|particular|exclusivo)\b",
    r"\bbenfeitorias?\b", r"\bdoa[çc][ãa]o\b", r"\busufruto\b", r"\bnua[\s-]?propriedade\b",
    # Sucessoes
    r"\babertura\s+da\s+sucess[ãa]o\b", r"\bsais[ie]na\b", r"\bde\s+cujus\b",
    r"\bherdeir[oa]s?\b", r"\bmeeir[oa]\b", r"\blegat[áa]ri[oa]s?\b",
    r"\binventariante\b", r"\bcessao\s+de\s+direitos\s+heredit[áa]rios\b",
    r"\bpartilha\s+em\s+vida\b", r"\bcompanheir[oa]\b",
    r"\bordem\s+de\s+voca[çc][ãa]o\s+heredit[áa]ria\b",
    r"\bdeserda[çc][ãa]o\b", r"\bindignidade\b",
    r"\bcl[áa]usula\s+de\s+(inalienabilidade|impenhorabilidade|incomunicabilidade)\b",
    # Incapazes / vulneraveis
    r"\bcuratela\b", r"\binterdi[çc][ãa]o\b", r"\bincapaz\b", r"\bcurador\b",
    r"\bestatuto\s+da\s+pessoa\s+com\s+defici[êe]ncia\b", r"\bestatuto\s+do\s+idoso\b",
    # Filiacao / parentesco
    r"\bpaternidade\b", r"\bmaternidade\b", r"\bfilia[çc][ãa]o\b",
    r"\bexame\s+de\s+DNA\b", r"\bsocioafetiv[oa]\b", r"\bmultiparentalidade\b",
    r"\bado[çc][ãa]o\b", r"\bregistro\s+civil\b",
    # Planejamento sucessorio / consultivo
    r"\bplanejamento\s+patrimonial\b", r"\bholding\b",
    r"\bdoa[çc][ãa]o\s+com\s+(usufruto|reserva)\b", r"\bITCMD\b",
    r"\bcontrato\s+de\s+convivência\b", r"\btestamento\s+(p[úu]blico|cerrado|particular)\b",
    # Violencia domestica
    r"\bviol[êe]ncia\s+dom[ée]stica\b", r"\bLei\s+Maria\s+da\s+Penha\b",
    r"\bLei\s+11\.?340\b", r"\bmedida\s+protetiva\b",
    # Esfera extrajudicial / cartorio
    r"\bdiv[óo]rcio\s+extrajudicial\b", r"\binvent[áa]rio\s+extrajudicial\b",
    r"\bescritura\s+p[úu]blica\b", r"\btabeli[ãa]o\b", r"\bResolu[çc][ãa]o\s+35\b",
    # Legislacao chave
    r"\bC[óo]digo\s+Civil\b", r"\bCC/2002\b", r"\bLivro\s+IV\b", r"\bLivro\s+V\b",
    r"\bLei\s+do\s+Div[óo]rcio\b", r"\bLei\s+11\.?441\b", r"\bLei\s+13\.?058\b",
    r"\bart\.?\s*1\.?5\d\d\b", r"\bart\.?\s*1\.?7\d\d\b", r"\bart\.?\s*1\.?8\d\d\b",
]

# Gatilho 3: commands prefixados do plugin
PLUGIN_COMMANDS = [
    "/start-familia",
    "/familia-master",
    "/triagem",
    "/caso-familia",
    "/divorcio",
    "/alimentos-guarda",
    "/uniao-estavel",
    "/inventario",
    "/interdicao",
    "/planejamento-sucessorio",
]

# Keywords gerais (fallback — protocolo cauteloso quando casa generico)
CONSUM_KEYWORDS_GENERAL = [
    r"\bfam[íi]lia\b", r"\bsucess[ãa]o\b", r"\bsucess[õo]es\b",
    r"\bc[ôo]njuge\b", r"\besposa?\b", r"\bmarido\b", r"\bcompanheir[oa]\b",
    r"\bfilh[oa]s?\b", r"\bpais\b", r"\bgenitor(a|es)?\b",
    r"\bheran[çc]a\b", r"\bbens\b", r"\bpatrim[ôo]nio\b",
    r"\bguarda\b", r"\balimentos\b", r"\bpartilha\b",
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
    """Verifica se existe `familia/cowork-state.json` no path."""
    if cowork is None:
        return False
    return (cowork / "familia" / "cowork-state.json").exists()


def _revisao_tecnica_enabled(cowork: Path | None) -> bool:
    """Le state.json e verifica revisao_tecnica.enabled. Default true se ausente."""
    if cowork is None:
        return True
    sf = cowork / "familia" / "cowork-state.json"
    if not sf.exists():
        return True
    try:
        state = json.loads(sf.read_text(encoding="utf-8"))
        return bool(state.get("revisao_tecnica", {}).get("enabled", True))
    except Exception:
        return True


def _resolve_cowork() -> Path | None:
    """Resolve COWORK root via env FAM_COWORK_PATH ou cwd ancestral."""
    env = os.environ.get("FAM_COWORK_PATH") or os.environ.get("COWORK_PATH")
    if env:
        p = Path(env)
        if (p / "familia" / "cowork-state.json").exists():
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
            f"[familia-sucessoes-adv-os] Bypass detectado ({bypass}). "
            "Pecas, pareceres e estrategias serao entregues SEM a "
            "Revisao Tecnica R1-R4. Use por sua conta e risco.\n"
        )
        return 0

    # Caso 2: tarefa do dominio + plugin configurado
    if is_medico and _has_medico_state(cowork):
        if not _revisao_tecnica_enabled(cowork):
            sys.stdout.write(
                "[familia-sucessoes-adv-os] Demanda de familia/sucessoes detectada. "
                "Revisao Tecnica DESATIVADA na configuracao. Aciono apenas a cadeia de skills.\n"
                "Acionar skill: familia-master.\n"
            )
        else:
            sys.stdout.write(
                "[familia-sucessoes-adv-os] Demanda de familia/sucessoes detectada. Plugin ativado.\n"
                "\n"
                "PROTOCOLO AUTOMATICO:\n"
                "1. Acionar skill `familia-master` (Tier 0 - sempre ativa)\n"
                "2. Aplicar Hierarquia das 4 Camadas (1-Proibicoes, 2-Protocolos, 3-Estilo, 4-Skills)\n"
                "3. Verificar as Proibicoes Absolutas, com atencao especial:\n"
                "   - P1: Validacao de Norma Vigente (CC/2002 + CPC/2015 + lei especial) antes de qualquer producao\n"
                "   - Coerencia de polo: requerente x requerido / inventariante x herdeiro - nunca redigir contra o cliente\n"
                "   - Nunca inventar jurisprudencia (STJ/TJ); marcar [VERIFICAR] e acionar jurisprudencia-familia\n"
                "   - Sigilo + LGPD: dados do nucleo familiar NUNCA no plugin (sigilo OAB + LGPD; pasta caso local)\n"
                "   - Sensibilidade humana: casos de familia envolvem luto, filhos e vulneraveis - calibrar o tom\n"
                "4. Acionar os Protocolos da Camada 2 conforme demanda\n"
                "   (P1 Validacao de Norma Vigente, P2 Integridade Documental, P3 Memoria de Caso,\n"
                "    P4 Cruzamento Judicial-Extrajudicial, P5 Localizacao/Foro de Familia, P6 Revisao R1-R4)\n"
                "5. Antes de entregar: Revisao Tecnica R1->R2->R3->R4 (skill `revisao-final-familia`)\n"
                "\n"
                "Bypass disponivel: `--no-revisao`, `--quick`, `/revisao off`.\n"
            )
        return 0

    # Caso 3: tarefa do dominio mas plugin NAO configurado
    if is_medico and not _has_medico_state(cowork):
        sys.stdout.write(
            "[familia-sucessoes-adv-os] Detectei demanda de familia/sucessoes, mas o plugin "
            "ainda nao foi configurado neste diretorio.\n"
            "\n"
            "RECOMENDACAO: rode /start-familia para configurar (~5 min).\n"
            "Vou criar uma pasta `familia/` aqui com a identidade do "
            "advogado/escritorio, OAB, cidade/UF, area de foco (familia / sucessoes / planejamento), "
            "tom de voz e configuracao das skills.\n"
            "\n"
            "Caso queira prosseguir SEM configurar, trabalho em modo fallback generico "
            "(persona neutra, qualidade reduzida). Apenas avise.\n"
        )
        return 0

    # Caso 4: tarefa do dominio geral - protocolo cauteloso
    if is_medico_other:
        sys.stdout.write(
            "[familia-sucessoes-adv-os] Tarefa de familia/sucessoes detectada (sem frente especifica). "
            "Aplique protocolo padrao:\n"
            "1. Questionamento previo (sem suposicoes silenciosas - exigir dado real do caso: polo, "
            "regime de bens, filhos menores/incapazes, patrimonio).\n"
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
