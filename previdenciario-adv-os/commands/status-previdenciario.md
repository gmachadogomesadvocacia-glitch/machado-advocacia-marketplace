---
description: Mostra o estado do plugin previdenciario.
allowed-tools: Read, Bash, Glob, Grep
argument-hint: [opcional]
---

Voce foi acionado pelo comando `/status-previdenciario` do plugin previdenciario-adv-os.

## PROTOCOLO

1. Procurar `previdenciario/cowork-state.json` subindo a arvore.
   - **Nao encontrado** → informar que o plugin nao esta configurado e sugerir `/start-previdenciario`.
   - **Encontrado** → ler e apresentar:
     - Advogado, OAB/UF, escritorio, cidade/UF
     - Frentes ativas (RGPS/RPPS/complementar/acidentario/planejamento/consultivo)
     - Tom de voz e modo de fluxo
     - Revisao Tecnica (ATIVA/DESATIVADA)
     - Casos em `previdenciario/casos/` (listar slugs)
2. Nao alterar nada — comando somente de leitura.

**Acao:** leitura de estado (sem skill de producao).
