#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Camada 4 (confiabilidade) — verificador de REGRESSOES.
Le regressoes.json e confere, sobre o conteudo do repo, que nenhum erro corrigido
reapareceu (modo proibido) e que toda correcao/garantia continua presente
(exigido / exigido_todos / exigido_conjunto).

Uso:  py tools/CONFIABILIDADE/check-regressao.py
Saida: relatorio por regra + resumo. Exit code 1 se houver QUALQUER falha
(pronto para entrar na suite de pre-publicacao — Camada 6).
"""
import json, re, sys, glob, os
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DATA = Path(__file__).resolve().parent / "regressoes.json"

def expand_braces(pattern):
    # expansao simples de UM nivel de chaves: a/{x,y}/b -> [a/x/b, a/y/b]
    m = re.search(r"\{([^}]*)\}", pattern)
    if not m:
        return [pattern]
    pre, post = pattern[:m.start()], pattern[m.end():]
    out = []
    for opt in m.group(1).split(","):
        out.extend(expand_braces(pre + opt + post))
    return out

def files_for(escopo):
    res = []
    for pat in expand_braces(escopo):
        res.extend(glob.glob(str(REPO / pat), recursive=True))
    # unicos, so arquivos
    return sorted({f for f in res if os.path.isfile(f)})

def read(f):
    return open(f, encoding="utf-8", errors="replace").read()

def matches(text, padrao):
    return re.search(padrao, text, re.IGNORECASE) is not None

def main():
    spec = json.load(open(DATA, encoding="utf-8"))
    regras = spec["regras"]
    falhas = []
    print("== VERIFICACAO DE REGRESSOES (Camada 4) ==")
    for r in regras:
        rid, modo, escopo = r["id"], r["modo"], r["escopo"]
        fs = files_for(escopo)
        padrao = r["padrao"]
        ok = True
        detalhe = ""
        if not fs:
            ok = False; detalhe = "escopo nao encontrou arquivos"
        elif modo == "proibido":
            hits = [f for f in fs if matches(read(f), padrao)]
            ok = (len(hits) == 0)
            if not ok: detalhe = "padrao PROIBIDO encontrado em: " + ", ".join(rel(h) for h in hits)
        elif modo == "exigido":
            hits = [f for f in fs if matches(read(f), padrao)]
            ok = (len(hits) >= 1)
            if not ok: detalhe = "padrao EXIGIDO ausente em todo o escopo"
        elif modo == "exigido_todos":
            faltam = [f for f in fs if not matches(read(f), padrao)]
            ok = (len(faltam) == 0)
            if not ok: detalhe = "padrao ausente em: " + ", ".join(rel(f) for f in faltam)
        elif modo == "exigido_conjunto":
            pats = padrao if isinstance(padrao, list) else [padrao]
            hits = [f for f in fs if all(matches(read(f), p) for p in pats)]
            ok = (len(hits) >= 1)
            if not ok: detalhe = "nenhum arquivo casa TODOS os padroes " + str(pats)
        else:
            ok = False; detalhe = "modo desconhecido: " + modo
        status = "PASS" if ok else "FALHA"
        print("  [%s] %-40s (%d arq, %s)%s" % (status, rid, len(fs), modo,
              "" if ok else "  -> " + detalhe))
        if not ok: falhas.append(rid)
    print("-- %d regras, %d falha(s) --" % (len(regras), len(falhas)))
    if falhas:
        print("REGRESSAO DETECTADA:", ", ".join(falhas))
        sys.exit(1)
    print("OK - nenhuma regressao.")
    sys.exit(0)

def rel(f):
    try: return str(Path(f).relative_to(REPO))
    except Exception: return f

if __name__ == "__main__":
    main()
