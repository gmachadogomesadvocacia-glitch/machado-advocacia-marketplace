# CLAUDE.md — Plugin isencao-ir-doenca-adv-os

> Instruções para futuras sessões neste sub-repositório.

## Identidade
- **Slug:** `isencao-ir-doenca-adv-os` (convenção: todo plugin termina em `-adv-os`)
- **Chassi modelo:** `consumidor-adv-os` / `direito-medico-adv-os` (padrão Adv-OS)
- **Pasta de estado runtime:** `isencao-ir/` — env `ISIR_PERSONA`
- **Uso:** interno (Machado Advocacia). Sem camada de despersonalização/audit.
- **Posição no roadmap:** plugin ANTECIPADO (alta prioridade), após a migração dos legados.

## Hierarquia das 4 Camadas
```
CAMADA 1 — PROIBICOES ABSOLUTAS (PA-01 a PA-14)  — inviáveis
CAMADA 2 — PROTOCOLOS TECNICOS (6)               — obrigatórios
CAMADA 3 — IDENTIDADE FIRAC + ESTILO              — tributário, sensível (cliente doente)
CAMADA 4 — SKILLS (Tier 0-3)                       — operacional
```
Injetada pela skill `isencao-ir-master` (Tier 0). Protocolos: P1 Selo de Validação Legal · P2 Integridade Documental · P3 Memória de Caso · P4 Cruzamento Administrativo-Judicial · P5 Foro/Rito · P6 R1-R4.

## Arquitetura em uma frase
Plugin side-aware (contribuinte × Fazenda/fonte) para a isenção de IRPF por doença grave (art. 6 XIV Lei 7.713/88), vias administrativa e judicial, com engine de persona em runtime e Suprema Corte R1-R4.

## Padrões a seguir
1. Skill folder = só `SKILL.md`. Material auxiliar em `templates/`/`scripts/`/`context/`.
2. `SKILL.md` ≤ 11264 bytes; `description` ≤ 1024 chars.
3. plugin.json minimal: name, version, description, author, license.
4. Tokens `{{...}}` literais no disco — resolvidos em runtime via `persona.md`.
5. **PA-04:** NUNCA opinar sobre conduta clínica/diagnóstico — o laudo é do médico; o plugin é jurídico.
6. **PA-10 / LGPD reforçada:** dado de saúde é SENSÍVEL (art. 11 LGPD + sigilo). `isencao-ir/` e `casos/` gitignored; laudo/CID nunca no plugin nem em pasta sincronizada.
7. Isenção só sobre PROVENTOS (PA-06); doença só do rol taxativo (PA-05); restituição só 5 anos (PA-09).
8. Jurisprudência: nunca citar Súmula/Tema sem validar (PA-01) — Súm. 598 e 627 STJ são as âncoras.

## Status do build
v0.1.0 — Núcleo operacional: engine, 10 commands, ~16 skills (Tier 0-3), Suprema Corte R1-R4. Roadmap geral: `../PLANO-novos-plugins-areas-direito.txt`.
