# civel-adv-os

Sistema operacional do advogado brasileiro de **Direito Civil e Processo Civil — o CÍVEL RESIDUAL**, no padrão Adv-OS (mesmo chassi de `direito-medico-adv-os`, `trabalhista-adv-os` e `consumidor-adv-os`).

**Residual** é a palavra-chave: este plugin cobre o que **não** está nos plugins especializados do escritório. Ele não invade consumo, família/sucessões, responsabilidade médica, imobiliário, usucapião, fiscal, criminal, trabalho ou INSS — quando a demanda pertence a um desses ramos, o plugin **roteia** para o plugin próprio (Proibição Absoluta **PA-09**, o cardeal do sistema).

Atende os **dois polos** da relação civil — **autor** (credor / lesado / demandante) × **réu** (devedor / causador do dano / demandado) — com orquestrador side-aware, triagem por 5 eixos, governança de 4 Camadas, Selo de Validação Legal Prévia e Suprema Corte R1-R4 sobre toda entrega. Persona resolvida em runtime via `/start-civel`.

---

## As 4 frentes

| Frente | Cobre |
|--------|-------|
| **Responsabilidade civil & indenizatórias** | Ato ilícito (CC 186/187/927), dano moral/material/estético, nexo, culpa × responsabilidade objetiva, quantum, acidente de trânsito (DPVAT/regresso), responsabilidade civil do Estado (CF 37 §6º) |
| **Contratos & obrigações civis** | Teoria geral, contratos típicos (prestação de serviço, mútuo, comodato, mandato, doação, fiança civil), inadimplemento, revisão/rescisão, anulação de negócio jurídico (erro, dolo, coação, lesão, estado de perigo, simulação, fraude — CC 138-184) |
| **Cobrança & execução** | Ação de cobrança, monitória (CPC 700), execução de título extrajudicial (CPC 784), busca e apreensão (DL 911/69) |
| **Obrigações & tutelas** | Obrigações de fazer/não fazer/dar, tutela provisória de urgência/evidência, consignação em pagamento, defesa cível / contestação |

Um caso pode cruzar frentes em paralelo (ex.: rescisão contratual + indenização por perdas e danos; cobrança + tutela de urgência) — o `civel-master` coordena (Protocolo P4 — Cruzamento Relação-Pretensão-Execução).

---

## Arquitetura — triagem por 5 eixos

A `triagem-civel` é a porta de entrada. Antes de tudo, o **passo zero (PA-09):** *é cível residual?* Se não for, roteia ao plugin próprio. Sendo cível, classifica em 5 eixos:

| Eixo | Valores |
|------|---------|
| **Frente** | responsabilidade civil & indenizatórias · contratos & obrigações · cobrança & execução · obrigações & tutelas |
| **Polo** | autor (credor/lesado/demandante) × réu (devedor/causador/demandado) — variável-mãe |
| **Relação / fato** | contratual × extracontratual; norma vigente à época do fato/contrato |
| **Valor** | estimativa da causa — JEC até 40 SM × vara cível comum |
| **Prazo** | prescrição × decadência (CC 205/206) |

---

## Skills (20, por Tier)

- **Tier 0 — Orquestração**
  `civel-master` (4 Camadas, 13 Proibições Absolutas, Protocolos, roteamento)
- **Tier 1 — Insumos (9)**
  `onboarding-civel` · `triagem-civel` · `analise-documental-civel` · `jurisprudencia-civel` · `calculos-civeis` · `analise-trilateral-civel` · `linha-estrategica-civel` · `memoria-de-caso-civel` · `estilo-juridico-civel`
- **Tier 2 — Produção (9)**
  `responsabilidade-civil` · `acidente-transito-civel` · `contratos-civeis` · `anulacao-negocio-juridico` · `cobranca-monitoria` · `execucao-titulo-extrajudicial` · `obrigacoes-e-tutelas` · `defesa-civel` · `responsabilidade-estado`
- **Tier 3 — Auditoria (1)**
  `revisao-final-civel` (Suprema Corte R1-R4)

---

## Commands (13)

Governança e fluxo: `/civel-master` · `/triagem` · `/start-civel` · `/status-civel` · `/caso-civel` · `/revisao-final`

Núcleos de produção diretos: `/responsabilidade-civil` · `/acidente-transito` · `/contratos` · `/anulatoria` · `/cobranca` · `/execucao` · `/resp-estado`

