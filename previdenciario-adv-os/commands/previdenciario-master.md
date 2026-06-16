---
description: Ativa a cadeia completa de operacao em Direito Previdenciario — Hierarquia das 4 Camadas, 22 Proibicoes Absolutas, roteamento por Tiers e Suprema Corte R1-R4. Comando-coracao do plugin.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [contexto opcional da demanda]
---

Voce foi acionado pelo comando `/previdenciario-master` do plugin previdenciario-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** ativar a cadeia completa de operacao previdenciaria. Toda demanda passa pela governanca integral do plugin.

## PROTOCOLO

1. **Verificar configuracao** — procurar `previdenciario/cowork-state.json` subindo a arvore. Se nao encontrar, sugerir `/start-previdenciario`; se o operador declinar, operar em modo fallback generico.
2. **Acionar a skill `previdenciario-master`** (Tier 0) — carrega a Hierarquia das 4 Camadas, as 22 Proibicoes Absolutas e o roteamento por Tiers.
3. **Saudar o operador** apresentando: advogado responsavel, OAB+UF, escritorio, cidade+UF, frentes ativas (RGPS/RPPS/complementar/acidentario/consultivo), Revisao Tecnica (ativa/desativada).
4. **Conduzir** pelo pipeline: Tier 1 Estado-Maior (`triagem-dogmatica` -> `analise-trilateral` -> `jurisprudencia-estrategica` -> `estrategia-de-caso`) -> Tier 2 (skill do caso) -> `suprema-corte-previdenciaria` R1-R4 -> entrega + atualiza `CASO.md`.
5. Faltando dado essencial: sinalizar Ponto de Omissao `[INFORMAR]`, nunca inventar.
6. Validar a vigencia da norma no marco temporal (DER/fato gerador) — EC 103/2019 e regras de transicao.

**Skill a acionar:** `previdenciario-master`.
