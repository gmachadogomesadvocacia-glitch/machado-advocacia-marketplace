---
description: Redige a resposta a acusacao (CPP 396-A, prazo 10 dias).
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao do caso]
---

Voce foi acionado pelo comando `/resposta-acusacao` do plugin criminal-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** redigir a resposta a acusacao apos o recebimento da denuncia/queixa, suscitando preliminares e a absolvicao sumaria.

## PROTOCOLO
1. **Conferir a triagem** — exigir `CASO.md` com polo (defesa), crime/tipificacao, fase e prazo. Sem triagem, acionar `/triagem` antes.
2. **Validar prazo** — resposta a acusacao no prazo de 10 dias (CPP art. 396-A); registrar a data da citacao e o termo final.
3. **Mapear hipoteses de absolvicao sumaria** (CPP art. 397) — existencia manifesta de causa excludente da ilicitude/culpabilidade, fato atipico, extincao da punibilidade (inclusive prescricao — PA-05).
4. **Acionar a skill `resposta-acusacao`** — arguir todas as preliminares (inepcia da denuncia, ilicitude da prova, incompetencia, nulidades), especificar provas e arrolar testemunhas; antecipar a reacao do MP (postura adversarial dura).
5. **Garantias e norma** — garantias constitucionais (PA-07), lei penal vigente no tempo do fato (PA-04), jurisprudencia validada (PA-01); jamais orientar obstrucao (PA-08).
6. Ao final, submeter a `revisao-final-criminal` (R1-R4) antes da entrega.

**Skill a acionar:** `resposta-acusacao`.
