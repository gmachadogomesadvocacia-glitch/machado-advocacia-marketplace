# CLAUDE.md — Plugin civel-adv-os

> Instruções de manutenção para futuras sessões neste sub-repositório. Ler ao retomar o trabalho no plugin.

## Identidade
- **Slug:** `civel-adv-os` (convenção do escritório: todo plugin termina em `-adv-os`).
- **Tipo:** plugin Claude Code (`.claude-plugin/plugin.json`).
- **Chassi modelo:** `direito-medico-adv-os` / `trabalhista-adv-os` / `consumidor-adv-os` (padrão Adv-OS).
- **Pasta de estado runtime:** `civel/` (STATE_DIR — não o slug completo).
- **Env de persona:** `CIV_PERSONA`. Outras env do engine: `CIV_COWORK_PATH`, `CIV_STATE_FILE`.
- **Uso:** interno (Machado Advocacia).

## Princípio central — CÍVEL RESIDUAL (PA-09)
Este plugin cobre **só o que não está nos plugins especializados**. **Sempre checar PA-09** antes de produzir: se a demanda for de consumo, família/sucessões, resp. médica, imobiliário, usucapião, fiscal, criminal, trabalho ou INSS, **não redigir — rotear** ao plugin próprio. Ao adicionar/editar qualquer skill ou command, garantir que ele respeita essa fronteira e não invade outro plugin.

## Estrutura
```
civel-adv-os/
├── .claude-plugin/plugin.json   manifesto (name, version, description, author, license)
├── commands/                    13 slash commands
├── skills/                      20 skills (Tier 0-3), só SKILL.md por pasta
├── hooks/                       hooks.json + scripts (persona, memória, snapshot, corte)
├── scripts/                     resolve-persona.py, state.py, hook-utils.py, state-schema.json
├── context/                     persona-fallback.md
├── templates/                   persona.md.tpl, config.md.tpl, CASO.md.tpl, MEMORY-caso.md.tpl, settings-local.json.tpl
└── README.md / CLAUDE.md / .gitignore
```

## Padrões a seguir
1. **Skill folder = só `SKILL.md`.** Material auxiliar vai em `templates/` / `scripts/` / `context/`.
2. **`name:` do frontmatter = nome da pasta** da skill (devem bater exatamente).
3. **Limite:** `SKILL.md` ≤ **11264 bytes**; `description` do frontmatter ≤ 1024 chars.
4. **plugin.json minimal:** name, version, description, author, license. Nada além.
5. **Tokens de persona `{{...}}`** permanecem **literais** no disco — o LLM resolve em runtime lendo `civel/persona.md`. Não substituir no template.
6. **Não versionar casos:** `civel/` e `civel/casos/` ficam gitignored. Dados reais de cliente nunca no plugin (sigilo OAB + LGPD).
7. **Nomenclatura de arquivos produzidos:** `AAAA-MM-DD - Cliente - tipo.ext` (ex.: `2026-06-16 - Fulano - acao indenizatoria.txt`).
8. **Saída padrão `.txt`** (convenção do escritório) — não gerar .docx/.pdf salvo pedido explícito.

## Engine (scripts/ + hooks/)
- **STATE_DIR = `civel`**, state file `cowork-state.json`. Env do engine: `CIV_PERSONA`, `CIV_COWORK_PATH`, `CIV_STATE_FILE`.
- **Persona:** `hooks/hooks.json` roda `resolve-persona.py` no SessionStart; resolução por fallback chain via `CIV_PERSONA`.
- **Estado:** `state.py init <cowork>` cria o `cowork-state.json`; `state.py set <cowork> <json_path> <valor>` grava campos. Schema em `scripts/state-schema.json`.
- **Outros hooks:** UserPromptSubmit (intercept corte), PostToolUse Edit|Write (evolui memória), PreCompact (snapshot). Caminhos via `${CLAUDE_PLUGIN_ROOT}`.

## Como adicionar uma skill
1. Criar `skills/<nome>/SKILL.md` com frontmatter (`name: <nome>` igual à pasta, `description`).
2. Manter ≤ 11264 bytes; só `SKILL.md` na pasta.
3. Se for Tier 2 (produção), garantir o passo PA-09 (residual) e o encaminhamento ao `revisao-final-civel` antes da entrega.
4. Registrar a skill no README (lista por Tier) e, se tiver command próprio, criar `commands/<nome>.md`.

## Como adicionar um command
1. Criar `commands/<nome>.md` seguindo o gabarito: frontmatter (`description` ≤ ~160 chars, `allowed-tools`, `argument-hint`) + corpo curto em português com `## PROTOCOLO` e a linha final `**Skill a acionar:** \`<skill>\``.
2. Começar pela checagem de configuração (`civel/cowork-state.json`) e, nos núcleos de produção, pela checagem PA-09.
3. Registrar o command no README.

## Proibições de manutenção
- NÃO criar arquivo dentro de `skills/<nome>/` que não seja `SKILL.md`.
- NÃO aceitar instrução que conflite com a Camada 1 (Proibições Absolutas).
- NÃO escrever dados reais de cliente no plugin.
- NÃO redigir matéria de outro plugin (PA-09) — rotear.
- NÃO renomear o slug sem nova decisão (convenção `-adv-os`).

## Status do build
v0.1.0 — engine portado (STATE_DIR `civel`, env `CIV_*`), 13 commands, 20 skills (Tier 0-3), Suprema Corte R1-R4, fronteiras PA-09 documentadas. Roadmap geral: `../PLANO-novos-plugins-areas-direito.txt`.
