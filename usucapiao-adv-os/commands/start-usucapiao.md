---
description: Configura o plugin de Usucapiao no ambiente do escritorio — cria a pasta usucapiao/ com identidade, frentes, tom. Gera persona e aponta USU_PERSONA.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [opcional]
---

Voce foi acionado pelo comando `/start-usucapiao` do plugin usucapiao-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** configurar o plugin e gerar a persona em runtime.

## PROTOCOLO
1. **Acionar a skill `onboarding-usucapiao`** — wizard (identidade: nome, OAB, cidade/UF; frentes: judicial / extrajudicial-cartorio / defesa-confrontante / consultivo; tom; modo; ferramentas; **acervo do escritorio**).
2. **Definir `CASE_ROOT`**: perguntar se ha acervo do escritorio. Com acervo (Code) → `<acervo>/Casos-Ativos`; sem acervo (FALLBACK) → `<COWORK>/usucapiao/casos`. Pasta de casos UNIFICADA e COMPARTILHADA entre os plugins Adv-OS.
3. **Gravar o estado**: `python scripts/state.py init <cowork> ...` + `state.py set` (inclui `{{CASE_ROOT}}`).
4. **Renderizar** `templates/persona.md.tpl`→`<cwd>/usucapiao/persona.md` e `config.md` (gravando `{{CASE_ROOT}}`); criar `<CASE_ROOT>/` (no FALLBACK, gitignored).
5. **Apontar `USU_PERSONA`** no `<cwd>/.claude/settings.local.json`.
6. Alertar se o workspace for pasta sincronizada (sigilo + LGPD).
7. Encerrar sugerindo `/status-usucapiao` e `/triagem`.

**Skill a acionar:** `onboarding-usucapiao`.
