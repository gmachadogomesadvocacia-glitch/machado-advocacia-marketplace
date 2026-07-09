---
description: Acordos despenalizadores.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao do caso]
---

Voce foi acionado pelo comando `/acordos` do plugin criminal-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** verificar o cabimento e operacionalizar os acordos despenalizadores, no melhor interesse do cliente.

## PROTOCOLO
1. **Conferir a triagem** — exigir `CASO.md` com polo, crime/tipificacao, pena minima, fase e prazo. Sem triagem, acionar `/triagem` antes.
2. **Aferir o instituto cabivel** — **ANPP** (CPP art. 28-A: pena minima inferior a 4 anos, sem violencia/grave ameaca, confissao formal); **transacao penal** (Lei 9.099 art. 76, infracao de menor potencial ofensivo); **suspensao condicional do processo** (Lei 9.099 art. 89, pena minima ate 1 ano).
3. **Acionar a skill `acordos-despenalizadores`** — analisar requisitos e vedacoes, negociar/impugnar condicoes, formular ou responder a proposta, ponderando custo-beneficio frente a defesa de merito.
4. **Norma e garantias** — lei vigente no tempo do fato (PA-04), prescricao (PA-05), garantias do investigado/reu e voluntariedade da confissao (PA-07); jamais orientar obstrucao (PA-08).
5. Ao final, submeter a `revisao-final-criminal` (R1-R4) antes da entrega.

**Skill a acionar:** `acordos-despenalizadores`.
