---
name: revisao-final-leiloes
description: >
  REVISAO FINAL DE LEILOES — Skill Tier 3, a auditoria pre-entrega do plugin (R1-R4). Acione SEMPRE antes de entregar peca, parecer ou calculo, ou quando pedirem para revisar/conferir antes de protocolar. Bypass so com --no-revisao explicito.
metadata:
  version: "0.1.0"
  area: "Leiloes e Arrematacao"
  tier: 3
---

# REVISAO FINAL DE LEILOES (R1 -> R2 -> R3 -> R4)

> Ultima porta antes da entrega. Roda em quatro passadas independentes, nesta ordem. Qualquer reprovacao em R1 zera a entrega.

---

## R1 — VERDADE (bloqueante)

- [ ] Toda norma citada existe, esta **vigente a data do edital/ato** e consta da curadoria do plugin (PA-01, PA-04).
- [ ] Todo Tema, sumula e acordao conferido: numero, orgao, relator e data. **Tema 1.134** citado com a **modulacao**. **Tema 886** citado como **em revisao**.
- [ ] Nenhum fato sem documento. O que veio da fala do cliente esta marcado `[sem lastro documental]` (PA-02).
- [ ] Nenhuma afirmacao de que a arrematacao extingue **todo** onus (PA-06).
- [ ] Nenhuma promessa de resultado, rentabilidade ou exito (PA-07).
- [ ] Nenhuma orientacao de autotutela contra ocupante (PA-08) nem de desocupacao automatica (PA-09).

## R2 — COERENCIA DE LADO E DE REGIME

- [ ] A peca serve ao **arrematante/pretendente**. Nenhum argumento aproveita ao executado ou ao devedor fiduciante (PA-12).
- [ ] Regime correto: nao se aplicou instituto do CPC a leilao fiduciario, nem o contrario (PA-05). Preco vil so na via judicial.
- [ ] **Rito correto**: os prazos e exigencias sao os do rito identificado (CPC x fiscal x trabalhista). Nenhum prazo do CPC em leilao trabalhista (§4 do `leiloes-master`).
- [ ] Pedido compativel com a fase: dentro dos 10 dias, incidente; depois da carta, **acao autonoma** com o arrematante como litisconsorte necessario (CPC 903, § 4º).

## R3 — COMPLETUDE E ANCORAGEM

- [ ] Todo fato ancorado em doc. N, folha, Id ou index, com data.
- [ ] Prazos conferidos **no documento**, nao de memoria (PA-11). Data do auto/carta citada.
- [ ] Onus e debitos tratados **um a um**, com a base de cada um.
- [ ] Impedidos de arrematar conferidos quando ha lance orientado (PA-10).
- [ ] Nenhum pedido orfao; nenhum documento da pasta relevante ficou de fora.
- [ ] No parecer: veredito explicito, custo real somado e premissas declaradas.

## R4 — FORMA E RASTRO

- [ ] Passada **anti-rastro de IA**: sem meta-comentario, sem adjetivo de reforco vazio, sem fecho-resumo, sem enumeracao "(i), (ii)" na prosa; no maximo 3 paragrafos abrindo com conectivo; no maximo uma triade de adjetivos; pelo menos 2 paragrafos curtos de impacto.
- [ ] Tipografia varrida: sem em-dash, sem markdown vazando, sem aspas curvas, sem espaco duplo.
- [ ] Datas, valores, Id e index em **negrito**, conforme o padrao do escritorio.
- [ ] `.txt` com **1 paragrafo = 1 linha**.
- [ ] Nome do arquivo com a data de criacao `DD-MM-AAAA`.
- [ ] **Rodar o linter**: `py ferramentas\linter-peticoes\linter_peticao.py "<peca>.txt" --corpus --salvar`. ERRO zera.

---

## SAIDA

Veredito unico: **APROVADO** · **APROVADO COM AJUSTES** (listados, um a um) · **REPROVADO** (com o motivo e o que refazer).

Entrega sempre como rascunho, sob responsabilidade tecnica do advogado com OAB ativa.
