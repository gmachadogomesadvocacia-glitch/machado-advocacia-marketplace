---
description: Produz a impugnacao administrativa ao auto de infracao / lancamento (PAF), que suspende a exigibilidade do credito (CTN 151 III). Prazo 30 dias.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao do caso]
---

Voce foi acionado pelo comando `/impugnacao` do plugin tributario-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** redigir a impugnacao administrativa ao auto de infracao ou ao lancamento, na frente administrativa (PAF — Dec. 70.235/72 federal; processo do ente estadual/municipal).

## PROTOCOLO
1. **Conferir a triagem** — exigir `CASO.md` com polo (contribuinte), esfera/tributo, fase e prazo. Sem triagem, acionar `/triagem` antes.
2. **Validar prazo e efeito** — impugnacao tempestiva (30 dias da ciencia do lancamento) suspende a exigibilidade do credito (CTN art. 151, III); registrar a data de ciencia e o termo final.
3. **Verificar decadencia x prescricao** (PA-05) — aferir se o lancamento ocorreu dentro do prazo decadencial (CTN 150 §4º / 173).
4. **Acionar a skill `impugnacao-administrativa`** — atacar a base do lancamento: nulidades formais, erro na materia tributavel, base de calculo, multa, e antecipar a manifestacao fiscal (postura adversarial dura).
5. **Norma vigente** no fato gerador, com regra de transicao da Reforma quando cabivel (PA-04); jurisprudencia administrativa/judicial validada (PA-01).
6. Ao final, submeter a `revisao-final-tributaria` (R1-R4) antes da entrega.

**Skill a acionar:** `impugnacao-administrativa`.
