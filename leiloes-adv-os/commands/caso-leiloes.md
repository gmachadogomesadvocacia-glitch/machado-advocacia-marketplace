---
description: Abre ou atualiza a ficha do caso.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [nome do caso]
---

Voce foi acionado pelo comando `/caso-leiloes` do plugin leiloes-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** criar ou atualizar `CASO.md` e `MEMORY.md` do caso.

## PROTOCOLO
1. Acionar `memoria-de-caso-leiloes`.
2. Criar a estrutura `<CASE_ROOT>/<slug>/` (CASO.md, MEMORY.md, arquivos/, pecas/) a partir dos templates. **Perguntar o caminho ao operador antes de criar** — nao decidir o destino sozinho.
3. Preencher com o resultado da triagem; registrar documentos como "doc. N".
4. Manter em destaque a **data do auto de arrematacao** e a **data-limite dos 10 dias**.
5. Compartimentar: dado de um caso nao migra para outro (PA-13).

**Skill a acionar:** `memoria-de-caso-leiloes`.