---

## Governança — as 4 Camadas

```
CAMADA 1 — PROIBIÇÕES ABSOLUTAS (PA-04 a PA-13)  — invioláveis
CAMADA 2 — PROTOCOLOS TÉCNICOS                    — obrigatórios
CAMADA 3 — IDENTIDADE FIRAC + ESTILO              — enxuto / humanizado
CAMADA 4 — SKILLS (Tier 0-3)                       — operacional
```

A camada superior sempre prevalece — inclusive contra o usuário. Injetada pela skill `civel-master`.

### 13 Proibições Absolutas (destaques)

- **PA-04 — Norma vigente** no fato/contrato (não aplicar lei posterior retroativamente).
- **PA-05 — Prescrição × decadência** (CC 205/206) — eixo crítico; nunca confundir os regimes.
- **PA-06 — Liquidação do dano e juros** — Súm. 54 STJ (extracontratual: do evento) e Súm. 362 STJ (moral: do arbitramento).
- **PA-07 — Responsabilidade contratual × extracontratual** — qualificar antes de redigir.
- **PA-08 — Via / pedido adequado** — monitória × cobrança × execução, conforme o título.
- **PA-09 — CÍVEL RESIDUAL / roteamento** — *não redigir matéria de outro plugin*; rotear. (Cardeal do sistema.)
- **PA-10 — Polo** (autor × réu) coerente em toda a peça.
- **PA-11 — Selo P1** (Validação Legal Prévia) antes de qualquer produção.
- **PA-13 — Revisão R1-R4** obrigatória antes da entrega.

> **Selo de Validação Legal Prévia (P1):** nenhuma skill de produção roda sem o selo da triagem.
> **Suprema Corte R1-R4:** R1 dados/escopo · R2 base jurídica · R3 tese · R4 completude/entrega. Reprovação em qualquer rodada bloqueia a entrega.

---

## Instalação rápida

Via marketplace `machado-advocacia-marketplace`:

```
/plugin install civel-adv-os@machado-advocacia-marketplace
```

## Fluxo de uso

1. `/start-civel` — configura o escritório (advogado, OAB/UF, firma, cidade/UF, e-mail, tom, frentes, polos). Gera `civel/persona.md` + `config.md` + `casos/` e aponta `CIV_PERSONA` no `settings.local.json`.
2. `/triagem` — porta de entrada: confirma que é cível residual (PA-09) e classifica nos 5 eixos → grava o `CASO.md`.
3. **Produção** — peça pelo núcleo correspondente (`/responsabilidade-civil`, `/contratos`, `/cobranca`, etc.).
4. `/revisao-final` — auditoria R1-R4 antes de entregar.

---

## Fronteiras / interfaces — o que NÃO entra (e para onde vai)

O caráter **residual** é operacionalizado por PA-09. Quando a demanda principal for de outro ramo, o plugin roteia:

| Se a demanda é de… | Vai para |
|--------------------|----------|
| Relação de **consumo** (CDC) | `consumidor-adv-os` |
| **Família / sucessões** | `familia-sucessoes-adv-os` |
| **Responsabilidade médica / odontológica** | `direito-medico-adv-os` |
| **Locação / posse / imóvel** | `imobiliario-adv-os` |
| **Usucapião** | `usucapiao-adv-os` |
| **Fiscal / tributário** | `tributario-adv-os` |
| **Crime** | `criminal-adv-os` |
| **Trabalho** | `trabalhista-adv-os` |
| **INSS / previdenciário** | `previdenciario-adv-os` |

> O cível residual cobre o **interstício** entre esses ramos. Em casos mistos (ex.: contrato civil com pano de fundo de consumo), a `triagem-civel` decide o eixo dominante e, quando necessário, coordena a interface sem duplicar o trabalho do plugin especializado.

---

## Sigilo & LGPD

A pasta `civel/casos/` é **gitignored** — dados de cliente nunca entram no plugin distribuído nem em pasta sincronizada sem ciência. Compartimentação por caso (sigilo OAB + LGPD). O `/start-civel` alerta se o workspace for pasta sincronizada (OneDrive / iCloud / Google Drive).

---

Uso interno — Machado Advocacia. Side-aware: **autor × réu**. Saída padrão em `.txt`.
