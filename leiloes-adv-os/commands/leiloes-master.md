---
description: Carrega a governanca do plugin e roteia.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao do caso]
---

Voce foi acionado pelo comando `/leiloes-master` do plugin leiloes-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** carregar a governanca de 4 Camadas e rotear a demanda.

## PROTOCOLO
1. Acionar a skill `leiloes-master` (Tier 0).
2. **Confirmar o POLO antes de tudo** (§0 da skill): o cliente compra ou perde o bem? Se nao for arrematante nem pretendente, **parar e rotear** (PA-12).
3. Aplicar a Hierarquia das 4 Camadas e conferir as 13 Proibicoes Absolutas.
4. Rotear conforme a fase e o obstaculo; lembrar que nada se produz antes da `triagem-leiloes` e do Selo P1.
5. Antes de qualquer entrega, Revisao R1-R4.

**Skill a acionar:** `leiloes-master`.
