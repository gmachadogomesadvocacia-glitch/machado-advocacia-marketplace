---
description: Acao renovatoria e revisional de aluguel (Lei 8.245/91).
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao do caso]
---

Voce foi acionado pelo comando `/renovatoria` do plugin imobiliario-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** estruturar a acao renovatoria de locacao nao residencial ou a revisional de aluguel, conforme o polo do cliente.

## PROTOCOLO
1. **Conferir a triagem** — `CASO.md` com o contrato (locacao nao residencial), o polo (locatario-empresario ou locador — PA-10), o tempo de contrato e de exploracao do ramo, e os prazos.
2. **Renovatoria — requisitos do art. 51** — contrato escrito por prazo determinado, prazo minimo de 5 anos (somado), exploracao do mesmo ramo por 3 anos. **PRAZO DECADENCIAL (art. 51 §5º): a acao deve ser proposta no interregno de 1 ano a, no maximo, 6 meses anteriores ao termo final do contrato — perda do prazo = decadencia, sem renovatoria (PA-07).** Conferir esse prazo ANTES de qualquer redacao.
3. **Revisional (art. 19)** — cabivel apos 3 anos de vigencia do contrato ou do ultimo acordo, para ajuste do aluguel ao valor de mercado; fixacao de aluguel provisorio.
4. **Defesa do locador** na renovatoria — exceptio (insuficiencia da proposta, retomada art. 52, melhor proposta de terceiro).
5. **Travas** — norma vigente no contrato (PA-04); jurisprudencia validada (PA-01); coerencia de polo (PA-10).
6. **Acionar a skill `renovatoria-revisional`** para redigir a peca escolhida.
7. Ao final, submeter a `revisao-final-imobiliaria` (R1-R4).

**Skill a acionar:** `renovatoria-revisional`.
