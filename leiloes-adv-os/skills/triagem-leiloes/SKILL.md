---
name: triagem-leiloes
description: >
  Triagem de leiloes Tier 1 — porta de entrada de todo caso. Classifica em 4D, fixa o rito, emite o Selo de Validacao de Norma Vigente e crava os prazos. Acione no inicio de qualquer caso de leilao ou arrematacao.
metadata:
  version: "0.1.0"
  area: "Leiloes e Arrematacao"
  tier: 1
---

# TRIAGEM DE LEILOES

> Tier 1. Primeira skill operacional. **Nada se produz antes dela + Selo P1.**

---

## PASSO ZERO — O POLO (bloqueante)

Antes de qualquer classificacao: **o cliente compra ou perde o bem?**

- **Compra** (arrematante consumado ou pretendente) -> segue.
- **Perde, cobra ou vende** (executado, devedor fiduciante, exequente, credor fiduciario) -> **PARE**. Roteie conforme a tabela do `leiloes-master` §0 e registre o roteamento. Nao produza nada aqui (PA-12).
- **Nao esta claro** -> pergunte. Nao presuma.

---

## 1. AS 4 DIMENSOES

**D1 — POLO**
`arrematante consumado` · `pretendente (pre-lance)`

**D2 — VIA**
`judicial - leilao` (CPC 879-908) · `judicial - VENDA DIRETA` (CPC 880; na Justica do
Trabalho, via coordenadoria de execucao, como a CAEX do TRT-1) · `extrajudicial fiduciario`
(Lei 9.514/97 c/ Lei 14.711/2023)

**Sinais da venda direta:** o proprio titulo do edital ("Edital de Venda Direta"),
coordenadoria de execucao no cabecalho (CAEX, CEJUSC-JT, nucleo de execucao), mencao a
"propostas nos autos" em dias determinados, e percentual de partida fixado (40% e usual).
**Se for venda direta, a primeira coisa a dizer ao cliente e que ele nao pode ofertar
sozinho** — depende de leiloeiro ou corretor credenciado no tribunal.

**D3 — FASE** (define a peca cabivel)

| Fase | Marco | Porta |
|------|-------|-------|
| Pre-lance | ainda nao deu lance | `due-diligence-lote` |
| Arrematado sem carta | auto assinado | `defesa-da-arrematacao` · `invalidacao-arrematacao` |
| Carta expedida sem posse | carta expedida | `imissao-na-posse-arrematante` |
| Posse com litigio residual | imitido, mas ha ocupante ou cobranca | `desocupacao-e-ocupantes` · `debitos-e-onus-propter-rem` |
| Desfazimento | quer desfazer ou foi evicto | `invalidacao-arrematacao` |

**D4 — OBSTACULO**
`onus e debitos` · `ocupacao` · `vicio do edital ou da intimacao` · `ataque do executado` · `inadimplemento do proprio arrematante`

---

## 2. O RITO (so na via judicial) — DEFINE OS PRAZOS

Identificar **antes** de calcular qualquer coisa: **civel (CPC)** · **fiscal (Lei 6.830/80)** · **trabalhista (CLT 888)** · **SFH (Lei 5.741/1971)**. Tabela comparativa no `leiloes-master` §4.

Sinais: numero do processo e vara; Fazenda no polo ativo (fiscal); Vara do Trabalho (CLT 888, com sinal de 20% e pagamento em 24 horas); **CEF ou agente do SFH no polo ativo + Justica Federal + "execucao hipotecaria" + mencao a Lei 5.741/1971 (rito do SFH)**.

**PERGUNTA OBRIGATORIA NO RITO DO SFH:** qual e o **saldo devedor** e qual e a **avaliacao**? O piso e o saldo (art. 6º), nao a avaliacao. Se o saldo superar o valor do imovel, a operacao ja nasce inviavel para o arrematante e o desfecho provavel e a adjudicacao ao credor (art. 7º) — dizer isso ao cliente **antes** de qualquer outro exame.

---

## 3. SELO DE VALIDACAO DE NORMA VIGENTE (P1)

Nao se emite o Selo sem responder:

1. **Qual a data de divulgacao do edital?** Decide a modulacao do **Tema 1.134** (tributos).
2. **Qual CPC rege o ato?** Interfere direto na sub-rogacao do condominio (REsp 1.769.443).
3. **Na via fiduciaria, qual a data do contrato e da consolidacao?** A Lei 14.711/2023 mudou prazos, referencial do 2º leilao e saldo remanescente; o **Tema 1.288** separa antes/depois da Lei 13.465/2017.
4. **O Tema 886 segue em revisao?** Se sim, nenhuma afirmacao definitiva sobre condominio.

Normas validadas entram no `CASO.md` com data. Fonte unica: a curadoria juridica do plugin.

---

## 4. PRAZOS — CRAVAR NA TRIAGEM, NAO DEPOIS

| Prazo | Marco | Base |
|-------|-------|------|
| **10 dias** — invalidacao/ineficacia/resolucao | aperfeicoamento da arrematacao | CPC 903, § 2º |
| **10 dias** — **desistencia por onus nao mencionado no edital** | prova do onus | CPC 903, § 5º, I |
| Apos a carta: so acao autonoma | expedicao da carta | CPC 903, §§ 3º e 4º |
| **24 horas** — pagamento (trabalhista) | arrematacao | CLT 888, § 4º |
| **15 dias** — purgacao (fiduciario) | intimacao | L9.514, art. 26, § 1º |
| **60 dias** — leilao apos consolidacao | registro da consolidacao | L9.514, art. 27 |
| **60 dias** — desocupacao na reintegracao liminar | decisao | L9.514, art. 30 |

Se houver prazo de 10 dias em curso, **urgencia maxima**: rotear de imediato, antes de qualquer outra producao (PA-11).

---

## 5. CONFERENCIA DO LANCE (quando pre-lance)

- **Impedidos de arrematar** (CPC 890): o cliente e tutor, curador, mandatario, servidor da justica na localidade, leiloeiro, preposto — **ou advogado de alguma das partes**? Se sim, o lance e nulo (PA-10).
- **Preco vil** (CPC 891): inferior ao minimo do edital ou, sem minimo, a 50% da avaliacao. **Nao se aplica ao fiduciario.**
- **Capacidade de pagamento no prazo do rito.**

---

## 6. SAIDA DA TRIAGEM

Gravar no `CASO.md`: as 4 dimensoes, o rito, o Selo (status, normas, data), os prazos com data-limite, os impedimentos conferidos e as lacunas como `[INFORMAR]` — nunca inventadas (PA-02).

**Rotear** para `analise-documental-leiloes` (edital + matricula) e para a skill de producao da fase. Lembrar a Revisao R1-R4 antes de qualquer entrega.
