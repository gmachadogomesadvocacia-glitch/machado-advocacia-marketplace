---
description: Impetra Habeas Corpus (CF 5 LXVIII; CPP 648) — liberdade, trancamento da acao/inquerito, relaxamento de prisao ilegal, excesso de prazo; liminar e Sum. 691 STF.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao do caso]
---

Voce foi acionado pelo comando `/habeas-corpus` do plugin criminal-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** redigir Habeas Corpus para tutelar a liberdade de locomocao ameacada ou violada por ilegalidade ou abuso de poder.

## PROTOCOLO
1. **Conferir a triagem** — exigir `CASO.md` com polo (defesa), crime/tipificacao, situacao prisional, autoridade coatora e prazo. Sem triagem, acionar `/triagem` antes.
2. **Prioridade a liberdade** — havendo pessoa presa, tratar como urgencia maxima; avaliar pedido de **liminar** e, quando aplicavel, o contorno da Sum. 691 STF (denegacao de liminar na origem).
3. **Identificar a hipotese** (CPP art. 648) — ausencia de justa causa, trancamento de inquerito/acao penal, relaxamento de prisao ilegal, excesso de prazo da custodia, nulidade do flagrante.
4. **Acionar a skill `habeas-corpus`** — fixar autoridade coatora e competencia, narrar a coacao ilegal, demonstrar o constrangimento e formular o pedido (liminar + ordem); postura adversarial dura.
5. **Garantias e norma** — invocar as garantias constitucionais (PA-07), lei penal vigente no tempo do fato (PA-04) e jurisprudencia validada (PA-01); jamais orientar fuga ou obstrucao (PA-08).
6. Ao final, submeter a `revisao-final-criminal` (R1-R4) antes da entrega.

**Skill a acionar:** `habeas-corpus`.
