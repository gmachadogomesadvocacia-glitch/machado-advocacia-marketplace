---
description: Aciona a Suprema Corte do usucapiao.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [documento a auditar]
---

Voce foi acionado pelo comando `/revisao-final` do plugin usucapiao-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** submeter o documento a auditoria final R1-R4 (Protocolo P6).

## PROTOCOLO
1. **Acionar a skill `revisao-final-usucapiao`** — R1 coleta/Selo P1 (matricula, planta+ART, posse); R2 base juridica (CC 1.238-1.244 + CF 183/191 + Lei 6.015 216-A; modalidade/requisitos; bem nao publico; citacoes completas no judicial / anuencias no extrajudicial); R3 tese/coerencia de polo/antecipacao adversarial (detencao, animus domini, interrupcao); R4 completude/estilo/descricao apta a registro.
2. Veredito: APROVADO / APROVADO COM RESSALVAS / REPROVADO. REPROVADO bloqueia — aponta a falha e devolve.
3. Bypass somente com `--no-corte` / `--quick` explicito.

**Skill a acionar:** `revisao-final-usucapiao`.
