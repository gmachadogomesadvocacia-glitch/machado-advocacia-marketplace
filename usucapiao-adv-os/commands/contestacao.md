---
description: Lado CONFRONTANTE/reu.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [dados da defesa]
---

Voce foi acionado pelo comando `/contestacao` do plugin usucapiao-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** defender o confrontante/oponente.

## PROTOCOLO
1. Confirmar polo = confrontante/reu. Selo P1.
2. **Judicial** → `contestacao-usucapiao`: preliminares (art. 337) + merito — descaracterizar a posse (e DETENCAO/comodato — PA-09; falta ANIMUS DOMINI; posse violenta/clandestina/precaria; INTERRUPCAO/oposicao), impugnar metragem/confrontacoes, alegar BEM PUBLICO (PA-04) ou o titulo/registro do reu.
3. **Extrajudicial** → `impugnacao-usucapiao-extrajudicial`: impugnar o pedido perante o oficial do RI; a impugnacao remete o caso ao juizo.
4. Submeter a `revisao-final-usucapiao` (R1-R4).

**Skill a acionar:** `contestacao-usucapiao` (ou `impugnacao-usucapiao-extrajudicial`).
