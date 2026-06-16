---
name: planejamento-prev-pj
description: >
  PLANEJAMENTO PREVIDENCIARIO PJ / SOCIO-EMPRESARIO — Skill Tier 2 F. Analisa e planeja
  a contribuicao previdenciaria para socios de sociedades limitadas, empresarios individuais,
  profissionais liberais com PJ propria, e MEI: otimizacao da contribuicao como CI (pro-labore
  vs distribuicao de lucros), calculo de carencia e TC para aposentadoria, planejamento de
  beneficios (B91/B41/B46), conversao de periodo MEI para contribuicao plena, aliquotas
  facultativo vs CI, e estrategia para maximizar RMI com menor custo contributivo.
  Acionar quando o usuario for socio de PJ, empresario, profissional liberal, MEI, ou
  quando o caso envolver otimizacao de contribuicao previdenciaria para pessoa juridica.
---

# PLANEJAMENTO PREVIDENCIARIO PJ / SOCIO-EMPRESARIO
> Tier 2 — Calculos / Planejamento | CI + MEI + Facultativo | Otimizacao RMI | PA-11

---

## 1. ENQUADRAMENTO DO CONTRIBUINTE PJ

```
SOCIO-ADMINISTRADOR / PRO-LABORE:
  Obrigacao: recolher contribuicao como CI sobre o pro-labore (art. 12, I, f, Lei 8.212)
  Base: pro-labore mensal
  Aliquota: 20% (CI) OU 11% (plano simplificado — so aposta B41 por idade)
  Teto de SC: teto do RGPS vigente

SOCIO NAO-ADMINISTRADOR SEM PRO-LABORE:
  Nao ha obrigacao de contribuicao — pode contribuir como FACULTATIVO
  Base: qualquer valor entre o piso (SM) e o teto (RGPS)
  Aliquota: 20% (facultativo) OU 11% (simplificado — limitado)

MEI (Microempreendedor Individual):
  Aliquota: 5% sobre SM (custo minimo)
  Beneficios disponiveis: aposentadoria por idade, B91, pensao, salario-maternidade
  NAO cobre: aposentadoria especial, B32, aposentadoria por TC com RMI cheia
  PA-11: a RMI do MEI e proporcional (1 SM se sempre recolheu sobre o piso)

AUTONOMO / PRESTADOR DE SERVICO (sem PJ):
  CI classico: 20% sobre a remuneracao recebida
  Pode ser retido na fonte: tomador retém 11% e recolhe GPS
```

---

## 2. OTIMIZACAO DA CONTRIBUICAO

### 2.1 Pro-labore vs Distribuicao de Lucros

```
REGRA GERAL:
  Pro-labore: sujeito ao IRPF progressivo + INSS CI
  Distribuicao de lucros: isenta de IRPF (§ 3o, art. 10, Lei 9.249/95) + sem INSS

ESTRATEGIA OTIMA (simplificada):
  Manter pro-labore no nivel minimo necessario para a contribuicao previdenciaria
  desejada, distribuindo o restante como lucros.

CALCULO DO PRO-LABORE MINIMO PARA APOSENTADORIA:
  → Qual RMI o socio deseja?
  → Qual regra de aposentadoria sera usada (pontos / permanente)?
  → Qual SC medio e necessario para atingir aquela RMI?
  → Pro-labore = SC desejado → contribuicao = pro-labore × 20%

Exemplo:
  Socio quer RMI de R$ 5.000/mes na aposentadoria por pontos
  SB necessario = R$ 5.000 (100% do SB)
  SC medio necessario ao longo dos anos = R$ 5.000
  Pro-labore = R$ 5.000 → INSS CI = R$ 1.000/mes

  Alternativa: pro-labore = R$ 2.000 (SC menor) → RMI futura = R$ 2.000
  Distribuir o restante como lucros: R$ 3.000 → sem INSS + sem IRPF
  Custo INSS: R$ 400/mes (vs R$ 1.000 se tudo fosse pro-labore)
  ESCOLHA: depende do plano de aposentadoria desejado
```

### 2.2 Aliquota 11% vs 20%

