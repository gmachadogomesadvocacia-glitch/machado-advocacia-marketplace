# leiloes-adv-os

> **O plugin do arrematante.** Sistema operacional do advogado que atua por **quem compra** em leilao, no padrao Adv-OS.

---

## Por que existe

Nos 15 plugins do escritorio, o leilao so aparecia de raspao — e sempre pelo angulo da relacao-base: o `imobiliario-adv-os` trata o leilao da Lei 9.514 pelo lado do **devedor fiduciante**, o `civel-adv-os` toca a expropriacao de passagem, o `tributario-adv-os` ve o leilao fiscal pelo lado do **contribuinte executado**.

Ninguem respondia as perguntas de quem **compra**: vale a pena dar o lance neste lote? que divida vem junto? quem esta dentro do imovel e como se tira? o que fazer quando o executado ataca a arrematacao? e quando o proprio arrematante quer desfazer o negocio?

E esse o recorte deste plugin.

---

## O eixo invariante

**O cliente e o arrematante ou o pretendente a arrematante.** Se for o executado, o devedor fiduciante, o exequente ou o credor fiduciario, o plugin **nao redige** — roteia:

| Cliente | Destino |
|---------|---------|
| Executado que quer suspender ou anular | `civel-adv-os` · `tributario-adv-os` · `trabalhista-adv-os` |
| Devedor fiduciante (purgacao, anulacao, saldo) | `imobiliario-adv-os` |
| Exequente conduzindo a expropriacao | plugin do rito |
| Credor fiduciario | `imobiliario-adv-os` |
| Ativo em falencia ou RJ (UPI, art. 142 LRF) | `recuperacao-judicial-adv-os` |

O mesmo leilao gera casos em plugins diferentes conforme o polo. **E o polo que decide, nunca o tema.**

---

## Cobertura

**Via judicial** — expropriacao do CPC (arts. 879 a 908), nos quatro ritos, que **nao** tem os mesmos prazos nem o mesmo piso:

| | CPC | Fiscal (L6.830) | Trabalhista (CLT 888) | SFH (L5.741/71) |
|---|---|---|---|---|
| Edital | 5 dias antes | 10 a 30 dias | **20 dias** | **10 dias** |
| **Lance minimo** | 50% da avaliacao | idem | idem | **o SALDO DEVEDOR** |
| Sinal | — | — | **20% do lance** | conferir edital |
| Pagamento | imediato | — | **24 horas** | conferir edital |

O **rito do SFH inverte a logica do piso**: o minimo e a divida, nao o bem (art. 6º da Lei 5.741/1971). Nao havendo licitante, o juiz adjudica ao credor em 48 horas (art. 7º). Calcular preco vil pelo art. 891 do CPC nesse rito e erro grave.

**Via extrajudicial fiduciaria** — Lei 9.514/97 na redacao da **Lei 14.711/2023**, incluindo a janela do art. 27, § 2º (o credor pode aceitar lance de metade da avaliacao), a blindagem dos §§ 11 e 12 e a reintegracao liminar do art. 30, assegurada expressamente ao adquirente em leilao.

**Fora da v0.1.0:** veiculos, leilao administrativo e aduaneiro, alienacao de ativos em falencia/RJ.

---

## Skill flagship

`due-diligence-lote` — parecer **pre-lance** com seis exames (edital, matricula, debitos, ocupacao, processo de origem, cliente), calculo do **custo real de aquisicao** e veredito fechado:

**ARREMATAR** · **ARREMATAR COM RESSALVA** · **NAO ARREMATAR**

---

## Instalacao

```
/plugin marketplace add gmachadogomesadvocacia-glitch/machado-advocacia-marketplace
/plugin install leiloes-adv-os@machado-advocacia-marketplace
/start-leiloes
```

---

## Commands

`/start-leiloes` · `/status-leiloes` · `/leiloes-master` · `/triagem` · `/caso-leiloes` · `/due-diligence` · `/edital` · `/imissao` · `/defesa-arrematacao` · `/invalidacao` · `/fiduciario` · `/desocupacao` · `/revisao-final`

---

## Skills (20)

**Tier 0** — `leiloes-master`
**Tier 1** — `onboarding-leiloes` · `triagem-leiloes` · `analise-documental-leiloes` · `jurisprudencia-leiloes` · `calculos-leiloes` · `analise-trilateral-leiloes` · `linha-estrategica-leiloes` · `memoria-de-caso-leiloes` · `estilo-juridico-leiloes`
**Tier 2** — `due-diligence-lote` **(flagship)** · `analise-edital-leilao` · `imissao-na-posse-arrematante` · `defesa-da-arrematacao` · `invalidacao-arrematacao` · `leilao-extrajudicial-fiduciario` · `desocupacao-e-ocupantes` · `debitos-e-onus-propter-rem` · `registro-carta-arrematacao`
**Tier 3** — `revisao-final-leiloes`

---

## Base normativa verificada

Toda citacao do plugin vem de curadoria conferida na fonte primaria (Planalto e portal do STJ) em **24/08/2026**:

CPC 879-908 · CTN 130 · CC 1.345, 1.499 e 447-457 · Lei 8.245 art. 8º · Lei 9.514 arts. 26, 26-A, 27, 27-A e 30 · Lei 6.830 arts. 22-24 · CLT 888 · Dec. 21.981/32 art. 24 · Res. CNJ 236/2016 · STJ **Tema 1.134** (com modulacao), **Tema 1.288**, REsp 1.769.443, RMS 65.084, REsp 2.198.525 — e o **Tema 886 sinalizado como em revisao**, com suspensao nacional.

**Dois pontos ficam deliberadamente em aberto**, porque a jurisprudencia nao os fechou: a responsabilidade por **condominio anterior** a arrematacao e **contra quem se volta o arrematante evicto**. O plugin diz isso ao cliente em vez de inventar certeza.

---

## As 13 Proibicoes Absolutas

Detalhadas na skill `leiloes-master`. As que mais mordem:

- **PA-05** — leilao judicial e leilao fiduciario **nao** sao o mesmo regime.
- **PA-06** — nunca afirmar que a arrematacao extingue **todo** onus.
- **PA-07** — nunca prometer resultado ou rentabilidade ao investidor.
- **PA-10** — conferir os impedidos de arrematar (CPC 890, **inclusive advogados das partes**).
- **PA-12** — o polo e sempre quem compra.

---

**Versao:** 0.1.0 · **Licenca:** MIT · **Autor:** Machado Advocacia
