# MEMORY — {{CLIENTE}}

> Diario de decisoes e historico do caso tributario. Complementa o `CASO.md` (estado vivo).
> Vive em `<COWORK>/tributario/casos/{{CASO_SLUG}}/MEMORY.md`. Atualizado pela skill
> `memoria-de-caso-tributario` ao fim de cada fase (Protocolo P3). Compartimentado por
> cliente — sigilo fiscal (art. 198 CTN) + LGPD.

---

## Estado executivo

- **Polo:** {{POLO}}
- **Frente(s):** {{FRENTE}}
- **Esfera / Tributo:** {{ESFERA}} / {{TRIBUTO}}
- **Fase atual:** {{FASE}}
  <!-- triagem | insumos | estrategia | producao | protocolado | impugnado | recurso
       | execucao | embargos | parcelamento/transacao | encerrado -->
- **Proximo passo:** {{PROXIMO_PASSO}}
- **Selo de Validacao de Norma Vigente (P1):** {{SELO_STATUS}}

---

## Linha estrategica adotada

{{LINHA_ESTRATEGICA}}

<!-- Tese central + teses subsidiarias + riscos mapeados na analise.
     Ex.: execucao fiscal -> decadencia do lancamento (art. 173 CTN) em pre-executividade
     (Sumula 393); subsidiaria: prescricao intercorrente (art. 40 LEF + Tema 566);
     risco: necessidade de garantia se materia exigir dilacao probatoria (-> embargos LEF). -->

---

## Decisoes do caso (log)

| Data | Decisao | Motivo | Quem |
|------|---------|--------|------|
| {{DATA}} | {{DECISAO}} | {{MOTIVO}} | {{AUTOR}} |

<!-- Registrar escolhas relevantes: via (administrativa x judicial), instrumento (embargos x
     excecao de pre-executividade; anulatoria x MS), opcao por parcelamento/transacao,
     deposito do montante integral (Sumula 112 STJ), valor da causa, etc. -->

---

## Quantum e calculos

{{QUANTUM}}

<!-- Memoria dos valores: principal + multa + juros SELIC, atualizacao do debito/credito,
     montante para deposito integral, valor da repeticao/compensacao pleiteada, honorarios,
     valor da causa. Atencao a norma vigente no fato gerador para multa e juros. -->

---

## Pecas produzidas

| Data | Peca | Status (rascunho/protocolada) | Revisao R1-R4 |
|------|------|-------------------------------|---------------|
| {{DATA_PECA}} | {{PECA}} | {{STATUS_PECA}} | {{REVISAO}} |

---

## Historico fatico-processual

{{HISTORICO}}

<!-- Linha do tempo: fato gerador, autuacao/lancamento, impugnacao administrativa, decisao DRJ,
     recurso ao CARF/TIT, inscricao em divida ativa, ajuizamento da execucao fiscal, citacao,
     garantia/penhora, embargos, sentenca/acordao, recurso, parcelamento/transacao. -->

---

**Plugin:** `tributario-adv-os` v{{PLUGIN_VERSION}}
**Atualizado em:** {{GENERATED_AT}}
