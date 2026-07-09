---
description: Impugnacao a laudo pericial desfavoravel.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [dados do laudo]
---

Voce foi acionado pelo comando `/impugnar-laudo` do plugin previdenciario-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** atacar tecnicamente o laudo pericial desfavoravel.

## PROTOCOLO
1. **Acionar a skill `pericia-medica-prev`** — analisa o laudo, formula quesitos complementares, confronta CID/capacidade laborativa, idade, profissao e condicoes sociais; mobiliza TNU (Sumula 25, 47) e a possibilidade de nova pericia.
2. Articular com `analise-trilateral` (nexo) e a prova dos autos.
3. Submeter a `suprema-corte-previdenciaria` (R1-R4).

**Skill a acionar:** `pericia-medica-prev`.
