---
name: analise-documental-imobiliaria
description: >
  Analise documental imobiliaria Tier 1 — Protocolo P2 (Integridade Documental). Checklist de
  integridade e extracao de dados-chave dos documentos do caso: matricula atualizada (cadeia dominial,
  onus reais — hipoteca, alienacao fiduciaria, penhora, usufruto, averbacoes), contrato (locacao,
  promessa, compra e venda — partes, objeto, prazo, valor, garantia, foro de eleicao), certidoes
  (negativas de onus, IPTU, acoes reais e pessoais reipersecutorias, do vendedor), convencao de
  condominio, comprovantes de pagamento, notificacao extrajudicial, edital de leilao na fiduciaria.
  Marca lacunas e nao inventa dados (PA-03). Ative ao receber matricula, contrato, certidoes ou
  qualquer documento imobiliario para analisar.
metadata:
  version: "0.1.0"
  area: "Direito Imobiliario e Locacao"
  tier: 1
---

# ANALISE DOCUMENTAL IMOBILIARIA

> Tier 1. **Protocolo P2.** Antes de qualquer tese, confira a integridade do acervo. Extraia os dados-chave, marque o que falta. **Nunca preencha lacuna com suposicao** (PA-03). Trate dados do cliente/imovel com sigilo (PA-12).

---

## 1. CHECKLIST DE INTEGRIDADE

| Documento | Confere |
|-----------|---------|
| **Matricula atualizada** (ate 30 dias) | cadeia dominial, proprietario atual, onus reais, averbacoes |
| Contrato (locacao / promessa / compra e venda) | partes, objeto, prazo, valor, garantia, foro de eleicao |
| Certidao negativa de onus reais | cartorio de registro de imoveis |
| Certidao de IPTU / quitacao | prefeitura |
| Certidoes de acoes reais e pessoais reipersecutorias | situacao do imovel |
| Certidoes pessoais do vendedor | civeis, fiscais, trabalhistas, falimentar |
| Convencao de condominio + regimento | quando ha condominio edilicio |
| Comprovantes de pagamento | alugueis, encargos, parcelas |
| Notificacao extrajudicial | constituicao em mora / denuncia / purgacao |
| Edital de leilao (fiduciaria) | art. 27 Lei 9.514 — datas, valor, lance |

## 2. MATRICULA — LEITURA ESTRUTURADA

- **R (registros):** transmissoes da propriedade — montar a cadeia dominial; o ultimo R indica o dono.
- **Av (averbacoes):** alteracoes (area, construcao, casamento, penhora cancelada).
- **Onus reais a rastrear:** hipoteca (vide Sum. 308 STJ — validar), **alienacao fiduciaria**, penhora, usufruto, servidao, indisponibilidade.
- Conferir numero da matricula, cartorio, area, descricao e confrontacoes. **Nao alterar nenhum numero** (PA-03).

## 3. CONTRATO — DADOS-CHAVE

Partes e qualificacao · objeto (imovel + matricula) · prazo e termo · valor e indice de reajuste (IGP-M/IPCA) · **garantia** (so uma — art. 37; cumulacao = nulidade, PA-08) · multa · foro de eleicao · data de celebracao (define a norma — PA-04).

## 4. EXTRACAO E LACUNAS

Para cada documento, registre:
```
DOC N: <tipo> — <data> — <dados-chave extraidos>
LACUNA: <o que falta / esta ilegivel / desatualizado>
```
Numere os documentos como **"doc. N"** (citados por numero nas pecas). Converta PDFs de processo antes de analisar.

## 5. ALERTAS

- Matricula desatualizada → exigir 2a via recente antes de afirmar dominio ou onus.
- Onus de **alienacao fiduciaria** na matricula → checar fase (consolidada? leilao?) e prazo de purgacao (rota: `alienacao-fiduciaria-imovel`).
- Garantia locaticia cumulada no contrato → apontar (PA-08).
- Promessa sem registro → ainda admite adjudicacao (Sum. 239 — validar) e embargos de terceiro (Sum. 84 — validar).
- Edital de leilao com vicio (preco vil, intimacao ausente) → marcar para anulatoria.

## 6. SAIDA

```
INTEGRIDADE: completo / incompleto
ONUS NA MATRICULA: ...
GARANTIA: ... (cumulada? S/N)
DOCS NUMERADOS: doc.1..N
LACUNAS A SUPRIR: ...
```
Sem integridade minima, sinalizar ao operador antes de produzir. Depois: `analise-trilateral-imobiliaria`.
