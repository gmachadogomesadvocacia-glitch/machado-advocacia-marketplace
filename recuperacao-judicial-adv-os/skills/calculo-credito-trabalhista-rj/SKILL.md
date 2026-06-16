---
name: calculo-credito-trabalhista-rj
description: >
  CALCULO-CREDITO-TRABALHISTA-RJ — Tier 2 (Produção). Calcula o crédito
  trabalhista a habilitar em recuperação judicial: atualiza o valor
  histórico até a data do pedido de RJ (art. 9º, II — congelamento de
  juros e correção), aplica o teto de 150 salários-mínimos (art. 83, I)
  com excedente migrando para Classe III, segrega verbas com tratamento
  próprio (FGTS — Tema 1.051 STJ; multas 477 e 467 CLT; honorários
  sucumbenciais; INSS empregado; contribuição sindical) e produz planilha
  discriminada verba × classe × valor. Integra-se ao plug-in
  `calculos-pjecalc` quando instalado. Acionada por `credor-trabalhista-rj`.
---

# CALCULO-CREDITO-TRABALHISTA-RJ

> Tier 2 | Cálculo de crédito trabalhista em RJ | arts. 9º II, 83 I, 84 LFRJ
> Tema 1.051 STJ | Tema 637 STJ | CLT arts. 467, 477

---

## 0. ESCOPO

Esta skill calcula. Não decide via, não redige peça. Recebe os dados
brutos, devolve planilha pronta para anexar à habilitação/impugnação/
retardatária. Outputs: planilha + memorial de cálculo.

---

## 1. ENTRADAS

```
1. valor_historico_total       (R$)
2. data_base_historica         (data)
3. componentes_do_credito      (lista — ver §3)
4. data_pedido_rj              (data — marco do corte)
5. fato_gerador_inicio         (data)
6. fato_gerador_fim            (data)
7. salario_minimo_vigente      (na data do pedido de RJ)
8. há liquidação JT concluída? (sim/não + valor liquidado)
9. há acordo homologado JT?    (sim/não + valor)
10. integração calculos-pjecalc disponível? (sim/não)
```

---

## 2. PASSOS DO CÁLCULO

### Passo 1 — Atualização monetária + juros até a DATA DO PEDIDO

```
Regra do art. 9º, II LFRJ:
  "valor atualizado até a data do pedido de recuperação judicial"

Operação:
  V_atualizado = V_historico × fator_correção(data_base → data_pedido)
                          + juros(data_base → data_pedido)

Indexador:
  • Pré-vigência do tema 1.191 STF (ADC 58/59) → TR + juros legais
  • Pós tema 1.191 STF                         → IPCA-E (fase pré-judicial)
                                                  + SELIC (fase judicial)
  ⚠️ Confirmar com `jurisprudencia-rj` o índice aplicável ao período.

Se calculos-pjecalc disponível → delegar a esse plug-in.
Se NÃO → memorial detalhado manual.

Resultado: V_total_atualizado_pedido (R$)
```

⚠️ **REGRA ABSOLUTA**: nunca atualizar além da data do pedido.
Acréscimos pós-pedido são suspensos pelo art. 9º, II (PA-CTH-03).

### Passo 2 — Aplicação do teto Classe I (150 SM)

```
TETO_CLASSE_I = 150 × salario_minimo_vigente_data_pedido

SE V_total_atualizado_pedido ≤ TETO_CLASSE_I:
    Classe_I  = V_total_atualizado_pedido
    Classe_III = 0

SE V_total_atualizado_pedido > TETO_CLASSE_I:
    Classe_I  = TETO_CLASSE_I
    Classe_III = V_total_atualizado_pedido − TETO_CLASSE_I
```

Fundamento: art. 83, I + art. 41, I + PA-08.

### Passo 3 — Segregação de verbas com tratamento próprio

