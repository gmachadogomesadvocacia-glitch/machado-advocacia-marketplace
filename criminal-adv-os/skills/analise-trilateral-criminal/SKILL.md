---
name: analise-trilateral-criminal
description: >
  Analise trilateral criminal Tier 1 — FIRAC adaptado ao processo penal. Ative apos a analise documental e antes da linha estrategica, ou quando pedir analise do caso, prismas, forcas e fraquezas.
metadata:
  version: "0.1.0"
  area: "Direito Penal e Processo Penal"
  tier: 1
---

# ANALISE TRILATERAL CRIMINAL (FIRAC penal)

> Tier 1. Olha o caso pelos **3 vertices**: ACUSACAO, DEFESA e JULGADOR. Antecipa o ataque mais forte e a leitura do juizo **antes** de escolher a tese. Gera o **quadro de forcas**. Roda apos `analise-documental-criminal`, antes de `linha-estrategica-criminal`.

---

## 1. OS 3 VERTICES

**Vertice 1 — ACUSACAO / MP**
- Qual a tese acusatoria **mais forte** (nao a media)? Que prova a sustenta?
- Materialidade e autoria que o MP invocara; capitulacao e causas de aumento.
- Como o MP rebatera a tese defensiva? Que precedente usaria?

**Vertice 2 — DEFESA (cliente)**
- O que **sustenta** o cliente: atipicidade, negativa de autoria, excludentes, insuficiencia de prova, nulidade, prescricao, desclassificacao.
- Provas e ilicitudes a favor; versao coerente com os autos (PA-03).
- *Flip de polo:* se o cliente e **assistente de acusacao** (vitima), este vertice sustenta a pretensao punitiva e o vertice 1 vira a defesa adversa.

**Vertice 3 — JULGADOR**
- Como o caso **aparece** para quem decide: o que salta, o que incomoda.
- Standard probatorio (alem de duvida razoavel); pontos que geram conviccao ou duvida.
- Sensibilidade do juizo a gravidade, clamor, perfil do reu.

## 2. ONUS DA PROVA

- O onus e da **acusacao**; ao reu nao cabe provar inocencia (CF 5º LVII).
- **In dubio pro reo** — duvida razoavel favorece a defesa.
- Mapear onde a prova acusatoria e fragil, indiciaria ou ilicita.

## 3. MAPA DE PROVAS, ILICITUDES E NULIDADES

| Prova | Quem favorece | Licitude | Observacao |
|-------|---------------|----------|------------|
| ... | acusacao/defesa | licita/ilicita | nulidade? cadeia de custodia? |

- Prova **ilicita** (CF 5º LVI) e derivada → inadmissivel.
- Nulidades absolutas x relativas; prejuizo (pas de nullite sans grief).

## 4. QUADRO DE FORCAS (saida)

```
PONTOS FORTES (defesa): ...
FRAGILIDADES (defesa): ...
TESE ACUSATORIA MAIS FORTE: ...
CONTRA-TESES (como o MP ataca): ...
LEITURA PROVAVEL DO JUIZO: ...
PROVAS-CHAVE / ILICITUDES: ...
RISCO GLOBAL: baixo / medio / alto
```

## 5. ANTECIPACAO ADVERSARIAL DURA

- Construir o **pior cenario** acusatorio e responde-lo antes de litigar.
- Nenhuma tese segue sem resposta a contra-tese mais forte.

## 6. PROIBICOES E INTEGRACAO

- **PA-03** fatos reais · **PA-07** garantias · **PA-10** coerencia de polo (defesa x assistencia).
- Insumos: `analise-documental-criminal`, `calculos-criminais`, `jurisprudencia-criminal`.
- Saida → `linha-estrategica-criminal` (define tese e via).
