#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Camada 1 — VERIFICADOR do livro-razao.
Garante que TODA citacao (Sumula/SV/Tema) presente nas skills existe no
jurisprudencia.json (livro-razao). Citacao orfa (fora do livro) = FALHA: tem
de ser registrada e verificada antes de publicar. Usar uma citacao REMOVIDO
tambem falha. Reporta a distribuicao de status.

Uso:  py tools/CONFIABILIDADE/check-jurisprudencia.py
Exit 1 se houver citacao orfa ou REMOVIDO em uso (entra na suite C6).
NOTA: rode o gerador (gerar-livro-razao.py) e cure o livro antes; o check roda
sobre o livro COMMITADO, pegando citacoes novas que ninguem registrou.
"""
import json, re, glob, sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
LIVRO = Path(__file__).resolve().parent / "jurisprudencia.json"
CIT = re.compile(r"(S[uú]mula\s+Vinculante\s*\d+|\bSV\s*\d+|S[uú]m(?:ula)?\.?\s*\d+|\bTema\s*\d+)", re.I)
NUM = re.compile(r"\d+")

def tipo_num(cit):
    s = cit.strip(); n = NUM.search(s).group(0)
    if re.match(r"S[uú]mula\s+Vinculante|SV", s, re.I): return "SV", n
    if re.match(r"Tema", s, re.I): return "Tema", n
    return "Sum", n

def main():
    livro = json.load(open(LIVRO, encoding="utf-8"))["entradas"]
    # indice (tipo,num) -> lista de status
    idx = {}
    for k, e in livro.items():
        idx.setdefault((e["tipo"], e["numero"]), []).append(e["status"])

    orfas = {}; removido = {}; cont = {"CONFIRMADO": 0, "VALIDAR": 0, "SUPERADO": 0, "REMOVIDO": 0, "orfa": 0}
    for f in sorted(glob.glob(str(REPO / "*/skills/*/SKILL.md"))):
        rel = str(Path(f).relative_to(REPO))
        for line in open(f, encoding="utf-8", errors="replace").read().splitlines():
            for m in CIT.finditer(line):
                tp, n = tipo_num(m.group(1))
                st = idx.get((tp, n))
                if not st:
                    orfas.setdefault((tp, n), set()).add(rel); cont["orfa"] += 1
                else:
                    # melhor status disponivel
                    best = "CONFIRMADO" if "CONFIRMADO" in st else ("VALIDAR" if "VALIDAR" in st else st[0])
                    cont[best] = cont.get(best, 0) + 1
                    if all(s == "REMOVIDO" for s in st):
                        removido.setdefault((tp, n), set()).add(rel)

    print("== VERIFICACAO DO LIVRO-RAZAO (Camada 1) ==")
    tot = sum(v for k, v in cont.items() if k != "orfa")
    print("  citacoes nas skills: %d (CONFIRMADO=%d VALIDAR=%d SUPERADO=%d) | orfas=%d"
          % (tot, cont["CONFIRMADO"], cont["VALIDAR"], cont["SUPERADO"], cont["orfa"]))
    falhou = False
    if orfas:
        falhou = True
        print("  FALHA - citacoes ORFAS (fora do livro-razao; registrar+verificar):")
        for (tp, n), fs in sorted(orfas.items()):
            print("    %s %s  em %s" % (tp, n, ", ".join(sorted(fs))[:120]))
    if removido:
        falhou = True
        print("  FALHA - citacao REMOVIDO ainda em uso:")
        for (tp, n), fs in sorted(removido.items()):
            print("    %s %s  em %s" % (tp, n, ", ".join(sorted(fs))[:120]))
    if cont["SUPERADO"]:
        print("  AVISO - %d citacao(oes) de tema/sumula SUPERADO em uso (conferir se o texto diz CANCELADO/SUPERADO)." % cont["SUPERADO"])
    if falhou:
        sys.exit(1)
    print("OK - toda citacao esta no livro-razao.")
    sys.exit(0)

if __name__ == "__main__":
    main()
