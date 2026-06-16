---
name: execucao-titulo-extrajudicial
description: >
  Tier 2 — execucao por quantia certa fundada em titulo executivo EXTRAJUDICIAL (CPC 783-784: cheque,
  nota promissoria, duplicata, letra de cambio, contrato assinado por 2 testemunhas, instrumento
  publico, confissao de divida, transacao referendada). Cobre os dois polos: EXEQUENTE/credor e
  EXECUTADO/devedor (defesa). Requisitos: certeza, liquidez e exigibilidade; citacao para pagar em 3
  dias (honorarios reduzidos a metade se paga); penhora, avaliacao, expropriacao; embargos a execucao
  (CPC 914-920, sem efeito suspensivo automatico — CPC 919); impenhorabilidade (CPC 833; bem de familia
  Lei 8.009). Inclui BUSCA E APREENSAO de bem alienado fiduciariamente (veiculo — DL 911/69: mora,
  notificacao/protesto, liminar, purgacao, consolidacao da propriedade, conversao em execucao). Ative
  em executar cheque/NP/duplicata/contrato, execucao de titulo extrajudicial, penhora, embargos a
  execucao, busca e apreensao, alienacao fiduciaria, DL 911 ou cobrar com titulo. Defesa do consumidor
  na busca e apreensao → rotear (PA-09).
metadata:
  version: "0.1.0"
  area: "Direito Civil e Processo Civil"
  tier: 2
---

# EXECUCAO DE TITULO EXTRAJUDICIAL + BUSCA E APREENSAO (CPC 783; DL 911/69)

> Tier 2. Side-aware: **EXEQUENTE/credor** x **EXECUTADO/devedor** (defesa). Peca e tom mudam (PA-10).
> **Eixo (PA-08):** so cabe execucao se ha titulo **liquido, certo e exigivel** (CPC 783). Sem isso → monitoria/cobranca (outra skill).

---

## 1. TITULO E REQUISITOS

- **Titulos extrajudiciais** (CPC 784): I cheque, letra de cambio, nota promissoria, duplicata, debenture; III contrato/instrumento particular assinado pelo devedor e **2 testemunhas**; II escritura/documento publico assinado pelo devedor; confissao de divida; transacao referendada (MP/Defensoria/advogados); credito de aluguel; etc.
- **Atributos** (CPC 783): **certeza** (existencia), **liquidez** (valor determinado/determinavel por calculo), **exigibilidade** (vencido, sem condicao pendente).
- **Prescricao do titulo** (PA-05): cheque 6 meses (apos prazo de apresentacao) para execucao; NP/letra 3 anos; depois cai para monitoria.

## 2. PROCEDIMENTO (EXEQUENTE)

1. Peticao inicial (CPC 798) com titulo + **demonstrativo do debito atualizado** (CPC 798 I "b").
2. Citacao para **pagar em 3 dias** (CPC 829). Pagamento integral nesse prazo → honorarios reduzidos pela metade (CPC 827 §1º).
3. Nao pago → **penhora** e avaliacao (CPC 831); ordem de bens CPC 835 (dinheiro/SISBAJUD primeiro); RENAJUD, INFOJUD.
4. Expropriacao: adjudicacao, alienacao por iniciativa particular, leilao (CPC 876+).
5. **Parcelamento** do executado (CPC 916) — deposito de 30% + 6 parcelas.

## 3. DEFESA DO EXECUTADO

- **Embargos a execucao** (CPC 914-920) — acao incidental, prazo **15 dias** da juntada do mandado/AR (CPC 915), **independem de penhora**; materia ampla (CPC 917: inexequibilidade do titulo, penhora incorreta, excesso, qualquer materia de defesa). **Sem efeito suspensivo automatico** (CPC 919) — exige garantia + fumus + periculum.
- **Excecao de pre-executividade** — materia de ordem publica conhecivel de oficio, sem dilacao probatoria (Sum. 393 STJ — validar).
- **Impenhorabilidade** (CPC 833): salario/proventos, bens de uso domestico, instrumentos de trabalho, pequena propriedade rural, etc.; **bem de familia** (Lei 8.009/90 — impenhorabilidade, salvo excecoes do art. 3º).

## 4. BUSCA E APREENSAO — ALIENACAO FIDUCIARIA (DL 911/69)

- **Cabimento** — inadimplemento do devedor em contrato com **garantia fiduciaria** (tipicamente veiculo financiado).
- **Mora** — comprova-se pela **notificacao extrajudicial** (carta com AR) ou **protesto** (Sum. 72 STJ — mora ex re, mas exige comprovacao — validar).
- **Liminar** (DL 911 art. 3º) — concedida a busca e apreensao; bem entregue ao credor.
- **Purgacao da mora / pagamento integral** — apos executada a liminar, o devedor paga a **integralidade da divida** (parcelas vencidas e vincendas) em **5 dias** para reaver o bem (art. 3º §2º — entendimento atual; **validar**).
- **Consolidacao** da propriedade e posse no credor (art. 3º §1º) se nao pago.
- **Conversao** em acao executiva (art. 4º) se o bem nao for encontrado/apreendido.
- **Defesa** (resposta em 15 dias, art. 3º §3º) — purgacao, descaracterizacao da mora, abusividade. Se for **consumidor**, rotear a defesa (PA-09).

## 5. ESTRUTURA DA PECA

**Execucao (exequente):** 1. Enderecamento (foro de eleicao/CPC 781 — lugar do cumprimento/domicilio do executado) · 2. Qualificacao · 3. Do titulo e do credito (certeza/liquidez/exigibilidade) · 4. Demonstrativo atualizado · 5. Pedidos (citacao p/ pagar em 3 dias; penhora; expropriacao; honorarios) · 6. Valor da causa (= credito) · 7. Provas/indicacao de bens.
**Busca e apreensao (credor):** enderecamento · contrato + comprovacao da mora (notificacao/protesto) · pedido de liminar · consolidacao · valor da causa = saldo devedor.

## 6. INTEGRACAO

- `calculos-civeis` → demonstrativo do debito, atualizacao, juros, prescricao do titulo (PA-06/PA-05).
- `jurisprudencia-civel` → Sum. 72, 393 STJ; teses do DL 911 (PA-01).
- `analise-documental-civel` → aferir titulo (2 testemunhas?), contrato fiduciario, notificacao.
- `estilo-juridico-civel` → forma · `revisao-final-civel` → R1-R4.

## 7. CHECKLIST DE SAIDA

- [ ] Titulo liquido/certo/exigivel (CPC 783) — senao, monitoria/cobranca (PA-08)
- [ ] Demonstrativo atualizado · Prescricao do titulo conferida (PA-05)
- [ ] B&A: mora comprovada (notificacao/protesto) antes da liminar (DL 911 — validar)
- [ ] Impenhorabilidade / bem de familia considerada (CPC 833; Lei 8.009)
- [ ] Defesa de consumidor roteada (PA-09) · Foro correto (P5)
- [ ] Polo coerente (PA-10) · Selo P1 feito · R1-R4 pendente
