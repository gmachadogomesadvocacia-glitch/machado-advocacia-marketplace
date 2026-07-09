---
description: Wizard de configuracao inicial do plugin no escritorio.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [opcional]
---

Voce foi acionado pelo comando `/start-tributario` do plugin tributario-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** conduzir o wizard de configuracao do plugin no ambiente do operador, gravando a identidade do escritorio fora do plugin distribuido.

## PROTOCOLO
1. **Verificar estado** — se ja existir `tributario/cowork-state.json`, avisar que o plugin esta configurado e oferecer reconfigurar; senao, seguir o wizard.
2. **Acionar a skill `onboarding-tributario`** — conduzir as perguntas: advogado (nome, OAB/UF/numero), firma, cidade/UF, email, tom/intensidade; frentes (administrativa / judicial / consultiva); esferas (federal / estadual / municipal); polo (contribuinte / fazenda / ambos); ferramentas.
3. **Definir a raiz dos casos (CASE_ROOT)** — perguntar o caminho do acervo (pasta "Gustavo Machado Advocacia" ou diretamente a "Casos-Ativos"). Se informado e acessivel (Code), `CASE_ROOT = <acervo>/Casos-Ativos` (pasta unificada por caso, compartilhada entre plugins); senao (nuvem/sem acervo), `CASE_ROOT = <cwd>/tributario/casos` (FALLBACK). O estado interno (`cowork-state.json`) fica sempre em `<cwd>/tributario/`.
4. **Inicializar o estado** — rodar `python scripts/state.py init <cowork>` e gravar os campos coletados (inclusive `CASE_ROOT`) via `python scripts/state.py set`.
5. **Renderizar artefatos** — `persona.md.tpl` -> `<cwd>/tributario/persona.md`, `config.md.tpl` -> `<cwd>/tributario/config.md` (gravando `{{CASE_ROOT}}`); criar a pasta `<CASE_ROOT>/` se acessivel.
6. **Apontar a persona** — gravar `TRIB_PERSONA` no `settings.local.json` apontando para a `persona.md` criada (variaveis do engine: `TRIB_PERSONA`, `TRIB_COWORK_PATH`, `TRIB_STATE_FILE`).
7. **Alerta de sigilo** — se o workspace for pasta sincronizada (OneDrive/iCloud/Google Drive/Dropbox), avisar sobre sigilo OAB (CTN art. 198) + LGPD; casos sao gitignored.
8. **Encerrar** confirmando a identidade gravada e sugerindo `/status-tributario` e `/triagem`.

**Skill a acionar:** `onboarding-tributario`.