```
[a] FGTS
    Natureza: depósito vinculado em favor do empregado, gestão da CEF.
    Sujeição à RJ: Tema 1.051 STJ — sujeita, com nuances.
    ⚠️ Confirmar jurisprudência atual via `jurisprudencia-rj`.
    Classe usual: I (com excedente em III, se aplicável).

[b] Multa do art. 477 CLT
    Natureza: trabalhista. Classe I (com excedente em III).

[c] Multa do art. 467 CLT
    Cabimento em RJ é controverso — a recuperanda não comparece à
    audiência da reclamatória nos moldes do dispositivo.
    Quando reconhecida, segue Classe I.

[d] Honorários sucumbenciais trabalhistas
    Natureza alimentar, equiparados a crédito trabalhista (Tema 637 STJ, REsp 1.152.218/RS).
    Classe: posição majoritária pelo enquadramento na Classe I; há
    decisões alocando em Classe III. CONFIRMAR via `jurisprudencia-rj`.

[e] INSS empregado descontado e não recolhido
    Crédito da União, não do credor pessoa física.
    NÃO HABILITA pelo credor. Apenas referenciar.

[f] Contribuição sindical
    Crédito do sindicato. NÃO HABILITA pelo credor pessoa física.

[g] Indenização por dano moral trabalhista
    Trabalhista por origem. Classe I (com teto). Confirmar JP.

[h] Indenização por acidente de trabalho
    Trabalhista. Pode ter componente previdenciário. Segregar.
```

### Passo 4 — Cindir por fato gerador (se aplicável)

```
SE fato_gerador a cavaleiro do pedido de RJ:
    proporção = dias_anteriores / (dias_anteriores + dias_posteriores)
    parcela_concursal  = V_total × proporção
    parcela_extraconc  = V_total × (1 − proporção)

A parcela_concursal entra na aplicação do teto de 150 SM e segue
a árvore de classe. A parcela_extraconcursal NÃO HABILITA — segue
o regime do art. 84 (se convolar em falência) ou pagamento no curso
normal da RJ.
```

### Passo 5 — Planilha discriminada

```
| Verba              | Histórico | Atualizado | Concursal | Extraconc | Classe |
|--------------------|-----------|------------|-----------|-----------|--------|
| Saldo de salário   | ...       | ...        | ...       | ...       | I      |
| Aviso prévio       | ...       | ...        | ...       | ...       | I      |
| 13º proporcional   | ...       | ...        | ...       | ...       | I      |
| Férias prop. + 1/3 | ...       | ...        | ...       | ...       | I      |
| Multa 40% FGTS     | ...       | ...        | ...       | ...       | I/III* |
| FGTS depósitos     | ...       | ...        | ...       | ...       | I/III* |
| Horas extras       | ...       | ...        | ...       | ...       | I/III* |
| Adic. insalub./per | ...       | ...        | ...       | ...       | I/III* |
| Multa 477          | ...       | ...        | ...       | ...       | I      |
| Multa 467          | ...       | ...        | ...       | ...       | I      |
| Honor. sucumb.     | ...       | ...        | ...       | ...       | I*     |
| Dano moral         | ...       | ...        | ...       | ...       | I      |
| TOTAL              | ...       | ...        | ...       | ...       | —      |

Linha-resumo:
| TOTAL CLASSE I (até 150 SM)             | R$ ...        |
| TOTAL CLASSE III (excedente)            | R$ ...        |
| TOTAL EXTRACONCURSAL (pós-pedido)       | R$ ...        |
| TOTAL GERAL                             | R$ ...        |

* sujeito a verificação jurisprudencial via `jurisprudencia-rj`.
```

### Passo 6 — Memorial de cálculo

Para cada verba, registrar:

```
Verba: [...]
Período: [início → fim]
Base de cálculo: [...]
Fórmula: [...]
Índice de correção: [...] (período × índice)
Juros: [...] (taxa × período)
Histórico: R$ [...]   Atualizado: R$ [...]   Δ = R$ [...]
```

---

## 3. COMPONENTES TÍPICOS DO CRÉDITO

Para cada verba presente, sinalizar no input:

- saldo de salário
- aviso prévio (indenizado ou trabalhado)
- 13º proporcional / integral
- férias proporcionais / vencidas + 1/3
- multa 40% FGTS
- FGTS depósitos não recolhidos
- horas extras + reflexos
- adicional de insalubridade / periculosidade / noturno
- intervalos suprimidos (art. 71 §4º CLT)
- domingos e feriados
- multa do art. 477 CLT
- multa do art. 467 CLT
- equiparação salarial / diferenças
- danos morais / materiais
- danos por acidente / doença ocupacional
- estabilidades (gestante, CIPA, acidentado)
- PLR
- comissões
- honorários sucumbenciais trabalhistas
- INSS empregado (informativo, não habilita)
- IR retido (informativo)
- contribuição sindical (não habilita pelo credor)

---

## 4. INTEGRAÇÃO COM `calculos-pjecalc`

