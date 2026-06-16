---
description: Le o estado atual do plugin (persona, caso ativo, frente/polo, valor da causa, prazos) e resume em uma fotografia rapida do escritorio e do caso.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [opcional]
---

Voce foi acionado pelo comando `/status-civel` do plugin civel-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** apresentar o estado vigente — config do escritorio e caso ativo — sem produzir peca.

## PROTOCOLO
1. **Verificar configuracao** — procurar `civel/cowork-state.json` subindo a arvore. Se ausente, sugerir `/start-civel`.
2. **Acionar a skill `memoria-de-caso-civel`** para ler o estado.
3. **Resumir a persona** — advogado, OAB+UF, escritorio, cidade/UF, frentes ativas, polo(s), tom, status da Revisao Tecnica.
4. **Resumir o caso ativo** (se houver) a partir do `CASO.md`: frente, polo do cliente, relacao/fato (contratual x extracontratual), valor estimado da causa, prazos criticos (prescricao x decadencia) e lacunas `[INFORMAR]` pendentes.
5. Se nao houver caso ativo, sugerir `/triagem` para abrir um.

**Skill a acionar:** `memoria-de-caso-civel`.
