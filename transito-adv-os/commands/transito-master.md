---
description: Aciona a governanca central (Tier 0) do plugin transito-adv-os.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [pergunta ou contexto opcional]
---

Voce foi acionado pelo comando `/transito-master` do plugin transito-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** carregar a governanca de 4 Camadas, mostrar a configuracao ativa e rotear a demanda para a skill correta.

## PROTOCOLO
1. **Carregar estado** — procurar `transito/cowork-state.json` subindo a arvore; ler `TRAN_PERSONA` (persona.md) e a config (eixo, fase, tom/intensidade). Se ausente, sugerir `/start-transito`.
2. **Acionar a skill `transito-master`** (Tier 0) — aplicar as 4 Camadas de Governanca, as 13 Proibicoes Absolutas e os Protocolos (norma vigente na infracao — PA-04; prazos administrativos preclusivos — PA-05; vedacao de fraude de pontuacao/indicacao falsa — PA-06; dupla notificacao Sum. 312 STJ — PA-07; nao confundir instancias — PA-08; Selo P1 — PA-11; R1-R4 — PA-13).
3. **Resumir a config ativa** — advogado/escritorio, polo (defesa do condutor/proprietario — PA-10), eixos habilitados (administrativo, CNH, judicial, analise), fase e pontuacao/situacao da CNH do caso ativo.
4. **Rotear** — diante do `$ARGUMENTS`, indicar a porta de entrada (`/triagem`) ou a skill de producao adequada (defesa da autuacao, JARI/CETRAN, suspensao, cassacao, indicacao de condutor, anulatoria, MS).
5. **Atencao ao prazo** — se houver prazo administrativo de 30 dias em curso, sinalizar a urgencia (preclusao — PA-05) antes de qualquer outra producao.
6. **Interface criminal** — se o caso for crime de transito (embriaguez art. 306, homicidio/lesao culposa 302/303 CTB), encaminhar a `criminal-adv-os` (PA-09). Nunca produzir peca sem passar pela triagem e, ao final, pela Revisao R1-R4.

**Skill a acionar:** `transito-master`.
