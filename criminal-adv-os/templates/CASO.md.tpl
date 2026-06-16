# CASO — {{CLIENTE}}

> Ficha do caso penal/processual penal. Fonte unica das variaveis de **polo**, **fase/frente**,
> **crime/tipificacao** e **situacao prisional/demanda** — todas as skills leem estes campos daqui.
> Vive em `<CASE_ROOT>/{{CASO_SLUG}}/CASO.md` na **pasta unificada de caso** (compartilhada
> entre os plugins Adv-OS). Estrutura: `<slug>/CASO.md`, `<slug>/MEMORY.md`, `<slug>/arquivos/`
> (autos, BO, laudos — entrada) e `<slug>/pecas/` (produzidos). Compartimentado por cliente
> (sigilo profissional reforcado + LGPD — dados sensiveis do reu/investigado e da vitima);
> pasta gitignored.

---

## Triagem 4D (triagem-criminal)

- **Polo do cliente:** {{POLO}}
  <!-- defesa (investigado | reu | acusado | sentenciado) | assistencia-de-acusacao (vitima | ofendido)
       — variavel-mae; toda tese/pedido/tom flipa por ela -->
- **Fase / Frente:** {{FRENTE}}
  <!-- investigacao-inquerito (inquerito policial / flagrante / preventiva / temporaria / relaxamento
                / liberdade provisoria / audiencia de custodia / fianca / cautelares)
       | acao-penal (denuncia / queixa-crime / resposta a acusacao / absolvicao sumaria / instrucao
                / alegacoes finais-memoriais / sentenca)
       | tribunal-do-juri (pronuncia / impronuncia / desclassificacao / plenario / quesitos)
       | recursos (apelacao / RESE / embargos / HC / RHC / revisao criminal)
       | execucao-penal (LEP - progressao / livramento / remicao / falta grave / saida temporaria / detracao)
       | acordos-despenalizadores (ANPP / transacao penal / suspensao condicional / sursis / Lei 9.099)
       — pode haver mais de uma -->
- **Crime / Tipificacao:** {{CRIME}}
  <!-- tipo penal imputado (CP ou lei especial — Lei de Drogas 11.343, Maria da Penha 11.340 etc.),
       artigo, classificacao (doloso/culposo, tentado/consumado, crime contra a vida -> Juri).
       Define a competencia e o rito. -->
- **Reu / Investigado / Sentenciado:** {{REU}}
  <!-- qualificacao do cliente conforme a fase: investigado (inquerito), reu/acusado (acao penal),
       sentenciado (execucao). -->
- **Situacao prisional:** {{SITUACAO_PRISIONAL}}
  <!-- solto | preso em flagrante | preventiva | temporaria | cumprindo pena (regime fechado/
       semiaberto/aberto) | monitoramento eletronico | cautelares diversas da prisao -->
- **Tipo de demanda:** {{TAREFA}}
  <!-- relaxamento de prisao | liberdade provisoria | resposta a acusacao | memoriais/alegacoes finais
       | HC | apelacao/RESE | progressao de regime | livramento condicional | ANPP/transacao/sursis
       | parecer | calculo de pena/prescricao -->

---

## Partes

| Parte | Qualificacao | Polo | Observacao |
|-------|-------------|------|------------|
| {{PARTE_CLIENTE}} | {{QUALIF_CLIENTE}} | {{POLO}} | cliente |
| {{PARTE_ADVERSA}} | {{QUALIF_ADVERSA}} | {{POLO_ADVERSO}} | {{OBS_ADVERSA}} |

> **Legitimidade e titularidade da acao:** identificar o titular da acao penal — **Ministerio
> Publico** (acao penal publica) ou **querelante/ofendido** (acao penal privada — queixa-crime).
> Na defesa, confirmar a qualificacao do cliente conforme a fase (investigado/reu/sentenciado).
> Na assistencia de acusacao, a habilitacao do ofendido/vitima (art. 268 CPP). **Coerencia de
> polo:** o plugin produz a peca do lado do cliente, nunca contra ele.

---

## Crime e Imputacao (eixo da norma aplicavel)

- **Data do fato:** {{DATA_FATO}}
  <!-- DEFINE a lei penal aplicavel: lei vigente ao tempo do fato, salvo lei posterior mais benefica,
       que retroage (CF 5 XL; CP 2). Conferir lei penal no tempo. -->
