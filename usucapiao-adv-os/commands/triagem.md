---
description: Acionamento direto da triagem 4D.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao do caso]
---

Voce foi acionado pelo comando `/triagem` do plugin usucapiao-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** enquadrar o caso e gravar no `CASO.md`.

## PROTOCOLO
1. **Acionar `usucapiao-master`** brevemente (config + governanca).
2. **Acionar a skill `triagem-usucapiao`** — classifica: polo (usucapiente/confrontante); via (judicial x extrajudicial — extrajudicial so com consenso); modalidade provavel; imovel (urbano/rural, matricula, metragem, bem publico? — PA-04). Faz o pre-check da posse (tempo, animus domini, detencao? — PA-08/09).
3. **Gravar** no `CASO.md`. Faltando dado → `[INFORMAR]`.
4. Rotear para o Selo P1, `analise-documental-usucapiao` e `analise-posse-usucapiao`.

**Skill a acionar:** `triagem-usucapiao`.
