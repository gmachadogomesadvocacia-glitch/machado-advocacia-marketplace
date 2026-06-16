---
name: habilitacao-credito-rj
description: >
  HABILITACAO-CREDITO-RJ — Tier 2 (Produção). Skill geral de habilitação,
  impugnação e divergência de créditos no QGC, para QUALQUER classe de
  credor (não-trabalhista). Para credor TRABALHISTA, a porta de entrada
  é `credor-trabalhista-rj` (eixo prioritário). Esta skill cobre os 4
  sub-fluxos explícitos: §A divergência administrativa (art. 7º §1º),
  §B impugnação judicial (art. 8º), §C habilitação retardatária (art. 10),
  §D reserva pelo art. 6º §2º. Antes de redigir, invoca
  `via-processual-rj` para decidir a via. Atua pelo credor (habilitando
  ou impugnando QGC) ou pelo devedor/AJ (impugnando créditos fraudulentos).
---

# HABILITACAO-CREDITO-RJ

> Tier 2 | Habilitação e Impugnação de Créditos | Arts. 7-20 LFRJ | QGC

---

## 0. ESCOPO E ROTEAMENTO INTERNO

Esta skill cobre habilitação/impugnação para credores **não-trabalhistas**
(fornecedor, instituição financeira, locador, ME/EPP, garantia real, e
todos os demais). Também atua **pelo devedor ou AJ** quando o objetivo é
impugnar crédito alheio (fraude, valor inflado, classificação indevida).

**REGRA DE ROTEAMENTO INTERNO**:

```
SE crédito de origem trabalhista (sentença JT, acordo JT, FGTS,
   reclamatória, CH, etc.):
   → ROTEAR PARA `credor-trabalhista-rj` (eixo prioritário)
   → ESTA SKILL não cobre o caso

SE crédito de natureza diversa (fornecedor, bancário, locatício, etc.):
   → seguir os 4 sub-fluxos desta skill
```

Aplica o **Protocolo P4** (Mapeamento de Credores) — atualiza o CASO.md
com créditos mapeados.

⚠️ **PA-15**: Créditos extraconcursais (art. 84) devem ser segregados.
⚠️ **PA-07**: Classificação incorreta pode alterar o quórum da AGC.
⚠️ **PA-24**: Toda peça passa por `revisao-final-rj` antes da entrega.

---

## 1. FLUXO MACRO

```
[Pedido de RJ + deferimento do processamento (art. 52)]
        ↓
  Publicação do edital do art. 52 §1º
        ↓
  [§A] Janela de 15 dias para habilitação/divergência ao AJ (art. 7º §1º)
        ↓
  AJ elabora a relação consolidada (art. 7º §2º — 45 dias)
        ↓
  Publicação da relação consolidada
        ↓
  [§B] Janela de 10 dias para IMPUGNAÇÃO judicial (art. 8º)
        ↓
  Decisão do juízo + Quadro Geral de Credores (art. 14)
        ↓
  [§C] Após QGC homologado: HABILITAÇÃO RETARDATÁRIA (art. 10)
        ↓
  Recurso: Agravo de Instrumento (art. 17)

[§D] em paralelo: ART. 6º §2º para créditos em liquidação (típico
     trabalhista, mas aplicável a qualquer crédito ilíquido em
     ação ajuizada antes do pedido de RJ)
```

---

## 2. DELEGAÇÃO À `via-processual-rj`

Antes de redigir QUALQUER peça desta skill, **sempre** invocar
`via-processual-rj` com os dados do caso. O veredito retornado
(I / III-A / III-B / IV / V / E / F) determina qual sub-fluxo
desta skill será executado.

---

## 3. §A — DIVERGÊNCIA / HABILITAÇÃO ADMINISTRATIVA (ART. 7º §1º)

### 3.1 Quando

- Edital do art. 52 §1º publicado.
- Janela de 15 dias ainda aberta.
- Crédito não consta da relação do devedor (art. 51, III) ou
  consta com erro.

### 3.2 Endereçamento

**ADMINISTRADOR JUDICIAL** (administrativo, não judicial).

### 3.3 Estrutura

