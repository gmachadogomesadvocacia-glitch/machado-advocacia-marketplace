---
name: defesa-busca-apreensao
description: >
  DEFESA BUSCA E APREENSAO — Skill Tier 2 (eixo bancario, lado consumidor/devedor). Acione quando o cliente e o consumidor/devedor e o caso envolve busca e apreensao, alienacao fiduciaria, financiamento de veiculo, retomada de bem, liminar de apreensao. Exige Selo P1 e o contrato.
metadata:
  version: "0.1.0"
  area: "Direito do Consumidor e Bancario"
  tier: 2
---

# DEFESA BUSCA E APREENSAO

> Skill **Tier 2** — eixo bancario, lado **consumidor/devedor**. Defesa na busca e apreensao de bem alienado fiduciariamente (DL 911/69). Especializa a logica defensiva e conecta-se a `revisional-bancaria`. So roda apos triagem, Selo P1 e linha estrategica.

---

## 0. PRE-REQUISITOS

- Polo = **consumidor/devedor** (PA-05). Lado banco/credor → `defesa-instituicao-financeira`.
- Selo P1 emitido. **CDC aplica-se (Sum. 297 STJ).**
- Dado-base: contrato de financiamento com alienacao fiduciaria, parcelas vencidas/vincendas, valor do bem, comprovante de notificacao/protesto, data de execucao da liminar. **Sem contrato e sem prova da notificacao, NAO opinar** (PA-15) → `[INFORMAR]`.

## 1. FRENTES DEFENSIVAS (e seus limites)

| Frente | Base | Limite/armadilha |
|--------|------|------------------|
| Purgacao da mora | DL 911/69 art. 3, §2 | Exige pagamento da **INTEGRALIDADE** da divida — parcelas vencidas **+ vincendas** — em **5 dias** da execucao da liminar (Tema 722 STJ) `[VERIFICAR]`. NAO basta quitar so as vencidas. |
| Descaracterizacao da mora | jurisprudencia | Cobranca de encargo abusivo no periodo da normalidade descaracteriza a mora → afasta a apreensao. Apurar via `revisional-bancaria`. |
| Invalidade da mora (notificacao) | DL 911/69 art. 2, §2; Sum. 72 STJ | A comprovacao da mora exige notificacao/protesto **valido**, com entrega no endereco contratual (nao exige recebimento pessoal). Vicio na constituicao → carencia/improcedencia. `[VERIFICAR]` |
| Restituicao do bem / conversao | DL 911/69 | Bem ja vendido pelo credor → conversao em perdas e danos; impugnar a venda por preco vil. |

> Toda Sumula/Tema marcado `[VERIFICAR]` vai a `jurisprudencia-consumidor` (P1/PA-01). Nunca presumir a constituicao da mora.

## 2. ESTRUTURA DA DEFESA

1. **Preliminar / tutela** — se a posse ainda existe, requerer **manutencao na posse** do bem (`tutela-urgencia-consumidor`), consignando o valor incontroverso.
2. **Da invalidade da mora** — FIRAC: notificacao/protesto viciado (Sum. 72) `[VERIFICAR]`; sem mora valida, nao ha acao.
3. **Da descaracterizacao da mora** — FIRAC apoiado nos encargos abusivos (juros acima da taxa media, capitalizacao nao pactuada) — remeter ao calculo da `revisional-bancaria`.
4. **Da purgacao da mora** (se for a estrategia) — depositar a integralidade (vencidas + vincendas) em 5 dias da execucao da liminar (art. 3, §2; Tema 722) `[VERIFICAR]`, com restituicao do bem.
5. **Pedidos** — improcedencia / carencia; subsidiariamente, purgacao com restituicao; conversao em perdas e danos se o bem ja foi alienado; revisao dos encargos (inciso do art. 51, PA-13).

## 3. PROVA E ONUS

Ao credor cabe provar a **mora valida** (notificacao/protesto regular) e a higidez dos encargos. Pleitear inversao do onus (art. 6, VIII) fundamentada (PA-12) e a exibicao do contrato e da planilha de evolucao da divida.

## 4. CHECKLIST

- [ ] Polo devedor coerente (PA-05) · Selo P1 · contrato e notificacao nos autos (PA-15)
- [ ] Mora: notificacao/protesto valido? (Sum. 72) `[VERIFICAR]`
- [ ] Purgacao = integralidade (vencidas + vincendas) em 5 dias (Tema 722) `[VERIFICAR]`
- [ ] Descaracterizacao por encargo abusivo → `revisional-bancaria` (calculo discriminado)
- [ ] Tutela de manutencao na posse, se cabivel
- [ ] `revisao-final-consumidor` R1-R4 (PA-22)

## 5. ENCERRAMENTO

Entrega a defesa do devedor com a mora atacada na origem (notificacao e encargos), a purgacao corretamente dimensionada pela integralidade e a posse protegida — pronta para a R1-R4.
