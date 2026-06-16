# CASO — {{CLIENTE}}

> Ficha do caso imobiliario/locaticio. Fonte unica das variaveis de **polo**, **frente**,
> **imovel** e **contrato/demanda** — todas as skills leem estes campos daqui. Vive em
> `<COWORK>/imobiliario/casos/{{CASO_SLUG}}/CASO.md`. Compartimentado por cliente
> (sigilo + LGPD — dados do cliente e do imovel).

---

## Triagem 4D (triagem-imobiliaria)

- **Polo do cliente:** {{POLO}}
  <!-- locador | locatario/inquilino | comprador | vendedor | possuidor | condominio | condomino
       | fiduciante | credor-fiduciario — variavel-mae; toda tese/pedido/tom flipa por ela -->
- **Frente:** {{FRENTE}}
  <!-- locacao (despejo / revisional / renovatoria / consignacao de aluguel / purgacao da mora
                / garantias - fianca/caucao/seguro-fianca)
       | contratos-imobiliarios (compra e venda / promessa / arras-sinal / distrato Lei 13.786
                / vicio redibitorio / eviccao / adjudicacao compulsoria)
       | direitos-reais-posse (possessorias / vizinhanca / condominio edilicio / alienacao
                fiduciaria Lei 9.514 / hipoteca / usucapiao=interface->plugin usucapiao)
       | consultivo (due diligence / analise de matricula / pareceres / contratos) — pode haver mais de uma -->
- **Imovel:** {{IMOVEL}}
  <!-- matricula n. / cartorio de registro de imoveis / endereco / area / tipo (urbano-residencial,
       comercial, terreno, rural). Define o foro da situacao do imovel (art. 47 CPC). -->
- **Contrato:** {{CONTRATO}}
  <!-- tipo (locacao residencial/comercial, compra e venda, promessa de compra e venda, distrato,
       convencao de condominio, alienacao fiduciaria) + DATA de celebracao — define o regime
       juridico aplicavel (Lei 8.245 / CC / Lei 9.514 / Lei 13.786 vigentes na data). -->
- **Tipo de demanda:** {{TAREFA}}
  <!-- despejo | revisional de aluguel | renovatoria | consignacao de aluguel | possessoria
       (reintegracao/manutencao/interdito) | adjudicacao compulsoria | rescisao/distrato
       | cobranca de cota condominial | consolidacao da propriedade/leilao | due diligence
       | parecer | calculo -->

---

## Partes

| Parte | Qualificacao | Polo | Observacao |
|-------|-------------|------|------------|
| {{PARTE_CLIENTE}} | {{QUALIF_CLIENTE}} | {{POLO}} | cliente |
| {{PARTE_ADVERSA}} | {{QUALIF_ADVERSA}} | {{POLO_ADVERSO}} | {{OBS_ADVERSA}} |

> **Legitimidade e titularidade:** conferir quem e o titular do dominio (matricula atualizada) x
> quem detem a posse (situacao de fato). Na locacao, verificar legitimidade do locador (proprietario,
> usufrutuario, administrador) e do fiador/garantidor. Na alienacao fiduciaria, separar fiduciante
> (devedor) de credor fiduciario. **Posse x propriedade x dominio:** a possessoria discute posse,
> nao titulo dominial — nao cumular indevidamente.

---

## Imovel e Contrato (eixo da norma aplicavel)

- **Data de celebracao do contrato / do fato:** {{CONTRATO_DATA}}
  <!-- DEFINE o regime juridico aplicavel. Aplicar a Lei 8.245 / CC / Lei 9.514 / Lei 13.786
       VIGENTES nesta data, nao necessariamente a redacao atual. -->
- **Valor do aluguel / preco / debito em discussao:** {{VALOR_DEBITO}}
- **Garantia locaticia (se houver):** {{GARANTIA}}
  <!-- caucao | fianca | seguro-fianca | cessao fiduciaria — ATENCAO: art. 37, paragrafo unico,
       Lei 8.245 veda CUMULACAO de garantias (so uma modalidade por contrato). -->

