---
description: Nucleo DIVORCIO/SEPARACAO.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [dados do casal/regime]
---

Voce foi acionado pelo comando `/divorcio` do plugin familia-sucessoes-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** conduzir o divorcio/separacao e a partilha.

## PROTOCOLO
1. Confirmar polo (requerente/requerido) e **regime de bens** (PA — nunca confundir comunhao parcial/universal/separacao/participacao).
2. **Acionar a skill `divorcio-separacao`** — verifica via (judicial x extrajudicial — Res. 35/2007 e 571/2023 CNJ, sem filhos menores/incapazes e sem litigio), partilha, uso do nome, eventual alimentos entre conjuges.
3. Se houver patrimonio, articular `calculos-familia` (meacao/monte); se houver filhos, `guarda-alimentos`.
4. Submeter a `revisao-final-familia` (R1-R4).

**Skill a acionar:** `divorcio-separacao`.
