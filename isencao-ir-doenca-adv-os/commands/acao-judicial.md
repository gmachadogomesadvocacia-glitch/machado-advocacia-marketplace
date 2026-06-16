---
description: Via JUDICIAL — acao declaratoria de isencao + repeticao de indebito (5 anos) + tutela para cessar a retencao. Ancorada nas Sumulas 598 e 627 STJ.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [dados do caso]
---

Voce foi acionado pelo comando `/acao-judicial` do plugin isencao-ir-doenca-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** redigir a acao judicial de isencao + restituicao.

## PROTOCOLO
1. Confirmar triagem + Selo P1 + linha estrategica (via judicial).
2. **Acionar a skill `acao-isencao-ir`** — declaratoria de isencao (art. 6 XIV) + repeticao de indebito dos ultimos 5 anos (CTN 168) + tutela para cessar a retencao; Sum. 598 (prova dispensa laudo oficial) e Sum. 627 (manutencao). So PROVENTOS (PA-06).
3. Articular `calculos-isencao-ir` (restituicao + Selic) e `estilo-juridico-isencao-ir`. Proteger o dado de saude (PA-10 — segredo de justica se necessario).
4. Submeter a `revisao-final-isencao-ir` (R1-R4).

**Skill a acionar:** `acao-isencao-ir`.
