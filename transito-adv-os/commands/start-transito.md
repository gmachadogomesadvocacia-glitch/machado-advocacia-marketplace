---
description: Wizard de configuracao inicial do plugin no escritorio — cria persona, config, pasta de casos e aponta TRAN_PERSONA no settings.local.json. Rode na primeira vez.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [opcional]
---

Voce foi acionado pelo comando `/start-transito` do plugin transito-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** conduzir o wizard de configuracao do plugin no ambiente do operador, gravando a identidade do escritorio fora do plugin distribuido.

## PROTOCOLO
1. **Verificar estado** — se ja existir `transito/cowork-state.json`, avisar que o plugin esta configurado e oferecer reconfigurar; senao, seguir o wizard.
2. **Acionar a skill `onboarding-transito`** — conduzir as perguntas: advogado (nome, OAB/UF/numero), firma, cidade/UF, email, tom/intensidade; eixos ativos (administrativo / CNH / judicial / analise).
3. **Inicializar o estado** — rodar `python scripts/state.py init <cowork>` e gravar os campos coletados via `python scripts/state.py set`.
4. **Renderizar artefatos** — `persona.md.tpl` -> `<cwd>/transito/persona.md`, `config.md.tpl` -> `<cwd>/transito/config.md`; criar a pasta `<cwd>/transito/casos/`.
5. **Apontar a persona** — gravar `TRAN_PERSONA` no `settings.local.json` apontando para a `persona.md` criada (variaveis do engine: `TRAN_PERSONA`, `TRAN_COWORK_PATH`, `TRAN_STATE_FILE`).
6. **Alerta de sigilo + LGPD** — se o workspace for pasta sincronizada (OneDrive/iCloud/Google Drive/Dropbox), avisar que a pasta de casos guarda dados pessoais do condutor (sigilo OAB + LGPD) e e gitignored.
7. **Encerrar** confirmando a identidade gravada e sugerindo `/status-transito` e `/triagem`.

**Skill a acionar:** `onboarding-transito`.
