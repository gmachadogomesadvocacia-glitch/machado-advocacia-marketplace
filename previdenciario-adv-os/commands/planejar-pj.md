---
description: Planejamento previdenciario para socio/PJ.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [perfil do cliente/empresa]
---

Voce foi acionado pelo comando `/planejar-pj` do plugin previdenciario-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** desenhar o planejamento previdenciario do socio/empresario.

## PROTOCOLO
1. **Acionar a skill `planejamento-prev-pj`** — analisa CI / MEI / pro-labore, base de contribuicao, regras de transicao da EC 103 e a otimizacao da RMI futura x custo presente.
2. Apresentar cenarios (recomendar-e-listar ou apenas-listar, conforme o modo configurado).
3. Marcar premissas e `[VERIFICAR]` quando depender de norma/tese nao confirmada.
4. Submeter a `suprema-corte-previdenciaria` (R1-R4) se virar parecer.

**Skill a acionar:** `planejamento-prev-pj`.
