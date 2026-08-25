# MEMORY — {{CLIENTE}}

> Diario de decisoes e historico do caso de leiloes. Complementa o `CASO.md` (estado vivo).
> Vive em `<COWORK>/leiloes/casos/{{CASO_SLUG}}/MEMORY.md`. Atualizado pela skill
> `memoria-de-caso-leiloes` ao fim de cada fase (Protocolo P3). Compartimentado por
> cliente — sigilo profissional + LGPD (dados do condutor/proprietario, CNH, placa/RENAVAM).

---

## Estado executivo

- **Polo:** {{POLO}}
- **Eixo(s):** {{FRENTE}}
- **Fase do processo administrativo:** {{RELACAO_JURIDICA}}
- **Valor da multa / Pontuacao em jogo:** {{QUANTUM_PRETENDIDO}}
- **Fase atual:** {{FASE}}
  <!-- triagem | due diligence pre-lance | lance dado | arrematado | carta expedida | imissao |
       indicacao do condutor | processo de suspensao/cassacao | via judicial (anulatoria/MS) | encerrado -->
- **Proximo passo:** {{PROXIMO_PASSO}}
- **Selo de Validacao Legal Previa (P1):** {{SELO_STATUS}}

---

## Linha estrategica adotada

{{LINHA_ESTRATEGICA}}

<!-- Tese central + teses subsidiarias + riscos mapeados na analise.
     Ex.: analise de vicios -> nulidade por dupla notificacao ausente (Sum. 312 STJ) ou descumprimento
     do prazo da NA (Sum. 127 STJ); subsidiaria: erro de aferição do equipamento (sem certificado
     INMETRO valido), sinalizacao deficiente, descricao generica da infracao, incompetencia do agente.
     Ex.: indicacao do real condutor -> CTB 257 par. 7, dentro do prazo, com identificacao valida
     (NUNCA indicacao falsa — crime art. 299 CP).
     Ex.: CNH -> defesa no processo de suspensao do direito de dirigir / cassacao; reabilitacao.
     Ex.: via -> escolher entre defesa previa x recurso a JARI x CETRAN x anulatoria x MS conforme
     a fase e os vicios. -->

---

## Decisoes do caso (log)

| Data | Decisao | Motivo | Quem |
|------|---------|--------|------|
| {{DATA}} | {{DECISAO}} | {{MOTIVO}} | {{AUTOR}} |

<!-- Registrar escolhas relevantes: arrematar x nao arrematar, desistir x manter o arremate,
     anulatoria x MS), tese (vicio formal x material do auto), opcao por nao recorrer, indicacao do
     condutor, etc. -->

---

## Pontuacao, Prazos e Calculo

{{QUANTUM}}

<!-- Memoria do calculo do CUSTO REAL DE AQUISICAO: lance + comissao do leiloeiro + ITBI +
     total de pontos no periodo de 12 meses, limites para suspensao (Lei 14.071/2020), valor da multa
     com eventual multiplicador, e contagem dos prazos administrativos preclusivos (defesa previa/JARI/
     CETRAN — em regra 30 dias da notificacao NA/NP). Aplicar a norma vigente na data da infracao. -->

---

## Pecas produzidas

| Data | Peca | Status (rascunho/protocolada) | Revisao R1-R4 |
|------|------|-------------------------------|---------------|
| {{DATA_PECA}} | {{PECA}} | {{STATUS_PECA}} | {{REVISAO}} |

---

## Historico fatico-processual

{{HISTORICO}}

<!-- Linha do tempo: divulgacao do edital, 1o e 2o leilao, lance, auto de arrematacao,
     autuacao (NA), defesa previa, notificacao da penalidade (NP), recurso a JARI, decisao JARI,
     recurso ao CETRAN, decisao CETRAN, lancamento de pontos, processo de suspensao/cassacao,
     eventual via judicial (anulatoria/MS). -->

---

**Plugin:** `leiloes-adv-os` v{{PLUGIN_VERSION}}
**Atualizado em:** {{GENERATED_AT}}
