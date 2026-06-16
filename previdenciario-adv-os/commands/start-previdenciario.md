---
description: Inicia o wizard de configuracao do plugin previdenciario — cria a pasta previdenciario/ com identidade do advogado, frentes de atuacao, tom e modo de fluxo. Gera persona e aponta PREV_PERSONA.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [opcional]
---

Voce foi acionado pelo comando `/start-previdenciario` do plugin previdenciario-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** configurar o plugin no ambiente do escritorio e gerar a persona em runtime.

## PROTOCOLO

1. **Acionar a skill `previdenciario-onboarding`** — conduz o wizard (identidade: nome, OAB, cidade/UF; frentes: RGPS / RPPS / previdencia complementar / acidentario / planejamento PJ / consultivo empresarial; tom de voz; modo de fluxo; ferramentas).
2. **Gravar o estado** com `python scripts/state.py init <cowork> ...` + `state.py set` para cada campo.
3. **Renderizar** os templates → `<cwd>/previdenciario/persona.md` e `config.md`; criar `<cwd>/previdenciario/casos/` (gitignored — LGPD).
4. **Apontar `PREV_PERSONA`** no `<cwd>/.claude/settings.local.json`.
5. Alertar se o workspace estiver em pasta sincronizada (dados sensiveis do segurado — LGPD).
6. Encerrar sugerindo `/status-previdenciario` e `/triagem`.

**Skill a acionar:** `previdenciario-onboarding`.
