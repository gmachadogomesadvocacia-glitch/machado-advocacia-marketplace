#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
datajud_client.py — cliente da API Publica do DataJud (CNJ) para jurimetria.

Le a CAPA + MOVIMENTOS de um processo por numero CNJ (dado por processo, gratuito).
NAO traz quantum/merito (lacuna estrutural do DataJud — isso vem do CASO.md).

- Chave publica buscada DINAMICAMENTE na wiki do CNJ (ela rotaciona); fallback embutido.
- Roteia o tribunal automaticamente pelo numero CNJ (segmento J + codigo TR).
- Backoff em 429/timeout (a chave publica e compartilhada e vem throttled).
- Saida UTF-8 (corrige o encoding do console Windows).

Uso CLI:
  py datajud_client.py <numero-cnj>
  py datajud_client.py <numero-cnj-so-digitos> --tribunal api_publica_trt1
"""
import json, re, sys, io, time, datetime, urllib.request, urllib.error

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

WIKI_KEY_URL = "https://datajud-wiki.cnj.jus.br/api-publica/acesso/"
BASE = "https://api-publica.datajud.cnj.jus.br/%s/_search"
CHAVE_FALLBACK = "cDZHYzlZa0JadVREZDJCendQbXY6SkJlTzNjLV9TRENyQk1RdnFKZGRQdw=="

# Mapa (segmento J, codigo TR do numero CNJ) -> alias DataJud. Foco no escritorio;
# extensivel. O numero CNJ e NNNNNNN-DD.AAAA.J.TR.OOOO (J=segmento, TR=tribunal).
ALIAS = {
    ("8", "19"): "api_publica_tjrj",   # TJRJ (estadual RJ)
    ("5", "01"): "api_publica_trt1",   # TRT-1 (trabalhista RJ)
    ("4", "02"): "api_publica_trf2",   # TRF2 / JF 2a Regiao (RJ-ES)
    ("8", "26"): "api_publica_tjsp",   # exemplos p/ ampliar
    ("5", "02"): "api_publica_trt2",
}

_CHAVE_CACHE = None


def so_digitos(num):
    return re.sub(r"\D", "", num)


def alias_do_numero(num, override=None):
    if override:
        return override if override.startswith("api_publica_") else "api_publica_" + override
    d = so_digitos(num)
    if len(d) != 20:
        return None
    j, tr = d[13], d[14:16]
    return ALIAS.get((j, tr))


def get_chave():
    """Busca a chave publica vigente na wiki do CNJ; fallback embutido."""
    global _CHAVE_CACHE
    if _CHAVE_CACHE:
        return _CHAVE_CACHE
    try:
        req = urllib.request.Request(WIKI_KEY_URL, headers={"User-Agent": "jurimetria-adv-os/0.1"})
        with urllib.request.urlopen(req, timeout=20) as r:
            html = r.read().decode("utf-8", "replace")
        # a chave aparece como "APIKey <base64...>" ou num bloco de codigo
        m = re.search(r"APIKey\s+([A-Za-z0-9+/=]{60,})", html) or \
            re.search(r"([A-Za-z0-9+/]{80,}==)", html)
        if m:
            _CHAVE_CACHE = m.group(1)
            return _CHAVE_CACHE
    except Exception:
        pass
    _CHAVE_CACHE = CHAVE_FALLBACK
    return _CHAVE_CACHE


def consultar(numero, override=None, max_tentativas=5):
    """Retorna o _source do processo (capa + movimentos) ou None se nao achar."""
    alias = alias_do_numero(numero, override)
    if not alias:
        raise ValueError("nao consegui rotear o tribunal do numero %r — passe --tribunal" % numero)
    url = BASE % alias
    body = json.dumps({"query": {"match": {"numeroProcesso": so_digitos(numero)}}}).encode()
    chave = get_chave()
    esperas = [0, 3, 8, 15, 25][:max_tentativas]
    ultimo = None
    for i, w in enumerate(esperas):
        if w:
            time.sleep(w)
        req = urllib.request.Request(url, data=body, method="POST")
        req.add_header("Authorization", "APIKey " + chave)
        req.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(req, timeout=45) as r:
                d = json.load(r)
            hits = d.get("hits", {}).get("hits", [])
            return hits[0]["_source"] if hits else None
        except urllib.error.HTTPError as e:
            ultimo = "HTTP %s" % e.code
            if e.code != 429:
                raise
        except Exception as e:
            ultimo = type(e).__name__
    raise RuntimeError("esgotou %d tentativas (alias %s): %s" % (len(esperas), alias, ultimo))


def _data(s):
    """'20241105084706' -> date; ISO '2024-11-05T..' -> date."""
    if not s:
        return None
    dig = re.sub(r"\D", "", str(s))[:8]
    try:
        return datetime.date(int(dig[0:4]), int(dig[4:6]), int(dig[6:8]))
    except Exception:
        return None


def resumo(src):
    """Extrai os campos jurimetricos de duracao a partir do _source do DataJud."""
    movs = src.get("movimentos", []) or []
    datas = sorted(d for d in (_data(m.get("dataHora")) for m in movs) if d)
    aj = _data(src.get("dataAjuizamento"))
    ult = datas[-1] if datas else None
    dur = (ult - aj).days if (aj and ult) else None
    ass = src.get("assuntos", []) or []
    return {
        "numero": src.get("numeroProcesso"),
        "grau": src.get("grau"),
        "classe": (src.get("classe") or {}).get("nome"),
        "assunto": ass[0].get("nome") if ass else None,
        "orgao": (src.get("orgaoJulgador") or {}).get("nome"),
        "ajuizamento": aj.isoformat() if aj else None,
        "ultimo_movimento": ult.isoformat() if ult else None,
        "duracao_dias": dur,
        "n_movimentos": len(movs),
    }


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    override = None
    if "--tribunal" in sys.argv:
        override = sys.argv[sys.argv.index("--tribunal") + 1]
    if not args:
        print("uso: py datajud_client.py <numero-processo> [--tribunal api_publica_xxx]")
        sys.exit(2)
    numero = args[0]
    print("consultando", numero, "(alias:", alias_do_numero(numero, override), ")...")
    src = consultar(numero, override)
    if not src:
        print("  processo nao encontrado no DataJud (pode nao estar indexado ou em segredo).")
        sys.exit(0)
    r = resumo(src)
    print(json.dumps(r, ensure_ascii=False, indent=2))
    if r["duracao_dias"] is not None:
        print("  -> duracao: %d dias (~%.1f meses), %d movimentos" %
              (r["duracao_dias"], r["duracao_dias"] / 30.44, r["n_movimentos"]))


if __name__ == "__main__":
    main()
