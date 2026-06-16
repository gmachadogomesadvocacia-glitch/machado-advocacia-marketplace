---
name: calculos-consumidor
description: >
  CALCULOS CONSUMIDOR — Skill Tier 1, motor de calculo consumerista/bancario. Cobre revisional
  bancaria (taxa do contrato x taxa media BACEN, expurgo de capitalizacao nao pactuada), repeticao de
  indebito (simples x dobro do art. 42), expurgo de tarifas, atualizacao (correcao + juros de mora) e
  quantificacao de dano moral por ancoragem. PA-20: nunca calculo estimativo silencioso — sem dado-base
  (contrato, taxas, valores, datas), NAO calcular: sinalizar o que falta. Acione quando o usuario pedir
  para calcular, liquidar, apurar o indebito, revisar parcelas, atualizar a divida ou dimensionar o dano
  moral. Gatilhos: calcular, quanto, valor da causa, revisional, repeticao de indebito, dobro, indebito,
  tarifa indevida, atualizar, correcao monetaria, juros de mora, Selic, memoria de calculo, taxa media.
metadata:
  version: "0.1.0"
  area: "Direito do Consumidor e Bancario"
  tier: 1
---

# CALCULOS CONSUMIDOR

> Skill **Tier 1** — motor de calculo. Entrega **memoria de calculo discriminada** (verba × base × resultado). **Sem dado-base, nao calcula** (**PA-20**): sinaliza o que falta como `[INFORMAR]`.

---

## 0. QUANDO ACIONAR

Quando a tese exige numero: revisional, indebito, expurgo, atualizacao ou dano moral; antes de fixar o **valor da causa** (que define o rito — JEC ate 40 SM, **P5**). Depende de `analise-documental` (docs essenciais — PA-15) e do **Selo P1**.

## 1. PRINCIPIO — PA-20

**Vedado o calculo estimativo silencioso e a promessa de resultado.** Todo numero nasce de **dado-base verificavel** (clausula, taxa, valor, data). Faltando dado, **nao calcular** — listar o `[INFORMAR]` e parar. Sumula/Tema usados no calculo so se VALIDADOS (**PA-01** → marcar `[VERIFICAR]` e acionar `jurisprudencia-consumidor`). Nunca alucinar valor, taxa ou data (**PA-03**).

---

## 2. MODULOS DE CALCULO

### (a) Revisional bancaria
1. **Comparar a taxa do contrato com a taxa media de mercado do BACEN** da especie/periodo — abusividade so se a do contrato destoa relevantemente da media (`[VERIFICAR]` Sum. 530 / 382 STJ). Dado-base: CET/cedula + taxa BACEN da serie.
2. **Expurgar capitalizacao nao pactuada** (`[VERIFICAR]` Sum. 539/541 — so se expressamente prevista). Recompor o saldo com a capitalizacao admitida (ou simples, se ausente pactuacao).
3. **Recompor as parcelas** com a taxa/encargos saneados; apurar a diferenca paga a maior.

### (b) Repeticao de indebito
- **Simples** — devolucao do valor cobrado indevidamente, atualizado.
- **Dobro (art. 42, § un.)** — exige **cobranca indevida + engano injustificavel** (conduta contra a boa-fe — `[VERIFICAR]` Tema 929 STJ). Sem os dois requisitos, so o simples (**PA-06**). Discriminar a base do dobro.

### (c) Expurgo de tarifas indevidas
- Listar tarifas/seguros cobrados sem pactuacao/destaque ou vedados; somar e atualizar. Resultado entra como base da repeticao (simples ou dobro).

### (d) Atualizacao (correcao + juros)
- **Correcao monetaria** desde o evento (cobranca/desembolso): indice do tribunal.
- **Juros de mora** (art. 406 CC / Selic) — termo inicial conforme a natureza (contratual x extracontratual; citacao x evento danoso). Evitar bis in idem (Selic ja embute correcao).

### (e) Dano moral — ancoragem
- **Nao** estimar valor solto. Indicar faixa por **ancoragem em precedentes** do TJ local/STJ para casos analogos (negativacao, corte de servico essencial, voo, recusa de cobertura), com funcao pedagogica e vedacao ao enriquecimento sem causa. Precedentes via `jurisprudencia-consumidor` (`[VERIFICAR]` ate validar).

---

## 3. DADOS-BASE NECESSARIOS (checar antes)

| Modulo | Dado-base minimo |
|--------|------------------|
| Revisional | Contrato/CET, taxa contratada, taxa media BACEN da serie, parcelas, datas |
| Indebito | Valor(es) cobrado(s), datas, prova de indevido + (para dobro) do engano |
| Tarifas | Discriminacao das tarifas, valores, pactuacao |
| Atualizacao | Valor historico, data do evento, indice/termo inicial dos juros |
| Dano moral | Precedentes analogos validados |

Faltou qualquer item → `[INFORMAR]`, **sem calcular** o modulo (PA-20).

## 4. SAIDA — MEMORIA DE CALCULO

```
MEMORIA DE CALCULO
Verba                         | Base                          | Resultado
Indebito (tarifas, doc. 3)    | R$ 1.240,00 cobrados          | R$ 1.240,00
  -> dobro (art. 42)          | engano injustificavel? [VERIFICAR Tema 929] | R$ 2.480,00
Correcao (desde 03/2025)      | indice TJ                     | R$ ...
Juros de mora (art. 406)      | desde a citacao/evento        | R$ ...
TOTAL (sujeito a dado [INFORMAR]) ........................... R$ ...
VALOR DA CAUSA SUGERIDO (define rito — P5) ................. R$ ...
```

Discriminar **verba × base × resultado**; marcar cada premissa pendente (`[VERIFICAR]` / `[INFORMAR]`).

## 5. ENCERRAMENTO

Entrega a memoria discriminada, o subtotal por verba e o valor da causa sugerido (com o rito que ele dispara — P5), sem nenhum numero estimado em silencio (PA-20) e com toda sumula/Tema marcada ate validacao (PA-01). Alimenta a peca e a `revisao-final-consumidor`.
