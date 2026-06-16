# MEMORY — {{CLIENTE}}

> Diario de decisoes e historico do caso de usucapiao. Complementa o `CASO.md` (estado vivo).
> Vive em `<COWORK>/usucapiao/casos/{{CASO_SLUG}}/MEMORY.md`. Atualizado pela skill
> `memoria-de-caso-usucapiao` ao fim de cada fase (Protocolo P3). Compartimentado por
> cliente — sigilo OAB + LGPD.

---

## Estado executivo

- **Polo:** {{POLO}}
  <!-- usucapiente | confrontante/oponente -->
- **Via / Modalidade:** {{EIXO}}
  <!-- judicial x extrajudicial; extraordinaria/ordinaria/especial urbana/rural/familiar/coletiva -->
- **Fase atual:** {{FASE}}
  <!-- triagem | insumos (matricula/planta/ata) | estrategia | producao | protocolado/registro |
       citacao/anuencia | impugnacao | sentenca | registro | recurso -->
- **Proximo passo:** {{PROXIMO_PASSO}}
- **Selo de Validacao de Norma Vigente (P1):** {{SELO_STATUS}}

---

## Linha estrategica adotada

{{LINHA_ESTRATEGICA}}

<!-- Modalidade e via escolhidas + fundamento + riscos mapeados na analise trilateral.
     Ex.: posse de 16 anos sem titulo -> usucapiao extraordinaria (CC art. 1.238); via
     extrajudicial se todos os confrontantes anuirem, senao judicial; risco: confrontante
     ausente / imovel proximo a area publica (conferir dominialidade — Sumula 340 STF). -->

---

## Decisoes do caso (log)

| Data | Decisao | Motivo | Quem |
|------|---------|--------|------|
| {{DATA}} | {{DECISAO}} | {{MOTIVO}} | {{AUTOR}} |

<!-- Registrar escolhas relevantes: via (judicial x cartorio), modalidade, soma de posses,
     estrategia de prova da posse, valor da causa, opcao por edital, etc. -->

---

## Prova da posse e requisitos

{{QUANTUM}}

<!-- Memoria dos requisitos: marco inicial da posse, tempo total (com accessio possessionis),
     justo titulo/boa-fe (se ordinaria), atos possessorios reunidos (IPTU/ITR, contas,
     benfeitorias), metragem x teto da modalidade, valor da causa (valor do imovel). -->

---

## Pecas produzidas

| Data | Peca | Status (rascunho/protocolada) | Revisao R1-R4 |
|------|------|-------------------------------|---------------|
| {{DATA_PECA}} | {{PECA}} | {{STATUS_PECA}} | {{REVISAO}} |

---

## Historico fatico-processual

{{HISTORICO}}

<!-- Linha do tempo: aquisicao/inicio da posse, atos possessorios, levantamento de matricula,
     planta/memorial e ATA notarial, requerimento ao RI ou ajuizamento, citacao/anuencia de
     confrontantes e entes (Uniao/Estado/Municipio), edital, impugnacao, sentenca/decisao
     do oficial, registro da propriedade, recurso. -->

---

**Plugin:** `usucapiao-adv-os` v{{PLUGIN_VERSION}}
**Atualizado em:** {{GENERATED_AT}}
