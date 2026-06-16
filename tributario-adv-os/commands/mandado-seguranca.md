---
description: Produz o mandado de seguranca tributario (Lei 12.016/2009) — direito liquido e certo, autoridade coatora, pedido de liminar. Prazo decadencial de 120 dias.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao do caso]
---

Voce foi acionado pelo comando `/mandado-seguranca` do plugin tributario-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** redigir o mandado de seguranca tributario, preventivo ou repressivo, contra ato de autoridade fiscal.

## PROTOCOLO
1. **Conferir a triagem** — `CASO.md` com o ato/ameaca coatora, a **autoridade coatora** correta, o polo (impetrante/contribuinte), a esfera e o foro (P5).
2. **Requisitos** — direito liquido e certo (prova pre-constituida, documental — PA-01); prazo decadencial de **120 dias** do ato (Lei 12.016/2009 art. 23) no MS repressivo; no preventivo, aferir o justo receio.
3. **Liminar** — fundamentar fumus boni iuris e periculum in mora; atentar para a vedacao de liminar para compensacao (Sum. 212 STJ) e para a Sum. 213 STJ (MS como via de compensacao).
4. **Norma vigente** no fato gerador + transicao da Reforma (PA-04); jurisprudencia validada (PA-01); coerencia de polo (PA-10).
5. **Acionar a skill `mandado-seguranca-tributario`** — peca enxuta, pedido liminar destacado, pedido determinado.
6. Ao final, submeter a `revisao-final-tributaria` (R1-R4).

**Skill a acionar:** `mandado-seguranca-tributario`.
