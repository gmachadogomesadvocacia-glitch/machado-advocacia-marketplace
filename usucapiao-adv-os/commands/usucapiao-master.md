---
description: Ativa a cadeia completa de Usucapiao (judicial e extrajudicial) — 4 Camadas, Proibicoes Absolutas, tabela de modalidades, Protocolos (Selo P1, Analise de Posse) e Suprema Corte R1-R4. Comando-coracao.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [contexto opcional]
---

Voce foi acionado pelo comando `/usucapiao-master` do plugin usucapiao-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** ativar a operacao completa de usucapiao (judicial e extrajudicial/cartorio).

## PROTOCOLO
1. **Verificar configuracao** — procurar `usucapiao/cowork-state.json`. Ausente → sugerir `/start-usucapiao`.
2. **Acionar a skill `usucapiao-master`** (Tier 0) — 4 Camadas, Proibicoes Absolutas, tabela de modalidades, roteamento.
3. **Saudar** (advogado, OAB+UF, escritorio, cidade+UF, frentes, Revisao Tecnica).
4. **Identificar o polo** (usucapiente x confrontante) e a via (judicial x extrajudicial).
5. **Conduzir** pelo pipeline: `triagem-usucapiao` → Selo P1 + `analise-documental-usucapiao` + `analise-posse-usucapiao` → `analise-trilateral-usucapiao` + `jurisprudencia-usucapiao` → `linha-estrategica-usucapiao` → producao → `revisao-final-usucapiao` R1-R4 → entrega + `CASO.md`.
6. **Bem PUBLICO nao e usucapivel** (PA-04). Faltando dado → `[INFORMAR]`, nunca inventar (PA-03).

**Skill a acionar:** `usucapiao-master`.
