---
name: suspensao-direito-dirigir
description: >
  Skill Tier 2 — processo administrativo de SUSPENSAO DO DIREITO DE DIRIGIR (CTB 261; Lei 14.071/2020). Ative em processo de suspensao do direito de dirigir, atingimento de pontos na CNH, infracao autossuspensiva ou defesa de suspensao da carteira.
metadata:
  version: "0.1.0"
  area: "Direito de Transito"
  tier: 2
---

# SUSPENSAO DO DIREITO DE DIRIGIR (CTB 261; Lei 14.071/2020)

> Tier 2. Processo administrativo **autonomo** (distinto da multa que o originou). Penalidade: suspensao do direito de dirigir + curso de reciclagem. Persona: {{ADVOGADO_NOME}} ({{OAB_UF}} {{OAB_NUMERO}}), {{FIRM_NAME}}. Tom: {{TOM_VOZ_PERFIL}} / {{TOM_VOZ_INTENSIDADE}}.

---

## 1. AS DUAS HIPOTESES (PA-04 — CONFERIR A LEI VIGENTE NA INFRACAO)

**A. Atingimento de pontos (sistema Lei 14.071/2020):** limite variavel conforme o nº de infracoes **gravissimas** nos ultimos 12 meses (validar a regra vigente):
- **40 pontos** — nenhuma gravissima;
- **30 pontos** — uma gravissima;
- **20 pontos** — duas ou mais gravissimas.
- ATENCAO PA-04: a Lei 14.071 alterou o sistema anterior (20 pontos fixos). Aplicar a regra **vigente na data dos fatos** (tempus regit actum).

**B. Infracao autossuspensiva (suspensao independe de pontos):**
- art. 165 (dirigir sob influencia de alcool/substancia — **infracao** administrativa);
- art. 173 (disputa/racha);
- art. 218 / excesso de velocidade **superior a 50%** do limite;
- demais hipoteses do CTB com previsao expressa de suspensao (validar cada artigo).
- Aqui a suspensao decorre da propria infracao — nao se confunde com crime de trânsito (se houver embriaguez **criminal**, art. 306 CTB, ou homicidio/lesao culposa, art. 302/303 → encaminhar a `criminal-adv-os` — PA-09).

## 2. RITO

1. **Instauracao** do processo pelo orgao executivo (DETRAN), com notificacao do condutor.
2. **Defesa** no prazo assinalado (em regra 30 dias — PA-05, preclusivo).
3. **Decisao** (periodo de suspensao).
4. **Recurso ao CETRAN** (prazo 30 dias — PA-05).
5. Cumprida a suspensao, **curso de reciclagem** como condicao de devolucao da CNH.

## 3. TESES DE DEFESA

- **Nulidade das multas que somaram pontos** — se a pontuacao decorre de autos viciados/anulaveis, ataca-se a base do processo (alimentado por `analise-vicios-auto-infracao`). Multas em recurso/sub judice nao devem compor a soma (verificar).
- **Recontagem da pontuacao** — exclusao de infracoes prescritas, anuladas ou de outro condutor (indicacao — ver `indicacao-condutor`).
- **Prescricao** da pretensao punitiva administrativa (verificar prazos — PA-05).
- **Desproporcionalidade** do periodo fixado (CTB 261 fixa limites — validar minimo/maximo).
- **Cerceamento de defesa** / vicio na instauracao ou notificacao.
- Norma aplicavel = vigente na infracao (PA-04).

## 4. ESTRUTURA DA DEFESA / RECURSO

1. **Enderecamento** — ao DETRAN (defesa) ou ao CETRAN (recurso).
2. **Identificacao** — nº do processo de suspensao, condutor, CNH, autos que somaram pontos.
3. **Tempestividade** (PA-05).
4. **Preliminares / Nulidades** — vicios da instauracao; nulidade dos autos-base.
5. **Merito** — recontagem de pontos, prescricao, desproporcionalidade.
6. **Pedidos** — arquivamento do processo de suspensao; subsidiariamente, reducao do periodo; exclusao dos pontos viciados.
7. **Provas** — autos das multas, certidoes de aferição, comprovantes de indicacao de condutor.
8. Fecho, {{ADVOGADO_NOME}}, {{OAB_UF}} {{OAB_NUMERO}}.

## 5. INTEGRACAO

- `analise-vicios-auto-infracao` → nulidade dos autos-base.
- `indicacao-condutor` → excluir pontos de infracao de outro condutor (PA-06: indicacao real).
- `calculos-transito` → soma e recontagem de pontos, prazos, periodo de suspensao.
- `jurisprudencia-transito` → validar CTB 261 e Lei 14.071 (PA-01/PA-02).
- `cassacao-cnh` → se houver risco de evoluir para cassacao (dirigir suspenso).
- `estilo-juridico-transito`; `revisao-final-transito` → R1-R4.

## 6. CHECKLIST DE SAIDA

- [ ] Hipotese identificada (pontos x autossuspensiva)
- [ ] Limite de pontos pela regra VIGENTE na infracao (PA-04; Lei 14.071)
- [ ] Crime de trânsito (306/302/303) roteado a criminal-adv-os (PA-09)
- [ ] Pontuacao recontada; autos viciados/sub judice/prescritos excluidos
- [ ] Prazos preclusivos conferidos (PA-05)
- [ ] Nada inventado (PA-01/PA-02); fatos ancorados (PA-03)
- [ ] Selo P1 feito · R1-R4 pendente
