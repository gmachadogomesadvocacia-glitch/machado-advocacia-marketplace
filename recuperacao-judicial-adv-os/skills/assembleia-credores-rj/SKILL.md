---
name: assembleia-credores-rj
description: >
  ASSEMBLEIA-CREDORES-RJ — Tier 2 (Produção). Acionar quando o usuário precisar se preparar para uma AGC, calcular quóruns de aprovação do plano (arts. 45 e 58), analisar se o cram down é viável, ou contestar irregularidades em assembleia já realizada.
---

# ASSEMBLEIA-CREDORES-RJ
> Tier 2 | AGC — Assembleia Geral de Credores | Arts. 36-46 + 56-58 LFRJ

---

## 0. ESCOPO

Prepara a estratégia assemblear completa. Opera como skill de devedor (maximizar aprovação)
ou de credor (maximizar poder de voto e bloqueio). Produz:
- Mapa de quóruns e forças
- Estratégia de aprovação / rejeição
- Documentos assembleare (pedido de convocação, ata, impugnação)
- Análise de cram down

⚠️ **PA-21**: Nunca apresentar análise de AGC sem calcular quóruns por classe individualmente.

---

## 1. REGRAS DA AGC — ARTS. 36-46 LFRJ

### 1.1 Convocação

| Aspecto | Regra |
|---------|-------|
| Quem convoca | Juiz (de ofício ou a requerimento) |
| Prazo de antecedência | 15 dias (publicação edital) |
| Presidência | Administrador Judicial |
| Publicidade | Edital em DJe e jornal de grande circulação |
| Poderes da AGC | Aprovar/rejeitar/modificar plano; eleger Comitê; deliberar sobre qualquer matéria de interesse dos credores |

### 1.2 Sistema de Votação — art. 45 LFRJ (pré-L14.112)

| Classe | Quórum de aprovação |
|--------|---------------------|
| I — Trabalhistas | Maioria simples dos credores presentes (por cabeça) |
| II — Garantia real | Maioria do valor dos créditos presentes |
| III — Quirografários | Maioria simples dos credores presentes E maioria do valor |
| IV — ME/EPP (L14.112) | Maioria simples dos credores presentes (por cabeça) |

**Regra geral pré-L14.112:** Aprovação pelo voto favorável dos credores de todas as classes,
observados os quóruns de cada classe.

### 1.3 Cram Down — art. 58, §1º (L14.112/2020)

Quando não há aprovação por todas as classes, o juiz PODE conceder a RJ se:

```
Requisitos cumulativos:
□ Aprovação por ao menos 1 das classes (após L14.112)
□ Voto favorável de mais de 1/3 dos credores nas classes que rejeitaram (por cabeça)
□ Não há discriminação injustificada entre credores (art. 58, §2º)
□ O plano não viola o "melhor interesse dos credores" (cada credor recebe ao menos
  o que receberia na falência)
□ [VERIFICAR] — Jurisprudência pós-L14.112 ainda em desenvolvimento
```

---

## 2. MAPA DE QUÓRUNS E FORÇAS

### 2.1 Instrumento de mapeamento

Para cada AGC, preencher a matriz de forças:

```
MAPA DE QUÓRUNS — [NOME DO DEVEDOR] — AGC de [data]

CLASSE I — TRABALHISTAS
Valor total: R$ [...]   |   Nº credores: [...]
┌─────────────────┬──────────────┬────────────────┬──────────┐
│ Credor          │ Valor (R$)   │ % da classe    │ Posição  │
├─────────────────┼──────────────┼────────────────┼──────────┤
│ [Nome]          │ [valor]      │ [%]            │ Favorável/Contrário/Indefinido │
└─────────────────┴──────────────┴────────────────┴──────────┘
Resultado estimado: [APROVAÇÃO / REJEIÇÃO / INCERTO]
Quórum necessário: maioria simples por cabeça

CLASSE II — GARANTIA REAL
[idem]
Quórum necessário: maioria do valor

CLASSE III — QUIROGRAFÁRIOS
[idem]
Quórum necessário: maioria simples por cabeça + maioria do valor

CLASSE IV — ME/EPP (se houver)
[idem]
Quórum necessário: maioria simples por cabeça
```

### 2.2 Análise estratégica

Com base no mapa, responder:
1. Qual classe apresenta maior risco de rejeição?
2. Qual credor/grupo de credores pode ser o "fiel da balança"?
3. É possível renegociar condições específicas para garantir aprovação de uma classe?
4. Se uma classe rejeitar: os requisitos do cram down estão preenchidos?
5. Há credores com habilitação disputada que, se incluídos/excluídos, alteram o quórum?

---

## 3. ESTRATÉGIAS POR POLO

### 3.1 Polo Devedor — maximizar aprovação

```
1. Identificar credores-chave com maior peso (valor) em cada classe
2. Negociar bilateralmente condições específicas para credores estratégicos
   (desde que mantido o tratamento igualitário dentro da mesma classe)
3. Oferecer garantias adicionais a credores com garantia real (Classe II)
   para converter posição de contrário para favorável
4. Para Classe I: garantir pagamento integral dos menores créditos trabalhistas
   rapidamente — cria goodwill e aprovação por cabeça
5. Para cram down: estratégia de aprovação mínima em 1 classe para acionar art. 58, §1º
```

### 3.2 Polo Credor — maximizar poder de bloqueio

```
1. Verificar se o crédito está corretamente classificado (classe errada = voto errado)
2. Identificar aliados na mesma classe para bloco de votos
3. Calcular se pode rejeitar o plano na sua classe individualmente
4. Contestar habilitações de credores ficticios ou com valores inflados
5. Apresentar plano alternativo (art. 56, §6º) se tiver 25%+ do valor total dos créditos
```

---

## 4. DOCUMENTOS DA AGC

### 4.1 Requerimento de Convocação de AGC (por credor)

```
EXCELENTÍSSIMO SENHOR DOUTOR JUIZ DE DIREITO
[VARA EMPRESARIAL / FALIMENTAR — COMARCA]

Processo nº [...] — Recuperação Judicial de [DEVEDOR]

[CREDOR], pessoa [jurídica/física], já qualificado nos autos, com crédito de
R$ [...] (Classe [I/II/III/IV]), vem, com base no art. 36 da L11.101/2005,
requerer a CONVOCAÇÃO DE ASSEMBLEIA GERAL DE CREDORES para deliberação sobre:

[objeto]

Fundamentos: [...]

Pedido: Defira a convocação com antecedência mínima de 15 dias, determinando
publicação de edital na forma do art. 36, §1º.
```

### 4.2 Impugnação de Deliberação Assemblear

Cabível quando houver:
- Irregularidade no procedimento de convocação
- Votação irregular (credores não habilitados votando)
- Cômputo incorreto dos votos por classe
- Impedimento de credor legítimo de votar
- Aprovação de matéria estranha à pauta

---

## 5. VEDAÇÕES (PA aplicáveis)

- **PA-07**: Classes de credores com regras de votação distintas — nunca misturar
- **PA-19**: Quóruns e regras de votação da L14.112/2020 — verificar texto vigente
- **PA-20**: Calcular cram down antes de concluir que o plano está rejeitado
- **PA-21**: Nunca apresentar análise de AGC sem calcular quóruns por classe
- **PA-24**: Revisao-final-rj antes de protocolar qualquer documento assemblear
