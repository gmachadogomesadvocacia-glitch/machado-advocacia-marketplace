# CASO — {{CLIENTE}}

> Ficha do caso de leilao/arrematacao. Fonte unica das variaveis de **polo**, **via**,
> **fase**, **dados do lote** e **demanda** — todas as skills leem estes campos daqui.
> Vive em `<CASE_ROOT>/{{CASO_SLUG}}/CASO.md` — estrutura unificada
> (CASO.md, MEMORY.md, arquivos/, pecas/), pasta COMPARTILHADA entre plugins do mesmo
> cliente; pecas produzidas em `{{CASO_SLUG}}/pecas/`. Compartimentado por cliente
> (sigilo profissional + LGPD — dados do cliente, do lote e do executado).

---

## Triagem 4D (triagem-leiloes)

- **Polo do cliente:** {{POLO}}
  <!-- arrematante consumado | pretendente a arrematante (pre-lance)
       — variavel-mae. O plugin so atua por quem COMPRA. Executado, devedor fiduciante,
       exequente e credor fiduciario NAO sao atendidos aqui: rotear (PA-12). -->
- **Via:** {{FRENTE}}
  <!-- judicial (expropriacao CPC 879-903, em execucao civel, fiscal ou trabalhista)
       | extrajudicial fiduciario (Lei 9.514/97 arts. 26, 26-A, 27 e 30) -->
- **Rito da execucao (so na via judicial):** {{RELACAO_JURIDICA}}
  <!-- civel/CPC | fiscal (Lei 6.830/80) | trabalhista (CLT 888) | SFH (Lei 5.741/71)
       DECISIVO: os tres ritos tem prazos e exigencias DIFERENTES para o arrematante
       (publicacao do edital, sinal, prazo de pagamento, preferencias). Nunca aplicar
       prazo do CPC em leilao trabalhista. -->
- **Fase:** {{FASE}}
  <!-- pre-lance (due diligence) | arrematado sem carta | carta expedida sem posse |
       posse obtida com litigio residual | desfazimento (invalidacao/eviccao/restituicao) -->
- **Obstaculo principal:** {{OBSTACULO}}
  <!-- onus e debitos | ocupacao do imovel | vicio do edital ou da intimacao |
       ataque do executado a arrematacao | inadimplemento do proprio arrematante -->
- **Tipo de demanda:** {{TAREFA}}
  <!-- parecer de viabilidade pre-lance | analise de edital | imissao na posse |
       defesa da arrematacao | invalidacao/desistencia | acao de eviccao |
       desocupacao | registro da carta | calculo do custo real de aquisicao -->

---

## Partes

| Parte | Qualificacao | Polo | Observacao |
|-------|-------------|------|------------|
| {{PARTE_CLIENTE}} | {{QUALIF_CLIENTE}} | {{POLO}} | cliente (arrematante/pretendente) |
| {{PARTE_ADVERSA}} | {{QUALIF_ADVERSA}} | {{POLO_ADVERSO}} | {{OBS_ADVERSA}} |

> **Impedidos de arrematar (CPC 890) — CONFERIR ANTES DE QUALQUER LANCE ORIENTADO:**
> tutores, curadores, testamenteiros, administradores e liquidantes quanto aos bens sob
> sua guarda; mandatarios; juiz, MP, Defensoria, escrivao e servidores da justica na
> localidade onde servem; servidores publicos quanto a bens do ente; leiloeiros e seus
> prepostos; **e os ADVOGADOS DE QUALQUER DAS PARTES** (inciso VI). Arrematacao por
> impedido e nula e o prejuizo e do cliente (PA-10).

---

## O Lote

- **Bem:** {{BEM}}
  <!-- imovel: matricula, RI, endereco, area; movel/veiculo: identificacao. -->
- **Avaliacao / lance pretendido ou dado:** {{QUANTUM}}
- **Piso do lance:** {{PRECO_VIL}}
  <!-- CPC/fiscal/trabalhista: vil = inferior ao MINIMO do edital; sem minimo, inferior a 50%
       da avaliacao (CPC 891). SFH (L5.741/71): o piso e o SALDO DEVEDOR (art. 6º), nao a
       avaliacao — anotar os DOIS numeros e a razao saldo/avaliacao. Fiduciaria: nao ha preco
       vil; vale o referencial do art. 27, § 2º. -->
- **Saldo devedor (rito SFH):** {{SALDO_DEVEDOR}}
  <!-- so no rito da Lei 5.741/71. Se saldo > avaliacao, a arrematacao por terceiro e
       inviavel e o desfecho provavel e a adjudicacao ao credor em 48h (art. 7º). -->
- **Onus e gravames na matricula:** {{ONUS}}
  <!-- hipoteca (extingue-se pela arrematacao — CC 1.499, VI), penhoras concorrentes,
       usufruto, indisponibilidade, alienacao fiduciaria, servidao. Um a um, com a fonte. -->
