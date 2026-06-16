---
description: Contratos civis — revisao, rescisao, resolucao por inadimplemento e perdas e danos; contratos tipicos (prestacao de servico, mutuo, comodato, mandato, doacao, fianca civil).
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [resumo do contrato e do litigio]
---

Voce foi acionado pelo comando `/contratos` do plugin civel-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** conduzir a demanda contratual civel pelo pipeline e produzir a peca do lado do cliente.

## PROTOCOLO
1. **Verificar configuracao** — procurar `civel/cowork-state.json` subindo a arvore. Se ausente, sugerir `/start-civel`.
2. **Acionar brevemente `civel-master`** (Tier 0) para a governanca; checar PA-09 — se for contrato de consumo, locacao/imovel, trabalho ou seguro-saude, rotear ao plugin proprio.
3. **Acionar a `triagem-civel`** para fixar polo, relacao (contratual — PA-07) e prazo, e gravar no `CASO.md`.
4. **Qualificar a pretensao:** revisao (onerosidade excessiva/teoria da imprevisao, CC 478), rescisao/resolucao por inadimplemento (CC 475), exceptio non adimpleti contractus, clausula penal (CC 408-416), perdas e danos.
5. **Norma vigente (PA-04):** aplicar a lei e a redacao contratual vigentes a epoca da celebracao/do fato; identificar o tipo contratual (prestacao de servico, mutuo, comodato, mandato, doacao, fianca civil) e seu regime.
6. **Via/pedido (PA-08):** definir se cabe acao de conhecimento, monitoria (`/cobranca`) ou execucao (`/execucao`) conforme o titulo; prazo decenal (CC 205) salvo prazo especial (PA-05).
7. **Rotear** para `contratos-civeis` e, antes da entrega, lembrar a Revisao R1-R4 (`revisao-final-civel`).

**Skill a acionar:** `contratos-civeis`.
