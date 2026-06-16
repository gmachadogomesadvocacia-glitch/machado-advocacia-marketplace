---
description: Abre ou atualiza o CASO.md do caso ativo (Protocolo P3) em tributario/casos/<slug>/ — memoria de caso compartimentada (sigilo OAB + LGPD).
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [novo <slug> | <slug> | list]
---

Voce foi acionado pelo comando `/caso-tributario` do plugin tributario-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** abrir, retomar ou atualizar o `CASO.md` do caso ativo, mantendo a memoria de caso compartimentada.

## PROTOCOLO
1. **Acionar a skill `memoria-de-caso-tributario`** (Protocolo P3) — operar a pasta `<cwd>/tributario/casos/<slug>/` com `CASO.md`, `MEMORY.md`, `arquivos/` e `pecas/`.
2. **Interpretar o argumento** — `novo <slug>` cria a estrutura a partir do `CASO.md.tpl`; `<slug>` retoma; `list` lista os casos; sem argumento, usa o caso ativo.
3. **Atualizar** — gravar polo, frente, esfera, tributo, fase, prazos e decisoes no `CASO.md`; lacunas essenciais como `[INFORMAR]` (PA-01).
4. **Sigilo** — garantir que a pasta de casos permanece gitignored; alertar se o workspace for pasta sincronizada (CTN 198 + LGPD).

**Skill a acionar:** `memoria-de-caso-tributario`.
