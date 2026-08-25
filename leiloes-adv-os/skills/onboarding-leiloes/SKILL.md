---
name: onboarding-leiloes
description: >
  Onboarding do plugin de leiloes Tier 1 — conduz o wizard do /start-leiloes e grava persona, config e estado. Acione quando o usuario rodar /start-leiloes ou pedir para configurar o plugin.
metadata:
  version: "0.1.0"
  area: "Leiloes e Arrematacao"
  tier: 1
---

# ONBOARDING DE LEILOES

> Tier 1. Conduz o `/start-leiloes`, grava o estado e sai. Nao produz peca.

## 1. O QUE PERGUNTAR

1. **Identidade** — nome do advogado, OAB (numero/UF), nome do escritorio, e-mail, telefone.
2. **Localizacao** — cidade e UF da sede. Eixo de juizo da execucao, registro de imoveis e foro da situacao do imovel.
3. **Polo** — confirmar que o escritorio atende **quem compra**: `arrematante` e/ou `pretendente a arrematante`. Explicar que executado, devedor fiduciante, exequente e credor fiduciario sao roteados a outro plugin (PA-12), e que isso e deliberado.
4. **Frentes** — due diligence pre-lance · leilao judicial · leilao extrajudicial fiduciario · imissao e desocupacao · defesa da arrematacao · invalidacao, desistencia e eviccao · registro e baixa de onus.
5. **Ritos que costuma enfrentar** — civel, fiscal, trabalhista. Serve para priorizar exemplos e alertas de prazo.
6. **Raiz do acervo** (`CASE_ROOT`) — onde ficam os casos.
7. **Tom de voz** — perfil e intensidade; postura default.
8. **Modo de comparativo** — `recomendar-e-listar` (default) ou `apenas-listar`.
9. **Revisao Tecnica** — ATIVA por default.
10. **Ferramentas** — peticionamento, nuvem, certificado digital, portais de leilao.

## 2. O QUE GRAVAR

- `<COWORK>/leiloes/cowork-state.json` (schema em `scripts/state-schema.json`)
- `<COWORK>/leiloes/persona.md` e `config.md` (a partir dos templates)
- `<COWORK>/leiloes/casos/` (gitignored)
- `LEIL_PERSONA` no `.claude/settings.local.json`

## 3. FECHAMENTO

Confirmar o que foi gravado, avisar que a persona vale **na proxima sessao** e indicar o proximo passo: `/triagem` para o primeiro caso, ou `/due-diligence` se ja houver um lote na mira.
