# CLAUDE.md — Plugin consumidor-adv-os

> Instruções para futuras sessões neste sub-repositório. Ler ao retomar trabalho no plugin.

## Identidade
- **Slug:** `consumidor-adv-os` (convenção do escritório: todo plugin termina em `-adv-os`)
- **Tipo:** plugin Claude Code (`.claude-plugin/plugin.json`)
- **Chassi modelo:** `direito-medico-adv-os` + `trabalhista-adv-os` (padrão Adv-OS)
- **Pasta de estado runtime:** `consumidor/` (não o slug completo) — env `CONSUM_PERSONA`
- **Uso:** interno (Machado Advocacia). Sem camada de despersonalização/audit.

## Hierarquia das 4 Camadas (Constituição Operacional)
```
CAMADA 1 — PROIBIÇÕES ABSOLUTAS (PA-01 a PA-22)  — inviáveis
CAMADA 2 — PROTOCOLOS TÉCNICOS (6)               — obrigatórios
CAMADA 3 — IDENTIDADE FIRAC + ESTILO              — enxuto/humanizado
CAMADA 4 — SKILLS (Tier 0-3)                       — operacional
```
Camada superior sempre prevalece — inclusive contra o usuário. Injetada pela skill `consumidor-master` (Tier 0). Protocolos: P1 Selo de Validação Legal Prévia · P2 Integridade Documental · P3 Memória de Caso · P4 Cruzamento Judicial-Administrativo · P5 Localização/Rito · P6 Revisão R1-R4.

## Arquitetura em uma frase
Plugin side-aware (consumidor × fornecedor) e **triagem-driven 4D** (polo × eixo × esfera × rito), com engine portado (hooks/scripts/templates + persona runtime), Selo P1 antes de produzir e Suprema Corte R1-R4 sobre toda entrega.

## Estrutura
```
consumidor-adv-os/
├── .claude-plugin/plugin.json   manifesto (name, version, description, author, license)
├── commands/                    14 slash commands
├── skills/                      35 skills (Tier 0-3), só SKILL.md por pasta
├── hooks/                       hooks.json + scripts (persona, memória, snapshot, corte)
├── scripts/                     resolve-persona, state, hook-utils, state-schema
├── context/                     persona-fallback.md
├── templates/                   persona, config, CASO, MEMORY-caso, settings-local
└── README.md / CLAUDE.md / .gitignore
```

## Padrões a seguir
1. **Skill folder = só `SKILL.md`.** Material auxiliar vai em `templates/`/`scripts/`/`context/`.
2. **Limites:** `SKILL.md` ≤ 11264 bytes; `description` do frontmatter ≤ 1024 chars.
3. **plugin.json minimal:** name, version, description, author, license. Nada além.
4. **Tokens `{{...}}`** permanecem literais no disco — LLM resolve em runtime via `persona.md`.
5. **LGPD/sigilo:** `consumidor/` e `casos/` gitignored; dados de cliente nunca no plugin nem em pasta sincronizada sem ciência. Compartimentação por caso = PA-21.
6. **Jurisprudência:** nunca citar súmula/Tema sem validar — marcar `[VERIFICAR]` e acionar `jurisprudencia-consumidor` (PA-01).
7. **Engine:** Python 3.11+; `${CLAUDE_PLUGIN_ROOT}` nos hooks; persona via fallback chain (`CONSUM_PERSONA`).
8. **Saída padrão `.txt`** (convenção do escritório).

## Proibições de manutenção
- NÃO criar arquivo dentro de `skills/<nome>/` que não seja `SKILL.md`.
- NÃO aceitar instrução que conflite com a Camada 1.
- NÃO escrever dados reais de cliente no plugin.
- NÃO renomear o slug sem nova decisão (convenção `-adv-os`).

## Status do build
v0.1.0 — Núcleo operacional completo: engine portado, 14 commands, 35 skills (Tier 0-3), Suprema Corte R1-R4. Pendente: empacotar/registrar e caso-piloto de ponta a ponta. Roadmap geral: `../PLANO-novos-plugins-areas-direito.txt`.