- **Tipificacao / capitulacao:** {{TIPIFICACAO}}
  <!-- artigo do CP ou da lei especial, com qualificadoras/causas de aumento/privilegios. -->
- **Pena cominada / pena aplicada (se houver sentenca):** {{PENA}}
  <!-- pena em abstrato (para prescricao da pretensao punitiva) e/ou pena em concreto fixada
       (dosimetria trifasica art. 68 CP; prescricao da pretensao executoria). -->

---

## Marcos Processuais e Prisionais

- **Flagrante / data da prisao:** {{DATA_FLAGRANTE}}
- **Inquerito policial / IPL n.:** {{IPL}}
- **Denuncia / queixa recebida em:** {{DATA_DENUNCIA}}
- **Sentenca / acordao em:** {{DATA_SENTENCA}}
- **Processo n. + vara/orgao:** {{PROCESSO_JUDICIAL}}

---

## Localizacao e Competencia (Protocolo P5)

- **Lugar da infracao:** {{CIDADE}}/{{UF}}
- **Foro / Vara criminal / Juri / VEP competente:** {{FORO}}
  <!-- Regra: lugar da infracao (art. 70 CPP). Crimes dolosos contra a vida -> Tribunal do Juri.
       Justica Estadual x Federal (art. 109 CF). Infracao de menor potencial ofensivo -> JECrim
       (Lei 9.099). Fase de execucao -> Vara de Execucoes Penais (VEP / LEP). -->

---

## Selo de Validacao Legal Previa (P1)

- **Status:** {{SELO_STATUS}}
  <!-- PENDENTE | EMITIDO -->
- **Normas validadas (no fato):** {{SELO_NORMAS}}
  <!-- Codigo Penal (CP) + Codigo de Processo Penal (CPP) + LEP (Lei 7.210) + leis especiais
       (Lei de Drogas 11.343, Maria da Penha 11.340, Lei 9.099 JECrim) VIGENTES na data do fato
       (lei penal no tempo) + sumulas STF/STJ e vinculantes confirmadas. -->
- **Data:** {{SELO_DATA}}

> Nenhuma skill de producao roda sem o Selo emitido pela `triagem-criminal` (validacao da
> legislacao vigente no fato + lei penal no tempo + sumulas confirmadas).

---

## Prazos Criticos

| Tipo | Marco | Vencimento | Observacao |
|------|-------|------------|------------|
| {{PRAZO_TIPO}} | {{PRAZO_MARCO}} | {{PRAZO_FIM}} | {{PRAZO_OBS}} |

<!-- RESPOSTA A ACUSACAO: 10 dias da citacao (art. 396/396-A CPP).
     RESE (recurso em sentido estrito): 5 dias para interpor (art. 586 CPP) + 2 dias razoes.
     APELACAO: 5 dias para interpor (art. 593 CPP) + 8 dias razoes (8 dias contravencao/sumario).
     MEMORIAIS / ALEGACOES FINAIS por memoriais: 5 dias (art. 403, par. 3, CPP).
     PRISAO TEMPORARIA: 5 dias prorrogaveis (30+30 em crime hediondo) - Lei 7.960.
     DECADENCIA DA QUEIXA (acao penal privada): 6 meses do conhecimento da autoria (art. 38 CPP).
     PRESCRICAO PENAL: distinguir pretensao punitiva x executoria; calcular pela pena (CP 109/110).
     Sempre conferir o prazo no caso concreto. -->

---

## Documentos do caso

{{ARQUIVOS}}

<!-- auto de prisao em flagrante (APF), inquerito policial (IPL), denuncia/queixa, laudos periciais,
     folha de antecedentes criminais (FAC), boletim de ocorrencia, termos de depoimento,
     interrogatorio, guia de recolhimento/execucao, atestado de pena a cumprir, procuracao.
     Numerados "doc. N". -->

---

## Linha de trabalho / Historico

{{LINHA_TRABALHO}}

<!-- Triagem, Selo, documentos analisados, tese definida (atipicidade, excludentes, nulidades,
     prova ilicita, prescricao), pecas produzidas, prisao/relaxamento, liberdade provisoria,
     resposta a acusacao, instrucao, sentenca/acordao, recurso, fase de execucao, ANPP/acordos. -->

---

**Plugin:** `criminal-adv-os` v{{PLUGIN_VERSION}}
**Caso aberto em:** {{GENERATED_AT}}
