---
name: estilo-juridico-usucapiao
description: >
  ESTILO JURIDICO USUCAPIAO — Tier 1 transversal (Camada 3). Padrao de redacao de toda peca de usucapiao: FIRAC, texto enxuto, docs 'doc. N', descricao tecnica do imovel apta a registro, antecipacao adversarial e tom tecnico imobiliario. Acione durante a redacao de qualquer peca, ou quando o usuario pedir o estilo, o padrao de redacao, ou a descricao do imovel para registro.
metadata:
  version: "0.1.0"
  area: "Usucapiao (Judicial e Extrajudicial)"
  tier: 1
---

# ESTILO JURIDICO USUCAPIAO (Camada 3)

> Skill **Tier 1 transversal**. Define o **padrao de redacao** de toda peca de usucapiao. Apoia (nao substitui) as skills de producao. Tom imobiliario, tecnico, enxuto.

---

## 1. ESTRUTURA FIRAC
**F**atos (descricao do imovel + historia da posse) · **I**ssue (a modalidade pleiteada e seus requisitos) · **R**ule (CC 1.238-1.244 / CF 183-191 / Lei 6.015 / CPC — Selo P1) · **A**nalise (subsuncao: posse ad usucapionem ao tipo) · **C**onclusao (pedido). Sem digressao; cada paragrafo serve a um requisito.

## 2. ENXUTO
- Peca curta e direta; um argumento por bloco. Cortar repeticao e citacao decorativa.
- Sem rol de documentos ao final: documentos numerados como **"doc. N"** e citados **no corpo** pelo numero, no ponto em que provam o fato.

## 3. DESCRICAO TECNICA DO IMOVEL — APTA A REGISTRO (nuclear)
- A descricao deve ser **registravel**: coerente com a **planta e o memorial descritivo** (PA-03 — nada de metragem/confrontacao inventada).
- Conter: **confrontacoes** (cada divisa e seu confrontante), **metragem/area**, perimetro/rumos quando houver, e **georreferenciamento** quando **rural** (com **ART/RRT** do responsavel tecnico).
- A descricao da inicial/requerimento deve ser a mesma que sera **levada ao Registro de Imoveis** na sentenca/registro — sem divergencia entre peca, planta e memorial.

## 4. ANTECIPACAO ADVERSARIAL DURA
Antecipar e neutralizar, no proprio texto, os ataques classicos:
- **Detencao x posse** (PA-09): afastar comodato/locacao/permissao; afirmar posse com **animus domini** (PA-08).
- **Interrupcao/oposicao** da posse: demonstrar continuidade (mansa, pacifica, ininterrupta) e afastar atos que a quebrariam.
- **Bem publico** (PA-04): comprovar a natureza **privada** do bem (matricula/origem).
- **Metragem/confrontacoes**: blindar contra impugnacao da area e das divisas (coerencia com planta).
- **Modalidade/requisitos** (PA-05): demonstrar tempo, justo titulo/boa-fe (se ordinaria), moradia, nao-propriedade de outro imovel (especiais).

## 5. TOM
Tecnico imobiliario e registral, sobrio. Combatividade dirigida a teses, nunca a pessoas. Coerencia de polo (PA-10): nunca afirmar tese contraria ao lado do cliente.

## 6. JURISPRUDENCIA E LEI
Toda sumula/tema/precedente entra como `[VERIFICAR]` e e validado por `jurisprudencia-usucapiao` (PA-01). Fundamento legal sempre da lei vigente do Selo P1 (PA-02).

## 7. CHECKLIST
- [ ] FIRAC · enxuto · docs "doc. N" citados no corpo (sem rol)
- [ ] Descricao do imovel apta a registro · coerente com planta/memorial+ART (georref. se rural)
- [ ] Antecipacao: detencao · animus domini · interrupcao · bem publico · metragem
- [ ] Coerencia de polo (PA-10) · jurisprudencia `[VERIFICAR]` (PA-01)

## 8. ENTREGA
Gatilho "gera docx": converter .txt em .docx timbrado via `gerador-peticoes` — Code.

## 9. ENCERRAMENTO
Aplicado, devolve a peca redigida ao padrao da casa e a encaminha a `revisao-final-usucapiao` R1-R4 (PA-13).