```
EXMO. SR. ADMINISTRADOR JUDICIAL DA RECUPERAÇÃO JUDICIAL DE [DEVEDOR]
Processo nº [...] — [Juízo]

[CREDOR], qualificação, por seu advogado infra-assinado (procuração
anexa), vem, com fundamento no art. 7º, §1º, da Lei nº 11.101/2005,
dentro do prazo de 15 dias da publicação do edital ocorrida em [data],
apresentar

DIVERGÊNCIA / HABILITAÇÃO DE CRÉDITO

I — DA TITULARIDADE
[origem do crédito]

II — DA NATUREZA E SUJEIÇÃO À RJ
[fato gerador anterior ao pedido — art. 49]

III — DA CLASSIFICAÇÃO (art. 83)
[Classe I/II/III/IV — com fundamento legal]

IV — DOS DOCUMENTOS
[lista]

V — DO PEDIDO
Requer o registro do crédito do Habilitante em R$ [...] (Classe [...])
para inclusão na relação consolidada.

[Local], [data].
[Advogado] — OAB/[UF]
```

### 3.4 Documentos de suporte por tipo de crédito

| Tipo | Documentos |
|------|-----------|
| Fornecedor | NF-e, duplicatas, contratos de fornecimento |
| Financeiro (banco) | CCB, contrato de mútuo, extrato de saldo devedor |
| Locatício | Contrato de locação, cálculo de aluguéis vencidos |
| Sentença judicial cível | Certidão do processo + cálculo atualizado |
| Garantia real | Instrumento de garantia + certidão de registro |
| ME/EPP (Classe IV) | Certidão de enquadramento + documentos da dívida |

---

## 4. §B — IMPUGNAÇÃO JUDICIAL (ART. 8º)

### 4.1 Quando

- Relação consolidada do AJ (art. 7º §2º) já publicada.
- Janela de 10 dias.
- Crédito não consta ou consta com erro de valor/classe.

### 4.2 Endereçamento

**JUÍZO DA RJ** — autuação em apartado (art. 8º + art. 13).

### 4.3 Pelo credor

```
EXMO. SR. JUIZ DE DIREITO DA [Vara]
Processo principal: [nº da RJ] — em apartado

[CREDOR], qualificação, nos autos da RJ de [DEVEDOR], com fundamento
no art. 8º da LFRJ, dentro do prazo de 10 dias da publicação da
relação consolidada ocorrida em [data], apresenta

IMPUGNAÇÃO À RELAÇÃO DE CREDORES

I — DOS FATOS
[crédito omitido / valor incorreto / classe errada]

II — DO DIREITO
[a] Concursalidade (art. 49)
[b] Classificação (art. 83)
[c] Valor atualizado até o pedido (art. 9º, II)

III — DOS DOCUMENTOS

IV — DO PEDIDO
a) recebimento e processamento da impugnação em apartado;
b) intimação do AJ e do devedor (art. 11);
c) procedência para incluir/retificar/reclassificar o crédito;
d) sucumbência.

[Local], [data].
[Advogado] — OAB/[UF]
```

### 4.4 Pelo devedor ou AJ — impugnação ofensiva

Fundamentos comuns:

1. **Simulação ou fraude**: crédito inexistente.
2. **Valor inflado**: juros abusivos, multas ilegais, capitalização.
3. **Prescrição**: crédito prescrito não habilita.
4. **Classificação indevida**: quirografário apresentado como real.
5. **Crédito subordinado**: sócio/controlador (art. 83, VIII).
6. **Duplicidade**: mesmo crédito habilitado duas vezes (cedente +
   cessionário) ou junto e separado.

Template:

```
IMPUGNAÇÃO DE CRÉDITO (PELO DEVEDOR OU AJ)
Processo nº [...] — RJ de [DEVEDOR]

IMPUGNANTE: [Devedor / Administrador Judicial]
CRÉDITO IMPUGNADO: [Credor X] — R$ [valor] — Classe [Y]

FUNDAMENTO:
I — Da prescrição (art. ... CC / art. 7º XXIX CF):
II — Do valor incorreto:
III — Da classificação indevida:
IV — Da simulação / fraude:

PEDIDO: exclusão / retificação para R$ [...] / reclassificação para
classe [Z].
```

---

## 5. §C — HABILITAÇÃO RETARDATÁRIA (ART. 10)

### 5.1 Quando

- Prazos do §A e §B perdidos.
- QGC já homologado (art. 14) ou em vias de homologação.

### 5.2 Consequências

- **SEM direito de voto na AGC** (art. 10, §1º). Alerta crítico.
- Custas pelo habilitante (art. 10, §3º).
- Não recebe valores já pagos no plano (art. 10, §6º).

### 5.3 Antes de redigir

Verificar se ainda há pretensão exercitável. Para crédito trabalhista,
consultar a verificação de §5-BIS de `credor-trabalhista-rj` (bienal CF,
intercorrente CLT, art. 11-A, art. 61). Para crédito não-trabalhista,
aplicar art. 205/206 CC conforme natureza, confirmando via
`jurisprudencia-rj` quando houver controvérsia.

