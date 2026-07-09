---
description: Mostra o estado do plugin de familia.
allowed-tools: Read, Bash, Glob, Grep
argument-hint: [opcional]
---

Voce foi acionado pelo comando `/status-familia` do plugin familia-sucessoes-adv-os.

## PROTOCOLO

1. Procurar `familia/cowork-state.json` subindo a arvore.
   - **Nao encontrado** → informar que o plugin nao esta configurado e sugerir `/start-familia`.
   - **Encontrado** → ler e apresentar:
     - Advogado, OAB/UF, escritorio, cidade/UF
     - Area de foco e polos atendidos
     - Tom de voz e modo de fluxo
     - Revisao Tecnica (ATIVA/DESATIVADA)
     - Casos em `familia/casos/` (listar slugs)
2. Nao alterar nada — comando somente de leitura.

**Acao:** leitura de estado (sem skill de producao).
