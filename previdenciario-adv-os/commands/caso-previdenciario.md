---
description: Abre, retoma ou lista um caso previdenciario em <CASE_ROOT>/<slug>/.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [novo <slug> | <slug> | list]
---

Voce foi acionado pelo comando `/caso-previdenciario` do plugin previdenciario-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** gerenciar a memoria de caso compartimentada por segurado.

## PROTOCOLO

1. Resolver o **CASE_ROOT** (raiz dos casos, gravada no `config.md`): no Code, o acervo do escritorio = `<acervo>/Casos-Ativos`; FALLBACK = `<COWORK>/previdenciario/casos`. Sem config → sugerir `/start-previdenciario`.
2. Interpretar `$ARGUMENTS`:
   - **`list`** → listar as pastas em `<CASE_ROOT>/`.
   - **`novo <slug>`** → criar a pasta unificada `<CASE_ROOT>/<slug>/` com `CASO.md`, `MEMORY.md`, `arquivos/` e `pecas/` (renderizar `templates/CASO.md.tpl` e `MEMORY-caso.md.tpl`). Pasta COMPARTILHADA entre os plugins Adv-OS.
   - **`<slug>`** → ler e retomar o `CASO.md` em `<CASE_ROOT>/<slug>/`.
3. Pecas produzidas vao em `<CASE_ROOT>/<slug>/pecas/`. Manter os dados do segurado (CNIS, NB, CPF, perfil contributivo) SOMENTE na pasta do caso (gitignored) — nunca no plugin distribuido (LGPD). Alertar se o workspace for sincronizado.
4. Estrutura do `CASO.md`: especie/B-code, regime, fase, DER/DIB/RMI, qualidade de segurado, carencia, CNIS, documentos, prazos (decadencia decenal art. 103 / prescricao quinquenal).

**Acao:** gerenciar `CASO.md` via templates do engine.
