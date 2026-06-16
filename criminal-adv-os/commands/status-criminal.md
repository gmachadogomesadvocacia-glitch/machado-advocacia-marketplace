---
description: Le o estado atual do plugin (persona, caso ativo, fase/polo, situacao prisional e prazos em aberto) e apresenta um resumo do que esta carregado.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [opcional]
---

Voce foi acionado pelo comando `/status-criminal` do plugin criminal-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** resumir o estado vivo do plugin e do caso ativo para o operador.

## PROTOCOLO
1. **Localizar o estado** — procurar `criminal/cowork-state.json` subindo a arvore; se ausente, sugerir `/start-criminal`.
2. **Acionar a skill `memoria-de-caso-criminal`** — ler a persona ativa (`CRIM_PERSONA`), o caso corrente em `criminal/casos/<slug>/CASO.md`, a situacao prisional e os prazos registrados.
3. **Resumir** — escritorio/advogado, polo (defesa x assistencia), fases configuradas; caso ativo, fase processual, situacao prisional (solto/preso e modalidade) e proximos prazos (custodia, resposta, recursal, prescricao — PA-05) e pendencias `[INFORMAR]`.
4. **Prioridade a liberdade** — se houver pessoa presa, destacar a urgencia no topo do resumo.
5. Nao alterar nenhum arquivo; este comando e somente leitura.

**Skill a acionar:** `memoria-de-caso-criminal`.
