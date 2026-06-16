---
name: resposta-acusacao
description: >
  Skill Tier 2 — resposta a acusacao (CPP 396 e 396-A), primeira defesa na acao penal, prazo de 10 dias
  contados da citacao. Conteudo: preliminares (inepcia da denuncia CPP 41, falta de justa causa,
  incompetencia, ilegitimidade de parte, nulidades, litispendencia/coisa julgada), mérito defensivo,
  pedido de absolvicao sumaria (CPP 397 — atipicidade, excludentes de ilicitude/culpabilidade,
  extincao da punibilidade), arrolamento de testemunhas (limite do CPP 401 — 8 na comum, 5 no sumario,
  5 por fato no juri) e requerimento de diligencias/pericias. Distingue rejeicao x recebimento da
  denuncia. Polo: defesa. Ative em citacao, denuncia recebida, resposta a acusacao, defesa previa,
  absolvicao sumaria, inepcia, prazo de 10 dias.
metadata:
  version: "0.1.0"
  area: "Direito Penal e Processo Penal"
  tier: 2
---

# RESPOSTA A ACUSACAO (CPP 396 e 396-A)

> Tier 2. Primeira defesa apos o recebimento da denuncia/queixa. Prazo: **10 dias da citacao** (CPP 396). Pode levar a absolvicao sumaria (CPP 397). Polo: defesa. Selo P1 antes de produzir.

---

## 1. MOMENTO E PRAZO

- Recebida a denuncia/queixa, o reu e **citado** para responder em **10 dias** (CPP 396).
- Citacao por edital sem comparecimento → suspensao do processo e da prescricao (CPP 366) — atencao a PA-05.
- A resposta e **obrigatoria**; nao apresentada, nomeia-se defensor (CPP 396-A §2º).

## 2. CONTEUDO (CPP 396-A) — ARGUIR TUDO

A defesa pode (e deve) alegar **tudo o que interesse**: preliminares, mérito, documentos, justificacoes, especificar provas e arrolar testemunhas. Materia nao deduzida aqui (salvo as de ordem publica) pode precluir.

## 3. PRELIMINARES (ataque a relacao processual)

- **Inepcia da denuncia** (CPP 41): falta de exposicao do fato com todas as circunstancias, da qualificacao, da classificacao ou do rol — denuncia generica/inepta.
- **Falta de justa causa**: ausencia de lastro probatorio minimo (materialidade + indicios de autoria).
- **Incompetencia** (absoluta/relativa); **ilegitimidade** de parte (ativa/passiva).
- **Nulidades** (CPP 564) — inclusive provas ilicitas (CF 5 LVI; PA-07).
- **Litispendencia, coisa julgada, extincao da punibilidade** (prescricao — PA-05).

## 4. ABSOLVICAO SUMARIA (CPP 397)

Apos a resposta, o juiz **absolve sumariamente** quando verificar:
- **I** — existencia manifesta de **excludente de ilicitude** (CP 23 — legitima defesa, estado de necessidade, estrito cumprimento de dever, exercicio regular de direito).
- **II** — existencia manifesta de **excludente de culpabilidade** (salvo inimputabilidade — que pede absolvicao impropria com medida de seguranca).
- **III** — que o **fato nao constitui crime** (atipicidade).
- **IV** — **extinta a punibilidade** (prescricao, decadencia, morte, anistia — PA-05).

> Tese de absolvicao sumaria exige **clareza manifesta**; do contrario, sustenta-se a tese para a instrucao e alegacoes finais.

## 5. PROVA E TESTEMUNHAS

- **Arrolar testemunhas** no numero maximo: **8** (rito comum ordinario, CPP 401), **5** (sumario, CPP 532), **5 por fato** (1ª fase do juri). Contar so as que prestam compromisso (CPP 401 §1º).
- Requerer **diligencias e pericias**, juntada de documentos, expedicao de oficios.
- Especificar a **finalidade** de cada prova (evitar indeferimento por impertinencia).

## 6. REJEICAO x RECEBIMENTO DA DENUNCIA

- **Rejeicao** (CPP 395): inepcia, falta de pressuposto processual/condicao da acao, ou falta de justa causa → cabe **RESE** (CPP 581 I).
- Recebimento e despacho que, embora sucinto, deve enfrentar as teses defensivas relevantes; recebimento indevido pode gerar HC por falta de justa causa.

## 7. ESTRUTURA DA PECA

1. Enderecamento (juizo da acao penal) · 2. Qualificacao do reu · 3. Sintese da imputacao · 4. **Preliminares** (cada uma em topico) · 5. Do mérito / teses de absolvicao sumaria (CPP 397) · 6. Dos pedidos (rejeicao tardia/absolvicao sumaria; subsidiariamente, regular instrucao) · 7. **Do rol de testemunhas** e diligencias · 8. Provas.

## 8. INTEGRACAO

- **Chassi:** `templates/pecas/resposta-acusacao.md` — abrir e preencher os `[____]` antes de redigir (padrao enxuto da casa; ver `_LEIA-ME.md`).
- `calculos-criminais` → prescricao, prazo da citacao.
- `jurisprudencia-criminal` → validar sumulas/precedentes (PA-01).
- `analise-documental-criminal` → denuncia, IP, BO, laudos.
- `estilo-juridico-criminal` → forma · `revisao-final-criminal` → R1-R4.

## 9. CHECKLIST DE SAIDA

- [ ] Prazo de 10 dias controlado (CPP 396)
- [ ] Preliminares exauridas (inepcia, justa causa, competencia, nulidades)
- [ ] Hipoteses de absolvicao sumaria do CPP 397 avaliadas
- [ ] Extincao da punibilidade verificada (prescricao — PA-05)
- [ ] Rol de testemunhas dentro do limite do rito (CPP 401/532)
- [ ] Diligencias e pericias requeridas com finalidade
- [ ] Polo coerente (PA-10) · Selo P1 feito · R1-R4 pendente
