---
description: Dispara a auditoria R1-R4 (Suprema Corte do plugin) sobre uma peca, defesa, parecer ou calculo antes da entrega.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [arquivo ou peca a auditar]
---

Voce foi acionado pelo comando `/revisao-final` do plugin tributario-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** submeter o documento produzido a auditoria R1-R4 antes de entregar ao operador.

## PROTOCOLO
1. **Acionar a skill `revisao-final-tributaria`** — executar as quatro rodadas:
   - **R1** coleta de dados (documentos, fato gerador, valores do `CASO.md`).
   - **R2** base juridica (norma vigente no fato gerador + transicao da Reforma — PA-04; decadencia x prescricao — PA-05; jurisprudencia validada — PA-01; polo — PA-10; foro/orgao/rito).
   - **R3** tese (fato-nexo-direito, antecipacao adversarial, coerencia de polo; elisao x evasao — PA-06).
   - **R4** completude (estilo do tipo de peca, tom, pedido determinado, prazo correto).
2. **Emitir veredito** por rodada — APROVADO / APROVADO COM RESSALVAS / REPROVADO. Reprovacao em qualquer rodada bloqueia a entrega e devolve ao produtor.
3. **Selo P1** — confirmar que toda norma e jurisprudencia citada passou pela validacao de vigencia (PA-11).
4. Bypass apenas por demanda explicita: `--no-revisao`, `--quick` (R1+R2), `/revisao off`.

**Skill a acionar:** `revisao-final-tributaria`.
