---
name: triagem-familia
description: >
  TRIAGEM-FAMILIA — Tier 1 (Porta de Entrada). Acionar sempre que um novo caso de família ou sucessões for aberto ou quando o usuário descrever uma situação familiar sem ainda ter identificado o caminho jurídico adequado.
metadata:
  version: "1.0.0"
---

# TRIAGEM-FAMILIA
> Tier 1 | Porta de Entrada | Polo / Tipo / Documentos / Competência / CASO.md

---

## 0. ESCOPO

Ponto de entrada obrigatório para qualquer novo caso. Esta skill:
- Identifica polo processual e tipo de caso
- Classifica como judicial ou extrajudicial
- Verifica condições de admissibilidade
- Mapeia documentos necessários
- Determina competência (vara ou cartório)
- Cria o CASO.md com estado inicial
- Dispara CHECKPOINT 1

Não produz peças. Produz: CASO.md + mapa de lacunas + rota estratégica inicial.

---

## 1. PROTOCOLO DE TRIAGEM

### 1.1 Coleta de Informações Essenciais

Execute as perguntas a seguir (ou extraia do contexto fornecido):

**Sobre as partes:**
1. Nome completo, CPF, profissão e renda estimada do cliente
2. Nome completo, CPF, profissão e renda estimada da outra parte
3. Há filhos? Quais idades? Há algum menor ou incapaz?
4. Estado civil formal (casados / união estável / solteiros)

**Sobre o caso:**
5. Qual é o objeto principal? (divórcio, alimentos, guarda, inventário, outro)
6. Há imóveis, veículos, empresas, investimentos ou dívidas relevantes?
7. Regime de bens (se casamento): comunhão parcial / universal / separação / participação
8. Data de início do casamento ou da união estável
9. Há separação de fato? Desde quando?
10. Há processo judicial em andamento? Qual número?
11. Há urgência? (liminar de alimentos, guarda emergencial, medida protetiva)
12. As partes já têm advogado? Há disposição para acordo?

**Para sucessões:**
13. Data do óbito e data da ciência do óbito pelo herdeiro
14. Há testamento? (público, particular, cerrado)
15. Quais são os herdeiros (descendentes, ascendentes, cônjuge/companheiro)?
16. O inventário será judicial ou extrajudicial? (verificar Res. 35/2007 CNJ)
17. Há bens imóveis? Em quais municípios?

---

### 1.2 Classificação: Judicial × Extrajudicial

**EXTRAJUDICIAL é possível quando** (Res. 35/2007 CNJ):
- Divórcio/separação: partes capazes, consensual, sem filhos menores/incapazes
- Inventário: todos os herdeiros capazes, consensual, sem testamento (em regra), advogado constituído
- Partilha: idem ao inventário

**JUDICIAL é obrigatório quando**:
- Há filhos menores ou incapazes (família)
- Há litígio entre as partes
- Há testamento contestado ou com restrições
- Há herdeiro incapaz ou ausente
- Uma das partes não tem advogado próprio (divórcio com advogado único — possível com cautela)

---

### 1.3 Competência

**Família (judicial)**:
- Ação de divórcio/dissolução: domicílio do guardião dos filhos; ausente → domicílio do réu
- Alimentos: domicílio do alimentando (Súm. 1 STJ)
- Guarda: domicílio da criança
- Vara de Família da Comarca de {{CIDADE}}/{{UF}} → verificar distribuição
- Casos de violência doméstica: Juizado de Violência Doméstica e Familiar

**Família (extrajudicial)**:
- Qualquer tabelionato de notas (escolha das partes — dentro ou fora da comarca)

**Sucessões (judicial)**:
- Inventário: último domicílio do falecido (art. 48 CPC)
- Se domicílio em {{CIDADE}}: distribuição nas varas cíveis (verificar redistribuição)

**Sucessões (extrajudicial)**:
- Qualquer tabelionato de notas onde houver imóvel ou, à livre escolha, se não houver imóvel

---

### 1.4 Documentos por Tipo de Caso

**DIVÓRCIO / SEPARAÇÃO**:
| Documento | Prioridade |
|-----------|-----------|
| Certidão de casamento (atualizada — últimos 90 dias) | Alta |
| RG e CPF de ambas as partes | Alta |
| Comprovante de residência | Alta |
| Escrituras e matrículas de imóveis | Alta |
| CRLVs de veículos | Média |
| Declaração de IR dos últimos 2 anos | Alta |
| Contratos sociais (se houver empresa) | Média |
| Extratos de investimentos e contas bancárias | Média |
| Certidão de nascimento dos filhos (se houver) | Alta |

**GUARDA E ALIMENTOS**:
| Documento | Prioridade |
|-----------|-----------|
| Certidão de nascimento dos filhos | Alta |
| Comprovante de renda do alimentante (holerites, IR, extratos) | Alta |
| Comprovante de despesas dos filhos (escola, saúde, atividades) | Alta |
| Estudo social ou laudo psicológico (se houver) | Média |

**INVENTÁRIO / ARROLAMENTO**:
| Documento | Prioridade |
|-----------|-----------|
| Certidão de óbito | Alta |
| RG e CPF do falecido e de todos os herdeiros | Alta |
| Certidão de casamento do falecido | Alta |
| Certidão de nascimento dos filhos | Alta |
| Escrituras e matrículas de imóveis | Alta |
| Declaração de IR dos 2 últimos anos (falecido) | Alta |
| Extratos de contas e investimentos | Alta |
| CRLVs de veículos | Média |
| Contratos sociais de empresas | Média |
| Testamento (se houver) | Alta |
| Certidão negativa de débitos (municipal, estadual, federal) | Média |

---

### 1.5 Checklist de Urgências

```
⚠️ URGÊNCIAS QUE REQUEREM TUTELA IMEDIATA:
□ Criança em risco de alienação parental
□ Alimentos atrasados (execução ou pedido inicial)
□ Ameaça de dilapidação patrimonial
□ Violência doméstica / necessidade de medida protetiva
□ Prazo de 60 dias para abertura do inventário (da ciência do óbito)
□ Leilão ou penhora de bem do espólio
□ Prazo recursal em andamento
```

Se algum item estiver marcado → acione **tutela-urgencia-familia** imediatamente.

---

## 2. CRIAÇÃO DO CASO.md

Ao final, gere o CASO.md conforme estrutura definida em **familia-master** (Seção 6).
Preencha todos os campos disponíveis. Marque com `[verificar]` o que estiver pendente.

---

## 3. CHECKPOINT 1

```
CHECKPOINT 1 — VALIDAÇÃO DE TRIAGEM
✅ Polo identificado: [...]
✅ Tipo de caso: [...]
✅ Via: [ ] Judicial — Vara de Família, {{CIDADE}}/{{UF}}
         [ ] Extrajudicial — Tabelionato de Notas
⚠️ Documentos faltantes: [lista]
⚠️ Urgências identificadas: [lista]
⚠️ Riscos: [lista]

Próximos passos:
1. [ação imediata]
2. [ação seguinte]
3. [skill recomendada]

CONFIRMAR para prosseguir?
```

Só avança após confirmação do advogado.
