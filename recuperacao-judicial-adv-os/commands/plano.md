---
description: Nucleo PLANO DE RECUPERACAO — elaboracao/analise do plano (meios de recuperacao, deagio, carencia, classes), com olhar de credor ou de devedor.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [dados do plano/empresa]
---

Voce foi acionado pelo comando `/plano` do plugin recuperacao-judicial-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** elaborar ou analisar o plano de recuperacao judicial.

## PROTOCOLO
1. **Acionar a skill `plano-recuperacao-rj`** — meios de recuperacao (art. 50), deagio, carencia, prazos, tratamento por classe, e a viabilidade economica do plano.
2. Coerencia de polo: pelo devedor (propor plano exequivel) x pelo credor (analisar/objetar, preservar o credito e a classe).
3. Considerar a AGC (`assembleia-credores-rj`) e o cram down (art. 58 §1).
4. Submeter a `revisao-final-rj` (R1-R4).

**Skill a acionar:** `plano-recuperacao-rj`.
