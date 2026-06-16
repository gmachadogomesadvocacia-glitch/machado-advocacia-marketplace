---
description: Le o estado atual do plugin (persona, caso ativo, frente/esfera, polo e prazos em aberto) e apresenta um resumo do que esta carregado.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [opcional]
---

Voce foi acionado pelo comando `/status-tributario` do plugin tributario-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** resumir o estado vivo do plugin e do caso ativo para o operador.

## PROTOCOLO
1. **Localizar o estado** — procurar `tributario/cowork-state.json` subindo a arvore; se ausente, sugerir `/start-tributario`.
2. **Acionar a skill `memoria-de-caso-tributario`** — ler a persona ativa (`TRIB_PERSONA`), o caso corrente em `tributario/casos/<slug>/CASO.md` e os prazos registrados.
3. **Resumir** — escritorio/advogado, polo, frentes e esferas configuradas; caso ativo, fase processual, proximos prazos (decadencia/prescricao/recursal — PA-05) e pendencias `[INFORMAR]`.
4. Nao alterar nenhum arquivo; este comando e somente leitura.

**Skill a acionar:** `memoria-de-caso-tributario`.
