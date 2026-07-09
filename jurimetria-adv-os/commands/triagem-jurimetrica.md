---
description: Define a pergunta analitica e o enquadramento 4D da demanda jurimetrica (tipo de analise x fonte x recorte x destino), com checagem previa de N.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao da demanda]
---

Voce foi acionado pelo comando `/triagem-jurimetrica` do plugin jurimetria-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** transformar o pedido em pergunta analitica precisa e rotear para o motor Tier 2 certo.

## PROTOCOLO

1. **Acionar a skill `triagem-jurimetrica`** com a demanda do argumento.
2. Classificar nas 4 dimensoes (tipo, fonte, recorte, destino) e **estimar o N disponivel** antes de prometer estatistica (N < limiar → avisar que a resposta sera qualitativa).
3. Apresentar o CHECKPOINT 1 (enquadramento) e aguardar confirmacao do operador.
4. Rotear: `instrumentar-caso` se faltar bloco → motor Tier 2 → `revisao-final-jurimetria`.

**Skill a acionar:** `triagem-jurimetrica`.
