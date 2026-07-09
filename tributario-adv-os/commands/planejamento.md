---
description: Planejamento tributario licito (elisao.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao do caso ou objetivo do cliente]
---

Voce foi acionado pelo comando `/planejamento` do plugin tributario-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** estruturar planejamento tributario licito na frente consultiva, sempre dentro dos limites da elisao.

## PROTOCOLO
1. **Conferir a triagem** — `CASO.md` com o perfil do cliente (PF/PJ), atividade, faturamento, esferas e objetivo consultivo.
2. **Elisao x evasao (PA-06)** — produzir apenas planejamento LICITO; rejeitar e sinalizar qualquer estrutura simulada/fraudulenta (evasao). Aferir proposito negocial e substancia.
3. **Acionar a skill `planejamento-tributario`** — comparar regimes (Simples / Lucro Presumido / Lucro Real), reorganizacao societaria, beneficios fiscais e impacto de cada cenario.
4. **Rotear quando cabivel:**
   - regularizacao de passivo -> `parcelamento-transacao` (parcelamentos + transacao tributaria Lei 13.988/2020).
   - efeitos da transicao CBS/IBS -> `reforma-tributaria` (EC 132/2023 + LC 214/2025, 2026-2033).
5. **Norma vigente** + regras de transicao (PA-04); jurisprudencia validada (PA-01).
6. Se o produto final for parecer/peca, submeter a `revisao-final-tributaria` (R1-R4).

**Skill a acionar:** `planejamento-tributario`.
