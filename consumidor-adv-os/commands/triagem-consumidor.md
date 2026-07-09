---
description: Executa a triagem 4D (polo x eixo x esfera x rito) de toda demanda consumerista/bancaria e grava o diagnostico no CASO.md.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [resumo da demanda]
---

Voce foi acionado pelo comando `/triagem-consumidor` do plugin consumidor-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** classificar a demanda nas 4 dimensoes simultaneas e gravar o resultado no `CASO.md`. Esta e a porta de entrada de todo caso.

## PROTOCOLO

1. **Verificar configuracao** — procurar `consumidor/cowork-state.json` subindo a arvore. Se ausente, sugerir `/start-consumidor`; se o operador declinar, operar em modo fallback generico.
2. **Acionar brevemente `consumidor-master`** (Tier 0) para carregar a governanca: 4 Camadas, Proibicoes Absolutas e os 6 Protocolos.
3. **Acionar a skill `triagem-consumidor`** — classificar nas 4D: **Polo** (consumidor/fornecedor), **Eixo** (bancario, negativacao, telecom, servicos essenciais, aereo, vicio/fato do produto, e-commerce, publicidade, clausulas abusivas, cobranca indevida, superendividamento, imobiliario), **Esfera** (judicial/administrativa/extrajudicial) e **Rito** (JEC ate 40 SM / vara comum / coletiva).
4. **Ler/perguntar o polo do cliente** — variavel-mae. Em ausencia ou contradicao, parar e perguntar antes de produzir (PA-05).
5. **Gravar** o diagnostico 4D no `CASO.md` via `memoria-de-caso-consumidor` (P3).
6. Faltando dado essencial, sinalizar `[INFORMAR]`, nunca inventar (PA-03).
7. Antes de qualquer entrega posterior, lembrar a Revisao R1-R4 (`revisao-final-consumidor`, PA-22).

**Skill a acionar:** `triagem-consumidor`.
