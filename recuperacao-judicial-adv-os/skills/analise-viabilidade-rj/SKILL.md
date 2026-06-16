---
name: analise-viabilidade-rj
description: >
  ANALISE-VIABILIDADE-RJ — Tier 1 (Insumo Estratégico). Elabora ou analisa o laudo de viabilidade
  econômico-financeira exigido pelo art. 53, II da LFRJ como fundamento do plano de recuperação.
  Avalia fluxo de caixa projetado, EBITDA, índices de endividamento, capacidade de pagamento,
  e sustentabilidade do negócio. Acionar quando o usuário precisar construir o argumento de
  viabilidade para o plano, contestar laudo apresentado pelo AJ ou credor, ou avaliar se
  a recuperação é economicamente justificável antes de peticionar.
---

# ANALISE-VIABILIDADE-RJ
> Tier 1 | Viabilidade Econômico-Financeira | Art. 53, II LFRJ | Laudo + Projeções

---

## 0. ESCOPO

Produz ou analisa laudo de viabilidade econômico-financeira. Opera com os dados fornecidos pelo
cliente ou presentes no CASO.md. Quando os dados forem insuficientes, sinaliza lacunas e solicita
complementação. Produz: Laudo de Viabilidade (LV) ou Análise Crítica de Laudo Externo.

⚠️ **PA-05**: Nenhum plano de recuperação pode ser apresentado sem demonstrar viabilidade.

---

## 1. POSIÇÃO NA ORQUESTRA

```
triagem-rj + auditoria-documental-rj
        ↓
[analise-viabilidade-rj]  ←─ Tier 1
        ↓
  CHECKPOINT 2 (completo)
        ↓
  plano-recuperacao-rj
```

---

## 2. METODOLOGIA DE ANÁLISE

### 2.1 Diagnóstico da Crise

Identificar a natureza da crise empresarial:

| Tipo de crise | Indicadores | Reversibilidade |
|---------------|-------------|-----------------|
| **Crise de liquidez** | Fluxo de caixa negativo temporário, dívida de curto prazo | Alta |
| **Crise de solvência** | PL negativo, dívida > capacidade de geração | Média |
| **Crise operacional** | EBITDA negativo, perda de market share | Baixa/Média |
| **Crise estrutural** | Modelo de negócio obsoleto | Baixa |
| **Crise conjuntural** | Externa (pandemia, câmbio, regulação) | Alta |

A natureza da crise define a viabilidade e molda o plano de recuperação.

### 2.2 Indicadores Financeiros Chave

Calcular com base nas demonstrações fornecidas:

**Liquidez:**
- Liquidez corrente = AC / PC (saudável: > 1,0)
- Liquidez imediata = Disponível / PC
- Necessidade de Capital de Giro (NCG) = (AC operacional - PC operacional)

**Endividamento:**
- Dívida líquida / EBITDA (benchmark: < 3,5x para setores maduros)
- Grau de endividamento = PT / PL
- Cobertura de juros = EBITDA / Despesas financeiras (saudável: > 2,0)

**Rentabilidade:**
- Margem EBITDA = EBITDA / Receita líquida
- ROIC = NOPAT / Capital investido
- Breakeven operacional (ponto de equilíbrio)

### 2.3 Projeção de Fluxo de Caixa

Elaborar ou validar projeção para o período do plano (mínimo 3 anos):

```
FCO (Fluxo de Caixa Operacional)
= EBITDA
- Variação do Capital de Giro
- CAPEX de manutenção
- Impostos sobre o resultado operacional

FCL (Fluxo de Caixa Livre)
= FCO - CAPEX de crescimento

Capacidade de pagamento da dívida reestruturada
= FCL disponível após operações essenciais
```

Premissas a documentar obrigatoriamente:
- Taxa de crescimento de receita (com justificativa de mercado)
- Evolução de margens (benchmarks do setor)
- Variação de preços de insumos
- Necessidade de investimento (CAPEX)

### 2.4 Análise de Sensibilidade

Elaborar três cenários:

| Cenário | Premissa de receita | Resultado esperado |
|---------|--------------------|--------------------|
| **Base** | Crescimento conservador | Viabilidade demonstrada |
| **Pessimista** | Queda de [X]% | Capacidade de pagamento mínima |
| **Otimista** | Crescimento acelerado | Pagamento antecipado |

O cenário pessimista deve ainda demonstrar capacidade de honrar o plano (fundamento da viabilidade).

### 2.5 Fundamentos Qualitativos

Além dos números, o laudo deve demonstrar:
- Posição competitiva da empresa no mercado
- Base de clientes e contratos relevantes
- Ativos estratégicos (tecnologia, marca, licenças, infraestrutura)
- Plano operacional de reestruturação (corte de custos, desinvestimento)
- Gestão: qualidade do management, plano de turnaround
- Suporte de sócios/investidores (aporte de capital previsto)

---

## 3. ESTRUTURA DO LAUDO DE VIABILIDADE

```
LAUDO DE VIABILIDADE ECONÔMICO-FINANCEIRA
[NOME DO DEVEDOR] | Processo nº [...]

1. OBJETO E METODOLOGIA
2. DIAGNÓSTICO DA CRISE
   2.1 Natureza e causas
   2.2 Indicadores financeiros históricos
3. ANÁLISE DE VIABILIDADE
   3.1 Premissas do plano operacional
   3.2 Projeção de fluxo de caixa (3-5 anos)
   3.3 Capacidade de pagamento da dívida reestruturada
   3.4 Análise de sensibilidade (3 cenários)
4. FUNDAMENTOS QUALITATIVOS
   4.1 Posição de mercado
   4.2 Ativos estratégicos
   4.3 Plano de reestruturação operacional
5. CONCLUSÃO DE VIABILIDADE
   "A empresa [NOME] demonstra viabilidade econômico-financeira para
    cumprimento do plano de recuperação judicial apresentado, sendo
    a preservação da empresa e dos empregos a alternativa superior
    à falência, nos termos do art. 47 da L11.101/2005."
6. RESSALVAS E CONDICIONANTES
```

---

## 4. ANÁLISE CRÍTICA DE LAUDO EXTERNO

Quando o usuário apresentar laudo elaborado pelo AJ ou por perito adversário, verificar:

- Premissas de receita: são realistas? Comparar com histórico e benchmarks setoriais
- Taxa de desconto utilizada: WACC calculado corretamente?
- Período de projeção: adequado à natureza do negócio?
- Tratamento de contingências: passivos ocultos foram considerados?
- Independência do laudo: conflito de interesse do elaborador?
- Dados de base: consistentes com as demonstrações do art. 51?

Pontos de impugnação mais comuns:
1. Projeções irrealisticamente pessimistas (quando o AJ recomenda falência)
2. Desconsideração de ativos intangíveis relevantes
3. Ausência de cenários alternativos
4. Comparação com empresas de setores diferentes
