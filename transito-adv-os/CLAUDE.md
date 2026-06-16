# CLAUDE.md — manutencao do plugin transito-adv-os

Instrucoes para quem (humano ou Claude) for editar este plugin. Curtas e
praticas. Para o uso pelo operador, ver `README.md`.

## Estrutura de pastas

```
transito-adv-os/
├── .claude-plugin/plugin.json   # manifesto (name, version, description)
├── commands/                    # 13 slash-commands (.md, frontmatter + corpo curto)
├── skills/<nome>/SKILL.md       # 20 skills, uma pasta por skill
├── templates/                   # persona.md.tpl, config.md.tpl, CASO.md.tpl, ...
├── scripts/                     # engine: state.py, resolve-persona.py, hook-utils.py
├── hooks/                       # SessionStart (injeta a persona) e outros
├── context/                     # contexto compartilhado entre skills
├── .gitignore                   # ignora transito/, casos/, CASO.md, arquivos/
├── README.md
└── CLAUDE.md                    # este arquivo
```

## Regras invariantes

- **PA-06 — invariante etica central.** A defesa legitima **nunca** vira fraude de
  pontuacao: o plugin jamais orienta indicacao falsa de condutor nem manobra para
  "passar pontos" a terceiro (crime de falsidade ideologica, art. 299 CP). Em
  `/indicar-condutor`, so se indica o **condutor real**. Essa proibicao nao admite
  bypass — nem por `--no-revisao`, nem por pedido explicito. Toda skill/command novo
  tem de respeita-la.
- **PA-05 — prazos preclusivos.** As vias administrativas tem **30 dias**. Perdido o
  prazo, perde-se a instancia. A triagem e o status tratam isso como prioridade
  maxima; todo command de producao confere o prazo antes de redigir.
- **PA-04 — norma vigente na infracao.** Sempre aplicar o CTB/Resolucao vigente na
  **data da infracao**, validado pelo Selo P1.
- **Limite de 11264 bytes por `SKILL.md`.** Skills maiores nao carregam. Ao crescer
  uma skill, fatiar conteudo para `context/` ou arquivos auxiliares.
- **`name:` no frontmatter da skill = nome da pasta.** Se renomear a pasta, atualizar
  o `name:`; eles tem que bater.
- **Tokens de persona literais em disco.** A persona renderizada
  (`<cwd>/transito/persona.md`) guarda os valores ja resolvidos; as skills resolvem
  placeholders `{{...}}` a partir dela. Nao hardcodar identidade de escritorio nas
  skills.
- **Nao versionar casos (sigilo + LGPD).** `transito/`, `casos/`, `CASO.md`,
  `arquivos/` ficam no `.gitignore` — dados pessoais do condutor + sigilo
  profissional OAB. Nunca remover essas entradas.

## Convencoes de entrega

- **Nomenclatura de arquivos novos:** `AAAA-MM-DD - Cliente - tipo.ext`
  (ex.: `2026-06-16 - Fulano - recurso JARI.txt`).
- **Entrega em `.txt` por padrao** (economia de tokens). Gerar `.docx`/`.pdf` somente
  a pedido explicito.

## Como adicionar uma skill nova

1. Criar `skills/<nome>/SKILL.md` com frontmatter (`name: <nome>` igual a pasta,
   `description:` com gatilhos claros). Respeitar o limite de 11264 bytes.
2. Se for Tier 2 (producao), encerrar sempre roteando para `revisao-final-transito` e
   respeitar a PA-06 (sem fraude de pontuacao) e a PA-05 (prazo preclusivo).
3. Registrar a skill no `README.md` (lista por Tier) e, se tiver comando proprio,
   criar o command correspondente.

## Como adicionar um command novo

1. Criar `commands/<nome>.md` no gabarito padrao: frontmatter (`description`,
   `allowed-tools: Read, Write, Edit, Bash, Glob, Grep`, `argument-hint`) + corpo curto
   em portugues com `## PROTOCOLO` e a linha final **Skill a acionar:** `<skill>`.
2. Um command e fino: valida pre-condicoes, aciona UMA skill principal e referencia as
   Proibicoes Absolutas por codigo (PA-04, PA-05, PA-06, PA-07, PA-08, ...). A logica
   pesada vive na skill, nao no command.
3. Comandos administrativos conferem o prazo de 30 dias (PA-05); comandos judiciais
   fixam esfera/competencia (estadual x federal, art. 109 CF) sem confundir instancias
   (PA-08).
4. Atualizar a tabela de comandos do `README.md`.

## Engine

- **`scripts/state.py`** — maquina de estados do `cowork-state.json`.
  CLI: `python scripts/state.py init <cowork>` e `... set <cowork> <json_path> <value>`.
- **`scripts/resolve-persona.py`** / **`hook-utils.py`** — resolucao da persona e
  utilitarios de hook.
- **Pasta de estado (STATE_DIR):** `transito/`.
- **Variaveis de ambiente do engine:** `TRAN_PERSONA` (caminho da persona.md),
  `TRAN_COWORK_PATH` (raiz do workspace), `TRAN_STATE_FILE` (cowork-state.json).
- **`hooks/`** — o SessionStart injeta a persona em toda sessao. Nao mover nem renomear
  sem ajustar o manifesto/hook.

## Ao mexer no manifesto

Manter `name` = `transito-adv-os` e a `description` alinhada com os 3 eixos + analise,
as 20 skills, as 13 PA e as interfaces (crime de transito -> `criminal-adv-os`;
reparacao civil/DPVAT -> `civel-adv-os`).
