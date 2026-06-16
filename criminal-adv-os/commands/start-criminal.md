---
description: Wizard de configuracao inicial do plugin no escritorio — cria persona, config, pasta de casos e aponta CRIM_PERSONA no settings.local.json. Rode na primeira vez.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [opcional]
---

Voce foi acionado pelo comando `/start-criminal` do plugin criminal-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** conduzir o wizard de configuracao do plugin no ambiente do operador, gravando a identidade do escritorio fora do plugin distribuido.

## PROTOCOLO
1. **Verificar estado** — se ja existir `criminal/cowork-state.json`, avisar que o plugin esta configurado e oferecer reconfigurar; senao, seguir o wizard.
2. **Acionar a skill `onboarding-criminal`** — conduzir as perguntas: advogado (nome, OAB/UF/numero), firma, cidade/UF, email, tom/intensidade; fases ativas (investigacao/inquerito, acao penal, juri, recursos, execucao penal, acordos); polo (defesa x assistencia de acusacao).
3. **Inicializar o estado** — rodar `python scripts/state.py init <cowork>` e gravar os campos coletados via `python scripts/state.py set`.
4. **Renderizar artefatos** — `persona.md.tpl` -> `<cwd>/criminal/persona.md`, `config.md.tpl` -> `<cwd>/criminal/config.md`; criar a pasta `<cwd>/criminal/casos/`.
5. **Apontar a persona** — gravar `CRIM_PERSONA` no `settings.local.json` apontando para a `persona.md` criada (variaveis do engine: `CRIM_PERSONA`, `CRIM_COWORK_PATH`, `CRIM_STATE_FILE`).
6. **Alerta de sigilo reforcado** — se o workspace for pasta sincronizada (OneDrive/iCloud/Google Drive/Dropbox), avisar sobre sigilo reforcado da defesa (dado penal sensivel + LGPD art. 11); a pasta de casos e gitignored (PA-09).
7. **Encerrar** confirmando a identidade gravada e sugerindo `/status-criminal` e `/triagem`.

**Skill a acionar:** `onboarding-criminal`.
