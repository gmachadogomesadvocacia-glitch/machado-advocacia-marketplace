---
description: Defesa previa / da autuacao (CTB 281-282).
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao do caso]
---

Voce foi acionado pelo comando `/defesa-autuacao` do plugin transito-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** redigir a defesa previa da autuacao, dirigida a autoridade autuadora antes da imposicao da penalidade.

## PROTOCOLO
1. **Conferir a triagem** — exigir `CASO.md` com polo (defesa), codigo CTB do auto, autoridade autuadora, data da infracao, datas das notificacoes e prazo. Sem triagem, acionar `/triagem` antes.
2. **Atencao ao prazo** — confirmar o prazo de 30 dias da Notificacao da Autuacao; vencido, e preclusivo (PA-05). Se ja houve penalidade, a via correta e `/recurso`, nao a defesa previa (PA-08).
3. **Analise de vicios** — acionar `analise-vicios-auto-infracao`: requisitos do auto (CTB 280), validade do equipamento/radar, dupla notificacao (Sum. 312 STJ — PA-07), tempestividade da NA, identificacao do agente e da via.
4. **Acionar a skill `defesa-autuacao`** — fundamentar na norma vigente na data da infracao (PA-04), narrar o vicio formal/material, formular o pedido de arquivamento ou insubsistencia do auto; postura adversarial.
5. **Vedacao** — jamais orientar fraude de pontuacao ou indicacao falsa de condutor (PA-06); a indicacao do real condutor segue por `/indicar-condutor`.
6. Ao final, submeter a `revisao-final-transito` (R1-R4) antes da entrega.

**Skill a acionar:** `defesa-autuacao`.
