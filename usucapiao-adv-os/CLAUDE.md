# CLAUDE.md — Plugin usucapiao-adv-os

> Instruções para futuras sessões neste sub-repositório.

## Identidade
- **Slug:** `usucapiao-adv-os` (convenção: `-adv-os`)
- **Chassi modelo:** `consumidor-adv-os` (padrão Adv-OS)
- **Pasta de estado runtime:** `usucapiao/` — env `USU_PERSONA`
- **Uso:** interno (Machado Advocacia). Sem despersonalização/audit.
- **Posição no roadmap:** Etapa C.

## Hierarquia das 4 Camadas
```
CAMADA 1 — PROIBICOES ABSOLUTAS (PA-01 a PA-13)  — inviáveis
CAMADA 2 — PROTOCOLOS TECNICOS (6)               — obrigatórios
CAMADA 3 — IDENTIDADE FIRAC + ESTILO              — imobiliário, técnico
CAMADA 4 — SKILLS (Tier 0-3)
```
Injetada por `usucapiao-master` (Tier 0). Protocolos: P1 Selo · P2 Documental · P3 Memória · P4 Análise de Posse · P5 Foro/RI · P6 R1-R4.

## Arquitetura em uma frase
Plugin side-aware (usucapiente × confrontante) para usucapião nas duas vias (judicial + extrajudicial/cartório), com tabela de modalidades, engine de persona em runtime e Suprema Corte R1-R4.

## Padrões a seguir
1. Skill folder = só `SKILL.md`. `SKILL.md` ≤ 11264 bytes; `description` ≤ 1024 chars.
2. plugin.json minimal: name, version, description, author, license.
3. Tokens `{{...}}` literais — resolvidos em runtime via `persona.md`.
4. **PA-04:** bem PÚBLICO não é usucapível (CF 183§3/191§ún; Súm. 340 STF).
5. **PA-05:** modalidade e requisitos corretos (tempo, metragem, justo título, boa-fé).
6. **PA-06:** no judicial, citar SEMPRE confrontantes + titulares + União/Estado/Município + edital de réus incertos.
7. **PA-07:** extrajudicial só com consenso; havendo litígio → judicial.
8. **PA-08/09:** posse ad usucapionem (animus domini), nunca detenção.
9. Jurisprudência: nunca citar sem validar (PA-01) — Súm. 391 e 340 STF são âncoras.

## Status do build
v0.1.0 — Núcleo operacional: engine, 10 commands, ~15 skills (Tier 0-3), Suprema Corte R1-R4. Roadmap geral: `../PLANO-novos-plugins-areas-direito.txt`.
