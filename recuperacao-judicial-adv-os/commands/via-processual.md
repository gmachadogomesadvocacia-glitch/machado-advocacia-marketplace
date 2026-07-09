---
description: Nucleo VIA PROCESSUAL.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [situacao do credito/fase]
---

Voce foi acionado pelo comando `/via-processual` do plugin recuperacao-judicial-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** definir a via processual correta antes de redigir a peca.

## PROTOCOLO
1. **Acionar a skill `via-processual-rj`** — decide entre: divergencia administrativa (art. 7 §1 — prazo do edital, 15 dias); impugnacao judicial (art. 8 — 10 dias); habilitacao retardataria (art. 10 — fora do prazo); reserva (art. 6 §2 — credito ilíquido/em discussao na JT).
2. Considerar a fase (edital do AJ, formacao do QGC, pos-QGC) e a situacao do credito (constituido, em liquidacao, em discussao).
3. Definida a via, encaminhar para `habilitacao-credito-rj` (ou `credor-trabalhista-rj` se CTH) produzir a peca.

**Skill a acionar:** `via-processual-rj`.
