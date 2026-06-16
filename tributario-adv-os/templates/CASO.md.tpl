# CASO — {{CLIENTE}}

> Ficha do caso tributario. Fonte unica das variaveis de **polo**, **frente**,
> **esfera** e **tributo/demanda** — todas as skills leem estes campos daqui. Vive em
> `<COWORK>/tributario/casos/{{CASO_SLUG}}/CASO.md`. Compartimentado por cliente
> (sigilo fiscal — art. 198 CTN + LGPD).

---

## Triagem 4D (triagem-tributaria)

- **Polo do cliente:** {{POLO}}
  <!-- contribuinte / sujeito passivo | fazenda-publica — variavel-mae; toda tese/pedido/tom flipa por ela -->
- **Frente:** {{FRENTE}}
  <!-- administrativa (impugnacao / recurso CARF/TIT/conselho / PAF Dec. 70.235/72)
       | judicial (embargos a execucao fiscal / excecao de pre-executividade / anulatoria
                   / declaratoria / mandado de seguranca / repeticao de indebito / compensacao
                   / consignacao)
       | consultiva (planejamento / parcelamento / transacao) — pode haver mais de uma -->
- **Esfera:** {{ESFERA}}
  <!-- federal (IR/IRPJ/IRPF/IPI/PIS/COFINS/CSLL/IOF/ITR/contribuicoes)
       | estadual (ICMS/IPVA/ITCMD) | municipal (ISS/IPTU/ITBI) -->
- **Tributo:** {{TRIBUTO}}
  <!-- qual tributo em discussao — ICMS / ISS / IR / IRPJ / IPTU / ITBI / ITCMD / PIS-COFINS / etc. -->
- **Tipo de demanda:** {{TAREFA}}
  <!-- impugnacao | recurso CARF/TIT | embargos a execucao fiscal | excecao de pre-executividade
       | anulatoria | declaratoria | mandado de seguranca | repeticao de indebito | compensacao
       | consignacao | planejamento | parcelamento | transacao | parecer | calculo -->

---

## Partes

| Parte | Qualificacao | Polo | Observacao |
|-------|-------------|------|------------|
| {{PARTE_CLIENTE}} | {{QUALIF_CLIENTE}} | {{POLO}} | cliente |
| {{PARTE_ADVERSA}} | {{QUALIF_ADVERSA}} | {{POLO_ADVERSO}} | {{OBS_ADVERSA}} |

> **Sujeicao passiva e responsabilidade:** verificar se o cliente e contribuinte (relacao
> pessoal e direta com o fato gerador — art. 121, I CTN) ou responsavel (art. 121, II + 128 ss).
> Em redirecionamento de execucao fiscal, conferir art. 135 CTN (excesso de poder/infracao) e
> Sumula 435 STJ (dissolucao irregular). Ilegitimidade passiva = tese central da defesa do socio.

---

## Fato Gerador (eixo da norma aplicavel)

- **Data do fato gerador:** {{FATO_GERADOR_DATA}}
  <!-- DEFINE a norma aplicavel. Sempre aplicar a legislacao vigente NESTA data, nao a atual.
       Atencao a transicao da Reforma Tributaria (CBS/IBS — EC 132/2023 + LC 214/2025;
       convivencia de regimes 2026-2033). -->
- **Base de calculo / aliquota discutidas:** {{BASE_ALIQUOTA}}
- **Valor do debito/credito:** {{VALOR_DEBITO}}

---

## Lancamento / Constituicao do Credito

- **Auto de infracao / lancamento n.:** {{AUTO_INFRACAO}}
- **CDA (certidao de divida ativa) n.:** {{CDA}}
- **Processo administrativo n. + orgao:** {{PROCESSO_ADMINISTRATIVO}}
- **Processo judicial n. + vara/orgao:** {{PROCESSO_JUDICIAL}}

---

## Localizacao e Competencia (Protocolo P5)

- **Domicilio do contribuinte:** {{CIDADE}}/{{UF}}
- **Foro / Vara de execucoes fiscais / Orgao administrativo:** {{FORO}}
  <!-- Execucao fiscal federal -> JF; ICMS/IPVA/ITCMD -> vara estadual / Fazenda Publica estadual;
       ISS/IPTU/ITBI -> vara da Fazenda Publica municipal. Administrativo -> DRJ/CARF, TIT,
       conselho de contribuintes do ente. -->

---

## Selo de Validacao de Norma Vigente (P1)

- **Status:** {{SELO_STATUS}}
  <!-- PENDENTE | EMITIDO -->
- **Normas validadas (no fato gerador):** {{SELO_NORMAS}}
  <!-- CTN + lei do tributo (LC/lei ordinaria do ente) + regulamento (RICMS/RIR/etc.)
       + sumulas/Temas STF-STJ + posicao CARF/TIT. Atencao a vigencia NA DATA do fato gerador
       e a transicao da Reforma (EC 132/LC 214). -->
- **Data:** {{SELO_DATA}}

> Nenhuma skill de producao roda sem o Selo emitido pela `triagem-tributaria` (validacao de
> norma vigente no fato gerador).

---

## Prazos Criticos

| Tipo | Marco | Vencimento | Observacao |
|------|-------|------------|------------|
| {{PRAZO_TIPO}} | {{PRAZO_MARCO}} | {{PRAZO_FIM}} | {{PRAZO_OBS}} |

<!-- Decadencia do lancamento: 5 anos (art. 173, I CTN; art. 150 §4 para homologacao).
     Prescricao da cobranca: 5 anos da constituicao definitiva (art. 174 CTN); intercorrente
     na execucao fiscal (art. 40 LEF + Sumula 314 + Tema 566 STJ). Impugnacao administrativa:
     30 dias (Dec. 70.235/72, federal). Recurso ao CARF: 30 dias. Embargos a execucao fiscal:
     30 dias da intimacao da penhora (art. 16 LEF). MS: 120 dias do ato coator. Sempre conferir. -->

---

## Documentos do caso

{{ARQUIVOS}}

<!-- auto de infracao, lancamento, CDA, decisao administrativa, citacao da execucao, guias,
     escrituracao fiscal/contabil, notas fiscais, contratos, comprovantes de recolhimento,
     procuracao. Numerados "doc. N". -->

---

## Linha de trabalho / Historico

{{LINHA_TRABALHO}}

<!-- Triagem, Selo, documentos analisados, tese definida, pecas produzidas, impugnacao/recurso
     protocolado, embargos opostos, sentenca/acordao, recurso, situacao do parcelamento/transacao. -->

---

**Plugin:** `tributario-adv-os` v{{PLUGIN_VERSION}}
**Caso aberto em:** {{GENERATED_AT}}
