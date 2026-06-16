---
description: Porta de entrada do plugin — triagem tributaria em 5 eixos (frente, tributo/esfera, fase, polo, prazo), grava no CASO.md e roteia para o Selo P1 e a analise documental.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao do caso]
---

Voce foi acionado pelo comando `/triagem` do plugin tributario-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** classificar a demanda tributaria nos 5 eixos e gravar o diagnostico no `CASO.md`. Esta e a porta de entrada de todo caso.

## PROTOCOLO
1. **Acionar brevemente `tributario-master`** (Tier 0) para carregar a governanca de 4 Camadas e os Protocolos antes de classificar.
2. **Acionar a skill `triagem-tributaria`** — classificar nos 5 eixos: **Frente** (administrativa / judicial / consultiva), **Tributo/Esfera** (federal IR/IPI/PIS/COFINS/CSLL — estadual ICMS/IPVA/ITCMD — municipal ISS/IPTU/ITBI), **Fase** (lancamento, contencioso administrativo, inscricao em DA, execucao fiscal, recursal), **Polo** (contribuinte x Fazenda — variavel-mae) e **Prazo** (decadencia x prescricao — PA-05; repeticao 5 anos — PA-09).
3. **Confirmar o polo do cliente** — em ausencia ou contradicao, parar e perguntar antes de produzir (PA-10).
4. **Gravar** o diagnostico no `CASO.md`; toda lacuna essencial entra como `[INFORMAR]`, nunca inventada (PA-01).
5. **Rotear** — encaminhar para o **Selo P1** (validacao de norma vigente no fato gerador — PA-04) e para `analise-documental-tributaria`.
6. Antes de qualquer entrega posterior, lembrar a Revisao R1-R4.

**Skill a acionar:** `triagem-tributaria`.
