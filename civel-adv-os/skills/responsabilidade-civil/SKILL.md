---
name: responsabilidade-civil
description: >
  Skill flagship Tier 2 — responsabilidade civil e acao indenizatoria (CC 186, 187, 927 e seguintes).
  Cobre os dois polos: AUTOR/lesado (acao de reparacao) e REU/causador (defesa). Trata os pressupostos
  (conduta, dano, nexo causal, culpa) e a responsabilidade objetiva (CC 927 § unico — risco), as
  modalidades de dano (material — dano emergente e lucro cessante; moral; estetico; perda de uma
  chance), o quantum (criterios e arbitramento — Sum. 362 STJ), juros e correcao (Sum. 54 STJ), as
  excludentes (caso fortuito/forca maior, culpa exclusiva da vitima, fato de terceiro) e a estrutura da
  peca. Ative em dano moral, dano material, dano estetico, ato ilicito, indenizacao, reparacao ou
  defesa em acao indenizatoria.
metadata:
  version: "0.1.0"
  area: "Direito Civil e Processo Civil"
  tier: 2
---

# RESPONSABILIDADE CIVIL E ACAO INDENIZATORIA (CC 186/187/927)

> Tier 2 flagship. Side-aware: identificar se o cliente e **autor/lesado** (pleiteia reparacao) ou **reu/causador** (defesa). A peca e o tom mudam conforme o polo (PA-10).

---

## 1. PRESSUPOSTOS (provar todos — regra geral, subjetiva)

| Pressuposto | Conteudo |
|-------------|----------|
| **Conduta** | Acao ou omissao voluntaria |
| **Culpa lato sensu** | Dolo ou culpa (negligencia, imprudencia, impericia) — salvo objetiva |
| **Dano** | Efetivo prejuizo (material, moral e/ou estetico) |
| **Nexo causal** | Liame entre a conduta e o dano |

> **Responsabilidade objetiva** (CC 927 § unico) — dispensa culpa quando ha previsao legal ou **atividade de risco**. Aqui prova-se conduta + dano + nexo. (Resp. do Estado e do consumo tem skills/plugins proprios.)

## 2. MODALIDADES DE DANO

- **Material** — *dano emergente* (o que efetivamente se perdeu) + *lucro cessante* (o que razoavelmente deixou de ganhar — CC 402). Exige prova/liquidacao.
- **Moral** — lesao a direito da personalidade (honra, imagem, integridade); *in re ipsa* em certos casos (presumido). Quantum por arbitramento.
- **Estetico** — autonomo e **cumulavel** com o moral (Sum. 387 STJ).
- **Perda de uma chance** — frustracao de probabilidade seria e real.

## 3. QUANTUM, JUROS E CORRECAO

- **Quantum do dano moral** — arbitramento judicial; criterios: extensao do dano (CC 944), capacidade das partes, carater pedagogico, razoabilidade/proporcionalidade; evitar enriquecimento sem causa.
- **Correcao monetaria do dano moral** — desde o **arbitramento** (Sum. 362 STJ).
- **Juros de mora:**
  - Extracontratual (ato ilicito) — desde o **evento danoso** (Sum. 54 STJ).
  - Contratual — desde a **citacao** (ou constituicao em mora).
- Liquidacao detalhada em `calculos-civeis` (PA-06).

## 4. EXCLUDENTES (defesa do reu)

- Caso fortuito / forca maior (CC 393).
- Culpa exclusiva da vitima; fato exclusivo de terceiro.
- Inexistencia de dano ou de nexo causal.
- Exercicio regular de direito / legitima defesa (CC 188).
- Prescricao (reparacao civil — 3 anos, CC 206 §3º, V — PA-05).

## 5. ESTRUTURA DA PECA

**Acao indenizatoria (autor):**
1. Enderecamento (foro — CPC 53 IV/V; domicilio do reu CPC 46) · 2. Qualificacao · 3. Dos fatos · 4. Do direito — pressupostos (conduta, culpa/risco, dano, nexo) · 5. Dos danos (material discriminado + moral + estetico) e do quantum · 6. Tutela de urgencia, se cabivel · 7. Pedidos (condenacao em R$, juros desde o evento/citacao, correcao, sucumbencia) · 8. Valor da causa (= soma dos danos) · 9. Provas.

**Defesa (reu):** impugnar cada pressuposto; excludentes; impugnar o quantum (excessivo); prescricao; ausencia de nexo/dano.

## 6. INTEGRACAO

- **CHASSI → `templates/pecas/acao-indenizatoria.md`** — abrir e preencher os `[____]` antes de redigir a inicial (padrao enxuto da casa).
- `calculos-civeis` → liquidacao do dano, juros, correcao, prescricao (PA-06/PA-05).
- `jurisprudencia-civel` → validar Sumulas (Sum. 37, 54, 362, 387, 403 — PA-01).
- `analise-documental-civel` → prova do dano e do nexo.
- `estilo-juridico-civel` → forma · `revisao-final-civel` → R1-R4.

## 7. CHECKLIST DE SAIDA

- [ ] Regime correto: subjetiva × objetiva (CC 927 § unico); contratual × extracontratual (PA-07)
- [ ] Os 4 pressupostos enderecados (ou os 3, na objetiva)
- [ ] Dano discriminado e provado; quantum fundamentado (CC 944)
- [ ] Juros e correcao com termo inicial certo (Sum. 54/362 — PA-06)
- [ ] Prescricao conferida (3 anos — PA-05) · Foro correto (P5)
- [ ] Polo coerente (PA-10) · Selo P1 feito · R1-R4 pendente
