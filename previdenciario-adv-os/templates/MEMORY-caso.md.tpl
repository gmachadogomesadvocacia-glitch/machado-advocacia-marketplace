# MEMORY — {{CLIENTE}}

> Diario de decisoes e historico do caso previdenciario. Complementa o `CASO.md` (estado vivo).
> Vive em `<CASE_ROOT>/{{CASO_SLUG}}/MEMORY.md` (pasta unificada do caso, compartilhada entre
> plugins: `CASO.md`, `MEMORY.md`, `arquivos/`, `pecas/`). Atualizado ao fim de cada
> fase (Protocolo Memoria de Caso). Compartimentado por segurado — sigilo OAB + LGPD art. 11
> (dados sensiveis de saude e contribuicao).

---

## Estado executivo

- **Sujeito:** {{SUJEITO}}
- **Regime:** {{REGIME}}
  <!-- RGPS | RPPS | previdencia-complementar | acidentario -->
- **Especie(s) de beneficio:** {{ESPECIE}}
- **Fase atual:** {{FASE}}
  <!-- triagem | insumos (CNIS/PPP/laudos) | estrategia | producao | administrativa | judicial
       | pericia | sentenca | recurso | cumprimento -->
- **Proximo passo:** {{PROXIMO_PASSO}}
- **Validacao de norma vigente (EC 103 + marco temporal):** {{SELO_STATUS}}

---

## Linha estrategica adotada

{{LINHA_ESTRATEGICA}}

<!-- Tese central + teses subsidiarias + riscos mapeados na analise trilateral (cliente/INSS/julgador).
     Ex.: aposentadoria por idade urbana -> reconhecimento de vinculos do CNIS + carencia;
     risco: perda da qualidade de segurado / DER mal posicionada. Conferir marco temporal (DER x EC 103). -->

---

## Decisoes do caso (log)

| Data | Decisao | Motivo | Quem |
|------|---------|--------|------|
| {{DATA}} | {{DECISAO}} | {{MOTIVO}} | {{AUTOR}} |

<!-- Registrar escolhas relevantes: via (administrativa x judicial), especie de beneficio,
     regra de transicao escolhida, reafirmacao da DER, pedido de tutela, valor pleiteado, acordo. -->

---

## Quantum e calculos

{{QUANTUM}}

<!-- Memoria dos valores: RMI/RMA, salario-de-beneficio, atrasados (parcelas vencidas, prescricao
     quinquenal), juros e correcao, honorarios, valor da causa. Nenhum calculo sem CNIS validado. -->

---

## Pecas produzidas

| Data | Peca | Status (rascunho/protocolada) | Revisao R1-R4 |
|------|------|-------------------------------|---------------|
| {{DATA_PECA}} | {{PECA}} | {{STATUS_PECA}} | {{REVISAO}} |

---

## Historico fatico-processual

{{HISTORICO}}

<!-- Linha do tempo: filiacao/vinculos, DER, indeferimento, recurso ao CRPS (JR/Camara),
     protocolo da acao no JEF/JF, pericia medica/social, contestacao do INSS, sentenca,
     recurso (RO/incidente TNU), cumprimento. -->

---

**Plugin:** `previdenciario-adv-os` v{{PLUGIN_VERSION}}
**Atualizado em:** {{GENERATED_AT}}
