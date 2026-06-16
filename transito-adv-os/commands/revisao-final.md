---
description: Dispara a auditoria R1-R4 (Suprema Corte do plugin) sobre uma peca, defesa, recurso ou parecer antes da entrega — inclui a checagem inegociavel da PA-06. Obrigatoria por default.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [arquivo ou peca a auditar]
---

Voce foi acionado pelo comando `/revisao-final` do plugin transito-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** submeter o documento produzido a auditoria R1-R4 antes de entregar ao operador.

## PROTOCOLO
1. **Acionar a skill `revisao-final-transito`** — executar as quatro rodadas:
   - **R1** coleta de dados (auto de infracao, notificacoes, datas, pontuacao e prazos do `CASO.md`).
   - **R2** base juridica (norma de transito vigente na data da infracao — PA-04; prazo administrativo preclusivo de 30 dias — PA-05; dupla notificacao Sum. 312 STJ — PA-07; instancia correta — PA-08; jurisprudencia validada — PA-01; polo defesa — PA-10; foro/orgao/competencia).
   - **R3** tese (vicio formal do auto, fato-nexo-direito, antecipacao adversarial, coerencia de polo).
   - **R4** completude (estilo do tipo de peca, tom, pedido determinado, prazo e instancia corretos).
2. **Checagem inegociavel da PA-06** — confirmar que nada na peca orienta fraude de pontuacao ou indicacao falsa de condutor (crime art. 299 CP). A defesa legitima nunca vira fraude; violacao bloqueia a entrega de imediato.
3. **Emitir veredito** por rodada — APROVADO / APROVADO COM RESSALVAS / REPROVADO. Reprovacao em qualquer rodada bloqueia a entrega e devolve ao produtor.
4. **Selo P1** — confirmar que toda norma e jurisprudencia citada passou pela validacao de vigencia (PA-11).
5. Bypass apenas por demanda explicita: `--no-revisao`, `--quick` (R1+R2), `/revisao off` — jamais para a PA-06, que e inegociavel.

**Skill a acionar:** `revisao-final-transito`.
