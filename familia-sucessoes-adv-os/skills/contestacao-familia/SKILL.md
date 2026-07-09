---
name: contestacao-familia
description: >
  CONTESTACAO-FAMILIA — Tier 2 (Produção). Acionar quando o advogado atuar pelo réu e precisar redigir a resposta ao processo.
metadata:
  version: "1.0.0"
---

# CONTESTACAO-FAMILIA
> Tier 2 | Produção | Contestação / Resposta | Polo Requerido

---

## 0. PRÉ-REDAÇÃO

```
□ CASO.md lido — polo REQUERIDO confirmado?
□ Petição inicial do adversário lida e resumida?
□ Documentos do cliente compilados?
□ Há exceções processuais a alegar? (incompetência, litispendência, conexão)
□ Há preliminares de mérito? (ilegitimidade, inépcia, prescrição/decadência)
□ Reconvenção necessária? (contra-ataque — alimentos, guarda, bens)
□ Prazo: 30 dias contados da citação (art. 335 CPC)
```

---

## 1. ESTRUTURA-PADRÃO

```
I — DA TEMPESTIVIDADE
  Citado em [data], o prazo de 30 dias vence em [data]. Tempestiva.

II — DAS PRELIMINARES (se houver)
  II.1 — Da incompetência relativa / absoluta
  II.2 — Da ilegitimidade de parte
  II.3 — Da inépcia da petição inicial
  II.4 — Da carência de ação (falta de interesse / possibilidade jurídica)

III — DA EXCEÇÃO DE INCOMPETÊNCIA (se outro foro)
  [Súm. 1 STJ — alimentos: foro do alimentando; divórcio: foro do guardião dos filhos]

IV — DO MÉRITO
  IV.1 — Dos fatos (versão do requerido — cronológica, objetiva)
  IV.2 — Do direito (desconstituição das teses do requerente)
  IV.3 — Dos pedidos do requerente (analisar um a um)

[V — DA RECONVENÇÃO (se cabível — art. 343 CPC)]

VI — DOS PEDIDOS
  a) acolhimento das preliminares (se houver);
  b) improcedência total dos pedidos;
  c) [pedidos específicos — redução de alimentos, guarda inversa, etc.]
  d) condenação do(a) Requerente em honorários e custas.

VII — DAS PROVAS
  [Documental juntada + testemunhal + pericial se necessário]

Nesses termos, pede deferimento.
```

---

## 2. TESES POR TIPO DE AÇÃO

### 2.1 Contestação em Divórcio Litigioso

**Sobre a partilha**:
- Verificar bens excluídos da comunhão (art. 1.659 CC — comunhão parcial)
  → bens anteriores ao casamento, doações, heranças, seguros de vida, pensões
- Demonstrar passivos comuns que devem ser divididos antes da meação
- Questionar avaliação de bens (pedir nova avaliação pericial)
- Bens onerados com dívidas: discutir compensação

**Sobre a guarda**:
- Apresentar contraproposta de guarda fundamentada no melhor interesse
- Se guarda compartilhada já é a regra (art. 1.584 §2º CC) — reforçar
- Documentar envolvimento do cliente com os filhos (fotos, mensagens, escola, médico)

**Sobre alimentos**:
- Demonstrar binômio: se alimentante → capacidade real (não aparente); se alimentando → necessidade real
- Questionar valores excessivos com comprovação de renda

---

### 2.2 Contestação em Ação de Alimentos

**Teses principais**:
- **Impossibilidade financeira**: demonstrar renda real com documentos (holerite, IR, extratos)
  e deduzir despesas próprias do alimentante
- **Ausência de necessidade do alimentando**: demonstrar que o alimentando tem renda
  ou que suas despesas são menores do que alegado
- **Alimentos excessivos**: propor valor proporcional ao binômio (art. 1.694 CC)
- **Exoneração**: maioridade + inserção no mercado de trabalho / casamento do alimentando
- **Revisão**: mudança de situação financeira (art. 1.699 CC)

```
Trinômio da jurisprudência do STJ:
1) Necessidade do alimentando
2) Possibilidade do alimentante
3) Proporcionalidade

Propor valor: R$ [X] ou [Y%] da renda líquida — justificado com cálculos
```

---

### 2.3 Contestação em Ação de Guarda

**Teses principais**:
- Melhor interesse da criança favorece o requerido (documentar rotina, vínculo, escola)
- Guarda compartilhada como regra — art. 1.584 §2º CC
- Alegações da outra parte sem fundamento (alienação parental inversa — L12.318/2010)
- Solicitar estudo psicossocial (art. 699 CPC — equipe multidisciplinar)
- Requerer oitiva da criança/adolescente (art. 28 §1º ECA)

---

### 2.4 Contestação em Inventário / Partilha

**Teses**:
- Impugnar nomeação do inventariante (art. 617 CPC — ordem de preferência)
- Impugnar avaliação dos bens
- Requerer colação de bens doados em vida (art. 2.002 CC)
- Arguir sonegados (art. 1.992 CC) — bens omitidos pelo inventariante
- Questionar partilha desproporcional — anular por vício (arts. 2.027-2.030 CC)
- Reconhecer meeiro que não foi incluído (cônjuge / companheiro)

---

## 3. RECONVENÇÃO

Usar reconvenção (art. 343 CPC) quando o requerido tem pedido próprio contra o requerente:
- Requerido pede alimentos ↔ Requerente tinha pedido guarda sem alimentos
- Requerido pede guarda unilateral ↔ Requerente pede guarda unilateral (versão contrária)
- Requerido pede partilha diferente

Reconvenção deve ter causa de pedir e pedido próprios — não é simples defesa.

---

## 4. PÓS-REDAÇÃO

1. Indicar documentos a anexar
2. Encaminhar para **revisao-final-familia**
3. Atualizar CASO.md: "Contestação redigida em [data] — prazo vence [data]"
