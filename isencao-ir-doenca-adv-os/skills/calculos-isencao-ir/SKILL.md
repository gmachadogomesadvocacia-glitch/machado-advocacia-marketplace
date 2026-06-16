---
name: calculos-isencao-ir
description: >
  CALCULOS ISENCAO-IR — Skill Tier 1. Apura a RESTITUICAO do indebito: soma do IR retido indevidamente,
  competencia a competencia, nos ULTIMOS 5 ANOS (CTN art. 168), com atualizacao pela Selic. Entrega
  memoria de calculo discriminada (competencia x base x IR retido x Selic x total). Sem os comprovantes
  de retencao (informes de rendimento), NAO calcula — sinaliza o que falta (PA-03/PA-11). Restituicao
  limitada a 5 anos (PA-09); so sobre PROVENTOS (PA-06). Acione apos a analise documental. Gatilhos:
  calcular, quanto vou receber, restituicao, valor retido, atualizar pela Selic, memoria de calculo,
  indebito, quanto da pra pedir de volta.
metadata:
  version: "0.1.0"
  area: "Isencao de IRPF por Doenca Grave"
  tier: 1
---

# CALCULOS ISENCAO-IR

> Skill **Tier 1** — apura a **restituicao do indebito**: IR retido indevidamente nos **ultimos 5 anos** (CTN art. 168), atualizado pela **Selic**. Sem comprovante de retencao, **nao calcula**.

---

## 0. PRE-REQUISITOS
- `analise-documental-isencao-ir` concluida; **informes de rendimentos / comprovantes de IR retido** presentes (D3).
- Marco da isencao definido (data do laudo / inicio da doenca) — pela `triagem`/`linha-estrategica`.
- Sem comprovante de retencao → **NAO calcular**; sinalizar `[INFORMAR]` o que falta (PA-03/PA-11). Nunca estimar valor sem base documental.

## 1. PERIMETRO DO INDEBITO
- Somente **IR retido sobre PROVENTOS** isentos (aposentadoria/pensao/reforma) — PA-06. Excluir retencao sobre eventual rendimento de **ativo** (nao isento).
- Apenas a partir do **marco da isencao**; antes do marco nao ha indebito.
- Apenas os **ultimos 5 anos** contados da data do pedido (CTN art. 168 — PA-09). Competencia anterior a isso = **prescrita**, fora do calculo.

## 2. APURACAO (competencia a competencia)
Para cada mes do periodo restituivel:
```
competencia | provento bruto | IR retido na fonte | indice Selic acumulado | valor atualizado
```
- Somar o **IR retido** de cada competencia (13o inclusive, quando tributado na fonte).
- **Atualizar pela Selic** desde cada retencao ate a data do calculo (Selic ja engloba juros + correcao; nao cumular com outro indice).

## 3. MEMORIA DE CALCULO (entregavel)
Tabela discriminada + totais:
- **Total do IR retido indevidamente** (historico)
- **Total atualizado pela Selic** (valor a restituir)
- Periodo coberto (mes inicial — mes final) e marco da isencao
- Notas: competencias prescritas excluidas; criterio Selic; fonte dos valores ("doc. N").

## 3.1 EXEMPLO RESOLVIDO (restituicao dos 5 anos)
Pedido protocolado em **06/2026** → restituivel a partir de **06/2021** (CTN 168); competencias anteriores **prescritas**. Aposentado, provento mensal isento, IR retido na fonte de **R$ 700/mes** (13o incluso = 13 retencoes/ano). Selic acumulada da media de cada ano ate 06/2026 (ilustrativa — usar a tabela oficial vigente):

```
ano  | IR retido no ano (13 x 700) | Selic acum. ate 06/2026 | valor atualizado
2021 (07-12, 6 retencoes=4.200) |  4.200,00 | ~1,55 |  6.510,00
2022 (13 x 700)                 |  9.100,00 | ~1,42 | 12.922,00
2023 (13 x 700)                 |  9.100,00 | ~1,28 | 11.648,00
2024 (13 x 700)                 |  9.100,00 | ~1,16 | 10.556,00
2025 (13 x 700)                 |  9.100,00 | ~1,07 |  9.737,00
2026 (01-06, 6 retencoes=4.200) |  4.200,00 | ~1,02 |  4.284,00
```
- **Total historico (IR retido):** R$ 44.800,00.
- **Total atualizado pela Selic (a restituir):** R$ 55.657,00.
- **Marco da prescricao:** competencias de **antes de 06/2021 estao prescritas** (CTN 168) e ficam **fora** do calculo — no exemplo, 2020 e anteriores nao entram.
> Numeros ilustrativos. No caso real, extrair o IR retido de cada competencia dos informes ("doc. N") e aplicar a **Selic oficial** de cada retencao ate a data do calculo (uma unica vez — sem cumular outro indice).

## 4. CHECKLIST
- [ ] So proventos isentos (PA-06) · so dentro de 5 anos (PA-09)
- [ ] Valores extraidos de comprovantes reais ("doc. N"), nada estimado (PA-03)
- [ ] Selic aplicada uma unica vez, sem cumulacao indevida
- [ ] Total historico e total atualizado separados

## 5. ENCERRAMENTO
Entrega a memoria de calculo discriminada com o valor a restituir, para instruir a `acao-isencao-ir`/requerimento e compor o valor da causa. Antes da entrega final, `revisao-final-isencao-ir` (R2/R4).
