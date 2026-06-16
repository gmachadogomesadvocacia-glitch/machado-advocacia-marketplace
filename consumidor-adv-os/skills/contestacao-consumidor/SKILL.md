---
name: contestacao-consumidor
description: >
  CONTESTACAO CONSUMIDOR — Skill Tier 2 (lado fornecedor/reu). Redige a defesa empresarial em acao
  consumerista: preliminares, prejudiciais (prescricao art. 27 / decadencia art. 26) e impugnacao
  ponto a ponto do merito, com as excludentes de responsabilidade (culpa exclusiva do consumidor ou de
  terceiro, caso fortuito/forca maior, inexistencia de defeito — art. 12 §3 / 14 §3 CDC) e o ataque ao
  dano moral e ao seu quantum. Peca-base das defesas do fornecedor. Acione quando o cliente e o
  fornecedor (banco, loja, operadora, prestador) e o usuario pede contestacao, defesa, resposta. Exige
  Selo P1 e os documentos da empresa.
metadata:
  version: "0.1.0"
  area: "Direito do Consumidor e Bancario"
  tier: 2
---

# CONTESTACAO CONSUMIDOR

> Skill **Tier 2** — lado fornecedor. Peca-base da defesa empresarial. So roda apos triagem, Selo P1 e a linha estrategica do polo reu.

---

## 0. PRE-REQUISITOS

- Polo do cliente = **fornecedor** (PA-05). Lado consumidor → `peticao-inicial-consumidor`.
- Selo P1 emitido. Documentos da empresa: contrato, faturas, telas de sistema, gravacoes, comprovantes de entrega/atendimento. Falta → `[INFORMAR]` (PA-15).
- Para instituicao financeira, usar tambem `defesa-instituicao-financeira` (taxa media, capitalizacao pactuada).

## 1. PRELIMINARES (CPC art. 337) — conforme o caso

Incompetencia, inepcia da inicial, ilegitimidade (ex.: responsabilidade na cadeia — art. 7/18/25; instituicao correta), conexao, falta de interesse. Nao alegar preliminar sem base (PA-20).

## 2. PREJUDICIAIS DE MERITO

- **Decadencia** (art. 26): vicio aparente — 30 dias (nao duravel) / 90 dias (duravel), contados da entrega ou da ciencia do vicio oculto.
- **Prescricao** (art. 27): fato do produto/servico — 5 anos da ciencia do dano e da autoria.
- Conferir obstativos (reclamacao comprovada, vicio oculto) antes de alegar (PA-11).

## 3. MERITO — IMPUGNACAO PONTO A PONTO

Para cada fato/pedido da inicial: admitir o incontroverso, impugnar especificadamente o controvertido (onus da impugnacao especifica, art. 341 CPC). Teses do fornecedor:

| Tese defensiva | Base |
|----------------|------|
| Inexistencia de vicio/defeito | art. 12 §3, II / 14 §3, I CDC |
| Culpa exclusiva do consumidor ou de terceiro | art. 12 §3, III / 14 §3, II |
| Caso fortuito / forca maior (externo) | jurisprudencia STJ |
| Regularidade da cobranca / debito existente | contrato + extratos |
| Exercicio regular de direito (negativacao de devedor) | art. 43 CDC; afasta dano moral |
| **Sumula 385 STJ** | preexistencia de inscricao legitima afasta dano moral por negativacao |

## 4. ATAQUE AO DANO MORAL E AO QUANTUM

Sustentar ausencia de ato ilicito/nexo/dano; mero aborrecimento nao indeniza; subsidiariamente, impugnar o **quantum** pleiteado (proporcionalidade, vedacao ao enriquecimento sem causa, parametros do TJ/STJ). Impugnar pedido de **repeticao em dobro**: sem cobranca indevida ou sem engano injustificavel, so cabe simples (art. 42 + Tema 929).

## 5. ONUS DA PROVA

Resistir/contextualizar a inversao (art. 6, VIII): demonstrar ausencia de verossimilhanca/hipossuficiencia, ou produzir a prova do fato impeditivo (a empresa costuma deter a prova documental — usa-la).

## 6. CHECKLIST

- [ ] Polo fornecedor coerente (PA-05) · Selo P1
- [ ] Decadencia/prescricao examinadas (PA-11) · impugnacao especifica de cada ponto
- [ ] Excludentes do art. 12 §3 / 14 §3 quando cabiveis · Sumula 385 se negativacao
- [ ] Ataque ao quantum do dano moral · dobro impugnado
- [ ] Sem alegacao temeraria (PA-20) · `revisao-final-consumidor` R1-R4 (PA-22)

> **CHASSI:** `templates/pecas/contestacao-fornecedor.md` — esqueleto no estilo da casa (texto corrido, impugnacao especifica ponto a ponto, excludentes art. 12 §3/14 §3, ataque ao quantum e ao dobro, docs "Doc. nº N" antes do protocolo, procuracao por ultimo). Especializar a partir dele.

## 7. ENCERRAMENTO

Entrega a defesa com preliminares pertinentes, prescricao/decadencia, impugnacao especifica e excludentes — calibrada ao polo fornecedor, pronta para a R1-R4.
