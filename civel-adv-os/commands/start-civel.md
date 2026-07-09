---
description: Wizard de configuracao do plugin.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [opcional]
---

Voce foi acionado pelo comando `/start-civel` do plugin civel-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** conduzir o wizard de configuracao do plugin no ambiente do operador, gravando a identidade do escritorio fora do plugin distribuido.

## PROTOCOLO
1. **Verificar estado** — se ja existir `civel/cowork-state.json`, avisar que o plugin esta configurado e oferecer reconfigurar; senao, seguir o wizard.
2. **Acionar a skill `onboarding-civel`** — conduzir as perguntas estruturadas: advogado (nome, OAB/UF/numero), escritorio (firma), cidade/UF, email, tom de voz e intensidade combativa (0-10); frentes ativas (responsabilidade-civil-indenizatorias / contratos-obrigacoes / cobranca-execucao / obrigacoes-tutelas); polo(s) de atuacao (autor x reu); modo de melhor saida.
3. **Inicializar o estado** — rodar `python scripts/state.py init <cowork>` para criar `civel/cowork-state.json`, e gravar os campos com `python scripts/state.py set <cowork> <json_path> <valor>`.
4. **Definir a pasta de casos (CASE_ROOT)** — perguntar se ha **acervo** do escritorio (pasta-fonte). Se sim (Code), `CASE_ROOT = <acervo>/Casos-Ativos`; se nao (Cowork/Chat), FALLBACK `CASE_ROOT = <COWORK>/civel/casos`. Criar a pasta `<CASE_ROOT>/` (unificada, COMPARTILHADA entre os plugins Adv-OS) e gravar `{{CASE_ROOT}}` no `config.md`. O estado interno (`<COWORK>/civel/cowork-state.json`) nao muda.
5. **Gerar artefatos** — renderizar `templates/persona.md.tpl` -> `<cwd>/civel/persona.md` e `templates/config.md.tpl` -> `<cwd>/civel/config.md` (com `{{CASE_ROOT}}` preenchido).
6. **Apontar a persona** — gravar `CIV_PERSONA` no `settings.local.json` apontando para `<cwd>/civel/persona.md`.
7. **Alertar sigilo + LGPD** — se o workspace for pasta sincronizada (OneDrive/iCloud/Google Drive), avisar do risco de espelhamento de dados de cliente; a pasta de casos (`<CASE_ROOT>/`) deve ficar gitignored.
8. **Confirmar** a identidade gravada e encerrar sugerindo `/status-civel` e `/triagem` para abrir o primeiro caso.

**Skill a acionar:** `onboarding-civel`.
