---
name: memoria-de-caso-leiloes
description: >
  Memoria de caso de leiloes Tier 1 — mantem CASO.md e MEMORY.md vivos e compartimentados. Acione ao abrir caso novo e sempre que houver decisao, prazo, peca ou documento novo.
metadata:
  version: "0.1.0"
  area: "Leiloes e Arrematacao"
  tier: 1
---

# MEMORIA DE CASO DE LEILOES

> Tier 1, Protocolo P3. O `CASO.md` e a **fonte unica** das variaveis; todas as skills leem dali.

## 1. ESTRUTURA

```
<CASE_ROOT>/<slug>/
   CASO.md       estado vivo (4D, rito, Selo, prazos, lote, edital, onus)
   MEMORY.md     diario de decisoes e historico
   arquivos/     edital, matricula, laudo, autos, auto e carta
   pecas/        producao
```
Pasta **compartilhada** entre plugins do mesmo cliente.

## 2. O QUE ATUALIZAR, E QUANDO

| Evento | Onde |
|--------|------|
| Triagem concluida | 4D + rito + Selo no `CASO.md` |
| Edital cruzado com matricula | quadro de onus + divergencias |
| **Auto de arrematacao assinado** | data + **data-limite dos 10 dias** em destaque |
| Carta expedida | data; a partir daqui, so acao autonoma |
| Decisao estrategica | `MEMORY.md`, com o porque |
| Peca produzida | `pecas/` + registro |
| Documento novo | `arquivos/` numerado "doc. N" |

## 3. REGRAS DURAS

- **Prazo nunca fica so na cabeca**: entra com data-limite no calendario (PA-11).
- Lacuna vira `[INFORMAR]`; fato sem documento, `[sem lastro documental]`.
- **Compartimentacao (PA-13)**: dado de um caso nao migra para outro. Achado de um processo so se reusa depois de conferido nos autos do novo.
- Data relativa vira data absoluta ("ontem" -> `23/08/2026`).
