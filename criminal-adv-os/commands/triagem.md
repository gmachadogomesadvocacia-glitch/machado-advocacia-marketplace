---
description: Porta de entrada do plugin.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao do caso]
---

Voce foi acionado pelo comando `/triagem` do plugin criminal-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** classificar a demanda criminal nos 5 eixos e gravar o diagnostico no `CASO.md`. Esta e a porta de entrada de todo caso.

## PROTOCOLO
1. **Acionar brevemente `criminal-master`** (Tier 0) para carregar a governanca de 4 Camadas e os Protocolos antes de classificar.
2. **Acionar a skill `triagem-criminal`** — classificar nos 5 eixos: **Fase** (investigacao/inquerito, acao penal, juri, recursos, execucao penal, acordos), **Polo** (defesa do investigado/reu/sentenciado x assistencia de acusacao — variavel-mae, PA-10), **Crime/Tipificacao** (capitulacao, competencia, especial x comum), **Situacao prisional** (solto, preso em flagrante/temporario/preventivo/definitivo) e **Prazo** (custodia, resposta, recursal; prescricao penal — PA-05).
3. **Prioridade a liberdade** — se houver pessoa presa, tratar a soltura como urgencia maxima e rotear de imediato a HC / relaxamento / liberdade provisoria / audiencia de custodia, antes de qualquer outra producao.
4. **Confirmar o polo do cliente** — em ausencia ou contradicao, parar e perguntar antes de produzir (PA-10).
5. **Gravar** o diagnostico no `CASO.md`; toda lacuna essencial entra como `[INFORMAR]`, nunca inventada (PA-01).
6. **Rotear** — encaminhar para o **Selo P1** (validacao de norma penal vigente no tempo do fato — PA-04) e para `analise-documental-criminal`.
7. Antes de qualquer entrega posterior, lembrar a Revisao R1-R4.

**Skill a acionar:** `triagem-criminal`.
