---
name: defesa-execucao-fiscal
description: >
  Skill flagship Tier 2 — defesa do contribuinte/executado na execucao fiscal (Lei 6.830/80 — LEF). Ative quando houver citacao em execucao fiscal, penhora, CDA, embargos ou excecao de pre-executividade.
metadata:
  version: "0.1.0"
  area: "Direito Tributario"
  tier: 2
---

# DEFESA EM EXECUCAO FISCAL (LEF 6.830/80)

> Tier 2 flagship. Defesa do **executado**. Duas vias com requisitos distintos — escolher a correta antes de redigir. Side-aware: polo do cliente e o **contribuinte/responsavel** (PA-10).

---

## 1. ESCOLHA DA VIA

| | EMBARGOS (LEF art. 16) | EXCECAO DE PRE-EXECUTIVIDADE |
|---|---|---|
| Garantia | **Exige** (penhora, deposito, fianca/seguro) | **Dispensa** |
| Materia | Ampla (qualquer defesa) | So ordem publica, conhecivel de oficio |
| Prova | Admite dilacao probatoria | **Sem** dilacao (prova pre-constituida) — Sum. 393 STJ |
| Prazo | 30 dias da intimacao da garantia (art. 16) | A qualquer tempo |
| Efeito suspensivo | Nao automatico (precisa garantia + risco + relevancia) | Pode suspender atos |

**Regra de decisao:** se a tese e nulidade da CDA, decadencia, prescricao, pagamento ou ilegitimidade **demonstravel de plano** → excecao de pre-executividade (mais rapida, sem garantia). Se exige prova/pericia ou e materia de merito ampla → embargos (garantir o juizo primeiro). PA-07: nunca propor excecao para materia que demande dilacao.

## 2. ARSENAL DE TESES (checklist)

**A. Nulidade da CDA** (LEF art. 2º §5º e §6º; CTN art. 202)
- Falta de requisito: nome/CPF-CNPJ do devedor, valor originario, termo inicial e forma de calculo dos juros/multa, origem/natureza/fundamento legal, numero do processo administrativo.
- CDA que nao permite identificar a divida → nulidade (cerceamento de defesa).
- Substituicao da CDA: so ate a decisao de 1ª instancia e nao para trocar o sujeito passivo (Sum. 392 STJ).

**B. Decadencia** (CTN art. 173, I / art. 150 §4º) — credito constituido fora do prazo de 5 anos.

**C. Prescricao** (CTN art. 174) — 5 anos da constituicao definitiva ate a citacao/despacho que ordena a citacao (LC 118/2005).

**D. Prescricao intercorrente** (LEF art. 40 + Sum. 314 STJ + **Tema 566 STJ**) — 1 ano de suspensao (nao localizado devedor/bens) + 5 anos de arquivamento; correndo automaticamente; intimacao da Fazenda.

**E. Ilegitimidade passiva / redirecionamento** (PA-08)
- Mero inadimplemento NAO autoriza redirecionar ao socio (Sum. 430 STJ).
- Redirecionamento exige excesso de poderes/infracao a lei/dissolucao irregular (art. 135 CTN; Sum. 435 STJ presume dissolucao irregular pela nao localizacao no domicilio fiscal).
- Tema 962 STJ e Tema 981 STJ (marco do redirecionamento e socio que se retirou).

**F. Excesso de execucao** — valor, multa confiscatoria, juros/SELIC, cumulacao indevida.

**G. Pagamento / parcelamento / suspensao** (CTN art. 151) — extincao ou suspensao da exigibilidade; adesao a parcelamento suspende.

## 3. GARANTIA DO JUIZO (para embargos / suspensao)

- Ordem da LEF art. 9º/11: deposito em dinheiro → fianca bancaria / seguro garantia → penhora.
- Seguro garantia e fianca bancaria equiparam-se a dinheiro para suspender/garantir (art. 9º §2º da LEF, redacao da Lei 13.043/2014) — (jurisprudencia a validar).
- Deposito integral em dinheiro suspende a exigibilidade (CTN art. 151, II; Sum. 112 STJ).

## 4. ESTRUTURA DA PECA

**Excecao de pre-executividade** (peticao nos autos da execucao):
1. Enderecamento (juizo da execucao fiscal) · 2. Qualificacao do excipiente · 3. Sintese da execucao e da CDA · 4. Cabimento (Sum. 393 STJ, prova pre-constituida) · 5. Materia de ordem publica (a tese) · 6. Pedidos (extincao/exclusao, suspensao dos atos) · 7. Provas documentais.

**Embargos a execucao fiscal** (acao incidental, autos proprios):
1. Enderecamento · 2. Qualificacao do embargante · 3. Tempestividade + garantia (art. 16) · 4. Fatos · 5. Direito (teses do arsenal) · 6. Efeito suspensivo (art. 919 §1º CPC + garantia) · 7. Pedidos (procedencia/extincao, levantamento da garantia) · 8. Provas/pericia.

## MODELO DE PECA

Chassis (abrir e substituir `[____]` antes de redigir):
- `templates/pecas/excecao-pre-executividade.md` — via sem garantia (Sum. 393 STJ).
- `templates/pecas/embargos-execucao-fiscal.md` — via ampla, exige garantia (LEF 16).

## 5. INTEGRACAO

- `calculos-tributarios` → confirmar decadencia/prescricao e excesso ANTES de afirmar.
- `jurisprudencia-tributaria` → validar Sumulas/Temas citados (PA-01).
- `analise-documental-tributaria` → conferir a CDA e o processo administrativo.
- `estilo-juridico-tributario` → forma final · `revisao-final-tributaria` → R1-R4 antes de entregar.

## 6. CHECKLIST DE SAIDA

- [ ] Via correta (PA-07: excecao so sem dilacao)
- [ ] Garantia equacionada (se embargos)
- [ ] Prazo conferido (art. 16; preclusao)
- [ ] CDA analisada item a item (CTN 202)
- [ ] Decadencia/prescricao calculadas, nao presumidas
- [ ] Polo coerente (PA-10) · Selo P1 feito · R1-R4 pendente
