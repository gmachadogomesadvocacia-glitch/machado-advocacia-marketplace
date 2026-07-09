---
description: Acionamento direto da triagem dogmatica previdenciaria.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao do caso]
---

Voce foi acionado pelo comando `/triagem` do plugin previdenciario-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** executar a triagem dogmatica do caso e gravar o diagnostico no `CASO.md`.

## PROTOCOLO

1. **Acionar `previdenciario-master`** brevemente para verificar configuracao + governanca.
2. **Acionar a skill `triagem-dogmatica`** — classifica:
   - **Especie (B-code):** B31/B32 incapacidade · B91/B94 acidentario · B41/B42 idade/tempo · B45 especial · BPC/LOAS · pensao por morte · salario-maternidade
   - **Regime:** RGPS · RPPS · previdencia complementar
   - **Competencia:** JEF · Justica Federal · Justica Estadual (acidentario) · administrativo (CRPS)
   - **Carencia + qualidade de segurado + DER otima**
3. **Gravar resultado** no `CASO.md` (abrir caso novo se necessario).
4. **Sugerir o pipeline Tier 1** (`analise-trilateral` -> `jurisprudencia-estrategica` -> `estrategia-de-caso`) e o Tenente Tier 2 cabivel.

**Skill a acionar:** `triagem-dogmatica`.
