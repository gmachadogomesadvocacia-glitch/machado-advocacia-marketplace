---
description: Abre ou atualiza o CASO.md do caso ativo (Protocolo P3) em imobiliario/casos/<slug>/.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [novo <slug> | <slug> | list]
---

Voce foi acionado pelo comando `/caso-imobiliario` do plugin imobiliario-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** abrir, retomar ou atualizar o `CASO.md` do caso ativo, mantendo a memoria de caso compartimentada.

## PROTOCOLO
1. **Acionar a skill `memoria-de-caso-imobiliario`** (Protocolo P3) — operar a pasta `<cwd>/imobiliario/casos/<slug>/` com `CASO.md`, `MEMORY.md`, `arquivos/` e `pecas/`.
2. **Interpretar o argumento** — `novo <slug>` cria a estrutura a partir do `CASO.md.tpl`; `<slug>` retoma; `list` lista os casos; sem argumento, usa o caso ativo.
3. **Atualizar** — gravar polo (PA-10), frente, imovel (matricula/endereco/area), contrato/tipo de demanda, fase, prazos e decisoes no `CASO.md`; lacunas essenciais como `[INFORMAR]` (PA-01). Nao confundir posse x propriedade x dominio (PA-05).
4. **Sigilo** — garantir que a pasta de casos permanece gitignored; alertar se o workspace for pasta sincronizada (sigilo OAB + LGPD).

**Skill a acionar:** `memoria-de-caso-imobiliario`.
