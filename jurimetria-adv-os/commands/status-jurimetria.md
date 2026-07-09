---
description: Mostra o estado do plugin jurimetria-adv-os.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [opcional]
---

Voce foi acionado pelo comando `/status-jurimetria` do plugin jurimetria-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** panorama do estado atual do plugin. Comando de leitura — nao produz analise.

## PROTOCOLO

1. **Verificar configuracao** — procurar `jurimetria/cowork-state.json` subindo a arvore. Ausente: informar e sugerir `/start-jurimetria`; encerrar.
2. **Ler** `jurimetria/cowork-state.json` e `jurimetria/config.md`.
3. **Exibir identidade** (advogado, OAB, escritorio), **CASE_ROOT**, **tribunais de referencia** e **N minimo**.
4. **Cobertura de instrumentacao** — rodar `py scripts/coletar_acervo.py "<CASE_ROOT>"` (sem --datajud) e reportar: CASO.md encontrados, com bloco, SEM bloco (lista curta) — o termometro da materia-prima.
5. **Exibir estado da Revisao R1-R4** (ativa/desativada).
6. Arquivo corrompido/incompleto: sinalizar e sugerir `/start-jurimetria`.

**Skill a acionar:** nenhuma (comando de leitura).