### 5.4 Estrutura

```
EXMO. SR. JUIZ DE DIREITO DA [Vara]
Processo principal: [nº da RJ] — em apartado

[CREDOR], nos autos da RJ de [DEVEDOR], com fundamento no art. 10
da LFRJ, apresenta

HABILITAÇÃO RETARDATÁRIA DE CRÉDITO

ciente das limitações do art. 10, §§1º e 3º.

I — DA TEMPESTIVIDADE
Justificativa: [...]

II — DA TITULARIDADE E NATUREZA
[origem, fato gerador, concursalidade]

III — DA CLASSIFICAÇÃO

IV — DOS DOCUMENTOS

V — DO PEDIDO
a) recebimento da habilitação retardatária;
b) processamento (art. 10 c/c art. 13);
c) reconhecimento do crédito de R$ [...] (Classe [...]);
d) custas pelo habilitante (art. 10, §3º).

[Local], [data].
```

---

## 6. §D — RESERVA POR ART. 6º §2º (CRÉDITO ILÍQUIDO)

### 6.1 Quando

- Ação judicial ajuizada antes do pedido de RJ.
- Liquidação ainda em curso (em regra, JT — mas também ações cíveis
  com fase de liquidação).
- Crédito ilíquido no momento da habilitação.

### 6.2 Endereçamento

**JUÍZO DA RJ** — petição requerendo reserva.

### 6.3 Estrutura

```
EXMO. SR. JUIZ DE DIREITO DA [Vara]
Processo: [nº da RJ]

[CREDOR], com fundamento no art. 6º, §2º, da LFRJ, vem requerer a

RESERVA DE CRÉDITO ILÍQUIDO

I — DOS FATOS
[ação nº ... em fase de liquidação — JT/cível]

II — DO DIREITO
A liquidação prossegue no juízo competente. Apurado o quantum,
expede-se certidão para habilitação. Enquanto isso, impõe-se a
reserva.

III — DO PEDIDO
a) reserva de R$ [valor estimado] em favor do Habilitante;
b) ofício ao juízo da liquidação;
c) após certidão, habilitação definitiva.
```

---

## 7. CRÉDITOS EXTRACONCURSAIS — ART. 84

⚠️ **PA-15**: NÃO habilitar no plano.

| Tipo | Art. 84 | Tratamento |
|------|---------|-----------|
| Remuneração do AJ | I | Prioritário |
| Trabalhistas pós-pedido (3 meses pré-falência) | I-B | Prioritário |
| Créditos decorrentes de atos do devedor durante a RJ | I-C | Prioritário |
| Tributários posteriores ao pedido | I-D | Prioritário |
| Garantia real pós-pedido | II | Preferencial |
| Despesas do processo | III | Preferencial |

Segregar no QGC do CASO.md.

---

## 8. CLASSES DA L14.112

| Classe | Conteúdo | Art. |
|--------|----------|------|
| I | Trabalhistas até 150 SM + acidente de trabalho | 83, I |
| II | Garantia real até o valor do bem | 83, II |
| III | Quirografários, especiais e subordinados não-sócios | 83, VI |
| IV | ME/EPP (LC 123) | 83, IV |
| —  | Subordinados (sócios) | 83, VIII (fora do plano) |

⚠️ **Cessão de crédito trabalhista** (art. 83 §4º): cessionário pode
ter classe rebaixada.

---

## 9. VEDAÇÕES

- **PA-15**: Extraconcursais não se sujeitam ao plano.
- **PA-07**: Classificação incorreta distorce quórum.
- **PA-08**: Trabalhista acima de 150 SM → excedente em Classe III.
- **PA-23**: Não atuar simultaneamente por credor e devedor.
- **PA-24**: `revisao-final-rj` antes de protocolar.

---

## 10. POSIÇÃO NO PIPELINE

```
[detecção: origem trabalhista?]
       SIM → ROTEAR para `credor-trabalhista-rj`
       NÃO ↓
[via-processual-rj] (decide a via)
       ↓
[§A / §B / §C / §D desta skill] (redação)
       ↓
[revisao-final-rj] (R1-R4)
       ↓
[memoria-de-caso-rj] (atualiza CASO.md)
       ↓
ENTREGA
```

---

## 11. MODELOS DE PEÇA (CHASSIS)

Antes de redigir, abrir o chassi (padrão enxuto) e substituir os `[____]`:
- Habilitação trabalhista (art. 10) → `templates/pecas/habilitacao-retardataria-trabalhista.md`
- Impugnação de crédito / §B (art. 8º) → `templates/pecas/impugnacao-credito-qgc.md`
