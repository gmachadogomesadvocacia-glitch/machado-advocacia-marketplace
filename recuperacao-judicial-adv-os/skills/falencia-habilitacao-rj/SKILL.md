---
name: falencia-habilitacao-rj
description: >
  Producao em FALENCIA (Lei 11.101/2005 + Lei 14.112/2020), lado CREDOR por padrao. Ative em:
  pedido de falencia (art. 94 — impontualidade, execucao frustrada, atos de falencia),
  habilitacao/impugnacao de credito na falencia, classificacao dos creditos (art. 83), pedido de
  RESTITUICAO (art. 85 / bem de terceiro), acoes revocatorias e ineficacia (arts. 129-130),
  ordem de pagamento, encerramento. Tambem defesa do devedor contra pedido de falencia. So apos
  triagem + Selo. Encerra em revisao-final-rj (R1-R5). NAO confundir com habilitacao em RJ.
---

# FALENCIA — PEDIDO, HABILITACAO E CLASSIFICACAO (Lei 11.101/2005)

> Skill **Tier 2** (producao). EIXO do plugin = **credor** (especialmente trabalhista — ver
> `credor-trabalhista-rj`). So apos `triagem-rj` + Selo. Distingue-se da RJ: aqui o devedor e
> liquidado; o foco e RECEBER na ordem do art. 83. Valores de `calculo-credito-trabalhista-rj`/calculo.

## 0. PRE-REQUISITOS
- **Selo P1**: Lei 11.101/2005 (com a Lei 14.112/2020) vigente + jurisprudencia cruzada com o
  livro-razao (PA-01). Confirmar a FASE (pedido / arrecadacao / QGC / pagamentos / encerramento).
- Documentos: titulo do credito, prova da impontualidade/protesto, sentenca de quebra (se ja houve),
  edital do art. 99, relacao de credores do AJ. Falta → `[INFORMAR]`.

## 1. PEDIDO DE FALENCIA (art. 94)
- Hipoteses: **impontualidade injustificada** de titulo(s) protestado(s) > 40 salarios minimos (I);
  **execucao frustrada** (II — triplice omissao); **atos de falencia** (III — rol). Verificar o piso e o protesto.
- Defesa do devedor: deposito elisivo, relevante razao de direito, ilegitimidade do titulo, abuso
  (pedido como meio de cobranca — vedado). Atencao a eventual pedido de RJ em resposta (art. 95).

## 2. HABILITACAO E IMPUGNACAO NA FALENCIA
- Habilitacao tempestiva (15 dias do edital art. 7 §1) ou **retardataria** (art. 10) ao AJ;
  divergencia/impugnacao (arts. 8-15) ao juiz. Mesmo procedimento da RJ quanto a forma.
- Provar origem, valor atualizado ate a **data da quebra** (a partir da decretacao, juros so se o
  ativo comportar — art. 124), classe e privilegios.

## 3. CLASSIFICACAO DOS CREDITOS (art. 83 — ordem de pagamento)
1. **Trabalhistas** ate 150 SM/credor + acidentarios (sem teto); o que exceder 150 SM → quirografario.
2. **Garantia real** ate o limite do bem gravado.
3. **Tributarios** (exceto multas).
4. **Privilegio especial**; 5. **Privilegio geral**; 6. **Quirografarios**;
7. **Multas** (contratuais/penais/tributarias); 8. **Subordinados**.
- **Creditos EXTRACONCURSAIS** (art. 84) e **restituicoes** (art. 85) sao pagos ANTES da ordem do art. 83.
- Honorarios advocaticios: natureza alimentar, equiparam-se a trabalhistas (**Tema 637 STJ**).

## 4. RESTITUICAO E REVOCATORIA
- **Restituicao (art. 85)**: bem de terceiro em poder da massa; ou em dinheiro (art. 86). Nao e
  habilitacao — e pedido proprio.
- **Ineficacia/revocatoria (arts. 129-130)**: atos prejudiciais praticados no termo legal ou em
  fraude a credores; a acao revocatoria (130) exige prova do conluio fraudulento (consilium fraudis).
- **Coobrigados (Sum. 581 STJ)**: a falencia/RJ do devedor principal nao impede execucao contra
  avalistas/fiadores. **Sum. 480 STJ**: juizo da recuperacao nao alcanca bens nao abrangidos —
  conferir o equivalente na falencia (juizo universal da falencia atrai, art. 76).

## 5. CHECKLIST
- [ ] Fase correta · Selo P1 (Lei 11.101 + 14.112) · titulo/protesto/piso 40 SM (se pedido)
- [ ] Habilitacao com valor ate a quebra · classe certa do art. 83 · extraconcursal/restituicao distinguidos
- [ ] Honorarios = trabalhista (Tema 637 STJ) · coobrigados (Sum. 581) considerados
- [ ] Citacoes no livro-razao (PA-01) · `revisao-final-rj` R1-R5 (C7)

## 6. ENCERRAMENTO
Entrega a peca (pedido de falencia / habilitacao / impugnacao / restituicao / revocatoria) com a
classificacao correta, pronta para a `revisao-final-rj` (R1-R5 + ficha). Nada protocola sem o OK (C7).
