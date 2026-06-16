---
name: anulatoria-transito
description: >
  Skill Tier 2 — ACAO ANULATORIA judicial de multa/auto de infracao ou de penalidade de
  suspensao/cassacao da CNH (rito comum). Competencia: Vara da Fazenda Publica ou Juizado Especial da
  Fazenda Publica (Lei 12.153/2009), conforme o valor/complexidade. Cabimento independe de exaurir a via
  administrativa (inafastabilidade — CF 5º XXXV). Teses: as mesmas nulidades da via administrativa
  (CTB 280, dupla notificacao — Sum. 312, equipamento sem aferição) + ilegalidade do ato. Tutela de
  urgencia para suspender exigibilidade/pontos. Valor da causa. Nao confundir instancias (PA-08).
  Ative para anular multa na Justica, acao judicial contra multa, anular suspensao/cassacao, ou levar a
  questao de trânsito ao Judiciario por rito ordinario.
metadata:
  version: "0.1.0"
  area: "Direito de Transito"
  tier: 2
---

# ACAO ANULATORIA DE DEBITO / ATO DE TRANSITO (rito comum)

> Tier 2. Via **judicial** de cognicao ampla — admite dilacao probatoria (pericia, prova testemunhal), ao contrario do MS. Persona: {{ADVOGADO_NOME}} ({{OAB_UF}} {{OAB_NUMERO}}), {{FIRM_NAME}}. Tom: {{TOM_VOZ_PERFIL}} / {{TOM_VOZ_INTENSIDADE}}.

---

## 1. CABIMENTO E COMPETENCIA

- **Objeto:** anular o **AIT/multa**, ou a **penalidade** de suspensao/cassacao, ou debito de IPVA/licenciamento vinculado.
- **Inafastabilidade (CF 5º XXXV):** NAO e necessario exaurir a via administrativa para ajuizar. A pendencia de recurso administrativo nao impede a acao (verificar litispendencia/identidade de pedido).
- **Competencia:** acao contra o ente publico (Estado/DETRAN, ou Municipio/Uniao conforme o autuador) → **Vara da Fazenda Publica**; ate 60 salarios minimos → **Juizado Especial da Fazenda Publica** (Lei 12.153/2009; verificar materia/complexidade — pericia complexa pode afastar o JEFP).
- Polo passivo = a pessoa juridica de direito publico do orgao autuador (PA-08 — identificar corretamente).

## 2. TESES (ilegalidade + nulidades)

- Mesmas nulidades da defesa administrativa (alimentadas por `analise-vicios-auto-infracao`): vicio formal do AIT (CTB 280); **ausencia/intempestividade da dupla notificacao** (Sum. 312 STJ — validar); equipamento sem **aferição valida** (INMETRO); identificacao errada; incompetencia; sinalizacao irregular.
- **Ilegalidade do ato** — violacao do CTB, das Resolucoes CONTRAN ou da Lei 14.071 (PA-02; norma vigente na infracao — PA-04).
- Eventual **prescricao** da cobranca/execucao fiscal do debito.
- Coerencia da causa de pedir (PA-10).

## 3. TUTELA DE URGENCIA (CPC 300)

- **Fumus boni iuris**: a nulidade evidente (ex.: ausencia de dupla notificacao, radar sem aferição).
- **Periculum in mora**: inscricao em divida ativa, bloqueio do licenciamento, soma de pontos, iminencia de suspensao/cassacao.
- **Pedido**: suspender a exigibilidade da multa, sustar a pontuacao, liberar o licenciamento/CNH ate o julgamento.

## 4. VALOR DA CAUSA

- Em regra o valor da multa impugnada (ou proveito economico). Se o pedido inclui suspensao/cassacao, estimar o conteudo economico; em caso de IPVA/debitos, somar (verificar — PA-03, sem inventar cifras).

## 5. ESTRUTURA DA PETICAO INICIAL

1. **Enderecamento** — Juizo da Vara da Fazenda Publica / Juizado Especial da Fazenda (Lei 12.153).
2. **Qualificacao** — autor (condutor/proprietario) e reu (ente publico do orgao autuador).
3. **Dos fatos** — AIT, notificacoes, tramitacao administrativa (PA-03).
4. **Do direito** — nulidades + ilegalidade (CTB, Resolucoes, Sum. 312 — validar).
5. **Da tutela de urgencia** — fumus + periculum.
6. **Dos pedidos** — anulacao do auto/penalidade; cancelamento da pontuacao; restituicao do pago; confirmacao da tutela; custas e honorarios.
7. **Provas** — documental anexa; protesto por pericia (aferição) e demais.
8. **Valor da causa**. Fecho, {{ADVOGADO_NOME}}, {{OAB_UF}} {{OAB_NUMERO}}.

## 6. CHASSI DA PECA (POINTER)

> Modelo pronto (fonte unica): `templates/pecas/anulatoria-multa.md`. Reabrir e preencher a partir dele — nao redigir do zero. Manutencao da estrutura/teses se faz no chassi, nao aqui (ver `templates/pecas/_LEIA-ME.md`).

## 7. INTEGRACAO

- `analise-vicios-auto-infracao` → teses; `analise-documental-transito` → AIT, notificacoes, decisoes adm.
- `jurisprudencia-transito` → validar Sum. 312/127 e precedentes (PA-01).
- `calculos-transito` → valor da causa, pontuacao, prazos.
- `mandado-seguranca-transito` → comparar via (MS quando ha direito liquido e certo).
- `estilo-juridico-transito`; `revisao-final-transito` → R1-R4.

## 8. CHECKLIST DE SAIDA

- [ ] Competencia certa (Vara da Fazenda x JEFP — Lei 12.153) e polo passivo correto (PA-08)
- [ ] Inafastabilidade (CF 5º XXXV) — sem exigir exaurir a via administrativa
- [ ] Teses ancoradas no auto (PA-03); norma vigente na infracao (PA-04)
- [ ] Tutela de urgencia com fumus + periculum
- [ ] Valor da causa fundamentado (sem cifra inventada — PA-03)
- [ ] Sumulas/precedentes validados (PA-01); fundamentacao real (PA-02)
- [ ] Selo P1 feito · R1-R4 pendente
