---
description: Submete uma peca, parecer ou calculo ja produzido a auditoria final R1-R4 (Suprema Corte do plugin) antes da entrega.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [arquivo ou peca a auditar] [--no-corte|--quick]
---

Voce foi acionado pelo comando `/revisao-final-consumidor` do plugin consumidor-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** auditar todo documento produzido em 4 rodadas obrigatorias antes de entregar ao operador. Reprovacao em qualquer rodada bloqueia a entrega.

## PROTOCOLO

1. **Verificar configuracao** — procurar `consumidor/cowork-state.json` subindo a arvore. Se ausente, sugerir `/start-consumidor`.
2. **Acionar brevemente `consumidor-master`** (Tier 0) para confirmar as Proibicoes Absolutas e o Protocolo P6.
3. **Acionar a skill `revisao-final-consumidor`** e correr as 4 rodadas:
   - **R1 Coleta** — documentos analisados? Selo P1 emitido? Pontos `[INFORMAR]` sinalizados (PA-15)?
   - **R2 Base juridica** — CDC/lei especial vigente? jurisprudencia validada (PA-01)? Sumula 385/530/539 conferidas? prazos (PA-11)? competencia/rito (PA-19)?
   - **R3 Tese** — FATO-NEXO-DIREITO amarrados? inversao do onus fundamentada (PA-12)? dobro do art. 42 justificado (PA-06)? coerencia de polo (PA-05)?
   - **R4 Completude** — estilo do tipo de peca? tom? valor da causa? pedido determinado e dano moral quantificado?
4. **Emitir** por rodada: APROVADO / APROVADO COM RESSALVAS / REPROVADO. Nenhum documento sai sem R1-R4.
5. **Bypass** apenas com `--no-corte` (pula a auditoria) ou `--quick` (R1+R2), explicito e registrado em log.

**Skill a acionar:** `revisao-final-consumidor`.
