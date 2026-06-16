# tributario-adv-os

**O sistema operacional do advogado tributarista brasileiro**, no padrao **Adv-OS**.

`tributario-adv-os` e um plugin do Claude Code que transforma o assistente num
operador de Direito Tributario disciplinado: faz a triagem do caso, valida a
norma vigente no fato gerador, monta a estrategia, redige a peca e audita tudo
antes da entrega. Side-aware: opera defendendo o **contribuinte** (defesa) ou,
quando for o caso, produzindo a peca da **Fazenda Publica**.

---

## O que ele cobre — 3 frentes x 3 esferas

| Frente | O que faz | Esferas |
|---|---|---|
| **Administrativa** | Impugnacao ao auto de infracao/lancamento (PAF — Dec. 70.235/72), recurso ao CARF/CSRF, TIT e conselhos de contribuintes | federal / estadual / municipal |
| **Judicial** | Defesa na execucao fiscal (embargos LEF + excecao de pre-executividade), acao anulatoria, mandado de seguranca, repeticao de indebito e compensacao | federal / estadual / municipal |
| **Consultiva** | Planejamento tributario licito, escolha de regime, parcelamento e transacao (Lei 13.988/2020), impacto da Reforma | federal / estadual / municipal |

- **Esfera federal:** IR, IPI, PIS, COFINS, CSLL, IOF, ITR, contribuicoes.
- **Esfera estadual:** ICMS, IPVA, ITCMD.
- **Esfera municipal:** ISS, IPTU, ITBI.
- **Reforma Tributaria:** skill dedicada a transicao **CBS/IBS** (EC 132/2023 +
  LC 214/2025), com convivencia de regimes no periodo **2026-2033**.

---

## As 20 skills (por Tier)

**Tier 0 — Governanca**
- `tributario-master` — orquestracao central, 4 Camadas, roteamento.

**Tier 1 — Insumos e estrategia**
- `onboarding-tributario` — wizard de configuracao do escritorio.
- `triagem-tributaria` — porta de entrada, 5 eixos + Selo de Validacao de Norma Vigente (P1).
- `analise-documental-tributaria` — leitura do auto/CDA/lancamento/documentos.
- `jurisprudencia-tributaria` — pesquisa e validacao de jurisprudencia (PA-01).
- `calculos-tributarios` — apuracao, atualizacao, Selic, multas.
- `analise-trilateral-tributaria` — cliente x adversario (Fazenda) x julgador.
- `linha-estrategica-tributaria` — define a tese central e as subsidiarias.
- `memoria-de-caso-tributario` — CASO.md compartimentado (P3).
- `estilo-juridico-tributario` — peca enxuta, docs numerados, tom do escritorio.

**Tier 2 — Producao**
- `impugnacao-administrativa` — impugnacao ao auto/lancamento (CTN 151 III).
- `recurso-administrativo-carf` — recurso voluntario/especial (CARF/CSRF/TIT).
- `defesa-execucao-fiscal` — embargos LEF art. 16 x excecao de pre-executividade.
- `acao-anulatoria-tributaria` — anulatoria de debito fiscal (art. 38 LEF).
- `mandado-seguranca-tributario` — MS tributario (Lei 12.016/2009).
- `repeticao-indebito-compensacao` — restituicao/compensacao (CTN 165-170).
- `planejamento-tributario` — planejamento licito (elisao).
- `parcelamento-transacao` — parcelamentos + transacao (Lei 13.988/2020).
- `reforma-tributaria` — CBS/IBS, transicao 2026-2033.

**Tier 3 — Auditoria**
- `revisao-final-tributaria` — Suprema Corte do plugin, auditoria R1-R4.

---

## Os 13 comandos

