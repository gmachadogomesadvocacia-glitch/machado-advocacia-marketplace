---
description: Mostra a configuracao e os casos ativos.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

Voce foi acionado pelo comando `/status-leiloes` do plugin leiloes-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** relatar o estado do plugin neste workspace.

## PROTOCOLO
1. Ler `<COWORK>/leiloes/cowork-state.json`, `persona.md` e `config.md`.
2. Reportar: identidade, localizacao, polo, frentes ativas, modo de comparativo, status da Revisao Tecnica e raiz do acervo.
3. Listar os casos em `CASE_ROOT` com fase e **prazos em curso** — destacando em primeiro lugar qualquer prazo de **10 dias** do art. 903 ainda aberto.
4. Se o plugin nao estiver configurado, sugerir `/start-leiloes`.
