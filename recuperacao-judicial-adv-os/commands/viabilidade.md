---
description: Nucleo VIABILIDADE.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [documentos da empresa em RJ]
---

Voce foi acionado pelo comando `/viabilidade` do plugin recuperacao-judicial-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** avaliar a viabilidade da RJ e a integridade documental.

## PROTOCOLO
1. **Acionar a skill `analise-viabilidade-rj`** — analisa a crise (economico-financeira), a viabilidade do soerguimento e os requisitos do pedido.
2. Articular `auditoria-documental-rj` para os documentos do art. 51 (demonstracoes contabeis, relacao de credores, balancos, extratos, certidoes) — identificar lacunas, inconsistencias, ativos ocultos e passivos contingentes.
3. Marcar `[VERIFICAR]` para dados/normas nao confirmados; submeter a `revisao-final-rj` se virar parecer.

**Skill a acionar:** `analise-viabilidade-rj`.
