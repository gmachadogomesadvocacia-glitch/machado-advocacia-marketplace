---
name: cumprimento-sentenca-consumidor
description: >
  CUMPRIMENTO DE SENTENCA CONSUMIDOR — Skill Tier 2 de execucao e side-aware. Conduz a fase de
  cumprimento: pagamento voluntario em 15 dias sob pena de multa de 10% + honorarios de 10% (CPC art.
  523); liquidacao quando o titulo e iliquido; execucao de astreintes pelo descumprimento de obrigacao
  de fazer (ex.: nao baixou a negativacao, nao religou o servico); penhora (art. 835); e impugnacao ao
  cumprimento (art. 525) quando o cliente e o executado/fornecedor. Side-aware: exequente consumidor x
  executado fornecedor, e vice-versa. Acione quando o usuario pede cumprimento de sentenca, executar a
  sentenca, cobrar a condenacao, astreintes, multa diaria, penhora, impugnacao ao cumprimento. Exige
  Selo P1 e o titulo conferido (PA-08 para prazos).
metadata:
  version: "0.1.0"
  area: "Direito do Consumidor e Bancario"
  tier: 2
---

# CUMPRIMENTO DE SENTENCA CONSUMIDOR

> Skill **Tier 2** de execucao, **side-aware**. Conduz a fase de cumprimento conforme o polo do cliente. So roda apos o transito/titulo exequivel, o Selo P1 e o CASO.md atualizado.

---

## 0. PRE-REQUISITOS

- **Declarar o polo do cliente nesta fase** (PA-05): exequente (credor) ou executado (devedor). No consumo, ambos os papeis ocorrem — consumidor exequente x fornecedor executado, e o inverso (ex.: condenacao do consumidor em verba sucumbencial; cobranca pelo fornecedor).
- **Selo de Validacao Legal Previa EMITIDO** (P1). Sem ele, nao redigir.
- Titulo executivo (sentenca/acordao transitado ou titulo provisorio) e a planilha de calculo. Falta → `[INFORMAR]` (PA-15). Calculo via `calculos-consumidor` — nada de estimativa silenciosa (PA-20).

## 1. PAGAMENTO VOLUNTARIO E MULTA (CPC art. 523)

Obrigacao de pagar quantia certa: requerer a intimacao do devedor para pagar em **15 dias**. Nao pago, incide **multa de 10% + honorarios de 10%** sobre o debito (art. 523 §1). Apresentar a **planilha atualizada** (principal + juros + correcao). **Conferir os prazos (PA-08)** e o termo inicial da intimacao.

## 2. LIQUIDACAO (titulo iliquido)

Se a sentenca nao fixou o valor, liquidar antes (CPC art. 509): por **calculo** (basta a memoria, art. 509 §2), por **arbitramento** (pericia) ou pelo **procedimento comum** (fatos novos). Comum no dano moral arbitrado em parametros ou na repeticao de indebito a apurar.

## 3. EXECUCAO DE ASTREINTES (obrigacao de fazer/nao fazer)

Quando a condenacao impos obrigacao de fazer e o fornecedor descumpriu — **nao baixou a negativacao**, **nao religou o servico essencial**, nao entregou o produto, nao restabeleceu a cobertura — executar a **multa diaria** (CPC art. 537):

- Demonstrar a data da intimacao para cumprir e a **persistencia do descumprimento**.
- Calcular as astreintes (valor diario x periodo) — `calculos-consumidor`.
- Atentar a possibilidade de **revisao do valor** pelo juizo (art. 537 §1) se excessivo/insuficiente; antecipar esse ataque.
- Requerer o cumprimento da obrigacao + a multa acumulada; cumular com perdas e danos se for o caso.

## 4. PENHORA E EXPROPRIACAO (CPC art. 835)

Nao havendo pagamento: requerer penhora pela ordem do art. 835 (dinheiro em primeiro — **SISBAJUD**; depois veiculos — RENAJUD, imoveis, etc.). Contra fornecedor, o bloqueio de ativos costuma ser eficaz. Observar impenhorabilidades (art. 833) quando o **executado e o consumidor** (salario, bem de familia).

## 5. IMPUGNACAO AO CUMPRIMENTO (art. 525) — cliente executado/fornecedor

Quando o cliente e o **executado**, defender por impugnacao no prazo de **15 dias** apos o prazo do art. 523 (PA-08), nas materias do art. 525 §1: falta/nulidade de citacao no processo de conhecimento (revelia), ilegitimidade, inexequibilidade do titulo, **excesso de execucao** (apontar o valor que entende correto, sob pena de rejeicao — art. 525 §4 e §5), penhora incorreta, cumprimento/compensacao. Atacar a planilha do exequente quando inflada. Pedir efeito suspensivo so com garantia + risco de dano grave (art. 525 §6).

## 6. SIDE-AWARENESS — RESUMO

| Cliente | Atua | Foco |
|---------|------|------|
| **Consumidor exequente** | cumprimento/execucao | receber a condenacao; cobrar astreintes; penhora rapida (SISBAJUD) |
| **Fornecedor executado** | impugnacao (art. 525) | excesso de execucao; revisao de astreintes excessivas; garantir o juizo |
| **Fornecedor exequente** | cumprimento | cobrar sucumbencia/condenacao do consumidor |
| **Consumidor executado** | impugnacao | impenhorabilidades (art. 833); excesso; gratuidade |

## 7. CHECKLIST ANTES DE ENTREGAR

- [ ] Polo nesta fase declarado e coerente (PA-05) · Selo P1 citado
- [ ] Titulo exequivel e liquido (ou liquidacao iniciada) · planilha com calculo real (PA-20)
- [ ] **Prazos conferidos (PA-08)** — 15 dias do art. 523 e da impugnacao (art. 525)
- [ ] Astreintes com data de descumprimento comprovada · risco de revisao antecipado
- [ ] Impenhorabilidades observadas quando o executado e consumidor · jurisprudencia validada (PA-01) `[VERIFICAR]` via `jurisprudencia-consumidor`
- [ ] Submeter a `revisao-final-consumidor` (R1-R4) antes da entrega (PA-22)

## 8. ENCERRAMENTO

Entrega a peca da fase de cumprimento — requerimento do exequente ou impugnacao do executado — com calculo real, prazos conferidos e astreintes/penhora tratadas, calibrada ao polo do cliente, pronta para a Suprema Corte R1-R4.
