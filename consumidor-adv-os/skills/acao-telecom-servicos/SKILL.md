---
name: acao-telecom-servicos
description: >
  ACAO TELECOM E SERVICOS ESSENCIAIS — Skill Tier 2 (lado consumidor). Cobre dois eixos: telecom
  (ANATEL — cobranca indevida, ma prestacao, fidelizacao abusiva, interrupcao, planos) e servicos
  essenciais (energia, agua, gas — Lei 8.987). Tese central dos essenciais: o corte so e licito com
  aviso previo e por DEBITO ATUAL — vedado o corte por debito pretérito apurado unilateralmente
  (recuperacao de consumo), em nome da essencialidade e da dignidade. Pedidos: restabelecimento,
  declaracao de inexigibilidade, repeticao de indebito e dano moral; religacao por
  `tutela-urgencia-consumidor`. Acione quando o consumidor reclama de conta de luz/agua/gas, corte de
  servico, cobranca de telefonia/internet, fidelizacao, multa de cancelamento, ANATEL ou recuperacao
  de consumo. Exige Selo P1.
metadata:
  version: "0.1.0"
  area: "Direito do Consumidor e Bancario"
  tier: 2
---

# ACAO TELECOM E SERVICOS ESSENCIAIS

> Skill **Tier 2** — lado consumidor, eixos telecom + servicos essenciais. Especializa a `peticao-inicial-consumidor`. So roda apos triagem, Selo P1 e linha estrategica.

---

## 0. PRE-REQUISITOS

- Polo do cliente = **consumidor** (PA-05). Se fornecedor → `contestacao-consumidor`.
- **Selo P1 EMITIDO**. Sem ele, nao redigir.
- CASO.md com: faturas, contrato/plano, protocolos de atendimento (ANATEL/ouvidoria), comprovante do corte ou da cobranca, historico de consumo. Falta de doc essencial → `[INFORMAR]` (PA-15).

## 1. EIXO TELECOM (ANATEL)

- **Cobranca indevida:** tarifas/servicos nao contratados, cobranca apos cancelamento, duplicidade → declaracao de inexigibilidade + repeticao de indebito (simples, ou **dobro** so com cobranca indevida E engano injustificavel, art. 42 + Tema 929, PA-06).
- **Ma prestacao / interrupcao:** sinal/velocidade abaixo do contratado, quedas → obrigacao de fazer + abatimento + dano moral conforme a gravidade.
- **Fidelizacao abusiva:** multa de permanencia desproporcional ou cobrada sem contrapartida (subsidio) e abusiva; o consumidor pode rescindir sem multa quando o fornecedor descumpre.
- Frente administrativa paralela na **ANATEL** coordenada pelo Protocolo P4 (sem contradicao; usar como prova).

## 2. EIXO SERVICOS ESSENCIAIS (energia, agua, gas — Lei 8.987)

Tese central — corte de servico essencial:

- **Licito** apenas com **aviso previo** e por **debito atual e contestado regularmente** (art. 6, §3, II, Lei 8.987).
- **Ilicito o corte por debito PRETERITO** apurado unilateralmente pela concessionaria — tipicamente **recuperacao de consumo** (suposta fraude no medidor cobrada retroativamente sem contraditorio) `[VERIFICAR]`. O servico essencial nao pode ser usado como meio de coercao para cobranca de divida antiga.
- **Essencialidade e dignidade:** energia/agua/gas tocam o minimo existencial — fundamentar a impossibilidade do corte e o dano moral in re ipsa pela privacao.
- Distinguir: o consumidor responde pelo debito legitimamente apurado **com** contraditorio e por via propria de cobranca — o que se combate e o corte como instrumento de pressao.

Validar a tese da recuperacao de consumo e o corte por debito pretérito via `jurisprudencia-consumidor` (PA-01) — sempre `[VERIFICAR]`.

## 3. TUTELA DE URGENCIA — RELIGACAO

Caso de corte = urgencia tipica. Pleitear **religacao imediata** (probabilidade do direito + perigo de dano, art. 300 CPC) **via `tutela-urgencia-consumidor`**. A privacao de servico essencial dispensa demonstracao reforcada do perigo.

## 4. ESTRUTURA E PEDIDOS (delega a `peticao-inicial-consumidor`)

Enderecamento → qualificacao → **Dos Fatos** (cronologia da cobranca/corte/interrupcao; docs "doc. N") → **Do Direito** (FIRAC: relacao de consumo; tese do eixo §1 ou §2; inversao do onus art. 6 VIII, PA-12; antecipacao adversarial — legitimidade do debito, regularidade do medidor, aviso previo) → **Da Tutela** (religacao, via `tutela-urgencia-consumidor`) → **Pedidos**:
- **restabelecimento** do servico;
- **declaracao de inexigibilidade** do debito indevido;
- **repeticao de indebito** (simples ou dobro conforme art. 42, PA-06);
- **dano moral quantificado** com ancoragem;
- juros e correcao.

→ valor da causa → requerimentos.

## 5. CHECKLIST

- [ ] Eixo identificado (telecom x essencial) e tese correta
- [ ] Essenciais: corte por debito **atual** x **pretérito** distinguido; recuperacao de consumo combatida `[VERIFICAR]`
- [ ] Dobro do indebito so com cobranca indevida + engano injustificavel (PA-06)
- [ ] Tutela de religacao encaminhada a `tutela-urgencia-consumidor` · inversao do onus (PA-12)
- [ ] Sumula/Tema com `[VERIFICAR]` (PA-01) · dano moral quantificado · docs "doc. N"
- [ ] Submeter a `revisao-final-consumidor` (R1-R4) antes da entrega (PA-22)

## 6. ENCERRAMENTO

Entrega a acao de telecom ou servico essencial com a tese de corte/cobranca bem amarrada, religacao via tutela, indebito corretamente qualificado e dano moral quantificado, pronta para a Suprema Corte R1-R4.
