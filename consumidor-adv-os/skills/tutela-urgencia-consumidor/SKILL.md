---
name: tutela-urgencia-consumidor
description: >
  TUTELA DE URGENCIA CONSUMIDOR — Skill Tier 2 transversal (side-aware). Acione quando o caso pede liminar, tutela de urgencia, tutela antecipada, medida liminar, religacao, baixa imediata, suspensao de cobranca. Exige Selo P1 e a prova do perigo.
metadata:
  version: "0.1.0"
  area: "Direito do Consumidor e Bancario"
  tier: 2
---

# TUTELA DE URGENCIA CONSUMIDOR

> Skill **Tier 2 transversal**, **side-aware**. Produz o capitulo/peticao de tutela provisoria em qualquer eixo consumerista. Acoplada as `acao-*` e a `contestacao-*`. So roda apos triagem, Selo P1 e linha estrategica.

---

## 0. PRE-REQUISITOS

- **Declarar o polo** (PA-05): o consumidor pede tutela para sanar o dano (baixa, religacao, posse); o fornecedor pode pedir tutela/efeito suspensivo ou resistir a antecipacao. Tese, pedido e tom flipam conforme o polo.
- Selo P1 emitido.
- Dado-base do perigo: prova concreta da urgencia (corte iminente, negativacao ativa, desconto em curso, apreensao). Sem prova do perigo, NAO afirmar urgencia (PA-15, PA-20) → `[INFORMAR]`.

## 1. ESPECIE E REQUISITOS

| Especie | Base | Requisitos |
|---------|------|-----------|
| Urgencia | art. 300 CPC | **Probabilidade do direito** (fumus) + **perigo de dano/risco ao resultado util** (periculum) + **reversibilidade** (§3) — ou caucao. |
| Evidencia | art. 311 CPC | Independe de perigo: abuso do direito de defesa, tese firmada em repetitivo/sumula, pedido com prova documental e fato incontroverso. |

- **Antecedente** (art. 303): quando a urgencia e contemporanea a propositura; aditar a inicial em 15 dias.
- **Incidental**: no corpo da inicial/peticao (o usual nas `acao-*`).
- **Astreintes** (art. 537): fixar multa diaria proporcional e exequivel para a obrigacao de fazer/nao fazer.

## 2. CASOS TIPICOS (lado consumidor)

| Caso | Probabilidade | Perigo |
|------|---------------|--------|
| Baixa de negativacao | inexistencia/inexigibilidade do debito (checar **Sum. 385** `[VERIFICAR]` antes) | restricao de credito |
| Religacao de servico essencial (luz/agua/telefone) | impossibilidade de corte por debito pretérito/discutido | dignidade, essencialidade |
| Suspensao de desconto/cobranca (consignado, tarifa) | cobranca indevida verossimil | comprometimento da renda/minimo existencial |
| Manutencao na posse (busca e apreensao) | mora descaracterizada/invalida | perda do bem → `defesa-busca-apreensao` |
| Fornecimento de produto/servico | contrato + recusa indevida | dano ao consumidor |

> Sumula/Tema `[VERIFICAR]` → `jurisprudencia-consumidor` (P1/PA-01). A evidencia (art. 311) e o atalho quando a tese ja esta firmada em repetitivo.

## 3. REVERSIBILIDADE E CONTRACAUTELA

Enderecar o §3 do art. 300: demonstrar que a medida e reversivel (baixa/religacao podem ser revertidas) ou oferecer caucao/deposito do incontroverso quando houver risco de irreversibilidade (PA-20 — nao prometer concessao automatica).

## 4. ESTRUTURA DO PEDIDO

1. Especie e fundamento (art. 300 ou 311).
2. **Probabilidade do direito** — FIRAC sintetico amarrado a tese de merito do eixo.
3. **Perigo de dano** — fato concreto e atual (doc. N).
4. **Reversibilidade / caucao** (se for o caso).
5. **Pedido liminar** determinado (o que, prazo, contra quem) + **astreintes** (art. 537) com teto.

## 5. CHECKLIST

- [ ] Polo declarado (PA-05) · Selo P1 · prova do perigo (PA-15)
- [ ] Probabilidade + perigo + reversibilidade (art. 300) OU evidencia (art. 311) bem enquadrados
- [ ] Baixa de negativacao? **Sum. 385 conferida** antes (PA-07) `[VERIFICAR]`
- [ ] Astreintes proporcionais (art. 537) · pedido determinado
- [ ] Antecedente (art. 303) x incidental decidido · sem promessa de concessao (PA-20)
- [ ] `revisao-final-consumidor` R1-R4 (PA-22)

## 6. ENCERRAMENTO

Entrega o pedido de tutela com a especie correta, os tres requisitos enfrentados, a reversibilidade resolvida e astreintes exequiveis — coerente com o polo, pronto para a R1-R4.
