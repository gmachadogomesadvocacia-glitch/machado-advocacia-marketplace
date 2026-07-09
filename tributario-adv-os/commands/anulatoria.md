---
description: Produz a acao anulatoria de debito fiscal (art. 38 LEF).
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao do caso]
---

Voce foi acionado pelo comando `/anulatoria` do plugin tributario-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** redigir a acao anulatoria de debito fiscal para desconstituir o lancamento ou a CDA.

## PROTOCOLO
1. **Conferir a triagem** — `CASO.md` com o ato a anular (lancamento/CDA), polo (contribuinte), esfera/tributo, valores e o foro competente (P5 — domicilio do contribuinte x sede do orgao).
2. **Cabimento e estrategia** — acao anulatoria do art. 38 LEF; avaliar deposito do montante integral (Sum. 112 STJ) para suspender a exigibilidade (CTN 151 II) e/ou tutela de urgencia; ponderar anulatoria x mandado de seguranca (modo de melhor saida).
3. **Causa de pedir** — vicios do lancamento, inconstitucionalidade/ilegalidade da exigencia, erro de base de calculo, decadencia (PA-05).
4. **Norma vigente** no fato gerador + transicao da Reforma (PA-04); jurisprudencia validada (PA-01); coerencia de polo (PA-10).
5. **Acionar a skill `acao-anulatoria-tributaria`** — peca enxuta, pedidos determinados, antecipacao adversarial.
6. Ao final, submeter a `revisao-final-tributaria` (R1-R4).

**Skill a acionar:** `acao-anulatoria-tributaria`.
