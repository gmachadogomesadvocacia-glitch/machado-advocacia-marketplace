---
description: Aciona a Suprema Corte previdenciaria — auditoria R1-R4 obrigatoria sobre toda peca/parecer/calculo antes da entrega. Bypass apenas com --no-corte/--quick explicito.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [documento a auditar]
---

Voce foi acionado pelo comando `/revisao-final` do plugin previdenciario-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** submeter o documento a auditoria final R1-R4 antes da entrega.

## PROTOCOLO

1. **Acionar a skill `suprema-corte-previdenciaria`** — executa:
   - **R1** — Proibicoes Absolutas (PAs) + dados do caso conferidos
   - **R2** — Fundamentacao: norma vigente no marco temporal (EC 103), jurisprudencia validada (STF/STJ/TNU/CRPS), carencia/qualidade de segurado, prazos
   - **R3** — Auto-critica adversarial (a tese resiste a contestacao do INSS?)
   - **R4** — Semaforo final: APROVADO / APROVADO COM RESSALVAS / REPROVADO
2. **REPROVADO** bloqueia a entrega — apontar a falha exata e devolver ao produtor.
3. Bypass somente com `--no-corte` / `--quick` explicito, registrado.

**Skill a acionar:** `suprema-corte-previdenciaria`.
