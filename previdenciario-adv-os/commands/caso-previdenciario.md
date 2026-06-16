---
description: Abre, retoma ou lista um caso previdenciario em previdenciario/casos/<slug>/ — CASO.md compartimentado por segurado (sigilo + LGPD). Suporta novo <slug>, <slug> (retomar) e list.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [novo <slug> | <slug> | list]
---

Voce foi acionado pelo comando `/caso-previdenciario` do plugin previdenciario-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** gerenciar a memoria de caso compartimentada por segurado.

## PROTOCOLO

1. Resolver o COWORK (`previdenciario/` subindo a arvore). Sem config → sugerir `/start-previdenciario`.
2. Interpretar `$ARGUMENTS`:
   - **`list`** → listar as pastas em `previdenciario/casos/`.
   - **`novo <slug>`** → criar `previdenciario/casos/<slug>/` e renderizar `templates/CASO.md.tpl` e `MEMORY-caso.md.tpl`.
   - **`<slug>`** → ler e retomar o `CASO.md` existente.
3. Manter os dados do segurado (CNIS, NB, CPF, perfil contributivo) SOMENTE na pasta local do caso (gitignored) — nunca no plugin distribuido (LGPD). Alertar se o workspace for sincronizado.
4. Estrutura do `CASO.md`: especie/B-code, regime, fase, DER/DIB/RMI, qualidade de segurado, carencia, CNIS, documentos, prazos (decadencia decenal art. 103 / prescricao quinquenal).

**Acao:** gerenciar `CASO.md` via templates do engine.
