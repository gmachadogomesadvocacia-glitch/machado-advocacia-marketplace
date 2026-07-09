---
name: defesa-autuacao
description: >
  Skill Tier 2 — DEFESA PREVIA / defesa da autuacao (CTB 281-282). Ative ao receber a Notificacao de Autuacao, redigir defesa previa, defesa da autuacao, ou impugnar o auto antes de virar multa.
metadata:
  version: "0.1.0"
  area: "Direito de Transito"
  tier: 2
---

# DEFESA PREVIA / DEFESA DA AUTUACAO (CTB 281-282)

> Tier 2. **Primeiro momento de defesa.** Apresentada apos a **Notificacao de Autuacao (NA)** e antes da aplicacao da penalidade. Alvo: **arquivar o auto** (CTB 281, par. unico) para que nunca vire multa. Persona: {{ADVOGADO_NOME}} ({{OAB_UF}} {{OAB_NUMERO}}), {{FIRM_NAME}}. Tom: {{TOM_VOZ_PERFIL}} / {{TOM_VOZ_INTENSIDADE}}.

---

## 1. POSICAO NO FLUXO (NAO CONFUNDIR — PA-08)

```
INFRACAO → AIT lavrado → NOTIFICACAO DE AUTUACAO (NA) → [DEFESA PREVIA — aqui]
        → julgamento → NOTIFICACAO DE PENALIDADE (NP) → [RECURSO JARI → CETRAN]
```

- **Defesa previa = ANTES da penalidade.** Dirigida ao **orgao/entidade autuador** (quem lavrou o AIT), nao a JARI.
- Apos a NP, o caminho e **recurso** (skill `recursos-administrativos`), nao defesa previa.
- Confundir as fases = vicio de instancia (PA-08). Confira a peca (NA x NP) antes de redigir.

## 2. PRAZO (PA-05 — PRECLUSIVO)

- Em regra **30 dias** contados da NA (CTB 281, par. unico; data-limite indicada na propria notificacao — **validar** no documento).
- Perdido o prazo, ocorre **preclusao**: a defesa previa nao mais cabe; resta aguardar a NP e recorrer. NUNCA afirmar tempestividade sem conferir a data (PA-03).
- Norma vigente na data da infracao (tempus regit actum — PA-04; atencao a Lei 14.071/2020).

## 3. FUNDAMENTOS (alimentados por analise-vicios-auto-infracao)

**A. Nulidades formais do AIT (CTB 280)** — auto deve conter tipificacao, local/data/hora, caracteristicas do veiculo, orgao/agente autuador, e registro do equipamento quando exigido. Falta de dado essencial que impeca a defesa → nulidade/arquivamento.

**B. Vicio da Notificacao de Autuacao** — NA fora do prazo legal de expedicao (CTB 281, par. unico — em regra 30 dias da infracao; ultrapassado → **arquivamento**). Endereco incorreto, ausencia de notificacao valida (Sum. 312 STJ — **validar**).

**C. Identificacao** — erro de placa, veiculo diverso, condutor nao identificado quando a infracao e de responsabilidade do condutor.

**D. Equipamento (radar)** — falta de **certidao de aferição valida (INMETRO/IPEM)**, equipamento nao homologado, margem de tolerancia (ver `defesa-radar-equipamentos`).

**E. Merito — inexistencia da infracao** — fato nao ocorreu, ausencia de tipicidade, prova insuficiente. Ancorar SEMPRE no documento (PA-03).

## 4. ESTRUTURA DA DEFESA PREVIA

1. **Enderecamento** — ao orgao/entidade autuador (o que consta no AIT/NA).
2. **Identificacao do auto e do autuado** — nº do AIT, placa, data/local, infracao tipificada; qualificacao do proprietario/condutor.
3. **Tempestividade** — data da NA e prazo (PA-05).
4. **Preliminares / Nulidades** — vicios formais e de notificacao (CTB 280; Sum. 312 — validar).
5. **Merito** — inexistencia da infracao.
6. **Pedidos** — acolhimento e **ARQUIVAMENTO do auto** (CTB 281, par. unico); subsidiariamente, requerer a certidao de aferição/imagens.
7. **Provas** — documentos anexos, requerimento de aferição e de imagens.
8. Fecho, local/data, {{ADVOGADO_NOME}}, {{OAB_UF}} {{OAB_NUMERO}}.

## 5. CHASSI DA PECA (POINTER)

> Modelo pronto (fonte unica): `templates/pecas/defesa-previa-autuacao.md`. Reabrir e preencher a partir dele — nao redigir do zero. Manutencao da estrutura/teses se faz no chassi, nao aqui (ver `templates/pecas/_LEIA-ME.md`).

## 6. INTEGRACAO

- `analise-vicios-auto-infracao` → catalogo de teses.
- `analise-documental-transito` → conferir AIT, NA, CRLV, CNH.
- `jurisprudencia-transito` → validar Sum. 312/127 e precedentes (PA-01).
- `calculos-transito` → prazos e pontuacao.
- `estilo-juridico-transito` → tom e forma.
- `revisao-final-transito` → R1-R4 antes de entregar.

## 7. CHECKLIST DE SAIDA

- [ ] Confirmado que e fase de AUTUACAO (NA), nao penalidade (PA-08)
- [ ] Prazo de 30 dias conferido na NA (PA-05)
- [ ] Norma vigente na data da infracao (PA-04; Lei 14.071)
- [ ] Nulidades e merito separados; teses ancoradas no auto (PA-03)
- [ ] Nenhuma sumula/norma inventada (PA-01/PA-02); marcadas "validar"
- [ ] Pedido de arquivamento expresso
- [ ] Selo P1 feito · R1-R4 pendente
