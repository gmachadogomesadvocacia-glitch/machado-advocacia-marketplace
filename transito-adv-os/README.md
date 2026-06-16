# transito-adv-os

**O sistema operacional do advogado de transito brasileiro**, no padrao **Adv-OS**.

`transito-adv-os` e um plugin do Claude Code que transforma o assistente num
operador de Direito de Transito disciplinado, focado em **recursos de multas e
defesa da CNH**: faz a triagem do caso, valida a norma de transito vigente na data
da infracao, identifica os vicios do auto, monta a estrategia, redige a peca e
audita tudo antes da entrega. **Foco absoluto na defesa do condutor/proprietario.**
No transito nao ha "outro lado" simetrico — o Estado autua e o plugin atua na
**defesa** (condutor x proprietario do veiculo; variante: indicacao do real condutor).

> **Atencao ao prazo:** as vias administrativas tem **prazo preclusivo de 30 dias**.
> Perdido o prazo, perde-se a instancia (PA-05). A triagem trata o prazo como
> prioridade maxima.

---

## Base legal

- **CTB — Codigo de Transito Brasileiro** (Lei 9.503/1997).
- **Lei 14.071/2020** — novo regime de pontuacao (20/30/40 pontos conforme a
  presenca de infracao gravissima) e suspensao do direito de dirigir.
- **Resolucoes CONTRAN** — requisitos do auto, equipamentos/radar, notificacoes,
  processos de suspensao e cassacao.
- **Sumula 312 STJ** — exigencia da **dupla notificacao** (da autuacao e da
  penalidade) sob pena de nulidade (PA-07).
- **Lei 12.016/2009** (mandado de seguranca) e **Dec. 20.910/1932** (prescricao
  quinquenal contra a Fazenda) na via judicial.

---

## Os 3 eixos + analise

| Eixo | O que faz |
|---|---|
| **Administrativo** | Defesa previa da autuacao (CTB 281-282), recurso a **JARI** (1a instancia) e a **CETRAN/CONTRANDIFE** (2a instancia). |
| **CNH** | Defesa nos processos de **suspensao** do direito de dirigir (pontuacao/autossuspensiva) e de **cassacao** da CNH + reabilitacao; **indicacao do real condutor** (CTB 257 §7o). |
| **Judicial** | **Acao anulatoria** de multa/auto/penalidade e **mandado de seguranca** contra ato de autoridade de transito (vicio formal, liminar). |
| **Analise** | Analise documental e de **vicios do auto de infracao** (requisitos CTB 280, equipamento/radar, dupla notificacao, tempestividade). |

---

## As 20 skills (por Tier)

**Tier 0 — Governanca**
- `transito-master` — orquestracao central, 4 Camadas, roteamento.

**Tier 1 — Insumos e estrategia**
- `onboarding-transito` — wizard de configuracao do escritorio.
- `triagem-transito` — porta de entrada, 5 eixos + Selo de Validacao Legal Previa (P1).
- `analise-documental-transito` — leitura do auto, das notificacoes e dos autos do processo.
- `jurisprudencia-transito` — pesquisa e validacao de jurisprudencia (PA-01).
- `calculos-transito` — contagem de pontos, valores da multa, prazos e prescricao.
- `analise-trilateral-transito` — condutor x orgao autuador x julgador (JARI/CETRAN/juiz).
- `linha-estrategica-transito` — define a tese central e as subsidiarias.
- `memoria-de-caso-transito` — CASO.md compartimentado (P3), sigilo + LGPD.
- `estilo-juridico-transito` — peca enxuta, docs numerados, tom do escritorio.

**Tier 2 — Producao**
- `analise-vicios-auto-infracao` — nulidades formais e materiais do auto.
- `defesa-autuacao` — defesa previa da autuacao (CTB 281-282).
- `recursos-administrativos` — recurso a JARI e a CETRAN/CONTRANDIFE.
- `suspensao-direito-dirigir` — defesa no processo de suspensao (CTB 261).
- `cassacao-cnh` — defesa na cassacao (CTB 263) e reabilitacao.
- `indicacao-condutor` — indicacao do real condutor infrator (CTB 257 §7o).
- `anulatoria-transito` — acao anulatoria judicial.
- `mandado-seguranca-transito` — MS contra ato de autoridade de transito.
- `defesa-radar-equipamentos` — vicios de afericao/calibracao de equipamentos e radares.

**Tier 3 — Auditoria**
- `revisao-final-transito` — Suprema Corte do plugin, auditoria R1-R4 (com checagem inegociavel da PA-06).

---

## Os 13 comandos

