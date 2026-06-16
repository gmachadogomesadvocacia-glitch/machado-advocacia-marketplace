---
name: estilo-juridico-isencao-ir
description: >
  ESTILO JURIDICO ISENCAO-IR — Skill Tier 1 transversal (Camada 3). Define o padrao de redacao de TODA
  peca de isencao de IRPF por doenca grave: FIRAC, enxuto, docs "doc. N", antecipacao adversarial dura
  (enquadramento no rol; so proventos; contemporaneidade Sum. 627; prova Sum. 598; prescricao 5 anos),
  valor da restituicao quantificado. TOM firme mas HUMANO — o cliente e pessoa doente. Protege o dado de
  saude (PA-10): segredo de justica quando necessario, sem expor CID alem do indispensavel. Apoia toda a
  producao. Acione ao redigir/revisar a forma de qualquer peca, requerimento, MS ou parecer de isencao.
metadata:
  version: "0.1.0"
  area: "Isencao de IRPF por Doenca Grave"
  tier: 1
---

# ESTILO JURIDICO ISENCAO-IR

> Skill **Tier 1 transversal** (Camada 3). Padroniza a FORMA de toda producao. Nao decide tese (isso e da linha estrategica) — garante redacao enxuta, FIRAC, antecipacao adversarial e **tom humano**, protegendo o dado de saude.

---

## 1. FIRAC POR BLOCO
Cada tese segue **F**ato → **I**ssue → **R**egra → **A**plicacao → **C**onclusao. Estrutura padrao da peca: enderecamento, qualificacao, fatos (doenca + provento + retencao), direito (art. 6 XIV + Sum. 598/627), pedidos (declaratorio de isencao + repeticao de indebito dos 5 anos + tutela/cessacao + isencao futura), valor da causa, requerimentos.

## 2. ENXUTO
- Peca curta e direta; um argumento por bloco; sem rol prolixo de jurisprudencia.
- Periodos curtos. Sem floreio. Cada paragrafo entrega um ponto.

## 3. DOCS "doc. N"
- Documentos numerados **antes do protocolo** e citados no corpo por numero: "conforme **doc. N**".
- Sequencia tipica: doc. 1 laudo; doc. 2 carta de concessao; doc. 3 informes de rendimento/IR retido; doc. 4 DIRPF; procuracao por ultimo.

## 4. ANTECIPACAO ADVERSARIAL (dura)
Neutralizar, no corpo, as quatro defesas da Fazenda/fonte:
1. **Enquadramento no rol** — afirmar a doenca como item do art. 6 XIV (PA-05); nunca forcar molestia de fora.
2. **So PROVENTOS** (PA-06) — delimitar que o pedido recai apenas sobre aposentadoria/pensao/reforma, antecipando a alegacao de que seria rendimento de ativo.
3. **Contemporaneidade — Sumula 627 STJ** (PA-08) — a isencao independe de sintomas atuais ou recidiva; vale em remissao.
4. **Prova — Sumula 598 STJ** (PA-07) — no judicial dispensa laudo OFICIAL; a doenca prova-se por outros meios.
+ **Prescricao 5 anos** — antecipar e limitar a restituicao aos ultimos 5 anos (CTN art. 168 — PA-09).

## 5. VALOR DA RESTITUICAO QUANTIFICADO
A peca deve trazer o **valor do indebito** dos 5 anos (calculo de `calculos-isencao-ir`, com Selic) e refletir no valor da causa. Sem comprovantes de retencao → `[INFORMAR]`, nao estimar no escuro (PA-03).

## 6. TOM — FIRME, HUMANO
Combatividade dirigida a teses, nunca a pessoas. **Sensibilidade**: o autor e uma pessoa doente — tom respeitoso, sobrio, sem dramatizacao gratuita nem frieza tecnica. Nunca opinar sobre conduta clinica/diagnostico (PA-04).

## 7. PROTECAO DO DADO DE SAUDE (PA-10)
- Pedir **segredo de justica** quando a exposicao do quadro for necessaria ao pedido.
- Expor o CID/diagnostico **apenas no indispensavel** ao enquadramento; o restante por referencia ao laudo (doc. N). LGPD art. 11 + sigilo.

## 8. APLICACAO
Esta skill apoia TODA producao: `requerimento-administrativo-isencao`, `retificacao-dirpf`, `acao-isencao-ir`, `mandado-seguranca-isencao`, `manutencao-isencao`. Antes da entrega, a forma e auditada na R4 da `revisao-final-isencao-ir` (PA-14).

## 9. ENCERRAMENTO
Entrega o padrao de redacao — FIRAC, enxuto, docs numerados, antecipacao adversarial dura, restituicao quantificada, tom humano e dado de saude protegido — para uniformizar toda peca do plugin.
