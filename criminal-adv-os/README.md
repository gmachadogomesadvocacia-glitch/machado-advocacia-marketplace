# criminal-adv-os

**O sistema operacional do advogado criminalista brasileiro**, no padrao **Adv-OS**.

`criminal-adv-os` e um plugin do Claude Code que transforma o assistente num
operador de Direito Penal e Processo Penal disciplinado: faz a triagem do caso,
valida a lei penal vigente no tempo do fato, monta a estrategia, redige a peca e
audita tudo antes da entrega. **Prioridade absoluta a liberdade quando ha pessoa
presa.** Side-aware: opera na **defesa** (investigado / reu / sentenciado) ou,
quando for o caso, na **assistencia de acusacao** (vitima/ofendido).

---

## O que ele cobre — as 6 fases

| Fase | O que faz |
|---|---|
| **Investigacao / Inquerito** | Flagrante, audiencia de custodia, relaxamento de prisao ilegal, liberdade provisoria, fianca, prisoes temporaria/preventiva, cautelares diversas (CPP 310/319). |
| **Acao penal** | Resposta a acusacao (CPP 396-A), preliminares, instrucao, alegacoes finais, absolvicao sumaria (CPP 397). |
| **Tribunal do Juri** | Pronuncia / impronuncia / desclassificacao / absolvicao sumaria, plenario, quesitos (CPP 406-497). |
| **Recursos** | Apelacao, RESE, embargos, RHC, recursos superiores; vedada a reformatio in pejus (CPP 617). |
| **Execucao penal** | LEP 7.210/84 — progressao, livramento, remicao, falta grave, agravo em execucao. |
| **Acordos despenalizadores** | ANPP (CPP 28-A), transacao penal e suspensao condicional do processo (Lei 9.099/95). |

> **Side-aware:** defesa x assistencia de acusacao. O polo e a variavel-mae —
> em ausencia ou contradicao, o plugin para e pergunta (PA-10).

---

## As 20 skills (por Tier)

**Tier 0 — Governanca**
- `criminal-master` — orquestracao central, 4 Camadas, roteamento.

**Tier 1 — Insumos e estrategia**
- `onboarding-criminal` — wizard de configuracao do escritorio.
- `triagem-criminal` — porta de entrada, 5 eixos + Selo de Validacao Legal Previa (P1).
- `analise-documental-criminal` — leitura do inquerito/denuncia/autos/laudos.
- `jurisprudencia-criminal` — pesquisa e validacao de jurisprudencia (PA-01).
- `calculos-criminais` — dosimetria, prescricao, marcos da execucao penal.
- `analise-trilateral-criminal` — cliente x acusacao/MP x julgador.
- `linha-estrategica-criminal` — define a tese central e as subsidiarias.
- `memoria-de-caso-criminal` — CASO.md compartimentado (P3), sigilo reforcado.
- `estilo-juridico-criminal` — peca enxuta, docs numerados, tom do escritorio.

**Tier 2 — Producao**
- `habeas-corpus` — HC liberatorio, trancamento, relaxamento, excesso de prazo (CF 5 LXVIII; CPP 648).
- `defesa-investigacao-flagrante` — custodia, relaxamento, liberdade provisoria, fianca (CPP 310).
- `resposta-acusacao` — resposta a acusacao + absolvicao sumaria (CPP 396-A / 397).
- `alegacoes-finais` — memoriais/alegacoes finais na instrucao.
- `tribunal-do-juri` — pronuncia/plenario/quesitos.
- `recursos-criminais` — apelacao, RESE, embargos, RHC, superiores.
- `execucao-penal` — beneficios e incidentes da LEP; agravo em execucao.
- `acordos-despenalizadores` — ANPP, transacao, sursis processual.
- `assistencia-de-acusacao` — atuacao pelo polo da vitima/ofendido.

**Tier 3 — Auditoria**
- `revisao-final-criminal` — Suprema Corte do plugin, auditoria R1-R4 (com checagem inegociavel da PA-08).

---

## Os 13 comandos

| Comando | Funcao |
|---|---|
| `/criminal-master` | Mostra a governanca e a config ativa; roteia a demanda. |
| `/triagem` | **Porta de entrada** — triagem em 5 eixos, grava no CASO.md. |
| `/start-criminal` | Wizard de configuracao do plugin no escritorio. |
| `/status-criminal` | Resume o estado: persona, caso ativo, fase/polo, situacao prisional, prazos. |
| `/caso-criminal` | Abre/atualiza o CASO.md do caso ativo (P3). |
| `/revisao-final` | Dispara a auditoria R1-R4 antes da entrega (inclui PA-08). |
| `/habeas-corpus` | Impetra HC — liberdade, trancamento, relaxamento, excesso de prazo. |
| `/flagrante` | Defesa na investigacao/flagrante — custodia, relaxamento, liberdade provisoria, fianca. |
| `/resposta-acusacao` | Resposta a acusacao (CPP 396-A) + absolvicao sumaria. |
| `/juri` | Tribunal do Juri — pronuncia/plenario/quesitos. |
| `/recursos` | Recursos criminais (apelacao, RESE, embargos, RHC, superiores). |
| `/execucao-penal` | Execucao penal (LEP) — progressao, livramento, remicao, agravo. |
| `/acordos` | Acordos despenalizadores (ANPP, transacao, sursis processual). |

