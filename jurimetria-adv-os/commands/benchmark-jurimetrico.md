---
description: Roda o Modulo B — regua publica de duracao via DataJud por classe+assunto+orgao, com comparacao opcional contra o acervo proprio no mesmo recorte CNJ (mediana com mediana).
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: <tribunal e classe (+ assunto/orgao)> [vs acervo]
---

Voce foi acionado pelo comando `/benchmark-jurimetrico` do plugin jurimetria-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** regua externa de tempo/composicao — e, se pedido, a comparacao com o portfolio.

## PROTOCOLO

1. Confirmar o recorte CNJ (classe obrigatoria; preferir codigos aos nomes). Recorte vago → passar antes pela `triagem-jurimetrica`.
2. **Acionar a skill `benchmark-datajud`**: `py scripts/benchmark_datajud.py --tribunal <alias> --classe... [--json amostra.json]`.
3. Se "vs acervo": rodar a perna propria (`coleta-acervo`) no MESMO recorte e comparar mediana com mediana, cada lado com seu N.
4. Declarar os limites da amostra (pagina unica dos recentes, censura, sem quantum) e nao explicar causa de diferenca sem dado (PE-08).
5. **Auditar com `revisao-final-jurimetria`** antes de entregar.

**Skill a acionar:** `benchmark-datajud`.
