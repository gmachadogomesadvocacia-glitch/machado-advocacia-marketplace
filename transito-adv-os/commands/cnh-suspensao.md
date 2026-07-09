---
description: Defesa no processo de suspensao do direito de dirigir.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao do caso]
---

Voce foi acionado pelo comando `/cnh-suspensao` do plugin transito-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** redigir a defesa no processo administrativo de suspensao do direito de dirigir.

## PROTOCOLO
1. **Conferir a triagem** — exigir `CASO.md` com polo (defesa), pontuacao acumulada no periodo de 12 meses, modalidade (pontuacao x autossuspensiva), notificacao de instauracao e prazo. Sem triagem, acionar `/triagem` antes.
2. **Identificar o limite de pontos** — conferir o teto aplicavel conforme a Lei 14.071/2020 (20/30/40 pontos segundo a presenca de infracao gravissima), validando a norma vigente na data dos fatos (PA-04).
3. **Atencao ao prazo** — prazo administrativo preclusivo de 30 dias da notificacao de instauracao (PA-05); nao confundir com o processo de cassacao nem com a via judicial (PA-08).
4. **Analise de vicios** — acionar `analise-vicios-auto-infracao`: validade das autuacoes-base que somam pontos (uma multa anulada derruba a contagem), dupla notificacao (Sum. 312 STJ — PA-07), prescricao das infracoes.
5. **Acionar a skill `suspensao-direito-dirigir`** — atacar a contagem de pontos e os autos-base, sustentar nulidades e formular o pedido de arquivamento; avaliar o curso de reciclagem como alternativa quando aplicavel.
6. **Vedacao** — jamais orientar fraude de pontuacao ou indicacao falsa de condutor (PA-06).
7. Ao final, submeter a `revisao-final-transito` (R1-R4) antes da entrega.

**Skill a acionar:** `suspensao-direito-dirigir`.
