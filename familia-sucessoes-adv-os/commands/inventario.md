---
description: Nucleo INVENTARIO/ARROLAMENTO — judicial ou extrajudicial, partilha da heranca, ITCMD e prazos. Nao confunde meacao com heranca.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [dados do espolio]
---

Voce foi acionado pelo comando `/inventario` do plugin familia-sucessoes-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** conduzir inventario/arrolamento e a partilha do espolio.

## PROTOCOLO
1. **Acionar a skill `inventario-arrolamento`** — via (judicial x extrajudicial — Res. 35/2007 CNJ, sem incapazes e sem litigio), nomeacao de inventariante, primeiras declaracoes, herdeiros, colacao e sonegados.
2. PA — **nunca confundir MEACAO (direito do conjuge/companheiro) com HERANCA (direito do herdeiro)**; verificar a legitima e a concorrencia (Tema 692 STJ).
3. **Prazos:** abertura em 60 dias da ciencia do obito; ITCMD (aliquota RJ 4% / da UF) — articular `calculos-familia`.
4. Reconhecimento de uniao estavel post mortem → `uniao-estavel`.
5. Submeter a `revisao-final-familia` (R1-R4).

**Skill a acionar:** `inventario-arrolamento`.
