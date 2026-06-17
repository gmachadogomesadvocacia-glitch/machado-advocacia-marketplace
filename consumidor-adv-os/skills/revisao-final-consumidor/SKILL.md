---
name: revisao-final-consumidor
description: >
  REVISAO FINAL CONSUMIDOR — Skill Tier 3, a Suprema Corte do plugin. Auditoria invariante R1-R4
  obrigatoria sobre todo documento consumerista (peca, defesa, parecer, calculo, reclamacao
  administrativa) ANTES da entrega: R1 coleta/escopo, R2 base juridica, R3 tese/coerencia de polo, R4
  completude/estilo. Cada etapa emite APROVADO, APROVADO COM RESSALVAS ou REPROVADO; reprovacao bloqueia
  a entrega e devolve ao produtor. Acione SEMPRE antes de entregar qualquer documento, ou quando o
  usuario pedir revisar, auditar, conferir antes de protocolar. Bypass so com --no-corte/--quick
  explicito, registrado.
metadata:
  version: "0.1.0"
  area: "Direito do Consumidor e Bancario"
  tier: 3
---

# REVISAO FINAL CONSUMIDOR (Suprema Corte R1-R4)

> Skill **Tier 3**, invariante. Operacionaliza o **Protocolo P6**. Nenhum documento sai sem passar por aqui (PA-22). Audita em 4 rodadas sequenciais; reprovacao em qualquer uma bloqueia a entrega.

---

## 0. ESCOPO

Auditar — nao reescrever do zero. Aponta falhas exatas, classifica e devolve. Aplica-se a toda saida de producao: inicial, contestacao, replica, recurso, tutela, calculo, parecer, reclamacao administrativa, acordo.

## 1. R1 — COLETA E ESCOPO

- Documentos do caso analisados? Faltou doc essencial sem `[INFORMAR]`? (PA-15)
- **Selo de Validacao Legal Previa EMITIDO** (P1)? Sem Selo → REPROVADO.
- Escopo unico (peca ≠ parecer ≠ calculo ≠ comunicacao)? Sem mistura de escopos.
- Dados do caso reais (partes, datas, valores, contrato)? Nada inventado (PA-03).

## 2. R2 — BASE JURIDICA

- CDC e lei especial **vigentes a epoca do fato gerador**?
- Jurisprudencia **classificada e validada** (PA-01)? Sem citacao alucinada (PA-02).
- Sumulas-chave conferidas conforme o caso: **385** (negativacao), **382** (>12% nao e per se abusivo) + **530** (taxa media BACEN na impossibilidade de provar a contratada), **539/541** (capitalizacao), **543** (distrato), **Tema 929** (dobro art. 42).
- Relacao de consumo verificada (destinatario final + vulnerabilidade — PA-04)?
- Prazos: decadencia (art. 26), prescricao (art. 27), arrependimento (art. 49), recurso JEC (10 dias)?
- Competencia/rito corretos (foro do consumidor art. 101; JEC x comum — PA-19)?

## 3. R3 — TESE

- **Coerencia de polo** (PA-05) — nenhum argumento contra o lado do cliente?
- FATO-NEXO-DIREITO amarrados em FIRAC?
- Inversao do onus **fundamentada** (verossimilhanca/hipossuficiencia, art. 6 VIII — PA-12)?
- Repeticao em **dobro** so com cobranca indevida + **engano injustificavel** (art. 42 + Tema 929 — PA-06)?
- Dano moral por negativacao passou pelo crivo da **Sumula 385** (PA-07)?
- Nulidade de clausula com o **inciso do art. 51** (PA-13)?
- **Antecipacao adversarial** presente (a melhor tese do adversario foi neutralizada)?

## 4. R4 — COMPLETUDE E ESTILO

- Estrutura do tipo de peca completa (enderecamento, qualificacao, fatos, direito, pedidos, valor da causa, requerimentos)?
- Pedidos **determinados**; **dano moral quantificado** (nao "a arbitrar" puro)?
- Estilo do escritorio: enxuto (~5 pgs), docs numerados "doc. N" e citados por numero, sem rol prolixo?
- Tom coerente com o polo e a persona; sem ataque pessoal (PA-17); sem tom dubitativo indevido?
- Superendividamento: minimo existencial preservado (PA-14)?

## R5 — VERIFICACAO ADVERSARIAL (RED-TEAM)

Mude de chapeu: voce AGORA e o fornecedor/banco / o juizo cetico. Unica missao: DERROTAR a peca. Achou UMA falha → REPROVADO. Eixos:

- **VALORES** — repeticao em dobro (art. 42 + Tema 929), revisao de juros/encargos e dano moral vem do `calculos-consumidor`?
- **RELACAO DE CONSUMO** — ha relacao de consumo (CDC aplicavel — Sum. 297 p/ bancos)? inversao do onus cabivel?
- **INSTRUMENTO/VIA** — peca certa (revisional x indenizatoria x defesa busca e apreensao)?
- **CITACOES** — Sum. 297/382/385/530 e Temas batem em tese? (530 = impossibilidade de provar a taxa, nao "abusividade".)
- **PRESCRICAO** — CDC art. 27 (5 anos) / CC conforme o caso, bem aplicado?
- **POLO** — coerente (consumidor x fornecedor)?

**Veredito R5:** PASSOU / REPROVADO (eixo + falha + correcao).

## FICHA DE CONFERENCIA (acompanha a entrega, nao integra a peca)

```
FICHA DE CONFERENCIA — pre-protocolo
- PREMISSAS: ...
- VALORES (cada R$ → fonte): R$ __ — origem calculos-consumidor
- CITACOES (cada uma → status): Sum. 297/385 STJ — CONFIRMADO | VALIDAR
- LACUNAS [INFORMAR]: ...
- RISCOS / PONTOS ADVERSARIAIS: ...
- VEREDITO: R1 _ · R2 _ · R3 _ · R4 _ · R5 _
- PENDE O OK INFORMADO DO ADVOGADO antes do protocolo.
```

## 5. VEREDITO

Cada rodada emite um dos tres:
- **APROVADO** — segue.
- **APROVADO COM RESSALVAS** — segue, mas registra as ressalvas no CASO.md para ciencia do advogado.
- **REPROVADO** — bloqueia. Apontar a falha exata (rodada + item + PA tocada) e devolver ao produtor para correcao; resubmeter apos corrigir.

Encerrar com o quadro: R1 [..] · R2 [..] · R3 [..] · R4 [..] · R5 [..] · **Veredito final** — e anexar a FICHA DE CONFERENCIA.

## 6. BYPASS

Apenas com `--no-corte` / `--quick` explicito do operador, registrado em log. Sem bypass silencioso (PA-22).

## 7. ENCERRAMENTO

So libera a entrega o documento que passa nas rodadas R1-R5 e que sai acompanhado da FICHA DE CONFERENCIA. A Suprema Corte e a ultima barreira antes do protocolo — e inviolavel.
