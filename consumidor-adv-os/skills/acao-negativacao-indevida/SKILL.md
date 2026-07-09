---
name: acao-negativacao-indevida
description: >
  ACAO NEGATIVACAO INDEVIDA — Skill Tier 2 (eixo negativacao, lado consumidor). Acione quando o cliente e o consumidor e o caso envolve nome negativado, inscricao indevida, SPC, Serasa, SCPC, cadastro de inadimplentes, negativacao por divida paga/inexistente. Exige Selo P1 e o extrato dos orgaos de protecao ao credito.
metadata:
  version: "0.1.0"
  area: "Direito do Consumidor e Bancario"
  tier: 2
---

# ACAO NEGATIVACAO INDEVIDA

> Skill **Tier 2** — eixo negativacao, lado **consumidor**. Especializa a `peticao-inicial-consumidor` para a declaratoria de inexistencia de debito + dano moral + baixa. So roda apos triagem, Selo P1 e linha estrategica.

---

## 0. PRE-REQUISITOS

- Polo = **consumidor** (PA-05). Lado fornecedor → `contestacao-consumidor` / `defesa-instituicao-financeira`.
- Selo P1 emitido.
- Dado-base: **extrato atual dos orgaos** (SPC/Serasa/SCPC) mostrando a inscricao impugnada **e todas as demais**; origem alegada do debito; prova de quitacao/inexistencia. Sem o extrato, NAO redigir (PA-15) → `[INFORMAR]`.

## 1. TRIAGEM CRITICA — SUMULA 385 (FAZER SEMPRE, PRIMEIRO)

**Sumula 385 STJ** `[VERIFICAR]`: havendo **inscricao legitima preexistente**, NAO ha dano moral pela anotacao irregular — cabe apenas o direito a **baixa/cancelamento**.

Antes de pedir dano moral, examinar o extrato:
- Inscricao impugnada e a **unica** ou as demais sao tambem indevidas/sub judice → dano moral cabivel.
- Existe outra inscricao **legitima** → **NAO** pedir dano moral (PA-07); pedir so a baixa. Pedir dano moral nesse cenario e violacao nuclear.

## 2. TESES

| Tese | Base | Observacao |
|------|------|-----------|
| Inexistencia/inexigibilidade do debito | art. 14/CDC; CC | Divida paga, fraude, inexistente, ja cancelada. |
| Ausencia de notificacao previa | **Sumula 359 STJ** `[VERIFICAR]`; art. 43, §2 CDC | O **orgao mantenedor** deve notificar previamente o consumidor antes de inscrever; a falta gera dever de cancelar (e, conforme o caso, dano moral). |
| Dano moral in re ipsa | jurisprudencia STJ `[VERIFICAR]` | Na negativacao indevida o dano e presumido — desde que **nao incida a Sum. 385**. |

> Toda Sumula/Tema `[VERIFICAR]` → `jurisprudencia-consumidor` (P1/PA-01).

## 3. ESTRUTURA (sobre a inicial-base)

1. **Dos Fatos** — origem do debito, prova de quitacao/inexistencia, a inscricao (doc. N) e o extrato integral dos orgaos (doc. N).
2. **Do Direito** — FIRAC: (a) inexistencia/inexigibilidade; (b) ausencia de notificacao previa (Sum. 359, art. 43 §2) `[VERIFICAR]`; (c) dano moral in re ipsa **com o filtro da Sum. 385** `[VERIFICAR]`.
3. **Antecipacao adversarial** — neutralizar a Sum. 385 (demonstrar que as demais inscricoes sao indevidas/inexistentes) e eventual exercicio regular de direito.
4. **Da Tutela** — baixa/suspensao imediata da inscricao (art. 300 CPC) → `tutela-urgencia-consumidor`; perigo de dano evidente (restricao de credito).
5. **Pedidos** — declaracao de inexistencia/inexigibilidade; baixa definitiva; **dano moral quantificado** com ancoragem em precedente (nunca "a arbitrar" puro), so se afastada a Sum. 385; inversao do onus (PA-12).

## 4. CHECKLIST

- [ ] Polo consumidor (PA-05) · Selo P1 · extrato integral dos orgaos analisado (PA-15)
- [ ] **Sumula 385 conferida** — ha outra inscricao legitima? (PA-07) `[VERIFICAR]`
- [ ] Notificacao previa do orgao (Sum. 359 / art. 43 §2) `[VERIFICAR]`
- [ ] Dano moral quantificado e ancorado em precedente · tutela de baixa
- [ ] `revisao-final-consumidor` R1-R4 (PA-22)

> **CHASSI:** `templates/pecas/acao-indenizatoria-negativacao.md` — esqueleto no estilo da casa (texto corrido, docs "Doc. nº N" antes do protocolo, procuracao por ultimo, antecipacao adversarial da Sum. 385 no corpo). Especializar a partir dele.

## 5. ENCERRAMENTO

Entrega a acao com a inexistencia do debito demonstrada, a Sumula 385 enfrentada de frente, a baixa em tutela e o dano moral quantificado — pronta para a R1-R4.
