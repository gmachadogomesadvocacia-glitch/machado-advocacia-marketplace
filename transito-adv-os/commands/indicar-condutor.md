---
description: Indicacao do real condutor infrator (CTB 257 §7o).
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao do caso]
---

Voce foi acionado pelo comando `/indicar-condutor` do plugin transito-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** preparar a indicacao formal do real condutor infrator, atribuindo a infracao a quem efetivamente dirigia o veiculo.

## PROTOCOLO
1. **Barreira PA-06 (inegociavel)** — confirmar com o operador que a pessoa a indicar **e o condutor real** no momento da infracao. Indicacao falsa de condutor e crime (falsidade ideologica, art. 299 CP) e jamais sera produzida — esta e a invariante central do comando.
2. **Conferir a triagem** — exigir `CASO.md` com polo (proprietario do veiculo), auto de infracao, dados do condutor real (nome, CNH, CPF, assinatura) e prazo. Sem triagem, acionar `/triagem` antes.
3. **Atencao ao prazo** — a indicacao acompanha o prazo da Notificacao da Autuacao (CTB 257 §7o); prazo preclusivo de 30 dias (PA-05).
4. **Acionar a skill `indicacao-condutor`** — montar o Formulario de Identificacao do Real Condutor Infrator (FICI) com os requisitos formais (copia da CNH, assinaturas do proprietario e do condutor), validando a norma vigente (PA-04).
5. **Consequencia** — esclarecer ao operador que a pontuacao migra para o condutor indicado e que a ausencia de indicacao mantem os pontos no proprietario (e pode gerar a multa do CTB 257 §8o).
6. Ao final, submeter a `revisao-final-transito` (R1-R4) antes da entrega.

**Skill a acionar:** `indicacao-condutor`.
