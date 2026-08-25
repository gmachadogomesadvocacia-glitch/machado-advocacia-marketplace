---
name: imissao-na-posse-arrematante
description: >
  Imissao na posse do arrematante Tier 2 — obter a posse apos a arrematacao judicial, com mandado e, se preciso, forca policial. Acione quando o cliente arrematou e nao tem a posse do bem.
metadata:
  version: "0.1.0"
  area: "Leiloes e Arrematacao"
  tier: 2
---

# IMISSAO NA POSSE DO ARREMATANTE

> Tier 2. Via **judicial**. Para o leilao fiduciario, a porta e a reintegracao do art. 30 da Lei 9.514 — ver `leilao-extrajudicial-fiduciario`.

## 1. O TITULO

**CPC 901, § 1º**: expedidos, apos o deposito do preco e o pagamento da comissao do leiloeiro e das despesas, a **carta de arrematacao** do imovel **com o respectivo mandado de imissao na posse** — ou a ordem de entrega, no movel.

Ou seja: a imissao **acompanha** a carta, nao depende de acao nova. Se a secretaria expediu a carta sem o mandado, o pedido e simples e nos proprios autos.

## 2. CONFERIR ANTES DE PEDIR

- [ ] preco depositado e comissao paga (901, § 1º);
- [ ] **10 dias do art. 903, § 2º** vencidos sem alegacao — antes disso a carta nem sai (§ 3º);
- [ ] ITBI recolhido e prova nos autos (901, § 2º);
- [ ] quem esta na posse: executado, locatario, posseiro (muda a peca — ver `desocupacao-e-ocupantes`).

## 3. A PECA

Peticao nos autos da execucao, enxuta:
1. arrematacao aperfeicoada, com **data do auto** e valor (doc. N);
2. pagamento integral e comissao quitada (doc. N);
3. carta expedida ou requerimento de expedicao;
4. **pedido**: expedicao/cumprimento do mandado de imissao, com prazo para desocupacao voluntaria;
5. subsidiariamente, **forca policial e ordem de arrombamento**, se houver resistencia — pedido fundamentado, nunca genérico;
6. se ha ocupante que nao e o executado, requerer a citacao/intimacao dele.

## 4. RESISTENCIA E LIMITES

- Recurso ou embargos do executado **nao** desfazem a arrematacao: ela e perfeita, acabada e irretratavel (903, caput), e eventual procedencia se resolve em **reparacao de prejuizos**.
- O executado costuma pedir prazo humanitario; avaliar acordo (custo x tempo) com a `linha-estrategica-leiloes`.
- **PA-08**: nada de troca de fechadura, corte de agua ou luz, ou remocao por conta propria. A posse se obtem por mandado.

## 5. DEPOIS DA POSSE

Registro da carta, baixa dos gravames e ITBI: `registro-carta-arrematacao`. Debitos que apareceram: `debitos-e-onus-propter-rem`.
