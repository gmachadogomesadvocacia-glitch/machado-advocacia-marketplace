---
name: especificacao-de-provas-medica
description: >
  ESPECIFICACAO DE PROVAS MEDICA — peca de especificacao/justificacao de provas em litigio medico
  (apos saneador ou despacho de especificacao, CPC arts. 348-357 e 369-380). Estrutura canonica:
  cada prova requerida com finalidade e pontos controvertidos que alcanca; pericia (arts. 464-465)
  como prova central do nexo, SEMPRE com pedido subsidiario de pericia como prova PROPRIA (nao so
  adesao a pericia da parte adversa) e custeio do reu hipossuficiente (CPC arts. 95 par.3, 98 par.5,
  99 par.3); depoimento pessoal sob pena de confissao (art. 385); renuncia a testemunhas como
  decisao estrategica registrada. Aciona: especificar provas, justificar provas, despacho de provas,
  saneamento, quais provas requerer, protesto generico por provas.
metadata:
  version: "0.1.0"
  area: "Direito Medico"
  tier: 2
---

# ESPECIFICACAO DE PROVAS MEDICA

> Skill **Tier 2** processual. A especificacao de provas parece burocratica e decide instrucoes inteiras: prova nao requerida = preclusao; prova requerida sem finalidade = indeferimento. Nasceu de caso real em que a peca foi resolvida sem chassi — e a auditoria R5 pegou exposicao estrategica que virou regra aqui.

---

## 0. QUANDO ACIONAR

Despacho de especificacao/justificacao de provas ou saneador (CPC art. 357) abrindo prazo para as partes. Vale para qualquer esfera civel do plugin (RC, plano de saude, contratos). Prazo tipico de 5-15 dias — conferir a intimacao `[VERIFICAR prazo no processo]`.

## 1. ANTES DE REDIGIR (leitura obrigatoria)

1. **O que o saneador fixou:** pontos controvertidos, onus de cada parte, prejudiciais relegadas ao merito. A peca especifica prova PARA os pontos fixados — prova sem ponto controvertido correspondente e inutil.
2. **O CASO.md:** teses vivas, lacunas de prova mapeadas na `analise-prontuario-medico`, datas em disputa (ciencia/actio nata — ver `dano-fracionado-actio-nata`).
3. **O que a parte adversa ja requereu** — define as jogadas defensivas do item 4.

## 2. ESTRUTURA CANONICA DA PECA

```
1. ENDERECAMENTO + numero do processo
2. REFERENCIA ao despacho/saneador (ID/evento) e ao prazo
3. PROVAS REQUERIDAS — uma secao por prova, cada uma com:
   (a) a prova; (b) FINALIDADE especifica; (c) ponto controvertido que alcanca
4. PROTESTO ESPECIFICO (nunca generico) por prova complementar sobre fato novo
5. FECHO, data, OAB
```

Regra do plugin: cada prova amarrada a um ponto controvertido, com finalidade dita em uma frase. "Protesta por todos os meios de prova" e vedado — generico nao preserva nada e sinaliza despreparo.

## 3. O ARSENAL TIPICO DO LITIGIO MEDICO

| Prova | Finalidade tipica | Base |
|-------|-------------------|------|
| **Pericia medica** | nexo causal, adequacao da conduta, autonomia de dano | CPC 464-465 |
| Juntada de prontuario COMPLETO | suprir lacunas de evolucao, autoria de atos | CPC 435 p.u. |
| Depoimento pessoal da parte adversa | data de ciencia (actio nata), fatos pessoais | CPC 385 (pena de confissao) |
| Testemunhas (equipe, acompanhantes) | dinamica do atendimento | CPC 442+ |
| Oficios (operadora, hospital, CRM) | escalas, protocolos institucionais, vinculos | CPC 438 |
| Prova tecnica simplificada | ponto de menor complexidade | CPC 464 par.2-4 |

Quesitos e assistente tecnico: ao ser deferida a pericia, acionar `analise-pericia-medica` (quesitos entram no prazo do art. 465 par.1, nao nesta peca — mas ja planejar).

## 4. AS DUAS REGRAS DE OURO DO REU (licoes da R5)

1. **Nunca so ADERIR a pericia requerida pela parte adversa.** Jogada adversa classica: desistir da pericia e pedir julgamento antecipado com inversao do onus — o reu fica sem prova tecnica. Blindagem de uma linha: "caso a parte autora desista da prova pericial, requer-se desde ja a pericia como prova propria da re".
2. **Reu hipossuficiente custeia como?** Pedir na mesma linha: gratuidade limitada ao ato (CPC art. 98 par.5), parcelamento (art. 98 par.6), remuneracao de perito conforme art. 95 par.3 (recursos do Estado quando beneficiario da gratuidade) e reducao equitativa (art. 99 par.3 c/c 98). Sem isso, a pericia propria vira onus impagavel.

## 5. RENUNCIA A PROVA E DECISAO ESTRATEGICA

Abrir mao de testemunhas/depoimento pode ser correto (encurtar instrucao quando a prova documental+pericial basta) — mas e DECISAO DO OPERADOR: registrar no CASO.md com data e motivo (PA-01: o advogado decide; a skill apresenta o trade-off). O mesmo vale para nao requerer prova cuja producao possa favorecer a tese adversa.

## 6. SIGILO E LGPD

Prontuario e dado sensivel: requerer segredo de justica se ainda nao decretado `[VERIFICAR]`; juntar prontuario pela via dos autos (nunca no plugin — PA-16); anonimizar terceiros nao-parte quando possivel.

## 7. INTEGRACAO

Acionada por: `medico-master`, saneador no CASO.md. Consome: `analise-prontuario-medico` (lacunas), `dano-fracionado-actio-nata` (prova da ciencia), `linha-estrategica` do caso. Entrega para: `revisao-final-medica` (R1-R5 — o R5 testa as jogadas adversas do item 4).
