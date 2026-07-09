---
name: triagem-dogmatica
description: >
  TRIAGEM DOGMATICA PREVIDENCIARIA — Skill Tier 1 (Estado-Maior). Acionar SEMPRE como primeira skill em novo caso.
---

# TRIAGEM DOGMATICA PREVIDENCIARIA
> Tier 1 — Estado-Maior | Porta de Entrada Dogmatica | Sempre antes dos Tenentes

---

## 0. FUNCAO NO PIPELINE

Triagem-Dogmatica → Analise-Trilateral → Skill especifica do Tier 2 → Suprema Corte R1-R4.
Sem triagem, a Suprema Corte trava em R1 por falta de fato.

---

## 1. ENQUADRAMENTO DA ESPECIE (B-CODE)

| B-Code | Beneficio | Codigo |
|--------|-----------|--------|
| B41 | Aposentadoria por tempo de contribuicao (pre-EC 103) / Programada pos-EC 103 | 41 |
| B42 | Aposentadoria por idade | 42 |
| B46 | Aposentadoria especial | 46 |
| B31 | Aposentadoria por incapacidade permanente | 31 |
| B32 | Aposentadoria por incapacidade permanente (acidentaria) | 32 |
| B91 | Auxilio por incapacidade temporaria (comum) | 91 |
| B94 | Auxilio por incapacidade temporaria (acidentario) | 94 |
| B21 | Pensao por morte (urbana) | 21 |
| B56 | BPC/LOAS idoso | 56 |
| B87 | BPC/LOAS pessoa com deficiencia | 87 |
| B80 | Salario-maternidade | 80 |

---

## 2. CHECKLIST DE TRIAGEM DOGMATICA

### 2.1 Categoria e Regime

```
□ Categoria: empregado CLT / CI (pro-labore ou autonomo) / MEI / segurado especial rural /
             domestico / preso que trabalha / aposentado que volta
□ Regime: RGPS (INSS) / RPPS (servidor) / Complementar (fundo de pensao)
□ Vinculo atual: ativo / desligado / periodo de graca
□ Se RPPS: orgao e regime (federal/estadual/municipal) — rota para rpps-servidor-publico
```

### 2.2 Datas Criticas (DER, DIB, DCB)

```
DER — Data de Entrada do Requerimento: quando o segurado pediu ao INSS
DIB — Data de Inicio do Beneficio: quando o INSS determinou que o beneficio começa
DCB — Data de Cessacao do Beneficio: quando o beneficio foi cortado (se ja ocorreu)

Verificar:
□ A DER foi registrada corretamente? (impacta retroativos)
□ A DIB e igual a DER (correto) ou posterior (possivel prejuizo)?
□ Ha DCB indevida? (beneficio foi cortado sem fundamento?)
```

### 2.3 Carencia e Qualidade de Segurado

```
□ Carencia necessaria: 0 (acidente) / 12 (maioria) / 18 (salario-maternidade) / 180 (aposentadoria)
□ Competencias computadas: verificar no CNIS
□ Qualidade de segurado: mantida / perdida / periodo de graca
  - Empregado: 12 meses apos desligamento (24 se >120 contribuicoes; 36 se desempregado involuntario)
  - CI/MEI: 12 meses apos ultima contribuicao
  - Segurado especial: atividade rural comprovada
```

### 2.4 Regra de Calculo (Protocolo P1 — EC 103)

```
□ Data de filiacao: antes ou apos 13/11/2019?
□ Se antes de 13/11/2019: mapear regras de transicao disponiveis (acionar beneficios-inss)
□ Se apos 13/11/2019: apenas regra permanente (60% + 2% a.a.)
□ Se RPPS: verificar regras da EC 103 para servidores (aposentadoria voluntaria/compulsoria)
```

### 2.5 Competencia Judicial

```
□ Beneficio INSS + valor ate 60 SM: JEF (Juizado Especial Federal)
□ Beneficio INSS + valor acima de 60 SM: JF ordinaria
□ RPPS federal: JF / TRF
□ RPPS estadual/municipal: Justica Estadual
□ Recurso administrativo em curso: CRPS (JR → CaJ → Pleno)
□ MS: TRF (ato de autoridade federal)
```

### 2.6 Provas Disponiveis

```
□ CNIS atualizado (extraido no Meu INSS)
□ PPP (Perfil Profissiografico Previdenciario) — se aposentadoria especial
□ LTCAT (Laudo Tecnico das Condicoes Ambientais do Trabalho) — se especial
□ Laudos medicos atualizados — se incapacidade
□ Carta de concessao / carta de indeferimento
□ CTPS (Carteira de Trabalho)
□ Certidao de tempo de servico (servico militar, RPPS)
□ Documentos rurais (ITR, sindicato, declaracao testemunhal)
```

---

## 3. OUTPUT DA TRIAGEM DOGMATICA

```
## TRIAGEM DOGMATICA — [NOME] — [DATA]

**Especie (B-Code):** [BXX — descricao]
**Categoria:** [empregado / CI / MEI / rural / especial]
**Regime:** [RGPS / RPPS]
**Data de filiacao:** [data ou "a confirmar via CNIS"]
**Regra aplicavel:** [permanente EC 103 / transicao: qual]
**DER:** [data] | **DIB:** [data ou "nao concedido"] | **DCB:** [data ou "N/A"]
**Qualidade de segurado:** [mantida / perdida / periodo de graca ate XX/XX/XXXX]
**Carencia:** [XX meses acumulados / necessarios: XX] → [cumprida / pendente]
**Competencia:** [JEF / JF / CRPS / TRF — justificativa]

**Provas disponiveis:** [lista]
**Provas ausentes / urgentes:** [lista + impacto]

**Alertas PA:** [lista de PAs ativadas e risco]
**Proxima skill:** analise-trilateral → [skill Tier 2 recomendada]
```
