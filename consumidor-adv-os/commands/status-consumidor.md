---
description: Mostra o estado do plugin consumidor-adv-os — identidade do operador (advogado, OAB, cidade/UF), polos, eixos, estado da Revisao Tecnica e casos ativos. Se nao configurado, sugere /start-consumidor.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [opcional]
---

Voce foi acionado pelo comando `/status-consumidor` do plugin consumidor-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** apresentar um panorama do estado atual do plugin a partir dos arquivos de configuracao. Comando de leitura — nao produz peca nem aciona skill de producao.

## PROTOCOLO

1. **Verificar configuracao** — procurar `consumidor/cowork-state.json` subindo a arvore. Se ausente, informar que o plugin nao esta configurado e sugerir `/start-consumidor`; encerrar.
2. **Ler** `consumidor/cowork-state.json` e `consumidor/config.md`.
3. **Exibir a identidade** — advogado responsavel, OAB+UF, escritorio, cidade/UF.
4. **Exibir os polos** de atuacao (consumidor/fornecedor/ambos) e os **eixos** habilitados.
5. **Exibir o estado da Revisao Tecnica** R1-R4 (`revisao-final-consumidor`): ativa ou desativada.
6. **Listar os casos ativos** em `consumidor/casos/` (slug + 1 linha de status, lido do CASO.md de cada um).
7. Nao aciona skill-alvo. Se algum arquivo estiver corrompido ou incompleto, sinalizar e sugerir `/start-consumidor` para reconfigurar.

**Skill a acionar:** nenhuma (comando de leitura).
