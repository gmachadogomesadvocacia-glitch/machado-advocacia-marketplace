---
description: Porta de entrada: classifica o caso e crava os prazos.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao do caso]
---

Voce foi acionado pelo comando `/triagem` do plugin leiloes-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** classificar a demanda em 4D, fixar o rito, emitir o Selo P1 e cravar os prazos no `CASO.md`.

## PROTOCOLO
1. Acionar brevemente `leiloes-master` para carregar a governanca.
2. **Passo zero — o polo:** o cliente compra ou perde o bem? Se for executado, devedor fiduciante, exequente ou credor fiduciario, **parar e rotear** (PA-12). Se nao estiver claro, perguntar.
3. Acionar `triagem-leiloes` e classificar: **polo** · **via** (judicial x fiduciario) · **fase** · **obstaculo**; na via judicial, identificar o **rito** (civel, fiscal Lei 6.830/80 ou trabalhista CLT 888), que muda todos os prazos.
4. **Emitir o Selo P1** — data de divulgacao do edital (modulacao do Tema 1.134), CPC aplicavel (condominio), datas do contrato e da consolidacao na via fiduciaria (Tema 1.288) e estado do Tema 886.
5. **Cravar os prazos com data-limite no calendario.** Havendo prazo de 10 dias do art. 903 em curso, tratar como urgencia maxima e rotear de imediato (PA-11).
6. Se houver lance a dar, conferir os **impedidos de arrematar** (CPC 890, inclusive advogados das partes — PA-10) e o piso do preco vil (891).
7. Gravar tudo no `CASO.md`; lacuna vira `[INFORMAR]`, nunca invencao (PA-02).
8. Rotear para `analise-documental-leiloes` e para a skill da fase.

**Skill a acionar:** `triagem-leiloes`.
