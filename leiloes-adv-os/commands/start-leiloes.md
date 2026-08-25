---
description: Configura o plugin no workspace.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [--update]
---

Voce foi acionado pelo comando `/start-leiloes` do plugin leiloes-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** rodar o wizard de configuracao e gravar persona, config e estado.

## PROTOCOLO
1. Acionar a skill `onboarding-leiloes`.
2. Coletar: identidade (nome, OAB, escritorio, contato), localizacao (cidade/UF), **polo** (arrematante e/ou pretendente — explicar que executado, devedor fiduciante, exequente e credor fiduciario sao roteados a outro plugin, e que isso e deliberado), frentes, ritos mais frequentes, raiz do acervo, tom de voz, modo de comparativo, Revisao Tecnica e ferramentas.
3. Gravar `<COWORK>/leiloes/cowork-state.json`, `persona.md`, `config.md`, `casos/` e apontar `LEIL_PERSONA` no `.claude/settings.local.json`.
4. Confirmar o gravado, avisar que a persona vale na proxima sessao e indicar o proximo passo (`/triagem` ou `/due-diligence`).

**Skill a acionar:** `onboarding-leiloes`.
