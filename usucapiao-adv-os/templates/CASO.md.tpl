# CASO — {{CLIENTE}}

> Ficha do caso de usucapiao. Fonte unica das variaveis de **polo**, **via**,
> **modalidade** e **esfera/rito** — todas as skills leem estes campos daqui. Vive em
> `<COWORK>/usucapiao/casos/{{CASO_SLUG}}/CASO.md`. Compartimentado por cliente
> (sigilo OAB + LGPD).

---

## Triagem 4D (triagem-usucapiao)

- **Polo do cliente:** {{POLO}}
  <!-- usucapiente (autor/requerente) | confrontante/oponente (defesa) — variavel-mae;
       toda tese/pedido/tom flipa por ela -->
- **Via:** {{VIA}}
  <!-- judicial (acao de usucapiao) | extrajudicial/cartorio (usucapiao administrativa —
       CPC art. 1.071 + Lei 6.015 art. 216-A + Provimento CNJ) -->
- **Modalidade:** {{MODALIDADE}}
  <!-- extraordinaria (CC art. 1.238) | ordinaria (CC art. 1.242) | especial urbana
       (CC art. 1.240 / CF art. 183) | especial rural (CC art. 1.239 / CF art. 191) |
       familiar (CC art. 1.240-A) | coletiva (Estatuto da Cidade — Lei 10.257 art. 10) -->
- **Esfera:** {{ESFERA}}
  <!-- judicial | extrajudicial (cartorio/RI) — pode migrar do cartorio p/ o judicial
       se houver impugnacao de confrontante (Protocolo P4) -->
- **Tipo de tarefa:** {{TAREFA}}
  <!-- peticao inicial | requerimento de usucapiao extrajudicial | contestacao/impugnacao |
       replica | tutela | recurso | parecer | ata notarial (minuta de requisitos) -->

---

## Partes

| Parte | Qualificacao | Polo | Observacao |
|-------|-------------|------|------------|
| {{PARTE_CLIENTE}} | {{QUALIF_CLIENTE}} | {{POLO}} | cliente |
| {{PARTE_ADVERSA}} | {{QUALIF_ADVERSA}} | {{POLO_ADVERSO}} | {{OBS_ADVERSA}} |

> **Citacao/anuencia obrigatoria:** confrontantes (e respectivos conjuges), titular(es)
> registral(is), e os entes publicos — **Uniao, Estado e Municipio** (CPC art. 246 §3).
> Reus em lugar incerto: edital (CPC art. 259, III). No extrajudicial, anuencia expressa
> dos confrontantes e titulares (silencio = discordancia, salvo Provimento CNJ aplicavel).

---

## Imovel

- **Natureza:** {{IMOVEL_NATUREZA}}
  <!-- urbano | rural -->
- **Registro:** {{IMOVEL_REGISTRO}}
  <!-- com matricula (n. ____ no RI de ____) | sem registro/sem matricula (imovel nao
       matriculado — abrir matricula) -->
- **Metragem:** {{IMOVEL_METRAGEM}}
  <!-- area total; conferir teto da modalidade: 250 m2 (especial urbana/familiar) /
       50 hectares (especial rural) -->
- **Confrontantes:** {{IMOVEL_CONFRONTANTES}}
  <!-- Norte / Sul / Leste / Oeste — nome e qualificacao de cada confinante -->
- **Dominialidade:** {{IMOVEL_DOMINIALIDADE}}
  <!-- particular | PUBLICO/terra devoluta (NAO usucapivel — Sumula 340 STF;
       CF art. 183 §3 e 191 par. unico) — afastar de plano -->

---

## Posse (posse ad usucapionem)

- **Inicio da posse:** {{POSSE_INICIO}}
- **Tempo de posse:** {{POSSE_TEMPO}}
  <!-- conferir o prazo da modalidade (15/10/5/2 anos); soma de posses — accessio possessionis -->
- **Justo titulo?** {{POSSE_JUSTO_TITULO}}
  <!-- exigido na ordinaria (art. 1.242). Ex.: contrato de compra e venda nao registrado,
       escritura, cessao de direitos -->
- **Boa-fe?** {{POSSE_BOA_FE}}
  <!-- exigida na ordinaria. Presumida com justo titulo -->
- **Animus domini:** {{POSSE_ANIMUS}}
  <!-- posse como dono — afastar deteccao/comodato/locacao (posse precaria nao usucape) -->
- **Atos possessorios:** {{POSSE_ATOS}}
  <!-- IPTU/ITR em nome do possuidor, contas de consumo, benfeitorias/construcao, moradia,
       cultivo, cercamento, declaracoes de vizinhos. Numerados "doc. N" -->

---

## Localizacao e Competencia (Protocolo P5)

- **Situacao do imovel:** {{CIDADE}}/{{UF}}
  <!-- Foro da situacao do imovel — art. 47 CPC (rei sitae). No extrajudicial, RI da
       circunscricao do imovel — Lei 6.015 art. 216-A. -->
- **Foro / Vara / RI:** {{FORO}}
  <!-- vara civel/registros publicos competente OU Registro de Imoveis da circunscricao.
       Conferir deslocamento p/ Justica Federal se houver interesse da Uniao/autarquia/EP -->
- **Entes a citar/notificar:** {{ENTES_CITAR}}
  <!-- Uniao + Estado + Municipio (manifestacao de interesse no imovel) -->
- **Processo n. / Protocolo:** {{PROCESSO}}

---

## Selo de Validacao de Norma Vigente (P1)

- **Status:** {{SELO_STATUS}}
  <!-- PENDENTE | EMITIDO -->
- **Normas validadas:** {{SELO_NORMAS}}
  <!-- CC arts. 1.238-1.244 + CF 183/191 + CPC (246 §3, 259 III, 1.071) + Lei 6.015 art. 216-A
       + Provimento CNJ vigente + sumulas/Temas (STF 340/237; STJ 11) -->
- **Data:** {{SELO_DATA}}

> Nenhuma skill de producao roda sem o Selo emitido pelo `usucapiao-master`
> (Validacao de Norma Vigente — CC + CPC + Lei 6.015 + Provimento CNJ).

---

## Prazos Criticos

| Tipo | Marco | Vencimento | Observacao |
|------|-------|------------|------------|
| {{PRAZO_TIPO}} | {{PRAZO_MARCO}} | {{PRAZO_FIM}} | {{PRAZO_OBS}} |

<!-- Prazo de posse cumprido na data do ajuizamento/requerimento. Impugnacao/manifestacao
     dos entes e confrontantes. Resposta a edital. Prazos recursais. Sempre conferir. -->

---

## Documentos do caso

{{ARQUIVOS}}

<!-- matricula/certidao do RI, planta e memorial descritivo (com ART e responsavel tecnico),
     ata notarial, comprovantes de posse (IPTU/ITR, contas, fotos, benfeitorias), justo titulo
     (contrato/escritura/cessao), declaracoes de confrontantes, certidoes negativas. Numerados "doc. N". -->

---

## Linha de trabalho / Historico

{{LINHA_TRABALHO}}

<!-- Triagem, Selo, documentos analisados, modalidade definida, via escolhida (judicial x
     cartorio), planta/ata providenciadas, peca/requerimento produzido, citacoes/anuencias,
     impugnacao, sentenca/registro. -->

---

**Plugin:** `usucapiao-adv-os` v{{PLUGIN_VERSION}}
**Caso aberto em:** {{GENERATED_AT}}
