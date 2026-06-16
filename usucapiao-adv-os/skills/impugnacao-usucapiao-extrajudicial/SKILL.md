---
name: impugnacao-usucapiao-extrajudicial
description: >
  IMPUGNACAO USUCAPIAO EXTRAJUDICIAL — Skill Tier 2, procedimento de cartorio (Lei 6.015 art. 216-A).
  Side-aware. (a) Pelo CONFRONTANTE/interessado: IMPUGNA fundamentadamente, perante o oficial do RI, o
  pedido de usucapiao extrajudicial; impugnacao nao resolvida no extrajudicial faz o oficial remeter os
  autos ao juizo (a via vira judicial). (b) Pelo REQUERENTE: responde a impugnacao, suscita duvida ou
  converte em acao judicial. Cobre prazos e o efeito da impugnacao sobre a via. Acione no procedimento
  de usucapiao em cartorio quando ha impugnacao a apresentar ou a responder. Exige Selo P1. Gatilhos:
  impugnar usucapiao extrajudicial, oficial do RI, notificacao do confrontante, responder impugnacao,
  suscitar duvida, converter em acao.
metadata:
  version: "0.1.0"
  area: "Usucapiao (Judicial e Extrajudicial)"
  tier: 2
---

# IMPUGNACAO USUCAPIAO EXTRAJUDICIAL (cartorio)

> Skill **Tier 2** — procedimento administrativo no Registro de Imoveis (Lei 6.015 **art. 216-A** + Provimento CNJ). **Side-aware:** atua pelo **confrontante/interessado** (impugnando) ou pelo **requerente** (respondendo). So roda apos Selo P1.

---

## 0. PRE-REQUISITOS
- Procedimento de usucapiao **extrajudicial** instaurado/prenotado no RI.
- **Selo P1** emitido (Lei 6.015 art. 216-A + CPC art. 1.071 + Provimento CNJ vigentes — PA-01/PA-02).
- Identificar o **lado**: confrontante/interessado (impugnante) x requerente (resposta). Coerencia de polo (PA-10).

## 1. LADO A — CONFRONTANTE / INTERESSADO (impugnar)
- **Quem pode:** titular registral, confrontante, ente publico, terceiro interessado notificado.
- **Onde/como:** impugnacao **escrita e fundamentada** dirigida ao **oficial do Registro de Imoveis** (nao ao juiz).
- **Prazo:** apresentar **dentro do prazo da notificacao** (em regra **15 dias** — Lei 6.015 art. 216-A §2º; o **silencio** e tido como **concordancia**, por isso impugnar a tempo e decisivo). Verificar a redacao vigente no Selo (PA-01).
- **Fundamentos** (mesma musculatura da contestacao): a posse do requerente e **DETENCAO** (PA-09); falta **animus domini** (PA-08); posse viciada/interrompida; **metragem/confrontacoes** erradas (invasao de area do impugnante); **bem publico** (PA-04); **titulo/registro** do impugnante; ausencia de requisito da **modalidade** (PA-05).
- **Efeito:** havendo impugnacao **nao superada** no extrajudicial, o oficial **remete os autos ao juizo competente** (CPC art. 1.071 §… / art. 216-A §10) — **a via vira JUDICIAL**.

## 2. LADO B — REQUERENTE (responder a impugnacao)
- **Responder** a impugnacao perante o oficial, afastando os fundamentos e juntando provas (ata notarial, planta+ART, anuencias, comprovantes de posse) — `usucapiao-extrajudicial`.
- **Suscitar duvida** (Lei 6.015 art. 198) quando o impasse for com o **proprio oficial** (exigencia registral), levando a questao ao juiz corregedor.
- **Converter em acao judicial** (`acao-usucapiao`) quando a impugnacao instaura litigio insanavel no cartorio (PA-07: nao insistir na via extrajudicial havendo oposicao real).

## 3. EFEITO DA IMPUGNACAO SOBRE A VIA
Impugnacao fundamentada e nao resolvida **encerra a via extrajudicial** quanto ao ponto controvertido e **desloca para o juizo**. O conjunto documental do cartorio aproveita a fase judicial. Atualizar o CASO.md (mudanca de via).

## 4. CHECKLIST
- [ ] Lado definido (impugnante x requerente) · coerencia de polo (PA-10) · Selo P1 (PA-11)
- [ ] **Prazo** da notificacao observado (silencio = concordancia — impugnar a tempo)
- [ ] Fundamentos: detencao/animus (PA-08/09) · metragem · bem publico (PA-04) · modalidade (PA-05)
- [ ] Efeito sobre a via avaliado (remessa ao juizo / duvida / conversao em acao — PA-07)
- [ ] Jurisprudencia `[VERIFICAR]` (PA-01) · `revisao-final-usucapiao` R1-R4 (PA-13)

## 5. ENCERRAMENTO
Entrega a impugnacao (ou a resposta/duvida/conversao) com prazo e efeito sobre a via tratados, coerente com o polo. Migrando para o judicial, roteia para `acao-usucapiao` ou `contestacao-usucapiao`. Toda producao passa por `revisao-final-usucapiao` (PA-13).
