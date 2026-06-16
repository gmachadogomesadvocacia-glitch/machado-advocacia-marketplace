---
description: Acionamento direto da triagem — verifica os 4 requisitos da isencao (doenca no rol art. 6 XIV; rendimento e provento; fonte pagadora; periodo retido) e a via. Porta de entrada.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao do caso]
---

Voce foi acionado pelo comando `/triagem` do plugin isencao-ir-doenca-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** enquadrar o caso e gravar no `CASO.md`.

## PROTOCOLO
1. **Acionar `isencao-ir-master`** brevemente (config + governanca).
2. **Acionar a skill `triagem-isencao-ir`** — confirma os 4 requisitos: R1 doenca no rol taxativo (laudo, sem opinar sobre diagnostico — PA-04); R2 rendimento e PROVENTO de aposentadoria/pensao/reforma (nao ativo — PA-06); R3 fonte pagadora (INSS/RPPS/fundo/ex-empregador); R4 periodo de retencao indevida (restituicao 5 anos — PA-09). Decide a via (administrativa/judicial/ambas).
3. **Gravar** no `CASO.md`. Faltando dado → `[INFORMAR]`.
4. Rotear para o Selo P1 e a producao da via.

**Skill a acionar:** `triagem-isencao-ir`.
