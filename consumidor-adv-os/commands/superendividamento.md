---
description: Acionamento direto do nucleo SUPERENDIVIDAMENTO.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [resumo da situacao de endividamento]
---

Voce foi acionado pelo comando `/superendividamento` do plugin consumidor-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** conduzir a demanda de superendividamento pelo pipeline e rotear para a producao da repactuacao com preservacao do minimo existencial.

## PROTOCOLO

1. **Verificar configuracao** — procurar `consumidor/cowork-state.json` subindo a arvore. Se ausente, sugerir `/start-consumidor`.
2. **Acionar brevemente `consumidor-master`** (Tier 0) para a governanca.
3. **Acionar a `triagem-consumidor`** (4D) para fixar polo, esfera e rito e gravar no `CASO.md`.
4. **Rotear** para `acao-superendividamento`: plano de pagamento, repactuacao em bloco e audiencia conciliatoria global (Lei 14.181/2021).
5. **Guarda nuclear (PA-14):** preservar sempre o **minimo existencial** (Lei 14.181 + Dec. 11.150/2022) — nenhuma proposta pode comprometer a subsistencia do consumidor.
6. **Insumos:** mapa de dividas, contratos, comprovantes de renda e despesas essenciais; sem eles, sinalizar `[INFORMAR]` (PA-15) e calcular o disponivel via `calculos-consumidor`.
7. Antes da entrega, lembrar a Revisao R1-R4 (`revisao-final-consumidor`, PA-22).

**Skill a acionar:** `consumidor-master` -> `triagem-consumidor` -> `acao-superendividamento`.
