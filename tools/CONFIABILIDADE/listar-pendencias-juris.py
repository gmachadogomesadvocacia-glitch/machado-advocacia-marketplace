#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Camada 5 — lista as PENDENCIAS do livro-razao (worklist da re-auditoria).
Imprime o que ainda precisa de verificacao: status VALIDAR, tribunal "?"
e itens SUPERADO (a reconfirmar). Assim a re-auditoria periodica e barata
e focada — nao re-faz o que ja esta CONFIRMADO.

Uso:  py tools/CONFIABILIDADE/listar-pendencias-juris.py
"""
import json
from pathlib import Path

LIVRO = Path(__file__).resolve().parent / "jurisprudencia.json"

def main():
    e = json.load(open(LIVRO, encoding="utf-8"))["entradas"]
    validar = [k for k, v in e.items() if v["status"] == "VALIDAR" and not k.startswith("?|")]
    amb = [k for k in e if k.startswith("?|")]
    superado = [k for k, v in e.items() if v["status"] == "SUPERADO"]
    print("== PENDENCIAS DO LIVRO-RAZAO (worklist da re-auditoria, C5) ==")
    print("VALIDAR (re-verificar enunciado/vigencia, %d):" % len(validar))
    for k in validar: print("  -", k)
    print("\nTRIBUNAL A CONFIRMAR (%d):" % len(amb))
    for k in amb: print("  -", k, " plugins:", ",".join(e[k]["plugins"]))
    print("\nSUPERADO/CANCELADO (reconfirmar que segue cancelado, %d):" % len(superado))
    for k in superado: print("  -", k, "->", e[k]["enunciado"][:80])
    print("\nTotal a tratar: %d (VALIDAR %d + ? %d + SUPERADO %d)" %
          (len(validar)+len(amb)+len(superado), len(validar), len(amb), len(superado)))

if __name__ == "__main__":
    main()
