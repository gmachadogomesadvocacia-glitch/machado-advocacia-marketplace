---
description: Dispara a auditoria R1-R4 (Suprema Corte do plugin) sobre uma peca, defesa, recurso ou parecer antes da entrega — inclui a checagem inegociavel da PA-08. Obrigatoria por default.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [arquivo ou peca a auditar]
---

Voce foi acionado pelo comando `/revisao-final` do plugin criminal-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** submeter o documento produzido a auditoria R1-R4 antes de entregar ao operador.

## PROTOCOLO
1. **Acionar a skill `revisao-final-criminal`** — executar as quatro rodadas:
   - **R1** coleta de dados (documentos, situacao prisional, datas e valores do `CASO.md`).
   - **R2** base juridica (lei penal vigente no tempo do fato — PA-04; prescricao penal CP 109-110 — PA-05; dosimetria trifasica CP 68 — PA-06; jurisprudencia validada — PA-01; polo — PA-10; competencia/foro/rito/prazo recursal).
   - **R3** tese (fato-nexo-direito, antecipacao adversarial, coerencia de polo; garantias constitucionais — PA-07).
   - **R4** completude (estilo do tipo de peca, tom, pedido determinado, prazo correto).
2. **Checagem inegociavel da PA-08** — confirmar que nada na peca orienta crime, destruicao de prova, fuga ou coacao de testemunha. A defesa tecnica nunca vira obstrucao; violacao bloqueia a entrega de imediato.
3. **Emitir veredito** por rodada — APROVADO / APROVADO COM RESSALVAS / REPROVADO. Reprovacao em qualquer rodada bloqueia a entrega e devolve ao produtor.
4. **Selo P1** — confirmar que toda norma e jurisprudencia citada passou pela validacao de vigencia (PA-11).
5. Bypass apenas por demanda explicita: `--no-revisao`, `--quick` (R1+R2), `/revisao off` — jamais para a PA-08, que e inegociavel.

**Skill a acionar:** `revisao-final-criminal`.
