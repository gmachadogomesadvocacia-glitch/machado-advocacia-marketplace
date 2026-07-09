---
name: tempo-processual
description: >
  TEMPO PROCESSUAL — Skill Tier 2. Analisa duracao e ritmo: quanto tempo processos de um recorte levam (ajuizamento ao ultimo movimento), como o tempo se distribui, ha quanto tempo um caso esta sem movimentar, e leitura de fases a partir dos movimentos DataJud quando marcos sao identificaveis (sentenca, transito). Acione para "quanto tempo demora", "esta parado ha quanto tempo", "quando devemos ter sentenca" (resposta descritiva, nao previsao), ou a perna de tempo de uma viabilidade.
metadata:
  version: "0.1.0"
  area: "Jurimetria"
  tier: 2
---

# TEMPO PROCESSUAL

> Skill **Tier 2**. Tempo e o dado que o sistema tem de melhor qualidade (DataJud da de graca) — e tambem o que mais convida a previsao indevida. Resposta padrao: "processos assim tem levado X" (descritivo), nunca "o seu vai levar X" (PE-02).

---

## 0. TRES PERGUNTAS DISTINTAS

1. **Duracao tipica do recorte** — `benchmark_datajud.py` (mediana/quartis da amostra publica) e/ou acervo com `--datajud`. Regua descritiva.
2. **Ritmo de UM processo** — `datajud_client.py <numero>`: idade, movimentos, ultima movimentacao. "Parado ha N meses" e leitura direta (com ressalva de atraso de indexacao).
3. **Tempo por FASE** (ajuizamento→sentenca, sentenca→transito) — exige marcos nos movimentos: filtrar codigos/descricoes da tabela CNJ (ex.: julgamento, transito em julgado, arquivamento definitivo). Nem todo tribunal registra igual — quando o marco nao e confiavel no recorte, dizer que a fase nao e mensuravel com o dado disponivel, e nao aproximar em silencio.

## 1. DISCIPLINA DA CENSURA (o freio central daqui)

- Processo **em andamento**: duracao observada e um MINIMO ("ja dura X", nunca "durou X").
- Misturar vivos e baixados numa media "de duracao" subestima — separar os grupos ou usar so os que atingiram o marco.
- Se a maioria do recorte esta viva, a mediana de duracao total e incalculavel com honestidade → reportar "idade atual" dos vivos e duracao so dos concluidos, com os dois Ns.

## 2. EXECUCAO

1. Recorte da triagem → escolher a(s) pergunta(s) acima.
2. Rodar o(s) script(s); para fases, puxar os movimentos completos (o `_source` do DataJud traz a lista) e identificar os marcos por codigo.
3. Estatistica: mediana e quartis (PE-11); N ≥ limiar para qualquer agregado (PE-04).
4. Comparacao acervo x tribunal: mesmo recorte CNJ (PE-09), mediana com mediana.

## 3. SAIDA

Cada numero: valor + N + grupo (vivos/concluidos) + fonte + data. "Estimativa" para o caso concreto so em faixa descritiva: "casos concluidos deste recorte levaram entre X e Y (p25-p75, N=..)" — e com a frase de que isso nao e previsao do caso individual.

## 4. ENCERRAMENTO

Entregar a leitura de tempo com censura e Ns a vista. Pergunta que era de gestao ("quais casos estao parados?") vira lista operacional: casos do acervo sem movimento ha mais de N meses, com numero e ultima movimentacao — insumo direto de trabalho.
