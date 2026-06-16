---
description: Le o estado atual do plugin (persona, caso ativo, frente/polo e prazos em aberto) e apresenta um resumo do que esta carregado.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [opcional]
---

Voce foi acionado pelo comando `/status-imobiliario` do plugin imobiliario-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** resumir o estado vivo do plugin e do caso ativo para o operador.

## PROTOCOLO
1. **Localizar o estado** — procurar `imobiliario/cowork-state.json` subindo a arvore; se ausente, sugerir `/start-imobiliario`.
2. **Acionar a skill `memoria-de-caso-imobiliario`** — ler a persona ativa (`IMOB_PERSONA`), o caso corrente em `imobiliario/casos/<slug>/CASO.md` e os prazos registrados.
3. **Resumir** — escritorio/advogado, polo do cliente (PA-10), frentes configuradas; caso ativo, frente, imovel (matricula/endereco), fase processual e proximos prazos (decadencia/prescricao/recursal; renovatoria art. 51 §5º — PA-07; purgacao da mora) e pendencias `[INFORMAR]`.
4. Nao alterar nenhum arquivo; este comando e somente leitura.

**Skill a acionar:** `memoria-de-caso-imobiliario`.
