---
name: calculos-transito
description: >
  Calculos de transito Tier 1 — nucleo de calculo e conferencia. Ative para calcular pontos, prazos ou valores.
metadata:
  version: "0.1.0"
  area: "Direito de Transito"
  tier: 1
---

# CALCULOS DE TRANSITO

> Tier 1. Nucleo de calculo e conferencia: **pontuacao**, **prazos** e **valores**. Toda conta sai com **memoria passo a passo e datas**. Aplica a norma **vigente na data da infracao** (PA-04) e respeita os prazos preclusivos (PA-05). Nenhum numero sem respaldo no documento (PA-03).

---

## 1. PONTUACAO

**Pontos por natureza (CTB 259):**

| Natureza | Pontos |
|----------|--------|
| Leve | 3 |
| Media | 4 |
| Grave | 5 |
| Gravissima | 7 (base; conferir multiplicadores aplicaveis) |

**Limite para suspensao do direito de dirigir (Lei 14.071/2020):** soma dos pontos nos **12 meses**:
- **20 pontos** se houver **2 ou mais infracoes gravissimas** no periodo;
- **30 pontos** se houver **1 infracao gravissima**;
- **40 pontos** se **nenhuma** gravissima.

**EAR / motorista profissional** (atividade remunerada): regra propria — limite de 40 pontos independentemente da natureza (conferir vigencia e enquadramento na data — PA-04). Verificar a anotacao de EAR na CNH.

> Atencao: infracoes **autossuspensivas** geram suspensao por si, fora da contagem de pontos. Conferir a tipificacao.

## 2. PRAZOS

| Prazo | Marco inicial | Regra |
|-------|---------------|-------|
| **Defesa previa / da autuacao** | data da NA | em regra **30 dias** (preclusivo — PA-05) |
| **Recurso a JARI** | data da NP | em regra **30 dias** |
| **Recurso ao CETRAN** | data da decisao da JARI | em regra **30 dias** |
| **Expedicao da NA** | data da autuacao | CTB 281 § unico — **30 dias**; ultrapassado → **arquivamento** |
| **Prescricao judicial** | conforme pretensao | **quinquenal** contra a Fazenda Publica |

**Contagem:** conferir o termo inicial (data da notificacao na propria peca), excluir/incluir conforme a regra do orgao e a norma vigente; registrar a **data de vencimento** explicita. Em duvida sobre a regra de contagem, marcar "[conferir norma]".

## 3. VALORES

- Multa **por natureza** (valor-base do CTB 258) e **multiplicador** quando previsto (ex.: gravissima x2, x3, x5, x10 — conferir a tipificacao).
- **Conversao em advertencia** (CTB 267): cabivel para infracao **leve ou media** sem reincidencia na mesma natureza nos 12 meses — verificar requisitos antes de pleitear.
- Nao inventar valores; usar o valor constante do auto/tabela vigente (PA-03/PA-04).

## 4. MEMORIA DE CALCULO (formato)

```
PONTUACAO
  infracao 1: <natureza> = <pts> (data DD/MM)
  infracao 2: ...
  soma 12 meses: <total> pts
  gravissimas no periodo: <n> → limite aplicavel: 20/30/40
  situacao: abaixo / no limite / acima → suspensao?

PRAZOS
  NA em DD/MM → defesa previa vence DD/MM (30 dias)
  NP em DD/MM → recurso JARI vence DD/MM
  expedicao da NA: DD/MM (dentro/fora dos 30 dias — CTB 281)

VALORES
  multa: natureza <x> base R$<...> × mult <...> = R$<...>
  advertencia (CTB 267): cabivel? sim/nao — por que
```

## 5. EXEMPLO RESOLVIDO (passo a passo)

**Cenario.** Condutor NAO profissional (sem EAR). Infracoes nos ultimos 12 meses, todas dentro do periodo:

| # | Data | Natureza | Pontos |
|---|------|----------|--------|
| 1 | 10/07/2025 | gravissima | 7 |
| 2 | 22/08/2025 | gravissima | 7 |
| 3 | 03/11/2025 | grave | 5 |
| 4 | 15/01/2026 | media | 4 |
| 5 | 28/03/2026 | leve | 3 |

**Passo a passo — pontuacao:**
1. Pontos por natureza (CTB 259): 7 + 7 + 5 + 4 + 3.
2. **Soma nos 12 meses = 26 pontos.**
3. Contar gravissimas no periodo: **2 gravissimas** (infracoes 1 e 2).
4. Limite aplicavel (Lei 14.071/2020): com **2 ou mais gravissimas → limite de 20 pontos**.
5. Comparar: 26 > 20 → **acima do limite**. Resultado: enseja **instauracao de processo de suspensao do direito de dirigir**.

> Sensibilidade: se a infracao 2 fosse afastada (defesa/recurso provido), restaria **1 gravissima** → limite sobe para **30 pontos**, e a soma cairia para 19 → **abaixo do limite** (sem suspensao). Por isso a contagem de gravissimas e decisiva — atacar uma gravissima pode mudar o patamar inteiro.

**Passo a passo — prazo preclusivo (30 dias):**
- Notificacao de Penalidade (NP) recebida em **02/06/2026**. Prazo de recurso a JARI: **30 dias** (PA-05).
- Contagem: termo inicial 02/06; +30 dias corridos → vencimento em **02/07/2026** (conferir a regra de contagem do orgao e eventual prorrogacao para o 1º dia util seguinte se cair em fim de semana/feriado — em duvida, marcar "[conferir norma]").
- Hoje 16/06/2026 → faltam **16 dias**: prazo **aberto**. Protocolar ate 02/07/2026, sob pena de preclusao da instancia.

## 6. INTEGRACAO

- `triagem-transito` / `analise-documental-transito` → datas e dados de entrada.
- `analise-vicios-auto-infracao` → prazo da NA estourado = tese de arquivamento.
- `linha-estrategica-transito` → custo/beneficio (valor × pontos × risco de suspensao).
- `revisao-final-transito` → R2 reconfere contas e datas.

## 7. CHECKLIST DE SAIDA

- [ ] Pontos por natureza corretos e somados nos 12 meses
- [ ] Limite (20/30/40) escolhido pelo nº de gravissimas (Lei 14.071)
- [ ] EAR/autossuspensiva consideradas quando aplicaveis
- [ ] Prazos com termo inicial e **data de vencimento** explicita (PA-05)
- [ ] Norma vigente na data da infracao (PA-04)
- [ ] Memoria passo a passo com datas; nenhum valor inventado (PA-03)
