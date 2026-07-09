---
name: calculos-imobiliarios
description: >
  Calculos imobiliarios Tier 1 — nucleo de calculo do plugin. Ative ao calcular debito de aluguel, purgacao, revisional, restituicao ou saldo.
metadata:
  version: "0.1.0"
  area: "Direito Imobiliario e Locacao"
  tier: 1
---

# CALCULOS IMOBILIARIOS

> Tier 1. Nucleo de calculo. Toda saida e uma **memoria de calculo passo a passo, com datas**. Nunca inventar valor, indice ou data (PA-03) — pedir o dado que faltar. Conferir o indice e a multa **no contrato** (PA-02/PA-04).

---

## 1. DEBITO LOCATICIO

Para cada competencia em atraso:
```
1. Aluguel base ............................. R$ ____
2. + Encargos (IPTU rateado, condominio) .... R$ ____
3. + Reajuste pelo indice contratual ........ IGP-M / IPCA (acumulado ate a competencia)
4. = Valor atualizado da parcela ............ R$ ____
5. + Multa moratoria (clausula contratual) .. ___%
6. + Juros de mora (1% a.m., salvo outro) ... desde o vencimento
7. = Total da competencia ................... R$ ____
```
Somar todas as competencias = **debito total**. Indicar data-base do calculo.

## 2. PURGACAO DA MORA (art. 62, II Lei 8.245)

Total a depositar para purgar e elidir o despejo:
```
Alugueis e acessorios vencidos + multas + juros
+ custas e honorarios advocaticios (10% ou contratado)
+ alugueis que se vencerem ate a data do deposito
= TOTAL DA PURGACAO
```
Conferir se o locatario tem direito (nao houve purgacao nos 24 meses anteriores — art. 62 § unico).

## 3. REVISIONAL (art. 19)

Aluguel vigente x **valor de mercado** atual (laudo/pesquisa). Apontar defasagem percentual e o novo valor pretendido. Periodicidade minima legal (3 anos) cumprida.

## 4. RESTITUICAO NO DISTRATO (Lei 13.786/2018; Sum. 543)

> **PA-04:** a Lei 13.786 so alcanca **contratos celebrados apos sua vigencia**. Contrato anterior → regime do CC + Sum. 543 (validar).

```
Valor pago pelo adquirente ................. R$ ____
- Retencao da incorporadora ................ ate 25% (ou 50% se patrimonio de afetacao)
- Comissao de corretagem ................... conforme contrato
- Demais encargos previstos em lei ......... ____
= VALOR A RESTITUIR ........................ R$ ____
```
Por culpa do **vendedor**: restituicao integral (Sum. 543 — validar). Por culpa do **comprador**: retencao na forma da lei vigente.

## 5. RESTITUICAO / ABATIMENTO POR VICIOS

Vicio redibitorio: abatimento (estimatoria) ou resolucao (redibitoria) — quantificar o custo do reparo ou a diferenca de valor. Documentar a base (orcamento, laudo).

## 6. SALDO NA ALIENACAO FIDUCIARIA (art. 27 §4º Lei 9.514)

Apos o leilao:
```
Valor arrematado ........................... R$ ____
- Divida (saldo devedor + encargos) ........ R$ ____
- Despesas, tributos, comissao do leiloeiro . R$ ____
= EXCEDENTE a devolver ao fiduciante ....... R$ ____
```
Se o lance nao cobre a divida, a obrigacao se extingue (art. 27 §5º). **Excedente e devido ao devedor** — checar se foi pago.

## 7. EXEMPLO RESOLVIDO — DEBITO LOCATICIO + PURGACAO DA MORA

> Numeros ilustrativos. Aluguel R$ 2.000,00 + IPTU rateado R$ 200,00/mes; multa moratoria contratual de 10%; juros de 1% a.m.; reajuste IGP-M ja incidente (aluguel vigente). Inadimplencia de 3 competencias; data-base do calculo 16/06/2026; deposito de purgacao previsto para 30/06/2026 (com 1 competencia a vencer ate la). Indices e percentuais conferidos no contrato (PA-02/PA-04).

**Parcela mensal em atraso (aluguel + encargos):** 2.000 + 200 = **R$ 2.200,00**.

| Competencia | Venc. | Base | Juros 1% a.m. (meses) | Multa 10% | Total |
|---|---|---|---|---|---|
| 03/2026 | 10/03 | 2.200,00 | 66,00 (3 m) | 220,00 | 2.486,00 |
| 04/2026 | 10/04 | 2.200,00 | 44,00 (2 m) | 220,00 | 2.464,00 |
| 05/2026 | 10/05 | 2.200,00 | 22,00 (1 m) | 220,00 | 2.442,00 |

**Debito total ate 16/06/2026 = 2.486 + 2.464 + 2.442 = R$ 7.392,00.**
(Juros calculados do vencimento ate a data-base; multa de 10% sobre cada parcela.)

**PURGACAO DA MORA (art. 62, II) — total a depositar em 15 dias:**
```
Debito acima (alugueis/encargos + multa + juros) ... R$ 7.392,00
+ Competencia 06/2026 a vencer ate o deposito ...... R$ 2.200,00   (art. 62, II — vincendas)
+ Custas processuais (estimativa) .................. R$   180,00
+ Honorarios advocaticios (10%) .................... R$   739,20
= TOTAL DA PURGACAO ................................ R$ 10.511,20
```
Conferir o direito: nao houve purgacao nos **24 meses** anteriores (art. 62, par. unico); do contrario, o beneficio nao cabe. Atualizar juros/competencias ate a **data efetiva** do deposito.

## 8. SAIDA

Sempre: tabela passo a passo, indice e multa **identificados pela clausula**, data-base, total destacado. Marcar `DADO FALTANTE` no que nao houver. Integra os pedidos liquidos da peca (`estilo-juridico-imobiliario`).
