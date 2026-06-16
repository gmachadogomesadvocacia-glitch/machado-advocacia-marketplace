---
description: Acionamento direto do nucleo BANCARIO/financeiro — revisional, busca e apreensao, repeticao de indebito, negativacao indevida. Roteia conforme o polo do cliente.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [resumo da demanda bancaria]
---

Voce foi acionado pelo comando `/bancario` do plugin consumidor-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** conduzir a demanda do eixo bancario/financeiro pelo pipeline e rotear para a skill de producao correta conforme o polo.

## PROTOCOLO

1. **Verificar configuracao** — procurar `consumidor/cowork-state.json` subindo a arvore. Se ausente, sugerir `/start-consumidor`.
2. **Acionar brevemente `consumidor-master`** (Tier 0) para a governanca (4 Camadas, Proibicoes).
3. **Acionar a `triagem-consumidor`** (4D) para fixar polo, esfera e rito e gravar no `CASO.md`.
4. **Rotear** conforme o polo e o pedido:
   - **consumidor:** `revisional-bancaria` (juros/capitalizacao/tarifas) · `acao-repeticao-indebito` · `acao-negativacao-indevida`;
   - **fornecedor:** `defesa-busca-apreensao` · `defesa-instituicao-financeira`.
5. **Guardas do eixo:** taxa media BACEN para juros (Sum. 530/382, PA-08); capitalizacao so com previsao expressa (Sum. 539/541, PA-09); Sumula 385 antes de dano moral por negativacao (PA-07); dobro do art. 42 so com engano injustificavel (PA-06).
6. Faltando contrato/extrato/fatura, sinalizar `[INFORMAR]` (PA-15), nunca inventar.
7. Antes da entrega, lembrar a Revisao R1-R4 (`revisao-final-consumidor`, PA-22).

**Skill a acionar:** `consumidor-master` -> `triagem-consumidor` -> skill de producao do eixo bancario.
