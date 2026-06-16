# CASO — {{CLIENTE}}

> Ficha do caso consumerista. Fonte unica das variaveis de **polo**, **eixo**,
> **esfera** e **rito** — todas as skills leem estes campos daqui. Vive em
> `<CASE_ROOT>/{{CASO_SLUG}}/CASO.md` — pasta unificada e COMPARTILHADA entre os
> plugins Adv-OS, com a estrutura `<CASE_ROOT>/{{CASO_SLUG}}/` { CASO.md, MEMORY.md,
> arquivos/, pecas/ } (pecas em `{{CASO_SLUG}}/pecas/`). Compartimentado por cliente
> (sigilo OAB + LGPD — PA-21).

---

## Triagem 4D (triagem-consumidor)

- **Polo do cliente:** {{POLO}}
  <!-- consumidor | fornecedor — variavel-mae; toda tese/pedido/tom flipa por ela (PA-05) -->
- **Eixo:** {{EIXO}}
  <!-- bancario | negativacao | telecom | servicos-essenciais | aereo | vicio-fato-produto
       | e-commerce | publicidade | clausula-abusiva | cobranca-indevida
       | superendividamento | consumo-imobiliario — pode ser mais de um -->
- **Esfera:** {{ESFERA}}
  <!-- judicial | administrativa (PROCON/consumidor.gov.br/BACEN/ANATEL/ANAC) | extrajudicial
       — pode haver 2+ em paralelo (Protocolo P4) -->
- **Rito:** {{RITO}}
  <!-- JEC (ate 40 SM, Lei 9.099) | vara civel comum | acao coletiva -->
- **Tipo de tarefa:** {{TAREFA}}
  <!-- peticao inicial | contestacao | replica | tutela | recurso | calculo
       | reclamacao administrativa | acordo | parecer -->

---

## Partes

| Parte | Qualificacao | Polo | Observacao |
|-------|-------------|------|------------|
| {{PARTE_CLIENTE}} | {{QUALIF_CLIENTE}} | {{POLO}} | cliente |
| {{PARTE_ADVERSA}} | {{QUALIF_ADVERSA}} | {{POLO_ADVERSO}} | {{OBS_ADVERSA}} |

> **Relacao de consumo (PA-04):** verificar destinatario final + vulnerabilidade
> (art. 2/3 CDC — finalista mitigada). Se PJ-insumo, justificar a vulnerabilidade
> ou afastar o CDC.

---

## Localizacao e Competencia (Protocolo P5)

- **Domicilio do consumidor:** {{CIDADE}}/{{UF}}
  <!-- Foro do domicilio do consumidor — art. 101, I CDC (competencia em favor do vulneravel). -->
- **Foro / Vara / JEC:** {{FORO}}
- **Processo n.:** {{PROCESSO}}

---

## Selo de Validacao Legal Previa (P1)

- **Status:** {{SELO_STATUS}}
  <!-- PENDENTE | EMITIDO -->
- **Normas validadas:** {{SELO_NORMAS}}
  <!-- CDC + lei especial (Lei 9.656 / ANATEL / ANAC / L14.181) + sumulas/Temas STJ -->
- **Data:** {{SELO_DATA}}

> Nenhuma skill de producao roda sem o Selo emitido pelo `validador-legislacao-consumidor`.

---

## Prazos Criticos

| Tipo | Marco | Vencimento | Observacao |
|------|-------|------------|------------|
| {{PRAZO_TIPO}} | {{PRAZO_MARCO}} | {{PRAZO_FIM}} | {{PRAZO_OBS}} |

<!-- Decadencia: vicio aparente 30/90 dias (art. 26). Prescricao: fato do produto/servico
     5 anos (art. 27). Arrependimento: 7 dias, so compra fora do estabelecimento (art. 49).
     Recursos JEC: 10 dias (Lei 9.099). Sempre conferir (PA-11). -->

---

## Documentos do caso

{{ARQUIVOS}}

<!-- contrato de adesao, faturas, extratos, prints, protocolos de atendimento,
     comprovante de negativacao, e-mails, gravacoes. Numerados "doc. N". -->

---

## Linha de trabalho / Historico

{{LINHA_TRABALHO}}

<!-- Triagem, Selo, documentos analisados, tese definida, pecas produzidas,
     reclamacao administrativa protocolada, audiencia, sentenca. -->

---

**Plugin:** `consumidor-adv-os` v{{PLUGIN_VERSION}}
**Caso aberto em:** {{GENERATED_AT}}
