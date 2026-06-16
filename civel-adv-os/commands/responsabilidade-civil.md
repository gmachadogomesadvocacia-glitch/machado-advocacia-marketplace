---
description: Acao indenizatoria / responsabilidade civil — dano moral, material e estetico; ato ilicito CC 186/187/927, nexo, culpa x responsabilidade objetiva, quantum.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [resumo do dano e do fato]
---

Voce foi acionado pelo comando `/responsabilidade-civil` do plugin civel-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** conduzir a demanda indenizatoria pelo pipeline e produzir a peca do lado do cliente.

## PROTOCOLO
1. **Verificar configuracao** — procurar `civel/cowork-state.json` subindo a arvore. Se ausente, sugerir `/start-civel`.
2. **Acionar brevemente `civel-master`** (Tier 0) para a governanca; checar PA-09 — se o dano for de consumo, resp. medica, transito (use `/acidente-transito`) ou resp. do Estado (use `/resp-estado`), rotear ao fluxo/plugin proprio.
3. **Acionar a `triagem-civel`** para fixar polo, relacao/fato e prazo, e gravar no `CASO.md`.
4. **Qualificar (PA-07):** distinguir responsabilidade **extracontratual** (ato ilicito, CC 186/187/927) de **contratual**; identificar culpa x responsabilidade objetiva (CC 927 §unico) e os elementos conduta-nexo-dano.
5. **Liquidar o dano (PA-06):** dano moral, material (dano emergente + lucros cessantes) e estetico; fundamentar o quantum; juros e correcao — termo inicial conforme Sum. 54 (extracontratual: do evento) e Sum. 362 STJ (moral: do arbitramento).
6. **Conferir o prazo (PA-05):** prescricao da pretensao de reparacao (CC 206 §3º V — 3 anos) x prazos especiais.
7. **Rotear** para `responsabilidade-civil` e, antes da entrega, lembrar a Revisao R1-R4 (`revisao-final-civel`).

**Skill a acionar:** `responsabilidade-civil`.
