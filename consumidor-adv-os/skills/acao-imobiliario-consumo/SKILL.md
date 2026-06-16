---
name: acao-imobiliario-consumo
description: >
  ACAO IMOBILIARIO DE CONSUMO — Skill Tier 2 de INTERFACE (lado consumidor/adquirente). Cobre a
  relacao de consumo com a incorporadora: atraso de obra (prazo de tolerancia de 180 dias;
  lucros cessantes/multa), distrato/resolucao do compromisso (Lei 13.786/2018 — percentual de
  retencao; e a Sumula 543 STJ sobre devolucao imediata e em parcela unica do que foi pago, com
  retencao limitada, quando aplicavel) e incorporacao imobiliaria. Skill de interface: migra para o
  futuro plugin `imobiliario-adv-os` quando este existir. Casos puramente reais (sem relacao de
  consumo) vao a advogado imobiliario. Acione quando o consumidor reclama de atraso na entrega do
  imovel, distrato com a construtora, devolucao de valores pagos, ou compra na planta. Exige Selo P1.
metadata:
  version: "0.1.0"
  area: "Direito do Consumidor e Bancario"
  tier: 2
---

# ACAO IMOBILIARIO DE CONSUMO

> **NOTA — SKILL DE INTERFACE.** Cobre apenas o recorte **consumerista** da relacao com a incorporadora/construtora. **Migra para o plugin `imobiliario-adv-os` quando este existir.** Casos puramente reais — sem relacao de consumo (negocio entre particulares, usucapiao, direito de vizinhanca, registro) — **vao a advogado imobiliario**, nao a esta skill.

> Skill **Tier 2** — lado consumidor/adquirente. Especializa a `peticao-inicial-consumidor`. So roda apos triagem, Selo P1 e linha estrategica.

---

## 0. PRE-REQUISITOS

- Polo do cliente = **consumidor/adquirente** (PA-05). Se incorporadora → `contestacao-consumidor`.
- **Relacao de consumo confirmada** (adquirente destinatario final x incorporadora/construtora, art. 2/3, PA-16). Sem consumo → encaminhar a advogado imobiliario.
- **Selo P1 EMITIDO**. Sem ele, nao redigir.
- CASO.md com: contrato/compromisso de compra e venda, memorial, comprovantes de pagamento, data prevista de entrega, distrato/notificacao. Falta de doc essencial → `[INFORMAR]` (PA-15).

## 1. ATRASO DE OBRA

- **Prazo de tolerancia de 180 dias** (art. 43-A da Lei 4.591, incluido pela Lei 13.786/2018) `[VERIFICAR]` — em regra valido se previsto em contrato; o atraso se conta **apos** esgotada a tolerancia.
- Esgotado o prazo + tolerancia, o adquirente pode:
  1. **resolver** o contrato com restituicao integral + multa; ou
  2. **manter** o contrato e exigir **lucros cessantes** (valor locativo do periodo de mora) e/ou **multa moratoria** contratual/legal `[VERIFICAR]`.
- Antecipar a defesa da incorporadora (forca maior, embargos, pandemia) — analisar criticamente: fortuito interno do empreendimento nao exclui a mora.

## 2. DISTRATO / RESOLUCAO DO COMPROMISSO

- **Lei 13.786/2018** (lei do distrato): disciplina o **percentual de retencao** pela incorporadora em caso de desfazimento por culpa do adquirente — limites e a base de calculo conforme o regime (com ou sem patrimonio de afetacao) `[VERIFICAR]`. Conferir a data do contrato: a lei se aplica aos contratos firmados **apos** sua vigencia.
- **Sumula 543 STJ** `[VERIFICAR]`: nos contratos **anteriores** a Lei 13.786 (ou quando aplicavel), a devolucao do que foi pago deve ser **imediata e em parcela unica**, com **retencao limitada** de percentual razoavel — afastando clausula de devolucao parcelada e retencao abusiva.
- **Resolucao por culpa da incorporadora** (ex.: atraso): devolucao **integral e imediata**, sem retencao, mais perdas e danos.
- Distinguir quem deu causa ao desfazimento — muda integralmente a retencao e a base.

## 3. INCORPORACAO E CLAUSULAS

- Relacao de consumo com a incorporadora → CDC aplicavel (clausulas abusivas art. 51, PA-13; inversao do onus art. 6 VIII, PA-12).
- Clausulas tipicamente atacadas: tolerancia desproporcional, retencao excessiva, devolucao parcelada, transferencia de tributos/comissao ao adquirente, juros no pe.

## 4. ESTRUTURA E PEDIDOS (delega a `peticao-inicial-consumidor`)

Enderecamento → qualificacao → **Dos Fatos** (compra na planta, prazo, atraso/distrato, recusa de devolucao; docs "doc. N") → **Do Direito** (FIRAC: relacao de consumo art. 2/3; atraso §1 ou distrato §2; nulidade de clausula art. 51 com inciso, PA-13; inversao do onus PA-12; antecipacao adversarial da forca maior e da retencao) → **Tutela** se houver → **Pedidos**:
- resolucao OU cumprimento + lucros cessantes/multa;
- **restituicao** (integral por culpa da incorporadora; com retencao limitada conforme Lei 13.786 / Sumula 543 `[VERIFICAR]`);
- nulidade das clausulas abusivas;
- **dano moral quantificado** quando configurado;
- juros e correcao.

→ valor da causa → requerimentos.

Lei 13.786, art. 43-A e Sumula 543 STJ sempre `[VERIFICAR]` via `jurisprudencia-consumidor` (PA-01).

## 5. CHECKLIST

- [ ] Relacao de consumo confirmada (PA-16) — senao, encaminhar a advogado imobiliario
- [ ] Data do contrato conferida (aplica-se ou nao a Lei 13.786) `[VERIFICAR]`
- [ ] Quem deu causa ao desfazimento definido (muda retencao e devolucao)
- [ ] Tolerancia de 180 dias, lucros cessantes/multa e Sumula 543 com `[VERIFICAR]` (PA-01)
- [ ] Clausula abusiva com inciso do art. 51 (PA-13) · inversao do onus (PA-12) · dano moral quantificado
- [ ] Nota de migracao para `imobiliario-adv-os` registrada · docs "doc. N"
- [ ] Submeter a `revisao-final-consumidor` (R1-R4) antes da entrega (PA-22)

## 6. ENCERRAMENTO

Entrega a acao imobiliaria de consumo com o recorte consumerista isolado, a culpa pelo desfazimento definida, a devolucao corretamente calibrada (Lei 13.786 / Sumula 543) e dano moral quantificado quando cabivel, pronta para a Suprema Corte R1-R4. Casos puramente reais seguem a advogado imobiliario.
