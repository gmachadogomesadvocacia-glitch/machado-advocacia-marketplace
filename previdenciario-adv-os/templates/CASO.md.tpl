# CASO — {{CLIENTE}}

> Ficha do caso previdenciario. Fonte unica das variaveis de **regime**, **especie de
> beneficio**, **fase** e **datas-chave** — todas as skills leem estes campos daqui. Vive em
> `<CASE_ROOT>/{{CASO_SLUG}}/CASO.md`. Pasta unificada do caso, COMPARTILHADA entre os
> plugins Adv-OS: `<CASE_ROOT>/{{CASO_SLUG}}/` com `CASO.md`, `MEMORY.md`, `arquivos/` e
> `pecas/` (pecas em `{{CASO_SLUG}}/pecas/`). Compartimentado por segurado
> (sigilo OAB + LGPD art. 11 — dados sensiveis de saude e contribuicao).

---

## Triagem (triagem-dogmatica)

- **Sujeito:** {{SUJEITO}}
  <!-- segurado | dependente | servidor-publico | empresa — toda tese/pedido/calculo flipa por ele -->
- **Regime:** {{REGIME}}
  <!-- RGPS (INSS, Lei 8.213) | RPPS (servidor, CF art. 40 + lei do ente) | previdencia-complementar
       | acidentario — NUNCA confundir RGPS com RPPS -->
- **Especie de beneficio:** {{ESPECIE}}
  <!-- B41 idade | B42 tempo de contribuicao | B46 especial | B32 invalidez/incapacidade permanente
       | B31 incapacidade temporaria (ex auxilio-doenca) | B91/B94 acidentario | B21 pensao por morte
       | B80 salario-maternidade | BPC/LOAS | revisao de RMI — pode ser mais de um -->
- **Fase:** {{FASE}}
  <!-- administrativa (INSS / CRPS - JR / Camara de Julgamento) | judicial (JEF / JF / vara estadual
       com competencia delegada) — pode haver as duas em sequencia -->
- **Tipo de tarefa:** {{TAREFA}}
  <!-- requerimento administrativo | recurso ao CRPS | peticao inicial | replica | tutela
       | recurso (RO/RE/incidente TNU) | calculo (RMI/atrasados) | revisao | parecer | acordo -->

---

## Partes

| Parte | Qualificacao | Polo | Observacao |
|-------|-------------|------|------------|
| {{PARTE_CLIENTE}} | {{QUALIF_CLIENTE}} | {{SUJEITO}} | cliente |
| {{PARTE_ADVERSA}} | {{QUALIF_ADVERSA}} | {{POLO_ADVERSO}} | {{OBS_ADVERSA}} |

> **Qualidade de segurado e carencia:** verificar manutencao da qualidade de segurado
> (art. 15 Lei 8.213 — periodo de graca) e cumprimento da carencia (art. 25/26) na DER.
> **Dependentes (pensao/BPC):** comprovar dependencia (art. 16) e dependencia economica
> quando exigida.

---

## Dados do Beneficio (do CNIS / carta de concessao-indeferimento)

- **NB (numero do beneficio):** {{NB}}
- **DER (data de entrada do requerimento):** {{DER}}
- **DIB (data de inicio do beneficio):** {{DIB}}
- **DCB (data de cessacao), se houver:** {{DCB}}
- **RMI / RMA:** {{RMI}}
- **CNIS analisado:** {{CNIS_STATUS}}
  <!-- SIM (data) | PENDENTE — nenhum calculo sem CNIS validado -->
- **PPP / LTCAT (especial):** {{PPP_LTCAT}}
  <!-- anexar e validar agentes nocivos; EPI eficaz nao afasta ruido > 85 dB (Tema 555) -->

---

## Localizacao e Competencia (Protocolo P5)

- **Domicilio do segurado:** {{CIDADE}}/{{UF}}
  <!-- Foro do domicilio do segurado — Justica Federal (JEF ate 60 SM); competencia delegada
       a Justica Estadual onde nao houver vara federal. -->
- **Foro / Vara / JEF:** {{FORO}}
- **Processo n.:** {{PROCESSO}}

---

## Validacao de Norma Vigente (EC 103 + marco temporal)

- **Status:** {{SELO_STATUS}}
  <!-- PENDENTE | EMITIDO -->
- **Regra aplicavel (na DER / fato gerador):** {{SELO_NORMAS}}
  <!-- regra vigente na DER: pre-EC 103 (ate 13/11/2019) x EC 103/2019 + regra de transicao especifica;
       Lei 8.213/91 (RGPS) / CF art. 40 + lei do ente (RPPS) / Lei 8.742 (BPC); sumulas/Temas STF/STJ/TNU -->
- **Data:** {{SELO_DATA}}

> Nenhuma skill de producao roda sem a validacao de vigencia da norma. A regra aplicavel e a
> vigente na DER/fato gerador — nunca aplicar a EC 103 retroativamente (conferir filiacao e transicao).

---

## Prazos Criticos

| Tipo | Marco | Vencimento | Observacao |
|------|-------|------------|------------|
| {{PRAZO_TIPO}} | {{PRAZO_MARCO}} | {{PRAZO_FIM}} | {{PRAZO_OBS}} |

<!-- Decadencia: 10 anos para revisao do ato de concessao (art. 103, caput, Lei 8.213).
     Prescricao: parcelas vencidas ha mais de 5 anos (art. 103, par. unico).
     Recurso ao CRPS: 30 dias do indeferimento. Recurso (RO) no JEF: 10 dias.
     Sempre conferir caso a caso. -->

---

## Documentos do caso

{{ARQUIVOS}}

<!-- CNIS, carta de concessao/indeferimento, PPP/LTCAT, CAT e laudos medicos, carteira de trabalho,
     comprovantes de recolhimento (GPS/DARF), documentos de dependencia, autodeclaracao rural.
     Numerados "doc. N". -->

---

## Linha de trabalho / Historico

{{LINHA_TRABALHO}}

<!-- Triagem (regime/especie/fase), validacao de norma, CNIS analisado, tese definida, pecas
     produzidas, requerimento/recurso administrativo protocolado, pericia, sentenca, recurso. -->

---

**Plugin:** `previdenciario-adv-os` v{{PLUGIN_VERSION}}
**Caso aberto em:** {{GENERATED_AT}}
