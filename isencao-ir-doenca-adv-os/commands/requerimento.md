---
description: Via ADMINISTRATIVA — requerimento de isencao a fonte pagadora (INSS/RPPS/fundo) + retificacao da DIRPF na Receita para a restituicao. Cessa a retencao na fonte.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [dados do beneficio/fonte]
---

Voce foi acionado pelo comando `/requerimento` do plugin isencao-ir-doenca-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** conduzir a via administrativa da isencao.

## PROTOCOLO
1. **Acionar a skill `requerimento-administrativo-isencao`** — requerimento a fonte pagadora (Meu INSS / RPPS / fundo EFPC) com laudo de servico medico oficial, pedido de cessacao da retencao e devolucao do retido.
2. Articular `retificacao-dirpf` para a restituicao dos ultimos 5 anos via Receita.
3. Registrar a recusa/silencio como prova (Protocolo P4) para eventual via judicial.
4. Submeter a `revisao-final-isencao-ir` (R1-R4).

**Skill a acionar:** `requerimento-administrativo-isencao`.
