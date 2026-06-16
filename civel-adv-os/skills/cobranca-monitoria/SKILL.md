---
name: cobranca-monitoria
description: >
  Tier 2 — recuperacao de credito SEM titulo executivo ou com prova escrita sem eficacia de titulo.
  Cobre os dois polos: AUTOR/credor (cobra) e REU/devedor (embargos/contestacao). (a) ACAO MONITORIA
  (CPC 700-702) — prova escrita sem forca executiva: cheque/nota promissoria prescritos, contrato,
  duplicata sem aceite, extrato; mandado de pagamento; embargos monitorios; Sum. 247, 282, 299, 384,
  503, 504, 531 STJ (validar). (b) ACAO DE COBRANCA (rito comum) — divida sem qualquer titulo,
  provando-se a relacao e o credito. Diferenca para a EXECUCAO de titulo extrajudicial (PA-08 — via
  adequada). Juros, correcao e prescricao da divida subjacente. Ative em cobrar divida, acao
  monitoria, cheque prescrito, nota promissoria prescrita, contrato sem testemunhas, acao de cobranca,
  duplicata sem aceite ou recuperacao de credito sem titulo. NAO confundir com execucao (titulo
  liquido/certo/exigivel) — rotear a `execucao-titulo-extrajudicial`.
metadata:
  version: "0.1.0"
  area: "Direito Civil e Processo Civil"
  tier: 2
---

# COBRANCA E MONITORIA — CREDITO SEM TITULO EXECUTIVO

> Tier 2. Side-aware: **AUTOR/credor** x **REU/devedor**. Peca e tom mudam (PA-10).
> **Eixo (PA-08):** escolher a via certa. Tem titulo liquido/certo/exigivel → **execucao** (outra skill). Tem prova escrita sem forca executiva → **monitoria**. Nao tem documento → **cobranca** (rito comum).

---

## 1. TRIAGEM DA VIA

| Situacao do credito | Via correta |
|---------------------|-------------|
| Titulo executivo (CPC 784) liquido/certo/exigivel | **Execucao** (rotear) |
| Prova **escrita** sem eficacia de titulo | **Monitoria** (CPC 700) |
| Sem prova escrita / credito a constituir | **Cobranca** (rito comum) |

## 2. ACAO MONITORIA (CPC 700-702)

- **Cabimento** — quem afirma, com base em **prova escrita** sem eficacia de titulo executivo, ter direito a pagamento de soma, entrega de coisa fungivel/movel ou bem imovel, ou cumprimento de obrigacao de fazer/nao fazer.
- **Prova escrita** classica: cheque ou nota promissoria **prescritos** (perderam a forca executiva — Sum. 299 e 504 STJ — validar), contrato escrito, duplicata sem aceite + comprovante de entrega, extrato de conta, e-mails/instrumentos particulares.
- **Procedimento:** peticao com demonstrativo do debito (valor atualizado) → juiz defere e expede **mandado de pagamento/entrega** em 15 dias → reu pode: (i) pagar (isento de custas e honorarios reduzidos), (ii) opor **embargos monitorios** (suspendem, rito comum), ou (iii) inertia → **constitui-se de pleno direito o titulo executivo judicial** (CPC 701 §2º).
- Sumulas (validar — PA-01): 247 (titulo de credito ou contrato), 282 (cabe ao protesto facultativo), 299 (cheque prescrito), 384 (data de emissao do cheque), 503/504 (prazo da monitoria: 5 anos do dia seguinte ao vencimento — cheque/NP), 531 (cabivel contra a Fazenda).

## 3. ACAO DE COBRANCA (rito comum)

- Para divida **sem titulo nem prova escrita habil a monitoria**: prova-se a existencia da obrigacao e do inadimplemento por todos os meios (testemunhas, documentos, confissao).
- Pedido condenatorio; sentenca = titulo executivo judicial.

## 4. JUROS, CORRECAO E PRESCRICAO (PA-05/PA-06)

- **Prescricao da pretensao** (atencao ao titulo subjacente):
  - Monitoria de cheque/NP: **5 anos** (Sum. 503/504 — validar).
  - Cobranca de divida liquida de instrumento publico/particular: **5 anos** (CC 206 §5º, I).
  - Honorarios, alugueis, prestacoes: prazos do CC 206.
  - Regra geral: **10 anos** (CC 205).
- Juros de mora e correcao desde o vencimento/constituicao em mora (contratual) — liquidacao em `calculos-civeis`.

## 5. DEFESA (REU)

- **Embargos monitorios** (CPC 702) — toda materia de contestacao; impugnar a prova escrita, a liquidez, alegar pagamento/prescricao; ma-fe do credor (multa CPC 702 §10/§11).
- **Cobranca** — contestacao comum: negar a divida, pagamento, prescricao, ausencia de prova.

## 6. ESTRUTURA DA PECA

**Monitoria (autor):** 1. Enderecamento (foro de eleicao/domicilio do reu — CPC 46/53) · 2. Qualificacao · 3. Dos fatos (origem do credito + prova escrita) · 4. Do direito (cabimento CPC 700; natureza da prova) · 5. Demonstrativo atualizado do debito · 6. Pedidos (expedicao do mandado de pagamento; constituicao do titulo; juros/correcao/sucumbencia) · 7. Valor da causa (= credito) · 8. Provas.
**Cobranca (autor):** mesma espinha, pedido condenatorio (rito comum).

## 7. INTEGRACAO

- `calculos-civeis` → demonstrativo do debito, juros, correcao, prescricao (PA-06/PA-05).
- `jurisprudencia-civel` → validar Sumulas da monitoria (247/299/503/504/531 — PA-01).
- `analise-documental-civel` → aferir se a prova escrita habilita monitoria ou execucao.
- `estilo-juridico-civel` → forma · `revisao-final-civel` → R1-R4.

## 8. CHECKLIST DE SAIDA

- [ ] Via correta: execucao x monitoria x cobranca (PA-08) · cumulacao CPC 327 se cabivel
- [ ] Prova escrita aferida (monitoria) · demonstrativo atualizado
- [ ] Prescricao da divida subjacente conferida (Sum. 503/504; CC 205/206 — PA-05)
- [ ] Juros/correcao com termo inicial certo (PA-06)
- [ ] Sumulas marcadas "validar" (PA-01) · Foro correto (P5)
- [ ] Polo coerente (PA-10) · Selo P1 feito · R1-R4 pendente
