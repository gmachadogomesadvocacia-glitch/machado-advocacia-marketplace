---
description: Redige a peticao inicial previdenciaria (JEF/JF) — FIRAC+AIDA, qualquer especie, com tutela quando cabivel. Exige triagem e estrategia previas.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [especie / dados do caso]
---

Voce foi acionado pelo comando `/redigir-peticao` do plugin previdenciario-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** redigir a inicial previdenciaria completa.

## PROTOCOLO
1. Confirmar que a triagem (`triagem-dogmatica`) e a `estrategia-de-caso` ja rodaram; senao, rode-as antes.
2. **Acionar a skill `peticao-inicial-prev`** — enderecamento (JEF/JF), qualificacao, fatos, direito (FIRAC), pedidos com tutela quando cabivel, valor da causa.
3. Aplicar `estilo-juridico-prev` e, se util, `visual-law-prev` (timeline/tabelas).
4. Submeter a `suprema-corte-previdenciaria` (R1-R4) antes da entrega.

**Skill a acionar:** `peticao-inicial-prev`.
