---
description: Aciona a Suprema Corte da isencao-IR.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [documento a auditar]
---

Voce foi acionado pelo comando `/revisao-final` do plugin isencao-ir-doenca-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** submeter o documento a auditoria final R1-R4 (Protocolo P6).

## PROTOCOLO
1. **Acionar a skill `revisao-final-isencao-ir`** — R1 coleta/Selo P1; R2 base juridica (art. 6 XIV Lei 7.713 + Sum. 598/627; doenca no rol; so proventos; restituicao 5 anos); R3 tese/coerencia de polo/antecipacao adversarial; R4 completude/estilo/protecao do dado de saude.
2. Veredito: APROVADO / APROVADO COM RESSALVAS / REPROVADO. REPROVADO bloqueia — aponta a falha e devolve.
3. Bypass somente com `--no-corte` / `--quick` explicito.

**Skill a acionar:** `revisao-final-isencao-ir`.
