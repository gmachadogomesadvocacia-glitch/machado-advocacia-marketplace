# MEMORY — {{CLIENTE}}

> Diario de decisoes e historico do caso imobiliario/locaticio. Complementa o `CASO.md` (estado vivo).
> Vive em `<COWORK>/imobiliario/casos/{{CASO_SLUG}}/MEMORY.md`. Atualizado pela skill
> `memoria-de-caso-imobiliario` ao fim de cada fase (Protocolo P3). Compartimentado por
> cliente — sigilo + LGPD (dados do cliente e do imovel).

---

## Estado executivo

- **Polo:** {{POLO}}
- **Frente(s):** {{FRENTE}}
- **Imovel / Contrato:** {{IMOVEL}} / {{CONTRATO}}
- **Fase atual:** {{FASE}}
  <!-- triagem | insumos | estrategia | producao | notificado | ajuizado | liminar | contestado
       | sentenca | recurso | consolidacao/leilao | distrato | encerrado -->
- **Proximo passo:** {{PROXIMO_PASSO}}
- **Selo de Validacao Legal Previa (P1):** {{SELO_STATUS}}

---

## Linha estrategica adotada

{{LINHA_ESTRATEGICA}}

<!-- Tese central + teses subsidiarias + riscos mapeados na analise.
     Ex.: despejo por falta de pagamento -> cobranca cumulada, atencao a purgacao da mora
     (art. 62, II, Lei 8.245); subsidiaria: denuncia vazia ao fim do prazo;
     risco: garantia cumulada indevidamente (art. 37, paragrafo unico) -> escolher uma modalidade.
     Ex.: possessoria -> reintegracao por esbulho (forca nova, liminar art. 558 CPC); nao cumular
     com discussao de dominio (posse x propriedade). -->

---

## Decisoes do caso (log)

| Data | Decisao | Motivo | Quem |
|------|---------|--------|------|
| {{DATA}} | {{DECISAO}} | {{MOTIVO}} | {{AUTOR}} |

<!-- Registrar escolhas relevantes: via (extrajudicial x judicial; despejo extrajudicial x acao;
     consolidacao da propriedade x cobranca), instrumento (possessoria x petitoria; distrato x
     rescisao judicial; renovatoria x novo contrato), pedido de liminar, valor da causa, etc. -->

---

## Quantum e calculos

{{QUANTUM}}

<!-- Memoria dos valores: alugueis em atraso + encargos (IPTU, condominio, agua/luz) + multa
     contratual + juros + correcao (indice contratual - IGP-M/IPCA), debito condominial, valor do
     contrato de compra e venda, arras/sinal a devolver, honorarios, valor da causa. Atencao ao
     indice e a norma vigente no contrato. -->

---

## Pecas produzidas

| Data | Peca | Status (rascunho/protocolada) | Revisao R1-R4 |
|------|------|-------------------------------|---------------|
| {{DATA_PECA}} | {{PECA}} | {{STATUS_PECA}} | {{REVISAO}} |

---

## Historico fatico-processual

{{HISTORICO}}

<!-- Linha do tempo: celebracao do contrato, inadimplencia/esbulho/turbacao, notificacao
     extrajudicial, ajuizamento (despejo/possessoria/revisional/renovatoria/adjudicacao/cobranca),
     liminar, citacao, purgacao da mora, contestacao, instrucao, sentenca/acordao, recurso,
     consolidacao da propriedade/leilao, distrato. -->

---

**Plugin:** `imobiliario-adv-os` v{{PLUGIN_VERSION}}
**Atualizado em:** {{GENERATED_AT}}
