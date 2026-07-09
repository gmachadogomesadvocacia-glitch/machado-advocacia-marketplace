---
name: calculos-familia
description: >
  CALCULOS-FAMILIA — Tier 2 (Produção). Realiza cálculos jurídicos especializados em Direito de Família e Sucessões: meação do cônjuge/companheiro, monte-mor e quinhões... Acionar quando o usuário pedir cálculos de partilha, herança, alimentos, tributos de transmissão ou atualização de débito alimentar.
metadata:
  version: "1.0.0"
---

# CALCULOS-FAMILIA
> Tier 2 | Cálculos | Meação / Monte-mor / Alimentos / ITCMD / ITBI / Partilha

---

## 0. AVISO IMPORTANTE

Todos os valores calculados são **estimativas jurídicas** baseadas nos dados fornecidos.
A apuração definitiva depende de avaliação pericial dos bens e da decisão judicial/escritura.
Sinalizar sempre com `[ESTIMATIVA — sujeita a revisão pericial]`.

---

## 1. CÁLCULO DE MEAÇÃO

**Conceito**: Meação é o direito do cônjuge/companheiro sobre os bens comuns —
independente de herança. É calculada antes da partilha hereditária.

**Regra geral**:
```
Monte Partilhável = Total dos bens comuns − Passivos comuns
Meação = Monte Partilhável ÷ 2
```

**Por regime de bens**:

| Regime | Bens que entram na meação |
|--------|--------------------------|
| Comunhão Parcial (art. 1.658 CC) | Bens adquiridos onerosamente na constância |
| Comunhão Universal (art. 1.667 CC) | Todos os bens (presentes e futuros, salvo art. 1.668) |
| Separação Total (art. 1.687 CC) | Nenhum bem — sem meação |
| Participação Final nos Aquestos (art. 1.672 CC) | Aquestos — bens adquiridos na constância |

**Bens excluídos da Comunhão Parcial (art. 1.659 CC)**:
- bens anteriores ao casamento
- bens recebidos por herança ou doação (salvo doação para o casal)
- bens sub-rogados em lugar dos anteriores
- obrigações anteriores ao casamento
- seguros de vida, pensões, proventos do trabalho pessoal

---

## 2. CÁLCULO DO MONTE-MOR E QUINHÕES

**Monte-mor** = valor total do acervo hereditário líquido

```
Monte-mor = Total de bens do falecido − Dívidas do espólio

Se houver cônjuge/companheiro com direito à meação:
  Meação do sobrevivente = Monte-mor × 50%
  Acervo para herança (Monte partível) = Monte-mor × 50%

Quinhão de cada herdeiro = Monte partível ÷ número de herdeiros
  (ajustado conforme testamento, colação e outros fatores)
```

**Exemplo**:
```
Patrimônio total: R$ 600.000,00
Dívidas: R$ 50.000,00
Monte-mor líquido: R$ 550.000,00
Meação da viúva: R$ 275.000,00
Monte partível: R$ 275.000,00
3 filhos → quinhão de cada: R$ 91.666,67
```

---

## 3. LEGÍTIMA E QUOTA DISPONÍVEL

**Base**: art. 1.789 CC — herdeiros necessários têm direito à metade do acervo (legítima)

```
Legítima = Monte-mor ÷ 2   (reservada a herdeiros necessários)
Quota disponível = Monte-mor ÷ 2   (pode ser disposta livremente)

Herdeiros necessários (art. 1.845 CC):
- Descendentes (filhos, netos)
- Ascendentes (pais, avós)
- Cônjuge (art. 1.845 após Lei 10.406/2002)
⚠️ Companheiro: discutido — verificar jurisprudência atual (Tema 809 STF)
```

**⚠️ PA-10**: Testamento que excede a quota disponível é nulo no excesso (art. 1.966 CC).

---

## 4. CÁLCULO DE ALIMENTOS

**Binômio (PA-04)**: Necessidade do alimentando × Possibilidade do alimentante

### 4.1 Por percentual da renda
```
Renda líquida do alimentante = Salário bruto − Impostos − INSS − descontos obrigatórios
Alimentos = Renda líquida × [percentual proposto]

Referências jurisprudenciais (STJ):
- 1 filho: 20-33% da renda líquida (variável conforme necessidade)
- 2 filhos: 30-40%
- Cônjuge sem renda: verificar caso a caso (temporários ou permanentes)
```

### 4.2 Por valor fixo
```
Quando o alimentante é autônomo / informal / sem comprovação de renda:
- Basear em: declaração de IR, estilo de vida, contas, imóveis
- Usar o padrão de vida da família como referência
- Documentar com: contas de restaurante, faturas de cartão, viagens, escola dos filhos
```

### 4.3 Planilha de necessidades do alimentando
```
Item                      Valor mensal estimado
Alimentação               R$ [X]
Moradia (aluguel/condomínio) R$ [X]
Saúde / Plano médico      R$ [X]
Escola / Material         R$ [X]
Transporte                R$ [X]
Vestuário                 R$ [X]
Atividades extracurriculares R$ [X]
Internet / Telefone       R$ [X]
TOTAL NECESSIDADE         R$ [TOTAL]
```

### 4.4 Atualização de débito alimentar
```
Correção: INPC (índice mais comum em alimentos) ou IPCA
Juros: 1% ao mês sobre parcelas em atraso (art. 407 CC)
Multa (prisão civil): 10% sobre o débito (art. 528 CPC — opcional)

Débito total = Σ(parcelas em atraso × INPC) + juros + multa (se aplicável)
```

---

## 5. ITCMD — IMPOSTO DE TRANSMISSÃO CAUSA MORTIS E DOAÇÃO ({{UF}})

