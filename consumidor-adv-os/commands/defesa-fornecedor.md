---
description: Acionamento direto do nucleo DEFESA DO FORNECEDOR (polo passivo).
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [resumo da acao a contestar]
---

Voce foi acionado pelo comando `/defesa-fornecedor` do plugin consumidor-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** conduzir a defesa do polo fornecedor pelo pipeline e rotear para a contestacao correta, com as preliminares e excludentes cabiveis.

## PROTOCOLO

1. **Verificar configuracao** — procurar `consumidor/cowork-state.json` subindo a arvore. Se ausente, sugerir `/start-consumidor`.
2. **Acionar brevemente `consumidor-master`** (Tier 0) para a governanca.
3. **Acionar a `triagem-consumidor`** (4D) — confirmar que o **polo do cliente e fornecedor** no `CASO.md`; toda tese flipa para a defesa (PA-05).
4. **Rotear** conforme o fornecedor:
   - generico (loja, operadora, prestador) → `contestacao-consumidor`;
   - banco/financeira → `defesa-instituicao-financeira` (e `defesa-busca-apreensao` quando for o caso).
5. **Guardas da defesa:** checar **prescricao** (art. 27) e **decadencia** (art. 26, PA-10/PA-11); arguir as **excludentes** de responsabilidade do fornecedor (art. 12 §3 / art. 14 §3 — culpa exclusiva, fato de terceiro, inexistencia do defeito); impugnar a inversao do onus (PA-12) e o dobro do art. 42 (PA-06); conferir a Sumula 385 contra dano moral por negativacao (PA-07).
6. Sem os autos/contrato, sinalizar `[INFORMAR]` (PA-15), nunca inventar fato.
7. Antes da entrega, lembrar a Revisao R1-R4 (`revisao-final-consumidor`, PA-22).

**Skill a acionar:** `consumidor-master` -> `triagem-consumidor` -> `contestacao-consumidor` / `defesa-instituicao-financeira`.