Se o plug-in `calculos-pjecalc` estiver instalado (verificar via
`installed_plugins.json`):

```
1. Construir arquivo .PJC com:
   - data-base: data do contrato / sentença
   - data-fim: DATA DO PEDIDO DE RJ (não a data atual!)
   - índices conforme jurisprudência aplicável
2. Executar o cálculo via script gerar-pjc.ps1.
3. Importar o resultado e mapear para a planilha desta skill.
```

⚠️ Atenção: o PjeCalc, por padrão, atualiza até a data corrente.
Configurar explicitamente a DATA DO PEDIDO DE RJ como data-fim.

---

## 5. SAÍDA

```
[BLOCO X — CÁLCULO]
1. Memorial de cálculo (passo a passo, por verba)
2. Planilha consolidada (tabela do Passo 5)
3. Resumo:
   • Total Classe I:        R$ ...
   • Total Classe III:      R$ ...
   • Total extraconcursal:  R$ ...
   • Total geral habilitado: R$ ...
4. Pendências:
   • [eventual confirmação de índice]
   • [eventual confirmação de classe — sucumbenciais, FGTS]
5. Data-base: DATA DO PEDIDO DE RJ — [data]
```

---

## 6. PROIBIÇÕES ESPECÍFICAS

- **PA-CALC-01**: Nunca atualizar além da data do pedido de RJ.
- **PA-CALC-02**: Nunca aplicar Classe I sem o teto de 150 SM.
- **PA-CALC-03**: Nunca classificar FGTS sem confirmar Tema 1.051 STJ.
- **PA-CALC-04**: Nunca habilitar INSS empregado em nome do credor.
- **PA-CALC-05**: Nunca esquecer de cindir crédito a cavaleiro do pedido.
- **PA-CALC-06**: Nunca usar a data atual como data-fim do cálculo.

---

## 7. ALERTAS DISPARADOS

- A7 — data-base do cálculo
- A8 — aplicação do teto Classe I
- A16 — FGTS / Tema 1.051
- A17 — honorários sucumbenciais
- A19 — cessão (se houver) → classe rebaixada (art. 83 §4º)

---

## 8. EXEMPLO RESOLVIDO

> Ilustra o método. Os índices de correção/juros saem do **Cálculo Oficial
> de Débitos Judiciais do TJ** (art. 9º, II, da LFRE) — os fatores abaixo são
> ilustrativos; no caso real, importar do Cálculo Oficial.

**Caso:** empregado dispensado sem justa causa em **15/03/2018**; TRCT
homologado, líquido rescisório **não pago** R$ 16.800,00; FGTS + 40% não
recolhidos R$ 6.000,00. **Pedido de RJ: 01/05/2022** (data-fim — PA-CALC-01/06).

**Passo 1 — Verbas (principal histórico, data do fato gerador 15/03/2018):**
- Rescisórias (TRCT) ......... R$ 16.800,00
- FGTS + multa de 40% ........ R$ 6.000,00

**Passo 2 — Atualização até 01/05/2022 (Cálculo Oficial):**
- Fator acumulado correção+juros (ilustrativo) ≈ 1,55
- Rescisórias: 16.800,00 × 1,55 = **R$ 26.040,00**
- FGTS+40%: 6.000,00 × 1,55 = **R$ 9.300,00**

**Passo 3 — Classificação (cravar o fato gerador — PA-CALC-06):**
- Rescisórias: trabalhista, fato gerador na rescisão (pré-pedido) → **Classe I**.
- FGTS+40%: concursal porque o fato gerador é anterior ao pedido (**Tema 1.051
  STJ** — validar); natureza trabalhista → Classe I. *Pendência: confirmar
  classificação do FGTS (PA-CALC-03).*

**Passo 4 — Teto da Classe I (150 SM — PA-CALC-02):**
- SM em 01/05/2022 = R$ 1.212,00 → teto = 150 × 1.212,00 = **R$ 181.800,00**.
- Total Classe I = 26.040,00 + 9.300,00 = **R$ 35.340,00** < teto → tudo na
  Classe I, **sem cisão** para a Classe III.

**Resultado:** habilitar **R$ 35.340,00 na Classe I** (art. 41, I, da LFRE),
atualizado até 01/05/2022. INSS empregado e IR são informativos (não habilitam
pelo credor — PA-CALC-04). Sucumbenciais, se houver, em separado (A17).
