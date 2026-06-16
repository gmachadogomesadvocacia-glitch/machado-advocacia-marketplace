---
name: revisional-bancaria
description: >
  REVISIONAL BANCARIA — Skill Tier 2 (eixo bancario, lado consumidor). Redige a acao revisional de
  contrato bancario/financeiro: impugna juros remuneratorios acima da taxa media de mercado, anatocismo/
  capitalizacao sem pactuacao, tarifas e encargos abusivos, comissao de permanencia cumulada, e mora
  descaracterizada. Integra-se a calculos-consumidor para a memoria de calculo. Acione quando o cliente
  e o consumidor e o caso envolve financiamento, emprestimo, cedula de credito, cartao, consignado,
  juros abusivos, capitalizacao ou tarifas. Exige Selo P1 e dado-base do contrato. Atencao reforcada as
  Sumulas 382 (taxa >12% nao e per se abusiva) e 530 (taxa media BACEN na impossibilidade de provar a contratada), e 539/541 (capitalizacao).
metadata:
  version: "0.1.0"
  area: "Direito do Consumidor e Bancario"
  tier: 2
---

# REVISIONAL BANCARIA

> Skill **Tier 2** — eixo bancario, lado consumidor. Especializa a `peticao-inicial-consumidor` para a revisao de contrato bancario. Disciplina rigida contra teses sem base (PA-08, PA-09).

---

## 0. PRE-REQUISITOS

- Polo = consumidor (PA-05). Lado banco → `defesa-instituicao-financeira`.
- Selo P1 emitido. **CDC aplica-se aos bancos (Sumula 297 STJ).**
- Dado-base do contrato: valor, prazo, taxa pactuada, sistema de amortizacao, tarifas, CET. Sem isso, NAO redigir nem calcular (PA-15, PA-20) → `[INFORMAR]`.

## 1. TESES ADMISSIVEIS (e seus limites)

| Tese | Base | Limite/armadilha |
|------|------|------------------|
| Juros remuneratorios abusivos | art. 6/51 CDC | NAO basta superar 12% a.a. (Sum. 382 STJ/596 STF). So abusivo se **acima da taxa media de mercado** do BACEN para a especie — comprovar discrepancia. **Sum. 530 STJ**: na **impossibilidade de comprovar a taxa efetivamente contratada**, aplica-se a taxa media de mercado divulgada pelo BACEN. |
| Capitalizacao (anatocismo) | art. 51 CDC | Permitida se **expressamente pactuada** (MP 2.170-36; Sum. 539/541 STJ). Sem pactuacao expressa → expurgar. |
| Comissao de permanencia | Sum. 30/294/472 STJ | Licita isolada ate a taxa do contrato, mas **nao cumulavel** com juros remuneratorios, moratorios, multa ou correcao. |
| Tarifas (TAC/TEC, cadastro, avaliacao) | Tema 618 STJ | TAC/TEC vedadas apos 30/04/2008; tarifa de cadastro so no inicio do relacionamento; analisar caso a caso. |
| Venda casada (seguro/serviços) | art. 39, I CDC | Seguro imposto no financiamento → restituicao. |
| Mora descaracterizada | jurisprudencia | Cobranca de encargo abusivo no periodo da normalidade descaracteriza a mora → afasta busca e apreensao/negativacao. |

> **PA-08:** nunca alegar juros abusivos por mero comparativo com 12%. **PA-09:** capitalizacao so se faltar pactuacao expressa. Toda tese marcada `[VERIFICAR]` vai a `jurisprudencia-consumidor`.

## 2. ESTRUTURA (sobre a inicial-base)

Segue a `peticao-inicial-consumidor`, com:
- **Dos Fatos** — contrato (doc. N), parcelas, evolucao da divida.
- **Do Direito** — um FIRAC por encargo impugnado (juros / capitalizacao / tarifa / comissao), sempre ancorado na sumula correta e na taxa media.
- **Da Tutela** (se cabivel) — consignar valor incontroverso, obstar negativacao/busca e apreensao, manter na posse do bem.
- **Pedidos** — revisao das clausulas (com inciso do art. 51, PA-13), recalculo pela taxa media, expurgo da capitalizacao nao pactuada, repeticao do indebito (simples ou dobro art. 42 conforme engano injustificavel), exibicao do contrato e da planilha.

## 3. CALCULO

Acionar `calculos-consumidor` para: recompor o saldo pela taxa media, expurgar capitalizacao/tarifas, apurar o indebito e atualizar. Entregar **memoria discriminada** (PA-20). Sem dado-base, apresentar o que falta antes de prosseguir.

## 4. CHECKLIST

- [ ] Taxa pactuada comprovada; se impossivel comprova-la, aplicar taxa media BACEN (Sum. 530)
- [ ] Capitalizacao: ha pactuacao expressa? (Sum. 539/541)
- [ ] Comissao de permanencia nao cumulada
- [ ] Mora: descaracterizada? reflexo em negativacao/busca e apreensao
- [ ] Pedido de exibicao do contrato/planilha · memoria de calculo anexa
- [ ] `revisao-final-consumidor` R1-R4 (PA-22)

## 5. ENCERRAMENTO

Entrega a revisional com cada encargo impugnado em FIRAC ancorado na sumula correta e calculo discriminado — sem as armadilhas do 12% e da capitalizacao presumida.
