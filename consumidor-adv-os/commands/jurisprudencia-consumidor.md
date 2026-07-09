---
description: Busca, valida e organiza jurisprudencia consumerista/bancaria.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [tese ou tema a pesquisar]
---

Voce foi acionado pelo comando `/jurisprudencia-consumidor` do plugin consumidor-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** localizar e validar fundamento jurisprudencial para a tese em jogo, classificando por forca e aderencia ao caso.

## PROTOCOLO

1. **Verificar configuracao** — procurar `consumidor/cowork-state.json` subindo a arvore. Se ausente, sugerir `/start-consumidor`.
2. **Acionar brevemente `consumidor-master`** (Tier 0) para a governanca e o polo do cliente (a jurisprudencia util flipa conforme o polo).
3. **Acionar a skill `jurisprudencia-consumidor`** — buscar STJ (Corte Especial, 3a/4a Turmas), TJs, sumulas e Temas repetitivos pertinentes ao eixo.
4. **PA-01 — nunca citar sem validar:** conferir existencia, numero, orgao, teor e vigencia de toda Sumula/Tema/IRDR antes de inserir. Nada de alucinacao jurisprudencial.
5. **Conferir** especialmente as sumulas-chave do eixo: Sumula 385 (negativacao preexistente), 530/382 (juros/taxa media), 539/541 (capitalizacao), Tema 929 (dobro do art. 42).
6. **Classificar** os precedentes por forca (vinculante > persuasivo) e aderencia factica; sinalizar contra-precedentes que o adversario usaria.
7. Antes de a tese ir para a peca, lembrar a Revisao R1-R4 (`revisao-final-consumidor`, PA-22).

**Skill a acionar:** `jurisprudencia-consumidor`.
