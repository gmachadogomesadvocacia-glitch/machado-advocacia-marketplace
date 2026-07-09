---
description: Defesa na investigacao/flagrante.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao do caso]
---

Voce foi acionado pelo comando `/flagrante` do plugin criminal-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** atuar na fase de investigacao/flagrante para libertar o cliente ou conter a custodia, na audiencia de custodia e nos pedidos correlatos.

## PROTOCOLO
1. **Conferir a triagem** — exigir `CASO.md` com polo (defesa), situacao prisional, crime/tipificacao e prazo. Sem triagem, acionar `/triagem` antes.
2. **Prioridade a liberdade** — fase de urgencia maxima; mapear a decisao do art. 310 CPP (relaxamento da prisao ilegal; conversao em preventiva; concessao de liberdade provisoria com ou sem fianca).
3. **Atacar o flagrante** — verificar legalidade do auto (especie de flagrante, comunicacao em 24h, nota de culpa), nulidades e cabimento de relaxamento.
4. **Acionar a skill `defesa-investigacao-flagrante`** — preparar a audiencia de custodia, requerer liberdade provisoria / fianca / cautelares diversas da prisao (CPP 319), antecipando a manifestacao do MP.
5. **Garantias e norma** — garantias constitucionais (PA-07), lei penal vigente no tempo do fato (PA-04); jamais orientar destruicao de prova, fuga ou coacao de testemunha (PA-08).
6. Ao final, submeter a `revisao-final-criminal` (R1-R4) antes da entrega.

**Skill a acionar:** `defesa-investigacao-flagrante`.
