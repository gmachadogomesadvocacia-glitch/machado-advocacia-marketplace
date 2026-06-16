---
name: analise-documental-familia
description: >
  ANALISE-DOCUMENTAL-FAMILIA — Tier 1 (Insumos). Analisa e interpreta documentos em casos de
  família e sucessões: certidões civis (casamento, nascimento, óbito), matrículas de imóveis,
  escrituras, testamentos, contratos de convivência, declarações de IR, holerites, extratos
  bancários, laudos médicos e psicológicos, estudos psicossociais, e contratos sociais.
  Identifica inconsistências, patrimônio oculto e riscos. Acionar quando o usuário fornecer
  documentos para análise ou quando precisar saber quais documentos são necessários para um caso.
metadata:
  version: "1.0.0"
---

# ANALISE-DOCUMENTAL-FAMILIA
> Tier 1 | Insumos | Análise de Certidões / Matrículas / Laudos / IR / Extratos

---

## 0. ESCOPO

Analisa documentos de dois ângulos:
1. **Diagnóstico**: o que o documento diz e o que implica para o caso
2. **Auditoria**: identificar inconsistências, omissões e indícios de patrimônio oculto

> **PDFs de processo:** no Code, converter com `ferramentas/pdf-para-md/` antes de analisar.

---

## 1. CERTIDÃO DE CASAMENTO

**O que verificar**:
```
□ Data exata do casamento (define início da comunhão — PA-03)
□ Regime de bens declarado na certidão
   → Comunhão parcial (padrão — art. 1.640 CC)
   → Comunhão universal / separação / participação (requer pacto antenupcial)
□ Pacto antenupcial registrado? (averbação na certidão)
□ Averbações posteriores (separação, divórcio)
□ Nomes das testemunhas e cartório (para eventual irregularidade)
```

---

## 2. CERTIDÃO DE NASCIMENTO DOS FILHOS

```
□ Nome dos pais — pai reconheceu (espontâneo ou judicial)?
□ Data de nascimento (para cálculo de maioridade — alimentos)
□ Averbações (adoção, reconhecimento posterior de paternidade)
□ Há filhos de outros relacionamentos não declarados?
```

---

## 3. CERTIDÃO DE ÓBITO

```
□ Data e local do óbito
□ Estado civil declarado (verificar consistência com a certidão de casamento)
□ Causa do óbito (relevante se há suspeita de incapacidade prévia — testamento)
□ Registro em cartório (município) → inventário no último domicílio (art. 48 CPC)
□ Declaração de Óbito (D.O.) — nome do médico declarante
```

---

## 4. MATRÍCULA DE IMÓVEL (Certidão do CRI)

```
□ Número da matrícula e cartório
□ Proprietário(s) atual(is) e forma de aquisição
□ Data de aquisição (verificar se foi antes ou durante o casamento/união — PA-07)
□ Forma de aquisição: compra, doação, herança (define se entra na comunhão)
□ Ônus e gravames:
   → Hipoteca? Valor e credor?
   → Penhora? Qual processo?
   → Alienação Fiduciária? Saldo devedor?
   → Usufruto? Em favor de quem? Vitalício?
   → Cláusulas de inalienabilidade, impenhorabilidade?
□ Área, localização, confrontações
□ Histórico de transmissões (cadeia dominial) — verificar regularidade
```

---

## 5. DECLARAÇÃO DE IR (IRPF)

**O que buscar**:
```
□ Renda bruta declarada (salários, aluguéis, CNPJ)
□ Bens declarados:
   → Imóveis (comparar com matrículas apresentadas — algum foi omitido?)
   → Veículos (comparar com CRLVs)
   → Investimentos (CDB, ações, fundos, LCI, LCA)
   → Participações societárias
   → Empréstimos concedidos
□ Dependentes declarados (filhos, cônjuge/companheiro)
□ Dívidas declaradas
□ Comparar os últimos 2-3 anos: houve variação de patrimônio suspeita?
```

**Sinais de patrimônio oculto**:
- Renda declarada baixa com padrão de vida alto (carro importado, viagens internacionais)
- Queda súbita de patrimônio próximo à separação (venda abaixo do mercado, doação a parentes)
- Empresa com lucros que "desaparecem" antes do inventário
- Investimentos zerados antes do inventário ou divórcio

---

## 6. HOLERITES E COMPROVANTES DE RENDA

```
□ Salário bruto × líquido (verificar descontos)
□ Benefícios: vale-alimentação, convênio médico, PLR, bônus
□ INSS e IR retido na fonte
□ Empregador (verificar inconsistências com o CNPJ declarado)
□ Comparar com a declaração de IR
□ Para autônomos / MEI: verificar notas fiscais e faturamento
```

---

## 7. LAUDO PSICOLÓGICO / ESTUDO PSICOSSOCIAL

**Em casos de guarda**:
```
□ Quem realizou? (CRAS, assistente social judicial, perito privado)
□ Qual é a recomendação sobre guarda?
□ O laudo analisou ambos os pais e a criança?
□ Há indícios de alienação parental no laudo?
□ O laudo tem data recente? (mais de 1 ano: solicitar novo)
□ Há recomendação de acompanhamento psicológico?
```

**Em interdição**:
```
□ CID do laudo médico
□ O médico é especialista na área (psiquiatra, neurologista)?
□ O laudo afirma incapacidade TOTAL ou parcial?
□ Há prontuário hospitalar / receitas médicas que corroboram?
□ TDA seria adequada? O laudo descarta esta alternativa?
```

---

## 8. TESTAMENTO

```
□ Tipo: público (tabelionato) / particular (3 testemunhas) / cerrado?
□ Data de lavratura — testador tinha capacidade plena na época?
□ Disposições: dentro da quota disponível (50%)?
□ Legítima preservada (50% para herdeiros necessários)?
□ Cláusulas restritivas: inalienabilidade, impenhorabilidade?
□ Testamenteiro nomeado?
□ Há revogação de testamento anterior?
□ Há cópia no Cadastro Nacional de Testamentos (CNT — CFN)?
□ Registro em cartório de registro de imóveis (se houver legado de imóvel)?
```

---

## 9. CONTRATO SOCIAL DE EMPRESA

**Para calcular patrimônio do cliente ou da contraparte**:
```
□ Capital social e % de participação do cônjuge/companheiro
□ Cláusula de transmissão de cotas (heranças, saída de sócio)
□ Pró-labore declarado (base para cálculo de alimentos)
□ Distribuição de lucros nos últimos 3 anos (IRPJ / SIMPLES)
□ Bens integralizados no capital
□ Cláusula de inegociabilidade de cotas (se houver)
□ Contabilidade (balanço, DRE) — se disponível
```

---

## 10. SAÍDA DA SKILL: RELATÓRIO DE ANÁLISE DOCUMENTAL (RAD)

Após analisar os documentos, emitir um RAD estruturado:

```
RELATÓRIO DE ANÁLISE DOCUMENTAL — [CASO]

1. DOCUMENTOS ANALISADOS: [lista]
2. PATRIMÔNIO MAPEADO: [tabela de bens]
3. INCONSISTÊNCIAS IDENTIFICADAS: [lista com destaque]
4. DOCUMENTOS FALTANTES: [lista com prioridade]
5. ALERTAS: [riscos, fraudes suspeitas, prazos]
6. RECOMENDAÇÕES: [próximos passos]
```

Encaminhar para **memoria-de-caso-familia** e atualizar o CASO.md.
