---
description: Nucleo HABILITACAO/IMPUGNACAO de credito (QGC) — divergencia (art. 7 §1), impugnacao (art. 8), retardataria (art. 10) e reserva (art. 6 §2), para qualquer classe de credor.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [dados do credito/QGC]
---

Voce foi acionado pelo comando `/habilitacao` do plugin recuperacao-judicial-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** habilitar, impugnar ou divergir credito no QGC.

## PROTOCOLO
1. Antes de redigir, decidir a via com `via-processual-rj`.
2. **Acionar a skill `habilitacao-credito-rj`** — cobre os 4 sub-fluxos: §A divergencia administrativa (art. 7 §1), §B impugnacao judicial (art. 8), §C habilitacao retardataria (art. 10), §D reserva (art. 6 §2). Atua pelo credor (habilitando/impugnando o QGC) ou pelo devedor/AJ (impugnando creditos).
3. Para credor TRABALHISTA, a porta de entrada e `/credor-trabalhista`.
4. Verificar prazos e classe; submeter a `revisao-final-rj` (R1-R4).

**Skill a acionar:** `habilitacao-credito-rj`.
