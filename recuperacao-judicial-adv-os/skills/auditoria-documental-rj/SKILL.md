---
name: auditoria-documental-rj
description: >
  AUDITORIA-DOCUMENTAL-RJ — Tier 1 (Insumo). Analisa os documentos de recuperação judicial:
  demonstrações contábeis, relação de credores, balanços, extratos, certidões e todos os
  documentos do art. 51 da LFRJ. Identifica lacunas, inconsistências, ativos ocultos,
  passivos contingentes e riscos de impugnação. Acionar quando o usuário precisar revisar
  documentos financeiros de empresa em RJ, analisar o art. 51, ou preparar a auditoria
  pré-petição para o devedor ou pré-habilitação para o credor.
---

# AUDITORIA-DOCUMENTAL-RJ
> Tier 1 | Análise Documental | Art. 51 LFRJ + Demonstrações + Contingências

---

## 0. ESCOPO

Recebe documentos financeiros e jurídicos do caso. Analisa, aponta lacunas, inconsistências
e riscos. Produz: Relatório de Auditoria Documental (RAD) + lista de pendências + alertas críticos.

Não redige peças processuais. Alimenta: plano-recuperacao-rj, habilitacao-credito-rj, contestacao-rj.

---

## 1. POSIÇÃO NA ORQUESTRA

```
triagem-rj (CASO.md)
        ↓
[auditoria-documental-rj]  ←─ Tier 1
  +  analise-viabilidade-rj
        ↓
  CHECKPOINT 2
        ↓
  plano-recuperacao-rj / habilitacao-credito-rj / contestacao-rj
```

---

## 2. PROTOCOLO DE ANÁLISE

### 2.1 Checklist do art. 51 LFRJ

Para cada documento, avaliar: **Recebido / Pendente / Incompleto / Inconsistente**

**Documentos Obrigatórios:**

| Item | Documento | Status | Observação |
|------|-----------|--------|------------|
| Art. 51, I | Exposição das causas da crise | | |
| Art. 51, II-a | Balanço patrimonial (últimos 3 anos) | | |
| Art. 51, II-b | DRE (últimos 3 anos) | | |
| Art. 51, II-c | DFC (últimos 3 anos) | | |
| Art. 51, II-d | DMPL (últimos 3 anos) | | |
| Art. 51, II-e | Notas explicativas | | |
| Art. 51, III | Relação nominal completa de credores | | |
| Art. 51, IV | Relação de empregados e salários | | |
| Art. 51, V | Certidão da Junta Comercial | | |
| Art. 51, VI | Relação e avaliação dos bens do ativo | | |
| Art. 51, VII | Extratos bancários (últimos 90 dias) | | |
| Art. 51, VIII | Relação de ações judiciais e processos | | |
| Art. 51, IX | Certidões de protesto | | |
| Art. 51, X | Identificação dos administradores (3 anos) | | |

### 2.2 Análise das Demonstrações Contábeis

Ao receber balanços, verificar:

**Ativo:**
- Há bens imóveis? Estão avaliados a valor de mercado ou valor contábil defasado?
- Recebíveis: estão provisionados adequadamente? Há créditos incobráveis inflando o ativo?
- Estoque: avaliação consistente com o setor? Há obsolescência não provisionada?
- Participações em controladas/coligadas: há consolidação necessária?

**Passivo:**
- Há passivos contingentes não contabilizados (processos trabalhistas, ambientais, tributários)?
- Dívidas fiscais: existe parcelamento ativo (PERT, REFIS)? Qual o montante?
- Créditos com garantia real: os bens dados em garantia estão identificados?
- Debêntures, CCB, CRI, CRA: condições de vencimento antecipado?

**Patrimônio Líquido:**
- PL negativo? Há mais de 2 exercícios consecutivos com PL negativo?
- Capital social integralizado conforme contrato/estatuto?

### 2.3 Análise da Relação de Credores

Verificar para cada credor listado:

```
□ Nome/CNPJ completo e correto
□ Valor correto (principal + juros + multa até a data do pedido)
□ Classificação correta (Classe I, II, III ou IV)
□ Documentação de suporte (nota fiscal, contrato, sentença)
□ Créditos trabalhistas: valor não excede 150 SM por credor (PA-08)?
□ Créditos com garantia real: bem dado em garantia identificado?
□ Presença de credores extraconcursais (art. 84) — segregar (PA-15)
```

**Alertas de classificação incorreta:**
- Créditos fiscais NÃO se sujeitam à RJ — listar separadamente
- Créditos de proprietários/sócios com contrato de mútuo — avaliar subordinação
- Créditos de empresas do grupo — risco de desconsideração

### 2.4 Detecção de Riscos no Período Suspeito

⚠️ **PA-12**: Atos praticados nos 2 anos anteriores ao pedido podem ser revogados (art. 129-130).

Identificar:
- Pagamentos antecipados a credores específicos (preferência indevida)
- Alienação de bens a valor inferior ao de mercado
- Constituição de garantias pós-vencimento da dívida
- Transferências para sócios ou empresas relacionadas
- Pagamento integral de dívidas quirografárias estando em crise

### 2.5 Documentos Específicos por Porte

**Para ME/EPP (Classe IV — L14.112/2020):**
- Certidão de enquadramento no Simples Nacional ou declaração
- Faturamento dos últimos 12 meses (limite ME: R$ 360k; EPP: R$ 4,8M)

**Para grupos econômicos:**
- Verificar necessidade de consolidação processual (PA-14)
- Documentos individuais de cada empresa do grupo

---

## 3. RELATÓRIO DE AUDITORIA DOCUMENTAL (RAD)

Estrutura do RAD:

```
RELATÓRIO DE AUDITORIA DOCUMENTAL — [NOME DO DEVEDOR]
Data: [data]
Fase: Pré-petição / Instrução / Plano

1. DOCUMENTOS RECEBIDOS E ANALISADOS
   [tabela com status de cada documento]

2. INCONSISTÊNCIAS IDENTIFICADAS
   2.1 [descrição + risco + recomendação]
   2.2 [...]

3. LACUNAS CRÍTICAS (IMPEDEM PROTOCOLO)
   [documentos faltantes que bloqueiam o pedido]

4. LACUNAS SECUNDÁRIAS (RECOMENDAR COMPLEMENTAÇÃO)
   [documentos que fortalecem mas não bloqueiam]

5. ALERTAS DO PERÍODO SUSPEITO
   [atos potencialmente revogáveis identificados]

6. PASSIVOS CONTINGENTES NÃO CONTABILIZADOS
   [estimativa de passivos não refletidos no balanço]

7. PENDÊNCIAS PARA PRÓXIMA FASE
   [ações necessárias antes de prosseguir]
```

---

## 4. CHECKPOINT 2 (parcial)

Ao final da auditoria, sinalize ao advogado:

```
RAD concluído — [X] itens analisados
⛔ BLOQUEADORES: [quantidade] — impedem protocolo imediato
⚠️ ALERTAS: [quantidade] — requerem atenção
✅ CONFORMES: [quantidade]

Recomendação: [ ] Prosseguir  [ ] Aguardar complementação  [ ] Revisar documentos
```
