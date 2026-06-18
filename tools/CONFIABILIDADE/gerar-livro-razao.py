#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Camada 1 — GERADOR do livro-razao de jurisprudencia.
Extrai TODAS as citacoes (Sumula/SV/Tema) das skills, deduz o tribunal pelo
contexto, aplica a curadoria (status conhecidos da auditoria) e escreve
jurisprudencia.json. O que nao esta na curadoria fica status VALIDAR.
Idempotente: re-rodar reflete o estado atual das skills.

Uso:  py tools/CONFIABILIDADE/gerar-livro-razao.py
"""
import json, re, glob, os
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
CURADORIA = HERE / "curadoria-jurisprudencia.json"
OUT = HERE / "jurisprudencia.json"

CIT = re.compile(r"(S[uú]mula\s+Vinculante\s*[\d.]*\d|\bSV\s*[\d.]*\d|S[uú]m(?:ula)?\.?\s*[\d.]*\d|\bTema\s*[\d.]*\d)", re.I)
NUM = re.compile(r"[\d.]*\d")
TRIB = re.compile(r"\b(STF|STJ|TST|TNU|CARF)\b")

def tipo_num(cit):
    s = cit.strip()
    n = NUM.search(s).group(0).replace(".", "")  # "1.051" -> "1051"
    if re.match(r"S[uú]mula\s+Vinculante|SV", s, re.I): return "SV", n
    if re.match(r"Tema", s, re.I): return "Tema", n
    return "Sum", n

def main():
    cur = json.load(open(CURADORIA, encoding="utf-8"))
    cur_e = cur["entradas"]
    # num -> set de tribunais curados (para resolver '?')
    by_num = {}
    for k in cur_e:
        t, tp, n = k.split("|")
        by_num.setdefault((tp, n), set()).add(t)

    entradas = {}
    for f in sorted(glob.glob(str(REPO / "*/skills/*/SKILL.md"))):
        plugin = Path(f).relative_to(REPO).parts[0]
        for line in open(f, encoding="utf-8", errors="replace").read().splitlines():
            cites = list(CIT.finditer(line))
            gts = set(TRIB.findall(line))
            for m in cites:
                tp, n = tipo_num(m.group(1))
                # so confia no tribunal da linha quando ha 1 tribunal E 1 citacao
                # (linha "54, 188 STF, 246..." ou "STF/STJ ..." e ambigua -> desambigua pela curadoria)
                trib = "?"
                if len(gts) == 1 and len(cites) == 1:
                    trib = next(iter(gts))
                if trib == "?":
                    cands = by_num.get((tp, n))
                    if cands and len(cands) == 1:
                        trib = next(iter(cands))
                if trib == "?" and tp == "SV":
                    trib = "STF"
                key = "%s|%s|%s" % (trib, tp, n)
                e = entradas.setdefault(key, {"tribunal": trib, "tipo": tp, "numero": n,
                    "status": "VALIDAR", "enunciado": "", "fonte": "", "data": "",
                    "plugins": set(), "ocorrencias": 0, "nota": ""})
                e["plugins"].add(plugin); e["ocorrencias"] += 1

    # aplicar curadoria
    for key, c in cur_e.items():
        if key in entradas:
            entradas[key].update({k: v for k, v in c.items() if k in ("status", "enunciado", "fonte", "data", "nota")})
            if not entradas[key].get("fonte"): entradas[key]["fonte"] = cur["fonte"]
            if not entradas[key].get("data"): entradas[key]["data"] = cur["data_auditoria"]
        else:
            # curado mas nao mais citado: registra como REMOVIDO do uso
            e = {"tribunal": key.split("|")[0], "tipo": key.split("|")[1], "numero": key.split("|")[2],
                 "status": c.get("status", "VALIDAR"), "enunciado": c.get("enunciado", ""),
                 "fonte": cur["fonte"], "data": cur["data_auditoria"],
                 "plugins": set(), "ocorrencias": 0, "nota": "curado, nao citado nas skills"}
            entradas[key] = e

    # serializar (sets -> listas ordenadas)
    out = {}
    for k in sorted(entradas):
        e = entradas[k]; e = dict(e); e["plugins"] = sorted(e["plugins"]); out[k] = e
    resumo = {"total": len(out)}
    for s in ("CONFIRMADO", "VALIDAR", "SUPERADO", "REMOVIDO"):
        resumo[s] = sum(1 for e in out.values() if e["status"] == s)
    doc = {"_doc": "Livro-razao de jurisprudencia (Camada 1). Gerado por gerar-livro-razao.py a partir das skills + curadoria. Status: CONFIRMADO (verificado, com fonte/data) | VALIDAR (extraido, a re-verificar) | SUPERADO (cancelado/superado) | REMOVIDO. As skills so devem citar o que esta aqui; check-jurisprudencia.py faz cumprir.",
           "resumo": resumo, "entradas": out}
    json.dump(doc, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("Livro-razao gerado: %d citacoes distintas" % resumo["total"])
    print("  CONFIRMADO=%d  VALIDAR=%d  SUPERADO=%d  REMOVIDO=%d" %
          (resumo["CONFIRMADO"], resumo["VALIDAR"], resumo["SUPERADO"], resumo["REMOVIDO"]))
    amb = [k for k in out if k.startswith("?|")]
    if amb: print("  tribunal a confirmar (%d): %s" % (len(amb), ", ".join(amb[:12]) + (" ..." if len(amb) > 12 else "")))

if __name__ == "__main__":
    main()
