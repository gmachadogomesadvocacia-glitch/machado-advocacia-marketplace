---
name: habeas-corpus
description: >
  Skill flagship Tier 2 — habeas corpus (CF 5 LXVIII; CPP 647-667). Remedio constitucional contra
  coacao ou ameaca ilegal a liberdade de locomocao. Cobre as hipoteses do CPP 648: ausencia de justa
  causa, excesso de prazo, incompetencia, cessada a causa da prisao, nulidade, extincao da punibilidade.
  Aplicacoes: trancamento de inquerito/acao penal por falta de justa causa, relaxamento de prisao
  ilegal, revogacao de preventiva, liberdade, nulidades. HC liberatorio e preventivo (salvo-conduto).
  Define competencia (autoridade coatora), liminar, e a vedacao da Sumula 691 STF e sua superacao.
  Ative em prisao ilegal, constrangimento ilegal, trancamento, excesso de prazo ou ameaca a liberdade.
metadata:
  version: "0.1.0"
  area: "Direito Penal e Processo Penal"
  tier: 2
---

# HABEAS CORPUS (CF 5º LXVIII; CPP 647-667)

> Tier 2 flagship. Remedio heroico contra coacao/ameaca ilegal a liberdade de locomocao. Rapido, sem dilacao probatoria (prova pre-constituida). Polo: paciente (defesa). Gratuito, dispensa advogado, mas aqui se redige tecnicamente.

---

## 1. ESPECIES

- **HC liberatorio (repressivo)** — coacao ja consumada (prisao ilegal, processo em curso). Pedido: soltura/trancamento.
- **HC preventivo** — ameaca iminente a liberdade. Pedido: **salvo-conduto**.

## 2. HIPOTESES DE CABIMENTO (CPP 648 — coacao ilegal)

| Inciso | Hipotese | Uso tipico |
|--------|----------|-----------|
| I | Falta de justa causa | **Trancamento** de IP/acao penal; atipicidade; ausencia de indicios |
| II | Excesso de prazo na prisao | Prisao que extrapola prazo razoavel |
| III | Autoridade incompetente | Vicio de competencia |
| IV | Cessada a causa que autorizou | Desaparecimento do fundamento da preventiva |
| V | Nao admissao de fianca quando cabivel | — |
| VI | Processo manifestamente nulo | Nulidade (ex.: prova ilicita, cerceamento) |
| VII | Extinta a punibilidade | Prescricao, morte, anistia |

> **Trancamento** e medida excepcional — so com atipicidade flagrante, ausencia de justa causa ou prova ilicita evidente, sem revolvimento fatico-probatorio.

## 3. PRISAO PREVENTIVA — ATACAR OS REQUISITOS (CPP 312-313)

- Preventiva exige **fumus comissi delicti** (prova da materialidade + indicio de autoria) **E** periculum libertatis (garantia da ordem publica/economica, conveniencia da instrucao, aplicacao da lei penal) — CPP 312.
- **Contemporaneidade** do perigo (CPP 312 §2º) e fundamentacao concreta (CPP 315) — vedado fundamento abstrato/gravidade em tese.
- Cabimento so nos crimes do CPP 313 (doloso > 4 anos, reincidente, violencia domestica, dúvida sobre identidade).
- **Medidas cautelares diversas** (CPP 319) — adequacao e proporcionalidade; preventiva e ultima ratio.
- Revisao periodica a cada 90 dias (CPP 316 § unico).

## 4. COMPETENCIA (autoridade coatora define o juizo)

- Coator = juiz de 1º grau → HC no **TJ/TRF**.
- Coator = Turma/Camara ou relator de Tribunal → **STJ**.
- Coator = STJ → **STF**.
- Coator = delegado/autoridade administrativa → juiz de 1º grau.

## 5. SUMULA 691 STF (e sua superacao)

- Sum. 691: nao cabe HC contra decisao que indefere liminar em outro HC.
- **Superacao** admitida em flagrante ilegalidade/teratologia ou manifesto constrangimento ilegal — fundamentar a excepcionalidade.

## 6. ESTRUTURA DA PECA

1. Enderecamento (tribunal/juizo competente conforme o coator) · 2. Impetrante e Paciente (qualificacao) · 3. Autoridade coatora · 4. Dos fatos · 5. Do direito — a coacao ilegal (CPP 648, inciso) · 6. **Da liminar** (fumus boni iuris + periculum in mora — risco a liberdade) · 7. Pedidos (concessao da ordem; liminar; soltura/salvo-conduto/trancamento) · 8. Provas pre-constituidas (documentos).

## 7. INTEGRACAO

- `calculos-criminais` → prescricao/excesso de prazo, se for a tese.
- `jurisprudencia-criminal` → validar Sumulas/precedentes (PA-01).
- `analise-documental-criminal` → peca coatora, autos, decisao de prisao.
- `estilo-juridico-criminal` → forma · `revisao-final-criminal` → R1-R4.

## 8. CHECKLIST DE SAIDA

- [ ] Hipotese do CPP 648 corretamente enquadrada
- [ ] Prova pre-constituida (HC nao admite dilacao — PA-07)
- [ ] Competencia certa (pela autoridade coatora)
- [ ] Liminar fundamentada (fumus + periculum)
- [ ] Se preventiva: requisitos do CPP 312/313 atacados concretamente
- [ ] Polo coerente (PA-10) · Selo P1 feito · R1-R4 pendente
