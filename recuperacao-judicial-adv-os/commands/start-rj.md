---
description: Configura o plugin de Recuperacao Judicial no ambiente do escritorio — cria a pasta recuperacao-judicial/ com identidade do advogado, frentes, tom. Gera persona e aponta RJ_PERSONA.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [opcional]
---

Voce foi acionado pelo comando `/start-rj` do plugin recuperacao-judicial-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** configurar o plugin e gerar a persona em runtime.

## PROTOCOLO

1. **Coletar** (wizard): identidade (nome, OAB, cidade/UF), frentes (credor-trabalhista / credor-geral / devedor-recuperando / administrador-judicial / consultivo), tom de voz e intensidade, modo de fluxo, ferramentas.
2. **Gravar o estado**: `python scripts/state.py init <cowork> --firm-name "..." --firm-slug "..." --advogado "..."` + `state.py set` para cada campo.
3. **Renderizar** `templates/persona.md.tpl` → `<cwd>/recuperacao-judicial/persona.md` e `config.md.tpl` → `config.md`; criar `<cwd>/recuperacao-judicial/casos/` (gitignored — sigilo + LGPD).
4. **Apontar `RJ_PERSONA`** no `<cwd>/.claude/settings.local.json` (render de `templates/settings-local.json.tpl`).
5. Alertar se o workspace for pasta sincronizada (dados de credor/devedor — LGPD).
6. Encerrar sugerindo `/status-rj` e `/triagem`.

**Acao:** orquestrar o engine (state + templates).
