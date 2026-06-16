# consumidor-adv-os

Sistema operacional do advogado brasileiro de **Direito do Consumidor e Bancário**, no padrão Adv-OS (mesmo chassi de `direito-medico-adv-os` e `trabalhista-adv-os`).

Atende os **dois polos** da relação de consumo — consumidor e fornecedor — com orquestrador side-aware, triagem 4D, governança de 4 Camadas, Selo de Validação Legal Prévia e Suprema Corte R1-R4 sobre toda entrega. Persona resolvida em runtime via `/start-consumidor`.

## Eixos cobertos (13)
Bancário/financeiro · Negativação & cadastros · Telecom · Serviços essenciais · Transporte aéreo · Vício & fato do produto · E-commerce · Publicidade · Cláusulas abusivas · Cobrança indevida · Superendividamento (L14.181) · Consumo imobiliário (interface).

> Plano de saúde é tratado **só como interface** → encaminha ao plugin de direito médico (sem duplicar).

## Arquitetura — triagem 4D
Cada caso é classificado em 4 dimensões simultâneas:

| Dimensão | Valores |
|----------|---------|
| **Polo** | Consumidor · Fornecedor |
| **Eixo** | os 13 acima |
| **Esfera** | Judicial · Administrativa (PROCON / consumidor.gov.br / BACEN / ANATEL / ANAC) · Extrajudicial |
| **Rito** | JEC · Vara cível comum · Ação coletiva |

## Commands
`/consumidor-master` · `/triagem-consumidor` · `/start-consumidor` · `/status-consumidor` · `/caso-consumidor` · `/revisao-final-consumidor` · `/jurisprudencia-consumidor` · `/calculos-consumidor`
Núcleos diretos: `/bancario` · `/contratual` · `/servicos-regulados` · `/produto` · `/superendividamento` · `/defesa-fornecedor`

## Skills (35)
- **Tier 0** — `consumidor-master` (orquestração; 4 Camadas, Proibições Absolutas, 6 Protocolos)
- **Tier 1 (12)** — onboarding, triagem 4D, validador (Selo P1), análise documental, análise contratual, jurisprudência, cálculos, trilateral, linha estratégica, memória de caso, estilo, timeline
- **Tier 2 (21)** — petição inicial, tutela de urgência, revisional bancária, defesa em busca e apreensão, negativação indevida, repetição de indébito, vício/fato do produto, superendividamento, transporte aéreo, telecom/serviços, publicidade abusiva, consumo imobiliário, contestação, defesa de instituição financeira, réplica, petição JEC, reclamação administrativa, acordo, recursos, embargos de declaração, cumprimento de sentença
- **Tier 3 (1)** — `revisao-final-consumidor` (Suprema Corte R1-R4)

## Primeiro uso
1. `/start-consumidor` — configura o escritório (advogado, OAB, cidade/UF, polos, eixos, tom). Gera `consumidor/persona.md` + `config.md` + `casos/`.
2. `/triagem-consumidor` — abre o primeiro caso (triagem 4D → `CASO.md`).
3. Produza a peça pelo núcleo correspondente; tudo passa pela `revisao-final-consumidor` antes da entrega.

## Marco normativo central
CDC (L8.078/90) · L14.181/2021 · Lei 9.099/95 (JEC) · Decreto 7.962/2013 · CC/2002 + CPC/2015 · resoluções ANATEL/ANAC/BACEN · súmulas STJ (297, 359, 385, 472, 479, 530, 539, 543) · Tema 929 (dobro art. 42) · Tema 210 STF (Montreal).

---
Uso interno — Machado Advocacia. Saída padrão em `.txt`.
