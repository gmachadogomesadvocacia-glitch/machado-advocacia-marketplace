---
name: linha-estrategica-transito
description: >
  Linha estrategica de transito Tier 1 — consolida a trilateral, a jurisprudencia e os calculos e define
  a instancia e a sequencia. Eixos de decisao: qual fase/instancia atacar (defesa previa × JARI × CETRAN ×
  judicial), efeito suspensivo, custo/beneficio (valor da multa × pontos × risco de suspensao), quando
  esgotar a via administrativa antes do judicial, quando ir direto ao mandado de seguranca (vicio formal
  evidente, direito liquido e certo). Avalia indicacao do real condutor × defesa. Decisao documentada e
  porta de producao indicada. Ative apos a trilateral, quando o usuario pedir a estrategia, a melhor tese,
  a instancia certa ou a sequencia de recursos.
metadata:
  version: "0.1.0"
  area: "Direito de Transito"
  tier: 1
---

# LINHA ESTRATEGICA DE TRANSITO

> Tier 1. Consolida `analise-trilateral-transito` + `jurisprudencia-transito` + `calculos-transito` e decide **onde** atacar, **em que ordem** e **com que peca**. Decisao **documentada** (vai ao CASO.md) e com a **porta de producao** indicada.

---

## 1. EIXOS DE DECISAO

**A. Fase / instancia** (nao confundir — PA-08)
- **Defesa previa / da autuacao** (apos a NA) — primeira oportunidade; ataca o auto antes da penalidade.
- **Recurso a JARI** (apos a NP) — 1ª instancia administrativa.
- **Recurso ao CETRAN** — 2ª instancia administrativa; esgota a via.
- **Judicial** — anulatoria ou mandado de seguranca.

**B. Efeito suspensivo**
- Verificar se o recurso suspende a exigibilidade (multa/pontos) ou se ha cobranca/pontuacao em curso; no judicial, avaliar **liminar/tutela**.

**C. Custo/beneficio** (com `calculos-transito`)
- valor da multa × pontos em jogo × **risco de suspensao** (limite 20/30/40) × custo da via × probabilidade da tese.
- Multa baixa e isolada → via administrativa basta; risco de suspensao iminente → priorizar a defesa que retira pontos.

**D. Administrativo antes do judicial?**
- Regra pratica: **esgotar a via administrativa** quando ha tese de merito a desenvolver e prazo confortavel.
- **Ir direto ao MS** quando ha **vicio formal evidente** e **direito liquido e certo** (ex.: ausencia comprovada de notificacao), com risco de preclusao/ato iminente.

**E. Indicacao de condutor × defesa**
- So indicar o **real** condutor (PA-06 — indicacao falsa e crime). Avaliar se a indicacao legitima e melhor que a defesa do proprietario.
- Embriaguez/acidente com vitima → checar se e **crime** (306, 302/303) → `criminal-adv-os` (PA-09).

## 2. MATRIZ DE ESCOLHA

```
TESE CENTRAL: ... (forca / instancia ideal)
TESES SUBSIDIARIAS: ...
INSTANCIA ESCOLHIDA: defesa previa | JARI | CETRAN | anulatoria | MS
EFEITO SUSPENSIVO / LIMINAR: necessario? sim/nao
CUSTO×BENEFICIO: valor × pontos × risco suspensao → vale a pena?
SEQUENCIA: passo 1 → passo 2 → ...
RISCO PRINCIPAL: ...
```

## 3. SAIDA

```
DECISAO ESTRATEGICA
  tese central: ...
  instancia/peca: <skill de producao>
  efeito suspensivo/tutela: ...
  sequencia recursal: ...
  prazo que governa: vence DD/MM (PA-05)
  registrar no CASO.md: sim
PORTA DE PRODUCAO:
  administrativo → defesa-autuacao | recursos-administrativos
  CNH → suspensao-direito-dirigir | cassacao-cnh | indicacao-condutor
  judicial → anulatoria-transito | mandado-seguranca-transito
  especifico → defesa-radar-equipamentos
```

## 4. INTEGRACAO

- Entra **apos** a trilateral; consome jurisprudencia validada (PA-01) e calculos (prazos/pontos).
- Grava a decisao em `memoria-de-caso-transito`.
- Aponta a skill de producao; estilo por `estilo-juridico-transito`; auditoria por `revisao-final-transito`.

## 5. CHECKLIST DE SAIDA

- [ ] Instancia escolhida e justificada (PA-08)
- [ ] Efeito suspensivo / liminar avaliado
- [ ] Custo×beneficio (valor × pontos × suspensao) feito
- [ ] Administrativo vs. MS direto decidido com criterio
- [ ] Indicacao de condutor so se for o real (PA-06); crime → criminal-adv-os (PA-09)
- [ ] Decisao documentada no CASO.md; porta de producao indicada
