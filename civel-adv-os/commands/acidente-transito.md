---
description: Reparacao civil por acidente de transito — danos materiais, morais e esteticos, DPVAT e acao de regresso. Nexo, culpa, excludentes e quantum no contexto viario.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [resumo do acidente]
---

Voce foi acionado pelo comando `/acidente-transito` do plugin civel-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** conduzir a demanda de reparacao por acidente de transito pelo pipeline e produzir a peca do lado do cliente.

## PROTOCOLO
1. **Verificar configuracao** — procurar `civel/cowork-state.json` subindo a arvore. Se ausente, sugerir `/start-civel`.
2. **Acionar brevemente `civel-master`** (Tier 0) para a governanca; checar PA-09 (se houver relacao de consumo — ex.: transporte de passageiros como servico — avaliar interface com `consumidor-adv-os`).
3. **Acionar a `triagem-civel`** para fixar polo (vitima/autor x condutor/seguradora/reu), relacao/fato e prazo, e gravar no `CASO.md`.
4. **Qualificar:** culpa do condutor (CTB), nexo, excludentes (caso fortuito, culpa exclusiva da vitima/terceiro); danos materiais (reparo, desvalorizacao), lucros cessantes (ex.: taxista/motorista de app), danos morais e esteticos.
5. **DPVAT e regresso:** abater/considerar o DPVAT quando cabivel; viabilizar a acao de regresso da seguradora contra o causador quando o cliente for a seguradora.
6. **Foro e prazo (PA-05/PA-08):** foro do lugar do fato (art. 53, IV, CPC) ou domicilio do autor; prescricao trienal (CC 206 §3º V).
7. **Rotear** para `acidente-transito-civel` e, antes da entrega, lembrar a Revisao R1-R4 (`revisao-final-civel`).

**Skill a acionar:** `acidente-transito-civel`.
