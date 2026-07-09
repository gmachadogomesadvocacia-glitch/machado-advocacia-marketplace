---
name: cassacao-cnh
description: >
  Skill Tier 2 — processo de CASSACAO da CNH (CTB 263). Ative em cassacao da CNH, recolhimento da carteira, reabilitacao apos cassacao, dirigir com CNH suspensa, ou distincao entre suspensao e cassacao.
metadata:
  version: "0.1.0"
  area: "Direito de Transito"
  tier: 2
---

# CASSACAO DA CNH (CTB 263)

> Tier 2. Penalidade administrativa mais grave da CNH: **recolhimento** do documento e veto a nova habilitacao por 2 anos. Persona: {{ADVOGADO_NOME}} ({{OAB_UF}} {{OAB_NUMERO}}), {{FIRM_NAME}}. Tom: {{TOM_VOZ_PERFIL}} / {{TOM_VOZ_INTENSIDADE}}.

---

## 1. HIPOTESES (CTB 263 — validar a redacao vigente)

- **(I) Dirigir com a CNH SUSPENSA** (durante o periodo de suspensao do direito de dirigir).
- **(II) Reincidencia**, no prazo de 12 meses, em certas infracoes (CTB 263, II — validar o rol/redacao).
- **(III) Condenacao judicial por crime de trânsito** (CTB 263, III) — atencao: a esfera **criminal** corre em paralelo; defesa do crime em si → `criminal-adv-os` (PA-09; nao confundir instancias — PA-08).

## 2. DISTINCAO SUSPENSAO x CASSACAO (nao confundir)

| | Suspensao (CTB 261) | Cassacao (CTB 263) |
|---|---|---|
| Efeito | temporario; CNH mantida | recolhimento; CNH cancelada |
| Retorno | apos prazo + reciclagem | nova habilitacao so apos **2 anos** |
| Gatilho | pontos / autossuspensiva | dirigir suspenso / reincidencia / crime |

## 3. EFEITO E REABILITACAO

- Cassada a CNH, o condutor fica **2 anos** sem poder se habilitar (CTB 263 §1º — validar).
- **Reabilitacao:** decorrido o prazo, o interessado pode requerer **nova habilitacao**, submetendo-se de novo a **todos os exames** (medico, psicotecnico, teorico e pratico). Nao e "devolucao" da antiga CNH.

## 4. TESES DE DEFESA

- **Inexistencia do pressuposto** — a suspensao que fundamenta a cassacao (hip. I) e nula/nao estava em vigor (atacar o processo de suspensao — ver `suspensao-direito-dirigir`).
- **Nulidade dos autos/processos-base** (alimentado por `analise-vicios-auto-infracao`).
- **Atipicidade da reincidencia** — infracoes nao se enquadram no rol (hip. II) ou nao houve transito em julgado da suspensao anterior.
- **Cerceamento de defesa / vicio de instauracao e notificacao** (PA-05 — prazos).
- **Desproporcionalidade**; prescricao da pretensao punitiva administrativa.
- Norma vigente na infracao (PA-04).

## 5. ESTRUTURA DA DEFESA / RECURSO

1. **Enderecamento** — ao DETRAN (defesa no processo) ou ao CETRAN (recurso).
2. **Identificacao** — nº do processo de cassacao, condutor, CNH, processo de suspensao-base.
3. **Tempestividade** (PA-05).
4. **Preliminares / Nulidades** — vicios da instauracao e dos processos-base.
5. **Merito** — inexistencia do pressuposto; atipicidade; prescricao.
6. **Pedidos** — arquivamento; subsidiariamente, conversao em penalidade menos grave se cabivel.
7. **Provas** — processo de suspensao, autos, certidoes.
8. Fecho, {{ADVOGADO_NOME}}, {{OAB_UF}} {{OAB_NUMERO}}.

## 6. INTEGRACAO

- `suspensao-direito-dirigir` → atacar a suspensao que e pressuposto da cassacao.
- `analise-vicios-auto-infracao` → nulidade dos autos-base.
- `criminal-adv-os` → defesa do crime de trânsito (PA-09).
- `calculos-transito` → prazos. `jurisprudencia-transito` → validar CTB 263 (PA-01/PA-02).
- `estilo-juridico-transito`; `revisao-final-transito` → R1-R4.

## 7. CHECKLIST DE SAIDA

- [ ] Hipotese de cassacao identificada (I/II/III — CTB 263)
- [ ] Distincao suspensao x cassacao clara na peca (PA-08)
- [ ] Crime de trânsito roteado a criminal-adv-os (PA-09)
- [ ] Pressuposto (suspensao-base) verificado e, se viciado, atacado
- [ ] Prazo de reabilitacao (2 anos) e nova habilitacao corretamente expostos
- [ ] Prazos preclusivos (PA-05); norma vigente na infracao (PA-04)
- [ ] Nada inventado (PA-01/PA-02); fatos ancorados (PA-03)
- [ ] Selo P1 feito · R1-R4 pendente
