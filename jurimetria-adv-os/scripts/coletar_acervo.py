#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
coletar_acervo.py — Modulo C (portfolio proprio) do plugin de jurimetria.

Varre TODOS os CASO.md sob uma raiz, extrai o bloco jurimetrico (ler_caso) e
consolida um DATASET + estatisticas descritivas do escritorio. Flagra os casos
SEM bloco (para preencher). Opcional: --datajud enriquece cada caso com a duracao.

Uso:
  py coletar_acervo.py "<raiz-do-acervo>/Casos-Ativos"
  py coletar_acervo.py <raiz> --datajud
  py coletar_acervo.py <raiz> --json saida.json

DISCIPLINA (freios estatisticos): isto e DESCRITIVO do proprio acervo, nao
preditivo. Todo numero vem com o N. Amostra pequena => tratar como qualitativo.
Nenhum dado sai daqui sem passar pelo check-sigilo (LGPD) — o numero do processo
e publico, mas o nome do cliente NAO entra no bloco.
"""
import os, sys, io, json, glob
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ler_caso

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

N_MINIMO_QUANT = 5  # abaixo disto, so qualitativo (nao reportar media como se fosse robusta)


def coletar(raiz, com_datajud=False):
    arquivos = glob.glob(os.path.join(raiz, "**", "CASO.md"), recursive=True)
    com_bloco, sem_bloco = [], []
    for f in arquivos:
        try:
            texto = open(f, encoding="utf-8", errors="replace").read()
        except Exception:
            continue
        d = ler_caso.parse_bloco(texto)
        if d is None:
            sem_bloco.append(f)
            continue
        d["_arquivo"] = os.path.relpath(f, raiz)
        d["percentual_exito"] = ler_caso.calcular_exito(d)
        if com_datajud:
            d.update(ler_caso.enrich_datajud(d))
        com_bloco.append(d)
    return com_bloco, sem_bloco, len(arquivos)


def _num(v):
    return v if isinstance(v, (int, float)) else None


def estatisticas(casos):
    n = len(casos)
    por_area = Counter(c.get("area") for c in casos if c.get("area"))
    por_tribunal = Counter(c.get("tribunal") for c in casos if c.get("tribunal"))
    por_status = Counter(c.get("status") for c in casos if c.get("status"))
    fechados = [c for c in casos if c.get("resultado")]
    por_resultado = Counter(c.get("resultado") for c in fechados)
    quant = [_num(c.get("quantum_obtido")) for c in casos]
    quant = [q for q in quant if q is not None]
    exitos = [_num(c.get("percentual_exito")) for c in casos]
    exitos = [e for e in exitos if e is not None]
    return {
        "N_total_com_bloco": n,
        "por_area": dict(por_area),
        "por_tribunal": dict(por_tribunal),
        "por_status": dict(por_status),
        "por_resultado (fechados)": dict(por_resultado),
        "quantum_obtido": {
            "N": len(quant),
            "soma": round(sum(quant), 2) if quant else 0,
            "media": (round(sum(quant) / len(quant), 2) if len(quant) >= N_MINIMO_QUANT else None),
            "nota": None if len(quant) >= N_MINIMO_QUANT else "N<%d: use so qualitativamente" % N_MINIMO_QUANT,
        },
        "taxa_exito_media": (round(sum(exitos) / len(exitos), 3)
                             if len(exitos) >= N_MINIMO_QUANT else None),
    }


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print("uso: py coletar_acervo.py <raiz-do-acervo> [--datajud] [--json saida.json]")
        sys.exit(2)
    raiz = args[0]
    com_dj = "--datajud" in sys.argv
    casos, sem_bloco, total = coletar(raiz, com_dj)
    stats = estatisticas(casos)
    print("== COLETA JURIMETRICA DO ACERVO ==")
    print("  raiz:", raiz)
    print("  CASO.md encontrados:", total, "| com bloco:", len(casos), "| SEM bloco:", len(sem_bloco))
    print()
    print(json.dumps(stats, ensure_ascii=False, indent=2))
    if sem_bloco:
        print("\n  CASOS SEM BLOCO JURIMETRICO (preencher — schema em caso-md-jurimetrico.md):")
        for f in sem_bloco[:30]:
            print("   -", os.path.relpath(f, raiz))
        if len(sem_bloco) > 30:
            print("   ... (+%d)" % (len(sem_bloco) - 30))
    if "--json" in sys.argv:
        saida = sys.argv[sys.argv.index("--json") + 1]
        json.dump({"casos": casos, "estatisticas": stats, "sem_bloco": len(sem_bloco)},
                  open(saida, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print("\n  dataset salvo em", saida)


if __name__ == "__main__":
    main()
