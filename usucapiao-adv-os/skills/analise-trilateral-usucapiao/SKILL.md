---
name: analise-trilateral-usucapiao
description: >
  ANALISE TRILATERAL USUCAPIAO — Skill Tier 1. Antes da linha estrategica, analisa o caso por 3 prismas
  obrigatorios: Cliente (posse + modalidade + documentacao), OPONENTE/confrontante (a melhor defesa
  contra a usucapiao) e Juiz/Oficial do RI (como o caso aparece para quem decide ou registra). Gera a
  matriz forcas x fragilidades x contra-teses. Acione apos a triagem e as analises de posse/documental,
  antes da estrategia. Gatilhos: analisar o caso pelos tres lados, qual a defesa do confrontante, pontos
  fortes e fracos da usucapiao, como o juiz/cartorio ve isso, antecipar a oposicao, trilateral.
metadata:
  version: "0.1.0"
  area: "Usucapiao (Judicial e Extrajudicial)"
  tier: 1
---

# ANALISE TRILATERAL USUCAPIAO

> Skill **Tier 1** — analisa o caso por **3 prismas** antes de definir a estrategia. Roda apos a triagem e as analises de posse/documental, **antes** da linha estrategica. O prisma Cliente flipa conforme o polo (usucapiente x confrontante).

---

## 0. PRE-CHECK
- Caso triado, posse analisada (modalidade definida), documentos inventariados.
- Nada inventado (PA-03). Coerencia de polo obrigatoria (PA-10).

## 1. PRISMA 1 — CLIENTE
- **Posse** ad usucapionem demonstravel (tempo + qualidade + animus domini — PA-08), nao detencao (PA-09).
- **Modalidade** correta com requisitos atendidos (PA-05); accessio possessionis se houver.
- **Documentacao** (mapa "doc. N"): matricula, planta+ART, comprovantes, anuencias.
- *(polo confrontante: o prisma vira a defesa — ver prisma 2 como tese propria.)*

## 2. PRISMA 2 — OPONENTE / CONFRONTANTE (a melhor defesa)
Construir a oposicao mais forte (e, se cliente, neutralizar; se confrontante, e a tese):
- **E detencao, nao posse** — comodato/locacao/permissao (PA-09); falta de **interversao**.
- **Falta animus domini** — possuia em nome alheio, pagava aluguel, reconhecia o dono.
- **Posse viciada** — **violenta, clandestina ou precaria** (nao ad usucapionem).
- **Interrupcao/oposicao** — acao possessoria, notificacao, esbulho repelido que **quebra a continuidade** e zera o prazo.
- **Metragem/confrontacoes erradas** — planta/memorial divergem da matricula; area acima do teto (especiais).
- **Bem PUBLICO** — nao usucapivel (PA-04; Sum. 340 STF).
- **Titular registral resiste** — nega anuencia (inviabiliza o extrajudicial — PA-07) ou contesta (judicial).

## 3. PRISMA 3 — JUIZ / OFICIAL DO RI
- **Juiz** (judicial): citacoes completas (confrontantes + titulares + Uniao/Estado/Municipio + edital — PA-06)? prova da posse robusta? descricao apta a registro?
- **Oficial do RI** (extrajudicial): consenso e anuencias presentes? ata notarial + planta/ART? silencio do confrontante (Lei 6.015 art. 216-A §2 — `[VERIFICAR]` via `jurisprudencia-usucapiao`)? Havendo duvida/impugnacao → remete ao judicial (PA-07).

## 4. MATRIZ
```
FORCAS (cliente)        | FRAGILIDADES (atacaveis)     | CONTRA-TESES (neutralizar/explorar)
- posse longa + docs    | - origem por comodato        | - interversao comprovada em [doc. N]
- animus domini provado | - planta x matricula diverge | - retificacao / nova ART
- modalidade certa      | - oposicao em 20xx           | - oposicao nao prosperou / fora do prazo
```

## 5. ENCERRAMENTO
Entrega os 3 prismas e a matriz forcas × fragilidades × contra-teses, com a melhor oposicao ja antecipada. Alimenta `linha-estrategica-usucapiao`. Jurisprudencia validada por `jurisprudencia-usucapiao` (Selo P1); toda peca produzida termina em `revisao-final-usucapiao`.
