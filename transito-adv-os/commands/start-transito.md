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
2. **Acionar a skill `onboarding-transito`** — conduzir as perguntas: advogado (nome, OAB/UF/numero), firma, cidade/UF, email, tom/intensidade; eixos ativos (administrativo / CNH / judicial / analise); **acervo** (raiz dos casos do escritorio).
3. **Definir CASE_ROOT** — se o operador informar o acervo (Code), `CASE_ROOT = <acervo>/Casos-Ativos`; senao, fallback `CASE_ROOT = <COWORK>/transito/casos`. Gravar `{{CASE_ROOT}}` no `config.md`. A pasta de cada caso (`<CASE_ROOT>/<slug>/`) e UNIFICADA e compartilhada entre plugins do mesmo cliente; o estado interno (`cowork-state.json`) NAO muda (segue em `<COWORK>/transito/`).
4. **Inicializar o estado** — rodar `python scripts/state.py init <cowork>` e gravar os campos coletados via `python scripts/state.py set`.
5. **Renderizar artefatos** — `persona.md.tpl` -> `<cwd>/transito/persona.md`, `config.md.tpl` -> `<cwd>/transito/config.md` (com `{{CASE_ROOT}}` resolvido); criar a raiz dos casos `<CASE_ROOT>/`.
6. **Apontar a persona** — gravar `TRAN_PERSONA` no `settings.local.json` apontando para a `persona.md` criada (variaveis do engine: `TRAN_PERSONA`, `TRAN_COWORK_PATH`, `TRAN_STATE_FILE`).
7. **Alerta de sigilo + LGPD** — se `CASE_ROOT` for pasta sincronizada (OneDrive/iCloud/Google Drive/Dropbox), avisar que a pasta de casos guarda dados pessoais do condutor (sigilo OAB + LGPD) e e gitignored.
8. **Encerrar** confirmando a identidade gravada e sugerindo `/status-transito` e `/triagem`.

**Skill a acionar:** `onboarding-transito`.
