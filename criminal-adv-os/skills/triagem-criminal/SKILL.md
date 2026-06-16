---
name: triagem-criminal
description: >
  Triagem criminal Tier 1 — primeiro contato com a demanda. Classifica em 5 eixos: (1) FASE
  (investigacao/inquerito, acao penal, juri, recursos, execucao penal, acordos), (2) POLO do cliente
  (defesa — investigado/reu/sentenciado — x assistencia de acusacao/vitima), (3) CRIME e TIPIFICACAO
  (capitulacao, pena cominada, competencia — comum/juri/JECrim), (4) SITUACAO PRISIONAL (solto, preso
  em flagrante, preventiva, temporaria, cumprindo pena), (5) PRAZO em curso (prescricao, resposta a
  acusacao 10 dias, RESE 5 dias, apelacao 5 dias, excesso de prazo). Define a porta de saida. Ative
  no inicio de qualquer caso penal.
metadata:
  version: "0.1.0"
  area: "Direito Penal e Processo Penal"
  tier: 1
---

# TRIAGEM CRIMINAL

> Tier 1. Primeira skill operacional. Classifica a demanda em **5 eixos**, identifica o **prazo/urgencia** (liberdade e prescricao primeiro) e roteia. Nada se produz antes da triagem + Selo P1.

---

## 1. OS 5 EIXOS

**Eixo 1 — FASE** (define a peca)
- Investigacao/Inquerito · Acao penal · Tribunal do Juri · Recursos · Execucao penal · Acordos despenalizadores (ver `criminal-master` §0).

**Eixo 2 — POLO**
- **Defesa** (investigado/acusado/reu/sentenciado) — padrao · **Assistencia de acusacao** (vitima/ofendido). Toda peca coerente com o polo (PA-10).

**Eixo 3 — CRIME / TIPIFICACAO**
- Capitulacao (artigo do CP ou lei especial); pena cominada (em abstrato); natureza da acao (publica incondicionada/condicionada/privada); **competencia**: comum, **Tribunal do Juri** (dolosos contra a vida — CF 5º XXXVIII), **JECrim** (menor potencial ofensivo, pena max 2 anos — Lei 9.099), foro por prerrogativa.

**Eixo 4 — SITUACAO PRISIONAL** (prioridade)
- Solto · Preso em flagrante · Preventiva · Temporaria · Cumprindo pena. Se preso → avaliar relaxamento/liberdade/HC e excesso de prazo IMEDIATAMENTE.

**Eixo 5 — PRAZO EM CURSO**

| Prazo | Marco | Fonte |
|-------|-------|-------|
| **Prescricao** (punitiva/executoria) | conforme pena | CP 109/110 |
| **Decadencia** (queixa/representacao) | 6 meses do conhecimento da autoria | CP 103 / CPP 38 |
| Resposta a acusacao | 10 dias da citacao | CPP 396/396-A |
| RESE | 5 dias | CPP 586 |
| Apelacao | 5 dias (razoes 8) | CPP 593/600 |
| Embargos de declaracao | 2 dias | CPP 619 |
| ANPP / proposta | fase pre-processual | CPP 28-A |

> Lei penal no tempo: aplicar a do fato, salvo a posterior **mais benefica**, que retroage (PA-04).

## 2. PERGUNTAS DE ABERTURA (faca as que faltarem)

1. Qual o documento/fato que originou a procura? (intimacao, citacao, prisao, IP, denuncia, sentenca)
2. Qual o crime imputado e a capitulacao? Ha denuncia/queixa recebida?
3. O cliente esta solto ou preso? Desde quando? Que tipo de prisao?
4. Em que fase esta o processo/investigacao? Numero, vara, comarca.
5. Datas: fato, flagrante, denuncia, citacao, sentenca.
6. O cliente e a defesa (investigado/reu) ou a vitima (assistente)?

## 3. SAIDA DA TRIAGEM

```
FASE: ...
POLO: ...
CRIME/TIPIFICACAO: ... (pena / competencia)
SITUACAO PRISIONAL: ...
PRAZO MAIS URGENTE: ... (vence em DD/MM)
PORTA DE SAIDA: <skill>
PENDENCIAS DOCUMENTAIS: ...
```
Depois: **Selo P1** → `analise-documental-criminal` → porta de producao.

## 4. ALERTAS DE TRIAGEM

- Cliente PRESO → prioridade absoluta: relaxamento (prisao ilegal), liberdade provisoria, ou HC; checar excesso de prazo (PA-07).
- Pena maxima ≤ 4 anos / crime sem violencia → avaliar **ANPP** (CPP 28-A); ≤ 2 anos → JECrim/transacao/sursis.
- Suspeita de prescricao → `calculos-criminais` ANTES de qualquer peca de merito.
- Crime doloso contra a vida → rito do Juri (competencia, fase de pronuncia).
- Pedido que tangencie destruir prova/coagir testemunha/fuga → recusar (PA-08).
- Crime tributario (Lei 8.137) ou de transito (CTB) → sinalizar interface.
