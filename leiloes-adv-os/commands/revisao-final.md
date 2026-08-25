---
description: Auditoria R1-R4 antes de entregar.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [arquivo]
---

Voce foi acionado pelo comando `/revisao-final` do plugin leiloes-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** auditar a entrega antes de sair do escritorio.

## PROTOCOLO
1. Acionar `revisao-final-leiloes`.
2. Rodar as quatro passadas na ordem: **R1 verdade** (norma vigente, Tema com modulacao, Tema 886 como em revisao, fato com documento, nenhuma promessa de resultado) — **bloqueante**; **R2 coerencia** (lado do arrematante, regime certo, rito certo, pedido compativel com a fase); **R3 completude** (ancoragem, prazos conferidos no documento, onus um a um, impedidos conferidos); **R4 forma** (anti-rastro de IA, tipografia, negrito, 1 paragrafo = 1 linha, nome do arquivo com a data).
3. **Rodar o linter**: `py ferramentas\linter-peticoes\linter_peticao.py "<peca>.txt" --corpus --salvar`. ERRO zera a entrega.
4. Fechar com veredito unico: **APROVADO** · **APROVADO COM AJUSTES** (listados) · **REPROVADO** (com o que refazer).

**Skill a acionar:** `revisao-final-leiloes`.
