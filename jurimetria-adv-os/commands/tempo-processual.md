---
description: Analisa duracao e ritmo processual — duracao tipica de um recorte, ritmo de um processo, tempo por fase quando os marcos existem, e lista de casos parados do acervo. Censura a direita sempre declarada.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: <recorte ou numero-cnj> [parados]
---

Voce foi acionado pelo comando `/tempo-processual` do plugin jurimetria-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** leitura de tempo — descritiva, nunca previsao.

## PROTOCOLO

1. Identificar a pergunta: duracao tipica de recorte | ritmo de UM processo | tempo por fase | casos parados do acervo.
2. **Acionar a skill `tempo-processual`** com o(s) script(s) adequado(s) (`benchmark_datajud.py`, `datajud_client.py`, `coletar_acervo.py --datajud`).
3. Separar SEMPRE vivos ("ja dura") de concluidos ("durou"); mediana/quartis antes de media.
4. "Parados": listar casos do acervo sem movimento ha mais de N meses (numero + ultima movimentacao) — saida operacional.
5. **Auditar com `revisao-final-jurimetria`** antes de entregar.

**Skill a acionar:** `tempo-processual`.
