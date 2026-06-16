---
name: repeticao-indebito-compensacao
description: >
  Conduz restituicao de tributo pago indevidamente ou a maior (CTN 165-168) e
  compensacao tributaria (CTN 170; Lei 9.430/96 art. 74 — PER/DCOMP federal).
  Aciona quando o cliente pagou tributo indevido/a maior, quer reaver valores,
  compensar creditos com debitos, ou recuperar indebito reconhecido em decisao.
  Cobre prazo de 5 anos (CTN 168; LC 118/2005 — termo no lancamento por
  homologacao; tese dos 5+5 superada para pagamentos pos-LC 118 — validar),
  legitimidade na repeticao de tributos indiretos (CTN 166), via administrativa
  (PER/DCOMP, restituicao) x judicial (acao de repeticao + compensacao) e
  correcao pela SELIC. Lado padrao: contribuinte.
metadata:
  version: "0.1.0"
  area: "Direito Tributario"
  tier: 2
---

# Repeticao de Indebito e Compensacao

Recuperacao de tributo **pago indevidamente ou a maior** (restituicao —
CTN 165) e **compensacao** com debitos (CTN 170). Lado padrao: **contribuinte**.

## Hipoteses de indebito (CTN 165)
- Pagamento de tributo indevido/maior que o devido (erro de fato/direito).
- Pagamento com base em norma depois julgada inconstitucional/ilegal.
- Erro na identificacao do sujeito passivo, aliquota, base de calculo etc.

## Prazo: 5 anos (CTN 168; LC 118/2005)
- **Regra geral (CTN 168):** 5 anos para pleitear a restituicao, contados da
  **extincao do credito** (pagamento).
- **Lancamento por homologacao + LC 118/2005:** a LC 118 fixou que, para esses
  tributos, o prazo de 5 anos conta do **pagamento antecipado** (art. 3o).
- **Tese dos "5+5"** (5 da homologacao tacita + 5 da repeticao): **superada**
  pelo STF para pagamentos **posteriores** a vigencia da LC 118 (RE 566.621 —
  validar); para pagamentos anteriores, transicao. **PA-04 / PA-05:** aplicar a
  regra conforme a data do pagamento; nao confundir com decadencia do Fisco.
- Em **acao judicial** que reconhece o indebito, o prazo dos creditos a
  restituir/compensar segue a mesma logica quinquenal (PA-09).

## Tributos indiretos — CTN 166
Tributos que **comportam transferencia do encargo** (ex.: ICMS, IPI): so cabe
restituicao a quem **provar nao ter repassado** o encargo ao terceiro, ou estar
**autorizado** por quem o suportou (CTN 166; Sumula 546/STF — validar).
Exigencia probatoria forte — **PA-03:** so afirmar nao repasse com prova.

## Compensacao (CTN 170; Lei 9.430/96, art. 74)
- **Federal — PER/DCOMP** (Lei 9.430/96, art. 74): o contribuinte declara a
  compensacao de creditos (indebito, saldo negativo, etc.) com debitos proprios,
  sob condicao resolutoria de **homologacao** pelo Fisco (prazo de 5 anos para
  homologar/glosar — validar).
- **Limites:** ha debitos **nao compensaveis** por lei (ex.: certas contribui-
  coes previdenciarias, debitos de terceiros, debitos com exigibilidade
  suspensa por nao homologacao) — **validar a vedacao vigente** antes de
  orientar (PA-06 — orientar so o licito).
- **Compensacao de indebito reconhecido em juizo:** depende do **transito em
  julgado** (CTN 170-A) — nao compensar antes (validar).
- **Sumula 213/STJ:** MS e via para **declarar** o direito a compensacao;
  **Sumula 460/STJ:** MS nao **convalida** a compensacao (ver
  `mandado-seguranca-tributario`).

## Via administrativa x judicial
- **Administrativa:** pedido de **restituicao/ressarcimento** ou **PER/DCOMP**
  (federal); equivalente no ente estadual/municipal (validar). Mais rapida; mas
  sujeita a glosa/nao homologacao.
- **Judicial:** **acao de repeticao de indebito** (rito comum) com pedido de
  restituicao e/ou **declaracao do direito a compensacao**; ou **MS** quando o
  direito for liquido e certo (declara o direito — Sum. 213). Escolha conforme
  prova, montante e risco de glosa.

## Correcao — SELIC
Na esfera federal, o indebito e atualizado pela **taxa SELIC** desde o pagamento
indevido (que ja engloba correcao + juros, vedada cumulacao com outros indices —
validar). Estadual/municipal: conferir indice do ente. Calculo →
`calculos-tributarios`.

## Estrutura (acao de repeticao)
1. Enderecamento (JF para tributo federal; Vara da Fazenda para estadual/
   municipal).
2. Qualificacao (autor-contribuinte; re-Fazenda/ente).
3. Sintese factica — pagamentos, fundamento do indebito, periodo, valores.
4. Fundamentos — ilegalidade/inconstitucionalidade; CTN 165/166; prazo.
5. Pedidos — restituicao e/ou declaracao do direito a compensacao
   (CTN 170-A se decorrente de indebito judicial); SELIC.
6. Valor da causa = montante a repetir/compensar (atualizado).
7. Provas — comprovantes de recolhimento; prova do nao repasse (indiretos).

## Proibicoes Absolutas aplicaveis
- **PA-01 / PA-02:** RE 566.621, Sum. 546, Temas — so consagrados e validados;
  nao inventar fundamentacao.
- **PA-03:** prova do pagamento e do nao repasse — nao alucinar.
- **PA-04 / PA-05:** prazo quinquenal correto; decadencia x prescricao; 5+5.
- **PA-06:** so compensacao **licita** — respeitar vedacoes e CTN 170-A.
- **PA-09:** repeticao/compensacao em 5 anos (CTN 168 / LC 118).
- **PA-10:** coerencia de polo. **PA-12:** sigilo fiscal + LGPD.

## Integracao e saida
- Quantum, SELIC, planilha de creditos → **calculos-tributarios**.
- Sumulas/Temas/REs → **jurisprudencia-tributaria** (validar, PA-01).
- Redacao/tom → **estilo-juridico-tributario** (persona literal).
- Pre-entrega → **revisao-final-tributaria** (Selo P1 + R1-R4).

### Checklist de saida
- [ ] Prazo de 5 anos aferido conforme data e tipo de lancamento.
- [ ] Tributo indireto: prova do nao repasse / autorizacao (CTN 166).
- [ ] Compensacao licita; CTN 170-A se indebito judicial.
- [ ] Via (admin/judicial/MS) adequada ao caso e a prova.
- [ ] SELIC/indice do ente; valor da causa correto.
- [ ] Polo e sigilo preservados.

**Lembrete:** **Selo P1** + auditoria **R1-R4** antes de entregar.
