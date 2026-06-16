---
name: analise-contratual-consumidor
description: >
  ANALISE CONTRATUAL CONSUMIDOR — Skill Tier 1 (Protocolo P2). Varre o contrato de adesao a caca de
  clausulas abusivas a luz do art. 51 do CDC (rol exemplificativo) e entrega a TABELA clausula →
  inciso do art. 51 → vicio → consequencia (nulidade de pleno direito, art. 51 caput). PA-13: nunca
  pedir nulidade sem indicar o inciso. Acione apos a analise documental, antes da producao; quando o
  usuario pedir para revisar o contrato, achar clausula abusiva, conferir taxas/encargos/foro/multa,
  ou avaliar fidelizacao e distrato. Gatilhos: clausula abusiva, contrato de adesao, art. 51, nulidade
  de clausula, foro de eleicao, comissao de permanencia, capitalizacao, fidelizacao, multa
  desproporcional, reajuste unilateral, perda das prestacoes, distrato, letra miuda.
metadata:
  version: "0.1.0"
  area: "Direito do Consumidor e Bancario"
  tier: 1
---

# ANALISE CONTRATUAL CONSUMIDOR

> Skill **Tier 1** — ramo do **Protocolo P2**. Caca clausulas abusivas no contrato de adesao e entrega a tabela mapeada ao **art. 51 do CDC** (rol **exemplificativo** — caput, "entre outras"). Toda nulidade citada traz o **inciso** (**PA-13**).

---

## 0. QUANDO ACIONAR

Apos `analise-documental-consumidor` (precisa do contrato como doc. essencial — PA-15) e do **Selo P1**. Antes de `analise-trilateral`, `linha-estrategica` e da redacao. Tambem em revisao contratual avulsa e em defesa (fornecedor: antecipar quais clausulas o consumidor atacara).

## 1. PRINCIPIO

Clausula abusiva e **nula de pleno direito** (art. 51, *caput*) — vicio reconhecivel de oficio, nao convalesce. O rol do art. 51 e **aberto**: serve de ancora, mas a abusividade tambem decorre da quebra do equilibrio e da boa-fe (art. 51, IV + § 1º). **Nunca pedir nulidade sem apontar o inciso** (**PA-13**); jurisprudencia so se VALIDADA (**PA-01** — marcar `[VERIFICAR]` e acionar `jurisprudencia-consumidor`).

---

## 2. VARREDURA — O QUE PROCURAR

### 2.1 Responsabilidade e direitos
- **Limitacao / exclusao de responsabilidade do fornecedor** → art. 51, **I** (so admite limitacao em situacoes justificaveis para consumidor PJ).
- **Renuncia ou disposicao de direitos** do consumidor → art. 51, **I**.
- **Inversao do onus da prova em prejuizo do consumidor** → art. 51, **VI**.
- Clausula que impoe representante / decisao unilateral ao fornecedor → art. 51, **VIII e XI**.

### 2.2 Foro, modificacao e equilibrio
- **Foro de eleicao abusivo** (afasta o foro do domicilio do consumidor, dificulta a defesa) → art. 51, **IV** + art. 101, I CDC.
- **Reajuste / variacao unilateral** de preco ou condicoes pelo fornecedor → art. 51, **X e XIII**.
- Vantagem exagerada / desequilibrio (art. 51, IV c/c § 1º).

### 2.3 Encargos financeiros (bancario)
- **Multa e encargos desproporcionais** (multa moratoria > 2% — art. 52, § 1º) → art. 51, **IV**.
- **Capitalizacao de juros sem pactuacao expressa** → art. 51, IV + **`[VERIFICAR]` Sum. 539/541 STJ** (validar).
- **Comissao de permanencia cumulada** com correcao/juros/multa → art. 51, IV + **`[VERIFICAR]` Sum. 30 / 294 / 472 STJ** (validar).
- Tarifas e seguros embutidos sem destaque/anuencia → art. 51, IV.

### 2.4 Permanencia e distrato
- **Fidelizacao excessiva** (prazo/multa desproporcionais ao beneficio) → art. 51, **IV**.
- **Perda total das prestacoes pagas** no distrato → art. 51, **II e IV** + **`[VERIFICAR]` Sum. 543 STJ** (restituicao das parcelas, retencao so do razoavel).

> Sumulas/Temas acima entram **so depois de validados** por `jurisprudencia-consumidor`; ate la, `[VERIFICAR]`.

---

## 3. SAIDA — TABELA DE CLAUSULAS

Para cada clausula suspeita:

| # | Clausula (transcricao curta + localizacao) | Inciso art. 51 | Vicio | Consequencia |
|---|--------------------------------------------|----------------|-------|--------------|
| 1 | "Fica eleito o foro de [cap. da matriz]" (cl. 18) | IV (+ art. 101, I) | Foro que dificulta a defesa do consumidor | Nulidade de pleno direito; declinacao ao foro do domicilio |
| 2 | "Multa de 10% sobre o saldo" (cl. 9) | IV (art. 52 § 1º) | Multa moratoria acima de 2% | Nulidade parcial; reducao a 2% |
| 3 | "Perda das quantias pagas" (cl. 12) | II e IV | Perda total no distrato | Nulidade; restituicao [VERIFICAR Sum. 543] |

Toda linha fecha com a base: **nulidade de pleno direito, art. 51, caput**. Indicar sempre o **inciso** (PA-13) e o efeito pratico (nulidade total/parcial, reducao, restituicao, declinacao de foro).

## 4. CHECKPOINT

Apresente a tabela. Marque clausulas que dependem de **prova** (ex.: desequilibrio concreto) e de **calculo** (encargos → rotear `calculos-consumidor`). Sumulas pendentes ficam `[VERIFICAR]` ate o retorno de `jurisprudencia-consumidor`. Atualize o `CASO.md` (**P3**).

## 5. ENCERRAMENTO

Entrega a tabela clausula → inciso → vicio → consequencia, com toda nulidade ancorada no inciso do art. 51 (PA-13) e jurisprudencia marcada `[VERIFICAR]` ate validacao (PA-01). Alimenta `linha-estrategica-consumidor`, as skills de producao e a `revisao-final-consumidor`.
