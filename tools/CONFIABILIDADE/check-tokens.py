#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Camada 6 (confiabilidade) — GUARDA DE TOKENS DE PERSONA/TEMPLATE.

Os plugins usam tokens Mustache ({{ADVOGADO_NOME}}, {{OAB_NUMERO}}, {{CIDADE}}...)
resolvidos em runtime. Dois modos de falha que este guarda fecha:

  (A) DRIFT/TYPO no repo: alguem escreve {{OAB_NUM}} em vez de {{OAB_NUMERO}} num
      template/skill — o token nunca resolve e sai literal na peca. Defesa: todo
      token usado no repo TEM de estar no registro canonico (tokens-registry.json).
      Token novo = registrar de proposito (forca revisao). Exit 1 se houver orfao.

  (B) VAZAMENTO na entrega: uma peca final (.txt/.docx convertido p/ texto) sai com
      {{QUALQUER_COISA}} literal. Defesa: modo --saida <arquivo|pasta> exige ZERO
      tokens. As entregas vivem no acervo (fora deste repo), entao este modo recebe
      um caminho; use-o na revisao final antes de protocolar.

Uso:
  py tools/CONFIABILIDADE/check-tokens.py            # modo A (repo) — entra na suite C6
  py tools/CONFIABILIDADE/check-tokens.py --init     # (re)gera o registro a partir do repo
  py tools/CONFIABILIDADE/check-tokens.py --saida "C:/.../peca.txt"   # modo B (vazamento)
"""
import json, re, glob, sys, os
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
REG = HERE / "tokens-registry.json"

TOKEN = re.compile(r"\{\{\s*([#/^]?)\s*([^}]+?)\s*\}\}")
# placeholders de documentacao que NAO sao tokens de runtime (reticencias, formato de data)
DOC_PLACEHOLDERS = {"...", "AAAA-MM-DD"}
EXTS = ("*.md", "*.tpl", "*.json")


def repo_files():
    fs = []
    for pat in EXTS:
        fs += glob.glob(str(REPO / "**" / pat), recursive=True)
    # so plugins (ignora tools/ e arquivos de raiz do repo de governanca)
    return sorted(f for f in fs if "tools" + os.sep not in str(Path(f).relative_to(REPO)))


def tokens_in(text):
    """tokens base (sem marcador de secao #/^//), com contagem."""
    out = {}
    for m in TOKEN.finditer(text):
        name = m.group(2).strip()
        if name in DOC_PLACEHOLDERS:
            continue
        out[name] = out.get(name, 0) + 1
    return out


def scan_repo():
    counts = {}
    where = {}
    for f in repo_files():
        rel = str(Path(f).relative_to(REPO))
        for name, c in tokens_in(open(f, encoding="utf-8", errors="replace").read()).items():
            counts[name] = counts.get(name, 0) + c
            where.setdefault(name, set()).add(rel)
    return counts, where


def lev1(a, b):
    """True se a e b distam <= 1 edicao (deteccao de typo)."""
    if a == b:
        return False
    if abs(len(a) - len(b)) > 1:
        return False
    # substituicao
    if len(a) == len(b):
        return sum(x != y for x, y in zip(a, b)) == 1
    # insercao/remocao
    lo, hi = (a, b) if len(a) < len(b) else (b, a)
    i = j = 0
    diff = 0
    while i < len(lo) and j < len(hi):
        if lo[i] == hi[j]:
            i += 1; j += 1
        else:
            diff += 1; j += 1
            if diff > 1:
                return False
    return True


def init():
    counts, _ = scan_repo()
    reg = {
        "_doc": "Registro CANONICO de tokens de persona/template (Camada 6). Todo {{token}} usado "
                "nos plugins tem de estar aqui; check-tokens.py reprova orfaos (typo/drift). "
                "Placeholders de doc ('...', 'AAAA-MM-DD') sao ignorados pelo guarda. "
                "Para adicionar um token novo: rode --init (revisa o diff) ou edite a lista a mao.",
        "tokens": sorted(counts.keys()),
    }
    json.dump(reg, open(REG, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("Registro gerado: %d tokens canonicos -> %s" % (len(reg["tokens"]), REG.name))


def verify():
    if not REG.exists():
        print("FALHA - registro ausente; rode: py tools/CONFIABILIDADE/check-tokens.py --init")
        sys.exit(1)
    canon = set(json.load(open(REG, encoding="utf-8"))["tokens"])
    counts, where = scan_repo()
    print("== GUARDA DE TOKENS (Camada 6) ==")
    print("  tokens distintos no repo: %d | registro canonico: %d" % (len(counts), len(canon)))
    orfaos = sorted(set(counts) - canon)
    falhou = False
    if orfaos:
        falhou = True
        print("  FALHA - token(s) FORA do registro (typo/drift; registrar de proposito):")
        for t in orfaos:
            print("    {{%s}}  (%dx)  em %s" % (t, counts[t], ", ".join(sorted(where[t]))[:120]))
    # advisory: typo provavel (token raro a 1 edicao de um token frequente)
    suspeitos = []
    for t, c in counts.items():
        if c <= 2:
            for u, cu in counts.items():
                if cu >= 5 and lev1(t, u):
                    suspeitos.append((t, c, u, cu))
    if suspeitos:
        print("  AVISO - possiveis typos (token raro parecido com um frequente):")
        for t, c, u, cu in suspeitos:
            print("    {{%s}} (%dx) ~ {{%s}} (%dx)" % (t, c, u, cu))
    if falhou:
        sys.exit(1)
    print("OK - todo token usado esta no registro canonico.")
    sys.exit(0)


def saida(path):
    p = Path(path)
    alvos = []
    if p.is_dir():
        for ext in ("*.txt", "*.md"):
            alvos += glob.glob(str(p / "**" / ext), recursive=True)
    elif p.is_file():
        alvos = [str(p)]
    else:
        print("FALHA - caminho inexistente:", path); sys.exit(1)
    print("== GUARDA DE VAZAMENTO DE TOKENS (entrega) ==")
    print("  arquivos verificados: %d" % len(alvos))
    vaz = {}
    for f in alvos:
        t = tokens_in(open(f, encoding="utf-8", errors="replace").read())
        if t:
            vaz[f] = t
    if vaz:
        print("  FALHA - token(s) NAO RESOLVIDO(S) na entrega (peca nao pode ir assim):")
        for f, t in vaz.items():
            print("    %s -> %s" % (f, ", ".join("{{%s}}" % k for k in t)))
        sys.exit(1)
    print("OK - nenhuma entrega com token literal.")
    sys.exit(0)


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--init" in args:
        init()
    elif "--saida" in args:
        i = args.index("--saida")
        saida(args[i + 1])
    else:
        verify()
