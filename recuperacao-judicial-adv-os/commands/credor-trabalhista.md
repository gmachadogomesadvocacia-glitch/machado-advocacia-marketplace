---
description: Nucleo CREDOR TRABALHISTA (eixo prioritario).
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [dados do credito trabalhista]
---

Voce foi acionado pelo comando `/credor-trabalhista` do plugin recuperacao-judicial-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** representar o CREDOR TRABALHISTA na habilitacao de credito (MODO CTH).

## PROTOCOLO
1. **Acionar a skill `credor-trabalhista-rj`** — conduz a coleta obrigatoria (22 campos), decide a via (divergencia/impugnacao/retardataria/reserva), classifica entre concursal e extraconcursal pelo fato gerador, aplica o teto de 150 SM (art. 83 I — excedente em Classe III) e verifica prescricao (bienal CF, intercorrente CLT, da habilitacao, pos-encerramento art. 61).
2. **Cruzamento JT x RJ** (Protocolo P8) → articular `cruzamento-jt-rj`.
3. **Calculo** → delegar a `calculo-credito-trabalhista-rj`; **via** → `via-processual-rj`; **peca** → `habilitacao-credito-rj`.
4. Submeter a `revisao-final-rj` (R1-R4).

**Skill a acionar:** `credor-trabalhista-rj`.
