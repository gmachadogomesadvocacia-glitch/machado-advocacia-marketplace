---
description: Defesa no processo de cassacao da CNH (CTB 263) e orientacao sobre a reabilitacao para reobtencao da habilitacao.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao do caso]
---

Voce foi acionado pelo comando `/cnh-cassacao` do plugin transito-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** redigir a defesa no processo administrativo de cassacao da CNH e orientar a reabilitacao.

## PROTOCOLO
1. **Conferir a triagem** — exigir `CASO.md` com polo (defesa), hipotese de cassacao (CTB 263: reincidencia no periodo de suspensao, condenacao por crime de transito, condutor com direito ja suspenso), notificacao e prazo. Sem triagem, acionar `/triagem` antes.
2. **Distinguir do processo de suspensao** — a cassacao pressupoe situacao mais grave; nao confundir as fases nem as instancias (PA-08), validando a norma vigente na data dos fatos (PA-04).
3. **Atencao ao prazo** — prazo administrativo preclusivo de 30 dias da notificacao (PA-05).
4. **Analise de vicios** — acionar `analise-vicios-auto-infracao`: validade do processo de suspensao anterior (cuja nulidade contamina a cassacao), dupla notificacao (Sum. 312 STJ — PA-07), proporcionalidade.
5. **Acionar a skill `cassacao-cnh`** — atacar os pressupostos da cassacao e formular o pedido de arquivamento; orientar, ao final, a **reabilitacao** (prazo do CTB 263 §2o, novos exames e nova habilitacao) quando a cassacao for inevitavel.
6. **Interface criminal** — se a cassacao decorrer de crime de transito, alinhar a defesa criminal por `criminal-adv-os` (PA-09). Vedada qualquer fraude de pontuacao/indicacao falsa (PA-06).
7. Ao final, submeter a `revisao-final-transito` (R1-R4) antes da entrega.

**Skill a acionar:** `cassacao-cnh`.