---

## Titulo / Constituicao do Direito

- **Matricula / Registro de Imoveis:** {{MATRICULA}}
- **Contrato / Escritura n.:** {{CONTRATO_REF}}
- **Notificacao extrajudicial / consolidacao da propriedade (alienacao fiduciaria):** {{NOTIFICACAO}}
- **Processo judicial n. + vara/orgao:** {{PROCESSO_JUDICIAL}}

---

## Localizacao e Competencia (Protocolo P5)

- **Situacao do imovel:** {{CIDADE}}/{{UF}}
- **Foro / Vara / Registro de Imoveis competente:** {{FORO}}
  <!-- Direitos reais sobre imoveis (possessorias, reivindicatoria, adjudicacao, usucapiao) ->
       foro da SITUACAO DO IMOVEL (art. 47 CPC). Locacao/despejo/cobranca -> foro do contrato /
       eleicao / domicilio. Registro -> registro de imoveis da circunscricao (Lei 6.015/73). -->

---

## Selo de Validacao Legal Previa (P1)

- **Status:** {{SELO_STATUS}}
  <!-- PENDENTE | EMITIDO -->
- **Normas validadas (no contrato/fato):** {{SELO_NORMAS}}
  <!-- Lei 8.245/Lei do Inquilinato + Codigo Civil + Lei 9.514 (alienacao fiduciaria) +
       Lei 13.786 (distrato) + Lei 6.015 (registros) + Lei 4.591 (incorporacao/condominio)
       VIGENTES na data do contrato/fato + sumulas confirmadas (STF/STJ). -->
- **Data:** {{SELO_DATA}}

> Nenhuma skill de producao roda sem o Selo emitido pela `triagem-imobiliaria` (validacao da
> legislacao vigente no contrato/fato + sumulas confirmadas).

---

## Prazos Criticos

| Tipo | Marco | Vencimento | Observacao |
|------|-------|------------|------------|
| {{PRAZO_TIPO}} | {{PRAZO_MARCO}} | {{PRAZO_FIM}} | {{PRAZO_OBS}} |

<!-- Prazo decadencial da RENOVATORIA: ajuizamento entre 1 ano e 6 meses antes do fim do contrato
     (art. 51, paragrafo 5, Lei 8.245) — fatal.
     PURGACAO DA MORA no despejo por falta de pagamento: 15 dias da citacao (art. 62, II, Lei 8.245).
     CONTESTACAO na acao possessoria: 15 dias (rito do CPC; na de forca nova ate 1 ano e dia cabe
     liminar — art. 558 CPC).
     Notificacao premonitoria / denuncia vazia: prazos do art. 46/47 Lei 8.245.
     Alienacao fiduciaria: purgacao da mora apos intimacao para consolidacao (art. 26, Lei 9.514).
     Sempre conferir o prazo no caso concreto. -->

---

## Documentos do caso

{{ARQUIVOS}}

<!-- contrato (locacao/compra e venda/promessa), matricula atualizada, certidoes (onus reais,
     negativas), escritura, comprovantes de pagamento/inadimplencia, notificacoes, convencao de
     condominio, demonstrativo de debito, laudo de vistoria, procuracao. Numerados "doc. N". -->

---

## Linha de trabalho / Historico

{{LINHA_TRABALHO}}

<!-- Triagem, Selo, documentos analisados, tese definida, pecas produzidas, notificacao enviada,
     acao ajuizada (despejo/possessoria/revisional/renovatoria/adjudicacao), liminar, contestacao,
     sentenca/acordao, recurso, situacao do distrato/consolidacao da propriedade. -->

---

**Plugin:** `imobiliario-adv-os` v{{PLUGIN_VERSION}}
**Caso aberto em:** {{GENERATED_AT}}
