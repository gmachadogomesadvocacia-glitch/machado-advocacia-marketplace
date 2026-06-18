#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Camada 6 (confiabilidade) — SCANNER DE SIGILO / PII no repositorio PUBLICO.

O marketplace e PUBLICO e os plugins lidam com dado sensivel (saude — LGPD art. 11),
nomes de clientes, CPF, processos. NADA disso pode vazar para o repo: os dados reais
entram em runtime (tokens {{...}}) e ficam no acervo (OneDrive), nunca aqui.

Este guarda varre o repo e REPROVA o push se achar:
  - CPF formatado (NNN.NNN.NNN-NN)            -> dado pessoal
  - CNPJ formatado (NN.NNN.NNN/NNNN-NN)       -> dado pessoal/empresarial
  - numero de processo CNJ (NNNNNNN-DD.AAAA.J.TR.OOOO) -> identifica caso real
  - e-mail real (exceto allowlist)            -> contato pessoal
  - telefone BR formatado                      -> contato pessoal
  - nomes de clientes do acervo (denylist EXTERNA, opcional)  -> identifica a pessoa

A denylist de NOMES nao pode viver no repo publico (seria o proprio vazamento); ela
e lida de um arquivo FORA do repo, se existir:
    %USERPROFILE%/.claude/sigilo-denylist.txt   (1 nome/trecho por linha; '#' = comentario)
Sem esse arquivo, o scanner roda so os padroes estruturais (que ja sao a maior protecao).

Uso:  py tools/CONFIABILIDADE/check-sigilo.py    (rodar antes de push — entra na suite C6)
Exit 1 se achar qualquer PII.
"""
import re, glob, sys, os
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
ALLOW = HERE / "sigilo-allowlist.txt"          # trechos no repo que parecem PII mas sao exemplos OK
DENY_EXT = Path(os.path.expanduser("~")) / ".claude" / "sigilo-denylist.txt"  # nomes de clientes (fora do repo)

EXTS = ("*.md", "*.tpl", "*.json", "*.txt", "*.py")

PADROES = {
    "CPF":      re.compile(r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b"),
    "CNPJ":     re.compile(r"\b\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}\b"),
    "PROCESSO": re.compile(r"\b\d{7}-\d{2}\.\d{4}\.\d\.\d{2}\.\d{4}\b"),
    "EMAIL":    re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    "TELEFONE": re.compile(r"\(\d{2}\)\s?9?\d{4}-\d{4}\b"),
}

# e-mails legitimos do projeto (o autor/marketplace) — nao sao vazamento de cliente
EMAIL_OK = re.compile(r"@(machadoadvocacia|example|exemplo)\.")


def carregar_lista(p):
    if not p.exists():
        return []
    out = []
    for ln in open(p, encoding="utf-8", errors="replace").read().splitlines():
        ln = ln.strip()
        if ln and not ln.startswith("#"):
            out.append(ln)
    return out


def repo_files():
    fs = []
    for pat in EXTS:
        fs += glob.glob(str(REPO / "**" / pat), recursive=True)
    return sorted(set(fs))


def main():
    allow = carregar_lista(ALLOW)
    nomes = carregar_lista(DENY_EXT)
    nomes_rx = [re.compile(re.escape(n), re.IGNORECASE) for n in nomes]

    print("== SCANNER DE SIGILO / PII (Camada 6) ==")
    print("  allowlist: %d trecho(s) | denylist de nomes (externa): %s (%d nome[s])"
          % (len(allow), "presente" if DENY_EXT.exists() else "ausente", len(nomes)))

    achados = []
    for f in repo_files():
        rel = str(Path(f).relative_to(REPO))
        texto = open(f, encoding="utf-8", errors="replace").read()
        for rotulo, rx in PADROES.items():
            for m in rx.finditer(texto):
                val = m.group(0)
                if val in allow:
                    continue
                if rotulo == "EMAIL" and EMAIL_OK.search(val):
                    continue
                achados.append((rel, rotulo, val))
        for n, rx in zip(nomes, nomes_rx):
            if rx.search(texto):
                achados.append((rel, "NOME-CLIENTE", n))

    if achados:
        print("  FALHA - possivel PII no repo publico (%d ocorrencia[s]):" % len(achados))
        for rel, rotulo, val in achados[:60]:
            print("    [%s] %s  ->  %s" % (rotulo, rel, val))
        if len(achados) > 60:
            print("    ... (+%d)" % (len(achados) - 60))
        print("  Remova/anonimize antes de publicar. Dados reais so em runtime (tokens) + acervo.")
        sys.exit(1)
    print("OK - nenhum indicio de PII estruturada no repo.")
    if not DENY_EXT.exists():
        print("  (dica: crie %s com os nomes dos casos ativos p/ cobertura total)" % DENY_EXT)
    sys.exit(0)


if __name__ == "__main__":
    main()
