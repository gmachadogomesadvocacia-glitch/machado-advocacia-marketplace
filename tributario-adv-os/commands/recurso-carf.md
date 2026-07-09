---
description: Produz o recurso administrativo.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao do caso]
---

Voce foi acionado pelo comando `/recurso-carf` do plugin tributario-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** redigir o recurso administrativo contra a decisao de primeira instancia no contencioso administrativo.

## PROTOCOLO
1. **Conferir a triagem** — `CASO.md` com a decisao recorrida (acordao/decisao DRJ ou equivalente estadual/municipal), polo, esfera e prazo recursal.
2. **Definir o orgao e a via** — federal: recurso voluntario ao CARF, recurso especial a CSRF (divergencia); estadual: TIT (SP) ou conselho de contribuintes; municipal: conselho do ente. Confirmar prazo (em regra 30 dias).
3. **Acionar a skill `recurso-administrativo-carf`** — atacar os fundamentos da decisao recorrida, demonstrar prequestionamento e, no recurso especial, comprovar a divergencia jurisprudencial com paradigmas.
4. **Norma vigente** no fato gerador + transicao da Reforma (PA-04); jurisprudencia (incl. sumulas CARF) validada (PA-01).
5. Ao final, submeter a `revisao-final-tributaria` (R1-R4) — atencao ao prazo recursal correto.

**Skill a acionar:** `recurso-administrativo-carf`.
