---
description: Monta o quadro de viabilidade de um caso candidato — precedente interno, faixa de quantum, tempo tipico e sinais de atencao — para o advogado decidir aceitar/propor. Sem probabilidade de exito (veda OAB).
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: <descricao do caso candidato>
---

Voce foi acionado pelo comando `/viabilidade-jurimetrica` do plugin jurimetria-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** apoio a decisao de negocio com o que os dados mostram de casos parecidos.

## PROTOCOLO

1. Colher do argumento (ou perguntar): area, tese, tribunal/orgao provavel, valor, polo.
2. **Acionar a skill `viabilidade-jurimetrica`** — as 4 pernas: precedente interno (caso a caso se N pequeno), faixa de quantum (`analise-quantum`), tempo tipico (`tempo-processual`), custo de oportunidade (dados do advogado).
3. Fechar com o item obrigatorio "O que os dados NAO dizem" — merito, prova, probabilidade.
4. Material para cliente/proposta: linguagem qualitativa + disclaimer + scanner de sigilo (P5).
5. **Auditar com `revisao-final-jurimetria`**; se o caso for aceito, sugerir `/instrumentar-caso` no nascimento.

**Skill a acionar:** `viabilidade-jurimetrica`.
