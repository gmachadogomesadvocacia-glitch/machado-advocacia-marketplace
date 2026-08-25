---
description: Defende o arremate contra ataque do executado.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [caso]
---

Voce foi acionado pelo comando `/defesa-arrematacao` do plugin leiloes-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** manter a arrematacao do cliente.

## PROTOCOLO
1. Acionar `defesa-da-arrematacao`.
2. Abrir pelo escudo do **CPC 903, caput**: arrematacao perfeita, acabada e irretratavel, ainda que procedentes os embargos — a procedencia se resolve em reparacao, nao devolve o bem.
3. **Conferir o prazo e a via do ataque**: dentro de 10 dias, incidente (§ 2º); depois da carta, so **acao autonoma**, com o arrematante como **litisconsorte necessario** (§ 4º). Faltando a citacao do cliente, alegar de plano; ataque intempestivo, arguir preclusao antes do merito.
4. Responder alegacao por alegacao: preco vil (piso do edital ou 50% da avaliacao — art. 891), nulidade de intimacao (art. 889 e seu paragrafo unico), impedimento (art. 890), publicidade conforme o rito.
5. Havendo suscitacao infundada de vicio para forcar a desistencia, requerer a multa do **art. 903, § 6º** (ate 20%), quando os autos sustentarem.
6. Rodar `analise-trilateral-leiloes`. Revisao R1-R4 antes de entregar.

**Skill a acionar:** `defesa-da-arrematacao`.
