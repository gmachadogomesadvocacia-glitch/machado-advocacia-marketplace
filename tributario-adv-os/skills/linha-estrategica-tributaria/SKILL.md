---
name: linha-estrategica-tributaria
description: >
  Linha estrategica tributaria Tier 1. Consolida a trilateral e a jurisprudencia e define a VIA (administrativa x judicial) e a sequencia. Criterios: suspensao da exigibilidade (CTN art. 151. Ative apos a trilateral, quando o usuario pedir a estrategia, a melhor via ou a linha de defesa/acao.
metadata:
  version: "0.1.0"
  area: "Direito Tributario"
  tier: 1
---

# LINHA ESTRATEGICA TRIBUTARIA

> Tier 1. Recebe o quadro de forcas da `analise-trilateral-tributaria` e decide **via + sequencia**. Decisao **documentada** no CASO.md. Polo padrao: contribuinte (PA-10).

---

## 1. VIA: ADMINISTRATIVA x JUDICIAL

**Administrativa** (impugnacao / recurso DRJ-CARF)
- **Suspende a exigibilidade SEM garantia** (CTN art. 151, III) — vantagem central.
- Sem custas nem sucumbencia; pode rever fato e prova; CARF como instancia tecnica.
- Mais lenta; nao impede inscricao se vencida.

**Judicial**
- **Mandado de seguranca** — direito liquido e certo, prova documental, sem dilacao; liminar suspende (CTN 151, IV); sem sucumbencia.
- **Anulatoria** — desconstituir o lancamento/CDA; admite prova ampla; deposito (CTN 151, II; Sum. 112) suspende.
- **Embargos / excecao** (ja em execucao) → `defesa-execucao-fiscal`.
- **Declaratoria / repeticao / compensacao** → indebito (PA-09).

## 2. SUSPENSAO DA EXIGIBILIDADE (CTN art. 151)

| Inciso | Hipotese | Garantia? |
|--------|----------|-----------|
| II | Deposito integral em dinheiro | sim (dinheiro — Sum. 112) |
| III | Impugnacao/recurso administrativo | **nao** |
| IV/V | Liminar (MS) / tutela | nao |
| VI | Parcelamento | adesao |

> Suspensao habilita **CND/CPEN** (certidao positiva com efeito de negativa — CTN 206), essencial para o contribuinte operar.

## 3. CRITERIOS DE DECISAO

1. **Prazo em curso** — citacao em execucao nao espera; priorizar garantia/embargos.
2. **Custo** — administrativo evita sucumbencia e garantia; judicial pesa custas e honorarios.
3. **Garantia** — ha bem para penhorar/seguro? Deposito viavel?
4. **Tempo x chance** — tese de plano (nulidade, prescricao) → MS/excecao; tese de fato → administrativo/anulatoria.
5. **Certidao** — necessidade urgente de CND favorece via que suspenda sem garantia.
6. **Risco de redirecionamento** (PA-08) — proteger o socio; afastar dissolucao irregular.

## 4. QUANDO ADMINISTRATIVO ANTES DO JUDICIAL

- Vale impugnar administrativamente quando: ha materia de fato/prova, suspende sem garantia (CTN 151, III), ainda nao houve inscricao, e ha chance real no CARF.
- Ir **direto ao judicial** (MS/anulatoria) quando: tese de direito de plano, urgencia de liminar/CND, ou a esfera administrativa ja se esgotou.

## 5. ELISAO x EVASAO (PA-06)

So planejar **elisao licita** (atos validos, anteriores ao fato gerador). Recusar evasao/sonegacao/fraude. Sinalizar interface penal (Lei 8.137) quando o caso tangenciar.

## 6. SAIDA

```
VIA ESCOLHIDA: ...
SEQUENCIA: ...
FUNDAMENTO DA SUSPENSAO: CTN 151, ...
EFEITO NA CERTIDAO (CND/CPEN): ...
PORTA DE PRODUCAO: <skill>
DECISAO REGISTRADA EM CASO.md: sim
```

Apos a decisao → porta de producao (ex.: `defesa-execucao-fiscal`, MS, anulatoria) → `estilo-juridico-tributario` → `revisao-final-tributaria` (R1-R4).