---

## Governanca

### 4 Camadas
O `criminal-master` (Tier 0) governa o pipeline em **4 Camadas**: (1) Insumos —
triagem, documentos, jurisprudencia, calculos; (2) Estrategia — trilateral e
linha estrategica; (3) Producao — as peças; (4) Auditoria — R1-R4. Nada e
entregue sem passar pela Camada 4.

### As 13 Proibicoes Absolutas (resumo)
- **PA-01** — nunca alucinar jurisprudencia; citar so o que foi validado.
- **PA-04** — usar a **lei penal vigente no tempo do fato** (CF 5 XL / CP 2); irretroatividade da lei mais gravosa, retroatividade da mais benefica.
- **PA-05** — calcular corretamente a **prescricao penal** (CP 109-110), punitiva e executoria; nao deixar passar.
- **PA-06** — respeitar a **dosimetria trifasica** (CP 68); nada de pena fora do metodo das tres fases.
- **PA-07** — preservar as **garantias constitucionais** (devido processo, contraditorio, ampla defesa, presuncao de inocencia, vedacao da prova ilicita).
- **PA-08** — **vedacao etico-penal inegociavel:** jamais orientar a pratica de crime, a destruicao de prova, a fuga ou a coacao de testemunha. A defesa tecnica nunca vira obstrucao.
- **PA-09** — **sigilo reforcado** da defesa; dado penal sensivel + LGPD; casos gitignored.
- **PA-10** — coerencia de polo (defesa x assistencia); em duvida/contradicao, parar e perguntar.
- **PA-11** — **Selo P1**: toda norma/jurisprudencia passa pela validacao de vigencia.
- **PA-13** — toda entrega passa pela auditoria **R1-R4**.

> A lista completa e operacional vive nas skills `criminal-master` e
> `revisao-final-criminal`; os codigos acima sao os ganchos referenciaveis.
> **PA-08 e PA-04 sao destaque absoluto:** a vedacao etico-penal nunca admite
> bypass, e a lei penal no tempo e a primeira checagem de todo caso.

### Selo P1 e R1-R4
- **Selo de Validacao Legal Previa (P1)** — aplicado na triagem e na revisao:
  nenhuma norma ou precedente entra na peca sem checagem de vigencia e de lei
  penal no tempo (PA-04).
- **Suprema Corte R1-R4** — auditoria obrigatoria em quatro rodadas (R1 dados,
  R2 base juridica, R3 tese, R4 completude) antes de qualquer entrega, com a
  **checagem inegociavel da PA-08**.

---

## Instalacao rapida

Via marketplace `machado-advocacia-marketplace`:

```
/plugin install criminal-adv-os@machado-advocacia-marketplace
```

---

## Fluxo de uso

```
/start-criminal      ->  configura o escritorio (1a vez): persona, fases, polo
/triagem             ->  classifica o caso nos 5 eixos e grava o CASO.md
   (se ha preso)     ->  PRIORIDADE: /habeas-corpus  /flagrante  (liberdade primeiro)
   (producao)        ->  /resposta-acusacao  /juri  /recursos
                         /execucao-penal  /acordos
/revisao-final       ->  auditoria R1-R4 antes de entregar (inclui PA-08)
```

A qualquer momento: `/status-criminal` para ver o estado e `/caso-criminal`
para atualizar o caso ativo. **Havendo pessoa presa, a liberdade vem antes de
tudo.**

---

## Sigilo e dados de cliente — reforcado

Os casos vivem em `criminal/casos/<slug>/` e sao **gitignored** por default —
**sigilo profissional reforcado da defesa + LGPD** (dado penal e dado pessoal
**sensivel**, LGPD art. 11). Nenhum dado de cliente persiste no plugin
distribuido. Se o workspace for pasta sincronizada (OneDrive / iCloud / Google
Drive / Dropbox), o plugin emite **alerta agressivo** (PA-09). Entregas em
**`.txt`** por padrao.

---

## Interface com outros plugins

- **Crimes tributarios (Lei 8.137/90)** — sonegacao, apropriacao indebita
  previdenciaria e correlatos — chegam **de** `tributario-adv-os`, que sinaliza
  o risco penal; a defesa criminal e produzida aqui.
- **Crimes de transito (CTB)** — homicidio e lesao culposa na direcao, embriaguez
  ao volante, fuga do local — chegam **de** `transito-adv-os`; a frente penal
  corre neste plugin.
- **Violencia domestica / Maria da Penha (Lei 11.340/06)** — **interface mutua**
  com `familia-sucessoes-adv-os`: medidas protetivas e o eixo familiar la, a
  frente criminal (acao penal, defesa, assistencia) aqui.

---

**Plugin:** `criminal-adv-os` · padrao Adv-OS · Machado Advocacia · licenca MIT.
