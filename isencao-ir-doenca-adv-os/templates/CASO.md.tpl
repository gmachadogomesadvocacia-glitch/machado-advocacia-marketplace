# CASO — {{CLIENTE}}

> Ficha do caso de isencao de IRPF por doenca grave. Fonte unica das variaveis de **polo**,
> **doenca**, **via**, **esfera** e **tipo de provento** — todas as skills leem estes campos
> daqui. Vive em `<COWORK>/isencao-ir/casos/{{CASO_SLUG}}/CASO.md`. Compartimentado por cliente
> (sigilo OAB + LGPD — dado de saude e SENSIVEL, art. 11).

---

## Triagem 4D (triagem-isencao-ir)

- **Polo do cliente:** {{POLO}}
  <!-- contribuinte/beneficiario (aposentado/pensionista/reformado) | Fazenda/fonte pagadora
       — variavel-mae; toda tese/pedido/tom flipa por ela -->
- **Doenca grave (lista art. 6, XIV, Lei 7.713/88):** {{DOENCA}}
  <!-- neoplasia maligna (cancer) | cardiopatia grave | cegueira | doenca de Parkinson |
       esclerose multipla | nefropatia grave | hepatopatia grave | AIDS/SIDA | hanseniase |
       paralisia irreversivel e incapacitante | espondiloartrose anquilosante | fibrose cistica |
       doenca de Paget (osteite deformante) | contaminacao por radiacao | alienacao mental |
       tuberculose ativa — DEVE estar na lista taxativa do dispositivo -->
- **CID:** {{CID}}
- **Data do laudo / diagnostico:** {{DATA_LAUDO}}
  <!-- laudo de servico medico oficial (Uniao/Estado/Municipio) ou prova suficiente da doenca
       (Sumula 598 STJ). O ADVOGADO NAO OPINA sobre a conduta clinica nem a gravidade — o laudo e do medico. -->
- **Fonte pagadora:** {{FONTE_PAGADORA}}
  <!-- INSS | RPPS (servidor) | fundo de pensao / previdencia complementar | ex-empregador -->
- **Tipo de provento:** {{TIPO_PROVENTO}}
  <!-- aposentadoria | pensao | reforma — a isencao SO alcanca proventos; NAO se estende a
       rendimentos de trabalho ATIVO (Sumula 627 STJ) -->
- **Via:** {{VIA}}
  <!-- administrativa (cessar retencao na fonte + retificar DIRPF) | judicial (acao declaratoria de
       isencao + repeticao de indebito) | mandado de seguranca -->
- **Esfera:** {{ESFERA}}
  <!-- administrativa (Receita Federal / fonte pagadora) | judicial (Justica Federal)
       — pode haver 2 em paralelo (Protocolo P4) -->
- **Tipo de tarefa:** {{TAREFA}}
  <!-- requerimento administrativo | acao declaratoria + repeticao | mandado de seguranca |
       replica | recurso | calculo de restituicao | parecer -->

---

## Partes

| Parte | Qualificacao | Polo | Observacao |
|-------|-------------|------|------------|
| {{PARTE_CLIENTE}} | {{QUALIF_CLIENTE}} | {{POLO}} | cliente (contribuinte) |
| {{PARTE_ADVERSA}} | {{QUALIF_ADVERSA}} | {{POLO_ADVERSO}} | {{OBS_ADVERSA}} (Uniao/Fazenda Nacional + fonte pagadora) |

> **Enquadramento (Selo P1):** verificar (a) doenca na lista taxativa do art. 6, XIV; (b) provento
> de aposentadoria/pensao/reforma (nao ativo — Sumula 627); (c) prova da doenca (Sumula 598).

---

## Periodo de Retencao e Restituicao

- **Inicio da retencao indevida:** {{INICIO_RETENCAO}}
  <!-- normalmente a partir da data do laudo / diagnostico da doenca grave -->
- **Valor retido (base p/ restituicao):** {{VALOR_RETIDO}}
- **Periodo restituivel:** {{PERIODO_RESTITUIVEL}}
  <!-- ultimos 5 anos — prescricao quinquenal do indebito (CTN art. 168) -->

---

## Localizacao e Competencia (Protocolo P5)

- **Domicilio do contribuinte:** {{CIDADE}}/{{UF}}
  <!-- Foro da Justica Federal do domicilio do contribuinte — art. 109, §2º CF. -->
- **Foro / Vara / JEF:** {{FORO}}
  <!-- Juizado Especial Federal (ate 60 SM) x vara federal comum. -->
- **Processo n.:** {{PROCESSO}}

---

## Selo de Validacao de Norma Vigente (P1)

- **Status:** {{SELO_STATUS}}
  <!-- PENDENTE | EMITIDO -->
- **Normas validadas:** {{SELO_NORMAS}}
  <!-- Validacao de Norma Vigente (Lei 7.713/88 art. 6 XIV + IN RFB 1500 + Sum. 598/627 STJ) -->
- **Data:** {{SELO_DATA}}

> Nenhuma skill de producao roda sem o Selo emitido pela `triagem-isencao-ir`.

---

## Prazos Criticos

| Tipo | Marco | Vencimento | Observacao |
|------|-------|------------|------------|
| {{PRAZO_TIPO}} | {{PRAZO_MARCO}} | {{PRAZO_FIM}} | {{PRAZO_OBS}} |

<!-- Prescricao da restituicao: quinquenal — ultimos 5 anos (CTN art. 168). MS: 120 dias do ato
     coator. Recursos JEF: 10 dias. Retificacao da DIRPF: dentro do prazo decadencial. Sempre conferir. -->

---

## Documentos do caso

{{ARQUIVOS}}

<!-- laudo de servico medico oficial / laudo pericial, CID, carta de concessao do beneficio,
     informe de rendimentos da fonte pagadora, DIRPF, comprovantes de retencao (IRRF),
     extratos de pagamento. Numerados "doc. N". DADO DE SAUDE = SENSIVEL (LGPD art. 11). -->

---

## Linha de trabalho / Historico

{{LINHA_TRABALHO}}

<!-- Triagem, Selo, documentos analisados, tese definida, requerimento administrativo protocolado,
     resposta da fonte/Receita, acao ajuizada, sentenca, restituicao calculada. -->

---

**Plugin:** `isencao-ir-doenca-adv-os` v{{PLUGIN_VERSION}}
**Caso aberto em:** {{GENERATED_AT}}
