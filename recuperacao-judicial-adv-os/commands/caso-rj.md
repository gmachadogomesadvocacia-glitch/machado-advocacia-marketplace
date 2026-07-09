---
description: Abre, retoma ou lista um caso de Recuperacao Judicial na pasta unificada <CASE_ROOT>/<slug>/.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [novo <slug> | <slug> | list]
---

Voce foi acionado pelo comando `/caso-rj` do plugin recuperacao-judicial-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** gerenciar a memoria de caso compartimentada.

## PROTOCOLO

1. Resolver o `CASE_ROOT` no `config.md` (Code: `<acervo>/Casos-Ativos`; fallback Cowork: `<COWORK>/recuperacao-judicial/casos`). Estado interno do plugin segue em `recuperacao-judicial/`. Sem config → sugerir `/start-rj`.
2. Interpretar `$ARGUMENTS`:
   - **`list`** → listar `<CASE_ROOT>/`.
   - **`novo <slug>`** → criar `<CASE_ROOT>/<slug>/` (com `arquivos/` e `pecas/`) e renderizar `templates/CASO.md.tpl` e `MEMORY-caso.md.tpl` (via `memoria-de-caso-rj`). Pasta COMPARTILHADA entre plugins do mesmo cliente (ex.: RJ + trabalhista).
   - **`<slug>`** → retomar o `CASO.md`.
3. Dados de credor/devedor (valores, CNPJ, processo) SOMENTE na pasta local (gitignored). Alertar se workspace sincronizado.
4. Estrutura do `CASO.md`: polo, classe do credito, valor, fato gerador (concursal/extraconcursal), via, processo de RJ + vara empresarial, processo trabalhista de origem (se CTH), teto 150 SM, prazos.

**Skill a acionar:** `memoria-de-caso-rj`.
