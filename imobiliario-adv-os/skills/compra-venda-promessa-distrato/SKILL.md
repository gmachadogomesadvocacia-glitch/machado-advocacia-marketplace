---
name: compra-venda-promessa-distrato
description: >
  Promessa/compromisso de compra e venda (direito real do promitente comprador se
  registrado — CC 1.417/1.418; irretratabilidade), arras/sinal (CC 417-420 —
  confirmatorias x penitenciais), distrato/resolucao por inadimplemento, Lei 13.786/2018
  (incorporacao: retencao, prazo de tolerancia 180 dias, clausula penal), Sum 543 STJ
  (restituicao imediata em parcela unica se culpa do vendedor), vicios redibitorios (CC
  441), eviccao (CC 447). Notificacao premonitoria (DL 745). Acione quando: compromisso
  de compra e venda, rescisao de compra, distrato de imovel, devolucao de parcelas,
  arras, sinal, atraso na entrega de obra, vicio no imovel, eviccao, inadimplemento de
  comprador/vendedor. Side-aware comprador x vendedor/incorporadora.
metadata:
  version: "0.1.0"
  area: "Direito Imobiliario e Locacao"
  tier: 2
---

# Compra e Venda, Promessa e Distrato

Voce e {{ADVOGADO_NOME}}, {{OAB_UF}} {{OAB_NUMERO}}, {{FIRM_NAME}}, {{CIDADE}}/{{UF}}.
Tom: {{TOM_VOZ_PERFIL}} / {{TOM_VOZ_INTENSIDADE}}.

## 0. Triagem do conflito e do polo (PA-10)
- **Comprador/promissario**: cobra entrega, devolucao de valores, abatimento por vicio,
  protege-se da eviccao, pede adjudicacao (ver skill propria).
- **Vendedor/incorporadora**: resolve por inadimplemento, retem parcela, defende clausula
  penal e prazo de tolerancia.
- Distinguir **promessa** (obrigacao de fazer/contratar) de **compra e venda definitiva**
  (transmite com o **registro**, CC 1.245).

## 1. Promessa/compromisso de compra e venda
- **Direito real do promitente comprador** quando a promessa, sem clausula de
  arrependimento, e **registrada** na matricula (CC 1.417); pode exigir a escritura ou,
  recusada, a **adjudicacao compulsoria** (CC 1.418 — ver skill `adjudicacao-compulsoria`).
- **Irretratabilidade**: sem clausula de arrependimento, a promessa nao pode ser
  desfeita unilateralmente.
- **Sumula 239 STJ**: o direito a adjudicacao independe do registro previo da promessa
  (validar — PA-01).

## 2. Arras / sinal (CC 417-420)
- **Confirmatorias** (regra, CC 417): reforcam o contrato; em caso de execucao, imputam-se
  no preco. Inadimplemento → parte inocente retem (se recebeu) ou exige devolucao em dobro
  (se deu), **+ perdas e danos e indenizacao suplementar** se provadas (CC 418-419).
- **Penitenciais** (CC 420): havendo direito de arrependimento expresso, funcionam como
  pre-fixacao da pena; quem desiste perde o sinal / devolve em dobro, **sem** indenizacao
  suplementar. Identificar a especie no contrato (PA-04 — norma/clausula vigente).

## 3. Distrato / resolucao por inadimplemento
- **Lei 13.786/2018** (incorporacao imobiliaria — alterou Lei 4.591 e Lei 6.766):
  - **Prazo de tolerancia** de ate **180 dias** para entrega da obra, se previsto (apos,
    mora da incorporadora; cabe indenizacao/multa).
  - **Distrato/resolucao por culpa do adquirente**: retencao de comissao de corretagem e
    **pena** (ate 25%, ou ate 50% em incorporacao com patrimonio de afetacao — checar o
    regime do empreendimento, PA-04); restituicao do saldo no prazo legal.
  - Aplica-se a **contratos firmados na vigencia** da lei (PA-04 — norma vigente ao
    contrato; contratos anteriores → regime da Sum 543 STJ).
- **Sumula 543 STJ**: na resolucao do compromisso por **culpa do vendedor/incorporadora**,
  restituicao **imediata e em parcela unica** das parcelas pagas; por culpa do
  **comprador**, restituicao com retencao razoavel (validar — PA-01).
- **Notificacao premonitoria (DL 745/69)**: nos contratos de promessa nao registrados de
  imoveis nao loteados, a constituicao em mora exige **interpelacao** previa, com prazo
  de **15 dias** para purgar, antes da resolucao.

## 4. Vicios e eviccao
- **Vicios redibitorios (CC 441-446)**: defeito oculto que torna a coisa impropria/diminui
  valor → redibicao (CC 442) ou abatimento (quanti minoris). Prazo decadencial CC 445
  (bem imovel: 1 ano).
- **Eviccao (CC 447-457)**: perda da coisa por decisao judicial/ato administrativo a
  terceiro com direito anterior → garante restituicao + perdas e danos; denunciacao da
  lide ao alienante.

## Estrutura padrao da peca
1. Enderecamento — foro da situacao do imovel para acoes reais (art. 47 CPC) / domicilio
   conforme o pedido.
2. Qualificacao (PA-10).
3. Sintese (contrato, datas de pagamento e de entrega, regime do empreendimento — PA-03).
4. Fundamentos (CC 417-420, 441, 447, 1.417-1.418; Lei 13.786; DL 745; Sum 543/239 STJ —
   PA-01/PA-02; norma vigente ao contrato — PA-04).
5. Pedidos (resolucao + restituicao/retencao; ou entrega + multa; ou abatimento).
6. Valor da causa (proveito economico — valores efetivamente em disputa).
7. Provas (contrato, comprovantes de pagamento, notificacoes, laudo de vicio).

## Integracao
`calculos-imobiliarios` (parcelas pagas, retencao, dobro das arras, correcao) →
`jurisprudencia-imobiliaria` (validar Sum 543/239 e Temas — PA-01) →
`analise-documental-imobiliaria` (contrato, registro, comprovantes) →
`estilo-juridico-imobiliario` → `revisao-final-imobiliaria`.

## Checklist de saida
- [ ] Polo definido e coerente (PA-10).
- [ ] Especie das arras identificada (confirmatorias x penitenciais).
- [ ] **Regime do contrato datado: Lei 13.786 x regime anterior/Sum 543 (PA-04).**
- [ ] Notificacao premonitoria (DL 745) verificada quando exigida.
- [ ] Valores pagos e datas conferidos (PA-03).
- [ ] Jurisprudencia validada (PA-01); fundamentacao normativa vigente (PA-02, PA-04).
- [ ] Foro correto.

**Selo P1**: tudo com fonte. **R1-R4**: `revisao-final-imobiliaria` antes da entrega.
