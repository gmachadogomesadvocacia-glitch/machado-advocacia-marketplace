---
description: Abre, retoma ou lista um caso de isencao de IRPF em isencao-ir/casos/<slug>/ — CASO.md compartimentado (sigilo + LGPD; dado de saude sensivel). Suporta novo <slug>, <slug> e list.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [novo <slug> | <slug> | list]
---

Voce foi acionado pelo comando `/caso-isencao-ir` do plugin isencao-ir-doenca-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** gerenciar a memoria de caso compartimentada por cliente.

## PROTOCOLO
1. Resolver o COWORK (`isencao-ir/`). Sem config → sugerir `/start-isencao-ir`.
2. Interpretar `$ARGUMENTS`:
   - **`list`** → listar `isencao-ir/casos/`.
   - **`novo <slug>`** → criar `isencao-ir/casos/<slug>/` e renderizar `templates/CASO.md.tpl` e `MEMORY-caso.md.tpl` (via `memoria-de-caso-isencao-ir`).
   - **`<slug>`** → retomar o `CASO.md`.
3. **DADO DE SAUDE E SENSIVEL** (LGPD art. 11 + sigilo): laudo, CID, diagnostico SOMENTE na pasta local (gitignored). Alertar fortemente se o workspace for sincronizado.
4. Estrutura do `CASO.md`: polo, doenca/CID/data do laudo, fonte pagadora, tipo de provento, periodo de retencao, valor retido, via, prazos (prescricao 5 anos).

**Skill a acionar:** `memoria-de-caso-isencao-ir`.
