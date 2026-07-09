---
description: Porta de entrada.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [resumo da demanda]
---

Voce foi acionado pelo comando `/triagem` do plugin civel-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** triar a demanda, confirmar que e cível residual e gravar o diagnostico no `CASO.md`. Porta de entrada de todo caso.

## PROTOCOLO
1. **Verificar configuracao** — procurar `civel/cowork-state.json` subindo a arvore. Se ausente, sugerir `/start-civel`; se o operador declinar, operar em modo fallback generico.
2. **Acionar brevemente `civel-master`** (Tier 0) para carregar a governanca: 4 Camadas, 13 Proibicoes Absolutas e Protocolos.
3. **PASSO ZERO (PA-09) — e civel residual?** Se a demanda pertencer a outro ramo (consumo, familia/sucessoes, resp. medica, locacao/posse/imovel, usucapiao, fiscal, crime, trabalho, INSS), PARAR e rotear ao plugin proprio. Nao prosseguir na triagem civel.
4. **Acionar a skill `triagem-civel`** — classificar nos **5 eixos**: **Frente** (responsabilidade civil & indenizatorias / contratos & obrigacoes / cobranca & execucao / obrigacoes & tutelas), **Polo** (autor x reu — variavel-mae), **Relacao/Fato** (contratual x extracontratual; ato/contrato e norma vigente a epoca — PA-04/PA-07), **Valor** (estimativa da causa, JEC ate 40 SM x vara comum), **Prazo** (prescricao x decadencia — CC 205/206 — PA-05).
5. **Confirmar o polo do cliente.** Em ausencia ou contradicao, parar e perguntar antes de produzir (PA-10).
6. **Gravar** o diagnostico dos 5 eixos no `CASO.md`. Lacunas ficam como `[INFORMAR]`, nunca inventar.
7. **Rotear** para o **Selo P1** (Validacao Legal Previa) e para `analise-documental-civel`.

**Skill a acionar:** `triagem-civel`.
