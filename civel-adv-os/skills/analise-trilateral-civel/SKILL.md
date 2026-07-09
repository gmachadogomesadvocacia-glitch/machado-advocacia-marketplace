---
name: analise-trilateral-civel
description: >
  Analise trilateral civel Tier 1 — FIRAC adaptado em 3 vertices. Ative apos a triagem e a analise documental, quando o usuario pedir analise do caso, forcas e fraquezas, tese adversa ou viabilidade.
metadata:
  version: "0.1.0"
  area: "Direito Civil e Processo Civil"
  tier: 1
---

# ANALISE TRILATERAL CIVEL

> Tier 1 (Insumo). FIRAC (Fatos-Questao-Regra-Aplicacao-Conclusao) lido por **3 prismas**. Roda depois de `triagem-civel` + `analise-documental-civel`, antes de `linha-estrategica-civel`. Side-aware: o prisma do cliente flipa conforme o polo (autor x reu).

---

## 1. OS 3 VERTICES

### Vertice CLIENTE (flipa pelo polo)
- **Autor (credor/lesado):** melhor tese para obter o credito/indenizacao — fato constitutivo, dano, nexo, titulo.
- **Reu (devedor/causador):** melhor defesa — fato impeditivo/modificativo/extintivo, prescricao, pagamento, inexistencia de nexo/culpa, excludentes (CC 393 — caso fortuito; culpa exclusiva da vitima/terceiro).

### Vertice PARTE ADVERSA
- Construir a **tese adversa mais forte** (nao a mais fraca). O que o outro lado alega? Quais documentos e precedentes contrarios? Onde a nossa narrativa cede?

### Vertice JUIZO
- Como o caso aparece para quem decide: o que precisa estar provado, o que e controvertido, qual a linha provavel do julgador no foro-eixo {{CIDADE}}/{{UF}}. Que duvida o juiz tera?

## 2. ONUS DA PROVA (CPC 373)

| Fato | Quem prova |
|------|-----------|
| **Constitutivo** do direito (existencia do credito, do contrato, do dano, do nexo) | **Autor** |
| **Impeditivo / modificativo / extintivo** (pagamento, prescricao, novacao, excludente) | **Reu** |
| **Distribuicao dinamica** (CPC 373 §1º) | A quem tiver maior aptidao — fundamentar |

- Mapear, para cada fato relevante: **quem prova** x **temos a prova?** (cruzar com `analise-documental-civel`). Lacuna de prova = fragilidade.

## 3. ANTECIPACAO ADVERSARIAL DURA

Para cada pilar da nossa tese, listar o **contra-ataque** previsivel e a **resposta**:
- Prescricao/decadencia (PA-05) — ja corrida? interrompida?
- Regime errado (contratual x extracontratual — PA-07) muda onus/prazo/juros?
- Via/pedido inadequado (PA-08) — o adverso argui carencia?
- Falta de nexo ou de prova do dano (PA-03).
- Excludentes de responsabilidade (CC 393, culpa exclusiva).

## 4. QUADRO DE FORCAS (saida)

```
POLO DO CLIENTE: autor / reu
PRISMA CLIENTE — tese central: ...
  Pontos fortes: ...
  Fragilidades (prova/prazo/via): ...
PRISMA ADVERSO — tese mais forte do outro lado: ...
  Contra-teses nossas: ...
PRISMA JUIZO — pontos controvertidos / o que provar: ...
  Risco percebido pelo julgador: baixo / medio / alto
ONUS DA PROVA — mapa fato x quem prova x temos prova: ...
RECOMENDACAO PRELIMINAR → linha-estrategica-civel
```

## 5. ALERTAS

- O prisma do cliente **muda com o polo** (PA-10) — nunca redigir contra o proprio lado.
- A tese adversa deve ser a **mais forte** possivel; subestimar e a maior causa de derrota.
- Toda forca/fragilidade ancora em **prova existente** (PA-03), nao em suposicao.
- Se a materia for de outro plugin, parar e rotear (PA-09).