| Comando | O que faz |
|---|---|
| `/transito-master` | Governanca central (Tier 0): 4 Camadas, config e roteamento. |
| `/triagem` | Porta de entrada — triagem em 5 eixos, grava no CASO.md, roteia para o Selo P1. |
| `/start-transito` | Wizard de configuracao do escritorio (persona, eixos, tom). |
| `/status-transito` | Resumo do estado: persona, caso ativo, eixo/fase, pontuacao, prazos. |
| `/caso-transito` | Abre/retoma/atualiza o CASO.md do caso ativo (P3). |
| `/defesa-autuacao` | Defesa previa da autuacao (CTB 281-282; prazo 30 dias). |
| `/recurso` | Recursos administrativos JARI (1a) e CETRAN (2a). |
| `/cnh-suspensao` | Defesa no processo de suspensao do direito de dirigir. |
| `/cnh-cassacao` | Defesa na cassacao da CNH + reabilitacao. |
| `/indicar-condutor` | Indicacao do real condutor (CTB 257 §7o) — so o condutor real (PA-06). |
| `/anulatoria` | Acao anulatoria judicial de multa/auto/penalidade. |
| `/mandado-seguranca` | MS contra ato de autoridade de transito (vicio formal; liminar). |
| `/revisao-final` | Auditoria R1-R4 antes da entrega (obrigatoria por default). |

---

## Governanca

O plugin opera sob **4 Camadas de Governanca** e **13 Proibicoes Absolutas (PA)**,
resumidas:

- **PA-04** — sempre a **norma vigente na data da infracao**, nunca a posterior.
- **PA-05** — respeitar os **prazos administrativos preclusivos (30 dias)**: vencido o
  prazo, perde-se a instancia. Tratada como prioridade na triagem.
- **PA-06** — **NUNCA orientar fraude de pontuacao ou indicacao falsa de condutor**
  (crime de falsidade ideologica, art. 299 CP). A defesa legitima jamais vira fraude.
  Invariante inegociavel — sem bypass.
- **PA-07** — exigir a **dupla notificacao** (autuacao + penalidade) sob pena de
  nulidade (Sumula 312 STJ).
- **PA-08** — **nao confundir as instancias** (administrativa JARI/CETRAN x judicial;
  defesa previa x recurso x suspensao x cassacao).
- **PA-09** — **crime de transito** (embriaguez, homicidio/lesao culposa) -> `criminal-adv-os`.
- **PA-10** — polo de **defesa** do condutor/proprietario; em duvida, parar e perguntar.
- **PA-11** — **Selo P1**: validar a vigencia de toda norma e jurisprudencia citada.
- **PA-13** — **Revisao R1-R4** obrigatoria antes da entrega.

A `revisao-final-transito` audita em 4 rodadas (R1 dados, R2 base juridica, R3 tese,
R4 completude) e a checagem da PA-06 e inegociavel.

---

## Instalacao rapida

Via marketplace `machado-advocacia-marketplace`:

```
/plugin install transito-adv-os@machado-advocacia-marketplace
```

Depois, configure o escritorio com `/start-transito`.

---

## Fluxo de uso

1. **`/start-transito`** — configura a persona, os eixos e o tom (so na 1a vez).
2. **`/triagem <descricao do caso>`** — classifica e grava o CASO.md. **Atencao ao
   prazo de 30 dias** — a triagem prioriza a preclusao (PA-05).
3. **Producao** — `/defesa-autuacao`, `/recurso`, `/cnh-suspensao`, `/cnh-cassacao`,
   `/indicar-condutor`, `/anulatoria` ou `/mandado-seguranca`, conforme o eixo/fase.
4. **`/revisao-final`** — auditoria R1-R4 antes de entregar.

---

## Sigilo e LGPD

A pasta de casos `transito/casos/` guarda dados pessoais do condutor (CPF, CNH,
enderecos) e e **gitignored** por padrao (sigilo profissional OAB + LGPD). Se o
workspace estiver em pasta sincronizada (OneDrive/iCloud/Google Drive/Dropbox), o
plugin alerta sobre o tratamento desses dados. Nenhum dado de cliente persiste no
plugin distribuido.

---

## Interfaces com outros plugins

O foco de `transito-adv-os` e a **defesa administrativa e judicial do condutor/
proprietario**. Demandas conexas seguem para os plugins proprios:

- **Crime de transito** — embriaguez ao volante (art. 306 CTB), homicidio/lesao
  culposa na direcao (arts. 302/303 CTB), racha, fuga -> **`criminal-adv-os`** (PA-09).
- **Reparacao civil do acidente / DPVAT** — danos materiais e morais decorrentes
  do sinistro, cobranca de seguro obrigatorio -> **`civel-adv-os`**.
