---
name: registro-carta-arrematacao
description: >
  Registro da carta de arrematacao Tier 2 — carta, ITBI, registro na matricula e baixa dos gravames. Acione depois de aperfeicoada a arrematacao, para consolidar a propriedade no nome do cliente.
metadata:
  version: "0.1.0"
  area: "Leiloes e Arrematacao"
  tier: 2
---

# REGISTRO DA CARTA DE ARREMATACAO

> Tier 2. Fecha o ciclo: sem registro, o cliente arrematou mas nao e proprietario.

## 1. A CARTA (CPC 901)

Expedida **apos** o deposito ou as garantias, o pagamento da **comissao do leiloeiro** e das despesas da execucao (§ 1º), e **apos** vencidos os 10 dias do art. 903, § 2º, sem alegacao (§ 3º).

**Conteudo obrigatorio (§ 2º)**: descricao do imovel, **remissao a matricula e aos registros**, copia do auto de arrematacao, **prova de pagamento do ITBI** e **indicacao da existencia de eventual onus real ou gravame**.

Conferir cada item antes de levar a registro — carta incompleta volta com exigencia do oficial e custa semanas.

## 2. ITBI

Recolhido pelo arrematante, com base e aliquota do municipio do imovel; a prova integra a carta. Divergencia sobre a base de calculo (valor da arrematacao x valor venal) e materia tributaria: rotear a `tributario-adv-os` se virar litigio.

## 3. REGISTRO E BAIXA DE GRAVAMES

Levar a carta ao **registro de imoveis da circunscricao**. Junto com o registro da aquisicao, requerer:

- **cancelamento da hipoteca** — extinta pela arrematacao (CC 1.499, VI), com a averbacao a vista da prova (CC 1.500);
- **baixa das penhoras** sub-rogadas no preco (CPC 908, § 1º), instruindo com a certidao do juizo;
- baixa de indisponibilidades e constricoes ja resolvidas.

Havendo exigencia do oficial, avaliar **duvida registral** (Lei 6.015) antes de discutir no juizo da execucao.

## 4. NA VIA FIDUCIARIA

Nao ha carta de arrematacao: o titulo e a **escritura ou o contrato de compra e venda** firmado com o credor fiduciario apos o leilao, levado a registro com o ITBI do adquirente. Conferir se a **consolidacao** foi averbada antes (art. 26, § 7º) — sem ela, o credor nao podia vender.

## 5. CHECKLIST FINAL DO CASO

- [ ] carta registrada e matricula em nome do cliente
- [ ] gravames baixados, um a um
- [ ] posse obtida
- [ ] debitos anteriores impugnados ou quitados conforme a analise
- [ ] `CASO.md` encerrado com o custo real **efetivo** (comparar com o estimado no parecer — e assim que a proxima due diligence fica melhor)
