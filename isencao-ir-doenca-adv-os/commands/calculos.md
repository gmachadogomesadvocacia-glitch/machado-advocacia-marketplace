---
description: Calcula a restituicao do IR retido indevidamente.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [valores/informes de rendimento]
---

Voce foi acionado pelo comando `/calculos` do plugin isencao-ir-doenca-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** apurar a restituicao do indebito.

## PROTOCOLO
1. **Acionar a skill `calculos-isencao-ir`** — soma o IR retido indevidamente, competencia a competencia, nos ultimos 5 anos (CTN art. 168), com atualizacao pela Selic; entrega memoria de calculo discriminada.
2. Sem os comprovantes de retencao (informes de rendimento), NAO calcular — sinalizar o que falta (PA-03).
3. Resultado alimenta a `acao-isencao-ir`/`retificacao-dirpf` e o valor da causa; enviar a `revisao-final-isencao-ir`.

**Skill a acionar:** `calculos-isencao-ir`.
