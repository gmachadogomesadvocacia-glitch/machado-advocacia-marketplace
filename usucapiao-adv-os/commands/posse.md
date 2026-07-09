---
description: Analise da POSSE ad usucapionem.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [historico da posse]
---

Voce foi acionado pelo comando `/posse` do plugin usucapiao-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** analisar a posse e definir a modalidade (Protocolo P4).

## PROTOCOLO
1. **Acionar a skill `analise-posse-usucapiao`** — verifica: tempo de posse (+ accessio possessionis); qualidade (mansa, pacifica, continua, ininterrupta, com ANIMUS DOMINI — PA-08); POSSE x DETENCAO (comodatario/locatario/permissionario nao usucapem — PA-09); justo titulo + boa-fe (ordinaria); metragem/destinacao; nao ser proprietario de outro imovel (especiais).
2. **Saida:** modalidade(s) cabivel(eis) + requisitos atendidos/faltantes + tempo necessario. Alimenta `linha-estrategica-usucapiao` e a peca.
3. Marcar `[INFORMAR]` o que faltar; sem opinar alem dos fatos (PA-03).

**Skill a acionar:** `analise-posse-usucapiao`.
