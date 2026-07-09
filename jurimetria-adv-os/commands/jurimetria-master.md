---
description: Aciona o orquestrador Tier 0 do jurimetria-adv-os.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [demanda jurimetrica]
---

Voce foi acionado pelo comando `/jurimetria-master` do plugin jurimetria-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** ativar explicitamente a governanca do plugin e tratar a demanda descrita no argumento.

## PROTOCOLO

1. **Acionar a skill `jurimetria-master`** (Tier 0) — Hierarquia das 4 Camadas, Proibicoes Estatisticas PE-01 a PE-14, Protocolos P1-P6.
2. Se ha demanda no argumento, seguir o pipeline: `triagem-jurimetrica` (pergunta + fonte + recorte + N previsto) → motor Tier 2 → `revisao-final-jurimetria`.
3. Sem argumento: apresentar o menu de motores (portfolio, caso unico, benchmark, quantum, tempo, viabilidade) e perguntar a demanda.

**Skill a acionar:** `jurimetria-master`.
