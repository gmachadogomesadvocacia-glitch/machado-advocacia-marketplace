---
name: acao-transporte-aereo
description: >
  ACAO TRANSPORTE AEREO — Skill Tier 2 (lado consumidor). Redige a acao do eixo aereo: atraso,
  cancelamento e overbooking (dano moral + material) e extravio ou avaria de bagagem. Aplica o divisor
  CRITICO entre voo DOMESTICO (CDC + Resolucao ANAC 400) e voo INTERNACIONAL (Tema 210 STF: a Convencao
  de Montreal prevalece sobre o CDC nos danos MATERIAIS — indenizacao tarifada, prazo de 2 anos; o dano
  MORAL segue o CDC). Analisa criticamente as excludentes da companhia (forca maior, meteorologia,
  seguranca, conexao perdida) e o prazo prescricional (Montreal 2 anos x CDC 5 anos). Acione quando o
  consumidor reclama de voo atrasado, cancelado, overbooking, bagagem extraviada/danificada, no-show,
  conexao perdida ou indenizacao de companhia aerea. Exige Selo P1.
metadata:
  version: "0.1.0"
  area: "Direito do Consumidor e Bancario"
  tier: 2
---

# ACAO TRANSPORTE AEREO

> Skill **Tier 2** — lado consumidor, eixo aereo. Especializa a `peticao-inicial-consumidor`. So roda apos triagem, Selo P1 e linha estrategica.

---

## 0. PRE-REQUISITOS

- Polo do cliente = **consumidor** (PA-05). Se fornecedor → `contestacao-consumidor`.
- **Selo P1 EMITIDO**. Sem ele, nao redigir.
- CASO.md com: bilhete/localizador, voo e datas, comprovante de embarque/atraso, tickets de bagagem, despesas materiais (recibos), protocolos de atendimento. Falta de doc essencial → `[INFORMAR]` (PA-15).

## 1. O DIVISOR-MAE: DOMESTICO x INTERNACIONAL

Determinar primeiro a natureza do voo — muda o regime juridico e o PRAZO.

| | **DOMESTICO** | **INTERNACIONAL** |
|---|---|---|
| Regime | **CDC** + Resolucao **ANAC 400** | **Tema 210 STF** `[VERIFICAR]` |
| Dano **MATERIAL** | CDC (reparacao integral) | **Convencao de Montreal** prevalece — indenizacao **tarifada** |
| Dano **MORAL** | CDC | **CDC** (Montreal nao alcanca o dano moral) `[VERIFICAR]` |
| Prazo | prescricao **CDC 5 anos** (art. 27) `[VERIFICAR]` | **Montreal 2 anos** para o dano material `[VERIFICAR]` |

**Tema 210 STF** `[VERIFICAR]`: nos voos internacionais, os tratados (Varsovia/Montreal) prevalecem sobre o CDC **apenas nos danos materiais**; o dano moral continua regido pelo CDC. Confirmar a tese, o alcance e o prazo via `jurisprudencia-consumidor` (PA-01) antes de redigir. **Atencao redobrada ao prazo de 2 anos** da Montreal — risco de perda do direito material (PA-11).

## 2. HIPOTESES E PEDIDOS

- **Atraso / cancelamento:** dever de assistencia material da ANAC 400 (informacao, alimentacao, hospedagem, reacomodacao/reembolso conforme o tempo); dano moral pela frustracao/quebra do contrato; dano material pelas despesas comprovadas.
- **Overbooking / preterição de embarque:** compensacao da ANAC 400 + reacomodacao/reembolso + dano moral.
- **Bagagem extraviada/avariada:** dano material (conteudo, com a tarifacao da Montreal no internacional) + dano moral; nos primeiros dias de extravio, despesas emergenciais.
- **No-show / cancelamento unilateral do trecho de volta:** abusividade da clausula.

## 3. EXCLUDENTES DA COMPANHIA — ANALISE CRITICA

A companhia invoca **forca maior / caso fortuito** (meteorologia, fechamento de aeroporto, seguranca, manutencao nao programada, malha aerea). Analisar com ceticismo:

- Meteorologia/seguranca podem afastar a responsabilidade **somente se** efetivamente comprovadas e se o atraso/cancelamento decorreu **exclusivamente** delas — antecipar e exigir prova (inversao do onus, art. 6 VIII, PA-12).
- Manutencao da aeronave e fortuito **interno** — integra o risco da atividade, nao exclui a responsabilidade.
- Reacomodacao tardia ou ma assistencia agrava o dano ainda que a causa inicial fosse externa.

## 4. ESTRUTURA (delega a `peticao-inicial-consumidor`)

Enderecamento → qualificacao → **Dos Fatos** (cronologia do voo, atraso/cancelamento/extravio, assistencia negada, despesas; docs "doc. N") → **Do Direito** (FIRAC: relacao de consumo; regime aplicavel conforme §1; ANAC 400 no domestico; Tema 210 no internacional `[VERIFICAR]`; inversao do onus PA-12; **antecipacao adversarial das excludentes** §3) → **Tutela** se houver → **Pedidos** (dano material comprovado; **dano moral quantificado** com ancoragem; juros e correcao) → valor da causa → requerimentos.

## 5. CHECKLIST

- [ ] Natureza do voo definida (domestico x internacional) e regime correto
- [ ] Tema 210 STF e Convencao de Montreal com `[VERIFICAR]` (PA-01)
- [ ] **Prazo conferido** — Montreal 2 anos (material internacional) x CDC 5 anos (PA-11) `[VERIFICAR]`
- [ ] Excludentes da companhia antecipadas e neutralizadas · inversao do onus fundamentada (PA-12)
- [ ] Dano moral quantificado · dano material comprovado · pedidos determinados · docs "doc. N"
- [ ] Submeter a `revisao-final-consumidor` (R1-R4) antes da entrega (PA-22)

## 6. ENCERRAMENTO

Entrega a acao aerea com o regime correto (CDC/ANAC ou Montreal/Tema 210), prazo conferido, excludentes neutralizadas e dano moral quantificado, pronta para a Suprema Corte R1-R4.
