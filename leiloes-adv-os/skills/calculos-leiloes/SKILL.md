---
name: calculos-leiloes
description: >
  Calculos de leiloes Tier 1 — custo real de aquisicao, comissao por rito, ITBI, prazos e conferencia do saldo fiduciario. Acione quando o caso exigir numero: quanto custa arrematar, quanto sobra, qual a data-limite.
metadata:
  version: "0.1.0"
  area: "Leiloes e Arrematacao"
  tier: 1
---

# CALCULOS DE LEILOES

> Tier 1. Todo numero sai com **premissa declarada** e fonte. Estimativa vem rotulada como estimativa.

## 1. CUSTO REAL DE AQUISICAO

```
  lance
+ comissao do leiloeiro
+ ITBI                       (aliquota do municipio do imovel)
+ custas, emolumentos, registro da carta
+ debitos que nao sub-rogam ou de sub-rogacao duvidosa
+ desocupacao                (acao + tempo + eventual acordo)
+ reforma e regularizacao
+ carrego ate a revenda      (IPTU + condominio)
= CUSTO REAL
```

Comparar com o valor de mercado **liquido**, nunca com a avaliacao judicial (que costuma ser desatualizada).

## 2. COMISSAO DO LEILOEIRO — POR RITO

- **CPC 884, p.u.**: o leiloeiro recebe **do arrematante** a comissao "estabelecida em lei ou arbitrada pelo juiz".
- **Dec. 21.981/32, art. 24**: na falta de estipulacao, 5% sobre moveis e **3% sobre imoveis**; o paragrafo unico manda os compradores pagarem 5% sobre quaisquer bens arrematados.
- **RMS 65.084**: piso de 5% — **julgado isolado**.
- **Execucao fiscal**: art. 23, § 2º, da Lei 6.830/80 poe a comissao no arrematante.

**Regra:** o **edital manda**. Na ausencia, apresentar a faixa (3% a 5%) como faixa, nunca como numero certo. Calcular o cenario conservador (5%).

## 3. PISO DO LANCE — DEPENDE DO RITO

- **CPC, fiscal e trabalhista:** vil = inferior ao minimo do edital; **sem minimo fixado**, inferior a **50% da avaliacao** (CPC 891, p.u.).
- **SFH (Lei 5.741/1971):** o piso e o **SALDO DEVEDOR** (art. 6º), nao a avaliacao. **Nao aplicar o art. 891 aqui.** Pedir sempre os dois numeros e apresentar a razao `saldo / avaliacao`: acima de 1,0 a arrematacao por terceiro ja e economicamente inviavel, e o desfecho provavel e a adjudicacao ao credor em 48 horas (art. 7º). O saldo costuma ser atualizado ate a data do leilao, entao o piso tende a **subir**.
- **Fiduciaria:** nao existe preco vil — vale o referencial do art. 27, § 2º, da Lei 9.514/97.
- **Venda direta judicial:** o piso e o **percentual fixado no edital** (40% da avaliacao e o
  usual na Justica do Trabalho). **Nao e preco vil**, ainda que abaixo de 50%: o art. 891
  so reputa vil o valor inferior ao minimo estipulado pelo juiz **quando ha minimo fixado**,
  e aqui ha. Registrar isso no parecer, porque o cliente costuma estranhar o desconto.
  Somar sempre a **comissao de 5% do credenciado**, que e paga pelo comprador **sobre o
  valor total da compra**, e conferir no edital o **sinal** (20% a vista, 25% parcelado, no
  padrao CAEX) e o **prazo do saldo** — em regra **24 horas**, o que exige caixa disponivel,
  nao promessa de crédito.

## 4. PARCELAMENTO (CPC 895)

Ate o inicio do 1º leilao, proposta nao inferior a avaliacao; ate o inicio do 2º, valor nao vil. Sempre **25% a vista** e o restante em **ate 30 meses**, com hipoteca do proprio imovel. Atraso: multa de 10% sobre a parcela inadimplida somada as vincendas. A proposta a vista **sempre** prevalece.

## 5. VIA FIDUCIARIA — CONFERIR O QUE O CREDOR SOMOU

Referencial do 2º leilao (art. 27, § 2º): divida + despesas + premios de seguro + encargos legais, tributos e cotas condominiais. Nao havendo lance, o credor **pode** aceitar ao menos **metade da avaliacao**. Sobra: entregue ao fiduciante em 5 dias (§ 4º). Conferir a memoria de calculo do credor item a item — e ali que aparecem despesas infladas.

## 6. PRAZOS — CALCULAR A DATA, NAO O NUMERO

Toda contagem sai com **data-limite** no calendario e a data do marco conferida no documento: 10 dias do art. 903 (§§ 2º e 5º), 24 horas da CLT 888, § 4º, 15 dias da purgacao, 60 dias do art. 27 e do art. 30.

**PA-07:** nunca converter esses numeros em promessa de lucro ou rentabilidade.
