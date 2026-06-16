---
name: triagem-tributaria
description: >
  Triagem tributaria Tier 1 — primeiro contato com a demanda. Classifica em 5 eixos: (1) FRENTE
  (administrativa, judicial, consultiva), (2) TRIBUTO e ESFERA (federal/estadual/municipal), (3) FASE
  (pre-lancamento, lancamento/auto, contencioso administrativo, inscricao em divida ativa, execucao
  fiscal, pos-transito), (4) POLO (contribuinte/defesa x Fazenda), (5) PRAZO em curso (decadencia,
  prescricao, prazo de impugnacao/recurso/embargos). Define a porta de saida e os checkpoints. Ative
  no inicio de qualquer caso tributario, quando o usuario trouxer auto de infracao, CDA, citacao em
  execucao fiscal, notificacao de lancamento, ou duvida sobre tributo/planejamento.
metadata:
  version: "0.1.0"
  area: "Direito Tributario"
  tier: 1
---

# TRIAGEM TRIBUTARIA

> Tier 1. Primeira skill operacional. Classifica a demanda em **5 eixos**, identifica o **prazo mais urgente** e roteia para a porta correta. Nada se produz antes da triagem + Selo P1.

---

## 1. OS 5 EIXOS

**Eixo 1 — FRENTE**
- Administrativa · Judicial · Consultiva (ver `tributario-master` §0).

**Eixo 2 — TRIBUTO + ESFERA**
- Federal: IR (IRPF/IRPJ), IPI, PIS/COFINS, CSLL, contrib. previdenciaria, ITR, IOF.
- Estadual: ICMS, ITCMD, IPVA.
- Municipal: ISS, IPTU, ITBI, taxas.
- Simples Nacional (LC 123/2006) atravessa esferas → tratar como regime.

**Eixo 3 — FASE** (define a peca cabivel)

| Fase | Marco | Porta |
|------|-------|-------|
| Pre-lancamento | duvida/risco, sem auto | planejamento-tributario / consulta fiscal |
| Lancamento / auto de infracao | notificacao do auto | impugnacao-administrativa |
| Contencioso administrativo | decisao 1ª instancia (DRJ/junta) | recurso-administrativo-carf |
| Inscricao em divida ativa | CDA inscrita, pre-ajuizamento | anulatoria / parcelamento-transacao / MS |
| Execucao fiscal | citacao na LEF 6.830 | defesa-execucao-fiscal |
| Pos-pagamento indevido | pagou a maior / indevido | repeticao-indebito-compensacao |

**Eixo 4 — POLO** — contribuinte (defesa, padrao) x Fazenda. Toda peca coerente com o polo (PA-10).

**Eixo 5 — PRAZO EM CURSO** (o mais critico)
- **Decadencia** (CTN art. 173 / 150 §4º) — Fazenda perde o direito de **constituir** o credito.
- **Prescricao** (CTN art. 174) — Fazenda perde o direito de **cobrar** (5 anos da constituicao definitiva).
- **Prazo de impugnacao** — 30 dias do auto (Dec. 70.235, federal; conferir lei estadual/municipal).
- **Embargos a execucao** — 30 dias da garantia/intimacao da penhora (LEF art. 16).
- **Excecao de pre-executividade** — sem prazo, mas so materia de ordem publica (Sum. 393 STJ).
- **Repeticao/compensacao** — 5 anos (CTN art. 168 / LC 118/2005).

> Datar SEMPRE pela norma vigente no **fato gerador** (PA-04). Atencao a transicao da Reforma (CBS/IBS).

## 2. PERGUNTAS DE ABERTURA (faca as que faltarem)

1. Qual o documento que originou a procura? (auto, CDA, citacao, notificacao, nenhum)
2. Qual tributo, qual ente, qual periodo (competencias/fatos geradores)?
3. Ha processo administrativo ou judicial em curso? Numero/fase?
4. Ja houve garantia, deposito, penhora, parcelamento?
5. Qual a data do documento e o prazo que corre agora?
6. O cliente e o contribuinte, o responsavel/socio, ou terceiro?

## 3. SAIDA DA TRIAGEM

Entregar um **bloco de classificacao**:
```
FRENTE: ...
TRIBUTO/ESFERA: ...
FASE: ...
POLO: ...
PRAZO MAIS URGENTE: ... (vence em DD/MM)
PORTA DE SAIDA: <skill>
PENDENCIAS DOCUMENTAIS: ...
```
Depois: **Selo P1** → `analise-documental-tributaria` → porta de producao.

## 4. ALERTAS DE TRIAGEM

- Citacao em execucao fiscal com prazo curto → priorizar garantia + embargos OU excecao de pre-executividade; nao deixar precluir.
- Suspeita de decadencia/prescricao → `calculos-tributarios` ANTES de qualquer peca de merito.
- Redirecionamento ao socio → checar art. 135 CTN, Sum. 435 STJ, Tema 962 STJ (PA-08).
- Pedido que tangencie sonegacao/fraude → recusar (PA-06); so elisao licita.
- Crime tributario (Lei 8.137) → sinalizar interface com o plugin criminal.
