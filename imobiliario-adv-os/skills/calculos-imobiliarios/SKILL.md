---
name: calculos-imobiliarios
description: >
  Calculos imobiliarios Tier 1 — nucleo de calculo do plugin. Produz memoria de calculo passo a passo,
  com datas, para: (a) debito locaticio (alugueis + encargos IPTU e condominio + reajuste pelo indice
  contratual IGP-M/IPCA + multa moratoria + juros); (b) purgacao da mora (art. 62 — total a depositar);
  (c) revisional (aluguel a mercado); (d) restituicao no distrato (Lei 13.786 — retencao de ate
  25%/50% na incorporacao + comissao; Sum. 543); (e) restituicao/abatimento por vicios; (f) saldo na
  alienacao fiduciaria apos leilao (art. 27 §4º — devolucao do excedente). Nao inventa valores, datas
  ou indices (PA-03). Ative ao calcular debito de aluguel, purgacao, revisional, restituicao ou saldo.
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

## 7. SAIDA

Sempre: tabela passo a passo, indice e multa **identificados pela clausula**, data-base, total destacado. Marcar `DADO FALTANTE` no que nao houver. Integra os pedidos liquidos da peca (`estilo-juridico-imobiliario`).
