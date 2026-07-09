---
description: Aciona a governanca central (Tier 0) do plugin criminal-adv-os.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [pergunta ou contexto opcional]
---

Voce foi acionado pelo comando `/criminal-master` do plugin criminal-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** carregar a governanca de 4 Camadas, mostrar a configuracao ativa e rotear a demanda para a skill correta.

## PROTOCOLO
1. **Carregar estado** — procurar `criminal/cowork-state.json` subindo a arvore; ler `CRIM_PERSONA` (persona.md) e a config (fase, polo, tom/intensidade). Se ausente, sugerir `/start-criminal`.
2. **Acionar a skill `criminal-master`** (Tier 0) — aplicar as 4 Camadas de Governanca, as 13 Proibicoes Absolutas e os Protocolos (Selo P1 — PA-11; R1-R4 — PA-13; polo defesa x assistencia — PA-10; sigilo reforcado — PA-09).
3. **Resumir a config ativa** — advogado/escritorio, polo (defesa x assistencia de acusacao), fases habilitadas (investigacao/acao penal/juri/recursos/execucao/acordos) e situacao prisional do caso ativo.
4. **Rotear** — diante do `$ARGUMENTS`, indicar a porta de entrada (`/triagem`) ou a skill de producao adequada (HC, flagrante, resposta a acusacao, juri, recursos, execucao penal, acordos).
5. **Prioridade a liberdade** — se houver pessoa presa, sinalizar a urgencia (HC/relaxamento/liberdade provisoria) antes de qualquer outra producao.
6. Nunca produzir peca sem passar pela triagem e, ao final, pela Revisao R1-R4.

**Skill a acionar:** `criminal-master`.
