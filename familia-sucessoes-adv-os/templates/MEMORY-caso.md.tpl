# MEMORY — {{CLIENTE}}

> Diario de decisoes e historico do caso de familia/sucessoes. Complementa o `CASO.md` (estado vivo).
> Vive em `<COWORK>/familia/casos/{{CASO_SLUG}}/MEMORY.md`. Atualizado pela skill
> `memoria-de-caso-familia` ao fim de cada fase (Protocolo P3). Compartimentado por
> cliente — sigilo OAB + LGPD (dados sensiveis do nucleo familiar).

---

## Estado executivo

- **Polo:** {{POLO}}
  <!-- requerente | requerido | inventariante | herdeiro | meeiro | consultor -->
- **Area / Tipo:** {{AREA}}
  <!-- familia/sucessoes — divorcio | guarda | alimentos | uniao estavel | interdicao
       | inventario | arrolamento | testamento | planejamento sucessorio -->
- **Regime de bens:** {{REGIME_BENS}}
- **Fase atual:** {{FASE}}
  <!-- triagem | insumos | estrategia | producao | protocolado | audiencia | recurso | partilha/formal -->
- **Proximo passo:** {{PROXIMO_PASSO}}
- **Validacao de Norma Vigente (P1):** {{SELO_STATUS}}

---

## Linha estrategica adotada

{{LINHA_ESTRATEGICA}}

<!-- Tese central + teses subsidiarias + riscos mapeados na analise.
     Ex.: divorcio litigioso -> partilha 50% do patrimonio comum (comunhao parcial) + guarda
     compartilhada + alimentos pelo binomio necessidade/possibilidade; risco: bem particular
     alegado pela parte adversa (conferir origem/data de aquisicao). -->

---

## Decisoes do caso (log)

| Data | Decisao | Motivo | Quem |
|------|---------|--------|------|
| {{DATA}} | {{DECISAO}} | {{MOTIVO}} | {{AUTOR}} |

<!-- Registrar escolhas relevantes: via (judicial x extrajudicial), guarda (compartilhada x unilateral),
     valor dos alimentos pleiteado, proposta de acordo, partilha proposta, opcao por arrolamento x
     inventario, doacao em vida x testamento, etc. -->

---

## Quantum e calculos

{{QUANTUM}}

<!-- Memoria dos valores: alimentos (percentual sobre rendimentos ou valor fixo; binomio),
     meacao e quinhao hereditario (percentuais por regime e ordem de vocacao), valor dos bens
     a partilhar, ITCMD estimado, valor da causa. -->

---

## Pecas produzidas

| Data | Peca | Status (rascunho/protocolada) | Revisao R1-R4 |
|------|------|-------------------------------|---------------|
| {{DATA_PECA}} | {{PECA}} | {{STATUS_PECA}} | {{REVISAO}} |

---

## Historico fatico-processual

{{HISTORICO}}

<!-- Linha do tempo: casamento/uniao, separacao de fato, obito (na sucessao), ajuizamento,
     contestacao, audiencia de conciliacao/instrucao, parecer do MP (havendo incapaz),
     sentenca, partilha/formal de partilha, recurso. -->

---

**Plugin:** `familia-sucessoes-adv-os` v{{PLUGIN_VERSION}}
**Atualizado em:** {{GENERATED_AT}}
