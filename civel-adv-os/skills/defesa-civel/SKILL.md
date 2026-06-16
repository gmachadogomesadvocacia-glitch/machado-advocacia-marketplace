---
name: defesa-civel
description: >
  Tier 2 — defesa do REU no processo civil civel. Skill do LADO OPOSTO (PA-10): aciona quando o cliente
  e o reu/executado. CONTESTACAO (CPC 335-342) — prazo 15 dias uteis, onus da impugnacao especificada
  (CPC 341), preliminares processuais (CPC 337 — incompetencia, inepcia, litispendencia, coisa julgada,
  ilegitimidade, falta de interesse, conexao, convencao de arbitragem, etc.), prejudiciais de merito
  (prescricao e decadencia), merito, principio da EVENTUALIDADE/concentracao da defesa. RECONVENCAO
  (CPC 343 — pretensao propria conexa). Impugnacao ao CUMPRIMENTO DE SENTENCA (CPC 525) e EMBARGOS A
  EXECUCAO (CPC 914-920). REVELIA e seus efeitos/excecoes (CPC 344-346). Distribuicao do onus da prova
  (CPC 373; dinamica §1º). Ative em contestar, contestacao, defesa do reu, reconvencao, impugnacao ao
  cumprimento de sentenca, embargos a execucao, revelia ou resposta do reu. Se a materia for de outro
  plugin (consumo/familia/etc.), redigir a defesa la — rotear (PA-09).
metadata:
  version: "0.1.0"
  area: "Direito Civil e Processo Civil"
  tier: 2
---

# DEFESA CIVEL — CONTESTACAO E RESPOSTAS DO REU (CPC 335 e ss.)

> Tier 2, **lado do REU** (PA-10). O regime de fatos, o onus e a estrategia sao espelhados em relacao a inicial: nao se pede, **resiste-se**.

---

## 1. CONTESTACAO (CPC 335-342)

- **Prazo: 15 dias uteis** (CPC 335; termo inicial conforme a forma de citacao/audiencia de conciliacao CPC 334).
- **Concentracao da defesa / eventualidade** (CPC 336) — alegar de uma so vez **toda** a materia de defesa, ainda que subsidiaria/contraditoria (na duvida, em ordem de prejudicialidade).
- **Onus da impugnacao especificada** (CPC 341) — presumem-se verdadeiros os fatos nao impugnados (salvo excecoes: direitos indisponiveis, fato que so se prova por documento, contradicao com a defesa em conjunto). **Vedada a contestacao por negativa geral** (salvo curador/defensor/MP).

### 1.1 Estrutura (ordem)
1. **Preliminares** (CPC 337) — antes do merito, materia processual: incompetencia (absoluta/relativa), inepcia da inicial, perempcao, litispendencia, coisa julgada, conexao, incapacidade/irregularidade de representacao, convencao de arbitragem, ausencia de legitimidade ou interesse, falta de caucao, indevida concessao de gratuidade.
2. **Prejudiciais de merito** — **prescricao** e **decadencia** (PA-05; conhecem-se de oficio, mas alegar). Distinguir CC 205/206 (prescricao) de decadencia (CC 178 e prazos especificos).
3. **Merito** — impugnacao fatica (negar/versao propria) e juridica; fatos impeditivos, modificativos ou extintivos do direito do autor (CC; CPC 373 II).
4. **Provas** e requerimentos finais; impugnacao ao valor da causa (no corpo — CPC 293).

## 2. RECONVENCAO (CPC 343)

- Pretensao propria do reu, **conexa** com a acao ou com o fundamento da defesa; na **mesma peca** da contestacao; dispensa nova citacao (intima-se o autor-reconvindo na pessoa do advogado, 15 dias). Pode ampliar subjetivamente.

## 3. REVELIA (CPC 344-346)

- Efeito material: **presuncao relativa** de veracidade dos fatos alegados (CPC 344) — **nao incide** se ha pluralidade de reus contestantes, direito indisponivel, fato inverossimil/contrariado por prova, ausencia de documento essencial (CPC 345).
- Efeito processual: dispensa de intimacao do revel sem advogado (CPC 346); pode intervir a qualquer tempo recebendo o processo no estado.

## 4. IMPUGNACAO AO CUMPRIMENTO DE SENTENCA (CPC 525)

- Apos garantido/penhorado (ou no prazo de 15 dias do CPC 525, conforme o caso), materia **restrita** (CPC 525 §1º): falta/nulidade de citacao no processo que correu a revelia, ilegitimidade, inexequibilidade do titulo, penhora/avaliacao incorreta, excesso de execucao, causas extintivas **posteriores** a sentenca (pagamento, novacao, prescricao). Excesso → exige indicar o valor correto (CPC 525 §4º/§5º).

## 5. EMBARGOS A EXECUCAO (CPC 914-920)

- Execucao de titulo extrajudicial — **15 dias** da juntada do mandado/AR, **independem de penhora**; materia ampla (CPC 917); **sem efeito suspensivo automatico** (CPC 919 — exige garantia + fumus + periculum). (Detalhe em `execucao-titulo-extrajudicial`.)

## 6. ONUS DA PROVA (CPC 373)

- Autor: fato constitutivo (I). Reu: fato impeditivo, modificativo ou extintivo (II). **Distribuicao dinamica** (§1º) — pelo juiz, fundamentadamente, quando impossivel/excessivamente dificil a uma parte. Convencao das partes (§3º/§4º).

## 7. ESTRUTURA DA PECA (REU)

Enderecamento (mesmo juizo) · qualificacao do reu · **PRELIMINARES** (CPC 337) · **PREJUDICIAIS** (prescricao/decadencia) · **DO MERITO** (impugnacao especificada + fatos extintivos/impeditivos) · **(RECONVENCAO**, se houver) · impugnacao ao valor da causa/gratuidade · **DOS PEDIDOS** (acolher preliminares/extincao; no merito, improcedencia; sucumbencia ao autor) · **DAS PROVAS**.

## 8. INTEGRACAO

- `calculos-civeis` → excesso de execucao, valor correto na impugnacao (CPC 525 §4º — PA-06).
- `jurisprudencia-civel` → teses defensivas, prescricao (PA-01/PA-05).
- `analise-documental-civel` → documentos do reu, prova do fato extintivo.
- `estilo-juridico-civel` → forma · `revisao-final-civel` → R1-R4.

## 9. CHECKLIST DE SAIDA

- [ ] Prazo (15 dias uteis) e termo inicial corretos · concentracao da defesa (CPC 336)
- [ ] Impugnacao especificada — nenhum fato relevante sem resposta (CPC 341)
- [ ] Preliminares (CPC 337) e prejudiciais (prescricao/decadencia — PA-05) na ordem
- [ ] Reconvencao conexa, se cabivel (CPC 343) · via correta (impugnacao x embargos — PA-08)
- [ ] **Polo coerente — peca de REU, sem pedir o que cabe ao autor (PA-10)**
- [ ] Materia de outro plugin roteada (PA-09) · Selo P1 feito · R1-R4 pendente
