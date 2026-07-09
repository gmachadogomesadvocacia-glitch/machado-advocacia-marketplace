---
name: analise-trilateral
description: >
  ANALISE TRILATERAL PREVIDENCIARIA — Skill Tier 1 (Estado-Maior). Acionar imediatamente apos triagem-dogmatica em qualquer caso previdenciario.
---

# ANALISE TRILATERAL PREVIDENCIARIA
> Tier 1 — Estado-Maior | Fato + Nexo + Direito | FIRAC base

---

## 0. FUNCAO

Produz a matriz trilateral que todas as skills Tier 2 usam para construir pecas.
Sem analise trilateral, a Suprema Corte trava em R3 por FIRAC incompleto.

---

## 1. DIMENSAO FATO

### 1.1 Cronologia do Segurado

Construir linha do tempo com:
```
[Ano] → Vinculo/Atividade → SC mensal → Observacao
Ex:
1985-1991 → Empregado CLT (metalurgia, exposicao a ruido 92 dB) → R$ X.XXX → CNIS registrado
1991-1994 → Desempregado → - → Gap: verificar periodo de graca
1994-2024 → Contribuinte Individual → R$ X.XXX → Recolhimento CI sobre pro-labore
```

### 1.2 Eventos Relevantes

```
□ Data do adoecimento / acidente (para beneficios por incapacidade)
□ Data da cessacao do vinculo (para verificacao de qualidade de segurado)
□ Data do requerimento administrativo (DER)
□ Data do indeferimento / concessao / cessacao
□ Recursos administrativos ja interpostos e resultados
```

### 1.3 Gaps e Inconsistencias no CNIS

```
□ Periodos sem contribuicao: intencionais ou erro de registro?
□ Recolhimentos como CI sem NF/DARF correspondentes
□ Vinculos no CNIS sem salario correspondente
□ Contribuicoes abaixo do piso ou acima do teto
```

---

## 2. DIMENSAO NEXO

### 2.1 Tipos de Nexo Relevantes por Beneficio

**Nexo Contributivo** (aposentadoria programada, pensao):
```
Tempo de contribuicao + carencia + qualidade de segurado
Gaps impactam? → verificar periodo de graca
Categoria correta no CNIS? → empregado vs CI vs MEI
```

**Nexo Medico-Legal** (incapacidade temporaria/permanente):
```
Diagnostico (CID): compativel com incapacidade para o trabalho habitual?
Doenca preexistente (PA-14): o INSS pode alegar — verificar data de filiacao vs CID
Relacao entre CID e atividade laboral?
Laudo medico: recente (< 6 meses) ou desatualizado?
```

**Nexo Ocupacional/Causal** (aposentadoria especial, acidentario):
```
Agente nocivo: qual? Em qual nivel de exposicao?
Periodo de exposicao: continuo ou intermitente?
PPP assinado por medico do trabalho com registro CRM?
LTCAT elaborado por profissional habilitado (engenheiro de seguranca ou medico do trabalho)?
NTEP (Nexo Tecnico Epidemiologico): aplicavel? Foi contestado pela empresa?
Tema 555 STF: para ruido, EPI eficaz NAO afasta o nexo (PA-05)
```

### 2.2 Nexo para Pensao por Morte

```
Qualidade de segurado do de cujus na data do obito?
Dependentes economicos: comprovar dependencia (conjuge/companheiro presumida; outros: provar)
Filhos invalidos ou com deficiencia: sem limite de idade
Duracao da pensao: calcular conforme art. 77 com redacao EC 103/2019
```

---

## 3. DIMENSAO DIREITO

### 3.1 Identificacao das Normas Aplicaveis

```
Lei 8.213/91 (beneficios): art. especifico para a especie do beneficio
EC 103/2019: regra permanente ou de transicao (conforme data de filiacao)
Decreto 3.048/99: regulamento
IN INSS 128/2022: procedimentos administrativos
Norma especifica: LC 150/2015 (domesticos), LC 123/2006 (MEI), Lei 9.717/98 (RPPS)
```

### 3.2 Jurisprudencia Estrategica

```
Mapear as teses disponiveis — acionar jurisprudencia-estrategica para pesquisa completa:
- Sumula TNU vinculante (para JEF)
- Tema repetitivo STJ (para TRF)
- Tese de repercussao geral STF (para todos)
- Jurisprudencia regional TRF (para JF)
```

### 3.3 Baloney Detection (Camada 3 — filtro de tese fraca)

```
REJEITAR imediatamente:
❌ Desaposentacao: STF Tema 709 — rejeitada definitivamente (PA-06)
❌ Revisao da vida toda em escala: apenas individualmente quando favoravel
❌ Teses baseadas em MPs ou medidas provisorias nao convertidas em lei
❌ Jurisprudencia de TRF contraria a sumula TNU vinculante

SINALIZAR como arriscado:
⚠️ Teses novas sem consolidacao (verificar se ha tema repetitivo pendente no STJ/STF)
⚠️ Teses que dependem de reforma legislativa em curso
```

### 3.4 Escala de Comprometimento da Tese

```
FORTE: amparada por sumula TNU + tema STJ/STF + fatos bem documentados
MEDIA: amparada por jurisprudencia nao uniformizada ou fatos com lacuna probatoria
FRACA: sem amparo jurisprudencial uniforme OU fato controvertido
→ Se FRACA: recomendar ao cliente os riscos antes de protocolar (Suprema Corte R3 bloqueia)
```

---

## 4. MATRIX TRILATERAL (OUTPUT)

```
## ANALISE TRILATERAL — [NOME] — [BENEFICIO PRETENDIDO] — [DATA]

DIMENSAO FATO:
  Cronologia: [resumo da linha do tempo]
  Gaps/riscos fatcos: [lista]
  Provas solidas: [lista]
  Provas ausentes/urgentes: [lista + impacto na tese]

DIMENSAO NEXO:
  Tipo de nexo: [contributivo / medico-legal / ocupacional / misto]
  Avaliacao: [FORTE / MEDIO / FRACO] — [justificativa]
  Riscos: [doenca preexistente / gap de qualidade / ausencia de PPP]

DIMENSAO DIREITO:
  Tese principal: [descricao + norma + jurisprudencia]
  Tese alternativa: [descricao se houver]
  Baloney detectado: [lista de teses rejeitadas]
  Escala de comprometimento: [FORTE / MEDIA / FRACA]

RECOMENDACAO:
  Caminho recomendado: [administrativo / judicial / ambos]
  Skill Tier 2 recomendada: [nome-da-skill]
  Urgencias: [prazos criticos, provas urgentes]
```
