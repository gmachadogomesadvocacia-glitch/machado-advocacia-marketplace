---
description: Compara unidades judiciarias da mesma comarca para a mesma classe+assunto (Modulo B por orgao julgador) — mediana/quartis de duracao, N e ritmo, com freios PE-04/PE-09 e leitura do que o numero nao diz. Nunca para escolher vara.
allowed-tools: Read, Bash, Glob, Grep
argument-hint: <classe + assunto + comarca | "1a x 3a VT p/ execucao">
---

Voce foi acionado pelo comando `/comparativo-varas` do plugin jurimetria-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** ritmo comparado entre varas, carimbado — sem virar forum shopping nem promessa.

## PROTOCOLO

1. **Acionar a skill `comparativo-varas`.** Confirmar a pergunta e o recorte (classe+assunto+comarca+janela) antes de rodar (checkpoint).
2. Rodar o Modulo B (`py scripts/benchmark_datajud.py`) UMA VEZ POR UNIDADE, mesmos filtros, sem paralelizar.
3. Freios: PE-04 (unidade com N < minimo sai da conta quantitativa), PE-09 (recorte identico), PE-11 (mediana/quartis), censura declarada.
4. Entregar o quadro comparativo com carimbo PE-01 em todo numero + secao de limitacoes + leitura; `revisao-final-jurimetria` (R1-R5) antes da entrega.
5. Pedido com fim de direcionar distribuicao: RECUSAR e explicar (fraude; distribuicao e sorteio).

**Skill a acionar:** `comparativo-varas`.
