---
description: Atuacao no Tribunal do Juri.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao do caso]
---

Voce foi acionado pelo comando `/juri` do plugin criminal-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** atuar nas fases do procedimento do juri — primeira fase (judicium accusationis) e plenario (judicium causae).

## PROTOCOLO
1. **Conferir a triagem** — exigir `CASO.md` com polo (defesa x assistencia de acusacao — PA-10), crime doloso contra a vida, fase e prazo. Sem triagem, acionar `/triagem` antes.
2. **Situar a fase** — primeira fase: alegacoes apos instrucao buscando impronuncia (CPP 414), desclassificacao (CPP 419) ou absolvicao sumaria (CPP 415); segunda fase: preparacao do plenario.
3. **Acionar a skill `tribunal-do-juri`** — conforme a fase, redigir as alegacoes/recurso ou montar a estrategia de plenario (tese, ordem de testemunhas, debates) e revisar a **quesitacao** (CPP 482-490), garantindo coerencia com a tese do polo.
4. **Garantias e norma** — soberania dos veredictos, plenitude de defesa e demais garantias (PA-07); lei penal vigente no tempo do fato (PA-04); jurisprudencia validada (PA-01); jamais orientar coacao de testemunha ou jurado (PA-08).
5. Ao final, submeter a `revisao-final-criminal` (R1-R4) antes da entrega.

**Skill a acionar:** `tribunal-do-juri`.