- **Debitos que acompanham o bem:** {{DEBITOS}}
  <!-- IPTU/taxas: CTN 130, par. unico — sub-rogacao no PRECO; Tema 1.134 STJ invalida
       clausula de edital em sentido contrario, MAS e MODULADO por data do edital.
       CONDOMINIO: zona cinzenta — depende do CPC aplicavel, da comprovacao documental do
       credito e do que o edital dispos; Tema 886 EM REVISAO. Nunca afirmar isencao. -->
- **Ocupacao:** {{OCUPACAO}}
  <!-- desocupado | executado e familia | locatario (conferir clausula de vigencia
       AVERBADA — L8.245 art. 8º) | posseiro | usucapiente. Nao ha desocupacao
       automatica (PA-09) e nao se orienta autotutela (PA-08). -->

---

## O Edital (documento-chave)

- **Data de divulgacao do edital:** {{DATA_EDITAL}}
  <!-- CRITICA: define a aplicacao da modulacao do Tema 1.134 (tributos). -->
- **Datas do 1º e do 2º leilao:** {{DATAS_LEILAO}}
- **Preco minimo fixado:** {{PRECO_MINIMO}}
- **Comissao do leiloeiro prevista:** {{COMISSAO}}
  <!-- o edital manda. Faixa provavel: 5% (RMS 65.084, julgado isolado) x 3% para imoveis
       na falta de estipulacao (Dec. 21.981/32 art. 24). Na execucao fiscal, art. 23, § 2º,
       da LEF poe a comissao no arrematante. -->
- **O edital MENCIONA os onus, recurso ou processo pendente (CPC 886, VI)?** {{EDITAL_ONUS}}
  <!-- SE NAO MENCIONOU e existe onus real ou gravame: o arrematante pode DESISTIR e
       reaver o deposito, provando em 10 DIAS (CPC 903, § 5º, I). Cravar a data-limite. -->
- **Condicoes especiais impostas pelo edital:** {{EDITAL_CONDICOES}}

---

## Marcos e Prazos Criticos

| Tipo | Marco | Vencimento | Observacao |
|------|-------|------------|------------|
| {{PRAZO_TIPO}} | {{PRAZO_MARCO}} | {{PRAZO_FIM}} | {{PRAZO_OBS}} |

- **Data do auto de arrematacao:** {{DATA_AUTO}}
- **Data da carta de arrematacao:** {{DATA_CARTA}}

<!-- PRAZOS DA VIA JUDICIAL (CPC):
     - invalidacao/ineficacia/resolucao: 10 dias apos o aperfeicoamento (art. 903, § 2º);
     - desistencia por onus nao mencionado no edital: 10 dias (art. 903, § 5º, I);
     - apos a carta, invalidacao so por ACAO AUTONOMA, com o arrematante como
       litisconsorte necessario (art. 903, § 4º).
     RITO FISCAL (LEF): edital entre 10 e 30 dias antes do leilao (art. 22, § 1º).
     RITO TRABALHISTA (CLT 888): edital com 20 dias de antecedencia; sinal de 20% do
       lance; pagamento do preco em 24 HORAS sob pena de perder o sinal.
     VIA FIDUCIARIA (L9.514): purgacao em 15 dias (art. 26, § 1º); leilao em 60 dias da
       consolidacao (art. 27); reintegracao liminar com 60 dias para desocupar (art. 30). -->

---

## Selo de Validacao de Norma Vigente (P1)

- **Status:** {{SELO_STATUS}}
  <!-- PENDENTE | EMITIDO -->
- **Normas validadas (vigentes a data do edital/ato):** {{SELO_NORMAS}}
  <!-- CPC 879-908 + CTN 130 + CC 1.345/1.499 + L8.245 art. 8º, ou L9.514 arts. 26/26-A/27/30
       na redacao da Lei 14.711/2023; mais Tema 1.134 (modulado), Tema 1.288 e o estado do
       Tema 886 (em revisao). Fonte unica: CURADORIA-juridica-leiloes. -->
- **Data:** {{SELO_DATA}}

> Nenhuma skill de producao roda sem o Selo emitido pela `triagem-leiloes`.

---

## Esfera e Competencia (Protocolo P5)

- **Juizo / cartorio do leilao:** {{FORO}}
  <!-- via judicial: o juizo da execucao onde corre a expropriacao (civel, fiscal ou
       trabalhista). via fiduciaria: o registro de imoveis da circunscricao do imovel;
       o litigio vai ao foro da situacao do imovel. -->
- **Localizacao do bem:** {{CIDADE}}/{{UF}}

---

## Documentos do caso

{{ARQUIVOS}}

<!-- edital completo, matricula atualizada e certidao de onus, laudo de avaliacao, auto e
     carta de arrematacao, comprovante do lance e do deposito, certidoes negativas
     (municipal, condominio, distribuidor), fotos e diligencia do imovel, comprovante da
     comissao. Numerados "doc. N". -->

---

## Linha de trabalho / Historico

{{LINHA_TRABALHO}}

<!-- Triagem, Selo, edital cruzado com a matricula, calculo do custo real, veredito do
     parecer pre-lance, lance, arrematacao, prazos cravados, pecas produzidas, decisoes. -->

---

**Plugin:** `leiloes-adv-os` v{{PLUGIN_VERSION}}
**Caso aberto em:** {{GENERATED_AT}}
