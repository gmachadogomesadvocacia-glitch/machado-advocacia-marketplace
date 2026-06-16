---
name: peticao-inicial-prev
description: >
  PETICAO INICIAL PREVIDENCIARIA — Skill Tier 2 A. Produz peticao inicial em acoes
  previdenciarias: concessoria de beneficio (B41/B42/B46/B31/B32/B21/B91/B87/B80),
  revisional de RMI, mandado de seguranca preventivo, acao de concessao de BPC/LOAS.
  Estrutura FIRAC + AIDA com fundamentacao em Lei 8.213/91, EC 103/2019, IN INSS,
  jurisprudencia TNU (vinculante para JEF), STJ e STF. Inclui pedido de tutela de urgencia
  quando cabivel. Acionar apos triagem-dogmatica + analise-trilateral + calculos-previdenciarios
  e jurisprudencia-estrategica. Suprema Corte R1-R4 aplicada automaticamente ao final.
---

# PETICAO INICIAL PREVIDENCIARIA
> Tier 2 — Contencioso | FIRAC + AIDA | JEF / JF | Suprema Corte automatica

---

## 0. PRE-REQUISITOS

Antes de produzir a peca:
- triagem-dogmatica: concluida (especie, categoria, regra, competencia)
- analise-trilateral: concluida (fato/nexo/direito validados)
- calculos-previdenciarios: RMI projetada (para valor da causa)
- jurisprudencia-estrategica: teses selecionadas (TNU/STJ/STF com numeros e datas)

Se algum pre-requisito estiver incompleto, reportar e aguardar antes de produzir.

---

## 1. ESTRUTURA FIRAC + AIDA

### FIRAC
```
F — Fatos: cronologia do segurado, vinculos, contribuicoes, adoecimento/exposicao
I — Issue: qual direito esta em disputa (concessao, revisao, manutencao)
R — Regra: normas aplicaveis (Lei 8.213, EC 103, IN INSS, sumulas TNU/STJ/STF)
A — Aplicacao: como a regra se aplica aos fatos do caso especifico
C — Conclusao: pedidos concretos em alineas
```

### AIDA (narrativa da peca)
```
A — Atencao: fato impactante que abre a peca (o que aconteceu com o segurado)
I — Interesse: por que isso viola o direito previdenciario
D — Desejo: o que o juiz deve fazer para corrigir
A — Acao: pedidos concretos e imediatos
```

---

## 2. TEMPLATE ESTRUTURAL

> CHASSI (padrao enxuto da casa): abrir `templates/pecas/peticao-inicial-concessao-beneficio.md`
> antes de redigir a inicial de concessao/restabelecimento contra o INSS e substituir os
> placeholders `[____]`. O esqueleto abaixo e referencia rapida; a fonte unica e o chassi.


```
[Exmo. Sr. Dr. Juiz Federal do Juizado Especial Federal / da [X]a Vara Federal de [Comarca]]

[Autor: Nome completo, CPF, NIT, qualificacao, endereco, representado pelo advogado
        [Nome], OAB/[UF] n. [numero], endereco para intimacoes]
[Reu: INSTITUTO NACIONAL DO SEGURO SOCIAL — INSS, autarquia federal, CNPJ [numero],
      representado pela Procuradoria Federal]

vem propor

ACAO DE CONCESSAO DE [BENEFICIO] / ACAO REVISIONAL DE RMI

pelos fatos e fundamentos a seguir:

I — DOS FATOS [F do FIRAC — cronologia + matriz trilateral]

II — DO DIREITO [R + A do FIRAC]
  II.1 — Da normativa aplicavel (Lei 8.213/91 + EC 103/2019 + IN INSS 128/2022)
  II.2 — Da jurisprudencia (TNU sumula + STJ tema + STF tema, com numeros e datas)
  II.3 — Da aplicacao ao caso concreto

III — DA TUTELA DE URGENCIA (se cabivel)
  fumus boni iuris: [demonstrar o direito aparente]
  periculum in mora: [carater alimentar — art. 6o CF]
  Referencia: art. 300 CPC + jurisprudencia especifica

IV — DOS PEDIDOS
  a) Concessao da tutela de urgencia para implantacao imediata de [BENEFICIO];
  b) Julgamento procedente para condenar o INSS a conceder [BENEFICIO] a partir de [DIB correta];
  c) Pagamento de [beneficio] vencido desde [data], com correcao pelo INPC e juros de mora
     na forma do art. 1o-F da Lei 9.494/97;
  d) Condenacao em honorarios advocaticios (art. 85 CPC);
  e) [pedidos especificos: dispensa de pericia / realizacao de pericia / inversao do onus da prova].

V — DO VALOR DA CAUSA
  R$ [soma das parcelas vencidas nos ultimos 5 anos] ([valor por extenso])

VI — DAS PROVAS
  Documental: [lista] / Pericial / Testemunhal (se cabivel)

[Local, data]
[Advogado — OAB]
```

---

## 3. ADAPTACOES POR ESPECIE

### 3.1 Aposentadoria Especial (B46) — Tema 555 STF

```
Incluir obrigatoriamente em II.2:
"Quanto ao EPI, o Supremo Tribunal Federal, no julgamento do Tema 555 (ARE 664.335,
Tribunal Pleno, Rel. Min. Luiz Fux, j. 04/12/2014), fixou que o fornecimento de EPI
eficaz nao afasta o reconhecimento da especialidade quando o agente nocivo e o RUIDO,
pois o dano auditivo e irreversivel e o EPI apenas reduz a exposicao, sem eliminar o risco."
```

### 3.2 BPC/LOAS (B56/B87) — Miserabilidade Subjetiva

```
Incluir em II.2 quando renda per capita supera 1/4 SM:
"O STF, no Tema 529 (RE 580.963, Tribunal Pleno, j. 18/04/2013), reconheceu que o
criterio objetivo de renda per capita de 1/4 do salario minimo nao e o unico criterio
para aferimento da miserabilidade, podendo o juiz considerar outros elementos de prova
que demonstrem a situacao de vulnerabilidade social."
```

### 3.3 Concessao Concessoria Pos-EC 103 — Regra de Transicao

```
Identificar a regra de transicao mais favoravel (acionar calculos-previdenciarios)
e demonstrar o preenchimento de cada requisito com dados do CNIS.
Calcular a RMI projetada pelas diferentes regras e justificar a escolhida.
```

---

## 4. CHECKLIST PRE-ENVIO (Suprema Corte R4)

```
□ Qualificacao completa do autor (CPF, NIT, endereco)?
□ INSS identificado como reu com CNPJ?
□ Fatos com cronologia completa (FIRAC)?
□ Fundamentacao com artigo especifico da Lei 8.213/91?
□ EC 103/2019 aplicada corretamente (regra de transicao)?
□ Jurisprudencia TNU com numero da sumula e data?
□ Pedidos em alineas (a, b, c, d)?
□ Valor da causa calculado (parcelas dos ultimos 5 anos)?
□ Documentos listados como provas?
□ Tutela de urgencia incluida se beneficio alimentar em risco?
```
