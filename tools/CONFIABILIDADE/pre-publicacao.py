#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Camada 6 — SUITE DE PRE-PUBLICACAO (porta unica antes de todo git push).
Roda TODAS as travas de confiabilidade e so retorna 0 se TUDO passar:
  1. estrutura: toda SKILL.md <= 11264 bytes; JSONs validos; name == pasta
  2. engine: guarda do encanamento (tools/check-engine.py — Eixo 2) [se existir]
  3. regressao: tools/CONFIABILIDADE/check-regressao.py (Camada 4)
  4. jurisprudencia: tools/CONFIABILIDADE/check-jurisprudencia.py (Camada 1)

Uso:  py tools/CONFIABILIDADE/pre-publicacao.py   (rodar ANTES de git push)
Exit 1 se qualquer trava falhar.
"""
import json, glob, os, sys, re, subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
PY = sys.executable
falhas = []

def secao(t): print("\n== %s ==" % t)

# 1. ESTRUTURA
secao("1. ESTRUTURA (tamanho / JSON / name==pasta)")
over = []
for f in glob.glob(str(REPO / "*/skills/*/SKILL.md")):
    if os.path.getsize(f) > 11264: over.append(str(Path(f).relative_to(REPO)))
print("  SKILL.md > 11264 bytes: %d" % len(over))
if over: falhas.append("tamanho"); [print("    OVER:", o) for o in over]

badjson = []
for f in glob.glob(str(REPO / "**/*.json"), recursive=True) + glob.glob(str(REPO / "**/*.json.tpl"), recursive=True):
    try: json.load(open(f, encoding="utf-8"))
    except Exception as e: badjson.append((str(Path(f).relative_to(REPO)), str(e)[:60]))
print("  JSON invalidos: %d" % len(badjson))
if badjson: falhas.append("json"); [print("    BAD:", b[0], b[1]) for b in badjson]

mism = []
for d in glob.glob(str(REPO / "*/skills/*/")):
    name = Path(d).name; sk = os.path.join(d, "SKILL.md")
    if os.path.isfile(sk):
        t = open(sk, encoding="utf-8", errors="replace").read()
        if not re.search(r"(?m)^name:\s*%s\s*$" % re.escape(name), t):
            mism.append(name)
print("  name != pasta: %d" % len(mism))
if mism: falhas.append("name"); print("    MISMATCH:", ", ".join(mism))

# 2-4. SCRIPTS
def roda(rotulo, rel):
    p = REPO / rel
    if not p.exists():
        print("  (pulado — %s nao existe)" % rel); return
    r = subprocess.run([PY, str(p)], cwd=str(REPO), capture_output=True, text=True)
    print((r.stdout or "").rstrip()[-400:])
    if r.returncode != 0:
        falhas.append(rotulo)
        if r.stderr: print("  stderr:", r.stderr.strip()[-200:])

secao("2. ENGINE (guarda do encanamento — Eixo 2)")
roda("engine", "tools/check-engine.py")
secao("3. REGRESSAO (Camada 4)")
roda("regressao", "tools/CONFIABILIDADE/check-regressao.py")
secao("4. JURISPRUDENCIA (Camada 1)")
roda("jurisprudencia", "tools/CONFIABILIDADE/check-jurisprudencia.py")

print("\n" + "=" * 48)
if falhas:
    print("PRE-PUBLICACAO REPROVADA — travas com falha: %s" % ", ".join(falhas))
    print("NAO PUBLICAR ate corrigir.")
    sys.exit(1)
print("PRE-PUBLICACAO OK — todas as travas passaram. Pode publicar.")
sys.exit(0)
