---
name: recursos-administrativos
description: >
  Skill Tier 2 — RECURSOS ADMINISTRATIVOS nas duas instancias, apos a Notificacao de Penalidade (NP).
  (1) Recurso a JARI (Junta Administrativa de Recursos de Infracoes — 1ª instancia; CTB 285); prazo
  30 dias da NP. (2) Recurso ao CETRAN/CONTRANDIFE (2ª instancia; CTB 288-290); deposito previo
  VEDADO (validar). Efeitos diferem por instancia (validar CTB 288 §2º). Conteudo: reitera e amplia as
  nulidades formais do AIT (CTB 280) e da dupla notificacao (Sum. 312) + merito. NAO confundir com defesa
  previa, que e anterior a NP (PA-08). Ative ao receber a Notificacao de Penalidade, recorrer a JARI ou ao
  CETRAN, redigir recurso administrativo de multa de transito ou recorrer da decisao da JARI.
metadata:
  version: "0.1.0"
  area: "Direito de Transito"
  tier: 2
---

# RECURSOS ADMINISTRATIVOS — JARI E CETRAN (CTB 285-290)

> Tier 2. Atua **apos a Notificacao de Penalidade (NP)** — a multa ja foi aplicada. Duas instancias administrativas sucessivas. Persona: {{ADVOGADO_NOME}} ({{OAB_UF}} {{OAB_NUMERO}}), {{FIRM_NAME}}. Tom: {{TOM_VOZ_PERFIL}} / {{TOM_VOZ_INTENSIDADE}}.

---

## 1. POSICAO NO FLUXO (PA-08)

```
DEFESA PREVIA (antes da NP) → julgamento → NP → RECURSO JARI (1ª inst.) → RECURSO CETRAN (2ª inst.)
```

- **Recurso so apos a NP.** Antes da NP, o caminho e **defesa previa** (skill `defesa-autuacao`) — nao confundir as fases (PA-08).
- Nao se "pula" a JARI: o CETRAN e instancia recursal da decisao da JARI.

## 2. 1ª INSTANCIA — JARI (CTB 285)

- **Orgao:** Junta Administrativa de Recursos de Infracoes, vinculada ao orgao autuador.
- **Prazo:** 30 dias da NP (PA-05 — preclusivo; conferir a data na NP, PA-03).
- **Efeito:** em regra **nao suspende a exigibilidade da multa**; ha hipoteses na 1ª instancia (validar CTB 288 §2º) — NUNCA afirmar efeito suspensivo sem validar.
- **Deposito previo VEDADO** como condicao de admissibilidade (validar — entendimento consolidado).

## 3. 2ª INSTANCIA — CETRAN / CONTRANDIFE (CTB 288-290)

- **Orgao:** CETRAN (estadual) ou CONTRANDIFE (infracoes federais/orgaos da Uniao).
- **Cabimento:** recurso da decisao da JARI que **manteve** a penalidade.
- **Prazo:** 30 dias da notificacao da decisao da JARI (PA-05).
- **Deposito previo VEDADO** (validar) — exigencia de garantia/recolhimento como requisito e ilegal.
- **Efeito:** verificar caso a caso (CTB 288-290 — validar).

## 4. CONTEUDO (reitera + amplia)

- Reitera as **nulidades** ja deduzidas (CTB 280; dupla notificacao — Sum. 312; identificacao; equipamento; competencia; sinalizacao) alimentadas por `analise-vicios-auto-infracao`.
- **Amplia**: enfrenta a motivacao da decisao recorrida; aponta omissao/contradicao do julgado; junta a certidao de aferição obtida; reforca o merito (inexistencia).
- Coerencia da tese de defesa entre as instancias (PA-10) — nao contradizer o que se alegou antes.

## 5. ESTRUTURA DOS DOIS RECURSOS

1. **Enderecamento** — a JARI (1ª inst.) ou ao CETRAN/CONTRANDIFE (2ª inst.).
2. **Identificacao do auto e do recorrente** — nº AIT, placa, infracao, nº do processo administrativo; qualificacao.
3. **Tempestividade** — data da NP (JARI) ou da decisao da JARI (CETRAN) e prazo (PA-05).
4. **Preliminares / Nulidades** — CTB 280; Sum. 312 (validar).
5. **Merito** — inexistencia/atipicidade; combate a decisao recorrida.
6. **Pedidos** — provimento; **anulacao do auto/penalidade**; cancelamento da pontuacao; restituicao do valor se pago.
7. **Provas** — documentos, certidao de aferição, imagens.
8. Fecho, local/data, {{ADVOGADO_NOME}}, {{OAB_UF}} {{OAB_NUMERO}}.

## 6. INTEGRACAO

- `analise-vicios-auto-infracao` → teses; `analise-documental-transito` → AIT, NP, decisao da JARI.
- `jurisprudencia-transito` → validar Sum. 312/127 e CTB 285-290 (PA-01/PA-02).
- `calculos-transito` → prazos, pontuacao, valor da multa.
- `estilo-juridico-transito` → forma. `revisao-final-transito` → R1-R4.

## 7. CHECKLIST DE SAIDA

- [ ] Confirmada a fase: ha NP (penalidade aplicada), nao mera autuacao (PA-08)
- [ ] Instancia correta (JARI 1ª / CETRAN 2ª) e enderecamento certo (PA-08)
- [ ] Prazo de 30 dias conferido (PA-05)
- [ ] Efeito suspensivo so afirmado se validado (CTB 288 §2º)
- [ ] Deposito previo nao exigido (vedado — validar)
- [ ] Coerencia com a defesa anterior (PA-10); nada inventado (PA-01/PA-02)
- [ ] Selo P1 feito · R1-R4 pendente
