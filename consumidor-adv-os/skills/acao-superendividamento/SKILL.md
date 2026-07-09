---
name: acao-superendividamento
description: >
  ACAO SUPERENDIVIDAMENTO — Skill Tier 2 (lado consumidor). Acione quando o cliente esta superendividado de boa-fe, nao consegue pagar o conjunto das dividas sem comprometer a subsistencia, ou pede repactuacao, plano de pagamento, renegociacao global, conciliacao com credores. Exige Selo P1 emitido.
metadata:
  version: "0.1.0"
  area: "Direito do Consumidor e Bancario"
  tier: 2
---

# ACAO SUPERENDIVIDAMENTO

> Skill **Tier 2** — lado consumidor. Repactuacao de dividas da **Lei 14.181/2021** (CDC arts. 54-A a 54-G e 104-A a 104-C). So roda apos a triagem, o Selo P1 e a linha estrategica. Polo do cliente = consumidor (PA-05); se credor/fornecedor, a frente e a defesa em conciliacao via `contestacao-consumidor`.

---

## 0. PRE-REQUISITOS

- Polo do cliente = **consumidor** pessoa fisica de **boa-fe** (PA-05).
- **Selo de Validacao Legal Previa EMITIDO** (P1). Sem ele, nao redigir.
- CASO.md com partes, eixo (superendividamento), esfera, rito e o **rol completo de dividas**. Falta de extrato/contrato/divida essencial → `[INFORMAR]` (PA-15).

## 1. CONCEITO E ELEGIBILIDADE (art. 54-A)

- **Superendividamento:** impossibilidade manifesta de o consumidor pessoa fisica, de **boa-fe**, pagar a totalidade de suas dividas de consumo, exigiveis e vincendas, sem comprometer o **minimo existencial** (art. 54-A, § 1º).
- Abrange dividas de consumo, presentes e futuras, com ou sem garantia.
- **Boa-fe e pressuposto:** o regime nao socorre quem se endividou por dolo ou ma-fe (art. 54-A, § 3º, parte final). Anteciparse a essa tese e travar o enquadramento.

### O que NAO entra na repactuacao (art. 54-A, § 3º)
- Dividas com **garantia real**;
- Dividas de **financiamento imobiliario**;
- Dividas de **credito rural**;
- Dividas com **garantia fiduciaria** / contratos de **alienacao fiduciaria**;
- Dividas decorrentes de aquisicao de **produto ou servico de luxo** de alto valor.

> Confira o enquadramento dessas exclusoes antes de listar a divida no plano (PA-15). Divida excluida fica fora da repactuacao global, mas o cenario completo deve constar para aferir o minimo existencial.

## 2. MINIMO EXISTENCIAL (PA-14)

- O plano de pagamento **nunca pode comprometer o minimo existencial** — nucleo da Lei 14.181 (PA-14).
- Parametro regulamentar: **Decreto 11.150/2022** `[VERIFICAR]` (validar vigencia e percentual atual via `validador-legislacao-consumidor` — PA-01/P1; o conteudo e objeto de revisao normativa).
- Demonstrar no caso concreto a renda liquida, despesas essenciais e a margem efetivamente disponivel para o plano.

## 3. VEDACAO AO ASSEDIO DE CONSUMO (arts. 54-C e 54-D)

- E vedado assediar/pressionar o consumidor, sobretudo idoso, analfabeto ou vulnerável, para contratar credito (art. 54-C).
- O fornecedor de credito deve avaliar a capacidade de pagamento e prestar informacao adequada (art. 54-D). A oferta irresponsavel de credito sustenta a revisao/modulacao da divida.

## 4. VIA PROCESSUAL — REPACTUACAO (art. 104-A)

1. **Peticao de instauracao** do processo de repactuacao, a pedido do consumidor, com a **lista de TODOS os credores** e o plano que se pretende.
2. **Audiencia conciliatoria GLOBAL** — o juiz designa audiencia reunindo **todos os credores** em conjunto. O consumidor apresenta proposta de **plano de pagamento com prazo de ate 5 anos**, preservado o minimo existencial e o pagamento integral do principal.
3. **Acordo homologado** vale como titulo executivo e novacao especifica; descumprimento sem justificativa permite execucao ou requerimento do art. 104-B.
4. **Credor ausente/recusante:** sua divida tem exigibilidade suspensa e a remuneracao do credito interrompida ate apresentar-se, conforme o regime do art. 104-A.

## 5. PLANO COMPULSORIO (art. 104-B)

- Se a **conciliacao do art. 104-A for total ou parcialmente frustrada**, abre-se, a requerimento do consumidor, o processo por **superendividamento para revisao e integracao dos contratos e repactuacao compulsoria**.
- O juiz, com auxilio de **administrador/conciliador**, instaura plano judicial compulsorio com os credores remanescentes, assegurados o minimo existencial e o prazo legal, podendo prever medidas de dilacao, reducao de encargos e suspensao/extincao de garantias quando cabivel.

## 6. ESTRUTURA DA PECA (FIRAC + estilo do escritorio)

1. **Enderecamento** — Juizo competente (foro do domicilio do consumidor, art. 101, I CDC; rito conforme P5).
2. **Qualificacao** — consumidor (boa-fe) e **todos os credores**.
3. **Dos Fatos** — origem do endividamento, boa-fe, renda e despesas; cada documento como **"doc. N"**.
4. **Do Direito** — FIRAC por tese: enquadramento no art. 54-A; minimo existencial (PA-14); boa-fe; eventual assedio/credito irresponsavel (54-C/54-D); exclusoes do § 3º afastadas/identificadas; antecipacao adversarial (ma-fe, divida excluida, capacidade de pagamento).
5. **Da Proposta de Plano** — plano de pagamento ate 5 anos, com quadro divida × credor × parcela, preservado o minimo existencial.
6. **Dos Pedidos** — instauracao da repactuacao (104-A), designacao de audiencia global, homologacao do plano; subsidiariamente o plano compulsorio (104-B); suspensao de cobrancas/negativacao no curso; gratuidade se cabivel.
7. **Do Valor da Causa** e **Requerimentos finais** — citacao de todos os credores, provas, intimacoes.

## 7. CHECKLIST ANTES DE ENTREGAR

- [ ] Polo coerente (PA-05) · Selo P1 citado · boa-fe demonstrada
- [ ] Minimo existencial preservado (PA-14) · Decreto 11.150/2022 `[VERIFICAR]`
- [ ] **Todos os credores** listados · plano ate 5 anos · exclusoes do § 3º checadas
- [ ] Sumula/Tema citados como `[VERIFICAR]` + `jurisprudencia-consumidor` (PA-01)
- [ ] Antecipacao adversarial · docs numerados "doc. N"
- [ ] Submeter a `revisao-final-consumidor` (R1-R4) antes da entrega (PA-22)

## 8. ENCERRAMENTO

Entrega o pedido de repactuacao enxuto, com enquadramento no art. 54-A, minimo existencial preservado, plano global ate 5 anos e a via compulsoria do art. 104-B em subsidiario, pronto para a Suprema Corte R1-R4.
