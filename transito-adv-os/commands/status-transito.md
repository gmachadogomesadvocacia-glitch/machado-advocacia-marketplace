---
description: Le o estado atual do plugin (persona, caso ativo, eixo/fase, pontuacao da CNH e prazos em aberto) e apresenta um resumo do que esta carregado.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [opcional]
---

Voce foi acionado pelo comando `/status-transito` do plugin transito-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** resumir o estado vivo do plugin e do caso ativo para o operador.

## PROTOCOLO
1. **Localizar o estado** — procurar `transito/cowork-state.json` subindo a arvore; se ausente, sugerir `/start-transito`.
2. **Acionar a skill `memoria-de-caso-transito`** — ler a persona ativa (`TRAN_PERSONA`), o caso corrente em `transito/casos/<slug>/CASO.md`, a pontuacao/situacao da CNH e os prazos registrados.
3. **Resumir** — escritorio/advogado, polo (defesa do condutor/proprietario), eixos configurados (administrativo/CNH/judicial/analise); caso ativo, eixo e fase, pontuacao acumulada e situacao da CNH (regular/suspensa/cassada) e proximos prazos (defesa previa, JARI, CETRAN, judicial — atencao a preclusao dos 30 dias, PA-05) e pendencias `[INFORMAR]`.
4. **Prioridade ao prazo** — se houver prazo administrativo de 30 dias em curso, destacar a urgencia no topo do resumo (PA-05).
5. Nao alterar nenhum arquivo; este comando e somente leitura.

**Skill a acionar:** `memoria-de-caso-transito`.
