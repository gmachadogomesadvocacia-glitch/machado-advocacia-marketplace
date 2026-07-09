---
description: Calculos consumeristas/bancarios.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [tipo de calculo e dados-base]
---

Voce foi acionado pelo comando `/calculos-consumidor` do plugin consumidor-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** produzir o calculo consumerista/bancario correto, discriminado e auditavel, sempre a partir de dado-base real.

## PROTOCOLO

1. **Verificar configuracao** — procurar `consumidor/cowork-state.json` subindo a arvore. Se ausente, sugerir `/start-consumidor`.
2. **Acionar brevemente `consumidor-master`** (Tier 0) para a governanca e o polo do cliente.
3. **Acionar a skill `calculos-consumidor`** conforme o pedido:
   - revisional bancaria (juros, capitalizacao, expurgo de encargos);
   - repeticao de indebito simples ou em dobro (art. 42 par. un. + Tema 929 STJ);
   - expurgo de tarifas abusivas (TAC/TEC, seguros embutidos);
   - quantificacao de dano moral.
4. **PA-15/PA-20 — nunca calcular sem dado-base:** exigir contrato, fatura, extrato ou comprovante. Sem o documento essencial, sinalizar `[INFORMAR]` e nao estimar em silencio.
5. **Dobro do art. 42 (PA-06):** so quando houver cobranca indevida efetiva + engano injustificavel; do contrario, indebito simples.
6. **Juros/capitalizacao:** exigir taxa media BACEN (Sum. 530/382) e previsao contratual expressa (Sum. 539/541) — nada de comparativo solto (PA-08/PA-09).
7. Entregar planilha discriminada e, antes da entrega, lembrar a Revisao R1-R4 (`revisao-final-consumidor`, PA-22).

**Skill a acionar:** `calculos-consumidor`.
