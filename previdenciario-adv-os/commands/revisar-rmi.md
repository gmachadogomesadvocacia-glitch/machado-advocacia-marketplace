---
description: Acao revisional de RMI.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [dados do beneficio]
---

Voce foi acionado pelo comando `/revisar-rmi` do plugin previdenciario-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** identificar e pleitear a revisao do beneficio.

## PROTOCOLO
1. **Acionar a skill `acao-revisional-rmi`** — verifica teses revisionais (Vida Toda — Tema 1102 STF; Tema 999; erro de calculo; reenquadramento), confronta a carta de concessao e o CNIS.
2. **Conferir a decadencia decenal** (art. 103 Lei 8.213) e a prescricao quinquenal antes de tudo — sinalizar se ja decaiu.
3. Validar a jurisprudencia viva (status atual dos Temas) via `jurisprudencia-estrategica` — nunca presumir.
4. Submeter a `suprema-corte-previdenciaria` (R1-R4).

**Skill a acionar:** `acao-revisional-rmi`.
