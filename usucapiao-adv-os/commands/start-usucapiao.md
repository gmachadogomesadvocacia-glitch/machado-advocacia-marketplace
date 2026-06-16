---
description: Configura o plugin de Usucapiao no ambiente do escritorio — cria a pasta usucapiao/ com identidade, frentes, tom. Gera persona e aponta USU_PERSONA.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [opcional]
---

Voce foi acionado pelo comando `/start-usucapiao` do plugin usucapiao-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** configurar o plugin e gerar a persona em runtime.

## PROTOCOLO
1. **Acionar a skill `onboarding-usucapiao`** — wizard (identidade: nome, OAB, cidade/UF; frentes: judicial / extrajudicial-cartorio / defesa-confrontante / consultivo; tom; modo; ferramentas).
2. **Gravar o estado**: `python scripts/state.py init <cowork> ...` + `state.py set`.
3. **Renderizar** `templates/persona.md.tpl`→`<cwd>/usucapiao/persona.md` e `config.md`; criar `<cwd>/usucapiao/casos/` (gitignored).
4. **Apontar `USU_PERSONA`** no `<cwd>/.claude/settings.local.json`.
5. Alertar se o workspace for pasta sincronizada (sigilo + LGPD).
6. Encerrar sugerindo `/status-usucapiao` e `/triagem`.

**Skill a acionar:** `onboarding-usucapiao`.
