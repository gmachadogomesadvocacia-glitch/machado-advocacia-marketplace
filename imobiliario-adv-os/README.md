# imobiliario-adv-os

**O sistema operacional do advogado imobiliarista brasileiro**, no padrao **Adv-OS**.

`imobiliario-adv-os` e um plugin do Claude Code que transforma o assistente num
operador de Direito Imobiliario e de Locacao disciplinado: faz a triagem do caso,
valida a norma vigente no contrato/fato, separa posse de propriedade, monta a
estrategia, redige a peca e audita tudo antes da entrega. Side-aware: produz a
peca **do lado do cliente** — locador x locatario, comprador x vendedor,
possuidor x esbulhador, condominio x condomino, fiduciante x credor fiduciario.

---

## O que ele cobre — 4 frentes

| Frente | O que faz |
|---|---|
| **Locacao** | Lei 8.245/91 — despejo por falta de pagamento (+ purgacao art. 62), denuncia vazia, infracao contratual; revisional de aluguel (art. 19); renovatoria (art. 51, prazo decadencial §5º); consignatoria de aluguel/chaves; garantias locaticias (vedada a cumulacao — art. 37). |
| **Contratos imobiliarios** | Promessa de compra e venda, arras, distrato/rescisao (Lei 13.786/2018), vicios redibitorios, eviccao, adjudicacao compulsoria (Sum. 239 STJ). |
| **Direitos reais e posse** | Acoes possessorias (reintegracao / manutencao / interdito — forca nova x velha); condominio edilicio e cobranca de cotas (propter rem); alienacao fiduciaria de imovel (Lei 9.514/97 — purgacao da mora, consolidacao, leilao). |
| **Consultivo** | Due diligence imobiliaria, revisao e minuta de contratos, regularizacao dominial/edilicia. |

> **Usucapiao = interface.** Tratada como roteamento para `usucapiao-adv-os`, nao como frente propria.

---

## As 20 skills (por Tier)

**Tier 0 — Governanca**
- `imobiliario-master` — orquestracao central, 4 Camadas, roteamento.

**Tier 1 — Insumos e estrategia**
- `onboarding-imobiliario` — wizard de configuracao do escritorio.
- `triagem-imobiliaria` — porta de entrada, 5 eixos + Selo de Validacao Legal Previa (P1).
- `analise-documental-imobiliaria` — matricula, contrato, notificacoes, certidoes.
- `jurisprudencia-imobiliaria` — pesquisa e validacao de jurisprudencia (PA-01).
- `calculos-imobiliarios` — debito locaticio, atualizacao, multas, cotas.
- `analise-trilateral-imobiliaria` — cliente x adversario x julgador.
- `linha-estrategica-imobiliaria` — define a tese central e as subsidiarias.
- `memoria-de-caso-imobiliario` — CASO.md compartimentado (P3).
- `estilo-juridico-imobiliario` — peca enxuta, docs numerados, tom do escritorio.

**Tier 2 — Producao**
- `despejo` — despejo + cobranca de alugueis (Lei 8.245; liminar art. 59).
- `renovatoria-revisional` — renovatoria (art. 51 §5º) e revisional (art. 19).
- `acoes-possessorias` — reintegracao / manutencao / interdito.
- `cobranca-condominial` — cotas condominiais propter rem.
- `compra-venda-promessa-distrato` — promessa, arras, distrato (Lei 13.786), vicios.
- `adjudicacao-compulsoria` — outorga de escritura/registro (Sum. 239 STJ).
- `alienacao-fiduciaria-imovel` — Lei 9.514/97, purgacao, leilao.
- `consignatoria-locaticia` — consignacao de aluguel/chaves.
- `due-diligence-imobiliaria` — due diligence e revisao de contratos.

**Tier 3 — Auditoria**
- `revisao-final-imobiliaria` — Suprema Corte do plugin, auditoria R1-R4.

---

## Os 13 comandos

