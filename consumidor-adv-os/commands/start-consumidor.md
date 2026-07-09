---
description: Wizard de configuracao inicial do plugin consumidor-adv-os.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [opcional]
---

Voce foi acionado pelo comando `/start-consumidor` do plugin consumidor-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** conduzir o wizard de configuracao do plugin no ambiente do operador, gravando a identidade do escritorio fora do plugin distribuido.

## PROTOCOLO

1. **Verificar estado** — se ja existir `consumidor/cowork-state.json`, avisar que o plugin esta configurado e oferecer reconfigurar; senao, seguir o wizard.
2. **Acionar a skill `onboarding-consumidor`** — conduzir as perguntas estruturadas: advogado (nome, OAB, UF), escritorio, cidade/UF, polos de atuacao (consumidor/fornecedor/ambos), eixos ativos, tom de voz e modo de fluxo (checkpoint/continuo).
2a. **Acervo e raiz dos casos (CASE_ROOT)** — perguntar pelo acervo do escritorio e definir o `CASE_ROOT` (pasta unificada e COMPARTILHADA entre os plugins Adv-OS): no Claude Code, `<acervo>/Casos-Ativos`; fora do Code (fallback), `<COWORK>/consumidor/casos`. Criar a pasta e gravar `{{CASE_ROOT}}` no estado/config.
3. **Inicializar o estado** — rodar `python scripts/state.py init` para criar `consumidor/cowork-state.json`.
4. **Gerar artefatos** — `consumidor/persona.md`, `consumidor/config.md` (com a `Raiz dos casos` = `{{CASE_ROOT}}`) e a pasta de casos em `{{CASE_ROOT}}`.
5. **Apontar a persona** — gravar `CONSUM_PERSONA` no `settings.local.json` apontando para a persona criada.
6. **Confirmar** ao operador a identidade gravada e sugerir `/triagem-consumidor` para abrir o primeiro caso.
7. Acionar brevemente `consumidor-master` para validar que a governanca (4 Camadas) reconhece a nova config.

**Skill a acionar:** `onboarding-consumidor`.
