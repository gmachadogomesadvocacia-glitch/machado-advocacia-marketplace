---
description: Cobranca de divida civel e acao monitoria (CPC 700).
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [resumo da divida e da prova]
---

Voce foi acionado pelo comando `/cobranca` do plugin civel-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** conduzir a cobranca de divida pelo pipeline e produzir a peca pela via adequada.

## PROTOCOLO
1. **Verificar configuracao** — procurar `civel/cowork-state.json` subindo a arvore. Se ausente, sugerir `/start-civel`.
2. **Acionar brevemente `civel-master`** (Tier 0) para a governanca; checar PA-09 — se a divida for de consumo, locaticia, trabalhista ou fiscal, rotear ao plugin proprio.
3. **Acionar a `triagem-civel`** para fixar polo (credor/autor x devedor/reu), relacao/fato e prazo, e gravar no `CASO.md`.
4. **Escolher a via (PA-08) — eixo central:** se houver **prova escrita sem eficacia de titulo executivo**, cabe **monitoria** (CPC 700); se nao houver documento, **acao de cobranca** (conhecimento); se houver **titulo executivo extrajudicial**, NAO e cobranca — rotear para `/execucao`.
5. **Liquidar (PA-06):** apurar o valor, juros de mora (CC 406) e correcao monetaria; termo inicial conforme a natureza da obrigacao.
6. **Conferir o prazo (PA-05):** prescricao da pretensao — geral decenal (CC 205) ou especial (CC 206, p.ex. quinquenal para dividas liquidas em instrumento).
7. **Rotear** para `cobranca-monitoria` e, antes da entrega, lembrar a Revisao R1-R4 (`revisao-final-civel`).

**Skill a acionar:** `cobranca-monitoria`.
