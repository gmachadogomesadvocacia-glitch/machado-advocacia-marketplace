---
name: estilo-juridico-leiloes
description: >
  Estilo juridico de leiloes Tier 1 — forma, voz e anti-rastro de IA nas pecas e pareceres do plugin. Acione ao redigir qualquer entrega antes da revisao final.
metadata:
  version: "0.1.0"
  area: "Leiloes e Arrematacao"
  tier: 1
---

# ESTILO JURIDICO DE LEILOES

> Tier 1. A forma do escritorio, aplicada ao dominio. Roda **antes** da `revisao-final-leiloes`.

## 1. VOZ

Peca enxuta, ancorada, sem rol prolixo. Documentos numerados "doc. N" e citados por numero. Combatividade dirigida a teses e fatos, nunca a pessoas.

**No PARECER a voz muda por completo, e isso e regra do escritorio (25/08/2026).** O
destinatario e o **cliente**, nao o juiz nem outro advogado. Objetivo, enxuto, em linguagem
que ele entende: a resposta no topo, 1 a 2 paginas, risco dito como consequencia pratica,
base legal em bloco final fora do texto. Se o cliente precisa de um advogado para traduzir o
parecer do advogado, o documento falhou. Estrutura completa em `due-diligence-lote` §5.

## 2. ANTI-RASTRO DE IA (obrigatorio)

- **Lexico proibido**: meta-comentario ("importante ressaltar", "cumpre salientar"); adjetivo de reforco vazio ("robusto", "cristalino", "resta evidente"); vocabulario de LLM ("crucial", "abordagem"); fecho-resumo; "(i), (ii), (iii)" na prosa.
- **Conectivo de esteira** ("Ademais", "Outrossim", "Destarte"): nenhum abre dois paragrafos seguidos; no maximo 3 paragrafos da peca comecam com conectivo.
- **Triade de adjetivos**: no maximo 1 por peca.
- **Ritmo**: pelo menos 2 paragrafos curtos de impacto (ate 30 palavras); quebrar frase acima de 60 palavras e paragrafo acima de 170.
- **Ancoragem**: todo fato com doc./fls./Id/data/valor; uma citacao literal curta entre aspas por secao de fatos; jurisprudencia com numero, relator, data e **so as duas linhas decisivas**, mais a aplicacao ao caso.

## 3. TIPOGRAFIA E ARQUIVO

Sem em-dash, aspas curvas, bullets decorativos, espaco duplo ou markdown vazando. **Datas, valores, Id e index em negrito.** `.txt` com **1 paragrafo = 1 linha**. Nome do arquivo terminando com a data de criacao `DD-MM-AAAA`.

## 4. VOCABULARIO DO DOMINIO — PRECISAO QUE IMPORTA

- **arrematacao** (leilao judicial) x **aquisicao em leilao** (fiduciario): nao sao sinonimos.
- **auto** de arrematacao (o ato) x **carta** de arrematacao (o titulo).
- **imissao na posse** (judicial, CPC 901, § 1º) x **reintegracao de posse** (fiduciario, L9.514, art. 30).
- **invalidacao** x **ineficacia** x **resolucao** (CPC 903, § 1º, I a III) — cada uma tem causa propria.
- **adjudicacao** (o credor fica com o bem) x **remicao** (o executado paga e resgata).
- **preco vil** so existe na via judicial.
