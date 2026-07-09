---
name: analise-trilateral-tributaria
description: >
  Analise trilateral tributaria (FIRAC adaptada). Antes de qualquer producao, ve a controversia pelos tres vertices: CONTRIBUINTE (tese do cliente), FAZENDA (a defesa/ataque fiscal mais forte) e JULGADOR (CARF ou juizo. Ative apos a triagem e antes da redacao, quando o usuario pedir analise do caso, forcas e fragilidades, ou contra-teses.
metadata:
  version: "0.1.0"
  area: "Direito Tributario"
  tier: 1
---

# ANALISE TRILATERAL TRIBUTARIA

> Tier 1. FIRAC adaptado ao contencioso fiscal. Acionada **apos** `triagem-tributaria` e **antes** da producao. Antecipacao adversarial **dura** — montar a tese da Fazenda como se fosse advoga-la.

---

## 1. OS TRES VERTICES

**Vertice 1 — CONTRIBUINTE (cliente, polo de defesa padrao)**
- Qual a tese central? Decadencia, prescricao, nulidade da CDA, ilegitimidade, inexigibilidade, excesso?
- Que fato/documento sustenta cada tese (lastro — PA-03)?

**Vertice 2 — FAZENDA (adversario)**
- Como o Fisco sustenta a higidez do lancamento e da CDA?
- Contra-argumentos previsiveis: confissao por declaracao (Sum. 436), substituicao da CDA (Sum. 392), redirecionamento (art. 135 CTN, Sum. 435), interrupcao da prescricao, dissolucao irregular.
- Qual a tese fazendaria **mais forte** contra o cliente? Enfrenta-la de frente.

**Vertice 3 — JULGADOR (CARF ou juizo)**
- Como o caso **aparece** para quem decide? Materia de ordem publica (favorece excecao) x merito que exige prova (exige embargos/dilacao)?
- Linha provavel: jurisprudencia dominante da esfera, sumulas vinculantes, posicao do CARF.

## 2. ONUS DA PROVA

| Fato | Onus |
|------|------|
| Higidez/legalidade do lancamento e da CDA | **Fisco** (presuncao de liquidez e certeza e relativa) |
| Fato extintivo (pagamento, decadencia, prescricao) | **Contribuinte** |
| Fato modificativo/impeditivo (isencao, imunidade, erro de base) | **Contribuinte** |
| Vicio formal aparente na CDA | aproveita ao contribuinte de plano |

> A CDA goza de presuncao **relativa** (LEF art. 3º); cabe ao executado afastar com prova.

## 3. QUADRO DE FORCAS (saida)

```
TESE              | FORCA (1-5) | LASTRO        | CONTRA-TESE FAZENDA      | RISCO
decadencia        |             | doc. N + datas| const. por declaracao    |
prescricao        |             | calculo       | despacho citacao retroage|
nulidade CDA      |             | CDA item a item| substituicao (Sum. 392) |
ilegit./redirec.  |             | contrato social| Sum. 435 (dissolucao)   |
```

## 4. SAIDA E INTEGRACAO

- Consolidar: pontos fortes, fragilidades, contra-teses e risco de redirecionamento (PA-08).
- Cruzar com `calculos-tributarios` (prazos) e `jurisprudencia-tributaria` (validar — PA-01).
- Entregar o quadro **antes** de `linha-estrategica-tributaria`, que escolhe a via e a sequencia.
- Coerencia de polo em todo o raciocinio (PA-10).
