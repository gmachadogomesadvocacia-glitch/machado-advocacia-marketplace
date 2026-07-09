---
description: Wizard de configuracao inicial do plugin no escritorio.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [opcional]
---

Voce foi acionado pelo comando `/start-imobiliario` do plugin imobiliario-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** conduzir o wizard de configuracao do plugin no ambiente do operador, gravando a identidade do escritorio fora do plugin distribuido.

## PROTOCOLO
1. **Verificar estado** — se ja existir `imobiliario/cowork-state.json`, avisar que o plugin esta configurado e oferecer reconfigurar; senao, seguir o wizard.
2. **Acionar a skill `onboarding-imobiliario`** — conduzir as perguntas: advogado (nome, OAB/UF/numero), firma, cidade/UF, email, tom/intensidade; frentes (locacao / contratos-imobiliarios / direitos-reais-posse / consultivo); pares de polo atendidos (locador x locatario, comprador x vendedor, possuidor x esbulhador, condominio x condomino, fiduciante x credor fiduciario); ferramentas.
3. **Inicializar o estado** — rodar `python scripts/state.py init <cowork>` e gravar os campos coletados via `python scripts/state.py set`.
4. **Definir CASE_ROOT (pasta unificada de caso)** — perguntar se ha acervo do escritorio configurado. No **Code** com acervo: `CASE_ROOT = <acervo>/Casos-Ativos`. Senao (Cowork ou sem acervo), **fallback**: `CASE_ROOT = <COWORK>/imobiliario/casos`. A pasta de caso e UNIFICADA e compartilhada entre os plugins Adv-OS do mesmo cliente (`<CASE_ROOT>/<slug>/` com CASO.md, MEMORY.md, arquivos/, pecas/). O estado interno (`cowork-state.json`) NAO muda — fica em `<COWORK>/imobiliario/`.
5. **Renderizar artefatos** — `persona.md.tpl` -> `<cwd>/imobiliario/persona.md` e `config.md.tpl` -> `<cwd>/imobiliario/config.md`, populando `{{FRENTES}}`, `{{POLOS}}` (pares de polo), `{{POLO_CLIENTE}}` e `{{CASE_ROOT}}`; criar a pasta `CASE_ROOT`.
6. **Apontar a persona** — gravar `IMOB_PERSONA` no `settings.local.json` apontando para a `persona.md` criada (variaveis do engine: `IMOB_PERSONA`, `IMOB_COWORK_PATH`, `IMOB_STATE_FILE`).
7. **Alerta de sigilo** — se o workspace for pasta sincronizada (OneDrive/iCloud/Google Drive/Dropbox), avisar sobre sigilo OAB + LGPD; a pasta de caso (`<CASE_ROOT>/<slug>/`) e gitignored.
8. **Encerrar** confirmando a identidade gravada e sugerindo `/status-imobiliario` e `/triagem`.

**Skill a acionar:** `onboarding-imobiliario`.
