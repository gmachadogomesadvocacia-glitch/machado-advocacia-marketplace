---
description: Ativa a cadeia completa de Recuperacao Judicial e Falencia.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [contexto opcional da demanda]
---

Voce foi acionado pelo comando `/rj-master` do plugin recuperacao-judicial-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** ativar a cadeia completa de operacao em Recuperacao Judicial/Falencia. EIXO PRIORITARIO: representacao do CREDOR, especialmente o CREDOR TRABALHISTA, em habilitacao de credito.

## PROTOCOLO

1. **Verificar configuracao** — procurar `recuperacao-judicial/cowork-state.json` subindo a arvore. Ausente → sugerir `/start-rj`; declinou → modo fallback.
2. **Acionar a skill `rj-master`** (Tier 0) — Hierarquia das 4 Camadas, 25 PAs + 11 PA-CTH, 8 Protocolos, roteamento.
3. **Detectar MODO CTH** — havendo lexico trabalhista (sentenca da JT, reclamatoria, verbas, FGTS, certidao de credito), ativar automaticamente o nucleo `credor-trabalhista-rj`.
4. **Saudar o operador** (advogado, OAB+UF, escritorio, cidade+UF, frentes, Revisao Tecnica).
5. **Conduzir** pelo pipeline: `triagem-rj` -> insumos (`auditoria-documental-rj` + `jurisprudencia-rj`) -> skill de producao conforme polo/via -> `revisao-final-rj` R1-R4 -> entrega + atualiza `CASO.md`.
6. Faltando dado essencial: sinalizar `[INFORMAR]`, nunca inventar. Validar norma vigente (L11.101 + L14.112).

**Skill a acionar:** `rj-master`.
