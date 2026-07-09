---
description: Porta de entrada do plugin.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao do caso]
---

Voce foi acionado pelo comando `/triagem` do plugin transito-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** classificar a demanda de transito nos 5 eixos e gravar o diagnostico no `CASO.md`. Esta e a porta de entrada de todo caso.

## PROTOCOLO
1. **Acionar brevemente `transito-master`** (Tier 0) para carregar a governanca de 4 Camadas e os Protocolos antes de classificar.
2. **Acionar a skill `triagem-transito`** — classificar nos 5 eixos: **Eixo** (administrativo / CNH / judicial / analise), **Fase** (defesa previa da autuacao, recurso JARI, recurso CETRAN, suspensao, cassacao, indicacao, anulatoria, MS), **Auto/Infracao** (codigo CTB, autoridade autuadora — DETRAN/municipio/PRF/DER, natureza leve/media/grave/gravissima), **Pontuacao/CNH** (pontos acumulados, processo de suspensao/cassacao em curso) e **Prazo** (administrativo preclusivo de 30 dias — PA-05).
3. **Prioridade ao prazo preclusivo** — se houver prazo administrativo de 30 dias em curso, tratar como urgencia maxima e rotear de imediato a defesa/recurso cabivel, antes de qualquer outra producao (PA-05).
4. **Confirmar o polo** — defesa do condutor x proprietario do veiculo; em ausencia ou contradicao, parar e perguntar antes de produzir (PA-10).
5. **Triagem de instancia** — fixar esfera/orgao/instancia sem confundi-las (administrativa JARI/CETRAN x judicial — PA-08) e a norma vigente na data da infracao (PA-04).
6. **Gravar** o diagnostico no `CASO.md`; toda lacuna essencial entra como `[INFORMAR]`, nunca inventada (PA-01).
7. **Rotear** — encaminhar para o **Selo P1** (validacao de norma de transito vigente — PA-11), para `analise-documental-transito` e para `analise-vicios-auto-infracao`.
8. **Crime de transito** — se houver embriaguez (art. 306) ou homicidio/lesao culposa (302/303 CTB), encaminhar a `criminal-adv-os` (PA-09). Antes de qualquer entrega posterior, lembrar a Revisao R1-R4.

**Skill a acionar:** `triagem-transito`.
