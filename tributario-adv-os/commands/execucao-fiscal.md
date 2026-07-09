---
description: Defesa na execucao fiscal (LEF 6.830/80).
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao do caso]
---

Voce foi acionado pelo comando `/execucao-fiscal` do plugin tributario-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** estruturar a defesa do executado na execucao fiscal, escolhendo a via processual correta.

## PROTOCOLO
1. **Conferir a triagem** — `CASO.md` com a CDA, o polo (executado/contribuinte ou responsavel), o ente exequente, garantia disponivel e prazos.
2. **Decidir a via (modo estrategico do escritorio):**
   - **Excecao de pre-executividade** — sem garantia, apenas materia de ordem publica conhecivel de oficio e que dispense dilacao probatoria: prescricao, decadencia, ilegitimidade, nulidade da CDA (Sum. 393 STJ). **PA-07** — nao usar para materia que exija prova.
   - **Embargos a execucao** — art. 16 LEF, exigem garantia do juizo (penhora/deposito/seguro/fianca); prazo de 30 dias; admitem ampla dilacao probatoria.
3. **Redirecionamento ao socio** (PA-08) — se houver, aferir os requisitos do art. 135 CTN / Sum. 435 STJ antes de aceitar a inclusao no polo passivo (PA-10).
4. **Decadencia x prescricao** (PA-05) e norma vigente no fato gerador (PA-04); jurisprudencia validada (PA-01).
5. **Acionar a skill `defesa-execucao-fiscal`** para redigir a peca escolhida.
6. Ao final, submeter a `revisao-final-tributaria` (R1-R4).

**Skill a acionar:** `defesa-execucao-fiscal`.
