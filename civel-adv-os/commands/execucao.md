---
description: Execucao de titulo executivo extrajudicial (CPC 784) e busca e apreensao em alienacao fiduciaria (DL 911/69).
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [resumo do titulo ou do contrato fiduciario]
---

Voce foi acionado pelo comando `/execucao` do plugin civel-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** conduzir a execucao de titulo extrajudicial ou a busca e apreensao fiduciaria pelo pipeline e produzir a peca do lado do cliente.

## PROTOCOLO
1. **Verificar configuracao** — procurar `civel/cowork-state.json` subindo a arvore. Se ausente, sugerir `/start-civel`.
2. **Acionar brevemente `civel-master`** (Tier 0) para a governanca; checar PA-09 — se a execucao for fiscal, trabalhista ou de consumo, rotear ao plugin proprio.
3. **Acionar a `triagem-civel`** para fixar polo (exequente/autor x executado/reu), relacao/fato e prazo, e gravar no `CASO.md`.
4. **Validar o titulo (PA-08):** confirmar **titulo executivo extrajudicial** (CPC 784) liquido, certo e exigivel. Sem titulo, NAO e execucao — rotear para `/cobranca` (monitoria/cobranca).
5. **Busca e apreensao (DL 911/69):** quando houver **alienacao fiduciaria**, exigir a comprovacao da **mora** (notificacao/protesto) antes da liminar; tratar a purgacao da mora e a consolidacao da propriedade.
6. **Liquidar e atualizar (PA-06):** demonstrativo do debito com juros e correcao; conferir prescricao da pretensao executiva (PA-05).
7. **Rotear** para `execucao-titulo-extrajudicial` e, antes da entrega, lembrar a Revisao R1-R4 (`revisao-final-civel`).

**Skill a acionar:** `execucao-titulo-extrajudicial`.
