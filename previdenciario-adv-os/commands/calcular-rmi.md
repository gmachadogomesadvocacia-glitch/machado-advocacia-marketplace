---
description: Calculo previdenciario — RMI, RMA, salario de beneficio, com auto-ataque (Protocolo P5). Nunca calcula sem dado-base (CNIS, salarios, marco temporal).
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [dados do calculo]
---

Voce foi acionado pelo comando `/calcular-rmi` do plugin previdenciario-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** apurar RMI/RMA/salario de beneficio com memoria discriminada.

## PROTOCOLO
1. Exigir o Selo de validacao da norma vigente no marco temporal (EC 103 + regra de transicao aplicavel).
2. **Acionar a skill `calculos-previdenciarios`** — apura salario de beneficio, coeficiente, RMI/RMA; aplica o Protocolo P5 e o auto-ataque (conferir o proprio calculo como faria o INSS).
3. Sem dado-base (CNIS, salarios de contribuicao, DER), NAO calcular — sinalizar `[INFORMAR]` o que falta.
4. Entregar memoria de calculo + enviar a `suprema-corte-previdenciaria` (R1-R4).

**Skill a acionar:** `calculos-previdenciarios`.
