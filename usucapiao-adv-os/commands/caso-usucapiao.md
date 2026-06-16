---
description: Abre, retoma ou lista um caso de usucapiao em usucapiao/casos/<slug>/ — CASO.md compartimentado (sigilo + LGPD). Suporta novo <slug>, <slug> e list.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [novo <slug> | <slug> | list]
---

Voce foi acionado pelo comando `/caso-usucapiao` do plugin usucapiao-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** gerenciar a memoria de caso compartimentada por cliente.

## PROTOCOLO
1. Resolver o COWORK (`usucapiao/`). Sem config → sugerir `/start-usucapiao`.
2. Interpretar `$ARGUMENTS`:
   - **`list`** → listar `usucapiao/casos/`.
   - **`novo <slug>`** → criar `usucapiao/casos/<slug>/` e renderizar `templates/CASO.md.tpl` e `MEMORY-caso.md.tpl` (via `memoria-de-caso-usucapiao`).
   - **`<slug>`** → retomar o `CASO.md`.
3. Dados do imovel/cliente (matricula, CPF, planta) SOMENTE na pasta local (gitignored). Alertar se sincronizado.
4. Estrutura do `CASO.md`: polo, via, modalidade, imovel (urbano/rural, matricula, metragem, confrontantes), posse (inicio, tempo, qualidade, justo titulo), entes a citar, foro/RI, prazos.

**Skill a acionar:** `memoria-de-caso-usucapiao`.
