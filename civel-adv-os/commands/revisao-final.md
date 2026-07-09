---
description: Dispara a auditoria R1-R4 da Suprema Corte do plugin sobre uma peca/parecer/calculo civel ja produzido.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [arquivo ou peca a auditar]
---

Voce foi acionado pelo comando `/revisao-final` do plugin civel-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** submeter o documento a auditoria final R1-R4 antes da entrega.

## PROTOCOLO
1. **Verificar configuracao** — procurar `civel/cowork-state.json` subindo a arvore. Se ausente, sugerir `/start-civel`.
2. **Acionar a skill `revisao-final-civel`** (Tier 3) e auditar em 4 rodadas, cada uma emitindo APROVADO / APROVADO COM RESSALVAS / REPROVADO:
   - **R1 — dados e escopo:** documentos, qualificacao, polo coerente (PA-10), valor da causa.
   - **R2 — base juridica:** norma vigente a epoca do fato/contrato (PA-04), prescricao x decadencia (PA-05), responsabilidade contratual x extracontratual (PA-07), via/pedido adequado (PA-08), jurisprudencia validada.
   - **R3 — tese:** fato-nexo-direito, liquidacao do dano e juros (Sum. 54/362 STJ — PA-06), antecipacao adversarial.
   - **R4 — completude e entrega:** estilo do tipo de peca, tom, pedido determinado, clareza, ressalva OAB.
3. **Reprovacao em qualquer rodada bloqueia a entrega** e devolve ao produtor com as correcoes.
4. Bypass disponivel `--no-revisao` / `/revisao off` — registrar a opcao no `CASO.md`.

**Skill a acionar:** `revisao-final-civel`.
