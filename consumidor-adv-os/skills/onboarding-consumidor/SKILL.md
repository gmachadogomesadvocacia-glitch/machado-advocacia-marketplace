---
name: onboarding-consumidor
description: >
  ONBOARDING CONSUMIDOR — Skill Tier 1, wizard de configuracao do plugin no ambiente do escritorio.
  Conduz perguntas estruturadas para criar a pasta consumidor/ com a identidade do advogado (nome,
  OAB, cidade/UF), polos de atuacao (consumidor/fornecedor/ambos), eixos do consumo, tom de voz,
  modo de melhor saida e ferramentas. Gera persona.md, config.md, a pasta casos/ e aponta
  CONSUM_PERSONA no settings.local.json. Acione quando o operador disser configurar consumidor,
  instalar, primeira vez, /start-consumidor, ou onboarding. Wizard travado em CONSUMIDOR.
metadata:
  version: "0.1.0"
  area: "Direito do Consumidor e Bancario"
  tier: 1
---

# ONBOARDING CONSUMIDOR (/start-consumidor)

> Skill **Tier 1** — wizard que configura o plugin no workspace do operador. Gera a persona em runtime (decisao de chassi) e o estado do plugin.

---

## 0. FUNCAO

Capturar a identidade do escritorio e gravar o estado, para que todas as skills resolvam os tokens `{{...}}` e operem com a persona real (substituindo a persona-fallback).

## 1. PERGUNTAS DO WIZARD (em blocos, confirmando ao fim)

**Bloco 1 — Identidade**
- Nome do advogado responsavel
- OAB (numero) e UF
- Nome do escritorio
- Cidade e UF de atuacao (eixo de foro/competencia — Protocolo P5)
- Email/telefone (opcional)

**Bloco 2 — Atuacao**
- Polos: consumidor | fornecedor | ambos
- Eixos atendidos (multipla escolha): bancario, negativacao, telecom, servicos-essenciais, aereo, vicio-fato-produto, e-commerce, publicidade, clausula-abusiva, cobranca-indevida, superendividamento, consumo-imobiliario

**Bloco 2b — Acervo e raiz dos casos (CASE_ROOT)**
- Perguntar o acervo do escritorio e definir o `CASE_ROOT` — pasta unificada e COMPARTILHADA entre os plugins Adv-OS. No Claude Code, usar `<acervo>/Casos-Ativos`; fora do Code (fallback), `<COWORK>/consumidor/casos`. Cada caso = `<CASE_ROOT>/<slug>/` { CASO.md, MEMORY.md, arquivos/, pecas/ }.

**Bloco 3 — Estilo e operacao**
- Tom de voz: tecnico-objetivo | tecnico-didatico | tecnico-cordial | personalizado
- Intensidade combativa (0-10; default 6)
- Modo de melhor saida: recomendar-e-listar (default) | apenas-listar
- Revisao Tecnica R1-R4: ativa (default) | desativada
- Output preferido: txt (default — convencao do escritorio) | docx
- Ferramentas (livre): sistema juridico, peticionamento eletronico, CRM, nuvem, assinatura digital

> Faltando dado essencial, pergunte; nao invente. Defaults aplicados so quando o operador autoriza ("pode usar o padrao").

## 2. GRAVACAO

1. Rodar `python scripts/state.py init <cowork_path> --firm-name "<...>" --firm-slug "<slug>" --advogado "<...>"` e depois `state.py set` para cada campo coletado (identity, tom_voz, areas/eixos, preferences).
2. Renderizar `templates/persona.md.tpl` → `<cowork>/consumidor/persona.md` resolvendo os tokens.
3. Renderizar `templates/config.md.tpl` → `<cowork>/consumidor/config.md`, gravando `{{CASE_ROOT}}` na secao `Acervo e casos`.
4. Criar a pasta de casos em `{{CASE_ROOT}}` (no Code, `<acervo>/Casos-Ativos`; no fallback `<cowork>/consumidor/casos`, gitignored — sigilo OAB + LGPD).
5. Renderizar `templates/settings-local.json.tpl` e fundir em `<cwd>/.claude/settings.local.json`, apontando `CONSUM_PERSONA` para o `persona.md` gerado.

## 3. AVISO DE SINCRONIZACAO (LGPD)

Se o workspace estiver em pasta sincronizada (OneDrive/iCloud/Google Drive/Dropbox), alertar: dados de caso/cliente nao devem ir para nuvem de terceiros sem ciencia (sigilo OAB + LGPD). Confirmar se o operador aceita ou prefere outro local para `casos/`.

## 4. ENCERRAMENTO

Ao final, confirmar o resumo da configuracao e avisar que a partir da proxima interacao a persona real e injetada (a fallback deixa de ser carregada). Sugerir `/status-consumidor` para conferir e `/triagem-consumidor` para abrir o primeiro caso.
