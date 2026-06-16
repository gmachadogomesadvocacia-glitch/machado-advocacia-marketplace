---
description: Mandado de seguranca contra ato de autoridade de transito (vicio formal; direito liquido e certo) — com pedido de liminar; Lei 12.016/2009.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao do caso]
---

Voce foi acionado pelo comando `/mandado-seguranca` do plugin transito-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** impetrar mandado de seguranca contra ato ilegal ou abusivo de autoridade de transito, com pedido de liminar.

## PROTOCOLO
1. **Conferir a triagem** — exigir `CASO.md` com polo (defesa), ato coator, autoridade impetrada (DETRAN, JARI, dirigente do orgao), prova pre-constituida e prazo. Sem triagem, acionar `/triagem` antes.
2. **Cabimento** — direito liquido e certo demonstravel de plano (vicio formal patente, recusa de licenciamento por multa indevida, exigencia ilegal); prazo decadencial de 120 dias do ato (Lei 12.016/2009 art. 23). Nao confundir a via com o recurso administrativo (PA-08).
3. **Fixar competencia e autoridade coatora** — orgao estadual/municipal -> Justica Estadual; orgao federal -> Justica Federal (art. 109 CF). Identificar corretamente a autoridade impetrada.
4. **Liminar** — avaliar fumus boni iuris e periculum in mora para suspender o ato (ex.: liberar licenciamento, sustar suspensao da CNH), validando a norma vigente (PA-04) e jurisprudencia (PA-01) e a dupla notificacao quando pertinente (Sum. 312 STJ — PA-07).
5. **Acionar a skill `mandado-seguranca-transito`** — redigir a inicial do MS com a prova documental, o pedido de liminar e a ordem definitiva.
6. **Vedacao** — jamais orientar fraude de pontuacao/indicacao falsa (PA-06).
7. Ao final, submeter a `revisao-final-transito` (R1-R4) antes da entrega.

**Skill a acionar:** `mandado-seguranca-transito`.
