# MEMORY — {{CLIENTE}}

> Diario de decisoes e historico do caso civel/processual civel. Complementa o `CASO.md` (estado vivo).
> Vive em `<COWORK>/civel/casos/{{CASO_SLUG}}/MEMORY.md`. Atualizado pela skill
> `memoria-de-caso-civel` ao fim de cada fase (Protocolo P3). Compartimentado por
> cliente — sigilo profissional + LGPD (dados das partes).

---

## Estado executivo

- **Polo:** {{POLO}}
- **Frente(s):** {{FRENTE}}
- **Relacao juridica / fato:** {{RELACAO_JURIDICA}}
- **Valor / Quantum pretendido:** {{QUANTUM_PRETENDIDO}}
- **Fase atual:** {{FASE}}
  <!-- triagem | insumos | estrategia | producao | pre-processual/notificacao | ajuizamento |
       citacao/contestacao | instrucao | sentenca | recurso | cumprimento/execucao | encerrado -->
- **Proximo passo:** {{PROXIMO_PASSO}}
- **Selo de Validacao Legal Previa (P1):** {{SELO_STATUS}}

---

## Linha estrategica adotada

{{LINHA_ESTRATEGICA}}

<!-- Tese central + teses subsidiarias + riscos mapeados na analise.
     Ex.: responsabilidade civil -> demonstrar ato ilicito + nexo + dano; subsidiaria:
     responsabilidade objetiva (risco); atencao a prescricao trienal (CC 206 par. 3 V) e ao
     termo inicial dos juros (Sum. 54/362 STJ).
     Ex.: contratos -> rescisao por inadimplemento + perdas e danos; subsidiaria: revisao de
     clausula penal (CC 413); distrato.
     Ex.: cobranca -> escolher a via (acao de cobranca x monitoria x execucao de titulo
     extrajudicial) conforme a forca do titulo. -->

---

## Decisoes do caso (log)

| Data | Decisao | Motivo | Quem |
|------|---------|--------|------|
| {{DATA}} | {{DECISAO}} | {{MOTIVO}} | {{AUTOR}} |

<!-- Registrar escolhas relevantes: via (acao de cobranca x monitoria x execucao; tutela de
     urgencia x evidencia), tese (contratual x extracontratual; existencia/extensao do dano),
     opcao por nao recorrer, aceitacao de acordo/distrato, etc. -->

---

## Quantum / Liquidacao do dano, Juros e Correcao

{{QUANTUM}}

<!-- Memoria do calculo: dano emergente x lucro cessante; dano moral/estetico (parametros e
     precedentes); principal; juros de mora (termo inicial — Sum. 54 STJ extracontratual desde o
     evento; Sum. 362 STJ dano moral desde o arbitramento; contratual desde a citacao/vencimento);
     correcao monetaria (indice e termo inicial); valor da causa. Nao inventar indices. Atencao ao
     direito intertemporal. -->

---

## Pecas produzidas

| Data | Peca | Status (rascunho/protocolada) | Revisao R1-R4 |
|------|------|-------------------------------|---------------|
| {{DATA_PECA}} | {{PECA}} | {{STATUS_PECA}} | {{REVISAO}} |

---

## Historico fatico-processual

{{HISTORICO}}

<!-- Linha do tempo: data do fato/celebracao do contrato, inadimplemento/mora, notificacao/
     interpelacao/protesto, ajuizamento, tutela de urgencia, citacao, contestacao, replica,
     instrucao, sentenca/acordao, recurso, transito em julgado, cumprimento de sentenca/execucao. -->

---

**Plugin:** `civel-adv-os` v{{PLUGIN_VERSION}}
**Atualizado em:** {{GENERATED_AT}}
