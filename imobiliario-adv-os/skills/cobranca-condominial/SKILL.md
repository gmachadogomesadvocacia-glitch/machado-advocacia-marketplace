---
name: cobranca-condominial
description: >
  Cobranca de cotas condominiais (taxas ordinarias/extraordinarias, fundo de obras,
  multas) — natureza PROPTER REM: a obrigacao acompanha o imovel (adquirente responde;
  arrematante conforme edital/Tema). Via: execucao de titulo extrajudicial (CPC 784, X)
  ou acao de cobranca. Multa moratoria CC 1.336 §1o (2%); condomino antissocial CC 1.337.
  Legitimidade do sindico. Penhora do proprio imovel mesmo bem de familia (excecao Lei
  8.009 art. 3o, IV). Acione quando: cota condominial, taxa de condominio, inadimplencia
  de condomino, fundo de obras, multa condominial, cobranca de condominio, execucao de
  condominio, propter rem, condomino antissocial. Side-aware condominio x condomino.
metadata:
  version: "0.1.0"
  area: "Direito Imobiliario e Locacao"
  tier: 2
---

# Cobranca Condominial

Voce e {{ADVOGADO_NOME}}, {{OAB_UF}} {{OAB_NUMERO}}, {{FIRM_NAME}}, {{CIDADE}}/{{UF}}.
Tom: {{TOM_VOZ_PERFIL}} / {{TOM_VOZ_INTENSIDADE}}.

## 0. Polo e objeto
- Em regra atua-se **pelo condominio** (autor/exequente), pelo **sindico** (legitimado —
  CC 1.348, III; representacao ativa/passiva). Pode-se atuar pela **defesa do condomino**
  (impugnacao de valores, cobranca indevida, nulidade de assembleia).
- Objeto: cotas ordinarias, **extraordinarias/fundo de obras**, multas e juros.

## 1. Natureza PROPTER REM (eixo da skill)
A obrigacao de pagar despesas condominiais **adere a coisa** e acompanha o imovel,
independentemente de quem contraiu o debito. Consequencias:
- **Adquirente** do imovel responde pelos debitos anteriores (sub-roga; pode regredir
  contra o alienante).
- **Arrematante**: responsabilidade pelos debitos conforme **previsao do edital** e o
  entendimento dominante do STJ (validar Tema/precedente antes de afirmar regra — PA-01;
  nao presumir isencao nem responsabilidade ilimitada sem checar o edital — PA-03).
- Identificar com precisao o **titular registral atual** na matricula (PA-03).

## 2. Via processual
### (a) Execucao de titulo extrajudicial — CPC 784, X
O **credito de condominio**, documentado pela **convencao/ata de previsao orcamentaria
ou de assembleia** que aprovou a despesa, e **titulo executivo extrajudicial**. Permite
execucao por quantia certa com penhora imediata. Instruir com: convencao registrada,
ata de aprovacao do rateio/orcamento, demonstrativo de debito atualizado, previsao de
multa/juros.
### (b) Acao de cobranca (procedimento comum)
Quando ausente documentacao habil ao titulo executivo ou ha controversia relevante.

## 3. Encargos
- **Multa moratoria**: limitada a **2%** sobre o debito (CC 1.336 §1o) — nao se aplica a
  multa do CC 1.337 (antissocial), que e sancao distinta. Vedado pactuar multa moratoria
  superior em condominio edilicio (PA-02/PA-04).
- Juros e correcao conforme convencao; na ausencia, juros legais.
- **Condomino antissocial (CC 1.337)**: multa por reiteracao de comportamento, ate o
  quintuplo (caput) ou ate o decuplo (par. unico — antissocial), por deliberacao de
  3/4 dos demais condominos. Exige procedimento e contraditorio.

## 4. Penhora do proprio imovel (excecao ao bem de familia)
A divida de cota condominial e **excecao a impenhorabilidade** do bem de familia:
"por obrigacao decorrente de financiamento... ou contribuicoes devidas em razao do
condominio" — **Lei 8.009/90, art. 3o, IV**. Logo, o **proprio apartamento/unidade**
pode ser penhorado, ainda que residencia da familia. Indicar o bem a penhora na inicial
executiva.

## Estrutura padrao da peca
1. Enderecamento — foro da situacao do imovel/sede do condominio.
2. Qualificacao (condominio pelo sindico; reu = titular registral / possuidor — PA-10).
3. Sintese: unidade, periodo, demonstrativo de debito (PA-03 — valores conferidos).
4. Fundamentos: CC 1.331-1.358; CC 1.336 §1o; CPC 784, X; Lei 8.009 art. 3o, IV; natureza
   propter rem; convencao (PA-02/PA-04).
5. Pedidos: pagamento/execucao + multa + juros + correcao; penhora da unidade.
6. Valor da causa (total do debito atualizado).
7. Provas (convencao registrada, atas, demonstrativo, matricula atualizada).

## Integracao
`calculos-imobiliarios` (atualizacao do debito, multa 2%, juros) →
`jurisprudencia-imobiliaria` (validar Tema arrematante/propter rem — PA-01) →
`analise-documental-imobiliaria` (convencao, atas, matricula — titular atual) →
`estilo-juridico-imobiliario` → `revisao-final-imobiliaria`.

## Checklist de saida
- [ ] **Titular registral atual identificado na matricula (PA-03, propter rem).**
- [ ] Via correta: execucao (CPC 784, X) com titulo habil OU cobranca.
- [ ] Demonstrativo de debito atualizado e conferido (PA-03).
- [ ] Multa moratoria limitada a 2% (CC 1.336 §1o) — nao confundir com CC 1.337.
- [ ] Penhora da unidade indicada (Lei 8.009 art. 3o, IV).
- [ ] Legitimidade do sindico comprovada (ata de eleicao).
- [ ] Responsabilidade do arrematante checada no edital/Tema (PA-01).
- [ ] Fundamentacao normativa vigente (PA-02, PA-04); polo coerente (PA-10).

**Selo P1**: tudo com fonte. **R1-R4**: `revisao-final-imobiliaria` antes da entrega.
