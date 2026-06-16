---
name: calculos-previdenciarios
description: >
  CALCULOS PREVIDENCIARIOS — Skill Tier 2 C. Consolida tres modalidades de calculo:
  (1) RMI — Renda Mensal Inicial: PBC, SB, fator previdenciario, aliquotas EC 103,
  regras de transicao (pontos progressivos, por idade, por tempo + reducao, pedagio);
  (2) RMA — Reajuste / Manutencao de Beneficio: INPC acumulado, teto historico;
  (3) Calculo do SB pela Regra da Vida Toda (art. 29, II). Protocolo P5 obrigatorio
  (memorial comparativo antes/depois). Auto-ataque: verificar se outra regra gera RMI
  maior. Acionar sempre que houver calculo de beneficio, simulacao de aposentadoria,
  ou contestacao de valor calculado pelo INSS.
---

# CALCULOS PREVIDENCIARIOS
> Tier 2 — Calculos | RMI + RMA + Fator | Protocolo P5 | Auto-ataque obrigatorio

---

## 0. PROTOCOLO P5 — MEMORIAL COMPARATIVO (OBRIGATORIO)

Sempre que calcular RMI, apresentar ao menos duas regras comparadas.
Nunca entregar apenas o calculo da regra aplicada pelo INSS — verificar se existe
regra mais favoravel (auto-ataque). Isso e obrigacao do advogado previdenciario.

---

## 1. CALCULO DA RMI — REGRAS EC 103/2019

### 1.1 Regra Permanente (pos-EC 103, filiados apos 13/11/2019)

```
PBC (Periodo de Base de Calculo): todos os salarios-de-contribuicao desde julho/1994
SB (Salario de Beneficio): media aritmetica simples de 100% dos SCs do PBC
Aliquota:
  Mulher: 60% + 2% por ano acima de 15 anos de contribuicao
  Homem:  60% + 2% por ano acima de 20 anos de contribuicao
  Limite: 100% do SB
  OBS: 100% apenas com 35 anos (H) / 30 anos (M) minimos de contribuicao

RMI = SB × aliquota

Piso: salario minimo vigente
Teto: teto do RGPS vigente (verificar tabela historica)
```

### 1.2 Regras de Transicao EC 103 (para filiados antes de 13/11/2019)

```
REGRA 1 — PONTOS PROGRESSIVOS (mais comum para homens com muito TC)
  Homem: 96+2 por ano ate atingir 105 pontos (1 ponto/ano)
          → 2026: 102 pontos; 2027: 103; ... 2033 em diante: 105 (permanente)
  Mulher: 86+2 por ano ate atingir 100 pontos
          Minimo: 30 anos (M) / 35 anos (H) de TC + pontos atingidos
  RMI: 100% do SB (sem reducao pela aliquota)
  SB: media dos 100% melhores SCs
  Vantagem: nao tem fator previdenciario, nao tem reducao de aliquota

REGRA 2 — IDADE PROGRESSIVA (para quem nao tem TC suficiente)
  Homem: 65 anos + TC minimo (15 anos ou carencia 180)
  Mulher: 62 anos (atingido em 2023) + TC minimo
  RMI: 60% + 2%/ano acima do TC minimo
  Observacao: esta regra e praticamente a regra permanente para segurados com filiacao antiga

REGRA 3 — PEDAGIO 50% (para quem estava proximo em 13/11/2019)
  Condicao: faltavam ate 2 anos de TC em 13/11/2019
  RMI: 100% do SB
  Requisito adicional: pagar 50% a mais do que faltava

REGRA 4 — PEDAGIO 100% (para aposentadoria por TC puro)
  Condicao: nao atingiu os pontos progressivos
  Requisito: TC minimo (35H / 30M) + pedagio de 100% do tempo faltante
  RMI: 100% do SB
  OBS: esta regra e desvantajosa para quem pode usar Pontos — comparar sempre

REGRA 5 — REGRA ANTERIOR A EC 103 (art. 3, EC 103 — direito adquirido)
  Para quem tinha direito adquirido antes de 13/11/2019
  Manter calculo anterior com fator previdenciario (se mais favoravel)
```

### 1.3 Fator Previdenciario (regras pre-EC 103 / beneficios antigos)

