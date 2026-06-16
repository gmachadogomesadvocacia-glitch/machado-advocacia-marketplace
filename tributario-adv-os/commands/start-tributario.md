---
description: Wizard de configuracao inicial do plugin no escritorio — cria persona, config, pasta de casos e aponta TRIB_PERSONA no settings.local.json. Rode na primeira vez.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [opcional]
---

Voce foi acionado pelo comando `/start-tributario` do plugin tributario-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** conduzir o wizard de configuracao do plugin no ambiente do operador, gravando a identidade do escritorio fora do plugin distribuido.

## PROTOCOLO
1. **Verificar estado** — se ja existir `tributario/cowork-state.json`, avisar que o plugin esta configurado e oferecer reconfigurar; senao, seguir o wizard.
2. **Acionar a skill `onboarding-tributario`** — conduzir as perguntas: advogado (nome, OAB/UF/numero), firma, cidade/UF, email, tom/intensidade; frentes (administrativa / judicial / consultiva); esferas (federal / estadual / municipal); polo (contribuinte / fazenda / ambos); ferramentas.
3. **Inicializar o estado** — rodar `python scripts/state.py init <cowork>` e gravar os campos coletados via `python scripts/state.py set`.
4. **Renderizar artefatos** — `persona.md.tpl` -> `<cwd>/tributario/persona.md`, `config.md.tpl` -> `<cwd>/tributario/config.md`; criar a pasta `<cwd>/tributario/casos/`.
5. **Apontar a persona** — gravar `TRIB_PERSONA` no `settings.local.json` apontando para a `persona.md` criada (variaveis do engine: `TRIB_PERSONA`, `TRIB_COWORK_PATH`, `TRIB_STATE_FILE`).
6. **Alerta de sigilo** — se o workspace for pasta sincronizada (OneDrive/iCloud/Google Drive/Dropbox), avisar sobre sigilo OAB (CTN art. 198) + LGPD; casos sao gitignored.
7. **Encerrar** confirmando a identidade gravada e sugerindo `/status-tributario` e `/triagem`.

**Skill a acionar:** `onboarding-tributario`.