| Comando | O que faz | Skill |
|---|---|---|
| `/imobiliario-master` | Governanca Tier 0, mostra config e roteia | `imobiliario-master` |
| `/triagem` | Porta de entrada — 5 eixos, grava no CASO.md | `triagem-imobiliaria` |
| `/start-imobiliario` | Wizard de configuracao do escritorio | `onboarding-imobiliario` |
| `/status-imobiliario` | Resumo do estado e do caso ativo | `memoria-de-caso-imobiliario` |
| `/caso-imobiliario` | Abre/atualiza o CASO.md (P3) | `memoria-de-caso-imobiliario` |
| `/revisao-final` | Auditoria R1-R4 antes da entrega | `revisao-final-imobiliaria` |
| `/despejo` | Despejo e cobranca de alugueis | `despejo` |
| `/renovatoria` | Renovatoria e revisional | `renovatoria-revisional` |
| `/possessoria` | Acoes possessorias | `acoes-possessorias` |
| `/condominio` | Cobranca de cotas condominiais | `cobranca-condominial` |
| `/compra-venda` | Promessa, arras, distrato, vicios | `compra-venda-promessa-distrato` |
| `/fiduciaria` | Alienacao fiduciaria de imovel | `alienacao-fiduciaria-imovel` |
| `/due-diligence` | Due diligence e revisao de contrato | `due-diligence-imobiliaria` |

---

## Governanca

**4 Camadas.** Toda demanda atravessa: (1) Identidade/persona, (2) Triagem +
Selo de Validacao Legal Previa, (3) Producao especializada, (4) Auditoria R1-R4.

**13 Proibicoes Absolutas (resumo).**
- **PA-01** — nunca citar lei/jurisprudencia sem validar; lacuna = `[INFORMAR]`.
- **PA-04** — aplicar a **norma vigente no contrato/fato**, nao a superveniente.
- **PA-05** — nao confundir **posse x propriedade x dominio** (armadilha central).
- **PA-06** — liminar de despejo **so** nas hipoteses do **art. 59 §1º + caucao**.
- **PA-07** — respeitar o **prazo decadencial da renovatoria (art. 51 §5º)**.
- **PA-08** — **cumulacao de garantias locaticias vedada (art. 37)**.
- **PA-09** — respeitar o **rito proprio da alienacao fiduciaria (Lei 9.514/97)**.
- **PA-10** — coerencia de **polo**: produzir sempre do lado do cliente.
- **PA-11** — **Selo P1**: norma e jurisprudencia validadas quanto a vigencia.
- **PA-13** — **R1-R4** obrigatorios antes de entregar.

**Selo de Validacao Legal Previa (P1).** A triagem valida a norma vigente no
contrato/fato antes de qualquer producao.

**Suprema Corte (R1-R4).** Auditoria final em 4 rodadas; reprovacao em qualquer
rodada bloqueia a entrega.

---

## Instalacao rapida

Via marketplace `machado-advocacia-marketplace`:

```
/plugin install imobiliario-adv-os@machado-advocacia-marketplace
```

---

## Fluxo de uso

```
/start-imobiliario   ->  configura o escritorio (persona, frentes, polos)
/triagem             ->  classifica o caso nos 5 eixos, grava no CASO.md
/despejo | /renovatoria | /possessoria | /condominio
/compra-venda | /fiduciaria | /due-diligence   ->  producao
/revisao-final       ->  auditoria R1-R4 antes de entregar
```

A qualquer momento: `/status-imobiliario` (estado) e `/caso-imobiliario` (memoria).

---

## Sigilo e LGPD

A pasta `imobiliario/casos/` e **gitignored** — dados de clientes, matriculas,
contratos e documentos nunca entram no plugin distribuido (sigilo OAB + LGPD).
O `/start-imobiliario` alerta quando o workspace e pasta sincronizada
(OneDrive/iCloud/Google Drive/Dropbox). A persona do escritorio vive em
`<cwd>/imobiliario/persona.md`, fora do plugin.

---

## Interfaces (roteamento para outros plugins)

| Situacao | Roteia para |
|---|---|
| Usucapiao (regularizacao por posse) | `usucapiao-adv-os` |
| IPTU/ITBI ja em execucao fiscal | `tributario-adv-os` |
| Imovel na planta / relacao de consumo (CDC) | `consumidor-adv-os` |
| Partilha / inventario do imovel | `familia-sucessoes-adv-os` |