```
Fp = (Tc × a / Es) × [1 + (Id + Tc × a) / 100]

Onde:
  Tc = tempo de contribuicao em anos
  a  = aliquota de contribuicao (0,31)
  Es = expectativa de sobrevida na data da aposentadoria (tabela IBGE)
  Id = idade do segurado na DER

Quando se aplica hoje:
- Revisao de beneficio concedido antes da EC 103 com fator
- Acao revisional para verificar se fator foi aplicado corretamente
- Acionar acao-revisional-rmi para correcao
```

---

## 2. CALCULO DO SALARIO DE BENEFICIO — VIDA TODA

```
Regra normal (art. 29, I): media dos 80% maiores SCs desde julho/1994
Regra da vida toda (art. 29, II): media de todos os SCs desde a filiacao ao RGPS

Quando usar art. 29, II:
□ O segurado tem SCs anteriores a julho/1994?
□ Os SCs pre-94 corrigidos (INPC) sao maiores que os pos-94?
□ O SB pela RVT supera o SB pelo PBC normal?

Se SIM para todos: RVT e mais favoravel — Tema 1102 STF (RE 1.276.977) / Tema 999 STJ (REsp 1.596.203)
Acionar acao-revisional-rmi para protocolar a acao
```

---

## 3. REAJUSTE DE BENEFICIO (RMA) — INPC

```
Os beneficios em manutencao sao reajustados anualmente pelo INPC (art. 41-A Lei 8.213)
Periodo: 1o de janeiro de cada ano (decreto anual)

Verificar:
□ O INSS aplicou o indice correto na competencia do reajuste?
□ Ha atraso no pagamento de diferenca de reajuste?
□ O beneficio esta abaixo do piso (SM) pos-reajuste?

Calculo de diferencas:
RMI x (produto dos indices INPC) = valor correto atual
Diferenca = valor correto - valor pago (por mes, desde o erro)
Prescricao das parcelas: ultimos 5 anos (art. 103-A Lei 8.213)
```

---

## 4. SIMULACAO — TABELA DE REGRAS

```
## SIMULACAO DE RMI — [NOME] — DER [DATA]

**Dados basicos:**
  Sexo: [M/F] | Nascimento: [data] | Idade na DER: [XX anos]
  TC total: [XX anos XX meses] | TC especial (convertido): [XX anos XX meses]
  Carencia: [XXX competencias]
  SC medio dos 100% melhores (SB base): R$ [X.XXX,XX]

**REGRA 1 — Pontos Progressivos (2026: 102 pontos):**
  Pontos atingidos? [SIM/NAO] — pontos atuais: [XX]
  RMI: 100% × R$ [SB] = R$ [X.XXX,XX]
  ✓/✗ elegivel

**REGRA 2 — Idade Progressiva:**
  Idade minima (2026): [62F/65H] — [atingida/nao atingida]
  Aliquota: 60% + 2% × [anos acima do minimo] = [XX]%
  RMI: [XX]% × R$ [SB] = R$ [X.XXX,XX]
  ✓/✗ elegivel

**REGRA 3 — Pedagio 50%:**
  Faltavam ate 2 anos em 13/11/2019? [SIM/NAO]
  RMI: 100% × R$ [SB] = R$ [X.XXX,XX]
  ✓/✗ elegivel

**REGRA FAVORAVEL:** [indicar qual] = R$ [X.XXX,XX]
**Diferenca em relacao ao menor calculo:** R$ [X.XXX,XX]/mes

**Observacoes PA-12:** [alertar se algum dado incerto — auto-ataque concluido]
```

---

## ALERTAS

```
⚠️ PA-12: nao apresentar calculo sem memorial comparativo (Protocolo P5 obrigatorio)
⚠️ PA-22: Tema 1102 STF / Tema 999 STJ (RVT) — analise individual obrigatoria — nao recomendar em escala
⚠️ PA-03: verificar decadencia (10 anos) antes de revisar RMI concedida
⚠️ Teto historico: verificar se o SB calculado supera o teto da competencia da DIB
⚠️ MEI: SC de 5% sobre SM — para RMI: so computa beneficios de baixo valor (PA-11)
```
