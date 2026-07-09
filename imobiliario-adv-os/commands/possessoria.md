---
description: Acoes possessorias (reintegracao / manutencao / interdito proibitorio).
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao do caso]
---

Voce foi acionado pelo comando `/possessoria` do plugin imobiliario-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** estruturar a acao possessoria adequada (ou a defesa do reu), conforme a agressao a posse e o polo do cliente.

## PROTOCOLO
1. **Conferir a triagem** — `CASO.md` com o tipo de agressao (esbulho / turbacao / ameaca), a data do ato, o polo (possuidor x esbulhador/turbador — PA-10) e a prova da posse anterior.
2. **TRAVA CENTRAL — posse x propriedade x dominio (PA-05)** — a possessoria discute **posse**, nao titulo. Nao deduzir, na possessoria, alegacao de dominio para disputar a posse (art. 557 CPC — exceptio proprietatis vedada). Se o cliente so tem titulo e nao posse, a via e petitoria (reivindicatoria), nao possessoria.
3. **Escolher a acao** — reintegracao (esbulho), manutencao (turbacao) ou interdito proibitorio (ameaca). Aplicar a fungibilidade (art. 554 CPC).
4. **Forca nova x forca velha** — se a agressao tem menos de **ano e dia** (forca nova), cabe o rito especial com liminar (art. 558-562 CPC); apos ano e dia (forca velha), rito comum, sem a liminar do procedimento especial.
5. **Travas** — norma vigente (PA-04); jurisprudencia validada (PA-01); coerencia de polo (PA-10).
6. **Acionar a skill `acoes-possessorias`** para redigir a peca escolhida.
7. Ao final, submeter a `revisao-final-imobiliaria` (R1-R4).

**Skill a acionar:** `acoes-possessorias`.
