---
description: Inicia o wizard de configuracao do plugin de familia — cria a pasta familia/ com identidade do advogado, area de foco, tom e modo de fluxo. Gera persona e aponta FAM_PERSONA.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [opcional]
---

Voce foi acionado pelo comando `/start-familia` do plugin familia-sucessoes-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** configurar o plugin no ambiente do escritorio e gerar a persona em runtime.

## PROTOCOLO

1. **Acionar a skill `onboarding-familia`** — conduz o wizard (identidade: nome, OAB, cidade/UF; **acervo do escritorio e raiz dos casos (CASE_ROOT)**; area de foco: familia / sucessoes / ambas; polos atendidos; tom de voz e intensidade; modo de fluxo; ferramentas).
2. **Gravar o estado** com `python scripts/state.py init <cowork> ...` + `state.py set` para cada campo. Gravar `{{CASE_ROOT}}` (raiz dos casos).
3. **Renderizar** os templates → `<cwd>/familia/persona.md` e `config.md` (com `{{CASE_ROOT}}` na secao "Acervo e casos"); criar a raiz unificada de casos `<CASE_ROOT>/` (gitignored — sigilo + LGPD). CASE_ROOT = `<acervo>/Casos-Ativos` no Code; **fallback** `<cwd>/familia/casos`. Cada caso = `<CASE_ROOT>/<slug>/` com `CASO.md`, `MEMORY.md`, `arquivos/` e `pecas/`, COMPARTILHADA entre plugins. O estado interno (`cowork-state.json`) permanece em `<cwd>/familia/`.
4. **Apontar `FAM_PERSONA`** no `<cwd>/.claude/settings.local.json`.
5. Alertar se o workspace estiver em pasta sincronizada (dados sensiveis de familia — LGPD).
6. Encerrar sugerindo `/status-familia` e `/triagem`.

**Skill a acionar:** `onboarding-familia`.
