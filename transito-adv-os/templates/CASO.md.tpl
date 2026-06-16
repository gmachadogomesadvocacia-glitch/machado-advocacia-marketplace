# CASO — {{CLIENTE}}

> Ficha do caso de transito. Fonte unica das variaveis de **polo**, **eixo**,
> **dados do auto/infracao** e **demanda** — todas as skills leem estes campos daqui.
> Vive em `<CASE_ROOT>/{{CASO_SLUG}}/CASO.md` — estrutura unificada `<CASE_ROOT>/{{CASO_SLUG}}/`
> (CASO.md, MEMORY.md, arquivos/, pecas/), pasta COMPARTILHADA entre plugins do mesmo cliente; pecas
> produzidas em `{{CASO_SLUG}}/pecas/`. Compartimentado por cliente (sigilo profissional + LGPD —
> dados do condutor/proprietario, CNH, placa/RENAVAM).

---

## Triagem 4D (triagem-transito)

- **Polo do cliente:** {{POLO}}
  <!-- condutor | proprietario do veiculo | indicacao do real condutor
       — variavel-mae; o plugin atua na DEFESA (o Estado autua, sem outro lado simetrico) -->
- **Eixo:** {{FRENTE}}
  <!-- administrativo-defesa-recursos (defesa previa/defesa da autuacao / recurso a JARI /
                recurso ao CETRAN-CONTRANDIFE)
       | cnh-habilitacao (pontuacao e pontos na CNH / suspensao do direito de dirigir /
                cassacao da CNH / infracao autossuspensiva / reabilitacao / indicacao-identificacao do condutor)
       | judicial-anulatoria-ms (acao anulatoria do auto / mandado de seguranca contra o orgao autuador)
       | analise-vicios-do-auto (sinalizacao / aferição do equipamento-radar INMETRO / dupla notificacao /
                descricao da infracao / competencia do agente)
       — pode haver mais de um -->
- **Fase do processo administrativo:** {{RELACAO_JURIDICA}}
  <!-- autuacao (AIT lavrado) | notificacao da autuacao (NA) - prazo de defesa previa aberto |
       notificacao da penalidade (NP) - prazo de recurso a JARI | decisao JARI - prazo CETRAN |
       decisao CETRAN | penalidade definitiva (pontos lancados) | processo de suspensao/cassacao
       instaurado | via judicial. -->
- **Orgao autuador / Agente:** {{REU}}
  <!-- orgao que lavrou o auto (DETRAN, municipio/agencia de transito, PRF, DER) e, se relevante,
       a autoridade de transito competente para julgar (instancia administrativa). -->
- **Valor da multa / Pontuacao em jogo:** {{QUANTUM_PRETENDIDO}}
  <!-- valor da multa (com multiplicador, se houver) + pontos na CNH decorrentes (classificacao:
       leve 3 / media 4 / grave 5 / gravissima 7) + risco de suspensao/cassacao. -->
- **Tipo de demanda:** {{TAREFA}}
  <!-- defesa previa | defesa da autuacao | recurso a JARI | recurso ao CETRAN-CONTRANDIFE |
       indicacao/identificacao do real condutor | defesa em processo de suspensao do direito de dirigir |
       defesa em processo de cassacao da CNH | acao anulatoria | mandado de seguranca |
       parecer | calculo de pontuacao/prazo -->

---

## Partes

| Parte | Qualificacao | Polo | Observacao |
|-------|-------------|------|------------|
| {{PARTE_CLIENTE}} | {{QUALIF_CLIENTE}} | {{POLO}} | cliente (condutor/proprietario) |
| {{PARTE_ADVERSA}} | {{QUALIF_ADVERSA}} | {{POLO_ADVERSO}} | {{OBS_ADVERSA}} |

> **Legitimidade:** confirmar quem figura no auto — **condutor** (quem dirigia) e/ou **proprietario
> do veiculo** (responsavel pela infracao quando nao identificado o condutor — CTB 257). A parte
> adversa e o **orgao autuador / autoridade de transito**. **Coerencia de polo:** o plugin produz a
> defesa do lado do cliente, nunca contra ele.

---

## Dados do Auto e da Infracao (eixo da norma aplicavel)

- **AIT (auto de infracao):** {{DATA_FATO}}
  <!-- numero do AIT, codigo da infracao (CTB/Resolucao CONTRAN) e enquadramento legal. -->
- **Classificacao e enquadramento:** {{FUNDAMENTO}}
  <!-- artigo do CTB + Resolucao CONTRAN; gravidade (leve/media/grave/gravissima) + multiplicador;
       se infracao autossuspensiva. Conferir a norma VIGENTE na data da infracao (tempus regit actum;
       Lei 14.071/2020 alterou pontuacao e validade da CNH). -->
