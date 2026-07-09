---
description: Responsabilidade civil do Estado / Fazenda Publica.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [resumo do dano e do ente causador]
---

Voce foi acionado pelo comando `/resp-estado` do plugin civel-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** conduzir a demanda de responsabilidade civil do Estado pelo pipeline e produzir a peca do lado do cliente.

## PROTOCOLO
1. **Verificar configuracao** — procurar `civel/cowork-state.json` subindo a arvore. Se ausente, sugerir `/start-civel`.
2. **Acionar brevemente `civel-master`** (Tier 0) para a governanca; checar PA-09 — se o dano envolver materia previdenciaria, tributaria ou medica de hospital publico com eixo proprio, avaliar a interface com o plugin especifico.
3. **Acionar a `triagem-civel`** para fixar polo (lesado/autor x ente publico/reu; ou agente, no regresso), relacao/fato e prazo, e gravar no `CASO.md`.
4. **Qualificar (CF 37 §6º):** responsabilidade **objetiva** por ato comissivo (teoria do risco administrativo) — basta conduta-nexo-dano; nas **omissoes**, discutir a responsabilidade subjetiva/faute du service conforme o caso. Tratar excludentes (caso fortuito, forca maior, culpa exclusiva da vitima).
5. **Liquidar (PA-06):** danos material, moral e estetico; juros e correcao no regime da Fazenda Publica.
6. **Prazo e foro (PA-05/PA-08):** prescricao quinquenal contra a Fazenda (Dec. 20.910/32; observar discussao Tema 553 STJ); foro/competencia conforme o ente (Justica Estadual x Federal — art. 109 CF); cabivel o regresso contra o agente em dolo/culpa.
7. **Rotear** para `responsabilidade-estado` e, antes da entrega, lembrar a Revisao R1-R4 (`revisao-final-civel`).

**Skill a acionar:** `responsabilidade-estado`.
