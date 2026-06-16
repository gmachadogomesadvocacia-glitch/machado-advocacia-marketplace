---
description: Aciona a Suprema Corte da RJ — auditoria R1-R4 obrigatoria sobre toda peca/calculo/parecer antes da entrega. Bypass apenas com --no-corte/--quick explicito.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [documento a auditar]
---

Voce foi acionado pelo comando `/revisao-final` do plugin recuperacao-judicial-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** submeter o documento a auditoria final R1-R4 antes da entrega (Protocolo P6).

## PROTOCOLO

1. **Acionar a skill `revisao-final-rj`** — verifica:
   - **R1** — base normativa (L11.101/2005 + L14.112/2020) e dados do caso
   - **R2** — coerencia de polo (credor x devedor x AJ); classe e fato gerador corretos; teto 150 SM (art. 83 I); prazos (divergencia 15 dias art. 7§1; impugnacao 10 dias art. 8; retardataria art. 10)
   - **R3** — jurisprudencia STJ validada (PA-01); prescricao analisada (bienal/intercorrente/habilitacao/pos-encerramento)
   - **R4** — completude, estilo, consistencia com o CASO.md
2. Veredito: APROVADO / APROVADO COM RESSALVAS / REPROVADO. REPROVADO bloqueia — apontar a falha e devolver.
3. Bypass somente com `--no-corte` / `--quick` explicito.

**Skill a acionar:** `revisao-final-rj`.
