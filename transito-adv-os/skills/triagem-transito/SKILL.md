---
name: triagem-transito
description: >
  Triagem de transito Tier 1 — primeiro contato com a demanda. Classifica em 5 eixos: (1) EIXO
  (administrativo, CNH/habilitacao, judicial, analise), (2) FASE do processo (autuacao — recebeu a NA;
  penalidade — recebeu a NP; recurso JARI; recurso CETRAN; pos-administrativo/judicial), (3) AUTO/
  INFRACAO (codigo CTB, natureza leve/media/grave/gravissima, orgao autuador, equipamento?), (4)
  PONTUACAO e situacao da CNH (pontos acumulados, suspensao/cassacao em curso), (5) PRAZO em curso
  (defesa previa, JARI, CETRAN — 30 dias da notificacao; preclusao). Define a porta de saida. Ative no
  inicio de qualquer caso de transito.
metadata:
  version: "0.1.0"
  area: "Direito de Transito"
  tier: 1
---

# TRIAGEM DE TRANSITO

> Tier 1. Primeira skill operacional. Classifica em **5 eixos**, identifica a **fase** e o **prazo preclusivo** (o mais critico), e roteia. Nada se produz antes da triagem + Selo P1.

---

## 1. OS 5 EIXOS

**Eixo 1 — EIXO**
- Administrativo · CNH/Habilitacao · Judicial · Analise de vicios (ver `transito-master` §0).

**Eixo 2 — FASE DO PROCESSO** (define a peca cabivel)

| Fase | Marco | Porta |
|------|-------|-------|
| Autuacao | recebeu a **Notificacao de Autuacao (NA)** | defesa-autuacao |
| Penalidade | recebeu a **Notificacao de Penalidade (NP)** | recursos-administrativos (JARI) |
| Recurso 1ª inst. julgado | decisao da JARI | recursos-administrativos (CETRAN) |
| Esgotada a via administrativa | decisao do CETRAN | anulatoria-transito / mandado-seguranca-transito |
| Pontuacao/suspensao | instauracao do processo de suspensao | suspensao-direito-dirigir |
| Cassacao | instauracao do processo de cassacao | cassacao-cnh |

**Eixo 3 — AUTO / INFRACAO**
- Codigo da infracao (CTB); natureza (leve 3 pts / media 4 / grave 5 / gravissima 7 — e multiplicadores); orgao autuador; houve **equipamento** (radar)? Identificacao do condutor pendente?

**Eixo 4 — PONTUACAO / CNH**
- Pontos acumulados nos 12 meses; limite aplicavel (20/30/40 conforme nº de gravissimas — Lei 14.071); ha processo de suspensao/cassacao em curso? Atividade remunerada (EAR)?

**Eixo 5 — PRAZO EM CURSO** (o mais critico)

| Prazo | Marco | Observacao |
|-------|-------|-----------|
| **Defesa previa / da autuacao** | em regra **30 dias** da NA | preclusao (PA-05) |
| **Recurso a JARI** | em regra **30 dias** da NP | 1ª instancia |
| **Recurso ao CETRAN** | em regra **30 dias** da decisao da JARI | 2ª instancia |
| Defesa no proc. de suspensao/cassacao | conforme instauracao | ampla defesa |
| Acao judicial | apos esgotar (ou nao) a via administrativa | prescricao quinquenal contra a Fazenda |

> Conferir o prazo na propria notificacao e na norma vigente (PA-04/PA-05).

## 2. PERGUNTAS DE ABERTURA (faca as que faltarem)

1. Qual documento o cliente recebeu? (NA, NP, decisao JARI/CETRAN, intimacao de suspensao/cassacao)
2. Qual a infracao (codigo/descricao), data, local e orgao autuador?
3. Foi por equipamento/radar? Ha foto?
4. Qual a pontuacao atual e a situacao da CNH? Motorista profissional (EAR)?
5. Qual a data da notificacao e o prazo que corre agora?
6. O cliente e o condutor, o proprietario, ou ambos? Ha indicacao de condutor pendente?

## 3. SAIDA DA TRIAGEM

```
EIXO: ...
FASE: ...
AUTO/INFRACAO: ... (codigo / natureza / orgao / equipamento?)
PONTUACAO/CNH: ...
PRAZO MAIS URGENTE: ... (vence em DD/MM)
PORTA DE SAIDA: <skill>
PENDENCIAS DOCUMENTAIS: ...
```
Depois: **Selo P1** → `analise-documental-transito` + `analise-vicios-auto-infracao` → porta de producao.

## 4. ALERTAS DE TRIAGEM

- Prazo preclusivo correndo → prioridade absoluta; nao deixar precluir a defesa/recurso (PA-05).
- Verificar SEMPRE a **dupla notificacao** (NA + NP — Sum. 312 STJ; PA-07) — vicio mais comum.
- Equipamento/radar → exigir certidao de **aferição INMETRO** valida (defesa-radar-equipamentos).
- Pontuacao no limite → avaliar suspensao iminente e medidas (suspensao-direito-dirigir).
- Pedido de indicacao de condutor → so o **real** condutor; indicacao falsa e crime (PA-06).
- Embriaguez/acidente com vitima → checar se e CRIME (306, 302/303) → `criminal-adv-os` (PA-09).
