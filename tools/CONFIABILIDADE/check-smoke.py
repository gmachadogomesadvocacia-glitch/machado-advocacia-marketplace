#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Camada 6 (confiabilidade) — SMOKE-TEST DE RUNTIME DO ENGINE.

check-engine.py (Eixo 2) confere que o encanamento EXISTE e e consistente. Este
guarda vai alem: EXECUTA o motor de estado de cada plugin (`scripts/state.py init`)
num diretorio temporario e confere que ele de fato roda e produz um cowork-state.json
VALIDO. Pega quebra de runtime (import quebrado, schema invalido, regressao no state.py)
que a checagem estrutural nao ve.

Uso:  py tools/CONFIABILIDADE/check-smoke.py
Exit 1 se o engine de qualquer plugin nao inicializar um estado valido.
"""
import subprocess, sys, json, tempfile, glob, os
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
PY = sys.executable


def main():
    plugins = sorted(glob.glob(str(REPO / "*" / "scripts" / "state.py")))
    print("== SMOKE-TEST DO ENGINE (Camada 6) ==")
    print("  plugins com engine: %d" % len(plugins))
    falhas = []
    for sp in plugins:
        plugin = Path(sp).relative_to(REPO).parts[0]
        with tempfile.TemporaryDirectory() as tmp:
            try:
                r = subprocess.run([PY, sp, "init", tmp], capture_output=True, text=True,
                                   cwd=str(REPO), timeout=60)
            except Exception as e:
                falhas.append((plugin, "exececao ao rodar: %s" % str(e)[:60])); continue
            states = glob.glob(os.path.join(tmp, "**", "cowork-state.json"), recursive=True)
            if r.returncode != 0:
                falhas.append((plugin, "init exit %d: %s" % (r.returncode, (r.stderr or r.stdout)[-80:]))); continue
            if not states:
                falhas.append((plugin, "init nao criou cowork-state.json")); continue
            try:
                json.load(open(states[0], encoding="utf-8"))
            except Exception as e:
                falhas.append((plugin, "state invalido: %s" % str(e)[:60])); continue
            print("  OK   %s" % plugin)
    if falhas:
        print("  FALHA - engine nao inicializou em:")
        for p, m in falhas:
            print("    %-28s %s" % (p, m))
        sys.exit(1)
    print("OK - engine de todos os plugins inicializa um estado valido.")
    sys.exit(0)


if __name__ == "__main__":
    main()
