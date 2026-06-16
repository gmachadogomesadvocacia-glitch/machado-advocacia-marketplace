---
name: calculos-civeis
description: >
  Calculos civeis Tier 1 — nucleo de liquidacao. (a) Dano material: dano emergente + lucro cessante
  (CC 402) — base, prova e projecao. (b) Dano moral/estetico: parametros do arbitramento (sem tabela;
  razoabilidade/proporcionalidade, CC 944). (c) Juros de mora: taxa (CC 406 — SELIC ou 1% conforme
  entendimento; validar), termo inicial (Sum. 54 STJ — extracontratual desde o evento; contratual desde
  a citacao/mora). (d) Correcao monetaria: indice e termo (Sum. 362 moral pelo arbitramento; Sum. 43
  material pelo prejuizo). (e) Prescricao/decadencia: CC 205/206; reparacao civil 3 anos; cobranca de
  divida liquida em instrumento 5 anos; anulacao 4 anos (CC 178); execucao de cheque. Memoria de calculo
  passo a passo com datas. Ative para liquidar dano, juros, correcao, quantum ou conferir prazo. PA-05,
  PA-06.
metadata:
  version: "0.1.0"
  area: "Direito Civil e Processo Civil"
  tier: 1
---

# CALCULOS CIVEIS

> Tier 1 (Insumo). Operacionaliza **P4 — Liquidacao e Prazos**. Calcula dano, juros e correcao e confere prescricao/decadencia **antes** de afirmar qualquer valor ou prazo. **Nao errar liquidacao/juros (PA-06) nem confundir prescricao x decadencia (PA-05).** Toda data sai de documento (PA-03).

---

## 1. DANO MATERIAL (CC 402-403)

- **Dano emergente:** o que efetivamente se perdeu — somar despesas comprovadas (notas, recibos, orcamentos).
- **Lucro cessante:** o que razoavelmente se deixou de lucrar — projecao com base em prova (historico, fluxo, contrato). Nao especular (PA-03/PA-06).
- Total material = emergente + cessante, cada parcela com sua data-base.

## 2. DANO MORAL / ESTETICO (CC 944)

- **Nao ha tabela.** Arbitramento por **razoabilidade e proporcionalidade**, considerando: gravidade/extensao, repercussao, condicao das partes, carater pedagogico, vedacao ao enriquecimento sem causa.
- Indicar **faixa** de parametros (com precedentes do foro-eixo via `jurisprudencia-civel`), nunca valor "de tabela".
- Estetico cumula com moral (Sum. 387 — validar); material cumula com moral (Sum. 37 — validar).

## 3. JUROS DE MORA (CC 406)

| Regime | Termo inicial dos juros | Fonte |
|--------|-------------------------|-------|
| **Extracontratual** | **evento danoso** | Sum. 54 STJ (validar) |
| **Contratual (sem termo)** | **citacao** | CC 405 |
| **Contratual com termo (mora ex re)** | **vencimento** | CC 397 |

- **Taxa:** CC 406 — entendimento oscila entre **SELIC** e **1% a.m.** conforme o periodo/orientacao; **validar** o criterio vigente antes de fixar (PA-06).
- Distinguir regime (PA-07) define o termo: nao aplicar Sum. 54 a caso contratual.

## 4. CORRECAO MONETARIA

| Verba | Termo inicial | Fonte |
|-------|---------------|-------|
| **Dano moral** | data do **arbitramento** | Sum. 362 STJ (validar) |
| **Dano material** | data do **efetivo prejuizo** | Sum. 43 STJ (validar) |

- Indice oficial do tribunal/tabela aplicavel (validar). Correcao recompoe; juros remuneram a mora — nao confundir.

## 5. PRESCRICAO / DECADENCIA

| Pretensao | Prazo | Termo inicial | Fonte |
|-----------|-------|---------------|-------|
| **Reparacao civil** | **3 anos** | actio nata (ciencia do dano) | CC 206 §3º, V |
| **Cobranca de divida liquida** (instrumento publico/particular) | **5 anos** | vencimento | CC 206 §5º, I |
| **Geral** (sem prazo especial) | **10 anos** | violacao do direito | CC 205 |
| **Anulacao** (vicio do consentimento — decadencia) | **4 anos** | conforme o vicio (CC 178) | CC 178 |
| **Execucao de cheque** | **6 meses** apos prazo de apresentacao | — | Lei 7.357/85 (validar) |
| **Execucao de NP/duplicata** | **3 anos** do vencimento | — | LUG / Lei 5.474 (validar) |

- **Prescricao** (perda da pretensao) x **decadencia** (perda do direito potestativo) — nunca trocar (PA-05).
- Causas de interrupcao/suspensao (CC 202/204): citacao, protesto, reconhecimento.

## 6. MEMORIA DE CALCULO (passo a passo)

```
1. Principal: <verba> R$ ____ (data-base DD/MM/AAAA — doc. N)
2. Correcao: indice ____ de DD/MM ate hoje → R$ ____
3. Juros de mora: <taxa> desde DD/MM (termo: evento/citacao) → R$ ____
4. TOTAL ATUALIZADO: R$ ____ (em DD/MM/AAAA)
PRESCRICAO: prazo __ anos, inicio DD/MM → vence DD/MM [OK / RISCO]
```

## 7. ALERTAS

- Conferir prescricao **antes** de qualquer promessa de quantum (PA-05).
- Termo dos juros muda com o regime (PA-07): evento (extra) x citacao/vencimento (contratual).
- Taxa de juros e indice de correcao: **validar** o criterio vigente (PA-06).
- Valores e datas sempre de documento (PA-03); marcar lacuna quando faltar prova.
