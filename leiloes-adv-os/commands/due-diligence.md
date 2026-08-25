---
description: Parecer pre-lance com veredito e custo real.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [lote/edital]
---

Voce foi acionado pelo comando `/due-diligence` do plugin leiloes-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** dizer ao cliente se vale a pena dar o lance, com veredito fechado.

## PROTOCOLO
1. Exigir **edital e matricula atualizada**. Sem eles, nao emitir parecer: entregar a lista do que falta.
2. Acionar `analise-documental-leiloes` (cruzar edital x matricula x autos) e, se preciso, `analise-edital-leilao`.
3. Acionar a skill **`due-diligence-lote`** e rodar os seis exames: edital · matricula e onus · debitos · ocupacao · processo de origem · cliente.
4. Calcular o **custo real de aquisicao** com `calculos-leiloes` (lance + comissao + ITBI + custas + debitos + desocupacao + reforma + carrego), com premissas declaradas.
5. Tratar onus e debitos **um a um** (PA-06): tributos com a modulacao do Tema 1.134 conferida pela **data do edital**; condominio como **risco quantificado com ressalva** (Tema 886 em revisao).
6. Rodar `analise-trilateral-leiloes` para antecipar o ataque do executado.
7. Fechar com **ARREMATAR / NAO ARREMATAR / ARREMATAR COM RESSALVA**, cada risco com probabilidade, impacto e providencia.
8. **Nunca** projetar rentabilidade, agio ou lucro (PA-07). Revisao R1-R4 antes de entregar.

**Skill a acionar:** `due-diligence-lote`.
