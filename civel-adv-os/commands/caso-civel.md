---
description: Abre, retoma, lista ou arquiva um caso civel em civel/casos/<slug>/ — CASO.md, MEMORY.md, arquivos/ e pecas/. Operacionaliza a Memoria de Caso (Protocolo P3).
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [novo <slug> | <slug> | list | arquivar <slug>]
---

Voce foi acionado pelo comando `/caso-civel` do plugin civel-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** operar a memoria de caso compartimentada por cliente (Protocolo P3), em `civel/casos/<slug>/`, mantendo o `CASO.md` como fonte da verdade.

## PROTOCOLO
1. **Verificar configuracao** — procurar `civel/cowork-state.json` subindo a arvore. Se ausente, sugerir `/start-civel`.
2. **Acionar brevemente `civel-master`** (Tier 0) para a governanca, em especial o sigilo OAB + LGPD (sem vazamento entre casos).
3. **Acionar a skill `memoria-de-caso-civel`** e interpretar o argumento:
   - `novo <slug>` — criar a pasta do caso com `CASO.md`, `MEMORY.md`, `arquivos/` e `pecas/`.
   - `<slug>` — retomar o caso: ler e resumir o estado vivo do `CASO.md`.
   - `list` — listar os casos em `civel/casos/` com 1 linha de status cada.
   - `arquivar <slug>` — arquivar o caso, preservando o acervo.
4. **Alertar** se o workspace for pasta sincronizada (OneDrive/iCloud/Google Drive) — risco de espelhamento de dados sensiveis.
5. Manter no `CASO.md` o polo do cliente, a frente, a relacao/fato e os prazos — lidos pelas demais skills.
6. Antes de entregar qualquer peca produzida no caso, lembrar a Revisao R1-R4 (`revisao-final-civel`).

**Skill a acionar:** `memoria-de-caso-civel`.
