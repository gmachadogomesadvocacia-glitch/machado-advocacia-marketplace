---
name: viabilidade-jurimetrica
description: >
  VIABILIDADE JURIMETRICA — Skill Tier 2, apoio a decisao de negocio: vale aceitar o caso? que esforco/proposta fazem sentido? Monta o dossie descritivo do caso candidato: precedente interno (casos semelhantes do acervo e como terminaram), faixa de quantum (analise-quantum), tempo tipico (tempo-processual/benchmark) e custo de oportunidade. Acione para "vale pegar este caso", "que proposta de honorarios fazer com base no historico", "ja tivemos caso parecido?", triagem de cliente novo com apoio de dados.
metadata:
  version: "0.1.0"
  area: "Jurimetria"
  tier: 2
---

# VIABILIDADE JURIMETRICA

> Skill **Tier 2**. A skill mais perto da fronteira proibida: apoio a decisao SIM, previsao de resultado NAO. O advogado decide; os dados so mostram o que ja aconteceu em casos parecidos (PE-02/PE-03).

---

## 0. ENTRADA

Descricao do caso candidato: area, tese pretendida, tribunal/orgao provavel, valor envolvido, polo. Vindo de outro plugin Adv-OS (triagem de area feita), aproveitar a classificacao.

## 1. AS QUATRO PERNAS DO DOSSIE

1. **Precedente interno** — dataset do acervo filtrado por area/assunto/tese semelhante: quantos casos, como terminaram, quantum pretendido x obtido, quanto tempo levaram. N pequeno e o normal aqui → apresentar caso a caso (qualitativo, PE-04), que e ate mais util para decidir.
2. **Faixa de valor** — `analise-quantum` no tema (bifasico: procedencia + valor entre procedentes).
3. **Tempo tipico** — `tempo-processual`/`benchmark-datajud` no orgao provavel: mediana e faixa dos concluidos, censura declarada.
4. **Custo de oportunidade** — horas/fases estimadas pelo proprio advogado (dado dele, nao dos scripts); a skill so organiza: tempo tipico x faixa de valor x regime de honorarios cogitado.

## 2. SAIDA — QUADRO DE VIABILIDADE

```
QUADRO DE VIABILIDADE — <caso candidato>
1. Precedente interno: [N casos semelhantes; desfechos um a um se N<limiar]
2. Faixa de quantum:   [fase 1 + fase 2, com Ns e fontes]
3. Tempo tipico:       [mediana/faixa dos concluidos no orgao, N, censura]
4. Sinais de atencao:  [o que nos casos passados azedou: tese barrada, orgao lento, reu insolvente...]
5. O que os dados NAO dizem: [merito do caso concreto, prova disponivel, probabilidade de exito]
Decisao: do advogado.
```

## 3. LINGUAGEM (a cerca de PE-03)

- PROIBIDO: "chance de exito de X%", "historicamente ganhamos", "provavel condenacao de R$ X".
- PERMITIDO: "dos N casos semelhantes fechados no acervo, A terminaram procedentes, B em acordo (coleta AAAA-MM-DD)"; "a faixa observada de quantum foi R$ X-Y".
- Em material para o CLIENTE (proposta): so linguagem qualitativa + disclaimer; scanner de sigilo antes de sair (P5). Honorarios sao decisao do advogado — a skill fornece a regua de tempo/valor, nao o preco.

## 4. ENCERRAMENTO

Entregar o quadro com as 4 pernas carimbadas e a fronteira explicita (item 5). Se o advogado aceitar o caso: `instrumentar-caso` ja no nascimento — o caso novo entra instrumentado e a jurimetria do futuro agradece.
