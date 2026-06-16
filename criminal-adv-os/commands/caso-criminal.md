---
description: Abre ou atualiza o CASO.md do caso ativo (Protocolo P3) em criminal/casos/<slug>/ — memoria de caso compartimentada (sigilo reforcado + LGPD, dado penal sensivel).
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [novo <slug> | <slug> | list]
---

Voce foi acionado pelo comando `/caso-criminal` do plugin criminal-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** abrir, retomar ou atualizar o `CASO.md` do caso ativo, mantendo a memoria de caso compartimentada.

## PROTOCOLO
1. **Acionar a skill `memoria-de-caso-criminal`** (Protocolo P3) — operar a pasta `<cwd>/criminal/casos/<slug>/` com `CASO.md`, `MEMORY.md`, `arquivos/` e `pecas/`.
2. **Interpretar o argumento** — `novo <slug>` cria a estrutura a partir do `CASO.md.tpl`; `<slug>` retoma; `list` lista os casos; sem argumento, usa o caso ativo.
3. **Atualizar** — gravar polo, fase, crime/tipificacao, situacao prisional, prazos e decisoes no `CASO.md`; lacunas essenciais como `[INFORMAR]` (PA-01).
4. **Sigilo reforcado** — garantir que a pasta de casos permanece gitignored; alertar se o workspace for pasta sincronizada (dado penal sensivel + LGPD art. 11 — PA-09).

**Skill a acionar:** `memoria-de-caso-criminal`.
