---
description: Produz a repeticao de indebito tributario / pedido de compensacao (CTN 165-170) — restituicao do que foi pago indevidamente. Prazo de 5 anos (PA-09).
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao do caso]
---

Voce foi acionado pelo comando `/repeticao` do plugin tributario-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** redigir a acao de repeticao de indebito ou o pedido de compensacao do tributo pago indevidamente.

## PROTOCOLO
1. **Conferir a triagem** — `CASO.md` com o tributo pago indevidamente, o polo (contribuinte), esfera, valores e comprovantes de recolhimento.
2. **Prazo (PA-09)** — repeticao/compensacao prescreve em **5 anos** (CTN art. 168 / art. 3º LC 118/2005 para o pagamento antecipado). Registrar o termo inicial e o termo final; alertar parcelas ja prescritas.
3. **Legitimidade** — nos tributos indiretos, aferir o art. 166 CTN (prova de nao repasse ou autorizacao de quem suportou o encargo).
4. **Via** — repeticao judicial x compensacao administrativa/judicial (CTN 170; habilitacao do credito); avaliar correcao pela Selic e o regime de compensacao aplicavel.
5. **Norma vigente** no fato gerador (PA-04); jurisprudencia validada (PA-01); coerencia de polo (PA-10).
6. **Acionar a skill `repeticao-indebito-compensacao`** e, ao final, submeter a `revisao-final-tributaria` (R1-R4).

**Skill a acionar:** `repeticao-indebito-compensacao`.
