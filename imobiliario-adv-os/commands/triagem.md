---
description: Porta de entrada do plugin.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao do caso]
---

Voce foi acionado pelo comando `/triagem` do plugin imobiliario-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** classificar a demanda imobiliaria nos 5 eixos e gravar o diagnostico no `CASO.md`. Esta e a porta de entrada de todo caso.

## PROTOCOLO
1. **Acionar brevemente `imobiliario-master`** (Tier 0) para carregar a governanca de 4 Camadas e os Protocolos antes de classificar.
2. **Acionar a skill `triagem-imobiliaria`** — classificar nos 5 eixos: **Frente** (locacao / contratos imobiliarios / direitos reais e posse / consultivo), **Polo** (locador x locatario, comprador x vendedor, possuidor x esbulhador, condominio x condomino, fiduciante x credor fiduciario — variavel-mae, PA-10), **Imovel** (matricula, endereco, area, situacao para foro — art. 47 CPC), **Contrato/tipo de demanda** (locacao residencial/nao residencial, promessa, condominio, alienacao fiduciaria) e **Prazo** (decadencia x prescricao; renovatoria art. 51 §5º — PA-07; purgacao da mora).
3. **Travar posse x propriedade x dominio** (PA-05) ja na triagem — nao confundir os planos; a via (possessoria x petitoria) depende disso.
4. **Confirmar o polo do cliente** — em ausencia ou contradicao, parar e perguntar antes de produzir (PA-10).
5. **Gravar** o diagnostico no `CASO.md`; toda lacuna essencial entra como `[INFORMAR]`, nunca inventada (PA-01).
6. **Rotear** — encaminhar para o **Selo P1** (validacao de norma vigente no contrato/fato — PA-04, PA-11) e para `analise-documental-imobiliaria` (matricula, contrato, notificacoes).
7. Antes de qualquer entrega posterior, lembrar a Revisao R1-R4.

**Skill a acionar:** `triagem-imobiliaria`.
