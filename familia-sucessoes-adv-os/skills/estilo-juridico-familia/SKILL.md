---
name: estilo-juridico-familia
description: >
  ESTILO-JURIDICO-FAMILIA — Transversal (Padrão de Redação). Define e aplica o padrão técnico
  de redação jurídica para peças de Direito de Família e Sucessões: vocabulário específico,
  tratamento das partes, estrutura de pedidos, forma de citar o CC/2002 e jurisprudência do STJ.
  Ajusta o tom conforme o tipo de peça: conciliatório (acordos, mediação), técnico-firme
  (petições), combativo (resistência a abuso). Consultar quando o usuário precisar padronizar
  ou revisar o estilo de uma peça, ou quando uma peça estiver tecnicamente correta mas
  com linguagem inadequada para o tipo de demanda familiar.
metadata:
  version: "1.0.0"
---

# ESTILO-JURIDICO-FAMILIA
> Transversal | Padrão de Redação | Família e Sucessões | TJ{{UF}} — Vara de Família

---

## 0. ESCOPO

Define linguagem, estrutura e tom para todas as peças do pipeline de família e sucessões.
Não produz peças — calibra e refina as peças produzidas pelas outras skills.

---

## 1. ESCALA DE TOM

O Direito de Família exige calibração de tom conforme o contexto:

| Situação | Tom | Escala |
|----------|-----|--------|
| Acordo extrajudicial / escritura pública | Conciliatório, neutro | 3/10 |
| Petição inicial consensual (divórcio conjunto) | Técnico, objetivo | 4/10 |
| Audiência de mediação / conciliação | Firme mas colaborativo | 5/10 |
| Petição inicial contenciosa | Técnico-assertivo | 7/10 |
| Contestação / réplica | Técnico-combativo | 7/10 |
| Recursos | Técnico-combativo | 8/10 |
| Violência doméstica / alienação parental / espoliação | Incisivo e documentado | 9/10 |

**Default do escritório: 7/10** — ajustar conforme o tipo de peça.

---

## 2. PRECISÃO TERMINOLÓGICA

Use os termos corretos em Direito de Família e Sucessões:

| ✅ Correto | ❌ Incorreto |
|-----------|-------------|
| Divórcio | "desquite" (obsoleto — L6.515/1977) |
| Regime de comunhão parcial de bens | "regime geral" |
| Meação | "metade dos bens" (impreciso — direito, não fração) |
| Legítima / quota indisponível | "herança obrigatória" |
| Monte-mor / Acervo hereditário | "bens do morto" |
| Herdeiros necessários (art. 1.845 CC) | "herdeiros obrigatórios" |
| Companheiro(a) / União estável | "amásio(a)" (informal, inadequado) |
| Alimentos / pensão alimentícia | "pensão" (sozinho — ambíguo) |
| Guarda compartilhada | "guarda alternada" (diferente — ver art. 1.583 CC) |
| Convivência / visitação | "visita" (prefira convivência — mais amplo e moderno) |
| Interdição | "incapacidade" (o resultado, não o processo) |
| Tomada de Decisão Apoiada (TDA) | "curatela leve" |
| Inventariante | "responsável pelo espólio" |
| Colação / imputação | "devolver bens" |
| Sonegação (art. 1.992 CC) | "esconder bens" |

---

## 3. IDENTIFICAÇÃO DAS PARTES

**Em peças de dissolução conjugal:**
- Requerente: "o(a) Requerente" (maiúscula)
- Requerido: "o(a) Requerido(a)"
- Filhos: "o(a) menor [NOME]" ou "a criança/adolescente [NOME]"
- Juízo: "este Egrégio Juízo" / "Vossa Excelência"

**Em inventário:**
- "o Espólio de [NOME DO FALECIDO]"
- "o(a) Inventariante [NOME]"
- "o(a) herdeiro(a) [NOME]"
- "o Meeiro / a Meeira [NOME]" (quando cônjuge/companheiro)

**Em alimentos:**
- Alimentante: "o(a) Alimentante" — nunca "o devedor" em peças iniciais
- Alimentando: "o(a) Alimentando(a)" ou "a criança/adolescente [NOME]"

---

## 4. CITAÇÃO DO CC/2002

```
Primeira citação: "Código Civil (Lei nº 10.406, de 10 de janeiro de 2002 — CC/2002)"
Citações subsequentes: "CC/2002" ou "o Código Civil"
Com artigo: "art. 1.694, caput, do CC/2002"
Sem confundir com CPC:
  CPC → "art. XXX do CPC/2015" / "Lei nº 13.105/2015"
```

---

## 5. CITAÇÃO DE JURISPRUDÊNCIA DO STJ

```
Padrão completo (primeira citação):
"conforme decidiu o Superior Tribunal de Justiça, na [3ª/4ª Turma],
no julgamento do REsp nº [número], Relatora a Ministra [nome],
julgado em [data], publicado no DJe de [data]"

Padrão abreviado (citações subsequentes):
"(STJ, REsp [número], [Turma], Rel. Min. [nome], j. [data])"

Súmula STJ:
"na forma da Súmula nº [número] do STJ: '[enunciado]'"

Tema repetitivo:
"nos termos do Tema [nº] do STJ, fixou-se a tese de que [...]"

⚠️ PA-01: Nunca citar julgado não confirmado. Se não tiver certeza, use
"conforme jurisprudência do STJ" ou acione jurisprudencia-familia.
```

