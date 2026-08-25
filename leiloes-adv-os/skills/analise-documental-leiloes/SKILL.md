---
name: analise-documental-leiloes
description: >
  Analise documental de leiloes Tier 1 — le e cruza edital, matricula, laudo, auto e carta, e devolve o que falta. Acione ao receber documentos de um leilao, antes de qualquer producao.
metadata:
  version: "0.1.0"
  area: "Leiloes e Arrematacao"
  tier: 1
---

# ANALISE DOCUMENTAL DE LEILOES

> Tier 1, Protocolo P2. Le os documentos, cruza-os entre si e devolve **o que falta**. Nao opina sobre viabilidade — isso e da `due-diligence-lote`.

## 1. CONVERTER ANTES DE LER

PDF apontado por caminho: converter com `ferramentas/pdf-para-md/pdf2md.py` e ler o `.md`. Excecoes (ler o PDF direto): assinatura, carimbo, selo, print, tabela cujo layout nao sobrevive ao texto, duvida sobre a digitalizacao. Numero critico vindo de OCR — processo, matricula, valor, data — se confere na pagina do PDF antes de entrar em peca.

## 2. OS DOCUMENTOS E O QUE EXTRAIR

| Documento | Extrair |
|-----------|---------|
| **Edital** | datas do 1º e 2º leilao, **data de divulgacao**, preco minimo, comissao, forma de pagamento, condicoes especiais e **a mencao de onus, recurso ou processo pendente (CPC 886, VI)** |
| **Matricula + certidao de onus** | proprietario, area, confrontacoes, **cada gravame com numero e data de registro** |
| **Laudo de avaliacao** | valor, data, metodo, estado do bem, se houve vistoria interna |
| **Autos da execucao** | penhora, intimacoes do art. 889, embargos, recursos, penhoras concorrentes |
| **Auto de arrematacao** | **data** (marco dos 10 dias), valor, assinaturas |
| **Carta de arrematacao** | descricao, remissao a matricula, prova do ITBI, **indicacao de onus (CPC 901, § 2º)** |
| **Via fiduciaria** | contrato, intimacao pessoal do devedor, certidao do RI, averbacao da consolidacao, editais dos dois leiloes |

## 3. O CRUZAMENTO (Protocolo P4)

O nucleo do trabalho: **edital x matricula x autos**.

- Onus que esta na matricula e **nao** esta no edital -> anotar em destaque. E a porta do art. 903, § 5º, I (desistencia em 10 dias).
- Area, confrontacoes e descricao do edital batem com a matricula?
- O executado foi intimado na forma do art. 889? E os credores com garantia averbada (inciso V) e o promitente comprador (inciso VI)?
- Na via fiduciaria: a intimacao pessoal foi regular? Houve o envio eletronico obrigatorio antes do edital (art. 26, § 4º-B)?

## 4. SAIDA

1. Ficha do lote com fonte de cada dado (doc. N, folha)
2. Quadro de onus, um a um, com registro e data
3. **Divergencias** entre os documentos, com o trecho exato
4. **O que falta** e o que cada falta impede de afirmar

Lacuna entra como `[INFORMAR]`; fato sem documento, como `[sem lastro documental]` (PA-02).
