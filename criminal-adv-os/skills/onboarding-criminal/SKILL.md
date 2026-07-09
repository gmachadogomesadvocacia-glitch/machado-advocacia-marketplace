---
name: onboarding-criminal
description: >
  Onboarding criminal Tier 1 — configura o escritorio e a persona do plugin no ambiente do operador. Ative em primeira configuracao, instalar, configurar escritorio, persona, primeira vez ou /start-criminal.
metadata:
  version: "0.1.0"
  area: "Direito Penal e Processo Penal"
  tier: 1
---

# ONBOARDING CRIMINAL

> Tier 1. Wizard de configuracao inicial. Cria a **persona local** do escritorio e o estado de caso. Roda uma vez por ambiente (e quando o operador pedir reconfigurar). Persona gravada FORA do plugin distribuido.

---

## 1. COMANDOS

- **`/start-criminal`** — este wizard (configura persona).
- **`/status-criminal`** — estado do caso ativo e pendencias.
- **`/caso-criminal`** — abre/retoma/lista caso (`memoria-de-caso-criminal`).

## 2. DADOS COLETADOS

| Campo | Token | Exemplo |
|-------|-------|---------|
| Nome do advogado | `{{ADVOGADO_NOME}}` | — |
| OAB UF | `{{OAB_UF}}` | RJ |
| OAB numero | `{{OAB_NUMERO}}` | 172.089 |
| Escritorio | `{{FIRM_NAME}}` | — |
| Cidade | `{{CIDADE}}` | — |
| UF de atuacao | `{{UF}}` | — |
| Email | `{{EMAIL}}` | — |
| Tom de voz | `{{TOM_VOZ_PERFIL}}` | tecnico-garantista |
| Intensidade | `{{TOM_VOZ_INTENSIDADE}}` | 7/10 |

## 3. FASES DE ATUACAO (marcar as ativas)

- [ ] **Investigacao / Inquerito** — flagrante, prisoes cautelares, custodia, relaxamento, liberdade.
- [ ] **Acao penal** — resposta a acusacao, instrucao, alegacoes finais.
- [ ] **Tribunal do Juri** — pronuncia, plenario, quesitos.
- [ ] **Recursos** — apelacao, RESE, embargos, HC/RHC, superiores.
- [ ] **Execucao penal** (LEP) — progressao, livramento, remicao, incidentes.
- [ ] **Acordos despenalizadores** — ANPP, transacao, sursis processual.

> Tambem registrar o **polo predominante**: defesa (padrao) e/ou assistencia de acusacao (vitima).

## 4. PERGUNTAS DO WIZARD

1. Nome completo e OAB (UF + numero)?
2. Nome do escritorio? Cidade/UF de atuacao? Email de contato?
3. Tom de voz preferido e intensidade (0-10)?
4. Quais fases voce atende? (marcar Eixo 3)
5. Atua so na defesa, so como assistente de acusacao, ou ambos?
6. **Acervo** — existe pasta-acervo do escritorio? Definir `CASE_ROOT` (raiz da **pasta unificada de caso**, compartilhada entre plugins): no Code → `<acervo>/Casos-Ativos`; **fallback** → `<COWORK>/criminal/casos`. Criar a pasta e gravar `{{CASE_ROOT}}` no `config.md`.
7. Modo de fluxo: `checkpoint` (default, confirma a cada etapa) ou `--continuo`?

## 5. SAIDA — GERA persona.md

Grava `<cwd>/criminal/persona.md` a partir do template, substituindo os tokens pelos dados coletados. A pasta `criminal/` fica **fora** do plugin distribuido e e **gitignored** por default (dado sensivel — PA-12 / LGPD). Grava tambem `{{CASE_ROOT}}` no `config.md` e cria a pasta unificada de caso em `<CASE_ROOT>/` (`<acervo>/Casos-Ativos` no Code; fallback `<COWORK>/criminal/casos`); o estado interno do plugin segue em `<COWORK>/criminal/`.

```
persona.md
├── Identidade: {{ADVOGADO_NOME}}, OAB/{{OAB_UF}} {{OAB_NUMERO}}, {{FIRM_NAME}}
├── Local: {{CIDADE}}/{{UF}} · {{EMAIL}}
├── Tom: {{TOM_VOZ_PERFIL}} · intensidade {{TOM_VOZ_INTENSIDADE}}/10
├── Fases ativas: [...]
└── Polo predominante: defesa / assistencia / ambos
```

## 6. ALERTAS

- Se a pasta de trabalho for sincronizada (OneDrive/iCloud/Google Drive/Dropbox) → **alertar**: dado penal e sensivel (PA-12, LGPD art. 11). Confirmar gitignore.
- Persona NUNCA versionada no plugin distribuido.
- Concluido o onboarding → sugerir `triagem-criminal` para o primeiro caso.
- Reconfigurar: rodar `/start-criminal` de novo sobrescreve a persona local.
