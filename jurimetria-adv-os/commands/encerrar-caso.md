---
description: Fecha o ciclo de vida de um caso — confirma o encerramento real, preenche o desfecho do bloco jurimetrico (com sync DataJud final), fecha a memoria do caso e arquiva a pasta no acervo formal com o operador escolhendo o destino.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: <caminho da pasta do caso | nome do caso>
---

Voce foi acionado pelo comando `/encerrar-caso` do plugin jurimetria-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** nenhum caso sai do acervo ativo sem desfecho registrado — a taxa de exito do portfolio nasce aqui.

## PROTOCOLO

1. **Acionar a skill `encerrar-caso`** no caso indicado.
2. Confirmar as pre-condicoes: o caso encerrou DE VERDADE? (transito + nada a executar, acordo cumprido, extincao definitiva). Execucao/parcelas pendentes = NAO encerra — so atualizar `status`.
3. Desfecho via `instrumentar-caso`: resultado, quantum_obtido, forma/data de encerramento, sync DataJud final, validacao com `py scripts/ler_caso.py`.
4. Fechar o MEMORY.md do caso (resumo final + licoes) e arquivar a pasta — **perguntando o destino ao operador** (nunca decidir sozinho), checando MAX_PATH (~250) e conferindo integridade apos mover. Mover, nunca apagar.
5. Entregar a ficha de encerramento (desfecho carimbado, pendencias `[PREENCHER]`, caminho antigo → novo).

**Skill a acionar:** `encerrar-caso`.
