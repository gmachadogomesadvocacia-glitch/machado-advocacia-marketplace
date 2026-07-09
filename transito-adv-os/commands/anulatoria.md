---
description: Acao anulatoria judicial de multa, auto de infracao ou penalidade de transito.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao do caso]
---

Voce foi acionado pelo comando `/anulatoria` do plugin transito-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** redigir a acao anulatoria judicial para desconstituir multa, auto de infracao ou penalidade de transito.

## PROTOCOLO
1. **Conferir a triagem** — exigir `CASO.md` com polo (defesa), ato impugnado, autoridade autuadora, historico da via administrativa e prazo. Sem triagem, acionar `/triagem` antes.
2. **Fixar a competencia** — orgao autuador estadual/municipal -> Justica Estadual; orgao federal (PRF/Uniao) -> Justica Federal (art. 109 CF); nao confundir a via judicial com a administrativa (PA-08).
3. **Verificar a via** — a anulatoria nao depende de exaurir a esfera administrativa, mas atentar a prescricao quinquenal contra a Fazenda (Dec. 20.910/32); a via administrativa preclusa (PA-05) nao impede a judicial.
4. **Analise de vicios** — acionar `analise-vicios-auto-infracao`: nulidades do auto, do equipamento/radar e dupla notificacao (Sum. 312 STJ — PA-07), com a norma vigente na data da infracao (PA-04) e jurisprudencia validada (PA-01).
5. **Acionar a skill `anulatoria-transito`** — qualificar as partes, narrar a causa de pedir, formular o pedido de anulacao (e eventual tutela de urgencia para suspender efeitos), com valor da causa e pedido determinado.
6. **Vedacao** — jamais orientar fraude de pontuacao/indicacao falsa (PA-06).
7. Ao final, submeter a `revisao-final-transito` (R1-R4) antes da entrega.

**Skill a acionar:** `anulatoria-transito`.
