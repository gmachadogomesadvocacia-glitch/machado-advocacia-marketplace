# CASO — {{CLIENTE}}

> Ficha do caso civel/processual civel. Fonte unica das variaveis de **polo**, **frente**,
> **relacao juridica/fato** e **demanda** — todas as skills leem estes campos daqui.
> Vive em `<CASE_ROOT>/{{CASO_SLUG}}/CASO.md` (pasta unificada de caso, COMPARTILHADA entre
> os plugins Adv-OS). Estrutura: `CASO.md`, `MEMORY.md`, `arquivos/`, `pecas/` (peças
> produzidas em `{{CASO_SLUG}}/pecas/`). CASE_ROOT = `<acervo>/Casos-Ativos` (Code) ou,
> sem acervo, `<COWORK>/civel/casos` (FALLBACK). Compartimentado por cliente
> (sigilo profissional + LGPD — dados das partes).

---

## Triagem 4D (triagem-civel)

- **Polo do cliente:** {{POLO}}
  <!-- autor (credor | lesado | demandante) | reu (devedor | causador do dano | demandado)
       — variavel-mae; toda tese/pedido/tom flipa por ela -->
- **Frente:** {{FRENTE}}
  <!-- responsabilidade-civil-indenizatorias (ato ilicito / dano moral-material-estetico /
                dano emergente-lucro cessante / nexo causal / responsabilidade objetiva /
                acidente de transito-DPVAT-regresso-seguradora / responsabilidade civil do Estado CF 37 par. 6)
       | contratos-obrigacoes (inadimplemento / mora / clausula penal / distrato-rescisao /
                revisao contratual / vicio redibitorio-eviccao / negocio juridico-vicios do consentimento)
       | cobranca-execucao (acao de cobranca / monitoria / execucao de titulo extrajudicial -
                cheque-nota promissoria-duplicata / busca e apreensao-alienacao fiduciaria DL 911)
       | obrigacoes-tutelas (obrigacao de fazer-nao fazer-dar / tutela provisoria de urgencia-evidencia /
                liminar / consignacao em pagamento)
       — pode haver mais de uma -->
- **Relacao juridica / fato:** {{RELACAO_JURIDICA}}
  <!-- fonte da pretensao: contrato (qual), ato ilicito (qual evento), titulo de credito (qual).
       Define a norma aplicavel (CC/CPC) e o regime (contratual x extracontratual). -->
- **Devedor / Causador do dano / Demandado:** {{REU}}
  <!-- qualificacao da parte adversa conforme a frente: devedor (contratos/cobranca),
       causador do dano (responsabilidade civil), demandado (tutelas). -->
- **Valor / Quantum pretendido:** {{QUANTUM_PRETENDIDO}}
  <!-- valor do debito (cobranca/execucao) | quantum indenizatorio (dano emergente + lucro cessante +
       dano moral/estetico) | valor da obrigacao (tutelas). Base do valor da causa. -->
- **Tipo de demanda:** {{TAREFA}}
  <!-- acao de cobranca | acao monitoria | execucao de titulo extrajudicial | busca e apreensao |
       acao indenizatoria | revisao/rescisao contratual | obrigacao de fazer/nao fazer/dar |
       tutela de urgencia/evidencia | consignacao em pagamento | contestacao | parecer |
       calculo de quantum/juros/correcao -->

---

## Partes

| Parte | Qualificacao | Polo | Observacao |
|-------|-------------|------|------------|
| {{PARTE_CLIENTE}} | {{QUALIF_CLIENTE}} | {{POLO}} | cliente |
| {{PARTE_ADVERSA}} | {{QUALIF_ADVERSA}} | {{POLO_ADVERSO}} | {{OBS_ADVERSA}} |

> **Legitimidade:** confirmar a legitimidade ativa (titular do direito — credor/lesado) e passiva
> (devedor/causador do dano/responsavel solidario). Na responsabilidade civil do Estado, a **Fazenda
> Publica** (CF 37, par. 6); na de transito, a seguradora (DPVAT/regresso). **Coerencia de polo:** o
> plugin produz a peca do lado do cliente, nunca contra ele.

---

## Relacao Juridica e Pretensao (eixo da norma aplicavel)

- **Data do fato / celebracao do contrato:** {{DATA_FATO}}
  <!-- DEFINE a norma aplicavel: conferir o direito intertemporal (CC/2002 x Codigo Civil de 1916
       e leis anteriores). Tambem fixa o termo inicial de prescricao e de juros/correcao. -->
