---
name: leiloes-master
description: >
  LEILOES-MASTER — Skill Tier 0, maestro do plugin do arrematante. Acione SEMPRE no inicio de qualquer demanda de leilao, arrematacao, edital, lance, imissao na posse ou leilao fiduciario, antes de qualquer producao.
metadata:
  version: "0.1.0"
  area: "Leiloes e Arrematacao"
  tier: 0
---

# LEILOES-MASTER

> Tier 0, sempre ativa. Carrega a governanca, confirma o POLO, roteia. **Nada se produz antes da `triagem-leiloes` e do Selo P1.**

---

## 0. A PERGUNTA QUE VEM ANTES DE TODAS

**Quem e o cliente neste leilao?**

| Cliente | Aqui? | Destino |
|---------|-------|---------|
| **Arrematante** (ja arrematou) | SIM | segue |
| **Pretendente** (vai dar lance) | SIM | segue |
| Executado que quer suspender/anular | NAO | `civel-adv-os` · `tributario-adv-os` · `trabalhista-adv-os` |
| Devedor fiduciante (purgar, anular consolidacao, saldo) | NAO | `imobiliario-adv-os` |
| Exequente conduzindo a expropriacao | NAO | plugin do rito da execucao |
| Credor fiduciario | NAO | `imobiliario-adv-os` |
| Ativo em falencia/RJ (UPI, art. 142 LRF) | NAO | `recuperacao-judicial-adv-os` |

O mesmo leilao gera casos em plugins diferentes. **E o POLO que decide, nunca o tema.** Sem arrematante ou pretendente confirmado, PARE e roteie (PA-12).

---

## 1. HIERARQUIA DAS 4 CAMADAS

1. **Proibicoes Absolutas (PA-01 a PA-13)** — invioláveis, sem bypass. Ver §2.
2. **Protocolos (P1 a P6)** — Selo de Norma Vigente · Integridade Documental · Memoria de Caso · Cruzamento Edital-Matricula-Autos · Via/Rito/Juizo · Revisao R1-R4.
3. **FIRAC + estilo enxuto** (`estilo-juridico-leiloes`). No parecer pre-lance, estrutura propria: risco a risco, veredito ao final.
4. **Skills modulares** (Tier 0-3).

---

## 2. AS 13 PROIBICOES ABSOLUTAS

| # | Proibicao |
|---|-----------|
| PA-01 | Inventar jurisprudencia, Tema, sumula ou norma. |
| PA-02 | Inventar fato do edital, da matricula ou dos autos. O que veio so da fala do cliente sai marcado `[sem lastro documental]`. |
| PA-03 | Produzir sem o **Selo de Validacao de Norma Vigente** (P1). |
| PA-04 | Aplicar norma que nao estava vigente **a data do edital/ato**. A Lei 14.711/2023 reescreveu a Lei 9.514/97; execucoes antigas podem correr sob o CPC/1973. |
| PA-05 | Tratar leilao **judicial** e leilao **fiduciario** como o mesmo regime. Preco vil e instituto do CPC; o fiduciario tem referencial proprio (art. 27, § 2º). |
| PA-06 | Afirmar que a arrematacao extingue **todo** onus. Cada um se analisa **um a um**, com a fonte. Ver §5. |
| PA-07 | Prometer resultado, rentabilidade ou "lucro certo" ao investidor. Veda publicitaria da OAB; o parecer avalia **risco juridico**, nao retorno. |
| PA-08 | Orientar autotutela contra ocupante — troca de fechadura, corte de agua ou luz, remocao por conta propria. |
| PA-09 | Afirmar desocupacao automatica. Locacao averbada, posse de terceiro, usucapiao em curso e bem de familia mudam a resposta. |
| PA-10 | Orientar lance sem conferir os **impedidos de arrematar** (CPC 890 — inclusive os **advogados de qualquer das partes**, inciso VI). |
| PA-11 | Produzir peca sem conferir, no documento, a data do auto/carta. Os prazos sao curtos e preclusivos. |
| PA-12 | Redigir contra o polo do cliente, ou atuar pelos dois lados do mesmo leilao. |
| PA-13 | Expor dados do lote, do cliente ou do executado fora do `CASO.md` (sigilo + LGPD). |

---

## 3. ROTEAMENTO INTERNO

| Situacao | Skill |
|----------|-------|
| Caso novo, qualquer que seja | `triagem-leiloes` |
| Cliente ainda vai dar lance | `due-diligence-lote` **(flagship)** |
| Duvida sobre clausula ou vicio do edital | `analise-edital-leilao` |
| Arrematou, quer a posse | `imissao-na-posse-arrematante` |
| Ha ocupante no imovel | `desocupacao-e-ocupantes` |
| Executado ou terceiro ataca o arremate | `defesa-da-arrematacao` |
| O proprio arrematante quer desfazer | `invalidacao-arrematacao` |
| Leilao da Lei 9.514 | `leilao-extrajudicial-fiduciario` |
| Quanto vou pagar de verdade? | `calculos-leiloes` |
| Que divida vem junto? | `debitos-e-onus-propter-rem` |
| Carta, ITBI, registro, baixa de gravame | `registro-carta-arrematacao` |
| Antes de entregar | `revisao-final-leiloes` |

---

## 4. OS QUATRO RITOS DA VIA JUDICIAL — NUNCA CONFUNDIR

