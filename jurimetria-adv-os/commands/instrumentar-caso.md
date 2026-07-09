---
description: Insere ou atualiza o bloco jurimetrico de um CASO.md (identificacao, classificacao CNJ via DataJud, caso, desfecho) e carimba datajud_sync.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: <caminho do CASO.md | lote> [--continuo]
---

Voce foi acionado pelo comando `/instrumentar-caso` do plugin jurimetria-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** a materia-prima da jurimetria — bloco correto em cada CASO.md.

## PROTOCOLO

1. **Acionar a skill `instrumentar-caso`** no CASO.md indicado (ou em lote, na lista de casos sem bloco da ultima coleta).
2. Fontes na ordem: corpo do CASO.md → DataJud (classe/assunto/orgao/data oficiais) → operador (polo, tese, quantum). Campo sem fonte fica vazio + `[PREENCHER]` (PE-12).
3. Nunca sobrescrever desfecho preenchido sem confirmacao; nome de cliente NUNCA no bloco (PE-06).
4. Validar com `py scripts/ler_caso.py "<CASO.md>"` e carimbar `datajud_sync`.
5. Resumo final: campos preenchidos (com fonte), pendencias `[PREENCHER]`.

**Skill a acionar:** `instrumentar-caso`.
