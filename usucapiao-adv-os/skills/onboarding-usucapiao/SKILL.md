---
name: onboarding-usucapiao
description: >
  ONBOARDING USUCAPIAO — Tier 1, wizard de configuracao (/start-usucapiao). Coleta identidade (nome, OAB, cidade/UF), frentes, tom e ferramentas; grava o estado, renderiza a persona e cria a pasta de casos. Acione quando o usuario disser configurar usucapiao, instalar, primeira vez, comecar a usar, onboarding, /start-usucapiao, ou montar o escritorio.
metadata:
  version: "0.1.0"
  area: "Usucapiao (Judicial e Extrajudicial)"
  tier: 1
---

# ONBOARDING USUCAPIAO (/start-usucapiao)

> Skill **Tier 1** — wizard de configuracao no ambiente do operador. Cria a pasta `usucapiao/` com identidade, frentes, tom e modo, fora do plugin distribuido. Persona local nunca entra no plugin (PA-12).

---

## 0. PRE-CHECK
1. Procurar `usucapiao/cowork-state.json` (subir a arvore a partir do `<cwd>`). Existe → perguntar se reconfigura ou retoma.
2. Wizard **travado em USUCAPIAO** — nao configura outra area.

## 1. PERGUNTAS (uma de cada vez, modo checkpoint)
1. **Identidade:** nome completo, **OAB (numero + UF)**, escritorio, **cidade/UF de atuacao** (eixo critico — foro da situacao do imovel / RI da circunscricao, P5).
2. **Frentes ativas** (uma ou mais):
   - `judicial` — acao de usucapiao;
   - `extrajudicial-cartorio` — usucapiao administrativa (CPC art. 1.071 + Lei 6.015 art. 216-A);
   - `defesa-confrontante` — defesa do confrontante/oponente (contestacao / impugnacao);
   - `consultivo-regularizacao` — pareceres e regularizacao fundiaria.
3. **Tom de voz:** perfil + intensidade (0–10). Combatividade dirigida a teses, nunca a pessoas.
4. **Modo de fluxo:** `checkpoint` (default — pausa nos pontos) ou `--continuo`.
5. **Acervo do escritorio (`CASE_ROOT`):** ha acervo? Com acervo (Code) → `<acervo>/Casos-Ativos`; sem acervo (FALLBACK) → `<COWORK>/usucapiao/casos`. Pasta de casos UNIFICADA e COMPARTILHADA entre os plugins Adv-OS.
6. **Ferramentas:** confirmar `pdf-para-md` (converter PDFs antes de analisar) e gerador de documentos, se disponiveis.

Faltando dado essencial → `[INFORMAR]`, nunca inventar (PA-03).

## 2. GRAVAR ESTADO
- Rodar `python scripts/state.py init` e em seguida `python scripts/state.py set ...` para cada campo coletado (identidade, frentes, tom, modo, `{{CASE_ROOT}}`).
- Estado persistido em `usucapiao/cowork-state.json`.

## 3. RENDERIZAR PERSONA E CONFIG
- Renderizar `templates/persona.md.tpl` → `<cwd>/usucapiao/persona.md`, substituindo `{{ADVOGADO_NOME}}`, `{{OAB_UF}}`, `{{OAB_NUMERO}}`, `{{FIRM_NAME}}`, `{{CIDADE}}`, `{{UF}}`, `{{TOM_VOZ_PERFIL}}`, `{{TOM_VOZ_INTENSIDADE}}`.
- Gravar tambem `<cwd>/usucapiao/config.md` (frentes ativas + modo de fluxo + ferramentas + `{{CASE_ROOT}}`).
- Criar `<CASE_ROOT>/` (pasta de casos UNIFICADA, COMPARTILHADA entre os plugins Adv-OS). No FALLBACK (`<COWORK>/usucapiao/casos`), **gitignored** por default — nenhum dado de cliente no plugin distribuido.

## 4. APONTAR A PERSONA
- Gravar `USU_PERSONA` apontando para `<cwd>/usucapiao/persona.md` no `settings.local.json`, para que `usucapiao-master` carregue a identidade renderizada.

## 5. ALERTA LGPD / SIGILO
- Se o `<cwd>` estiver em pasta **sincronizada** (OneDrive / iCloud / Google Drive / Dropbox), alertar: dados de imovel, matricula, partes e confrontantes sao protegidos por **sigilo OAB + LGPD** (PA-12). Confirmar a pasta de casos `gitignored` e fora do espelho publico.

## 6. ENCERRAMENTO
Entrega o escritorio configurado: estado gravado, `persona.md` + `config.md` renderizados, `casos/` criada e `USU_PERSONA` apontada. Proximo passo: `triagem-usucapiao` (ou `/start-usucapiao` de novo para ajustar).
