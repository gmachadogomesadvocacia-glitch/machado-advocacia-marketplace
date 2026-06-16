---
description: Dispara a auditoria R1-R4 (Suprema Corte do plugin) sobre uma peca, parecer, contrato ou calculo imobiliario antes da entrega. Obrigatoria por default.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [arquivo ou peca a auditar]
---

Voce foi acionado pelo comando `/revisao-final` do plugin imobiliario-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** submeter o documento produzido a auditoria R1-R4 antes de entregar ao operador (PA-13).

## PROTOCOLO
1. **Acionar a skill `revisao-final-imobiliaria`** — executar as quatro rodadas:
   - **R1** coleta de dados (matricula, contrato, notificacoes, valores e prazos do `CASO.md`).
   - **R2** base juridica (norma vigente no contrato/fato — PA-04; posse x propriedade x dominio — PA-05; liminar de despejo so art. 59 §1º + caucao — PA-06; renovatoria art. 51 §5º — PA-07; cumulacao de garantias vedada art. 37 — PA-08; rito da alienacao fiduciaria — PA-09; jurisprudencia validada — PA-01; polo — PA-10; foro/registro/rito).
   - **R3** tese (fato-nexo-direito, antecipacao adversarial, coerencia de polo).
   - **R4** completude (estilo do tipo de peca, tom, pedido determinado, valor da causa, prazo correto).
2. **Emitir veredito** por rodada — APROVADO / APROVADO COM RESSALVAS / REPROVADO. Reprovacao em qualquer rodada bloqueia a entrega e devolve ao produtor.
3. **Selo P1** — confirmar que toda norma e jurisprudencia citada passou pela validacao de vigencia (PA-11).
4. Bypass apenas por demanda explicita: `--no-revisao`, `--quick` (R1+R2), `/revisao off`.

**Skill a acionar:** `revisao-final-imobiliaria`.
