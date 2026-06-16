---
description: Acionamento direto do nucleo SERVICOS REGULADOS — telecom, energia, agua e transporte aereo. Roteia para a acao judicial e a reclamacao administrativa na agencia (ANATEL/ANAC/ANEEL/agencia).
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [resumo da demanda de servico regulado]
---

Voce foi acionado pelo comando `/servicos-regulados` do plugin consumidor-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** conduzir a demanda de servico regulado pelo pipeline e coordenar a frente judicial com a administrativa na agencia reguladora.

## PROTOCOLO

1. **Verificar configuracao** — procurar `consumidor/cowork-state.json` subindo a arvore. Se ausente, sugerir `/start-consumidor`.
2. **Acionar brevemente `consumidor-master`** (Tier 0) para a governanca.
3. **Acionar a `triagem-consumidor`** (4D) para fixar polo, esfera e rito e gravar no `CASO.md`.
4. **Rotear** conforme o subdominio:
   - telecom/energia/agua → `acao-telecom-servicos`;
   - transporte aereo (atraso, cancelamento, bagagem, overbooking) → `acao-transporte-aereo`;
   - e a `reclamacao-administrativa` na agencia competente (ANATEL/ANAC/ANEEL/agencia estadual ou consumidor.gov.br).
5. **Cruzamento multi-esfera (P4):** coordenar a via administrativa com a judicial sem contradicao, usando a reclamacao como prova — via `timeline-consumidor`.
6. **Guardas:** lei especial do setor conferida no Selo P1; sem protocolo/fatura/print, sinalizar `[INFORMAR]` (PA-15).
7. Antes da entrega, lembrar a Revisao R1-R4 (`revisao-final-consumidor`, PA-22).

**Skill a acionar:** `consumidor-master` -> `triagem-consumidor` -> `acao-telecom-servicos` / `acao-transporte-aereo` + `reclamacao-administrativa`.
