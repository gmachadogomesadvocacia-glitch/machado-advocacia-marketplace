---
name: contestacao-usucapiao
description: >
  CONTESTACAO USUCAPIAO — Skill Tier 2 (lado confrontante/reu). Redige a DEFESA na acao de usucapiao:
  preliminares (CPC art. 337) e merito para DESCARACTERIZAR a posse do autor — e detencao/permissao/
  comodato e nao posse (PA-09), falta animus domini, posse violenta/clandestina/precaria nao usucape,
  interrupcao/oposicao que quebra a continuidade — impugnar metragem/confrontacoes, alegar BEM PUBLICO
  (PA-04) ou o justo titulo/registro do reu, e a posse do proprio confrontante. Side-aware
  (confrontante/reu). Acione quando o cliente e o confrontante/titular/reu e ha acao de usucapiao a
  contestar. Exige Selo P1, matricula/certidoes e a analise de posse.
metadata:
  version: "0.1.0"
  area: "Usucapiao (Judicial e Extrajudicial)"
  tier: 2
---

# CONTESTACAO USUCAPIAO (defesa)

> Skill **Tier 2** — lado **confrontante/titular/reu**. Defesa na acao de usucapiao. So roda apos triagem, Selo P1 e analise de posse. **Side-aware:** toda tese serve a quem se opoe ao reconhecimento (PA-10).

---

## 0. PRE-REQUISITOS
- Polo = confrontante / titular registral / ente publico. Via = judicial.
- **Selo P1** emitido. Matricula/certidao do RI do reu, planta/contratos, prova da oposicao. Falta → `[INFORMAR]` (PA-03).

## 1. PRELIMINARES (CPC art. 337)
Conforme o caso: incompetencia (foro da situacao do imovel), inepcia (descricao do imovel insuficiente/sem planta+ART), ilegitimidade, ausencia de citacao de confrontante/ente obrigatorio (PA-06), litispendencia/coisa julgada, conexao com possessoria/reivindicatoria.

## 2. MERITO — EIXOS DE DEFESA
1. **Descaracterizar a posse do autor (nuclear):**
   - E **DETENCAO**, nao posse (PA-09): comodato, locacao, permissao, mera tolerancia, posse a titulo precario — o detentor **nao usucape**.
   - Falta **animus domini** (PA-08): nunca se comportou como dono.
   - Posse **violenta, clandestina ou precaria** nao conduz a usucapiao (vicios objetivos).
   - **Interrupcao/oposicao** que quebra a continuidade: notificacoes, acoes, esbulho repelido, pagamentos do titular — afasta posse mansa/pacifica/ininterrupta.
2. **Impugnar metragem e confrontacoes** — divergencia entre a planta/memorial e a area real; invasao de area do confrontante; descricao inapta a registro.
3. **Bem PUBLICO (PA-04)** — imovel publico **nao e usucapivel** (CF 183§3/191§un; Sum. 340 STF `[VERIFICAR]`).
4. **Titulo/registro do reu** — propriedade registrada em nome do confrontante/titular; cadeia dominial integra.
5. **Posse do proprio confrontante** — demonstrar que **quem exerce a posse** ad usucapionem (ou a propriedade) e o cliente, nao o autor.
6. **Erro de modalidade/requisitos do autor (PA-05)** — tempo insuficiente, metragem acima do limite (especiais), falta de justo titulo/boa-fe (ordinaria), autor proprietario de outro imovel.

## 3. ESTRUTURA (FIRAC)
Preliminares · impugnacao especificada dos fatos (CPC art. 341 — nada de impugnacao generica) · merito pelos eixos acima, com docs "doc. N" (matricula, contratos, notificacoes) · pedidos: acolher preliminares / julgar **improcedente** o reconhecimento do dominio / condenar em sucumbencia.

## 4. CHECKLIST
- [ ] Coerencia de polo (confrontante — PA-10) · Selo P1 (PA-11)
- [ ] Posse do autor atacada: detencao (PA-09) · animus domini (PA-08) · vicios · interrupcao
- [ ] Metragem/confrontacoes impugnadas · bem publico avaliado (PA-04)
- [ ] Titulo/registro e posse do cliente demonstrados · impugnacao especificada (art. 341)
- [ ] Jurisprudencia `[VERIFICAR]` (PA-01) · `revisao-final-usucapiao` R1-R4 (PA-13)

## 5. CHASSI
Redigir a partir do modelo da casa: **`templates/pecas/contestacao-usucapiao.md`** (padrao enxuto, side-aware, ler a NOTA DE USO antes). Nao duplicar o modelo aqui.

## 6. ENCERRAMENTO
Entrega a contestacao com preliminares e os eixos de merito que descaracterizam a posse do autor, coerente com o polo, pronta para a Suprema Corte R1-R4.
