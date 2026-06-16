# MEMORY — {{CLIENTE}}

> Diario de decisoes e historico do caso de isencao de IRPF por doenca grave. Complementa o
> `CASO.md` (estado vivo). Vive em `<COWORK>/isencao-ir/casos/{{CASO_SLUG}}/MEMORY.md`. Atualizado
> pela skill `memoria-de-caso-isencao-ir` ao fim de cada fase (Protocolo P3). Compartimentado por
> cliente — sigilo OAB + LGPD; dado de saude e SENSIVEL (art. 11).

---

## Estado executivo

- **Polo:** {{POLO}}
- **Doenca / CID:** {{DOENCA}}
- **Tipo de provento / fonte pagadora:** {{TIPO_PROVENTO}} / {{FONTE_PAGADORA}}
- **Fase atual:** {{FASE}}
  <!-- triagem | insumos | estrategia | producao | protocolado (adm/judicial) | sentenca | restituicao | recurso -->
- **Proximo passo:** {{PROXIMO_PASSO}}
- **Selo de Validacao de Norma Vigente (P1):** {{SELO_STATUS}}

---

## Linha estrategica adotada

{{LINHA_ESTRATEGICA}}

<!-- Tese central + teses subsidiarias + riscos mapeados na analise.
     Ex.: isencao desde a data do laudo -> declaratoria + repeticao de indebito dos ultimos 5 anos;
     risco: Sumula 627 (afastar rendimentos de ativo); via administrativa antes da judicial. -->

---

## Decisoes do caso (log)

| Data | Decisao | Motivo | Quem |
|------|---------|--------|------|
| {{DATA}} | {{DECISAO}} | {{MOTIVO}} | {{AUTOR}} |

<!-- Registrar escolhas relevantes: via (administrativa x judicial x MS), termo inicial da isencao,
     periodo da restituicao pleiteada, pedido de tutela de cessacao da retencao, etc. -->

---

## Quantum e calculos de restituicao

{{QUANTUM}}

<!-- Memoria dos valores: IRRF retido mes a mes, periodo restituivel (5 anos — CTN art. 168),
     correcao (SELIC), valor da causa. NAO opinar sobre conduta clinica — apenas o enquadramento. -->

---

## Pecas produzidas

| Data | Peca | Status (rascunho/protocolada) | Revisao R1-R4 |
|------|------|-------------------------------|---------------|
| {{DATA_PECA}} | {{PECA}} | {{STATUS_PECA}} | {{REVISAO}} |

---

## Historico fatico-processual

{{HISTORICO}}

<!-- Linha do tempo: aposentadoria/pensao, diagnostico/laudo, inicio da retencao, requerimento
     administrativo (fonte/Receita), retificacao da DIRPF, ajuizamento, sentenca, restituicao, recurso. -->

---

**Plugin:** `isencao-ir-doenca-adv-os` v{{PLUGIN_VERSION}}
**Atualizado em:** {{GENERATED_AT}}
