---
name: contestacao-rj
description: >
  CONTESTACAO-RJ — Tier 2 (Produção). Redige contestações, impugnações e defesas em
  processos de recuperação judicial: impugnação ao pedido de RJ (pelo credor), impugnação
  ao plano de recuperação (pelo credor), contestação ao pedido de falência (pelo devedor),
  resposta à impugnação de crédito, e defesa contra atos de revogação do período suspeito.
  Acionar quando o usuário precisar contestar qualquer medida em processo de insolvência,
  independentemente do polo. Side-aware: a estratégia muda completamente conforme o polo.
---

# CONTESTACAO-RJ
> Tier 2 | Contestação e Impugnação | Defesa em RJ/Falência | Side-Aware

---

## 0. ESCOPO

Redige peças defensivas e impugnatórias em processos de insolvência. Antes de redigir,
confirma o polo no CASO.md — estratégia, teses e pedidos são opostos conforme o lado.

⚠️ **PA-02**: Confirmar polo processual antes de iniciar qualquer redação.
⚠️ **PA-03**: Não confundir defesas de RJ com defesas de falência — prazos e teses são distintos.

---

## 1. MAPA DE PEÇAS POR POLO E SITUAÇÃO

| Situação | Polo | Peça |
|----------|------|------|
| Credor questiona o pedido de RJ | Credor | Impugnação ao processamento |
| Credor rejeita o plano apresentado | Credor | Impugnação ao plano (art. 55) |
| Devedor recebe pedido de falência | Devedor | Contestação + pedido de RJ (art. 95) |
| Credor tem crédito impugnado | Credor | Resposta à impugnação de crédito |
| Devedor é alvo de ação revocatória | Devedor | Contestação à ação revocatória |
| AJ pede afastamento dos administradores | Devedor | Defesa + recursos |
| Credor requer convolação em falência | Devedor | Defesa à convolação (art. 73) |

---

## 2. IMPUGNAÇÃO AO PROCESSAMENTO DA RJ (Polo: Credor)

Prazo: manifestação dentro do prazo fixado pelo juiz após a publicação do deferimento.

```
IMPUGNAÇÃO AO PROCESSAMENTO DA RECUPERAÇÃO JUDICIAL
Processo nº [...] | Devedor: [...]

IMPUGNANTE: [Credor]

I — DOS FATOS
[contextualização do pedido de RJ e da situação do credor]

II — DOS FUNDAMENTOS DA IMPUGNAÇÃO

[ESCOLHER OS APLICÁVEIS:]

2.1 Ausência de requisito do art. 48:
"O devedor não comprovou o exercício regular de atividade empresarial
pelo período mínimo de 2 (dois) anos exigido pelo art. 48 da LFRJ,
conforme se verifica pela certidão da Junta Comercial acostada, que
demonstra [razão específica]."

2.2 Inelegibilidade por RJ anterior:
"O devedor obteve recuperação judicial encerrada há menos de 5 (cinco)
anos, conforme certidão do processo nº [...], em violação ao art. 48, II."

2.3 Fraude na relação de credores (art. 51, III):
"A relação de credores apresentada omite crédito deste impugnante de
R$ [...], devidamente documentado, o que torna a petição inepta."

2.4 Incompetência do juízo:
"O principal estabelecimento do devedor não é [comarca], mas sim [outra
comarca], onde concentra o maior volume de negócios, conforme documentos
(...), aplicando-se a Súm. 480 do STJ."

2.5 Ausência de viabilidade econômica:
"Os documentos do art. 51 não demonstram qualquer viabilidade econômica,
sendo a situação do devedor de falência de fato, não de crise superável."

III — DO PEDIDO
[rejeição do processamento / decretação da falência / determinação de emenda]
```

---

## 3. IMPUGNAÇÃO AO PLANO DE RECUPERAÇÃO (Polo: Credor)

Prazo: 30 dias após a publicação do plano (art. 55 LFRJ).

