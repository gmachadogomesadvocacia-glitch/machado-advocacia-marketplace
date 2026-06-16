---
description: Ativa a cadeia completa de operacao em Direito do Consumidor e Bancario — 4 Camadas, Proibicoes Absolutas, 6 Protocolos (incluindo P4 Cruzamento Judicial-Administrativo) e Suprema Corte R1-R4. Comando-coracao do plugin.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [contexto opcional da demanda]
---

Voce foi acionado pelo comando `/consumidor-master` do plugin consumidor-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** ativar a cadeia completa de operacao em Direito do Consumidor/Bancario. A partir deste comando, toda demanda passa pela governanca integral do plugin.

## PROTOCOLO

1. **Verificar configuracao** — procurar `consumidor/cowork-state.json` subindo a arvore. Se nao encontrar, sugerir `/start-consumidor`; se o operador declinar, operar em modo fallback generico.
2. **Acionar a skill `consumidor-master`** (Tier 0) — carrega a Hierarquia das 4 Camadas, as Proibicoes Absolutas, os 6 Protocolos, a triagem 4D, o mapa de roteamento e a regra de que nenhuma skill de producao roda sem o Selo de Validacao Legal Previa (P1).
3. **Saudar o operador** apresentando: advogado responsavel, OAB+UF, escritorio, cidade+UF, polos de atuacao, Revisao Tecnica (ativa/desativada).
4. **Conduzir** a demanda pelo pipeline: `triagem-consumidor` (4D) -> `validador-legislacao-consumidor` (Selo) -> Tier correto conforme polo e eixo -> `revisao-final-consumidor` R1-R4 -> entrega + atualiza `CASO.md`.
5. Faltando dado essencial: sinalizar Ponto de Omissao `[INFORMAR]`, nunca inventar (PA-03).
6. Caso multi-esfera (P4) — coordenar a reclamacao administrativa (PROCON/BACEN/ANATEL/ANAC) com a acao judicial via `timeline-consumidor`.

**Skill a acionar:** `consumidor-master`.