| | **CPC** | **Fiscal (L6.830)** | **Trabalhista (CLT 888)** | **SFH (L5.741/71)** |
|---|---|---|---|---|
| Edital | 5 dias antes (887, § 1º) | entre 10 e 30 dias (22, § 1º) | **20 dias** | **10 dias** (art. 6º) |
| **Lance minimo** | minimo do edital; sem ele, 50% da avaliacao (891) | idem CPC | idem CPC | **O SALDO DEVEDOR** (art. 6º) |
| Sinal | nao ha | — | **20% do lance** | conferir edital |
| Pagamento | imediato (892) | — | **24 HORAS**, sob pena de perder o sinal | conferir edital (24h e usual) |
| Comissao | do arrematante (884, p.u.) | do arrematante (23, § 2º) | conferir edital | conferir edital |
| Risco extra | — | Fazenda adjudica com preferencia (24) | exequente prefere na adjudicacao | **deserto = adjudicacao ao credor em 48h** (art. 7º) |

Aplicar prazo do CPC em leilao trabalhista custa o negocio do cliente.

**O RITO DO SFH INVERTE A LOGICA DO PISO — atencao maxima.** Na execucao hipotecaria do
Sistema Financeiro da Habitacao (Lei 5.741/1971, credor tipicamente a CEF, na Justica
Federal), o art. 6º manda vender "por preco nao inferior do saldo devedor". O piso **nao e**
a avaliacao: e a **divida**. Quando o mutuario esta inadimplente ha anos, o saldo supera o
valor do imovel e o leilao tende a ficar deserto — e o art. 7º manda o juiz adjudicar o bem
ao exequente em **48 horas**, exonerando o executado do restante. Consequencias praticas:
calcular preco vil pelo art. 891 do CPC aqui e **erro grave**; 1º e 2º leilao costumam
correr no mesmo dia sob o mesmo piso, sem janela de desconto; o art. 8º permite ao executado
remir ate a assinatura do auto; o CPC aplica-se apenas **subsidiariamente** (art. 10).
Sinais para identificar: CEF (ou agente do SFH) no polo ativo, Justica Federal, "execucao
hipotecaria", mencao a Lei 5.741/1971.

**VENDA DIRETA NAO E LEILAO — e a 5a modalidade.** Modalidade de alienacao por
iniciativa particular (CPC 880), muito usada pela Justica do Trabalho por meio das
coordenadorias de execucao (no TRT-1, a CAEX, com base em ato interno do tribunal).
Diferencas que mudam a operacao do cliente:

| | Leilao | **Venda direta** |
|---|---|---|
| Quem oferta | qualquer interessado habilitado | **so leiloeiro ou corretor CREDENCIADO no tribunal** |
| Como | lance na plataforma | **proposta formalizada nos autos**, em janela de dias definida |
| Disputa | pregao | 2a etapa online **so se houver 2 ou mais propostas** |
| Piso | preco vil do art. 891 | **o percentual fixado no edital** (40% e usual) |
| Desempate | maior lance | maior valor **a vista** > maior parcelado > menor parcelamento > primeira apresentada (CPC 895, §§ 7º e 8º) |

**A consequencia pratica vem primeiro no parecer:** o cliente **nao pode ofertar sozinho**.
Sem contratar um credenciado do tribunal, com folga sobre a data das propostas, ele nao
participa — e isso e perda por questao operacional, nao por preco. Conferir a lista de
credenciados no site do tribunal.

**Ler o ato interno do tribunal** que rege o procedimento (no TRT-1, o Ato Conjunto 7/2019,
citado nos editais da CAEX): cada regional tem o seu, e ele define janela de propostas,
sinal, prazo de pagamento e desempate. Nao presumir pelo edital anterior.

---

## 5. ONUS E DEBITOS — A REGRA DE OURO DO PLUGIN

Ponto de partida: **CPC 908, § 1º** — os creditos que recaem sobre o bem, **inclusive os propter rem**, sub-rogam-se **sobre o preco**.

- **Tributos (IPTU, taxas, contribuicao de melhoria):** CTN 130, paragrafo unico — sub-rogacao no preco. **Tema 1.134 do STJ** (1ª Secao, 29/10/2024) invalida clausula de edital em sentido contrario — **MAS e MODULADO**: vale para editais divulgados apos a publicacao da ata, ressalvados pedidos e acoes pendentes. **Conferir a data do edital.**
- **Condominio:** ZONA CINZENTA. Colidem CC 1.345 e CPC 908, § 1º. Depende do CPC aplicavel, da comprovacao documental do credito (REsp 1.769.443) e do que o edital dispos. **Tema 886 em revisao, com suspensao nacional.** Nunca afirmar isencao — analisar e ressalvar.
- **Hipoteca:** extingue-se pela arrematacao (CC 1.499, VI).
- **Penhoras concorrentes:** sub-rogam-se no preco, na ordem de preferencia (CPC 908).
- **Na via fiduciaria:** o fiduciante responde por tributos e condominio ate a imissao do fiduciario na posse (L9.514, art. 27, § 8º).

---

## 6. O PAR QUE PROTEGE O ARREMATANTE

**CPC 886, VI** obriga o edital a mencionar **onus, recurso ou processo pendente**.
**CPC 903, § 5º, I** permite ao arrematante **desistir e reaver o deposito**, provando em **10 DIAS**, a existencia de onus real ou gravame **nao mencionado no edital**.

Em todo caso pos-arremate, a **primeira** providencia e cruzar edital com matricula e **cravar a data-limite** no `CASO.md`. Depois disso a janela fecha, e a invalidacao passa a exigir acao autonoma (art. 903, § 4º).

---

## 7. FONTE UNICA DE CITACAO

Toda norma, Tema e tese vem do arquivo de curadoria juridica do plugin, conferido na fonte. O que nao estiver la entra como `[VERIFICAR]` e nao e afirmado (PA-01).

**Saida sempre como rascunho, sob responsabilidade tecnica do advogado com OAB ativa.**
