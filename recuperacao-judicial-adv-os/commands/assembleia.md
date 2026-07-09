---
description: Nucleo AGC.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [dados da AGC]
---

Voce foi acionado pelo comando `/assembleia` do plugin recuperacao-judicial-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** atuar na Assembleia Geral de Credores.

## PROTOCOLO
1. **Acionar a skill `assembleia-credores-rj`** — convocacao e quorum (art. 35-46), votacao por classe (I/II/III/IV), aprovacao/rejeicao do plano, cram down (art. 58 §1) e atas.
2. Estrategia de voto conforme o polo e a classe do cliente; preservar o credito trabalhista.
3. Submeter eventuais pecas (objeção, recurso) a `revisao-final-rj`.

**Skill a acionar:** `assembleia-credores-rj`.
