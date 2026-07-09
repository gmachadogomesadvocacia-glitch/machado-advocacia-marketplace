---
description: Abre, retoma, lista ou arquiva um caso consumerista em consumidor/casos/<slug>/.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [novo <slug> | <slug> | list | arquivar <slug>]
---

Voce foi acionado pelo comando `/caso-consumidor` do plugin consumidor-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** operar a memoria de caso compartimentada por cliente (Protocolo P3), em `consumidor/casos/<slug>/`.

## PROTOCOLO

1. **Verificar configuracao** — procurar `consumidor/cowork-state.json` subindo a arvore. Se ausente, sugerir `/start-consumidor`.
2. **Acionar brevemente `consumidor-master`** (Tier 0) para a governanca, em especial PA-21 (sigilo OAB + LGPD, sem vazamento entre casos).
3. **Acionar a skill `memoria-de-caso-consumidor`** e interpretar o argumento:
   - `novo <slug>` — criar a pasta do caso com `CASO.md`, `MEMORY.md`, `arquivos/` e `pecas/`.
   - `<slug>` — retomar o caso: ler e resumir o estado vivo do `CASO.md`.
   - `list` — listar os casos em `consumidor/casos/` com 1 linha de status cada.
   - `arquivar <slug>` — mover o caso para o estado arquivado, preservando o acervo.
4. **Alertar** se o workspace for pasta sincronizada (OneDrive/iCloud/Google Drive) — risco de espelhamento de dados sensiveis.
5. Manter o `CASO.md` como fonte da verdade do polo do cliente, lido pelas demais skills.
6. Antes de entregar qualquer peca produzida no caso, lembrar a Revisao R1-R4 (`revisao-final-consumidor`, PA-22).

**Skill a acionar:** `memoria-de-caso-consumidor`.
