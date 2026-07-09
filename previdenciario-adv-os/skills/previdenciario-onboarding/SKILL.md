---
name: previdenciario-onboarding
description: >
  PREVIDENCIARIO ONBOARDING — Skill Engine. Acionar com /start-previdenciario ou quando o usuario disser "tenho um caso previdenciario", "preciso analisar um caso do INSS", ou similar — especialmente quando as informacoes ainda nao foram coletadas.
---

# PREVIDENCIARIO ONBOARDING
> Engine | /start-previdenciario | 6 Blocos | Ficha de Caso + Roteamento Automatico

---

## QUANDO USAR

Acionar este onboarding quando:
- Usuario diz /start-previdenciario
- Usuario traz um caso novo sem ter fornecido ainda as informacoes basicas
- As informacoes minimas para triagem nao estao presentes na conversa

Nao usar quando o caso ja foi triado e o usuario esta em uma fase especifica
(ex: "preciso de quesitos periciais" → ir direto para pericia-medica-prev).

---

## BLOCO 0 — ACERVO E PASTA DO CASO (CASE_ROOT)

```
Perguntar / resolver:
1. Ha acervo do escritorio (Code)? Qual a raiz?
   → CASE_ROOT = <acervo>/Casos-Ativos (fonte da verdade no Code)
   → FALLBACK (Cowork / sem acervo): <COWORK>/previdenciario/casos
2. Definir o <slug> do caso (kebab-case do nome do segurado).
3. Criar a pasta unificada <CASE_ROOT>/<slug>/ com CASO.md, MEMORY.md, arquivos/, pecas/.
   Pasta COMPARTILHADA entre os plugins Adv-OS; pecas em <slug>/pecas/.
4. Gravar {{CASE_ROOT}} no config.md / estado (gitignored quando local — LGPD).
```

## WIZARD — 6 BLOCOS

### BLOCO 1 — IDENTIFICACAO DO SEGURADO

```
Perguntar:
1. Nome completo do segurado
2. CPF / NIT / PIS (opcional — apenas se necessario para calculo)
3. Data de nascimento
4. Sexo
5. Estado / Cidade de residencia (para competencia JEF)
6. E o proprio segurado ou um dependente?
```

### BLOCO 2 — SITUACAO ATUAL DO BENEFICIO

```
Perguntar:
1. Ha beneficio em vigor? Qual especie (B-code)?
   → Se sim: NB e RMI atual
2. Ja houve requerimento ao INSS? Foi concedido ou negado?
   → Se negado: qual o fundamento do INSS?
   → Se concedido: data do primeiro pagamento (DIB)?
3. Ja houve acao judicial? Em qual fase?
4. Ha algum prazo critico? (recurso, audiencia, pericia agendada)
```

### BLOCO 3 — HISTORICO LABORAL RESUMIDO

```
Perguntar:
1. Empregado CLT, contribuinte individual, MEI, servidor publico ou rural?
2. Tempo estimado de contribuicao (anos)?
3. Ha periodos sem registro no CNIS? Periodos rurais?
4. Trabalhou com agentes nocivos (ruido, quimicos, biologicos)?
5. Ha CNIS disponivel para analise? (pedir upload)
```

### BLOCO 4 — DOCUMENTACAO DISPONIVEL

```
Perguntar:
1. Tem CNIS extraido recentemente? (fundamental — pedir upload)
2. Tem carta de concessao ou indeferimento do INSS?
3. Tem laudos medicos, relatorios de especialista, CID?
4. Tem PPP ou LTCAT (se atividade especial)?
5. Tem CTPS, contratos, declaracoes rurais?
```

### BLOCO 5 — OBJETIVO DO CLIENTE

```
Perguntar:
1. O que o cliente quer obter?
   □ Concessao de beneficio ainda nao obtido
   □ Revisao de RMI de beneficio ja concedido
   □ Impugnar cessacao/alta medica indevida
   □ Recurso contra indeferimento do INSS
   □ Planejamento (quando se aposentar / como otimizar)
   □ Regularizacao de contribuicoes em atraso
   □ Outro: [especificar]
2. Ha pressa? (saude critica, sem renda, prazo recursal proximo)
```

### BLOCO 6 — URGENCIAS E PRAZOS

```
Verificar automaticamente:
□ Ha prazo de recurso ao JR vencendo? (30 dias da decisao adversa)
□ Ha audiencia ou pericia agendada?
□ Beneficio cessado sem pagamento? (urgencia de tutela)
□ Beneficiario esta sem renda? (tutela de urgencia / beneficio emergencial?)
□ Decadencia proxima? (revisao de RMI — 10 anos do primeiro pagamento)
```

---

## FICHA DE CASO — OUTPUT DO WIZARD

```
## FICHA DE CASO PREVIDENCIARIO — [NOME] — [DATA]

**Segurado:** [nome] | Nasc.: [data] | Sexo: [M/F] | UF: [estado]
**Tipo de segurado:** CLT / CI / MEI / Servidor / Rural
**TC estimado:** [XX anos XX meses]

**Situacao atual:**
  Beneficio: [especie + NB] / Sem beneficio
  DIB / DER: [datas]
  Indeferimento: [fundamento INSS se houver]

**Documentos disponiveis:** [lista]
**Documentos faltantes:** [lista]

**Objetivo:** [concessao / revisao / recurso / planejamento]
**Urgencias:** [listar em ordem de prioridade]
**Prazo critico:** [data — se houver]

---

## ROTEAMENTO AUTOMATICO

Com base na ficha acima, as proximas skills a acionar sao:

1. triagem-dogmatica → confirmar B-code e competencia
2. analise-cnis → se CNIS disponivel
3. [skill especifica] → [fundamento do roteamento]

⚠️ URGENCIA: [acao imediata necessaria se prazo critico]
```

---

## INSTRUCOES DE ROTEAMENTO

Depois de completar a ficha:

- TC incompleto ou periodos faltantes → analise-cnis
- CNIS com periodos especiais → analise-ppp-ltcat-aposentadoria-especial
- Incapacidade / alta medica indevida → pericia-medica-prev
- Indeferimento com prazo de recurso aberto → administrativo-inss-crps
- Beneficio concedido com RMI suspeita → calculos-previdenciarios → acao-revisional-rmi
- Acao judicial necessaria → peticao-inicial-prev
- Servidor publico → rpps-servidor-publico
- Acidente / doenca ocupacional → acidentario-do-trabalho
- Planejamento PJ / socio → planejamento-prev-pj
- Fundo de pensao / PGBL → previdencia-complementar

---

## ALERTAS

```
⚠️ Nao iniciar analise tecnica antes de completar os 6 blocos — dados incompletos levam a conclusoes erradas
⚠️ Urgencia de prazo: se o prazo de recurso ao JR for inferior a 5 dias uteis → alertar em vermelho no topo
⚠️ LGPD — PA-21: CPF, NIT, CID e laudos sao dados sensiveis — nao solicitar se nao for necessario
⚠️ Roteamento: este wizard entrega a ficha, mas o advogado decide o caminho — nao automatizar decisoes
```