| Comando | Funcao |
|---|---|
| `/tributario-master` | Mostra a governanca e a config ativa; roteia a demanda. |
| `/triagem` | **Porta de entrada** — triagem em 5 eixos, grava no CASO.md. |
| `/start-tributario` | Wizard de configuracao do plugin no escritorio. |
| `/status-tributario` | Resume o estado: persona, caso ativo, frente/esfera, prazos. |
| `/caso-tributario` | Abre/atualiza o CASO.md do caso ativo (P3). |
| `/revisao-final` | Dispara a auditoria R1-R4 antes da entrega. |
| `/impugnacao` | Impugnacao administrativa ao auto/lancamento. |
| `/recurso-carf` | Recurso administrativo (CARF/CSRF/TIT/conselhos). |
| `/execucao-fiscal` | Defesa na execucao fiscal (embargos x excecao). |
| `/anulatoria` | Acao anulatoria de debito fiscal (art. 38 LEF). |
| `/mandado-seguranca` | MS tributario (Lei 12.016/2009). |
| `/repeticao` | Repeticao de indebito / compensacao (CTN 165-170). |
| `/planejamento` | Planejamento licito, regimes, parcelamento/transacao, reforma. |

---

## Governanca

### 4 Camadas
O `tributario-master` (Tier 0) governa o pipeline em **4 Camadas**: (1) Insumos —
triagem, documentos, jurisprudencia, calculos; (2) Estrategia — trilateral e
linha estrategica; (3) Producao — as peças; (4) Auditoria — R1-R4. Nada e
entregue sem passar pela Camada 4.

### As 13 Proibicoes Absolutas (resumo)
- **PA-01** — nunca alucinar jurisprudencia; citar so o que foi validado.
- **PA-04** — usar a norma vigente no fato gerador (+ regra de transicao da Reforma).
- **PA-05** — nunca confundir decadencia com prescricao.
- **PA-06** — nunca confundir elisao (licita) com evasao (ilicita); nada de planejamento simulado.
- **PA-07** — excecao de pre-executividade so para materia de ordem publica sem dilacao probatoria.
- **PA-08** — nao aceitar redirecionamento ao socio sem os requisitos do art. 135 CTN / Sum. 435 STJ.
- **PA-09** — prazo de 5 anos na repeticao/compensacao.
- **PA-10** — coerencia de polo; em duvida/contradicao, parar e perguntar.
- **PA-11** — Selo P1: toda norma/jurisprudencia passa pela validacao de vigencia.
- **PA-13** — toda entrega passa pela auditoria R1-R4.

> A lista completa e operacional vive nas skills `tributario-master` e
> `revisao-final-tributaria`; os codigos acima sao os ganchos referenciaveis.

### Selo P1 e R1-R4
- **Selo de Validacao de Norma Vigente (P1)** — aplicado na triagem e na revisao:
  nenhuma norma ou precedente entra na peca sem checagem de vigencia.
- **Suprema Corte R1-R4** — auditoria obrigatoria em quatro rodadas (R1 dados,
  R2 base juridica, R3 tese, R4 completude) antes de qualquer entrega.

---

## Instalacao rapida

Via marketplace `machado-advocacia-marketplace`:

```
/plugin install tributario-adv-os@machado-advocacia-marketplace
```

---

## Fluxo de uso

```
/start-tributario     ->  configura o escritorio (1a vez): persona, frentes, esferas, polo
/triagem              ->  classifica o caso nos 5 eixos e grava o CASO.md
   (producao)         ->  /impugnacao  /recurso-carf  /execucao-fiscal
                          /anulatoria  /mandado-seguranca  /repeticao  /planejamento
/revisao-final        ->  auditoria R1-R4 antes de entregar
```

A qualquer momento: `/status-tributario` para ver o estado e `/caso-tributario`
para atualizar o caso ativo.

---

## Sigilo e dados de cliente

Os casos vivem em `tributario/casos/<slug>/` e sao **gitignored** por default —
**sigilo profissional (CTN art. 198) + LGPD**. Nenhum dado de cliente persiste
no plugin distribuido. Se o workspace for pasta sincronizada (OneDrive / iCloud
/ Google Drive / Dropbox), o plugin emite alerta. Entregas em **`.txt`** por
padrao.

---

## Interface com outros plugins

**Crimes tributarios (Lei 8.137/90)** — sonegacao, apropriacao indebita
previdenciaria e correlatos — sao tratados em **interface com o plugin
criminal**. Este plugin sinaliza o risco penal e encaminha; nao produz a defesa
criminal.

---

**Plugin:** `tributario-adv-os` · padrao Adv-OS · Machado Advocacia · licenca MIT.
