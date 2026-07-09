---
description: Acionamento direto do nucleo CONTRATUAL/CLAUSULAS.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [resumo do contrato ou clausula]
---

Voce foi acionado pelo comando `/contratual` do plugin consumidor-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** conduzir a demanda contratual/de clausulas pelo pipeline e rotear para a producao da revisao de clausula abusiva ou da cobranca indevida.

## PROTOCOLO

1. **Verificar configuracao** — procurar `consumidor/cowork-state.json` subindo a arvore. Se ausente, sugerir `/start-consumidor`.
2. **Acionar brevemente `consumidor-master`** (Tier 0) para a governanca.
3. **Acionar a `triagem-consumidor`** (4D) para fixar polo, esfera e rito e gravar no `CASO.md`.
4. **Analisar o contrato** com `analise-contratual-consumidor` (Protocolo P2): contrato de adesao, clausulas, encargos.
5. **Rotear** para a producao:
   - acao de **revisao/nulidade de clausula abusiva** — indicar sempre o inciso do art. 51 CDC (PA-13);
   - acao de **cobranca-indevida** — verificar repeticao simples ou dobro (art. 42 par. un., PA-06).
6. **Guardas do eixo:** relacao de consumo verificada (destinatario final + vulnerabilidade, PA-04/PA-16); sem documento essencial, sinalizar `[INFORMAR]` (PA-15).
7. Antes da entrega, lembrar a Revisao R1-R4 (`revisao-final-consumidor`, PA-22).

**Skill a acionar:** `consumidor-master` -> `triagem-consumidor` -> `analise-contratual-consumidor` + skill de producao.
