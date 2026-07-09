---
description: Ativa a cadeia completa de operacao em Direito de Familia e Sucessoes.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [contexto opcional da demanda]
---

Voce foi acionado pelo comando `/familia-master` do plugin familia-sucessoes-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** ativar a cadeia completa de operacao em Familia e Sucessoes. Toda demanda passa pela governanca integral do plugin.

## PROTOCOLO

1. **Verificar configuracao** — procurar `familia/cowork-state.json` subindo a arvore. Se nao encontrar, sugerir `/start-familia`; se o operador declinar, operar em modo fallback generico.
2. **Acionar a skill `familia-master`** (Tier 0) — carrega a Hierarquia das 4 Camadas, as Proibicoes Absolutas (PA-01..PA-20), o FIRAC Familia e o roteamento por tipo de caso.
3. **Saudar o operador** apresentando: advogado responsavel, OAB+UF, escritorio, cidade+UF, area de foco (familia/sucessoes), Revisao Tecnica (ativa/desativada).
4. **Identificar o polo** (requerente / requerido / inventariante / herdeiro / meeiro / consultor) — inviolavel.
5. **Conduzir** pelo pipeline: `triagem-familia` -> insumos (documental + jurisprudencia) -> `linha-estrategica-familia` -> skill de producao -> `revisao-final-familia` R1-R4 -> entrega + atualiza `CASO.md`.
6. Faltando dado essencial: sinalizar `[INFORMAR]`, nunca inventar.
7. Calibrar o tom a sensibilidade do caso (filhos, luto, espoliacao) — combatividade proporcional.

**Skill a acionar:** `familia-master`.
