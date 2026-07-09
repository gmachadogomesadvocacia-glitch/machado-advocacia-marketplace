---
name: embargos-declaracao-consumidor
description: >
  EMBARGOS DE DECLARACAO CONSUMIDOR — Skill Tier 2 recursal. Acione quando o usuario pede embargos de declaracao, aclaratorios, sanar omissao/ contradicao/obscuridade, ou prequestionar. Exige Selo P1 e o prazo conferido (PA-08).
metadata:
  version: "0.1.0"
  area: "Direito do Consumidor e Bancario"
  tier: 2
---

# EMBARGOS DE DECLARACAO CONSUMIDOR

> Skill **Tier 2** recursal, **side-aware**. Aclaratorios para sanar vicio da decisao — nunca para rediscutir o merito. So roda apos a triagem, o Selo P1 e a leitura integral da decisao embargada.

---

## 0. PRE-REQUISITOS

- **Declarar a parte que embarga** (PA-05): consumidor ou fornecedor. Calibrar ao polo do cliente.
- **Selo de Validacao Legal Previa EMITIDO** (P1). Sem ele, nao redigir.
- Decisao embargada (sentenca, interlocutoria ou acordao) lida na integra; identificar o trecho viciado. Falta → `[INFORMAR]` (PA-15).

## 1. BASE E PRAZO

| Foro | Base | Prazo `[VERIFICAR]` (PA-08) |
|------|------|------------------------------|
| Vara comum | CPC art. 1.022 a 1.026 | 5 dias uteis |
| JEC | Lei 9.099 art. 48 a 50 | 5 dias (contados da ciencia) |

**Efeito interruptivo:** os embargos **interrompem** o prazo dos demais recursos (CPC art. 1.026; e, no JEC, art. 50 — apos a EC/Lei 13.105 o efeito e interruptivo). Conferir o prazo correto e o termo inicial (PA-08).

## 2. HIPOTESES DE CABIMENTO (estritas — art. 1.022)

| Vicio | O que e |
|-------|---------|
| **Omissao** | a decisao deixou de enfrentar ponto/pedido/tese sobre o qual devia se manifestar (inclui o art. 1.022 § un.: fundamento que o juiz deveria conhecer de oficio ou tese repetitiva) |
| **Contradicao** | proposicoes inconciliaveis dentro da propria decisao (fundamentacao x dispositivo) |
| **Obscuridade** | falta de clareza que impede compreender o julgado |
| **Erro material** | equivoco evidente (nome, valor, data, calculo) corrigivel a qualquer tempo |

Apontar o **vicio especifico** e o trecho exato. Sem uma dessas hipoteses, **nao cabem** embargos.

## 3. FUNCAO DE PREQUESTIONAMENTO

Quando a decisao omite questao federal/constitucional necessaria ao **REsp/RE**, os embargos servem para prequestionar (CPC art. 1.025 — consideram-se incluidos os elementos para fins de prequestionamento). Indicar expressamente o dispositivo do CDC/CC/CPC que o tribunal deve enfrentar, preparando o acesso ao STJ (ver `recursos-consumidor`).

## 4. EFEITOS INFRINGENTES (excepcionais)

Os embargos podem, **excepcionalmente**, modificar o julgado quando o saneamento do vicio (em especial a omissao/contradicao) altera o resultado. Nesse caso, **intimar a parte contraria** para contrarrazoes (CPC art. 1.023 §2). Pedir o efeito infringente apenas quando ele decorrer logicamente da correcao do vicio — nunca como pretexto para rediscussao.

## 5. LIMITE — NAO E RECURSO DE REVISAO

Proibido usar os embargos para **rediscutir o merito** ou o acerto do julgamento; isso e materia de apelacao/recurso inominado/REsp. Embargos manifestamente protelatorios sujeitam o embargante a **multa** (CPC art. 1.026 §2 e §3). Nao transformar aclaratorios em segunda defesa (PA-20).

## 6. ESTRUTURA DA PECA

1. Enderecamento ao proprio juizo/orgao prolator + referencia aos autos.
2. Tempestividade (prazo de 5 dias).
3. Do vicio — apontar omissao/contradicao/obscuridade/erro material no trecho exato.
4. Do prequestionamento (se for o caso) — indicar o dispositivo a ser enfrentado.
5. Pedido — sanar o vicio; se cabivel, efeito infringente (com pedido de intimacao da parte contraria).

## 7. CHECKLIST ANTES DE ENTREGAR

- [ ] Parte embargante declarada e coerente (PA-05) · Selo P1 citado
- [ ] **Prazo de 5 dias conferido (PA-08)** e efeito interruptivo registrado
- [ ] Vicio especifico apontado (omissao/contradicao/obscuridade/erro) com o trecho exato
- [ ] Sem rediscussao de merito · sem carater protelatorio (PA-20)
- [ ] Prequestionamento indicado quando visar REsp/RE · jurisprudencia validada (PA-01) `[VERIFICAR]` via `jurisprudencia-consumidor`
- [ ] Submeter a `revisao-final-consumidor` (R1-R4) antes da entrega (PA-22)

## 8. ENCERRAMENTO

Entrega os embargos enxutos, com o vicio especifico apontado, sem rediscutir o merito e (quando for o caso) prequestionando — calibrados ao polo do embargante, prontos para a Suprema Corte R1-R4.
