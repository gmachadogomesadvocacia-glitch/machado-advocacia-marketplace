---
description: Submete uma analise jurimetrica a Suprema Corte do plugin.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [caminho ou referencia da analise]
---

Voce foi acionado pelo comando `/revisao-final-jurimetria` do plugin jurimetria-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** auditoria pre-entrega obrigatoria (PE-14) de qualquer saida com numeros.

## PROTOCOLO

1. Identificar a analise-alvo (argumento, ou a ultima produzida na sessao).
2. **Acionar a skill `revisao-final-jurimetria`**: R1 (dados/proveniencia) → R2 (metodo) → R3 (interpretacao — descritivo x promessa) → R4 (forma/sigilo) → R5 (red-team: derrubar cada numero, refazer 2-3 contas por amostragem).
3. Emitir o quadro R1-R5 + FICHA DE CONFERENCIA (fontes, numeros-chave com N, casos fora da conta, uso permitido).
4. REPROVADO → devolver com a falha exata (rodada + item + PE); nao entregar.

**Skill a acionar:** `revisao-final-jurimetria`.
