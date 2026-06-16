---
description: Due diligence imobiliaria e revisao de contrato (consultivo) — analise de matricula, certidoes, riscos, regularizacao e minuta/revisao contratual.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao do caso]
---

Voce foi acionado pelo comando `/due-diligence` do plugin imobiliario-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** conduzir a due diligence de um imovel ou a revisao/minuta de um contrato imobiliario na frente consultiva.

## PROTOCOLO
1. **Conferir a triagem** — `CASO.md` com o objetivo (aquisicao, locacao, garantia, financiamento), o imovel (matricula/endereco/area), as partes e o polo do cliente (PA-10).
2. **Analise dominial e de riscos** — matricula atualizada e cadeia dominial, onus reais (hipoteca, alienacao fiduciaria, usufruto, penhora, indisponibilidade), certidoes (negativas do vendedor — pessoais, trabalhistas, fiscais — para risco de fraude a credor/execucao), regularidade fiscal (IPTU/ITBI), regularidade edilicia (habite-se, averbacao da construcao) e condominial.
3. **TRAVA — posse x propriedade x dominio (PA-05)** — distinguir quem tem posse, quem tem o titulo e o que esta no registro; apontar divergencias como risco.
4. **Revisao/minuta de contrato** — clausulas de garantia (respeitar a vedacao a cumulacao de garantias — art. 37 — PA-08 na locacao), preco, condicao, multa, foro de eleicao e clausulas de risco; norma vigente (PA-04).
5. **Interfaces** — usucapiao (regularizacao por posse) -> `usucapiao-adv-os`; debitos de IPTU/ITBI ja em execucao fiscal -> `tributario-adv-os`; partilha/inventario do imovel -> `familia-sucessoes-adv-os`.
6. **Acionar a skill `due-diligence-imobiliaria`** para produzir o parecer/relatorio ou a minuta.
7. Ao final, submeter a `revisao-final-imobiliaria` (R1-R4).

**Skill a acionar:** `due-diligence-imobiliaria`.
