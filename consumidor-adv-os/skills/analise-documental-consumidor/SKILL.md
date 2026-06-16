---
name: analise-documental-consumidor
description: >
  ANALISE DOCUMENTAL CONSUMIDOR — Skill Tier 1 (Protocolo P2, Integridade Documental). Faz o
  inventario e a aferição de integridade dos documentos do caso, monta o mapa de documentos
  numerados "doc. N" pronto para citacao no texto e sinaliza documento essencial faltante como
  [INFORMAR] (PA-15) — sem ele nao se analisa o pedido. Acione apos a triagem e o Selo P1, antes
  de qualquer analise de merito; quando o usuario juntar contrato/fatura/extrato/print/protocolo,
  pedir para conferir os documentos, montar o indice de provas ou numerar docs. Gatilhos: tenho os
  documentos, anexei o contrato, segue a fatura/extrato, print do app, protocolo de atendimento,
  comprovante de negativacao, SPC/Serasa, bilhete aereo, nota fiscal, ordem de servico, indice de docs.
metadata:
  version: "0.1.0"
  area: "Direito do Consumidor e Bancario"
  tier: 1
---

# ANALISE DOCUMENTAL CONSUMIDOR

> Skill **Tier 1** — operacionaliza o **Protocolo P2 (Integridade Documental)**. Entrega o inventario, a checagem de integridade e o **mapa de documentos numerados "doc. N"** que alimenta toda a producao. Sem documento essencial, o pedido nao se analisa (**PA-15**).

---

## 0. QUANDO ACIONAR

Apos a `triagem-consumidor` e o **Selo P1** (`validador-legislacao-consumidor`), antes de `analise-contratual`, `analise-trilateral` e qualquer peca. Tambem quando chegam documentos novos a um caso ja aberto. PDFs de processo: no Code, converter com `ferramentas/pdf-para-md/` antes de analisar.

## 1. PRINCIPIO

Nenhum pedido se sustenta sem o documento que o lastreia (**PA-15**). O documento essencial **faltante** vira **Ponto de Omissao `[INFORMAR]`** — nunca se presume conteudo de documento ausente (**PA-03**: vedada a alucinacao fatica de contrato, valor, data, cobranca, inscricao). O resultado e gravado no `CASO.md` (**P3**).

---

## 2. CHECKLIST POR EIXO

Marque cada item: **PRESENTE** · **`[INFORMAR]`** (faltante) · **N/A**. Os itens em **negrito** sao essenciais — sua ausencia trava a analise do pedido correspondente.

### 2.1 Bancario / financeiro
- **Contrato de adesao** (mutuo, financiamento, cartao, cheque especial) assinado.
- **Faturas** / demonstrativos do cartao.
- **Extratos bancarios** do periodo.
- **CET (Custo Efetivo Total) / cedula de credito bancario** com taxas pactuadas.
- Comprovantes de pagamento das parcelas.
- Demonstrativo de evolucao da divida.

### 2.2 Negativacao
- **Comprovante de negativacao** — extrato SPC / Serasa / SCPC com data e valor.
- **Comprovante da divida (ou da sua inexistencia)** que originou a inscricao.
- Extrato consolidado para checagem da **Sumula 385 STJ** (inscricoes preexistentes legitimas — PA-07).
- Comprovante de pagamento / quitacao, se a tese for divida ja paga.

### 2.3 Telecom / servicos essenciais (energia, agua, gas)
- **Faturas** do servico.
- **Numero de protocolo de atendimento** das reclamacoes (com data/hora).
- **Prints de tela / app / site** do pedido de cancelamento ou contestacao.
- E-mails / SMS / gravacoes de atendimento.
- Comprovante de corte / suspensao do servico, quando houver.

### 2.4 Aereo (transporte)
- **Bilhete aereo + cartao de embarque**.
- **Comprovante dos gastos** decorrentes (hospedagem, alimentacao, transporte, recompra).
- Registro de irregularidade de bagagem (RIB/PIR), no extravio.
- Comunicacoes da companhia (atraso, cancelamento, no-show).

### 2.5 Vicio / fato do produto ou servico
- **Nota fiscal** da compra.
- **Termo de garantia** (legal e contratual).
- **Ordem de servico** / comprovante de envio a assistencia tecnica (marca os 30 dias do art. 18).
- Fotos / laudos do defeito; em fato do produto, prova do dano e do nexo.

### 2.6 E-commerce / compra online
- **Comprovante da compra** e do pagamento.
- **Prints** da oferta, do site e da confirmacao do pedido.
- Registro da data de recebimento (marca os 7 dias do **arrependimento, art. 49** — so fora do estabelecimento).
- E-mails de confirmacao / rastreamento.

### 2.7 Transversais (todo caso)
- Documento de identidade e comprovante de residencia do cliente (foro — art. 101, I CDC).
- Procuracao e declaracao de hipossuficiencia (se gratuidade).
- Numero(s) de protocolo de atendimento de todas as tratativas.

---

## 3. AFERICAO DE INTEGRIDADE

Para cada documento PRESENTE, verifique:
1. **Legibilidade** — completo, sem paginas faltando, datas/valores visiveis.
2. **Autoria e data** — quem emitiu e quando; print precisa de URL/data/hora visiveis.
3. **Pertinencia** — o documento prova mesmo o fato alegado (ex.: extrato cobre o periodo da cobranca).
4. **Cadeia** — documentos que se referenciam batem entre si (fatura x extrato x contrato).

Documento ilegivel ou parcial conta como faltante → `[INFORMAR]`.

---

## 4. SAIDA — MAPA DE DOCUMENTOS "doc. N"

Numere em ordem logica (cronologica ou por tese), para citacao direta no corpo da peca ("...conforme doc. 3"), no padrao enxuto do escritorio (docs numerados antes do protocolo, citados por numero, sem rol prolixo).

```
MAPA DE DOCUMENTOS
doc. 1  — Contrato de adesao (cartao), 12 fls. ......... PRESENTE
doc. 2  — Faturas jan–jun/2026 ........................ PRESENTE
doc. 3  — Extrato Serasa 03/06/2026 (negativacao) ..... PRESENTE
doc. 4  — Comprovante de quitacao da divida ........... [INFORMAR]
...
ESSENCIAIS FALTANTES (travam o pedido): doc. 4
```

## 5. CHECKPOINT

Apresente o mapa e a lista de essenciais faltantes. **Havendo essencial `[INFORMAR]`, pare e peca o documento antes de avancar** para `analise-contratual` ou para a producao (PA-15). Atualize o `CASO.md` via `memoria-de-caso-consumidor` (**P3**) com o mapa e o status dos prazos (decadencia art. 26 / prescricao art. 27 / arrependimento art. 49) que os documentos permitirem aferir.

## 6. ENCERRAMENTO

Entrega: inventario por eixo, aferição de integridade, mapa "doc. N" pronto para citacao e a lista de essenciais faltantes. Roteia para `analise-contratual-consumidor` (cacar clausulas abusivas) e devolve os Pontos de Omissao a `revisao-final-consumidor` (R1).