**Base**: Lei Estadual de ITCMD do {{UF}} (verificar nº/ano vigente); arts. 35-42 CTN
**Alíquota**: **4%** (PA-13)
**Fato gerador**: transmissão causa mortis (herança) ou inter vivos (doação)
**Base de cálculo**: valor venal / de mercado do bem transmitido (não histórico)

```
ITCMD = Base de cálculo × 4%

Exemplo:
Imóvel avaliado em R$ 400.000,00:
ITCMD = R$ 400.000 × 4% = R$ 16.000,00

⚠️ Isenções no {{UF}}: verificar se herdeiro mora no imóvel e se é o único bem do espólio
   (isenções da lei estadual de ITCMD — arts. e limites a confirmar com a SEFAZ/{{UF}})
```

**Prazo**: guia a ser gerada no portal da SEFAZ/{{UF}} (portal da Fazenda estadual)
antes de lavrar a escritura ou homologar a partilha.

---

## 6. ITBI — IMPOSTO DE TRANSMISSÃO DE BENS IMÓVEIS ({{CIDADE}})

**Base**: art. 156, II, CF; Lei Municipal de {{CIDADE}}
**Fato gerador**: transmissão inter vivos onerosa de bem imóvel (compra, dação em pagamento)
**⚠️ PA-14**: Não incide no inventário (transmissão causa mortis → ITCMD) nem em meação
   (não é transmissão — é partilha de patrimônio comum)

```
Verificar alíquota vigente junto à Prefeitura de {{CIDADE}}
(geralmente 2% ou 3% sobre o valor de transmissão)

ITBI = Valor de transmissão × alíquota municipal
```

---

## 7. PARTILHA DE BENS — MODELO DE PLANILHA

```
PLANILHA DE PARTILHA — [NOME DO CASO]
Regime: [comunhão parcial / universal / etc.]

BENS COMUNS:
| Bem | Descrição | Valor | Para quem fica |
|-----|-----------|-------|---------------|
| Imóvel (mat. XXXX) | Casa Rua X | R$ 400.000 | Cliente |
| Veículo (XXXX-XXXX) | Fiat | R$ 45.000 | Contraparte |
| Investimentos XP | Conta XXXX | R$ 80.000 | Dividir 50/50 |
| TOTAL COMUM | | R$ 525.000 | |

PASSIVOS COMUNS:
| Dívida | Credor | Valor | Responsável |
| Financiamento imóvel | Banco X | R$ 120.000 | Cliente (assume) |
| TOTAL PASSIVO | | R$ 120.000 | |

MONTE PARTILHÁVEL LÍQUIDO: R$ 405.000
MEAÇÃO CLIENTE: R$ 202.500
MEAÇÃO CONTRAPARTE: R$ 202.500

TORNAS/COMPENSAÇÕES:
[se um cônjuge fica com mais bens do que sua meação, paga tornas ao outro]
```

---

## 7-A. EXEMPLO RESOLVIDO — ALIMENTOS + PARTILHA (números concretos)

**Cenário**: casal em comunhão parcial. Alimentante (pai) é assalariado; 1 filho menor.
Dissolução com partilha. Dados fornecidos pelo cliente.

### (a) Alimentos — percentual sobre rendimentos LÍQUIDOS (binômio PA-04)

```
Salário bruto do alimentante ........... R$ 6.000,00
(−) INSS ............................... R$   600,00
(−) IRRF ............................... R$   300,00
(=) RENDA LÍQUIDA ...................... R$ 5.100,00

Necessidade do filho (planilha §4.3) ... R$ 1.700,00/mês
Possibilidade: renda líquida R$ 5.100,00 comporta o encargo.

Percentual pleiteado: 30% da renda líquida
Alimentos = R$ 5.100,00 × 30% = R$ 1.530,00/mês
```
Resultado: **R$ 1.530,00/mês (30% do líquido)** — cobre ~90% da necessidade
declarada e preserva a subsistência do alimentante. [ESTIMATIVA — ajustar à prova]

### (b) Partilha — meação na COMUNHÃO PARCIAL (só os aquestos)

Regra: partilham-se apenas os bens COMUNS (adquiridos onerosamente na constância —
art. 1.658 CC). Excluem-se os anteriores e os havidos por herança/doação (art. 1.659 CC).

```
BENS DO CASAL                              Valor        Comum?
Apartamento comprado na constância ..... R$ 400.000   SIM (aquesto)
Carro comprado na constância ........... R$  50.000   SIM (aquesto)
Sítio herdado pelo marido .............. R$ 300.000   NÃO (herança — art. 1.659, I)
Poupança da esposa (anterior à união) .. R$  20.000   NÃO (anterior)

MASSA PARTÍVEL (só os comuns) = 400.000 + 50.000 = R$ 450.000
(−) Saldo do financiamento do apto (dívida comum) ..... R$  90.000
(=) MONTE PARTÍVEL LÍQUIDO ............................ R$ 360.000

Meação de cada cônjuge = 360.000 ÷ 2 = R$ 180.000
```
O sítio (R$ 300.000) e a poupança (R$ 20.000) NÃO entram — ficam, respectivamente,
com marido e esposa, fora da partilha. Cada um leva **R$ 180.000** dos aquestos;
se um ficar com o apartamento (valor > sua meação), paga **tornas** ao outro.
[ESTIMATIVA — sujeita a avaliação pericial dos bens]

---

## 8. SAÍDA DA SKILL

Apresentar:
1. Tabela de cálculo com valores e memória de cálculo
2. Indicação de `[ESTIMATIVA]` onde necessário
3. Alertas sobre tributos (ITCMD, ITBI)
4. Sugestão de quinhões se for inventário
5. Encaminhar para revisao-final-familia se integrar peça processual