```
IMPUGNAÇÃO AO PLANO DE RECUPERAÇÃO JUDICIAL
Processo nº [...] | Devedor: [...]

IMPUGNANTE: [Credor — Classe X]

I — DA LEGITIMIDADE E TEMPESTIVIDADE
[Credor da Classe X, crédito de R$ [...], protocolado dentro do prazo do art. 55]

II — DOS FUNDAMENTOS DA IMPUGNAÇÃO

2.1 Inviabilidade econômico-financeira (art. 53, II):
"O laudo de viabilidade apresentado pelo devedor parte de premissas irrealistas,
notadamente: [i] taxa de crescimento de receita de X% sem base histórica;
[ii] desconsideração do passivo fiscal de R$ [...]; [iii] WACC subdimensionado..."

2.2 Discriminação entre credores da mesma classe (art. 58, §2º):
"O plano prevê deságio de X% para credores quirografários individuais e de Y% para
credores institucionais, sem qualquer justificativa objetiva, em violação à isonomia."

2.3 Prazo de carência excessivo / abusivo:
"O plano prevê carência de X anos para a Classe III, durante a qual não haverá
qualquer pagamento, enquanto os encargos continuam fluindo, o que configura
benefício unilateral ao devedor desproporcional ao sacrifício imposto."

2.4 Ausência de meios de recuperação concretos:
"O plano se limita a declarações genéricas de intenção sem especificar os meios
do art. 50 a serem efetivamente implementados."

2.5 Cram down indevido (se o juiz for conceder):
"Não estão preenchidos os requisitos do art. 58, §1º pois [razão específica]."

III — DO PEDIDO
Rejeição do plano / Determinação de modificação / Convocação de AGC
```

---

## 4. CONTESTAÇÃO AO PEDIDO DE FALÊNCIA (Polo: Devedor)

Prazo: 10 dias após citação (art. 98 LFRJ).

```
CONTESTAÇÃO
Processo nº [...] | Requerente: [Credor] | Requerido: [Devedor]

I — DA PRELIMINAR: ELISÃO DA FALÊNCIA / PEDIDO DE RECUPERAÇÃO JUDICIAL
"Com base no art. 95 da LFRJ, o devedor requer a conversão em processo de
recuperação judicial, demonstrando: [i] elegibilidade pelo art. 48;
[ii] viabilidade econômica; [iii] documentos do art. 51 em anexo."

OU

I — DA TEMPESTIVIDADE DO PAGAMENTO (art. 94, I):
"O alegado inadimplemento não é injustificado. O devedor [pagou / depositou /
a dívida é objeto de discussão judicial por meio de [ação anterior]]."

II — DO MÉRITO
2.1 Ausência de requisito do art. 94:
"O crédito não alcança o mínimo de 40 salários mínimos exigido pelo art. 94, I."

2.2 Falsidade do título (art. 96, VI):
"O título executivo apresentado [é falso / foi pago / é inexigível] conforme [prova]."

2.3 Vício formal do título:
"[Protesto irregular / título prescrito / endosso inválido]"

III — DO PEDIDO
[extinção do processo / conversão em RJ / improcedência]
```

---

## 5. DEFESA À CONVOLAÇÃO EM FALÊNCIA (art. 73 — Polo: Devedor)

Causas de convolação (art. 73):
- I: Deliberação dos credores na AGC
- II: Não apresentação do plano no prazo (60 dias — PA-06)
- III: Rejeição do plano pela AGC (sem cram down)
- IV: Descumprimento do plano ou das obrigações assumidas

Estratégia de defesa:
```
Para o inc. II (prazo): demonstrar que o prazo ainda não transcorreu ou que
houve prorrogação judicial deferida / requerida tempestivamente.

Para o inc. III (rejeição): demonstrar que o cram down é aplicável e requerê-lo.

Para o inc. IV (descumprimento): demonstrar que:
- Descumprimento foi pontual e já regularizado
- Força maior / caso fortuito (pandemia, interrupção de fornecimento)
- Novação das obrigações aprovada pelos credores
```

---

## 6. VEDAÇÕES

- **PA-02**: Confirmar polo antes de redigir — teses são opostas por polo
- **PA-03**: Não confundir defesas de RJ com falência — prazos e base legal diferentes
- **PA-04**: Verificar fase processual atual — defesas fora do prazo são intempestivas
- **PA-24**: Revisao-final-rj antes de protocolar qualquer contestação
