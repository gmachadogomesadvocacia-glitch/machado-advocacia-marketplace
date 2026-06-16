---
description: Configura o plugin de Isencao de IRPF no ambiente do escritorio — cria a pasta isencao-ir/ com identidade, frentes, tom. Gera persona e aponta ISIR_PERSONA. Alerta LGPD (dado de saude).
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [opcional]
---

Voce foi acionado pelo comando `/start-isencao-ir` do plugin isencao-ir-doenca-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** configurar o plugin e gerar a persona em runtime.

## PROTOCOLO
1. **Acionar a skill `onboarding-isencao-ir`** — wizard (identidade: nome, OAB, cidade/UF; frentes: administrativa / judicial / manutencao / consultivo; tom; modo; ferramentas).
2. **Gravar o estado**: `python scripts/state.py init <cowork> ...` + `state.py set`.
3. **Renderizar** `templates/persona.md.tpl`→`<cwd>/isencao-ir/persona.md` e `config.md`; criar `<cwd>/isencao-ir/casos/` (gitignored).
4. **Apontar `ISIR_PERSONA`** no `<cwd>/.claude/settings.local.json`.
5. **ALERTA LGPD REFORCADO**: o plugin lida com DADO DE SAUDE (sensivel — art. 11 LGPD + sigilo). Avisar fortemente se o workspace for pasta sincronizada (nuvem de terceiros).
6. Encerrar sugerindo `/status-isencao-ir` e `/triagem`.

**Skill a acionar:** `onboarding-isencao-ir`.
