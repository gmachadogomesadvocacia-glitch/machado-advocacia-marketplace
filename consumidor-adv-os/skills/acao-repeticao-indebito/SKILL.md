---
name: acao-repeticao-indebito
description: >
  ACAO REPETICAO DE INDEBITO — Skill Tier 2 (eixo cobranca indevida, lado consumidor). Acione quando o cliente e o consumidor e o caso envolve cobranca indevida, desconto indevido, restituicao, devolucao em dobro, valor pago a maior, divida ja quitada cobrada de novo. Exige Selo P1 e a prova do pagamento.
metadata:
  version: "0.1.0"
  area: "Direito do Consumidor e Bancario"
  tier: 2
---

# ACAO REPETICAO DE INDEBITO

> Skill **Tier 2** — eixo cobranca indevida, lado **consumidor**. Especializa a `peticao-inicial-consumidor` para a restituicao do indebito. Disciplina rigida sobre o dobro do art. 42 (PA-06). So roda apos triagem, Selo P1 e linha estrategica.

---

## 0. PRE-REQUISITOS

- Polo = **consumidor** (PA-05). Lado fornecedor → `contestacao-consumidor` / `defesa-instituicao-financeira`.
- Selo P1 emitido.
- Dado-base: **prova do efetivo pagamento** (extrato, fatura, comprovante de desconto) e a discriminacao dos valores indevidos. Sem prova do desembolso, NAO quantificar (PA-15, PA-20) → `[INFORMAR]`.

## 1. SIMPLES versus DOBRO — O NUCLEO DA SKILL

Art. 42, paragrafo unico, CDC: o consumidor cobrado em quantia indevida tem direito a repeticao **em dobro** do que pagou, salvo **engano justificavel**.

- **Pressupostos do dobro** (PA-06): (a) cobranca indevida; (b) **pagamento** pelo consumidor; (c) **engano injustificavel** do fornecedor.
- **Tema 929 STJ** `[VERIFICAR]`: o dobro **independe de prova de ma-fe ou dolo**, bastando a conduta culposa contraria a boa-fe objetiva; **nao cabe** em engano justificavel. **Modulacao**: aplicacao a partir de **30/03/2021** (cobrancas anteriores seguem o regime antigo, que exigia ma-fe). `[VERIFICAR]`
- Sem engano injustificavel ou sem pagamento → so **restituicao simples** (corrigida).

> Pedir o dobro sem cobranca indevida + engano injustificavel e violacao nuclear (PA-06). Tema 929 marcado `[VERIFICAR]` → `jurisprudencia-consumidor` (P1/PA-01).

## 2. CASOS TIPICOS

| Caso | Observacao |
|------|-----------|
| Desconto indevido em consignado/beneficio | Servico/emprestimo nao contratado; sinalizar interface previdenciaria se desconto sobre beneficio INSS. |
| Tarifas e servicos embutidos | Seguro, "protecao", pacote nao solicitado (art. 39, I — venda casada). |
| Divida paga cobrada de novo / valor a maior | Conferir quitacao; tipico cenario de dobro. |

## 3. PRESCRICAO

Aferir o prazo conforme a natureza (PA-11): pretensao de reparacao por fato do servico — **art. 27 CDC (5 anos)**; repeticao pura de valores pagos a maior em contrato — pode atrair prazo do **CC** conforme o caso. **Definir caso a caso** `[VERIFICAR]` e nunca presumir.

## 4. ESTRUTURA (sobre a inicial-base)

1. **Dos Fatos** — a cobranca indevida, os comprovantes de pagamento (doc. N), a discriminacao do indebito.
2. **Do Direito** — FIRAC: (a) carater indevido da cobranca; (b) **simples x dobro** (art. 42 + Tema 929, com a modulacao 30/03/2021) `[VERIFICAR]`; (c) prescricao enfrentada.
3. **Antecipacao adversarial** — neutralizar a tese de "engano justificavel".
4. **Pedidos** — restituicao **discriminada** (indicar expressamente simples OU dobro, com fundamento); correcao e juros; inversao do onus (PA-12); tutela de cessacao do desconto se ainda vigente (`tutela-urgencia-consumidor`).

## 5. CHECKLIST

- [ ] Polo consumidor (PA-05) · Selo P1 · prova do pagamento (PA-15, PA-20)
- [ ] Dobro pedido SO com cobranca indevida + engano injustificavel (Tema 929 / modulacao 30/03/2021) (PA-06) `[VERIFICAR]`
- [ ] Prescricao definida (art. 27 / CC) (PA-11) `[VERIFICAR]`
- [ ] Restituicao discriminada e corrigida · `calculos-consumidor` se necessario
- [ ] `revisao-final-consumidor` R1-R4 (PA-22)

## 6. ENCERRAMENTO

Entrega a acao de repeticao com o indebito comprovado e a escolha simples/dobro corretamente fundamentada no Tema 929 e na sua modulacao — pronta para a R1-R4.
