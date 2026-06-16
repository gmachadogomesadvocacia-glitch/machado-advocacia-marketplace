# MEMORY — {{CLIENTE}}

> Diario de decisoes e historico do caso penal/processual penal. Complementa o `CASO.md` (estado vivo).
> Vive em `<COWORK>/criminal/casos/{{CASO_SLUG}}/MEMORY.md`. Atualizado pela skill
> `memoria-de-caso-criminal` ao fim de cada fase (Protocolo P3). Compartimentado por
> cliente — sigilo profissional reforcado + LGPD (dados sensiveis do reu/investigado e da vitima).

---

## Estado executivo

- **Polo:** {{POLO}}
- **Fase / Frente(s):** {{FRENTE}}
- **Crime / Tipificacao:** {{CRIME}}
- **Situacao prisional:** {{SITUACAO_PRISIONAL}}
- **Fase atual:** {{FASE}}
  <!-- triagem | insumos | estrategia | producao | inquerito | flagrante/custodia | denunciado
       | resposta a acusacao | instrucao | memoriais | sentenca | recurso | execucao | encerrado -->
- **Proximo passo:** {{PROXIMO_PASSO}}
- **Selo de Validacao Legal Previa (P1):** {{SELO_STATUS}}

---

## Linha estrategica adotada

{{LINHA_ESTRATEGICA}}

<!-- Tese central + teses subsidiarias + riscos mapeados na analise.
     Ex.: flagrante -> arguir relaxamento por ilegalidade da prisao; subsidiaria: liberdade
     provisoria com/sem fianca (art. 310 CPP); atencao a lei penal no tempo.
     Ex.: acao penal -> absolvicao por atipicidade/excludente; subsidiaria: desclassificacao;
     ultima ratio: dosimetria favoravel (trifasico art. 68 CP) - nao inventar fracoes.
     Ex.: execucao -> progressao de regime; livramento condicional; remicao pelo trabalho/estudo. -->

---

## Decisoes do caso (log)

| Data | Decisao | Motivo | Quem |
|------|---------|--------|------|
| {{DATA}} | {{DECISAO}} | {{MOTIVO}} | {{AUTOR}} |

<!-- Registrar escolhas relevantes: via (relaxamento x liberdade provisoria; HC x recurso;
     ANPP/transacao/sursis x defesa de merito), tese (atipicidade x excludente x nulidade),
     opcao por nao recorrer, aceitacao de acordo despenalizador, etc. -->

---

## Quantum / Pena e Prescricao

{{QUANTUM}}

<!-- Memoria do calculo: pena-base (circunstancias judiciais art. 59), agravantes/atenuantes,
     causas de aumento/diminuicao (trifasico art. 68 CP), regime inicial, detracao (CP 42),
     prescricao da pretensao punitiva x executoria (CP 109/110), pena a cumprir, datas-base para
     progressao/livramento. Atencao a lei penal no tempo. -->

---

## Pecas produzidas

| Data | Peca | Status (rascunho/protocolada) | Revisao R1-R4 |
|------|------|-------------------------------|---------------|
| {{DATA_PECA}} | {{PECA}} | {{STATUS_PECA}} | {{REVISAO}} |

---

## Historico fatico-processual

{{HISTORICO}}

<!-- Linha do tempo: data do fato, flagrante/prisao, audiencia de custodia, inquerito,
     oferecimento/recebimento da denuncia ou queixa, citacao, resposta a acusacao, instrucao,
     alegacoes finais/memoriais, sentenca/acordao, recurso, transito em julgado, guia de execucao,
     incidentes da execucao (progressao, falta grave, livramento). -->

---

**Plugin:** `criminal-adv-os` v{{PLUGIN_VERSION}}
**Atualizado em:** {{GENERATED_AT}}
