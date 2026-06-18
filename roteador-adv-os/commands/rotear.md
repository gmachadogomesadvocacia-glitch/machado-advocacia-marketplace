---
description: Identifica automaticamente qual plugin Adv-OS atende o tema descrito e confirma antes de acionar.
allowed-tools: Read, Glob, Grep
argument-hint: "[descreva o caso/fato ou cole o documento]"
---

# /rotear — porta de entrada unica do escritorio

Aciona o **roteador central** sobre o relato em `$ARGUMENTS` (ou sobre a ultima
mensagem do usuario, se vazio).

## PROTOCOLO
1. **Acionar a skill `roteador-adv-os`** — extrai os sinais, classifica entre os 11
   plugins e aplica as regras de desambiguacao.
2. **Sugerir e confirmar**: anuncia o tema detectado + os sinais e pergunta antes de
   acionar o `/start-<plugin>`. Se ambiguo, lista os candidatos e pergunta.
3. So apos o "ok" do usuario, aciona o comando de entrada do plugin escolhido.

> Nao produz peca aqui — so identifica e roteia. Em duvida real, pergunta.

**Skill a acionar:** `roteador-adv-os`.
