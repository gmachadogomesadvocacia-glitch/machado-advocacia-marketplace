---
name: calculos-tributarios
description: >
  Nucleo de calculo tributario. Apura DECADENCIA (CTN art. 173, I. Ative para conferir prazos, decadencia, prescricao ou montante do debito. PA-05, PA-03, PA-09.
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

## 2-A. EXEMPLO RESOLVIDO — DECADENCIA x PRESCRICAO (passo a passo)

> Caso: IRPJ, lancamento de oficio (SEM pagamento antecipado). Fato gerador em 2016; auto de infracao notificado em 12/03/2018; sem impugnacao; citacao na execucao fiscal em 20/05/2024. Verificar decadencia e prescricao.

**Passo 1 — DECADENCIA (poder de CONSTITUIR — CTN 173, I).**
Sem pagamento antecipado, aplica-se a regra geral: termo inicial = 1º dia do exercicio SEGUINTE aquele em que o lancamento poderia ter sido feito.
- Fato gerador: exercicio de 2016 → poderia lancar em 2016.
- Termo inicial: 01/01/2017.
- Prazo de 5 anos → decadencia venceria em **31/12/2021**.
- Lancamento (notificacao do auto): **12/03/2018**. Como 12/03/2018 < 31/12/2021, o credito foi constituido DENTRO do prazo. **NAO ha decadencia.**
- (Contraste: se fosse lancamento por homologacao COM pagamento antecipado, o termo inicial seria o fato gerador — CTN 150, §4º — e o prazo correria do proprio fato gerador de 2016.)

**Passo 2 — CONSTITUICAO DEFINITIVA.**
Notificado em 12/03/2018 e nao impugnado, o credito se torna definitivo ao fim do prazo de impugnacao (30 dias — PAF). Constituicao definitiva: **~11/04/2018** (inicio do prazo prescricional).

**Passo 3 — PRESCRICAO (poder de COBRAR — CTN 174).**
- Prazo: 5 anos da constituicao definitiva (11/04/2018) → venceria em **~11/04/2023**.
- Interrupcao: despacho que ordena a citacao (CTN 174, I, LC 118/2005), retroagindo a propositura (Sum. 106 STJ — validar). Citacao em 20/05/2024; conferir a DATA DO DESPACHO e a data do AJUIZAMENTO nos autos.
- Se o ajuizamento/despacho ocorreu APOS 11/04/2023 → **prescricao consumada** (extincao, CTN 156, V). Se ocorreu ANTES, sem causa interruptiva no interregno, o prazo nao se completou.

**Conclusao:** sem decadencia (constituido em 2018, dentro do prazo de 2021); a prescricao depende da data do despacho/ajuizamento — provavel prescricao se a execucao so foi proposta perto de 2024. Refazer com as datas reais dos autos (PA-03), nunca presumir.

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
