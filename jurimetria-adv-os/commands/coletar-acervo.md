---
description: Roda o Modulo C — varre todos os CASO.md do acervo, consolida o dataset do portfolio e entrega o relatorio descritivo (composicao, quantum, taxa de exito) com freio de N-minimo e lista dos casos sem bloco.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [recorte opcional: area, status, periodo] [--datajud]
---

Voce foi acionado pelo comando `/coletar-acervo` do plugin jurimetria-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** o retrato jurimetrico do portfolio proprio.

## PROTOCOLO

1. Ler o CASE_ROOT da config (`jurimetria/config.md`); ausente → sugerir `/start-jurimetria`.
2. **Acionar a skill `coleta-acervo`**: rodar `py scripts/coletar_acervo.py "<CASE_ROOT>"` (com `--datajud` so se pedido — e lento, avisar). Recorte no argumento → usar `--json` e agregar o subgrupo com o mesmo freio de N.
3. Redigir o relatorio pela `estilo-relatorio-jurimetrico` (cobertura de instrumentacao SEMPRE declarada; casos sem bloco listados com oferta de `/instrumentar-caso`).
4. **Auditar com `revisao-final-jurimetria`** antes de entregar (PE-14).
5. Entregar em `.txt` se o operador quiser arquivo; senao, no chat com carimbos.

**Skill a acionar:** `coleta-acervo`.
