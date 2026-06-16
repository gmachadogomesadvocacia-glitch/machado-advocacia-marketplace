---
name: linha-estrategica-usucapiao
description: >
  LINHA ESTRATEGICA USUCAPIAO — Skill Tier 1. Consolida a analise trilateral e a jurisprudencia e
  define a linha do caso: a VIA (judicial x extrajudicial — extrajudicial so com CONSENSO/anuencias;
  havendo litigio/oposicao vai para judicial, PA-07), a MODALIDADE mais favoravel (quando cabe mais de
  uma, a de menor prazo/menos requisitos — ex.: extraordinaria dispensa justo titulo), o foro (situacao
  do imovel) ou o RI da circunscricao, e a interface com possessorias/reivindicatoria. Respeita
  {{MODO_MELHOR_SAIDA}}. Acione apos a trilateral/jurisprudencia, quando o usuario pede a estrategia, a
  melhor via, a melhor modalidade ou a linha de acao. Saida: linha estrategica para o advogado validar.
metadata:
  version: "0.1.0"
  area: "Usucapiao (Judicial e Extrajudicial)"
  tier: 1
---

# LINHA ESTRATEGICA USUCAPIAO

> Skill **Tier 1**. Consolida `analise-trilateral-usucapiao` + `jurisprudencia-usucapiao` e fecha as decisoes estruturais do caso (via, modalidade, foro/RI, interface com outras acoes). Roda apos os insumos e antes da producao. Respeita `{{MODO_MELHOR_SAIDA}}`.

---

## 0. PRE-REQUISITOS
- Triagem feita, **Selo P1** emitido, posse analisada (`analise-posse-usucapiao`).
- Trilateral e jurisprudencia consolidadas. Faltando dado → `[INFORMAR]` (PA-03), nunca inventar.

## 1. DECISAO 1 — VIA (judicial x extrajudicial)
- **Extrajudicial (cartorio)** — SO com **CONSENSO**: anuencia dos confrontantes e titulares (ou silencio = concordancia, Lei 6.015 art. 216-A), ata notarial, planta/memorial com **ART**. Sem litigio.
- **Judicial** — sempre que houver **litigio/oposicao**, falta de anuencia, reu incerto, ou ente publico em conflito. Propor a extrajudicial havendo oposicao/sem requisitos e **violacao (PA-07)**.
- Regra: na duvida sobre consenso, **judicial**. A via extrajudicial pode virar judicial a qualquer momento (oposicao superveniente).

## 2. DECISAO 2 — MODALIDADE MAIS FAVORAVEL (PA-05)
- Quando **mais de uma** modalidade cabe, escolher a de **menor prazo / menos requisitos**:
  - **Extraordinaria** (CC 1.238, 15/10 anos) **dispensa justo titulo e boa-fe** (Sum. 391 STF `[VERIFICAR]`) — escolha segura quando faltar titulo.
  - **Especial urbana** (1.240/CF 183, 5 anos, ate 250 m2, moradia, nao proprietario) ou **rural** (1.239, 50 ha) quando o perfil do imovel/posse encaixa — prazo menor.
  - **Familiar** (1.240-A, **2 anos**) so no cenario de abandono do lar por ex-conjuge/companheiro.
- Conferir requisitos antes de fixar: tempo, metragem, justo titulo, boa-fe, moradia, nao ser proprietario de outro imovel. **Bem PUBLICO nao e usucapivel (PA-04).**
- Toda tese sobre modalidade/requisito apoiada em lei vigente (Selo) e jurisprudencia `[VERIFICAR]` via `jurisprudencia-usucapiao` (PA-01).

## 3. DECISAO 3 — FORO / REGISTRO (P5)
- **Judicial:** foro da **situacao do imovel** (CPC art. 47).
- **Extrajudicial:** **Registro de Imoveis da circunscricao** do imovel.

## 4. DECISAO 4 — INTERFACE COM OUTRAS ACOES
- **Possessoria** em curso (do confrontante/terceiro): a usucapiao pode ser arguida como **materia de defesa** (Sum. 237 STF `[VERIFICAR]`) e/ou ajuizada a acao propria; avaliar reconvencao/conexao.
- **Reivindicatoria** do titular registral: a posse ad usucapionem ja consumada e **defesa de merito**; alinhar a tese para nao confessar detencao (PA-09).
- Mapear medidas urgentes (manutencao/reintegracao, registro de protesto) conforme o polo.

## 5. MELHOR SAIDA
Respeitar `{{MODO_MELHOR_SAIDA}}`: apontar a via e a modalidade de **maior probabilidade de exito com menor custo/prazo**, com as subsidiarias e os riscos (oposicao de confrontante, bem publico, metragem, interrupcao da posse).

## 6. SAIDA — LINHA ESTRATEGICA (para validar)
```
LINHA ESTRATEGICA — [cliente]
- Polo: [usucapiente / confrontante]
- Via recomendada: [judicial / extrajudicial] + motivo (consenso? litigio?)
- Modalidade principal: [...] (prazo/requisitos) | Subsidiarias: [...]
- Foro / RI: [situacao do imovel / RI da circunscricao]
- Interface: [possessoria / reivindicatoria / nenhuma] + medida
- Riscos: [oposicao · bem publico · metragem · interrupcao]
- Proxima peca: [acao-usucapiao / usucapiao-extrajudicial / contestacao / impugnacao]
```

## 7. ENCERRAMENTO
Entrega a linha estrategica para o advogado validar e roteia para a producao (`estilo-juridico-usucapiao`), que termina em `revisao-final-usucapiao` R1-R4 (PA-13).
