---
description: Acionamento direto da triagem de familia/sucessoes — enquadra area, polo, tipo de caso e urgencia, e abre o CASO.md. Porta de entrada de toda demanda.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao do caso]
---

Voce foi acionado pelo comando `/triagem` do plugin familia-sucessoes-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** enquadrar o caso e gravar o diagnostico no `CASO.md`.

## PROTOCOLO

1. **Acionar `familia-master`** brevemente para verificar configuracao + governanca.
2. **Acionar a skill `triagem-familia`** — classifica:
   - **Area:** Familia · Sucessoes · Ambas (dissolucao com espolio)
   - **Polo:** requerente · requerido · inventariante · herdeiro/meeiro · testamenteiro · consultor
   - **Tipo:** divorcio/separacao · guarda/alimentos · uniao estavel · interdicao/curatela/TDA · inventario/arrolamento · testamento/planejamento · violencia domestica
   - **Regime de bens** (quando patrimonial) e **urgencia** (alimentos provisionais, guarda liminar)
3. **Gravar resultado** no `CASO.md` (abrir caso novo se necessario).
4. **Sugerir** o pipeline e a skill de producao cabivel.

**Skill a acionar:** `triagem-familia`.
