---
description: Via EXTRAJUDICIAL/CARTORIO.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [dados do imovel/posse]
---

Voce foi acionado pelo comando `/extrajudicial` do plugin usucapiao-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** conduzir a usucapiao em cartorio.

## PROTOCOLO
1. Confirmar que ha **CONSENSO** (anuencias) — havendo litigio/oposicao, ir para `/judicial` (PA-07). Selo P1 + modalidade definida.
2. **Acionar a skill `usucapiao-extrajudicial`** — ata notarial (tempo de posse), planta e memorial com ART assinados pelos confrontantes, certidoes, anuencias (silencio do confrontante notificado = concordancia, art. 216-A §2 — verificar redacao vigente), requerimento ao oficial do RI.
3. RI da circunscricao do imovel (P5). Bem nao publico (PA-04).
4. Submeter a `revisao-final-usucapiao` (R1-R4).

**Skill a acionar:** `usucapiao-extrajudicial`.
