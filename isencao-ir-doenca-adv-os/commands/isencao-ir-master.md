---
description: Ativa a cadeia completa de Isencao de IRPF por doenca grave — 4 Camadas, Proibicoes Absolutas, Protocolos (Selo P1, Cruzamento Administrativo-Judicial) e Suprema Corte R1-R4. Comando-coracao.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [contexto opcional]
---

Voce foi acionado pelo comando `/isencao-ir-master` do plugin isencao-ir-doenca-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** ativar a operacao completa de isencao de IRPF por doenca grave (art. 6 XIV Lei 7.713/88).

## PROTOCOLO
1. **Verificar configuracao** — procurar `isencao-ir/cowork-state.json`. Ausente → sugerir `/start-isencao-ir`.
2. **Acionar a skill `isencao-ir-master`** (Tier 0) — 4 Camadas, Proibicoes Absolutas, Protocolos, roteamento.
3. **Saudar** (advogado, OAB+UF, escritorio, cidade+UF, frentes, Revisao Tecnica).
4. **Conduzir** pelo pipeline: `triagem-isencao-ir` (4 requisitos) → Selo P1 + `analise-documental-isencao-ir` → `analise-trilateral-isencao-ir` + `jurisprudencia-isencao-ir` → `linha-estrategica-isencao-ir` (via) → skill de producao → `revisao-final-isencao-ir` R1-R4 → entrega + atualiza `CASO.md`.
5. Faltando dado → `[INFORMAR]`, nunca inventar (PA-03). NUNCA opinar sobre conduta clinica (PA-04). Proteger dado de saude (PA-10).

**Skill a acionar:** `isencao-ir-master`.
