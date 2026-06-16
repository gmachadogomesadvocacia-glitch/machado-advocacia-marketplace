---
name: timeline-consumidor
description: >
  TIMELINE CONSUMIDOR — Skill Tier 1. Monta a linha do tempo fatico-processual do caso e coordena as
  esferas paralelas (judicial + administrativa — Protocolo P4), evitando teses contraditorias entre as
  frentes. Marca os prazos criticos: decadencia do vicio (30/90 dias, art. 26), prescricao do fato do
  produto/servico (5 anos, art. 27), arrependimento (7 dias, art. 49 — so fora do estabelecimento),
  prazo de resposta do PROCON/consumidor.gov.br e recurso no JEC (10 dias, Lei 9.099). Saida: timeline
  com datas, eventos, pecas e alertas de prazo. Acione quando o usuario pedir a linha do tempo do caso,
  a cronologia dos fatos, controle de prazos, calcular decadencia/prescricao, quando vence o prazo,
  ordenar eventos, ou coordenar as frentes judicial e administrativa.
metadata:
  version: "0.1.0"
  area: "Direito do Consumidor e Bancario"
  tier: 1
---

# TIMELINE CONSUMIDOR

> Skill **Tier 1**. Ordena os fatos e atos do caso numa **linha do tempo** unica, calcula os **prazos criticos** consumeristas e **coordena as esferas paralelas** (judicial + administrativa) pelo **Protocolo P4**, impedindo teses contraditorias entre frentes.

---

## 0. QUANDO ACIONAR

Quando o advogado pedir a linha do tempo, a cronologia, o controle de prazos, o calculo de decadencia/prescricao, "quando vence", ou a coordenacao entre acao judicial e reclamacao administrativa. Util na triagem (mapear prazos), na estrategia (P4) e antes de protocolar.

## 1. PRE-CHECK

1. Ler o `CASO.md` e o `MEMORY.md` em `consumidor/casos/<slug>/` — polo, eixo, esfera, partes, documentos, prazos ja anotados.
2. Coletar as **datas-base** dos documentos (contratacao, cobranca, inscricao, entrega, atendimento/protocolo, ciencia do dano). Data ausente → `[INFORMAR]` (PA-15); **nunca presumir data** (PA-03/PA-11).

---

## 2. PRAZOS CRITICOS (calcular e alertar)

| Prazo | Marco inicial | Duracao | Base | Observacao |
|-------|---------------|---------|------|------------|
| **Decadencia do vicio** | entrega do produto / termino do servico (vicio aparente) ou ciencia (vicio oculto) | **30 dias** (nao duravel) / **90 dias** (duravel) | art. 26 CDC | Obsta-se por reclamacao comprovada (art. 26 §2). Nao confundir com fato (PA-10) |
| **Prescricao do fato** (produto/servico) | ciencia do **dano e da autoria** | **5 anos** | art. 27 CDC | Acidente de consumo / responsabilidade pelo fato |
| **Arrependimento** | recebimento ou assinatura | **7 dias** | art. 49 CDC | **So** compra fora do estabelecimento (internet, telefone, domicilio) |
| **Resposta administrativa** | protocolo da reclamacao | conforme orgao | PROCON / consumidor.gov.br (≈10 dias para manifestacao do fornecedor) | Gera prova da resistencia (P4) |
| **Recurso no JEC** | intimacao da sentenca | **10 dias** | art. 42 Lei 9.099 | Recurso inominado; conferir tempestividade |

> Aplicar tambem prazos do CPC/CDC pertinentes ao caso (contestacao, embargos). **Sempre conferir** (PA-11). Confundir vicio (decadencia, art. 26) com fato (prescricao, art. 27) e proibido (PA-10).

---

## 3. MONTAGEM DA TIMELINE

Ordene cronologicamente **todos** os eventos faticos e processuais, atrelando a cada um a fonte documental ("doc. N") e a esfera:

```
LINHA DO TEMPO — <cliente> (polo: <...>)

| Data        | Evento                              | Esfera        | Doc/Peca   | Prazo gerado / alerta              |
|-------------|-------------------------------------|---------------|------------|------------------------------------|
| AAAA-MM-DD  | contratacao                         | -             | doc. 1     | -                                  |
| AAAA-MM-DD  | cobranca/inscricao indevida         | -             | doc. 3     | decadencia art.26 ? / fato art.27 ?|
| AAAA-MM-DD  | reclamacao consumidor.gov.br        | administrativa| doc. 5     | resposta do fornecedor em ~10 d    |
| AAAA-MM-DD  | ajuizamento                         | judicial      | inicial    | -                                  |
| AAAA-MM-DD  | sentenca                            | judicial      | -          | recurso JEC: 10 d (vence AAAA-MM-DD)|

ALERTAS DE PRAZO
- [VENCE EM N DIAS] ...
- [VENCIDO] ... (avaliar obstativo/causa de interrupcao)
LACUNAS [INFORMAR]
- datas/documentos ausentes que afetam a contagem.
```

---

## 4. COORDENACAO DE ESFERAS PARALELAS (Protocolo P4)

Quando ha frente **judicial + administrativa** simultaneas:

1. Marcar na timeline qual fato sustenta cada frente.
2. **Checar coerencia entre frentes** — a narrativa e os pedidos na reclamacao administrativa (PROCON/consumidor.gov.br/BACEN/ANATEL/ANAC) **nao podem contradizer** a tese da acao judicial; contradicao vira prova contra o cliente (P4).
3. Usar a via administrativa como **prova** (resistencia do fornecedor, confissao, recusa documentada) na acao judicial.
4. Sinalizar litispendencia/risco de decisoes conflitantes; registrar a coordenacao no `MEMORY.md`.

---

## 5. SAIDA E REGISTRO

Entregar a tabela da secao 3 + os alertas de prazo + as lacunas. Gravar os prazos criticos no bloco **Prazos Criticos** do `CASO.md` e o historico no `MEMORY.md` via `memoria-de-caso-consumidor`. Em caso de prazo a vencer, destacar no encerramento para o advogado.

---

## 6. ENCERRAMENTO

Entrega a linha do tempo com datas, eventos, pecas e alertas, os prazos consumeristas calculados (art. 26 / 27 / 49 / resposta administrativa / recurso JEC) e a coordenacao das esferas paralelas (P4) sem teses contraditorias. Nenhuma data presumida (PA-03/PA-11); coerencia de polo preservada (PA-05).
