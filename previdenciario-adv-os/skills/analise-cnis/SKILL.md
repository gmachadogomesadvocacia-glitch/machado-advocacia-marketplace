---
name: analise-cnis
description: >
  ANALISE DE CNIS — Skill Tier 2 C. Le e analisa Cadastro Nacional de Informacoes Sociais
  (CNIS): identifica vinculos empregaticios, periodos de contribuicao como CI/MEI, gaps,
  salarios-de-contribuicao por competencia, DER potencial, tempo total de contribuicao
  valido, carencia acumulada, qualidade de segurado, e periodos de beneficio. Detecta
  inconsistencias (vinculos sem salario, recolhimentos abaixo do piso, periodos rurais
  nao registrados). Acionar sempre que um CNIS for disponibilizado para analise ou quando
  o caso envolver discussao sobre tempo de contribuicao, carencia ou DER.
---

# ANALISE DE CNIS
> Tier 2 — Analise | Cadastro Nacional de Informacoes Sociais | Auditoria Completa

---

## 1. LEITURA ESTRUTURADA DO CNIS

### 1.1 Tipos de Registro no CNIS

```
VINCULO — Empregado CLT: registrado com CNPJ do empregador, data de admissao e demissao
RECOLHIMENTO — Contribuinte Individual: GPS ou DARF com base e data de pagamento
BENEFICIO — Codigo do beneficio + DIB + DCB: computa como tempo e carencia (em alguns casos)
VINCULO SEM SALARIO — sinal de alerta: vinculo registrado mas SC zerado ou abaixo do piso
RECOLHIMENTO CI SEM NF — sinal de alerta: CI recolheu mas nao ha NFS-e correspondente
```

### 1.2 Calculo do Tempo de Contribuicao

```
Para cada vinculo/recolhimento valido:
1. Verificar se a competencia esta dentro do periodo de filiacao (a partir da 1a contribuicao)
2. Verificar se o SC esta entre o piso (SM) e o teto (verificar tabela historica)
3. Computar: cada competencia valida = 1 mes de TC
4. Periodos de beneficio que computam: auxilio-doenca, acidente (computa TC e carencia)
5. Periodos que NAO computam TC: desemprego (sem contribuicao), periodo de graca

Resultado: X anos Y meses de TC (arredondar sempre para baixo — meses exatos)
```

### 1.3 Calculo da Carencia

```
Carencia e o numero minimo de contribuicoes mensais (nao e o mesmo que TC)
Diferenca pratica:
- Segurado especial rural: carencia sem recolhimento (atividade comprovada)
- Contribuinte individual: so conta se SC foi efetivamente recolhido

Minimos por beneficio:
- Aposentadoria por idade (EC 103): 180 contribuicoes
- Aposentadoria especial: 180 contribuicoes
- Auxilio por incapacidade: 12 contribuicoes (0 se acidente)
- Pensao por morte: 0 (basta qualidade de segurado)
```

---

## 2. IDENTIFICACAO DE GAPS E INCONSISTENCIAS

```
GAPS — periodos sem contribuicao:
□ Sao intencionais ou erro de registro?
□ Impactam a qualidade de segurado? (verificar periodo de graca)
□ Precisam ser complementados? (CI pode recolher retroativamente com NF — limite: 5 anos)

VINCULOS SEM SALARIO:
□ Empregador pode ter deixado de recolher INSS — responsabilidade do empregador (art. 33)
□ Segurado pode reclamar o credito mesmo sem SC no CNIS
□ Requerer ao INSS o computo do vinculo sem recolhimento (art. 45-A, Lei 8.213)

RECOLHIMENTOS ABAIXO DO PISO:
□ Qualquer SC < piso (SM) da competencia: nao computa corretamente
□ MEI: SC de 5% sobre SM — conta apenas para beneficios especificos (PA-11)

PERIODOS RURAIS NAO REGISTRADOS:
□ Rural nao tem registro formal no CNIS em periodos antigos
□ Provar com inicio de prova material + TNU Sumula 6
□ Solicitar ao INSS o reconhecimento do periodo

PERIODOS DE BENEFICIO NO CNIS:
□ B91/B94: computa carencia + TC durante o beneficio
□ B31/B32: computa carencia + TC
□ Verificar se os periodos de beneficio estao incluidos no total
```

---

## 3. OTIMIZACAO DA DER

```
DER (Data de Entrada do Requerimento) = data em que o segurado pede o beneficio
DIB = data que o INSS fixa para inicio dos pagamentos (normalmente = DER)

Estrategia:
1. O segurado ja cumpriu os requisitos? → DER IMEDIATA (nao perder retroativos)
2. Esta proximo de cumprir? → calcular quando sera o melhor momento (maior RMI)
3. Ha regra de transicao prestes a ser mais favoravel? → aguardar ou antecipar

Armadilha comum: aguardar "mais um pouco" pode ser desvantajoso se o fator
previdenciario ou a aliquota da regra de transicao estiver diminuindo com o tempo.
Acionar calculos-previdenciarios para simular.
```

---

## 4. SAIDA DA ANALISE DE CNIS

```
## ANALISE DE CNIS — [NOME] — [DATA DE EXTRACAO]

**Tempo de Contribuicao Total Valido:** XX anos XX meses
**Carencia Acumulada:** XXX competencias
**Qualidade de Segurado:** Mantida / Perdida / Periodo de graca ate [data]
**DER Otima Calculada:** [data — se ja cumpriu requisitos]

**Vinculos/Periodos Validos:** [resumo por periodo e categoria]
**Gaps Identificados:** [lista com datas e impacto]
**Inconsistencias:** [lista com recomendacao]
**Periodos Rurais Nao Registrados:** [se houver — documentacao necessaria]

**Tempo Faltante para [regra mais favoravel]:** [X anos Y meses]
**Recomendacao:** [acionar calculos-previdenciarios para simulacao de RMI]
```
