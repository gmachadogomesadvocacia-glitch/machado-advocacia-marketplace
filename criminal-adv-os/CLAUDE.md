# CLAUDE.md — manutencao do plugin criminal-adv-os

Instrucoes para quem (humano ou Claude) for editar este plugin. Curtas e
praticas. Para o uso pelo operador, ver `README.md`.

## Estrutura de pastas

```
criminal-adv-os/
├── .claude-plugin/plugin.json   # manifesto (name, version, description)
├── commands/                    # 13 slash-commands (.md, frontmatter + corpo curto)
├── skills/<nome>/SKILL.md       # 20 skills, uma pasta por skill
├── templates/                   # persona.md.tpl, config.md.tpl, CASO.md.tpl, ...
├── scripts/                     # engine: state.py, resolve-persona.py, hook-utils.py
├── hooks/                       # SessionStart (injeta a persona) e outros
├── context/                     # contexto compartilhado entre skills
├── .gitignore                   # ignora criminal/, casos/, CASO.md, arquivos/
├── README.md
└── CLAUDE.md                    # este arquivo
```

## Regras invariantes

- **PA-08 — invariante etica central.** A defesa tecnica **nunca** vira obstrucao:
  o plugin jamais orienta a pratica de crime, a destruicao de prova, a fuga ou a
  coacao de testemunha. Essa proibicao nao admite bypass — nem por `--no-revisao`,
  nem por pedido explicito. Qualquer skill ou command novo tem de respeita-la.
- **Limite de 11264 bytes por `SKILL.md`.** Skills maiores que isso nao carregam.
  Ao crescer uma skill, fatiar conteudo para `context/` ou para arquivos auxiliares.
- **`name:` no frontmatter da skill = nome da pasta.** Se renomear a pasta,
  atualizar o `name:`; eles tem que bater.
- **Tokens de persona literais em disco.** A persona renderizada
  (`<cwd>/criminal/persona.md`) guarda os valores ja resolvidos; as skills
  resolvem placeholders `{{...}}` a partir dela. Nao hardcodar identidade de
  escritorio nas skills.
- **Nao versionar casos (sigilo reforcado).** `criminal/`, `casos/`, `CASO.md`,
  `arquivos/` ficam no `.gitignore` — dado penal **sensivel** (LGPD art. 11) +
  sigilo profissional da defesa. Nunca remover essas entradas.

## Convencoes de entrega

- **Nomenclatura de arquivos novos:** `AAAA-MM-DD - Cliente - tipo.ext`
  (ex.: `2026-06-16 - Fulano - habeas corpus liberatorio.txt`).
- **Entrega em `.txt` por padrao** (economia de tokens). Gerar `.docx`/`.pdf`
  somente a pedido explicito.

## Como adicionar uma skill nova

1. Criar `skills/<nome>/SKILL.md` com frontmatter (`name: <nome>` igual a pasta,
   `description:` com gatilhos claros). Respeitar o limite de 11264 bytes.
2. Se for Tier 2 (producao), encerrar sempre roteando para `revisao-final-criminal`
   e respeitar a PA-08.
3. Registrar a skill no `README.md` (lista por Tier) e, se tiver comando
   proprio, criar o command correspondente.

## Como adicionar um command novo

1. Criar `commands/<nome>.md` no gabarito padrao: frontmatter
   (`description`, `allowed-tools: Read, Write, Edit, Bash, Glob, Grep`,
   `argument-hint`) + corpo curto em portugues com `## PROTOCOLO` e a linha final
   **Skill a acionar:** `<skill>`.
2. Um command e fino: valida pre-condicoes, aciona UMA skill principal e referencia
   as Proibicoes Absolutas por codigo (PA-04, PA-05, PA-06, PA-08, ...). A logica
   pesada vive na skill, nao no command.
3. Comandos de producao defensiva priorizam a liberdade quando ha pessoa presa.
4. Atualizar a tabela de comandos do `README.md`.

## Engine

- **`scripts/state.py`** — maquina de estados do `cowork-state.json`.
  CLI: `python scripts/state.py init <cowork>` e `... set <cowork> <json_path> <value>`.
- **`scripts/resolve-persona.py`** / **`hook-utils.py`** — resolucao da persona
  e utilitarios de hook.
- **Pasta de estado (STATE_DIR):** `criminal/`.
- **Variaveis de ambiente do engine:** `CRIM_PERSONA` (caminho da persona.md),
  `CRIM_COWORK_PATH` (raiz do workspace), `CRIM_STATE_FILE` (cowork-state.json).
- **`hooks/`** — o SessionStart injeta a persona em toda sessao. Nao mover nem
  renomear sem ajustar o manifesto/hook.

## Ao mexer no manifesto

`/.claude-plugin/plugin.json` controla `name`, `version` e `description`. Subir a
`version` a cada release com mudanca relevante.
