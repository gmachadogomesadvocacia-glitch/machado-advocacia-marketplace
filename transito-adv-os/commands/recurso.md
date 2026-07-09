---
description: Recursos administrativos apos a Notificacao da Penalidade.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao do caso]
---

Voce foi acionado pelo comando `/recurso` do plugin transito-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** redigir o recurso administrativo cabivel apos a imposicao da penalidade, na instancia correta.

## PROTOCOLO
1. **Conferir a triagem** — exigir `CASO.md` com polo (defesa), codigo CTB, autoridade, data da Notificacao da Penalidade e prazo. Sem triagem, acionar `/triagem` antes.
2. **Fixar a instancia** — 1a instancia: **JARI** (Junta Administrativa de Recursos de Infracoes); 2a instancia: **CETRAN** (orgao estadual) ou **CONTRANDIFE** (ambito federal/DF). Nao confundir as instancias (PA-08); o recurso de 2a so cabe apos decisao da JARI.
3. **Atencao ao prazo** — 30 dias da NP ou da decisao da JARI; vencido, e preclusivo (PA-05).
4. **Analise de vicios** — acionar `analise-vicios-auto-infracao`: requisitos do auto, equipamento/radar, dupla notificacao (Sum. 312 STJ — PA-07), cerceamento de defesa na 1a instancia.
5. **Acionar a skill `recursos-administrativos`** — fundamentar na norma vigente na data da infracao (PA-04) e em jurisprudencia validada (PA-01); narrar o vicio e formular o pedido de provimento; postura adversarial.
6. **Vedacao** — jamais orientar fraude de pontuacao ou indicacao falsa (PA-06).
7. Ao final, submeter a `revisao-final-transito` (R1-R4) antes da entrega.

**Skill a acionar:** `recursos-administrativos`.
