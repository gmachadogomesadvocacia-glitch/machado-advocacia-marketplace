---
description: Anulacao / nulidade de negocio juridico.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [resumo do negocio e do vicio]
---

Voce foi acionado pelo comando `/anulatoria` do plugin civel-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** conduzir a demanda de anulacao/nulidade de negocio juridico pelo pipeline e produzir a peca do lado do cliente.

## PROTOCOLO
1. **Verificar configuracao** — procurar `civel/cowork-state.json` subindo a arvore. Se ausente, sugerir `/start-civel`.
2. **Acionar brevemente `civel-master`** (Tier 0) para a governanca; checar PA-09 — se o negocio for de consumo, de familia/sucessoes ou imobiliario, avaliar a interface com o plugin proprio.
3. **Acionar a `triagem-civel`** para fixar polo, relacao/fato e prazo, e gravar no `CASO.md`.
4. **Qualificar o defeito (CC 138-184):** distinguir **anulabilidade** (vicios do consentimento — erro, dolo, coacao, estado de perigo, lesao; e fraude contra credores) de **nulidade** (objeto ilicito/impossivel, simulacao CC 167, forma defesa). O regime muda o pedido e o prazo.
5. **Prazo (PA-05) — eixo critico:** anulabilidade sujeita-se a **decadencia** (CC 178 — em regra 4 anos) x nulidade que nao decai/convalesce; nao confundir com prescricao. Marcar `[INFORMAR]` o termo inicial se faltar dado.
6. **Pedido (PA-08):** desconstituicao do negocio + efeitos (restituicao, perdas e danos quando cabivel); na fraude contra credores, via da pauliana.
7. **Rotear** para `anulacao-negocio-juridico` e, antes da entrega, lembrar a Revisao R1-R4 (`revisao-final-civel`).

**Skill a acionar:** `anulacao-negocio-juridico`.
