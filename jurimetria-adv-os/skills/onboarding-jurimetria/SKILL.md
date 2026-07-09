---
name: onboarding-jurimetria
description: >
  ONBOARDING JURIMETRIA — Skill Tier 1, wizard de configuracao do plugin no ambiente do escritorio. Acione quando o operador disser configurar jurimetria, instalar, primeira vez, /start-jurimetria, ou onboarding.
metadata:
  version: "0.1.0"
  area: "Jurimetria"
  tier: 1
---

# ONBOARDING JURIMETRIA (/start-jurimetria)

> Skill **Tier 1** — wizard que configura o plugin no workspace do operador. Gera a persona em runtime e o estado do plugin.

---

## 0. FUNCAO

Capturar a identidade do escritorio e — o essencial deste plugin — **onde esta o acervo** (CASE_ROOT) e **quais tribunais** servem de regua, para que todas as skills resolvam os tokens `{{...}}`.

## 1. PERGUNTAS DO WIZARD (em blocos, confirmando ao fim)

**Bloco 1 — Identidade**
- Nome do advogado responsavel; OAB (numero) e UF
- Nome do escritorio; cidade e UF
- Email/telefone (opcional)

**Bloco 2 — Acervo (CASE_ROOT)**
- Raiz dos casos — pasta unificada e COMPARTILHADA entre os plugins Adv-OS. No Claude Code, `<acervo>/Casos-Ativos`; fora do Code (fallback), `<COWORK>/jurimetria/casos`.
- Cada `CASO.md` sob a raiz deve carregar o bloco jurimetrico (`templates/bloco-jurimetrico.md.tpl`). Avisar que a skill `instrumentar-caso` preenche os que faltarem.

**Bloco 3 — Benchmark**
- Tribunais de referencia (ex.: TJRJ, TRT1, TRF2) — viram os aliases DataJud do `benchmark_datajud.py`.

**Bloco 4 — Freios e estilo**
- N minimo para media/taxa (default 5 — PE-04)
- Revisao R1-R4: ativa (default) | desativada
- Modo de melhor saida: recomendar-e-listar (default) | apenas-listar
- Output preferido: txt (default)

> Faltando dado essencial, pergunte; nao invente. Defaults so com autorizacao do operador.

## 2. GRAVACAO

1. Rodar `python scripts/state.py init <cowork_path> --firm-name "<...>" --firm-slug "<slug>" --advogado "<...>"` e depois `state.py set` para cada campo coletado.
2. Renderizar `templates/persona.md.tpl` → `<cowork>/jurimetria/persona.md` resolvendo os tokens (inclusive `{{CASE_ROOT}}`, `{{TRIBUNAIS}}`, `{{N_MINIMO}}`).
3. Renderizar `templates/config.md.tpl` → `<cowork>/jurimetria/config.md`.
4. Renderizar `templates/settings-local.json.tpl` e fundir em `<cwd>/.claude/settings.local.json`, apontando `JURI_PERSONA` para o `persona.md` gerado.

## 3. AVISO DE SINCRONIZACAO (LGPD)

Se o workspace estiver em pasta sincronizada (OneDrive/iCloud/Google Drive/Dropbox), alertar: datasets e relatorios com dados de caso nao devem ir para nuvem de terceiros sem ciencia (sigilo OAB + LGPD). Confirmar o local de saida dos relatorios.

## 4. PRIMEIRA COLETA (opcional, recomendada)

Oferecer rodar `py scripts/coletar_acervo.py "<CASE_ROOT>"` na hora: mostra quantos CASO.md existem, quantos ja tem bloco jurimetrico e a lista dos que faltam — o retrato inicial da instrumentacao.

## 5. ENCERRAMENTO

Confirmar o resumo da configuracao; avisar que a partir da proxima interacao a persona real e injetada. Sugerir `/status-jurimetria` para conferir e `/coletar-acervo` para o primeiro retrato do portfolio.
