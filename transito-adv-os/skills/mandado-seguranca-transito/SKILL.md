---
name: mandado-seguranca-transito
description: >
  Skill Tier 2 — MANDADO DE SEGURANCA contra ato de autoridade de trânsito (Lei 12.016/2009). Ative para impetrar MS de trânsito, mandado de seguranca contra DETRAN, liminar para liberar CNH ou suspender penalidade administrativa.
metadata:
  version: "0.1.0"
  area: "Direito de Transito"
  tier: 2
---

# MANDADO DE SEGURANCA EM TRANSITO (Lei 12.016/2009)

> Tier 2. Via **celere** quando o direito e **liquido e certo** e a prova ja esta pronta. Sem dilacao probatoria — se depender de pericia/testemunha, usar `anulatoria-transito`. Persona: {{ADVOGADO_NOME}} ({{OAB_UF}} {{OAB_NUMERO}}), {{FIRM_NAME}}. Tom: {{TOM_VOZ_PERFIL}} / {{TOM_VOZ_INTENSIDADE}}.

---

## 1. REQUISITOS (Lei 12.016/2009)

- **Direito liquido e certo** — situacao demonstravel **de plano**, por documento, sem necessidade de instrucao.
- **Prova pre-constituida** — toda a documentacao acompanha a inicial (AIT, notificacoes, certidao da ausencia de aferição, decisao administrativa).
- **Ato de autoridade** — comissivo ou omissivo, ilegal ou abusivo, de agente publico no exercicio da funcao.

## 2. QUANDO O MS E PREFERIVEL A ANULATORIA

- Vicio **formal evidente e documental**: ausencia/intempestividade da **dupla notificacao** (Sum. 312 STJ — validar); **radar sem certidao de aferição valida**; ato praticado por autoridade incompetente; recusa ilegal de renovacao/liberacao da CNH.
- **Anulatoria** (skill propria) quando o caso exige **prova a produzir** (pericia no equipamento, testemunhas, contraditorio amplo) — MS nao comporta.

## 3. AUTORIDADE COATORA E PRAZO

- **Coator:** quem **pratica ou ordena** o ato — em regra o **diretor/superintendente do DETRAN** ou do orgao executivo de trânsito; identificar corretamente (erro pode gerar extincao). A pessoa juridica e notificada para ingressar (Lei 12.016, art. 7º).
- **Prazo decadencial: 120 dias** contados da ciencia do ato impugnado (Lei 12.016, art. 23 — PA-05; conferir a data, PA-03). Escoado, resta a anulatoria.

## 4. LIMINAR (Lei 12.016, art. 7º, III)

- **Fumus boni iuris**: ilegalidade evidente do ato (a nulidade documental).
- **Periculum in mora**: iminencia/efetivacao da suspensao/cassacao, bloqueio do licenciamento, recusa de CNH.
- **Pedido liminar**: liberar a CNH / o licenciamento, suspender a pontuacao, sustar o processo de suspensao ou cassacao ate o julgamento.

## 5. ESTRUTURA DA INICIAL DO MS

1. **Enderecamento** — Juizo competente (Vara da Fazenda Publica estadual; Justica Federal se a autoridade for federal — PA-08).
2. **Impetrante** (condutor/proprietario) e **autoridade coatora** (cargo + orgao); indicacao da pessoa juridica.
3. **Dos fatos** — ato coator, com a prova pre-constituida (PA-03).
4. **Do direito liquido e certo** — fundamentacao (CTB; Sum. 312 — validar; Lei 14.071 — norma vigente, PA-04).
5. **Da liminar** — fumus + periculum.
6. **Dos pedidos** — concessao da seguranca; anulacao do ato; liberacao da CNH/licenciamento; confirmacao da liminar.
7. **Documentos** — prova pre-constituida integral.
8. Fecho, {{ADVOGADO_NOME}}, {{OAB_UF}} {{OAB_NUMERO}}.

## 6. INTEGRACAO

- `analise-vicios-auto-infracao` → identificar o vicio **documental** que sustenta o DLC.
- `analise-documental-transito` → garantir prova pre-constituida completa.
- `jurisprudencia-transito` → validar Sum. 312 e cabimento do MS (PA-01).
- `anulatoria-transito` → via alternativa quando faltar prova pre-constituida.
- `calculos-transito` → prazo de 120 dias, pontuacao.
- `estilo-juridico-transito`; `revisao-final-transito` → R1-R4.

## 7. CHECKLIST DE SAIDA

- [ ] Direito liquido e certo com prova pre-constituida (sem dilacao)
- [ ] Autoridade coatora corretamente identificada (cargo/orgao); juizo certo (PA-08)
- [ ] Prazo decadencial de 120 dias conferido (PA-05)
- [ ] Liminar com fumus + periculum
- [ ] Vicio documental real e ancorado (PA-03); norma vigente na infracao (PA-04)
- [ ] Sumula/precedente validado (PA-01); fundamentacao real (PA-02)
- [ ] Selo P1 feito · R1-R4 pendente
