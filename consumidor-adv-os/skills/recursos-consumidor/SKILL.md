---
name: recursos-consumidor
description: >
  RECURSOS CONSUMIDOR — Skill Tier 2 recursal e side-aware. Acione quando o usuario pede recurso, recorrer, apelacao, recurso inominado, agravo, REsp em materia de consumo. Exige Selo P1 e o prazo conferido (PA-08).
metadata:
  version: "0.1.0"
  area: "Direito do Consumidor e Bancario"
  tier: 2
---

# RECURSOS CONSUMIDOR

> Skill **Tier 2** recursal, **side-aware**. Roteia para o recurso correto conforme o rito e a parte. So roda apos a triagem, o Selo P1, e a leitura integral da decisao recorrida.

---

## 0. PRE-REQUISITOS

- **Declarar a parte que recorre** (PA-05): consumidor ou fornecedor. Toda razao e calibrada ao polo do recorrente; nada pode ir contra o cliente.
- **Selo de Validacao Legal Previa EMITIDO** (P1). Sem ele, nao redigir.
- Decisao recorrida (sentenca, acordao ou interlocutoria) lida na integra. Falta → `[INFORMAR]` (PA-15).
- **Rito definido na triagem** (Protocolo P5): JEC x vara comum — determina qual recurso cabe.

## 1. ROTEAMENTO — QUAL RECURSO CABE

| Decisao recorrida | Rito | Recurso | Base | Prazo `[VERIFICAR]` (PA-08) |
|-------------------|------|---------|------|------------------------------|
| Sentenca | Vara comum | **Apelacao** | CPC art. 1.009 | 15 dias uteis |
| Sentenca | JEC | **Recurso inominado** | Lei 9.099 art. 41 | 10 dias (corridos) |
| Interlocutoria / tutela | Vara comum | **Agravo de instrumento** | CPC art. 1.015 (rol) | 15 dias uteis |
| Acordao (ofensa a lei federal) | — | **Recurso especial** ao STJ | CF art. 105, III + CPC art. 1.029 | 15 dias uteis |

**Conferir o prazo correto (PA-08)** caso a caso — contagem em dias uteis (CPC art. 219) vs. corridos no JEC; termo inicial pela intimacao. Embargos de declaracao **interrompem** o prazo (ver `embargos-declaracao-consumidor`).

## 2. APELACAO (vara comum — CPC art. 1.009)

Cabivel da sentenca. Razoes: error in judicando / in procedendo, com prequestionamento. **Efeito** suspensivo como regra (art. 1.012); excecoes no §1. Atentar ao art. 1.013 (efeito devolutivo em profundidade) e ao art. 1.014 (questoes de fato novas). Preparo obrigatorio salvo gratuidade.

## 3. RECURSO INOMINADO (JEC — Lei 9.099 art. 41)

Cabivel da sentenca no Juizado Especial Civel, julgado pela Turma Recursal. Necessita de **advogado** (art. 41 §2). **Efeito so devolutivo** como regra (art. 43) — efeito suspensivo so com risco de dano. **Preparo:** 10 dias para recolher (art. 42 §1), sob pena de desercao; gratuidade afasta. Atencao a competencia/rito do JEC (PA-19).

## 4. AGRAVO DE INSTRUMENTO (CPC art. 1.015)

Cabivel das interlocutorias do rol do art. 1.015 — em especial **tutela provisoria** (concessao/negacao de retirada de negativacao, religacao de servico, suspensao de cobranca, busca e apreensao). Pode-se pedir **efeito suspensivo** ou a **antecipacao da tutela recursal** (art. 1.019, I). Instruir com as pecas obrigatorias (art. 1.017). Fora do rol → diferir para a apelacao.

## 5. RECURSO ESPECIAL AO STJ (CF art. 105, III)

Cabivel de acordao que contraria/nega vigencia a lei federal (CDC, CC, CPC) ou diverge de outro tribunal. Requisitos: esgotamento das instancias, **prequestionamento** (questao federal debatida no acordao — usar embargos de declaracao se omisso) e demonstracao do cabimento. **Sumula 7 STJ** `[VERIFICAR]` — vedado o reexame de prova; a tese deve ser **de direito**, nunca pedido de reanalise factica. Atencao a repercussao das teses repetitivas e a admissibilidade.

## 6. EFEITOS, PREPARO E GRATUIDADE

- **Efeitos:** identificar suspensivo x devolutivo conforme o recurso; pedir suspensivo/antecipacao quando houver risco de dano.
- **Preparo/custas:** recolher no prazo proprio; comprovar nos autos.
- **Gratuidade (art. 98 CPC / Lei 1.060):** se deferida, dispensa o preparo — invocar quando o consumidor for hipossuficiente.

## 7. CHECKLIST ANTES DE ENTREGAR

- [ ] Parte recorrente declarada e coerente (PA-05) · Selo P1 citado
- [ ] Recurso correto para o rito · **prazo conferido (PA-08)** com contagem (uteis x corridos) e termo inicial
- [ ] Prequestionamento presente quando exigido · Sumula 7 respeitada no REsp `[VERIFICAR]`
- [ ] Efeitos requeridos · preparo recolhido OU gratuidade invocada
- [ ] Jurisprudencia validada (PA-01) — Sumula/Tema `[VERIFICAR]` via `jurisprudencia-consumidor`
- [ ] Submeter a `revisao-final-consumidor` (R1-R4) antes da entrega (PA-22)

## 8. ENCERRAMENTO

Entrega o recurso cabivel ao rito e a parte, com prazo conferido, efeitos e preparo tratados — calibrado ao polo do recorrente, pronto para a Suprema Corte R1-R4.