- **Fundamento juridico / regime:** {{FUNDAMENTO}}
  <!-- contratual (CC 389 e ss.) x extracontratual/aquiliana (CC 186, 187, 927); responsabilidade
       subjetiva (culpa) x objetiva (risco, CC 927 par. unico; CF 37 par. 6). -->
- **Quantum / valor da obrigacao:** {{QUANTUM}}
  <!-- discriminar: dano emergente + lucro cessante + dano moral/estetico (responsabilidade civil);
       principal + juros + correcao (cobranca/execucao); valor da obrigacao (tutelas). -->

---

## Marcos Processuais e Materiais

- **Data do fato / inadimplemento:** {{DATA_INADIMPLEMENTO}}
- **Vencimento / mora:** {{DATA_MORA}}
- **Notificacao / interpelacao / protesto:** {{DATA_NOTIFICACAO}}
- **Citacao:** {{DATA_CITACAO}}
- **Sentenca / acordao em:** {{DATA_SENTENCA}}
- **Processo n. + vara/orgao:** {{PROCESSO_JUDICIAL}}

---

## Localizacao e Competencia (Protocolo P5)

- **Domicilio do reu / lugar do ato-fato / cumprimento da obrigacao:** {{CIDADE}}/{{UF}}
- **Foro / Vara civel / Juizado especial competente:** {{FORO}}
  <!-- Regra geral: domicilio do reu (art. 46 CPC). Responsabilidade civil -> lugar do ato/fato
       (art. 53, IV, CPC). Contratos -> lugar do cumprimento da obrigacao. Fazenda Publica federal ->
       Justica Federal (art. 109 CF). Ate 40 SM -> juizado especial civel (Lei 9.099). -->

---

## Selo de Validacao Legal Previa (P1)

- **Status:** {{SELO_STATUS}}
  <!-- PENDENTE | EMITIDO -->
- **Normas validadas (no fato/contrato):** {{SELO_NORMAS}}
  <!-- Codigo Civil (CC) + Codigo de Processo Civil (CPC) VIGENTES na data do fato/contrato
       (direito intertemporal — CC/2002 x institutos anteriores) + sumulas STF/STJ confirmadas
       (ex.: Sum. 54 e Sum. 362 STJ — juros; Sum. 37 STJ — cumulacao dano moral e material). -->
- **Data:** {{SELO_DATA}}

> Nenhuma skill de producao roda sem o Selo emitido pela `triagem-civel` (validacao da legislacao
> vigente ao fato/contrato + direito intertemporal + sumulas confirmadas).

---

## Prazos Criticos

| Tipo | Marco | Vencimento | Observacao |
|------|-------|------------|------------|
| {{PRAZO_TIPO}} | {{PRAZO_MARCO}} | {{PRAZO_FIM}} | {{PRAZO_OBS}} |

<!-- CONTESTACAO: 15 dias uteis (art. 335 CPC), contados conforme art. 335 I-III.
     EMBARGOS A ACAO MONITORIA: 15 dias uteis (art. 702 CPC).
     EMBARGOS A EXECUCAO: 15 dias uteis (art. 915 CPC).
     APELACAO: 15 dias uteis para interpor e arrazoar (art. 1003 par. 5 / 1009 CPC).
     EMBARGOS DE DECLARACAO: 5 dias uteis (art. 1023 CPC).
     PRESCRICAO: regra geral 10 anos (CC 205); especiais no CC 206 (ex.: 3 anos para reparacao
       civil — art. 206 par. 3 V; 5 anos para divida liquida em instrumento — art. 206 par. 5 I).
     DECADENCIA: prazos legais/convencionais (ex.: vicio redibitorio — CC 445).
     Sempre conferir o prazo no caso concreto e o termo inicial. -->

---

## Documentos do caso

{{ARQUIVOS}}

<!-- contrato e aditivos, titulo de credito (cheque/nota promissoria/duplicata), comprovantes de
     pagamento, notificacao/interpelacao/protesto, boletim de ocorrencia (transito), orcamentos e
     notas fiscais (dano material), laudos, prova do dano e do nexo, demonstrativo de debito
     atualizado, procuracao. Numerados "doc. N". -->

---

## Linha de trabalho / Historico

{{LINHA_TRABALHO}}

<!-- Triagem, Selo, documentos analisados, tese definida (existencia/extensao do dano, nexo causal,
     culpa/dolo, inadimplemento, prescricao/decadencia, revisao de clausulas), pecas produzidas,
     tutela de urgencia, citacao, contestacao, instrucao, sentenca/acordao, recurso, cumprimento de
     sentenca/execucao. -->

---

**Plugin:** `civel-adv-os` v{{PLUGIN_VERSION}}
**Caso aberto em:** {{GENERATED_AT}}
