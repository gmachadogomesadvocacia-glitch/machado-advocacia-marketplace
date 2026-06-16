---
name: revisao-final-isencao-ir
description: >
  REVISAO FINAL ISENCAO-IR — Skill Tier 3, a Suprema Corte do plugin. Auditoria invariante R1-R4
  obrigatoria sobre todo documento (acao, requerimento administrativo, MS, calculo, parecer) ANTES da
  entrega: R1 coleta/escopo, R2 base juridica, R3 tese/coerencia de polo, R4 completude/estilo. Cada
  etapa emite APROVADO, APROVADO COM RESSALVAS ou REPROVADO; reprovacao bloqueia a entrega. Acione
  SEMPRE antes de entregar, ou quando o usuario pedir revisar/auditar/conferir antes de protocolar.
  Bypass so com --no-corte/--quick explicito.
metadata:
  version: "0.1.0"
  area: "Isencao de IRPF por Doenca Grave"
  tier: 3
---

# REVISAO FINAL ISENCAO-IR (Suprema Corte R1-R4)

> Skill **Tier 3**, invariante (Protocolo P6). Nenhum documento sai sem passar aqui (PA-14). Audita em 4 rodadas; reprovacao em qualquer uma bloqueia a entrega.

---

## 0. ESCOPO
Auditar, nao reescrever. Aponta a falha exata, classifica e devolve. Aplica-se a acao, requerimento administrativo, retificacao DIRPF, MS, calculo, parecer.

## 1. R1 — COLETA E ESCOPO
- Documentos analisados? Laudo (doenca/CID/data), comprovantes de IR retido, carta de concessao, DIRPF?
- **Selo P1 EMITIDO** (Lei 7.713/88 + IN RFB + Sum. 598/627)? Sem Selo → REPROVADO.
- Dados reais (doenca, valores, datas, fonte)? Nada inventado (PA-03)? Faltou doc → `[INFORMAR]`?
- **Nenhuma opiniao sobre conduta clinica/diagnostico** (PA-04)?

## 2. R2 — BASE JURIDICA
- Art. 6, XIV, Lei 7.713/88 vigente? IN RFB 1500/2014?
- Jurisprudencia validada (PA-01): **Sumula 598** (prova flexivel) e **Sumula 627** (manutencao) corretamente aplicadas?
- Doenca **dentro do rol taxativo** (PA-05)? Isencao limitada a **proventos** (PA-06)?
- Restituicao limitada aos **ultimos 5 anos** (CTN art. 168 — PA-09)?
- Foro/rito corretos (domicilio do contribuinte; Justica Federal; JEF ate 60 SM)?

## 3. R3 — TESE
- **Coerencia de polo** (PA-12) — nada contra o lado do cliente?
- FATO (doenca + provento + retencao) → DIREITO (art. 6 XIV + sumulas) → CONCLUSAO (pedidos) amarrados?
- Pedido de isencao + repeticao + tutela completos e determinados?
- Antecipacao adversarial: a Fazenda alegara que a doenca nao se enquadra, que o rendimento e de ativo, ou contemporaneidade — neutralizado?

## 4. R4 — COMPLETUDE E ESTILO
- Estrutura da peca completa (enderecamento, qualificacao, fatos, direito, pedidos, valor da causa)?
- Restituicao quantificada (calculo anexo)? Valor da causa correto?
- Estilo enxuto, docs "doc. N"; tom firme e **humano** (cliente doente)?
- **Dado de saude protegido** (PA-10) — segredo de justica quando necessario; sem exposicao desnecessaria de CID?

## 5. VEREDITO
Cada rodada: **APROVADO** / **APROVADO COM RESSALVAS** (registra no CASO.md) / **REPROVADO** (bloqueia; aponta rodada+item+PA; devolve). Encerrar com o quadro R1-R4 + veredito final.

## 6. BYPASS
Apenas `--no-corte` / `--quick` explicito, registrado. Sem bypass silencioso (PA-14).

## 7. ENCERRAMENTO
So libera o documento que passa nas 4 rodadas. E a ultima barreira antes do protocolo.
