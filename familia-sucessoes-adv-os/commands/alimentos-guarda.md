---
description: Nucleo GUARDA/ALIMENTOS.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [dados dos filhos/renda]
---

Voce foi acionado pelo comando `/alimentos-guarda` do plugin familia-sucessoes-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** conduzir guarda, convivencia e alimentos.

## PROTOCOLO
1. **Acionar a skill `guarda-alimentos`** — guarda (regra: compartilhada, art. 1.583-1.590 CC + ECA), regime de convivencia/visitas, e alimentos pelo **binomio necessidade-possibilidade** (art. 1.694 CC).
2. Prioridade absoluta ao **melhor interesse da crianca/adolescente**; atencao a alienacao parental (Lei 12.318).
3. Urgencia → `tutela-urgencia-familia` (alimentos provisorios/provisionais; guarda liminar). Calculo → `calculos-familia`.
4. Submeter a `revisao-final-familia` (R1-R4).

**Skill a acionar:** `guarda-alimentos`.
