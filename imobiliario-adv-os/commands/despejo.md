---
description: Acao de despejo e cobranca de alugueis (Lei 8.245/91).
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao do caso]
---

Voce foi acionado pelo comando `/despejo` do plugin imobiliario-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** estruturar a acao de despejo (com ou sem cumulacao de cobranca de alugueis) ou a defesa do locatario, conforme o polo do cliente.

## PROTOCOLO
1. **Conferir a triagem** — `CASO.md` com o contrato de locacao (residencial/nao residencial), o polo (locador ou locatario — PA-10), o fundamento (falta de pagamento, denuncia vazia art. 46/57, infracao contratual), as garantias e os prazos.
2. **Definir a via e o fundamento** (modo estrategico do escritorio) — despejo por falta de pagamento c/c cobranca; denuncia vazia; despejo por infracao contratual/uso indevido.
3. **Liminar** — so concedida nas hipoteses do **art. 59 §1º** da Lei 8.245/91 e mediante **caucao** de 3 alugueis (PA-06). Nao requerer liminar fora dessas hipoteses.
4. **Purgacao da mora** — no polo do locatario, aferir o direito do **art. 62, II** (e a limitacao do paragrafo unico — uma vez em 24 meses); no polo do locador, antecipar a purgacao.
5. **Garantias** — verificar a vedacao a cumulacao de garantias (art. 37 — PA-08) e a regularidade da garantia exigida.
6. **Travas** — norma vigente no contrato (PA-04); nao confundir posse x propriedade (PA-05); jurisprudencia validada (PA-01).
7. **Acionar a skill `despejo`** para redigir a peca escolhida.
8. Ao final, submeter a `revisao-final-imobiliaria` (R1-R4).

**Skill a acionar:** `despejo`.
