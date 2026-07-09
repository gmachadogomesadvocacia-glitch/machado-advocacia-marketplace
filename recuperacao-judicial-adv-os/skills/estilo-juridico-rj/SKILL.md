---
name: estilo-juridico-rj
description: >
  ESTILO-JURIDICO-RJ — Transversal (Padrão de Redação). Define e aplica o padrão técnico de redação jurídica para peças de recuperação judicial e falência: vocabulário específico de insolvência empresarial, tratamento das partes, estrutura de pedidos, forma de citar a LFRJ e jurisprudência do STJ. Aplicado automaticamente a toda peça produzida no pipeline de RJ. Consultar quando o usuário precisar padronizar uma peça, adaptar o estilo ao tipo de juízo (vara empresarial especializada), ou humanizar um texto jurídico de insolvência mantendo a precisão técnica.
---

# ESTILO-JURIDICO-RJ
> Transversal | Padrão de Redação | Insolvência Empresarial | Vara Empresarial/Falimentar

---

## 0. ESCOPO

Define o padrão de linguagem, estrutura e tom para todas as peças do pipeline de RJ.
Não produz peças — calibra e refina as peças produzidas pelas outras skills.

> Gatilho "gera docx": converter .txt em .docx timbrado via `gerador-peticoes` — Code.

---

## 1. PRINCÍPIOS DE REDAÇÃO EM INSOLVÊNCIA

### 1.1 Precisão terminológica

Em insolvência, cada palavra tem peso técnico. Use os termos corretos:

| ✅ Correto | ❌ Incorreto |
|-----------|-------------|
| Recuperação judicial | "concordata" (obsoleto — revogada pela LFRJ) |
| Stay period / suspensão do art. 6º | "proteção automática" |
| Assembleia Geral de Credores (AGC) | "reunião de credores" |
| Quadro Geral de Credores (QGC) | "lista de credores" |
| Administrador Judicial | "síndico" (obsoleto) |
| Convolação em falência | "transformação em falência" |
| Cram down | "imposição do plano" (aceitável em certos contextos) |
| Credores sujeitos à recuperação | "credores do processo" |
| Meios de recuperação (art. 50) | "formas de pagamento" |
| Haircut / deságio | "desconto" (correto — mas usar "deságio" em peças) |
| Massa falida | "empresa falida" (informal) |
| Verificação de créditos | "análise dos créditos" |

### 1.2 Identificação das partes

**Devedor:** "o Devedor" (maiúscula, sem repetir razão social em todo parágrafo)
**Credores:** "o Credor [NOME]" ou "os credores da Classe [I/II/III/IV]"
**Administrador Judicial:** "o Administrador Judicial" ou "o AJ"
**Juízo:** "este Egrégio Juízo" / "Vossa Excelência"

### 1.3 Citação da Lei de Falências

```
Primeira citação: "Lei nº 11.101, de 9 de fevereiro de 2005 (LFRJ)"
Citações subsequentes: "LFRJ" ou "a Lei"
Com reforma: "art. X da LFRJ, com a redação da Lei nº 14.112/2020"
```

### 1.4 Citação de jurisprudência do STJ

```
Padrão completo (primeira citação):
"conforme decidiu o Superior Tribunal de Justiça, na [3ª/4ª Turma],
no julgamento do REsp nº [número], Relator o Ministro [nome],
julgado em [data], publicado no DJe de [data]"

Padrão abreviado (citações subsequentes):
"(STJ, REsp [número], [Turma], Rel. Min. [nome], j. [data])"

Tema repetitivo:
"nos termos do Tema [nº] do STJ, fixou-se a tese de que [...]"
```

---

## 2. ESTRUTURA-PADRÃO POR TIPO DE PEÇA

### 2.1 Petição Inicial (RJ / Habilitação / RE)

```
[Cabeçalho: Exmo. Sr. Dr. Juiz...]
[Qualificação das partes]
[Exposição dos fatos — F do FIRAC]
[Do direito — R + A do FIRAC]
[Dos documentos juntados]
[Dos pedidos — C do FIRAC em alíneas]
[Do valor da causa]
[Nesses termos, pede deferimento.]
[Local, data]
[Advogado — OAB]
```

### 2.2 Contestação / Impugnação

```
[Cabeçalho]
[Qualificação]
[I — Da tempestividade]
[II — Da preliminar (se houver)]
[III — Do mérito]
[IV — Dos documentos]
[V — Dos pedidos]
[Nesses termos, pede deferimento.]
```

### 2.3 Recurso (AI / Apelação)

```
[Cabeçalho — tribunal destinatário]
[Qualificação]
[I — Do cabimento e tempestividade]
[II — Do efeito suspensivo (se requerido)]
[III — Dos fatos]
[IV — Do direito]
[V — Dos pedidos]
[Nesses termos, pede conhecimento e provimento.]
```

---

## 3. TOM E REGISTRO

### 3.1 Tom adequado à insolvência

Peças de RJ são lidas por juízes de varas empresariais especializadas e por administradores
judiciais com expertise financeira. O tom deve ser:

- **Técnico e objetivo**: evitar digressões filosóficas ou históricas desnecessárias
- **Economicamente informado**: demonstrar compreensão da situação financeira, não apenas jurídica
- **Pragmático**: o juiz quer saber: qual é o problema, qual é a solução, qual é o pedido
- **Não dramático**: evitar apelos emocionais sobre "empregos e famílias" em excesso — usar com parcimônia e apenas quando relevante ao fundamento do art. 47

### 3.2 Linguagem a evitar

```
❌ "Venho, mui respeitosamente, perante Vossa Excelência..."
   → Prefira: "Vem [PARTE], por meio de seu advogado, ..."

❌ Parágrafos com mais de 8 linhas sem ponto final
   → Frases curtas e diretas em insolvência

❌ Repetição excessiva dos mesmos argumentos
   → Argumento deve aparecer uma vez, com força, não três vezes diluídas

❌ "Conforme amplamente sabido..." / "É de notório saber que..."
   → Cite a lei ou jurisprudência, não o óbvio
```

### 3.3 Padrão de negrito e destaques

```
✅ Negrito para: dispositivo legal citado pela primeira vez, valor em discussão, 
   data de prazo crítico, nome das partes na qualificação
✅ Itálico para: termos em latim (fumus boni iuris, periculum in mora) ou inglês técnico (stay, cram down)
❌ Negrito excessivo (mais de 3 destaques por parágrafo)
❌ CAIXA ALTA em meio ao texto (exceto siglas estabelecidas: RJ, RE, AGC, QGC, AJ)
```

---

## 4. VALORES E DATAS

```
Valores monetários:
✅ "R$ 1.500.000,00 (um milhão e quinhentos mil reais)"
❌ "R$1.5M" ou "R$ 1.500.000"

Datas:
✅ "[dia] de [mês por extenso] de [ano]"
✅ "[dia]/[mês]/[ano]" em tabelas

Percentuais:
✅ "70% (setenta por cento)"
✅ "3/5 (três quintos) do valor total dos créditos"
```

---

## 5. CHECKLIST DE ESTILO (aplicar antes da revisao-final-rj)

```
□ Terminologia técnica correta (sem "concordata", "síndico")?
□ Partes identificadas consistentemente ao longo da peça?
□ Citações da LFRJ com número de artigo e versão correta (pré ou pós L14.112)?
□ Jurisprudência no formato correto?
□ Tom técnico-objetivo sem dramatismo excessivo?
□ Pedidos em alíneas (a, b, c) claras e numeradas?
□ Valores com centavos e por extenso?
□ Siglas definidas na primeira ocorrência?
```
