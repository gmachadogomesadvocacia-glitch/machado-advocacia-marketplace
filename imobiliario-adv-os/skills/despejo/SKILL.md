---
name: despejo
description: >
  Skill flagship Tier 2 — acao de despejo e cobranca de alugueis (Lei 8.245/91). Cobre os dois polos:
  LOCADOR (despejo por falta de pagamento c/c cobranca, denuncia vazia/cheia, infracao contratual,
  para uso proprio, fim do prazo) e LOCATARIO (defesa, purgacao da mora art. 62, discussao de encargos,
  retencao por benfeitorias). Trata as liminares de despejo do art. 59 §1º (hipoteses taxativas +
  caucao de 3 alugueis), a purgacao da mora (art. 62, II), as garantias (fianca/caucao/seguro-fianca),
  o despejo na denuncia vazia (art. 46/57) e a execucao dos alugueis. Ative em despejo, falta de
  pagamento, denuncia vazia, retomada, cobranca de aluguel ou defesa do inquilino.
metadata:
  version: "0.1.0"
  area: "Direito Imobiliario e Locacao"
  tier: 2
---

# ACAO DE DESPEJO E COBRANCA (Lei 8.245/91)

> Tier 2 flagship. Side-aware: identificar se o cliente e **locador** (autor) ou **locatario** (reu). A peca e o tom mudam conforme o polo (PA-10).

---

## 1. FUNDAMENTO DO DESPEJO (escolher a causa correta)

| Causa | Base | Observacao |
|-------|------|-----------|
| Falta de pagamento (alugueis/encargos) | art. 9º, III + art. 62 | Cumula com cobranca; reu pode **purgar a mora** |
| Infracao legal/contratual | art. 9º, II | Ex.: sublocacao vedada, desvio de uso, dano |
| Denuncia vazia (residencial, contrato por prazo indeterminado) | art. 46 §2º / art. 57 | Sem motivo, apos 30 meses ou na prorrogacao |
| Denuncia cheia / retomada | art. 47 | Uso proprio, obras, etc. — exige motivacao |
| Fim do prazo (nao residencial) | art. 56/57 | Notificacao |
| Mutuo acordo / fim por descumprimento | art. 9º, I | — |

## 2. LIMINAR DE DESPEJO (art. 59 §1º) — HIPOTESES TAXATIVAS (PA-06)

Cabe liminar (desocupacao em 15 dias), **mediante caucao de 3 alugueis**, nas hipoteses do art. 59 §1º, entre elas:
- descumprimento do mutuo acordo (I);
- extincao do contrato de trabalho (II);
- termino do prazo da locacao para temporada (III);
- morte do locatario sem sucessor legitimo na locacao (IV);
- permanencia do sublocatario apos extincao (V);
- **falta de pagamento, em locacao sem qualquer das garantias do art. 37, e o reu nao purgar/contestar** (IX);
- termino do prazo notificado e nao desocupacao (VIII).

> Fora dessas hipoteses → NAO ha liminar; segue rito comum. Nunca pedir liminar sem enquadrar + sem oferecer a caucao (PA-06).

## 3. PURGACAO DA MORA (defesa do locatario — art. 62, II)

- O locatario pode **purgar a mora** no prazo de **15 dias** da citacao, pagando alugueis e encargos vencidos, multa, juros, custas e honorarios.
- Vedada a purgacao se ja houver ocorrido nos **24 meses** anteriores (art. 62, par. unico).
- Calcular o montante com `calculos-imobiliarios`.

## 4. GARANTIAS LOCATICIAS (art. 37-42)

- Modalidades: **caucao** (bens moveis/imoveis ou dinheiro, ate 3 alugueis), **fianca**, **seguro-fianca**, cessao fiduciaria de quotas de fundo.
- **Vedada a cumulacao** — so UMA modalidade por contrato (art. 37 § unico); exigir mais e contravencao (art. 43, PA-08).
- Fianca: exoneracao do fiador (art. 40); responsabilidade ate efetiva entrega das chaves se houver clausula (Sum. 214 STJ — fiador nao responde por aditamento que nao anuiu).

## 5. ESTRUTURA DA PECA

> **Chassi pronto:** `templates/pecas/acao-despejo-cobranca.md` (padrao enxuto; abrir e substituir `[____]` antes de redigir).

**Despejo por falta de pagamento c/c cobranca (locador):**
1. Enderecamento (foro do imovel/eleicao) · 2. Qualificacao · 3. Do contrato e da mora · 4. Do direito (art. 9º III / 62) · 5. Da liminar, se cabivel (art. 59 §1º IX + caucao) · 6. Pedidos: rescisao + despejo + condenacao nos alugueis/encargos vencidos e vincendos + multa + honorarios · 7. Valor da causa (12 alugueis — art. 58, III) · 8. Provas.

**Defesa do locatario:** contestacao + **purgacao da mora** (se cabivel) OU impugnacao do debito (encargos indevidos, recibos), retencao/indenizacao por benfeitorias necessarias (art. 35), excesso de cobranca.

## 6. INTEGRACAO

- `calculos-imobiliarios` → debito, purgacao, atualizacao (indice contratual, multa, juros).
- `jurisprudencia-imobiliaria` → validar Sumulas (PA-01).
- `analise-documental-imobiliaria` → contrato, comprovantes, notificacao.
- `estilo-juridico-imobiliario` → forma · `revisao-final-imobiliaria` → R1-R4.

## 7. CHECKLIST DE SAIDA

- [ ] Causa de despejo correta e fundamentada
- [ ] Liminar so se enquadrada no art. 59 §1º + caucao (PA-06)
- [ ] Purgacao da mora avaliada (cabe? ja usou nos 24 meses?)
- [ ] Garantia conferida (uma so — PA-08)
- [ ] Valor da causa (12 alugueis) · Foro do imovel
- [ ] Polo coerente (PA-10) · Selo P1 feito · R1-R4 pendente
