---
name: revisao-final-usucapiao
description: >
  REVISAO FINAL USUCAPIAO — Skill Tier 3, a Suprema Corte do plugin. Auditoria invariante R1-R4
  obrigatoria sobre todo documento (acao, requerimento extrajudicial, contestacao, impugnacao, parecer)
  ANTES da entrega: R1 coleta/escopo, R2 base juridica, R3 tese/coerencia de polo, R4 completude/estilo.
  Cada etapa emite APROVADO, APROVADO COM RESSALVAS ou REPROVADO; reprovacao bloqueia a entrega. Acione
  SEMPRE antes de entregar, ou quando o usuario pedir revisar/auditar/conferir antes de protocolar.
  Bypass so com --no-corte/--quick explicito.
metadata:
  version: "0.1.0"
  area: "Usucapiao (Judicial e Extrajudicial)"
  tier: 3
---

# REVISAO FINAL USUCAPIAO (Suprema Corte R1-R4)

> Skill **Tier 3**, invariante (Protocolo P6). Nenhum documento sai sem passar aqui (PA-13). Audita em 4 rodadas; reprovacao em qualquer uma bloqueia a entrega.

---

## 0. ESCOPO
Auditar, nao reescrever. Aponta a falha exata, classifica e devolve. Aplica-se a acao, requerimento extrajudicial, contestacao, impugnacao, parecer.

## 1. R1 — COLETA E ESCOPO
- Documentos analisados? Matricula/certidao do RI, **planta e memorial com ART**, comprovantes de posse, anuencias?
- **Selo P1 EMITIDO**? Sem Selo → REPROVADO.
- Dados reais (imovel, metragem, confrontantes, tempo de posse)? Nada inventado (PA-03)? Faltou doc → `[INFORMAR]`?

## 2. R2 — BASE JURIDICA
- CC arts. 1.238-1.244 + CF 183/191 + CPC + Lei 6.015 art. 216-A + Provimento CNJ vigentes?
- Jurisprudencia validada (PA-01)?
- **Modalidade correta e requisitos atendidos** (tempo, metragem, justo titulo/boa-fe — PA-05)?
- **Bem nao publico** (PA-04)? Posse ad usucapionem (nao detencao — PA-08/PA-09)?
- **Citacoes completas** no judicial (confrontantes + titulares + Uniao/Estado/Municipio + edital — PA-06)? OU consenso/anuencias no extrajudicial (PA-07)?
- Foro (situacao do imovel) / RI da circunscricao corretos (P5)?

## 3. R3 — TESE
- **Coerencia de polo** (PA-10)?
- FATO (posse + imovel) → DIREITO (modalidade + requisitos) → CONCLUSAO (pedido de dominio/registro) amarrados?
- Antecipacao adversarial: a oposicao alegara detencao, falta de animus domini, interrupcao da posse, bem publico, ou ausencia de requisito — neutralizado?

## 4. R4 — COMPLETUDE E ESTILO
- Estrutura completa (qualificacao, descricao do imovel, fundamento, pedidos, valor da causa)?
- **Descricao do imovel apta a REGISTRO** (planta/memorial coerentes)?
- Estilo tecnico e enxuto, docs "doc. N"? Pedido determinado?

## 5. VEREDITO
Cada rodada: **APROVADO** / **APROVADO COM RESSALVAS** (registra no CASO.md) / **REPROVADO** (bloqueia; aponta rodada+item+PA; devolve). Encerrar com o quadro R1-R4 + veredito final.

## 6. BYPASS
Apenas `--no-corte` / `--quick` explicito, registrado (PA-13).

## 7. ENCERRAMENTO
So libera o documento que passa nas 4 rodadas. E a ultima barreira antes do protocolo/registro.
