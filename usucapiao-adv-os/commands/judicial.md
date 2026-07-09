---
description: Via JUDICIAL.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [dados do imovel/posse]
---

Voce foi acionado pelo comando `/judicial` do plugin usucapiao-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** redigir a acao judicial de usucapiao.

## PROTOCOLO
1. Confirmar triagem + Selo P1 + analise de posse (modalidade) + linha estrategica (via judicial).
2. **Acionar a skill `acao-usucapiao`** — inicial com qualificacao, descricao do imovel, causa de pedir (posse ad usucapionem + modalidade), **rol completo de citacoes** (confrontantes + titulares + Uniao/Estado/Municipio + edital — CPC 246§3/259 III — PA-06), planta/memorial com ART, e pedidos (declaracao do dominio + registro no RI).
3. Foro = situacao do imovel (P5). Bem nao publico (PA-04). Articular `estilo-juridico-usucapiao`.
4. Submeter a `revisao-final-usucapiao` (R1-R4).

**Skill a acionar:** `acao-usucapiao`.
