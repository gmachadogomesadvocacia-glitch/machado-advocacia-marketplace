---
description: Trata o ocupante do imovel arrematado.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [caso]
---

Voce foi acionado pelo comando `/desocupacao` do plugin leiloes-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** definir como se retira cada ocupante, dentro da lei.

## PROTOCOLO
1. Acionar `desocupacao-e-ocupantes`.
2. Identificar quem esta no imovel, com diligencia no local, data e foto quando possivel.
3. Havendo **locatario**, conferir os **tres requisitos cumulativos** do art. 8º da Lei 8.245: prazo determinado + clausula de vigencia + **averbacao na matricula**. Conferir na matricula, nao no contrato. Faltando um, denuncia com 90 dias. Na via fiduciaria, o regime e o do art. 27, § 7º (30 dias para desocupar, denuncia em 90 dias da consolidacao).
4. Para os demais (executado, posseiro, comodatario, usucapiente com acao em curso, promitente comprador com registro), seguir a tabela da skill — usucapiao em curso e **risco alto** e pode justificar desistencia ou eviccao.
5. Comparar acao x acordo por custo e tempo (`linha-estrategica-leiloes`) e registrar a escolha.
6. **Nunca** orientar troca de fechadura, corte de agua ou luz, remocao de pertences ou "desocupacao amigavel" que seja despejo disfarcado (PA-08). Nunca afirmar desocupacao automatica (PA-09).
7. Lancar o custo estimado no calculo do custo real.

**Skill a acionar:** `desocupacao-e-ocupantes`.
