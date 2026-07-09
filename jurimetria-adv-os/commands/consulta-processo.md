---
description: Consulta um processo por numero CNJ no DataJud (Modulo A).
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: <numero-cnj | caminho do CASO.md>
---

Voce foi acionado pelo comando `/consulta-processo` do plugin jurimetria-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** o retrato oficial de UM processo (tempo e andamentos).

## PROTOCOLO

1. **Acionar a skill `consulta-datajud`**:
   - numero CNJ → `py scripts/datajud_client.py <numero>`;
   - caminho de CASO.md → `py scripts/ler_caso.py "<caminho>" --datajud` (une acervo + DataJud).
2. Reportar capa, duracao (ajuizamento → ultimo movimento), numero de movimentos e ultima movimentacao, com data da consulta.
3. Declarar os limites: nao encontrado ≠ inexistente (indexacao/segredo); duracao ≠ tempo ate sentenca; sem quantum (PE-07).
4. Se veio de CASO.md: apontar divergencias de classificacao e oferecer gravar `datajud_sync` via `instrumentar-caso`.

**Skill a acionar:** `consulta-datajud`.
