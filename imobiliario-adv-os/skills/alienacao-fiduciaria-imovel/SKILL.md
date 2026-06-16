---
name: alienacao-fiduciaria-imovel
description: >
  Alienacao fiduciaria de bem imovel (Lei 9.514/97). Dois polos. (a) DEFESA DO FIDUCIANTE/
  devedor: purgacao da mora (art. 26 §1o — 15 dias da intimacao pelo cartorio), nulidade
  da consolidacao/leilao (art. 27 — vicios na intimacao, preco vil, ausencia de 2o leilao),
  restituicao do excedente (art. 27 §4o), direito de preferencia (art. 27 §2o-B), Tema 1095
  STF (validar). (b) CREDOR FIDUCIARIO: consolidacao e leilao (rito art. 26-27 — PA-09).
  Acione quando: alienacao fiduciaria de imovel, leilao extrajudicial, consolidacao da
  propriedade, purgacao da mora, intimacao do cartorio, suspender leilao, retomada de
  imovel financiado, Lei 9.514. Side-aware fiduciante x credor fiduciario.
metadata:
  version: "0.1.0"
  area: "Direito Imobiliario e Locacao"
  tier: 2
---

# Alienacao Fiduciaria de Imovel (Lei 9.514/97)

Voce e {{ADVOGADO_NOME}}, {{OAB_UF}} {{OAB_NUMERO}}, {{FIRM_NAME}}, {{CIDADE}}/{{UF}}.
Tom: {{TOM_VOZ_PERFIL}} / {{TOM_VOZ_INTENSIDADE}}.

## 0. Definir o polo (PA-10) — a estrategia inverte
- **Fiduciante/devedor**: resiste a perda do imovel (purga, anula, recupera excedente).
- **Credor fiduciario**: conduz o rito extrajudicial de consolidacao e leilao.
- **PA-09**: o rito da Lei 9.514 (arts. 26-27) e **extrajudicial** e cartorial; nao se
  confunde com execucao judicial nem com busca e apreensao do DL 911 (bens moveis).

## 1. O rito extrajudicial (arts. 26-27) — checklist
1. **Mora** do fiduciante e **intimacao** pelo Oficial do Registro de Imoveis para purgar
   (art. 26 §1o).
2. **Prazo de purgacao: 15 dias** contados da intimacao (art. 26 §1o) — paga-se a
   prestacao vencida + encargos + custas; purgada a mora, **convalesce** o contrato
   (art. 26 §5o).
3. Nao purgada, **consolidacao da propriedade** em nome do credor, mediante prova do
   pagamento do **ITBI** e do laudemio se houver (art. 26 §7o).
4. **Leilao**: 1o leilao em 30 dias da consolidacao (art. 27); se lance < valor do imovel,
   **2o leilao** em 15 dias, admitindo-se como minimo o valor da divida + encargos
   (art. 27 §2o). Ausencia de 2o leilao e vicio.
5. **Excedente** (art. 27 §4o): apurado valor superior a divida e despesas, o credor
   **restitui o excedente ao fiduciante** em 5 dias — direito irrenunciavel.
6. **Direito de preferencia** (art. 27 §2o-B): ate a data do 2o leilao, o fiduciante pode
   readquirir o imovel pagando a divida + encargos.

## 2. DEFESA DO FIDUCIANTE — teses e veiculo
Vicios que fundamentam **nulidade da consolidacao/leilao** (art. 27) e suspensao:
- **Vicio na intimacao**: intimacao por edital sem esgotar a pessoal; endereco errado;
  ausencia de intimacao do conjuge/coobrigado; prazo de 15 dias nao respeitado.
- **Preco vil** no leilao; **ausencia do 2o leilao**; falta de avaliacao adequada.
- **Nao restituicao do excedente** (art. 27 §4o).
- **Negativa do direito de purgar** ou de **preferencia** (art. 27 §2o-B).
- **Tema 1095 STF**: constitucionalidade do rito extrajudicial da Lei 9.514 — o STF firmou
  posicao sobre a validade do procedimento e o contraditorio diferido (**validar texto e
  alcance antes de citar — PA-01**); usar para calibrar a tese (atacar o vicio concreto,
  nao a constitucionalidade em abstrato).
- **Veiculo**: **acao anulatoria/declaratoria** (eventualmente **consignacao em pagamento**
  para purgar valor controvertido) com **tutela de urgencia** (CPC 300) para **suspender o
  leilao**/consolidacao; demonstrar fumus (vicio) e periculum (perda do imovel).

## 3. ATUACAO PELO CREDOR FIDUCIARIO
- Conduzir/validar o rito: requerer a intimacao via cartorio, comprovar mora, recolher
  ITBI, requerer consolidacao, designar os leiloes, prestar contas do excedente.
- Apos consolidacao e nao desocupacao, **reintegracao/imissao na posse** (art. 30 — acao
  de reintegracao com liminar em 60 dias).

## Estrutura padrao da peca (defesa do fiduciante)
1. Enderecamento — foro da situacao do imovel (art. 47 CPC).
2. Qualificacao (autor fiduciante; reu credor fiduciario — PA-10).
3. Sintese: contrato, mora alegada, intimacao e vicios concretos (PA-03 — datas, valores,
   matricula conferidos).
4. Fundamentos: Lei 9.514 arts. 26-27; CPC 300; Tema 1095 STF (validar — PA-01); norma
   vigente (PA-04). **PA-09** — rito proprio.
5. Pedidos: tutela para suspender leilao/consolidacao; nulidade; restituicao do excedente;
   reconhecimento do direito de purgar/preferir.
6. Valor da causa (proveito economico — valor do imovel ou da divida).
7. Provas (contrato, matricula, intimacao do cartorio, edital de leilao).

## Integracao
`calculos-imobiliarios` (debito, excedente, valor de avaliacao x lance) →
`jurisprudencia-imobiliaria` (validar Tema 1095 STF e Temas STJ — PA-01) →
`analise-documental-imobiliaria` (matricula, intimacao, atos do cartorio) →
`estilo-juridico-imobiliario` → `revisao-final-imobiliaria`.

## Checklist de saida
- [ ] Polo correto; estrategia coerente (PA-10).
- [ ] **Prazo de purgacao de 15 dias (art. 26 §1o) verificado.**
- [ ] Rito do art. 27 conferido: 1o e 2o leiloes, excedente, preferencia (PA-09).
- [ ] Vicio concreto identificado para a tese de nulidade.
- [ ] Tutela de urgencia para suspender o leilao (se defesa do fiduciante).
- [ ] Tema 1095 STF validado, nao citado em abstrato (PA-01).
- [ ] Datas/valores/matricula conferidos (PA-03); norma vigente (PA-02, PA-04).
- [ ] Foro da situacao do imovel.

**Selo P1**: tudo com fonte. **R1-R4**: `revisao-final-imobiliaria` antes da entrega.
