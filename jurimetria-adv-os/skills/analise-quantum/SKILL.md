---
name: analise-quantum
description: >
  ANALISE QUANTUM — Skill Tier 2. Constroi a faixa de valores (quantum) de um tema combinando as duas
  fontes que TEM valor: o acervo proprio (quantum pretendido/obtido dos blocos jurimetricos) e a
  jurisprudencia dos tribunais (valores em acordaos de temas semelhantes). Metodo bifasico inspirado
  na ABJ: primeiro a taxa de procedencia do tema, depois a distribuicao de valor entre os
  procedentes. O DataJud NAO participa (nao tem quantum). Acione para "qual a faixa de condenacao em
  X", "quanto vale um caso desses", "quanto pedir", ou a perna de valor de uma viabilidade.
metadata:
  version: "0.1.0"
  area: "Jurimetria"
  tier: 2
---

# ANALISE QUANTUM

> Skill **Tier 2**. Valor e o dado mais sensivel do sistema: e onde a promessa proibida (PE-03) mora. A saida e sempre FAIXA descritiva com procedencia dos valores — nunca "voce vai receber X".

---

## 0. FONTES (e so elas)

| Fonte | O que da | Cuidado |
|-------|----------|---------|
| **Acervo proprio** (Modulo C, casos FECHADOS do recorte) | quantum_pretendido x obtido reais, acordos incluidos | N quase sempre pequeno → PE-04 |
| **Jurisprudencia** (acordaos do tribunal de referencia no tema) | valores arbitrados em 2o grau | e amostra do que foi RECORRIDO — vies duplo (PE-05); cada valor citado com processo/orgao/data `[VERIFICAR]` se nao conferido |

**DataJud nao entra** (PE-07). APIs comerciais com quantum (Data Lawyer, Predictus, Digesto) sao opcao paga fora do MVP — mencionar, nao integrar.

## 1. METODO BIFASICO (inspirado na ABJ)

Nunca misturar as duas perguntas num numero so:

1. **Fase 1 — Procedencia:** no recorte, qual a proporcao de procedente/parcial/improcedente/acordo? (Acervo: `por_resultado` dos fechados; jurisprudencia: leitura qualitativa.) Com N < limiar → so qualitativo.
2. **Fase 2 — Valor entre os procedentes:** distribuicao do quantum SO nos casos com exito (mediana, faixa, quartis se N permitir — PE-11). Media esconde outlier; distribuicao judicial e assimetrica.

"Valor esperado" (procedencia x valor) so com os DOIS Ns declarados e rotulo explicito de descritivo — e nunca em material que va ao cliente sem reformulacao qualitativa (PE-03).

## 2. EXECUCAO

1. Recorte da triagem → dataset do acervo (`coletar_acervo.py --json`) filtrado por area/assunto + `resultado` preenchido.
2. Jurisprudencia: pesquisar o tema nos tribunais de referencia; extrair valores com identificacao completa. Sem inventar julgado — regra PA-01 dos plugins de area vale aqui dobrada.
3. Montar as duas fases; harmonizar: mesmo tema, mesmo tribunal, epoca proxima (valor de 2015 nao e valor de hoje — corrigir ou declarar nominal).
4. Cruzar: acervo dentro da faixa da jurisprudencia? Divergencia e achado, nao erro — investigar recorte.

## 3. SAIDA

```
FAIXA DE QUANTUM — <tema/recorte>
Fase 1 (procedencia): [distribuicao com N e fonte] ou [qualitativo]
Fase 2 (valor entre procedentes):
  - Acervo proprio: mediana R$ __, faixa R$ __ a __ (N=__, fechados, coleta AAAA-MM-DD)
  - Jurisprudencia <tribunal>: valores de R$ __ a __ ([lista de julgados com data])
Limitacoes: [Ns, vies de selecao das 2 fontes, epoca dos valores]
Leitura: [o que da para dizer; o que NAO da]
```

## 4. ENCERRAMENTO

A faixa serve de referencia interna para pedido/proposta — a decisao de quanto pedir e do advogado. Se o numero for para peca, viaja com carimbo completo (PE-13) e entra pela skill do plugin da area.
