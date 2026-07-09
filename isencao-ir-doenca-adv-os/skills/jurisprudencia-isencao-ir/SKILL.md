---
name: jurisprudencia-isencao-ir
description: >
  JURISPRUDENCIA ISENCAO-IR — Skill Tier 1 (apoio ao Selo P1). Gatilhos: sumula, Tema, STJ, jurisprudencia, ha sumula sobre, precedente, Sumula 598, Sumula 627, isencao mantida em remissao, prova da doenca sem laudo oficial.
metadata:
  version: "0.1.0"
  area: "Isencao de IRPF por Doenca Grave"
  tier: 1
---

# JURISPRUDENCIA ISENCAO-IR

> Skill **Tier 1** — apoio ao **Selo P1**. Busca viva + validacao + classificacao. **PA-01: nunca citar sumula/Tema sem validar.** Toda citacao nasce `[VERIFICAR]` ate ser confirmada.

---

## 0. REGRA DE OURO (PA-01)
Nenhuma sumula, Tema ou acordao entra na peca sem validacao da existencia, da redacao e da vigencia. Citacao nao validada = `[VERIFICAR]`. Sem fonte confiavel = **IMPOSSIBILIDADE** (nao citar).

## 1. CLASSIFICACAO EM 3 NIVEIS
- **VALIDADA** — existencia, texto e vigencia confirmados; aplicacao aderente ao caso. Pode citar.
- **[VERIFICAR]** — relevante mas nao confirmada nesta sessao; marcar e confirmar antes de produzir.
- **IMPOSSIBILIDADE** — nao localizada/superada/inaplicavel; **nao citar** e registrar o motivo.

## 2. PRECEDENTES-ANCORA (sempre revalidar)

| Ancora | Tese | Uso |
|--------|------|-----|
| **Sumula 598 STJ** `[VERIFICAR]` | Desnecessario laudo medico **oficial**; a doenca pode ser provada por outros meios | Neutraliza a exigencia de laudo de servico oficial no judicial (PA-07) |
| **Sumula 627 STJ** `[VERIFICAR]` | Isencao **mantida** independentemente de contemporaneidade dos sintomas ou recidiva | Sustenta a isencao em remissao/cura aparente (PA-08) |
| **Nao-extensao a rendimentos de ATIVO** (STJ) `[VERIFICAR]` | Isencao alcanca so **proventos** (aposentadoria/pensao/reforma), nao salario/pro labore | Delimita o pedido; antecipa objecao da Fazenda (PA-06) |
| **IN RFB 1500/2014** `[VERIFICAR]` | Regulamenta a isencao, o rol e a exigencia administrativa de laudo de servico medico oficial | Base da via administrativa; confrontar com a Sum. 598 no judicial |

> O **rol de doencas e taxativo** (PA-05); a **prova e flexivel** (Sum. 598). Nao confundir os planos.

## 3. BUSCA VIVA
1. Procurar a fonte primaria (STJ/RFB) e a redacao vigente.
2. Conferir se ha **superacao/revisao** (sumula cancelada, Tema afetado, IN revogada).
3. Aferir aderencia factual ao caso (doenca do rol, provento, marco temporal).
4. Registrar fonte e data da consulta no `CASO.md`.

## 4. SAIDA PARA O SELO P1
Entregar o quadro de precedentes classificados. O **Selo P1** so e emitido com: art. 6, XIV, Lei 7.713/88 vigente + IN RFB 1500/2014 + Sumulas 598 e 627 **confirmadas** (VALIDADA). Qualquer ancora em `[VERIFICAR]` impede o selo ate a confirmacao.

## 5. ENCERRAMENTO
Devolve precedentes classificados (VALIDADA / [VERIFICAR] / IMPOSSIBILIDADE) com fonte, alimentando o Selo P1, a `analise-trilateral-isencao-ir` e a producao. Citacao em peca, so depois de `revisao-final-isencao-ir` (R2).
