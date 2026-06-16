---
description: Recursos criminais — apelacao, RESE, embargos de declaracao/infringentes, RHC e recursos superiores; vedada a reformatio in pejus.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao do caso]
---

Voce foi acionado pelo comando `/recursos` do plugin criminal-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** identificar o recurso cabivel e redigir as razoes, respeitando os prazos e a vedacao da reformatio in pejus.

## PROTOCOLO
1. **Conferir a triagem** — exigir `CASO.md` com polo, decisao recorrida, fase e **prazo recursal** preciso. Sem triagem, acionar `/triagem` antes.
2. **Identificar o recurso** — apelacao (CPP 593), recurso em sentido estrito (CPP 581), embargos de declaracao, embargos infringentes, RHC, recurso especial/extraordinario; conferir cabimento, tempestividade e preparo.
3. **Reformatio in pejus** — em recurso exclusivo da defesa, vedada a piora da situacao do reu (CPP 617); confirmar antes de redigir.
4. **Acionar a skill `recursos-criminais`** — redigir as razoes atacando dosimetria (PA-06), nulidades, absolvicao e demais teses, com antecipacao das contrarrazoes (postura adversarial dura).
5. **Norma e prescricao** — lei penal vigente no tempo do fato (PA-04), prescricao da pretensao punitiva/executoria (PA-05), jurisprudencia validada (PA-01); garantias (PA-07).
6. Ao final, submeter a `revisao-final-criminal` (R1-R4) antes da entrega.

**Skill a acionar:** `recursos-criminais`.
