---
description: Aciona a Suprema Corte da familia.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [documento a auditar]
---

Voce foi acionado pelo comando `/revisao-final` do plugin familia-sucessoes-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** submeter o documento a auditoria final R1-R4 antes da entrega.

## PROTOCOLO

1. **Acionar a skill `revisao-final-familia`** — executa:
   - **R1** — dados do caso conferidos; documentos essenciais; Pontos de Omissao sinalizados
   - **R2** — base juridica: CC/2002 + CPC/2015 + ECA/Estatuto do Idoso vigentes; jurisprudencia STJ/TJ validada; regime de bens correto; prazos (inventario, ITCMD, recursos)
   - **R3** — tese: coerencia de polo; melhor interesse da crianca; meacao x heranca nao confundidas; antecipacao adversarial
   - **R4** — completude/estilo: estrutura da peca, valor da causa, pedido determinado, tom calibrado a sensibilidade do caso
2. Veredito: APROVADO / APROVADO COM RESSALVAS / REPROVADO. REPROVADO bloqueia — apontar a falha e devolver.
3. Bypass somente com `--no-corte` / `--quick` explicito.

**Skill a acionar:** `revisao-final-familia`.
