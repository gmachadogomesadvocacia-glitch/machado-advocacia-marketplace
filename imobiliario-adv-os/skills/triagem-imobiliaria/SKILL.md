---
name: triagem-imobiliaria
description: >
  Triagem imobiliaria Tier 1 — primeiro contato com a demanda. Ative no inicio de qualquer caso imobiliario ou locaticio.
metadata:
  version: "0.1.0"
  area: "Direito Imobiliario e Locacao"
  tier: 1
---

# TRIAGEM IMOBILIARIA

> Tier 1. Primeira skill operacional. Classifica a demanda em **5 eixos**, identifica o **prazo mais urgente** e roteia. Nada se produz antes da triagem + Selo P1.

---

## 1. OS 5 EIXOS

**Eixo 1 — FRENTE**
- Locacao · Contratos imobiliarios · Direitos reais e posse · Consultivo (ver `imobiliario-master` §0).

**Eixo 2 — POLO** (define a peca e o tom)
- Locador × Locatario · Comprador/promitente × Vendedor/promitente · Possuidor × esbulhador/turbador · Condominio × condomino · Fiduciante × credor fiduciario. Toda peca coerente com o polo (PA-10).

**Eixo 3 — IMOVEL**
- Urbano/rural; endereco; **matricula** (no e cartorio); area; registrado em nome de quem; ha onus (hipoteca, alienacao fiduciaria, penhora, usufruto)?

**Eixo 4 — CONTRATO**
- Tipo (locacao residencial/nao residencial/temporada; promessa; compra e venda); data de celebracao (define a norma — PA-04); vigencia/prazo; valor; **garantia** (fianca, caucao, seguro-fianca — so uma, art. 37).

**Eixo 5 — PRAZO EM CURSO** (o mais critico)

| Prazo | Marco | Fonte |
|-------|-------|-------|
| **Decadencia da renovatoria** | 1 ano a 6 meses antes do fim do contrato | art. 51 §5º Lei 8.245 |
| **Purgacao da mora** (despejo p/ falta de pagto) | 15 dias da citacao | art. 62, II Lei 8.245 |
| **Contestacao possessoria** | 15 dias (forca nova) | CPC 564 |
| **Consolidacao na alienacao fiduciaria** | purgar em 15 dias da intimacao | art. 26 §1º Lei 9.514 |
| **Distrato / arrependimento** | conforme contrato + Lei 13.786 | Lei 13.786/2018 |
| **Acao de despejo / cobranca** | prescricao do aluguel: 3 anos | CC art. 206 §3º |

> Datar SEMPRE pela norma vigente no **contrato/fato** (PA-04).

## 2. PERGUNTAS DE ABERTURA (faca as que faltarem)

1. Qual o documento/fato que originou a procura? (contrato, notificacao, citacao, matricula, nenhum)
2. Qual o imovel (endereco, matricula) e quem consta como proprietario?
3. Qual a relacao: locacao? compra/promessa? posse? condominio? financiamento/fiduciaria?
4. Datas: celebracao do contrato, inicio/fim, inadimplemento, notificacao.
5. Ja houve notificacao extrajudicial, acao, liminar, leilao, garantia executada?
6. O cliente e qual polo?

## 3. SAIDA DA TRIAGEM

```
FRENTE: ...
POLO: ...
IMOVEL: ... (matricula / situacao)
CONTRATO: ... (tipo / data / garantia)
PRAZO MAIS URGENTE: ... (vence em DD/MM)
PORTA DE SAIDA: <skill>
PENDENCIAS DOCUMENTAIS: ...
```
Depois: **Selo P1** → `analise-documental-imobiliaria` → porta de producao.

## 4. ALERTAS DE TRIAGEM

- Possessoria → confirmar **forca nova (<1 ano) x forca velha** (rito e liminar mudam) e nao discutir dominio (PA-05).
- Despejo por falta de pagamento → checar direito a purgacao (art. 62) e cabimento de liminar (art. 59, PA-06).
- Renovatoria → conferir o prazo decadencial IMEDIATAMENTE (PA-07) — e o mais fatal.
- Garantia locaticia cumulada no contrato → apontar nulidade (art. 37/43, PA-08).
- Alienacao fiduciaria → verificar fase (intimacao, consolidacao, leilao) e prazo de purgacao (PA-09).
- Pedido de usucapiao → rotear ao `usucapiao-adv-os` (interface).