```
ALIQUOTA 11% (plano simplificado — IN INSS 128/2022, art. 171):
  Habilitado para: empregado CLT (desconto em folha), CI com renda propria, facultativo
  NAO habilitado: CI que presta servico exclusivamente para PJ (deve ser 20%)
  LIMITACAO CRITICA: so acumula TC para aposentadoria por IDADE (B41/B42)
  NAO permite: aposentadoria por pontos (regras de transicao), aposentadoria especial,
               complementacao com periodos de outras aliquotas para pontos

ALIQUOTA 20% (CI classico):
  Permite: todas as formas de aposentadoria, inclusive por pontos/TC
  Custo maior, mas garante todas as opcoes

ESTRATEGIA:
  Se o socio quer aposentadoria por pontos ou tem TC suficiente → aliquota 20%
  Se o socio so precisa da aposentadoria por idade ou do B91 → 11% e suficiente
```

### 2.3 Conversao de Periodo MEI para CI Pleno

```
O MEI pode complementar a aliquota para 20% retroativamente (ultimos 5 anos)?
  SIM: recolhimento complementar (diferenca entre 5% e 20% + juros/correcao)
  Prazo: 5 anos prescricao (art. 45-B, Lei 8.212)
  Efeito: o periodo converte para 20% e passa a contar para aposentadoria por pontos/TC

Quando vale a pena:
  MEI tem periodos longos e quer usar para aposentadoria por pontos
  Calculo: diferencas retroativas + juros vs ganho na RMI futura — simular
```

---

## 3. SIMULACAO DE PLANEJAMENTO

```
## PLANEJAMENTO PREVIDENCIARIO PJ — [NOME] — [DATA]

**Perfil:** Socio-administrador / MEI / Autonomo
**Empresa:** [nome / CNPJ / atividade]
**Pro-labore atual:** R$ [X.XXX,00] / SC atual: R$ [X.XXX,00]
**TC acumulado ate hoje:** [XX anos XX meses]
**Idade atual:** [XX anos] | **Objetivo de aposentadoria:** [aos XX anos / em X anos]

**Regra de aposentadoria viavel:**
  Pontos: [XX pontos acumulados / faltam X pontos / ano de elegibilidade: XXXX]
  Por idade: [elegivel em XXXX — idade XX anos]
  Especial: [applicavel? Se sim: acionar analise-ppp-ltcat]

**Cenario ATUAL (pro-labore/SC atual):**
  RMI estimada: R$ [X.XXX,00] / mes
  Custo mensal INSS: R$ [XXX,00] / mes
  Custo total ate aposentadoria: R$ [XX.XXX,00]

**Cenario OTIMIZADO (pro-labore ajustado):**
  Pro-labore sugerido: R$ [X.XXX,00] → SC = R$ [X.XXX,00]
  RMI estimada: R$ [X.XXX,00] / mes
  Custo mensal INSS: R$ [XXX,00] / mes
  Economia mensal vs cenario atual: R$ [XXX,00]

**Aliquota recomendada:** 20% / 11% — [fundamento]
**MEI complementar:** recomendar / nao recomendar — [calculo]

**Proximo passo:** [iniciar recolhimento ajustado / complementar retroativos / agendar DER]
```

---

## 4. BENEFICIOS DISPONIVEIS PARA O PJ

```
B91 (auxilio por incapacidade):
  CI: carencia de 12 contribuicoes (0 se acidente)
  MEI: carencia de 12 (idem)
  Importante: manter a qualidade de segurado (nao deixar de recolher)

B41/B42 (aposentadoria por idade):
  CI 20% ou 11%: carencia de 180 contribuicoes + 65 anos (H) / 62 anos (M)
  MEI: idem — RMI calculada sobre SC historico (quase sempre 1 SM se so recolheu 5%)

Pensao por morte / salario-maternidade:
  Dependem da qualidade de segurado na data do evento
  MEI: cobertos desde que qualidade mantida

Aposentadoria especial (B46):
  Para CI com atividade especial: possivel se comprovada a exposicao
  Exige PPP e LTCAT — acionar analise-ppp-ltcat-aposentadoria-especial
```

---

## ALERTAS

```
⚠️ PA-11: MEI com SC de 5% sobre SM = RMI proxima de 1 SM — informar ao cliente antes de recomendar MEI
⚠️ Aliquota 11% bloqueia aposentadoria por pontos — armadilha comum para socios que contribuem 11% por anos
⚠️ Distribuicao de lucros: isencao IRPF e legislacao atual — reforma tributaria em discussao (verificar)
⚠️ Complementacao retroativa MEI: verificar janela de 5 anos — nao e possivel complementar alem do limite
⚠️ Qualidade de segurado: CI que deixa de recolher perde qualidade — orientar continuidade mesmo em meses ruins
```
