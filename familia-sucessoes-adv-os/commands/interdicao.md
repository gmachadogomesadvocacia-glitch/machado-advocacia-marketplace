---
description: Nucleo INTERDICAO/CURATELA — curatela do incapaz e Tomada de Decisao Apoiada (TDA), com modalidade e extensao corretas (CC + CPC + CRPD).
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [dados da pessoa a proteger]
---

Voce foi acionado pelo comando `/interdicao` do plugin familia-sucessoes-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** conduzir curatela/interdicao ou TDA.

## PROTOCOLO
1. **Acionar a skill `interdicao-curatela`** — avalia a incapacidade, a modalidade e a EXTENSAO da curatela (limitada aos atos patrimoniais/negociais — CC + CPC + Estatuto da Pessoa com Deficiencia/CRPD).
2. PA — **nunca confundir interdicao/curatela com Tomada de Decisao Apoiada (TDA, art. 1.783-A CC)**; preferir a medida menos restritiva.
3. Definir o curador, prestacao de contas e laudo pericial.
4. Submeter a `revisao-final-familia` (R1-R4).

**Skill a acionar:** `interdicao-curatela`.
