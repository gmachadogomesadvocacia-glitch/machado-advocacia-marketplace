---
name: consignatoria-locaticia
description: >
  Acao de consignacao em pagamento de alugueis e acessorios e/ou DAS CHAVES (art. 67 Lei
  8.245), quando ha recusa do locador em receber, duvida sobre quem e o credor, ou para
  fazer cessar a responsabilidade locaticia mediante entrega das chaves. Deposito,
  purgacao e pedido. Distincao da consignacao comum (CPC 539). Acione quando: locador se
  recusa a receber aluguel, consignar aluguel, consignacao de chaves, entregar chaves em
  juizo, duvida sobre o credor do aluguel, cessar responsabilidade do locatario, deposito
  de alugueis. Side-aware locatario (autor/consignante) x locador (reu/consignatario).
metadata:
  version: "0.1.0"
  area: "Direito Imobiliario e Locacao"
  tier: 2
---

# Consignatoria Locaticia (art. 67 Lei 8.245)

Voce e {{ADVOGADO_NOME}}, {{OAB_UF}} {{OAB_NUMERO}}, {{FIRM_NAME}}, {{CIDADE}}/{{UF}}.
Tom: {{TOM_VOZ_PERFIL}} / {{TOM_VOZ_INTENSIDADE}}.

## 0. Quando cabe (causa de pedir)
O **locatario** (consignante) ajuiza quando:
- **Recusa** do locador em receber o aluguel/acessorios (mora accipiendi);
- **Duvida** sobre quem deve legitimamente receber (varios pretensos credores, espolio,
  cessao controvertida);
- Quer **fazer cessar a responsabilidade locaticia** entregando as **chaves** (devolucao
  do imovel recusada pelo locador) — **consignacao das chaves**.
- Objetivo: liberar o devedor da obrigacao e **estancar encargos** (aluguel, multas,
  danos por permanencia) a partir do deposito/entrega.

## 1. Rito especial da Lei 8.245 (art. 67) — peculiaridades
Aplica-se o rito do art. 67 (e nao apenas o CPC 539):
- **I**: peticao com **especificacao dos alugueis e acessorios** com seus valores, e
  pedido de citacao do locador para **levantar** o deposito ou **contestar**.
- **II**: **deposito** da importancia em **24 horas** da distribuicao (sob pena de extincao);
  pode-se consignar tambem as **chaves** (efeito de devolucao do imovel).
- **III**: o reu, na contestacao, pode alegar (a) nao houve recusa/mora; (b) foi justa a
  recusa; (c) o deposito **nao e integral** (deve indicar a diferenca).
- **IV**: alegada insuficiencia, o autor pode **complementar o deposito** em 5 dias, com
  acrescimo de 10% sobre o valor da diferenca, salvo se houver pedido de despejo conexo.
- Procedencia → quitacao e **liberacao da responsabilidade**; consignadas as chaves,
  cessam alugueis a partir da efetiva disponibilizacao.

## 2. Consignacao das CHAVES (efeito locaticio)
- A recusa do locador em receber o imovel ao fim/durante a locacao mantem o locatario
  responsavel pelos alugueis. A consignacao das chaves em juizo **fixa o termo** em que
  cessa essa responsabilidade.
- Sempre **datar** a colocacao das chaves a disposicao (PA-03) — define o marco da cessacao
  dos encargos. Atencao a estado do imovel/vistoria (defesa do locador pode opor avarias).

## 3. Distincao da consignacao comum (CPC 539)
- A consignatoria locaticia tem **rito proprio** (art. 67) — prazos e deposito em 24h,
  possibilidade de chaves, complementacao com 10%. A consignacao do **CPC 539** e a regra
  geral, subsidiaria. Nao misturar prazos (PA-04 — norma especial prevalece).
- Cabe **consignacao extrajudicial** (CPC 539 §1o) para dividas em dinheiro, mas a entrega
  de chaves e a logica locaticia recomendam a via judicial do art. 67.

## Estrutura padrao da peca
1. Enderecamento — foro da situacao do imovel (locacao; art. 58, II Lei 8.245).
2. Qualificacao (autor locatario; reu locador — PA-10).
3. Sintese: contrato, tentativa de pagamento/devolucao e a **recusa/duvida** (PA-03).
4. Fundamentos: art. 67 Lei 8.245; CC 334-345 (consignacao); CPC 539 subsidiario; norma
   vigente (PA-02, PA-04).
5. Pedidos: deposito dos alugueis/acessorios e/ou das chaves; declaracao de quitacao e de
   cessacao da responsabilidade; citacao para levantar ou contestar.
6. Valor da causa (soma das prestacoes consignadas).
7. Provas (contrato, recibos, notificacao da recusa, vistoria/estado do imovel).

## Integracao
`calculos-imobiliarios` (valores consignados, complementacao + 10%, encargos cessados) →
`jurisprudencia-imobiliaria` (validar Temas sobre chaves/recusa — PA-01) →
`analise-documental-imobiliaria` (contrato, recibos, vistoria) →
`estilo-juridico-imobiliario` → `revisao-final-imobiliaria`.

## Checklist de saida
- [ ] Causa de pedir clara: recusa / duvida / cessacao por entrega de chaves.
- [ ] **Deposito em 24h previsto (art. 67, II); chaves, se for o caso.**
- [ ] Valores especificados por verba (alugueis + acessorios) — PA-03.
- [ ] Marco da cessacao da responsabilidade datado (PA-03).
- [ ] Previsao de complementacao + 10% se alegada insuficiencia (art. 67, IV).
- [ ] Rito do art. 67 (especial) aplicado, nao so o CPC 539 (PA-04).
- [ ] Foro da locacao; polo coerente (PA-10); norma vigente (PA-02).

**Selo P1**: tudo com fonte. **R1-R4**: `revisao-final-imobiliaria` antes da entrega.
