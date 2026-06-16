---
description: Mostra o estado do plugin de Usucapiao — identidade do operador, frentes ativas, Revisao Tecnica e casos ativos. Se nao configurado, sugere /start-usucapiao.
allowed-tools: Read, Bash, Glob, Grep
argument-hint: [opcional]
---

Voce foi acionado pelo comando `/status-usucapiao` do plugin usucapiao-adv-os.

## PROTOCOLO
1. Procurar `usucapiao/cowork-state.json` subindo a arvore.
   - **Nao encontrado** → informar que nao esta configurado e sugerir `/start-usucapiao`.
   - **Encontrado** → apresentar: advogado, OAB/UF, escritorio, cidade/UF; frentes; tom e modo; Revisao Tecnica (ATIVA/DESATIVADA); casos em `usucapiao/casos/`.
2. Somente leitura.

**Acao:** leitura de estado.
