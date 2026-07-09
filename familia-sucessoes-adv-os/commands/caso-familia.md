---
description: Abre, retoma ou lista um caso de familia/sucessoes em familia/casos/<slug>/.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [novo <slug> | <slug> | list]
---

Voce foi acionado pelo comando `/caso-familia` do plugin familia-sucessoes-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** gerenciar a memoria de caso compartimentada por cliente.

## PROTOCOLO

1. Resolver o COWORK (`familia/` subindo a arvore). Sem config → sugerir `/start-familia`.
2. Interpretar `$ARGUMENTS`:
   - **`list`** → listar as pastas em `familia/casos/`.
   - **`novo <slug>`** → criar `familia/casos/<slug>/` e renderizar `templates/CASO.md.tpl` e `MEMORY-caso.md.tpl` (via skill `memoria-de-caso-familia`).
   - **`<slug>`** → ler e retomar o `CASO.md` existente.
3. Manter dados sensiveis do nucleo familiar (filhos menores, patrimonio, CPF) SOMENTE na pasta local do caso (gitignored) — nunca no plugin distribuido (LGPD + sigilo OAB). Alertar se o workspace for sincronizado.
4. Estrutura do `CASO.md`: area, polo, tipo, regime de bens, partes do nucleo, filhos menores/incapazes, patrimonio mapeado, vara/comarca, prazos (inventario 60 dias, ITCMD, recursos).

**Skill a acionar:** `memoria-de-caso-familia`.
