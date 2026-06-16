---
name: analise-carta-concessao-indeferimento
description: >
  ANALISE DE CARTA DE CONCESSAO / INDEFERIMENTO — Skill Tier 2 C. Le e interpreta cartas
  de concessao de beneficio (verifica DIB, RMI, especie concedida, regra de transicao
  aplicada, tempo de contribuicao computado) e cartas de indeferimento (identifica fundamento
  legal do INSS, carencia negada, tempo insuficiente, qualidade de segurado perdida, alta
  medica indevida, DII posterior a DER). Emite diagnostico com pontos de impugnacao.
  Acionar sempre que o usuario apresentar uma carta do INSS — seja concessao ou indeferimento.
---

# ANALISE DE CARTA DE CONCESSAO / INDEFERIMENTO
> Tier 2 — Analise | Concessao + Indeferimento | Diagnostico + Pontos de Impugnacao

---

## 1. ANALISE DE CARTA DE CONCESSAO

### 1.1 Checklist de Concessao

```
□ Especie concedida (B-code) e a correta para a patologia/situacao do segurado?
□ DIB (Data de Inicio do Beneficio) = DER? Se DIB posterior a DER: ha retroativos perdidos
□ RMI calculada esta correta? (acionar calculos-previdenciarios para conferencia)
□ Regra de transicao aplicada e a mais favoravel? (EC 103 — verificar todas as regras)
□ Tempo de contribuicao computado esta completo? (conferir com CNIS — acionar analise-cnis)
□ Periodos especiais reconhecidos (se aplicavel)? (acionar analise-ppp-ltcat se B46)
□ Acrescimo de 25% concedido se havia indicacao de assistencia permanente? (art. 45 Lei 8.213)
□ Houve cumulacao indevida de beneficio? (B91 + salario = possivel, B31/B32 + salario = verificar)
```

### 1.2 Erros Comuns em Cartas de Concessao

```
ERRO 1 — DIB posterior a DER:
  Causa: INSS atrasou a pericia ou a analise; DER estava correta mas DIB foi fixada depois
  Impacto: retroativos perdidos entre DER e DIB
  Medida: impugnar administrativamente (art. 41-A, Lei 8.213) ou acao de revisao

ERRO 2 — RMI calculada errada:
  Causa: INSS aplicou regra permanente EC 103 em vez de regra de transicao mais favoravel
  Medida: acionar acao-revisional-rmi — verificar decadencia (10 anos)

ERRO 3 — Especie errada:
  Ex: INSS concedeu B91 (temporario) quando o caso era B32 (permanente/sequela)
  Impacto: beneficio cessara indevidamente no prazo fixado
  Medida: recurso ao JR (CRPS) — 30 dias da ciencia

ERRO 4 — Periodos nao computados:
  Causa: vinculo sem salario no CNIS, periodo rural nao registrado, competencia contestada
  Medida: impugnar administrativamente ou acao de reconhecimento de tempo

ERRO 5 — Acrescimo 25% nao aplicado:
  Verificar se laudo pericial indicou necessidade de assistencia permanente (art. 45)
  Medida: recurso administrativo ou acao de revisao
```

---

## 2. ANALISE DE CARTA DE INDEFERIMENTO

### 2.1 Fundamentos Tipicos de Indeferimento

```
FUNDAMENTO A — Carencia insuficiente
  O que verificar:
  □ O INSS computou corretamente todas as competencias validas do CNIS?
  □ Ha periodos de beneficio (B91/B94) que computam carencia?
  □ Ha qualidade de segurado especial rural que nao exige recolhimento?
  □ Ha vinculo sem salario que deve ser computado (art. 45-A Lei 8.213)?
  □ Para acidente (B91 com nexo): carencia = ZERO — INSS errou?

FUNDAMENTO B — Qualidade de segurado perdida
  O que verificar:
  □ Quando foi a ultima contribuicao ou fim do vinculo?
  □ Qual era o periodo de graca aplicavel? (art. 15 Lei 8.213)
     - 12 meses (geral)
     - 24 meses (se >120 contrib. ou desempregado comprovado)
     - 36 meses (se desempregado com CTPS anotada)
  □ Ha beneficio por incapacidade que manteve a qualidade de segurado?

FUNDAMENTO C — Incapacidade nao reconhecida (alta medica)
  O que verificar:
  □ A pericia foi realizada ou o INSS indeferiu sem pericia?
  □ Ha laudo proprio divergente? → TNU Sumula 25 — impugnar com laudo
  □ A DII (data de inicio da incapacidade) e anterior a DER?
  □ Acionar pericia-medica-prev para impugnacao

FUNDAMENTO D — Tempo de contribuicao insuficiente
  O que verificar:
  □ O INSS computou todos os periodos do CNIS (vinculos + CI + MEI + beneficios)?
  □ Ha periodos especiais que nao foram reconhecidos?
  □ Ha tempo rural que nao foi registrado no CNIS?
  □ Qual a diferenca entre o apurado e o necessario?

FUNDAMENTO E — Requisito de idade ou regra de transicao
  O que verificar:
  □ Qual a data de nascimento do segurado?
  □ Qual era a regra de transicao mais favoravel na DER?
  □ O INSS aplicou a regra correta da EC 103?
```

### 2.2 Saida do Diagnostico

```
## DIAGNOSTICO — CARTA [CONCESSAO/INDEFERIMENTO] — [NOME] — NB: [NUMERO]

**Tipo:** Concessao / Indeferimento
**Especie (B-code):** [XXX]
**Fundamento INSS:** [transcrever resumido]
**DIB:** [data] / **DER:** [data]
**RMI informada:** R$ [valor] (se concessao)

**Pontos Suspeitos:**
1. [ponto — ex: DIB posterior a DER por X dias]
2. [ponto — ex: carencia negada mas periodos B91 nao computados]
3. [ponto — ex: regra de transicao incorreta — RMI potencial maior]

**Caminho Recomendado:**
□ Recurso JR (CRPS) — prazo: 30 dias — acionar administrativo-inss-crps
□ Acao Revisional — acionar acao-revisional-rmi
□ Acao de Concessao — acionar peticao-inicial-prev
□ Impugnacao Medica — acionar pericia-medica-prev

**Skills Adicionais Necessarias:** [lista]
**Urgencia:** [prazo mais proximo]
```

---

## ALERTAS

```
⚠️ PA-03: verificar decadencia (10 anos) antes de propor revisao de RMI
⚠️ PA-07: se DIB posterior a DER → retroativos — nao deixar passar
⚠️ Prazo JR: 30 dias da ciencia — verificar IMEDIATAMENTE ao receber indeferimento
⚠️ PA-14: doenca preexistente — verificar se INSS alega e preparar defesa
```
