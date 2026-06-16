---
description: Mostra o estado do plugin de Isencao de IRPF — identidade do operador, frentes ativas, Revisao Tecnica e casos ativos. Se nao configurado, sugere /start-isencao-ir.
allowed-tools: Read, Bash, Glob, Grep
argument-hint: [opcional]
---

Voce foi acionado pelo comando `/status-isencao-ir` do plugin isencao-ir-doenca-adv-os.

## PROTOCOLO
1. Procurar `isencao-ir/cowork-state.json` subindo a arvore.
   - **Nao encontrado** → informar que nao esta configurado e sugerir `/start-isencao-ir`.
   - **Encontrado** → apresentar: advogado, OAB/UF, escritorio, cidade/UF; frentes; tom e modo; Revisao Tecnica (ATIVA/DESATIVADA); casos em `isencao-ir/casos/`.
2. Somente leitura.

**Acao:** leitura de estado.
