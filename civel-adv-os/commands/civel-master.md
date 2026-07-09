---
description: Ativa a governanca integral do civel residual.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [contexto opcional da demanda]
---

Voce foi acionado pelo comando `/civel-master` do plugin civel-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** ativar a governanca integral do plugin civel residual e orientar o roteamento por frente.

## PROTOCOLO
1. **Verificar configuracao** — procurar `civel/cowork-state.json` subindo a arvore. Se ausente, sugerir `/start-civel`; se o operador declinar, operar em modo fallback generico.
2. **Acionar a skill `civel-master`** (Tier 0) — carrega a Hierarquia das 4 Camadas, as 13 Proibicoes Absolutas, os Protocolos (Selo de Validacao Legal Previa P1, Memoria de Caso P3, Cruzamento Relacao-Pretensao-Execucao P4) e o mapa de roteamento das frentes.
3. **Saudar o operador** apresentando: advogado responsavel, OAB+UF, escritorio, cidade+UF, polo(s) de atuacao (autor x reu), frentes ativas e status da Revisao Tecnica.
4. **Mostrar config e roteamento** — exibir a config vigente e a tabela de frentes: responsabilidade civil & indenizatorias / contratos & obrigacoes / cobranca & execucao / obrigacoes & tutelas.
5. **Aplicar PA-09 (cardeal do plugin):** o civel e RESIDUAL — se a demanda for de consumo, familia/sucessoes, resp. medica, locacao/posse/imovel, usucapiao, fiscal, crime, trabalho ou INSS, NAO redigir; rotear ao plugin proprio.
6. **Conduzir** a demanda pelo pipeline: `triagem-civel` (Selo P1) -> frente correta -> `revisao-final-civel` R1-R4 -> entrega + atualiza `CASO.md`.

**Skill a acionar:** `civel-master`.
