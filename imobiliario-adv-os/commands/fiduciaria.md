---
description: Alienacao fiduciaria de imovel (Lei 9.514/97) — rito da consolidacao e do leilao, purgacao da mora, nulidade de leilao; rito proprio obrigatorio (PA-09).
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao do caso]
---

Voce foi acionado pelo comando `/fiduciaria` do plugin imobiliario-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** atuar na alienacao fiduciaria de imovel (Lei 9.514/97), conforme o polo do cliente (fiduciante x credor fiduciario).

## PROTOCOLO
1. **Conferir a triagem** — `CASO.md` com o contrato de alienacao fiduciaria, a matricula, o estagio da mora, as notificacoes/intimacoes do registro de imoveis, o polo (fiduciante x credor fiduciario — PA-10) e os prazos.
2. **TRAVA — rito da Lei 9.514/97 (PA-09)** — respeitar o rito extrajudicial proprio: intimacao do fiduciante pelo oficial do RI para purgar a mora (art. 26), consolidacao da propriedade no nome do credor (art. 26 §7º), e os dois leiloes (art. 27). Nao tratar como busca e apreensao de bem movel (Dec-Lei 911) nem como execucao comum.
3. **Purgacao da mora** — no polo do fiduciante, aferir o prazo de 15 dias da intimacao e o direito de purgar (e a possibilidade ate a arrematacao — jurisprudencia do STJ); no polo do credor, antecipar a purgacao e a regularidade da intimacao.
4. **Nulidade do leilao / da consolidacao** — verificar vicios na intimacao (pessoal/por edital), no valor de avaliacao, no preco vil e no devido procedimento; cabivel acao anulatoria/tutela de urgencia.
5. **Travas** — norma vigente no contrato (PA-04); nao confundir posse x propriedade x dominio (PA-05); jurisprudencia validada (PA-01); coerencia de polo (PA-10).
6. **Acionar a skill `alienacao-fiduciaria-imovel`** para redigir a peca escolhida.
7. Ao final, submeter a `revisao-final-imobiliaria` (R1-R4).

**Skill a acionar:** `alienacao-fiduciaria-imovel`.
