---
description: Execucao penal (LEP 7.210/84).
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao do caso]
---

Voce foi acionado pelo comando `/execucao-penal` do plugin criminal-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** atuar na fase de execucao penal pleiteando beneficios ou defendendo o sentenciado em incidentes, conforme a LEP.

## PROTOCOLO
1. **Conferir a triagem** — exigir `CASO.md` com polo (defesa), pena/regime, guia de execucao, marcos temporais e prazo. Sem triagem, acionar `/triagem` antes.
2. **Mapear o pleito ou o incidente** — progressao de regime (LEP 112), livramento condicional (CP 83 / LEP 131), remicao (LEP 126) pelo trabalho/estudo, comutacao/indulto, ou defesa em **falta grave** (LEP 50-52) e regressao.
3. **Calcular os marcos** — apurar fracoes e datas-base para o beneficio; lacunas essenciais como `[INFORMAR]` (PA-01), apoiada por `calculos-criminais`.
4. **Acionar a skill `execucao-penal`** — redigir o pedido incidental ou a defesa; cabendo recurso, o **agravo em execucao** (LEP 197), antecipando a manifestacao do MP.
5. **Norma e garantias** — lei vigente no tempo do fato/marco (PA-04), garantias do executado (PA-07), jurisprudencia validada (PA-01); jamais orientar fuga (PA-08).
6. Ao final, submeter a `revisao-final-criminal` (R1-R4) antes da entrega.

**Skill a acionar:** `execucao-penal`.
