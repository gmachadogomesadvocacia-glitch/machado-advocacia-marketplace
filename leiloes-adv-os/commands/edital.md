---
description: Analisa o edital: vicios e clausulas invalidas.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [edital]
---

Voce foi acionado pelo comando `/edital` do plugin leiloes-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** separar o que o edital pode impor do que e invalido.

## PROTOCOLO
1. Converter o PDF com `pdf-para-md` e ler o edital **inteiro** — nunca o resumo do site do leiloeiro.
2. Acionar `analise-edital-leilao`.
3. Conferir o conteudo obrigatorio do **CPC 886**, com atencao ao **inciso VI** (mencao de onus, recurso ou processo pendente) e o prazo de publicidade do **rito** (5 dias CPC · 10 a 30 fiscal · 20 trabalhista).
4. Marcar as clausulas invalidas: atribuicao de tributos anteriores ao arrematante (CTN 130, p.u. + Tema 1.134), afastamento da sub-rogacao do art. 908, § 1º, supressao da desistencia do art. 903, § 5º, dispensa das cientificacoes do art. 889.
5. Se o edital **omitiu onus** que consta da matricula e ja houve arremate, abrir a resposta com a **data-limite dos 10 dias** do art. 903, § 5º, I.
6. Entregar quadro clausula -> valida/invalida -> base -> efeito no custo ou no risco.

**Skill a acionar:** `analise-edital-leilao`.
