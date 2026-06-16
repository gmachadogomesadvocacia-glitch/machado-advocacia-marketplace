---
name: linha-estrategica-criminal
description: >
  Linha estrategica criminal Tier 1 — consolida a trilateral e a jurisprudencia e define a tese central
  e a sequencia de atos. Eixos: liberdade primeiro (relaxamento/liberdade/HC se preso), teses de
  absolvicao (CPP 386 — atipicidade, negativa de autoria, legitima defesa e demais excludentes,
  insuficiencia de prova), nulidades, prescricao, desclassificacao, e despenalizacao (ANPP, transacao,
  sursis processual quando cabivel) x litigar. Decide quando impetrar HC x aguardar e quando aceitar
  ANPP. Entrega decisao documentada e aponta a porta de producao. Ative apos a analise trilateral, ou
  quando pedir estrategia, melhor tese, linha de defesa ou plano do caso.
metadata:
  version: "0.1.0"
  area: "Direito Penal e Processo Penal"
  tier: 1
---

# LINHA ESTRATEGICA CRIMINAL

> Tier 1. Converte o **quadro de forcas** em **tese central + teses subsidiarias + sequencia de atos**. Liberdade primeiro. Decisao **documentada** no CASO.md. Roda apos `analise-trilateral-criminal` e `jurisprudencia-criminal`, antes da producao.

---

## 1. ORDEM DE PRIORIDADE DOS EIXOS

```
1. LIBERDADE (se preso)  → relaxamento / liberdade provisoria / HC; excesso de prazo
2. ABSOLVICAO (CPP 386)  → atipicidade · negativa de autoria · excludentes · insuficiencia de prova
3. NULIDADES             → prova ilicita, cerceamento, vicios processuais
4. PRESCRICAO            → extincao da punibilidade (calculos-criminais)
5. DESCLASSIFICACAO      → tipo menos grave / competencia
6. DESPENALIZACAO        → ANPP · transacao · sursis processual (x litigar)
```

> Liberdade e prescricao sao **sempre** avaliadas primeiro.

## 2. TESES DE ABSOLVICAO (CPP 386)

| Inciso | Hipotese |
|--------|----------|
| I | provada a inexistencia do fato |
| II | nao haver prova da existencia do fato |
| III | nao constituir o fato infracao penal (**atipicidade**) |
| IV | provado que o reu nao concorreu (**negativa de autoria**) |
| V | nao existir prova de ter concorrido |
| VI | excludentes (legitima defesa, estado de necessidade, estrito cumprimento, exercicio regular) ou duvida sobre elas |
| VII | nao existir prova suficiente (**in dubio pro reo**) |

## 3. DECISOES-CHAVE

**HC agora x aguardar**
- Impetrar **ja** se ha constrangimento ilegal atual, prisao sem fundamento, excesso de prazo, prova ilicita evidente ou atipicidade flagrante (trancamento).
- Aguardar se a via ordinaria resolve melhor e o HC tende a supressao de instancia.

**Aceitar ANPP x litigar**
- ANPP (CPP 28-A): cabivel se confissao formal, crime sem violencia/grave ameaca, pena minima < 4 anos, nao reincidente, requisitos preenchidos. Pesar contra a chance real de absolvicao e o risco da pena.
- Transacao/sursis processual (Lei 9.099) quando o patamar permitir.
- **PA-08:** acordo nunca implica orientar ato ilicito.

## 4. SEQUENCIA DE ATOS (exemplo)

```
1. [se preso] HC / pedido de liberdade  → habeas-corpus / defesa-investigacao-flagrante
2. Resposta a acusacao (absolvicao sumaria?) → resposta-acusacao
3. Instrucao / alegacoes finais            → alegacoes-finais
4. [juri] pronuncia / plenario             → tribunal-do-juri
5. Recursos / execucao conforme desfecho
```

## 5. DECISAO DOCUMENTADA (saida)

```
TESE CENTRAL: ...
TESES SUBSIDIARIAS: ...
EIXO PRIORITARIO: liberdade / absolvicao / nulidade / prescricao / desclassif. / despenalizacao
ANPP/ACORDO: cabivel? aceitar? por que
RISCOS: ...
PROXIMO ATO + PORTA DE PRODUCAO: <skill>
```

## 6. PROIBICOES E INTEGRACAO

- **PA-10** coerencia de polo · **PA-07** garantias · **PA-08** sem ato ilicito · **PA-05/PA-06** se a tese for prescricao/dosimetria.
- Insumos: `analise-trilateral-criminal`, `jurisprudencia-criminal`, `calculos-criminais`.
- Saida → porta de producao (HC, resposta, alegacoes, juri, recursos, execucao, acordos) + registro no CASO.md.
