---
name: dano-fracionado-actio-nata
description: >
  DANO FRACIONADO E ACTIO NATA AUTONOMA — prescricao quando a parte fraciona os danos do mesmo evento medico em pretensoes com termos iniciais proprios (ex.: obito prescrito x "dano autonomo" descoberto anos depois). Aciona: dano autonomo, fracionamento de danos, actio nata, prescricao parcial, dano descoberto depois, agravamento x dano novo, prejudicial relegada ao merito.
metadata:
  version: "0.1.0"
  area: "Direito Medico"
  tier: 2
---

# DANO FRACIONADO E ACTIO NATA AUTONOMA

> Skill **Tier 2** (RC), irma da `prescricao-erro-medico`. Entra quando o caso tem MAIS DE UM dano alegado do mesmo evento, com datas de ciencia diferentes — o cenario em que a prescricao "meio prescrita" decide o litigio. Nasceu de caso real (obito perioperatorio prescrito + recorte de dano dito autonomo dentro do prazo).

---

## 0. QUANDO ACIONAR

(a) A parte adversa fraciona os danos para contornar prescricao consumada; (b) o cliente-autor descobriu dano novo apos a consumacao do prazo do dano original; (c) o saneador relegou a prejudicial de prescricao ao merito por causa do recorte; (d) qualquer caso com 2+ pretensoes indenizatorias do mesmo evento medico.

## 1. O TESTE DE AUTONOMIA (nucleo da skill)

Cada pretensao fracionada passa por 3 perguntas — responder POR DANO, em tabela:

1. **E dano DISTINTO ou desdobramento?** Dano autonomo = lesao a bem juridico diverso ou prejuizo novo que NAO era consequencia previsivel do dano original. Mero agravamento, sofrimento continuado ou nova repercussao do MESMO dano = a actio nata ja correu do dano original.
2. **Quando houve ciencia inequivoca DESTE dano e de sua extensao?** (actio nata subjetiva — Sum. 278 STJ por analogia). Ciencia de terceiro nao basta; ciencia parcial que ja permitia agir conta.
3. **A pretensao deste dano tem fundamento proprio** (nexo e prova proprios) ou depende integralmente da controversia do dano prescrito? Dependencia total e indicio de fracionamento artificial.

**Regra de bolso:** dano autonomo legitimo sobrevive sozinho — tem fato lesivo identificavel, data de ciencia propria e prova propria. Se para julga-lo o juiz precisa reabrir o merito do dano prescrito, a defesa tem tese forte de fracionamento artificial.

## 2. PRAZOS APLICAVEIS (remissao)

O prazo de CADA pretensao segue a `prescricao-erro-medico`: 3 anos CC art. 206 par.3 V (nao consumerista) x 5 anos CDC art. 27 (consumerista); Fazenda = Dec. 20.910/32. O que ESTA skill define e o TERMO INICIAL de cada uma. Suspensoes/interrupcoes (CC arts. 197-204) tambem se aferem por pretensao.

## 3. LADO AUTOR (fundamentar a autonomia)

- Narrar o dano novo com data e circunstancia da descoberta (documento da ciencia: exame, laudo, comunicacao).
- Demonstrar que antes da descoberta nao havia como agir (impossibilidade de conhecimento, nao mera inercia).
- Pedir por dano, com causa de pedir propria — nao "reabrir" o evento inteiro.
- Antecipar a defesa: explicar por que NAO e desdobramento do dano ja prescrito.

## 4. LADO REU (impugnar o fracionamento)

- Linha do tempo unica: evento -> ciencia do dano original -> consumacao do prazo -> ajuizamento. Situar cada "dano novo" nela.
- Atacar pelas 3 perguntas do teste: mesmo bem juridico? consequencia previsivel? ciencia anterior demonstravel (prontuario, e-mails, atendimentos posteriores)?
- Requerer que a prejudicial seja decidida por pretensao (prescricao PARCIAL) — a improcedencia do recorte nao depende do merito do prescrito.
- Cautela PA-02/PA-21: sustentar prescricao nao e prometer exito; manter defesa de merito subsidiaria (nexo, culpa, quantum) para o recorte sobrevivente.

## 5. QUANDO O SANEADOR RELEGA AO MERITO

Relegar a prescricao ao merito NAO e derrota: significa que a autonomia do dano e controvertida. Consequencias praticas: (a) a instrucao deve produzir prova da DATA DE CIENCIA (depoimento pessoal art. 385 CPC dirigido a isso; documentos de atendimentos posteriores); (b) quesitos periciais devem separar dano original x alegado dano novo; (c) razoes finais retomam o teste de autonomia com a prova colhida.

## 6. SAIDA

Tabela por pretensao: dano | autonomo? (teste 3 perguntas) | prazo | termo inicial (fonte da ciencia) | consumacao | situacao. Cada data com documento de origem (PA-13); o que nao tiver fonte fica `[PREENCHER]`. Passa por `revisao-final-medica` (R5 ataca pela linha do tempo adversa).

## 7. INTEGRACAO

Acionada por: `medico-master`, `triagem-medica`, `prescricao-erro-medico` (quando detecta 2+ danos). Alimenta: `responsabilidade-civil-medica` (defesa/peca), `especificacao-de-provas-medica` (prova da ciencia), `timeline-multiesfera`. Entrega para: `revisao-final-medica` (R1-R5).
