---
name: jurisprudencia-civel
description: >
  Jurisprudencia civel Tier 1 — validacao jurisprudencial (PA-01). Hierarquia STF > STJ > TJ. Como
  confirmar sumula, tema repetitivo e precedente ANTES de citar (nunca alucinar). Catalogo de sumulas
  STJ consagradas em materia civel (sempre validar): Sum. 54 (juros de mora desde o evento na
  extracontratual), Sum. 362 (correcao do dano moral desde o arbitramento), Sum. 37 (cumulacao de dano
  material e moral), Sum. 387 (cumulacao de dano estetico e moral), Sum. 403 (dano pelo uso de imagem com
  fins economicos), Sum. 326 (sem sucumbencia ao autor por dano moral arbitrado a menor), Sum. 43
  (correcao do dano material desde o efetivo prejuizo). Ative quando o usuario pedir jurisprudencia,
  sumula, tema, precedente ou fundamento de tribunal em materia civel.
metadata:
  version: "0.1.0"
  area: "Direito Civil e Processo Civil"
  tier: 1
---

# JURISPRUDENCIA CIVEL

> Tier 1 (Insumo). Faz cumprir a **PA-01 — proibicao de alucinacao jurisprudencial**. **Regra de ouro: nunca citar sumula, tema ou precedente sem validar.** Se nao for possivel confirmar, citar como tese e sinalizar "(validar)".

---

## 1. HIERARQUIA E PESO

```
STF (constitucional / repercussao geral)
  > STJ (uniformizacao da lei federal / repetitivos / sumulas)
    > TJ local (orientacao de 2º grau — foro-eixo {{CIDADE}}/{{UF}})
```
- Repetitivo (STJ) / repercussao geral (STF) → forca vinculante (CPC 927).
- Preferir precedente **atual** e do **tribunal competente**.

## 2. COMO VALIDAR ANTES DE CITAR

1. Confirmar **numero + enunciado + tribunal** (nao citar de memoria).
2. Conferir se a sumula/tema **continua vigente** (nao cancelado/superado).
3. Conferir **aderencia factica** — a tese cabe no caso concreto?
4. Conferir o **regime** (contratual x extracontratual — muda o termo dos juros; PA-07).
5. Sem confirmacao segura → marcar **"(validar)"** e nao afirmar como certo.

## 3. SUMULAS STJ CONSAGRADAS — MATERIA CIVEL (sempre validar)

| Sumula | Enunciado (sintese) | Uso |
|--------|---------------------|-----|
| **54** | Juros de mora correm do **evento danoso** na responsabilidade **extracontratual** | Liquidacao (`calculos-civeis`) |
| **362** | Correcao monetaria do **dano moral** desde a data do **arbitramento** | Liquidacao do moral |
| **43** | Correcao do **dano material** desde a data do **efetivo prejuizo** | Liquidacao do material |
| **37** | Cumulaveis as indenizacoes por **dano material e moral** do mesmo fato | Cumulacao de pedidos |
| **387** | Cumulaveis as indenizacoes por **dano estetico e moral** | Cumulacao de pedidos |
| **403** | Independe de prova de prejuizo a indenizacao pelo uso **nao autorizado da imagem com fins economicos** | Direito de imagem |
| **326** | Na acao de dano moral, condenacao em montante **inferior** ao pedido **nao gera sucumbencia** ao autor | Custas/honorarios |

> Estes enunciados sao consagrados, mas a citacao em peca exige **conferir o texto oficial atual** (PA-01). Distinguir contratual x extracontratual ao aplicar a Sum. 54 (na contratual, mora em regra da citacao/constituicao).

## 4. PESQUISA DE TESE NOVA

- Buscar repetitivo/sumula sobre o ponto antes de fundamentar.
- Se a tese for de **outro plugin** (consumo/familia/imovel/medico/fiscal/penal/trabalho/INSS), nao redigir aqui — rotear (PA-09).
- Nunca inventar **numero de Tema** ou de REsp; sem fonte confiavel, descrever a orientacao sem atribuir numero.

## 5. SAIDA

```
PRECEDENTES APLICAVEIS
- Sum. STJ XX — <enunciado> — [CONFIRMADO / VALIDAR] — uso: ...
- Tema/REsp — <tese> — [VALIDAR]
TESE ADVERSA POSSIVEL (precedente contrario): ...
```
Alimenta `analise-trilateral-civel` e `linha-estrategica-civel`.

## 6. ALERTAS

- Sem confirmacao → **nao citar como certo** (PA-01).
- Sum. 54 (evento) so na **extracontratual** — na contratual, regra diversa (PA-07).
- Correcao: moral pela Sum. 362 (arbitramento); material pela Sum. 43 (prejuizo). Nao trocar.
- Cumulacao material+moral (37) e estetico+moral (387) — coerencia com os pedidos (PA-08).
