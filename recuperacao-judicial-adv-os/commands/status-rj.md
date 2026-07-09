---
description: Mostra o estado do plugin de Recuperacao Judicial.
allowed-tools: Read, Bash, Glob, Grep
argument-hint: [opcional]
---

Voce foi acionado pelo comando `/status-rj` do plugin recuperacao-judicial-adv-os.

## PROTOCOLO

1. Procurar `recuperacao-judicial/cowork-state.json` subindo a arvore.
   - **Nao encontrado** → informar que nao esta configurado e sugerir `/start-rj`.
   - **Encontrado** → apresentar: advogado, OAB/UF, escritorio, cidade/UF; frentes ativas; tom e modo; Revisao Tecnica (ATIVA/DESATIVADA); casos em `recuperacao-judicial/casos/`.
2. Somente leitura — nao alterar nada.

**Acao:** leitura de estado.