- **Valor da multa / Pontuacao:** {{QUANTUM}}
  <!-- valor da multa (com multiplicador) + pontos lancados na CNH + impacto no total de pontos
       no periodo de 12 meses (limites para suspensao). -->

---

## Marcos do Processo (datas das notificacoes)

- **Data e local da infracao:** {{DATA_INADIMPLEMENTO}}
- **Notificacao da autuacao (NA) — recebimento:** {{DATA_MORA}}
- **Notificacao da penalidade (NP) — recebimento:** {{DATA_NOTIFICACAO}}
- **Defesa previa / recurso protocolado em:** {{DATA_CITACAO}}
- **Decisao JARI / CETRAN em:** {{DATA_SENTENCA}}
- **Processo administrativo / judicial n. + orgao/vara:** {{PROCESSO_JUDICIAL}}

> A **dupla notificacao** (NA e NP) e requisito de validade. A ausencia de qualquer delas, ou o
> descumprimento do prazo de notificacao da autuacao (Sum. 127 STJ), gera nulidade (Sum. 312 STJ;
> CTB 280-281).

---

## Esfera e Competencia (Protocolo P5)

- **Orgao autuador / Local da infracao / Domicilio:** {{CIDADE}}/{{UF}}
- **Instancia / Foro competente:** {{FORO}}
  <!-- Via administrativa: orgao autuador (DETRAN/municipio/PRF/DER) -> JARI -> CETRAN
       (ou CONTRANDIFE no ambito federal). Via judicial: acao anulatoria ou MS no foro do domicilio
       do condutor/proprietario ou do local da infracao; Justica Federal quando o autuador for
       federal (art. 109 CF — ex.: PRF). -->

---

## Selo de Validacao Legal Previa (P1)

- **Status:** {{SELO_STATUS}}
  <!-- PENDENTE | EMITIDO -->
- **Normas validadas (vigentes na data da infracao):** {{SELO_NORMAS}}
  <!-- CTB (Lei 9.503/97) + Lei 14.071/2020 + Resolucoes CONTRAN VIGENTES na data da infracao
       (tempus regit actum) + sumulas STF/STJ confirmadas (ex.: Sum. 312 STJ — dupla notificacao;
       Sum. 127 STJ — prazo de notificacao da autuacao). -->
- **Data:** {{SELO_DATA}}

> Nenhuma skill de producao roda sem o Selo emitido pela `triagem-transito` (validacao do CTB +
> Lei 14.071/2020 + Resolucoes CONTRAN vigentes na data da infracao + sumulas confirmadas).

---

## Prazos Criticos

| Tipo | Marco | Vencimento | Observacao |
|------|-------|------------|------------|
| {{PRAZO_TIPO}} | {{PRAZO_MARCO}} | {{PRAZO_FIM}} | {{PRAZO_OBS}} |

<!-- DEFESA PREVIA / DEFESA DA AUTUACAO: em regra 30 dias contados da NA (notificacao da autuacao).
     RECURSO A JARI: em regra 30 dias contados da NP (notificacao da penalidade).
     RECURSO AO CETRAN/CONTRANDIFE: em regra 30 dias da decisao da JARI.
     INDICACAO DO REAL CONDUTOR: dentro do prazo da defesa da autuacao (CTB 257 par. 7).
     MANDADO DE SEGURANCA: 120 dias do ato (Lei 12.016/2009 art. 23).
     PRESCRICAO / DECADENCIA ADMINISTRATIVA: conferir no caso concreto.
     Prazos administrativos sao PRECLUSIVOS — conferir a data de cada notificacao e nao perder. -->

---

## Documentos do caso

{{ARQUIVOS}}

<!-- auto de infracao (AIT), notificacao da autuacao (NA), notificacao da penalidade (NP), fotos do
     radar/sinalizacao, certificado de aferição do equipamento (INMETRO), CNH e CRLV, comprovante de
     pontuacao (DETRAN/SNE), comprovantes de protocolo, procuracao. Numerados "doc. N". -->

---

## Linha de trabalho / Historico

{{LINHA_TRABALHO}}

<!-- Triagem, Selo, dados do auto analisados, vicios identificados (sinalizacao, aferição do
     equipamento, dupla notificacao, descricao da infracao, competencia do agente), tese definida,
     pecas produzidas (defesa previa, recurso JARI/CETRAN, indicacao do condutor, anulatoria, MS),
     protocolos, decisoes administrativas, eventual via judicial. -->

---

**Plugin:** `transito-adv-os` v{{PLUGIN_VERSION}}
**Caso aberto em:** {{GENERATED_AT}}
