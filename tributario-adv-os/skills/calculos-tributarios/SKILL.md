---
name: calculos-tributarios
description: >
  Nucleo de calculo tributario. Apura DECADENCIA (CTN art. 173, I — regra geral, 1º dia do exercicio
  seguinte; x art. 150 §4º — lancamento por homologacao, do fato gerador, salvo dolo/fraude/simulacao),
  PRESCRICAO (CTN art. 174, 5 anos da constituicao definitiva; interrupcao pelo despacho que ordena a
  citacao — LC 118/2005), PRESCRICAO INTERCORRENTE (LEF art. 40 + Sum. 314 STJ + Tema 566 STJ — 1 ano
  de suspensao + 5 anos), atualizacao do debito (SELIC, multa de mora x multa de oficio, juros,
  confisco) e prazo de repeticao/compensacao (5 anos — CTN 168/LC 118). Sempre refazer, nunca presumir.
  Ative para conferir prazos, decadencia, prescricao ou montante do debito. PA-05, PA-03, PA-09.
metadata:
  version: "0.1.0"
  area: "Direito Tributario"
  tier: 1
---

# CALCULOS TRIBUTARIOS

> Tier 1. Nucleo de calculo. **Sempre refazer, nunca presumir** (PA-03/PA-05). Toda contagem com **datas** e **memoria passo a passo**. Datar pela norma vigente no fato gerador (PA-04).

---

## 1. DECADENCIA (Fazenda perde o direito de CONSTITUIR) — PA-05

| Regra | Termo inicial | Base |
|-------|---------------|------|
| Geral | 1º dia do exercicio **seguinte** aquele em que poderia ter lancado | CTN art. 173, I |
| Lancamento por homologacao **com pagamento antecipado** | data do **fato gerador** | CTN art. 150 §4º |
| Dolo, fraude ou simulacao | volta a regra geral (art. 173, I) | CTN art. 150 §4º in fine |
| Sem declaracao / sem pagamento | art. 173, I (Sum. 555 STJ — validar) | — |

- Prazo: **5 anos**. Decadencia extingue o credito (CTN 156, V).

## 2. PRESCRICAO (Fazenda perde o direito de COBRAR) — PA-05

- Prazo: **5 anos** da **constituicao definitiva** (CTN art. 174).
- Constituicao definitiva = fim do prazo de impugnacao ou transito administrativo; na declaracao, a entrega (Sum. 436 STJ — validar).
- **Interrupcao**: despacho do juiz que ordena a citacao (CTN 174, I, redacao da LC 118/2005), retroagindo a propositura (Sum. 106 STJ — validar). Tambem: protesto judicial, ato de constituicao em mora, reconhecimento do debito (parcelamento).
- Nao confundir com decadencia (PA-05): decadencia = antes do lancamento; prescricao = depois da constituicao.

## 3. PRESCRICAO INTERCORRENTE (LEF art. 40)

- **1 ano** de suspensao (nao localizado devedor ou bens) + **5 anos** de arquivamento.
- Sum. 314 STJ + **Tema 566 STJ** (validar): o prazo corre automaticamente; marco e a ciencia da Fazenda da nao localizacao; reconhecimento de oficio apos intimacao.

## 4. ATUALIZACAO DO DEBITO

- **SELIC** acumulada (federal: juros + correcao desde 1996; estaduais/municipais conforme lei propria).
- **Multa de mora** (atraso, espontaneo) x **multa de oficio** (lancamento, infracao) — nao cumular indevidamente.
- **Juros** sobre o principal corrigido; observar capitalizacao vedada.
- **Confisco** (CF art. 150, IV): multa excessiva pode ser reduzida (Temas STF — validar). Sinalizar excesso de execucao.

## 5. REPETICAO / COMPENSACAO (PA-09)

- Prazo: **5 anos** (CTN art. 168; LC 118/2005 — tese dos "5+5" superada para fatos pos-LC 118).
- Indebito (pagamento a maior/indevido): termo inicial = data do pagamento.
- Compensacao so com lei autorizadora e credito liquido e certo (CTN 170; Sum. 213/460/461 STJ — validar).

## 6. MEMORIA DE CALCULO (formato de saida)

```
EVENTO            DATA        BASE LEGAL
Fato gerador      DD/MM/AAAA  CTN ...
Lancamento/decl.  DD/MM/AAAA  ...
Const. definitiva DD/MM/AAAA  CTN 174
Marco do prazo    DD/MM/AAAA
PRAZO: decadencia/prescricao vence em DD/MM/AAAA
VALOR: originario + multa + juros/SELIC = R$ ...
CONCLUSAO: (consumado / em curso / X dias restantes)
```

## 7. INTEGRACAO

- Recebe datas/valores de `analise-documental-tributaria`.
- Alimenta `defesa-execucao-fiscal` (decadencia/prescricao/excesso) e `linha-estrategica-tributaria`.
- Nunca afirmar prazo consumado sem a memoria acima (PA-03).