---

## 6. ESTRUTURA-PADRÃO POR TIPO DE PEÇA

### 6.1 Petição Inicial

```
EXMO(A). SR(A). DR(A). JUIZ(A) DE DIREITO DA [Xª VARA DE FAMÍLIA DE {{CIDADE}}/{{UF}}]

[NOME DO CLIENTE], [qualificação completa: nacionalidade, estado civil, profissão, RG, CPF,
endereço], por seu advogado que esta subscreve (OAB/{{OAB_UF}} {{OAB_NUMERO}} — {{ADVOGADO_NOME}}),
vem, respeitosamente, perante Vossa Excelência, propor a presente

[AÇÃO DE (NOME DA AÇÃO)]

em face de [NOME DO RÉU], [qualificação], pelos fatos e fundamentos jurídicos a seguir:

I — DOS FATOS
[Narrativa cronológica, objetiva, com datas]

II — DO DIREITO
[Base legal — CC/2002 + CPC/2015 + legislação especial + jurisprudência validada]

III — DOS PEDIDOS
Ante o exposto, requer:
a) [pedido principal]
b) [pedido acessório]
c) [tutela antecipada, se cabível]
d) [produção de provas]
e) a intimação do(a) Requerido(a) para responder à presente ação;
f) a condenação do(a) Requerido(a) ao pagamento das custas e honorários advocatícios.

IV — DO VALOR DA CAUSA
Dá-se à presente causa o valor de R$ [VALOR] ([por extenso]).

Nesses termos, pede deferimento.

{{CIDADE}}/{{UF}}, [data].

{{ADVOGADO_NOME}}
OAB/{{OAB_UF}} {{OAB_NUMERO}}
{{FIRM_NAME}}
```

### 6.2 Contestação

```
[Cabeçalho]
I — DA TEMPESTIVIDADE
II — DA PRELIMINAR (se houver: ilegitimidade, inépcia, coisa julgada)
III — DO MÉRITO
  III.1 — Dos fatos (versão do requerido)
  III.2 — Do direito (desconstituição das alegações)
IV — DA IMPUGNAÇÃO AOS DOCUMENTOS (se houver)
V — DOS PEDIDOS
  a) acolhimento das preliminares (se houver);
  b) improcedência total dos pedidos;
  c) condenação do(a) Requerente em honorários e custas.
```

### 6.3 Recurso (Apelação / Agravo)

```
[Cabeçalho — Tribunal de Destino: TJ{{UF}}]
I — DO CABIMENTO E TEMPESTIVIDADE
II — DO EFEITO SUSPENSIVO (se requerido — art. 1.012 CPC)
III — DOS FATOS
IV — DAS RAZÕES
  IV.1 — [primeiro fundamento]
  IV.2 — [segundo fundamento]
V — DOS PEDIDOS
  Requer conhecimento e provimento do presente recurso, para [resultado pretendido].
```

---

## 7. LINGUAGEM A EVITAR

```
❌ "Venho, com o devido respeito, mui respeitosamente..."
   → Prefira: "Vem [PARTE], por seu advogado, propor..."

❌ Adjetivos emocionais desnecessários: "cruel", "monstruoso", "perverso"
   → Use fatos e documentos — deixe os fatos falar

❌ Parágrafo com mais de 8 linhas sem ponto final em peças técnicas
   → Em Família, peças claras e diretas convencem mais

❌ Repetição de argumentos
   → Um argumento forte, uma vez, com fundamento

❌ "Conforme é de notório saber..."
   → Cite a lei ou o precedente

❌ "O pai/mãe não presta" sem fato concreto
   → Específico: "em [data], o(a) [PARTE] deixou de pagar a pensão de R$ X,
      conforme extrato bancário juntado às fls. X"
```

---

## 8. VALORES, DATAS E FORMATAÇÃO

```
Valores monetários:
✅ "R$ 3.500,00 (três mil e quinhentos reais)"
❌ "R$3500" ou "3.500 reais"

Datas:
✅ "[dia] de [mês por extenso] de [ano]"
✅ "[dd/mm/aaaa]" em tabelas e listas

Percentuais:
✅ "25% (vinte e cinco por cento)"

ITCMD ({{UF}}): sempre "4% (quatro por cento) sobre o valor de mercado do bem"
ITBI ({{CIDADE}}): verificar alíquota municipal vigente (art. 156, II, CF)
```

---

## 9. CHECKLIST DE ESTILO (aplicar antes da revisao-final-familia)

```
□ Terminologia correta (sem "desquite", "amásio", "pensão" sem qualificação)?
□ Partes identificadas consistentemente ao longo da peça?
□ Citações do CC/2002 com número de artigo correto?
□ Jurisprudência no formato correto e validada?
□ Tom ajustado ao tipo de peça (combativo/conciliatório)?
□ Pedidos em alíneas (a, b, c) claras e numeradas?
□ Valores com centavos e por extenso?
□ Endereçamento: Vara de Família — {{CIDADE}}/{{UF}}?
□ Assinatura: {{ADVOGADO_NOME}} — OAB/{{OAB_UF}} {{OAB_NUMERO}} — {{FIRM_NAME}}?
```
