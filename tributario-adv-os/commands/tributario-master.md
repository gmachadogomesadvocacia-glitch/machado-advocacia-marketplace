---
description: Aciona a governanca central (Tier 0) do plugin tributario-adv-os.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [pergunta ou contexto opcional]
---

Voce foi acionado pelo comando `/tributario-master` do plugin tributario-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** carregar a governanca de 4 Camadas, mostrar a configuracao ativa e rotear a demanda para a skill correta.

## PROTOCOLO
1. **Carregar estado** — procurar `tributario/cowork-state.json` subindo a arvore; ler `TRIB_PERSONA` (persona.md) e a config (frentes, esferas, polo, tom). Se ausente, sugerir `/start-tributario`.
2. **Acionar a skill `tributario-master`** (Tier 0) — aplicar as 4 Camadas de Governanca, as 13 Proibicoes Absolutas e os Protocolos (Selo P1, R1-R4, P4 cruzamento administrativo-judicial, P5 localizacao/orgao).
3. **Resumir a config ativa** — advogado/escritorio, polo (contribuinte x Fazenda), frentes (administrativa/judicial/consultiva) e esferas (federal/estadual/municipal).
4. **Rotear** — diante do `$ARGUMENTS`, indicar a porta de entrada (`/triagem`) ou a skill de producao adequada (impugnacao, CARF, execucao fiscal, anulatoria, MS, repeticao, planejamento).
5. Nunca produzir peca sem passar pela triagem e, ao final, pela Revisao R1-R4.

**Skill a acionar:** `tributario-master`.
