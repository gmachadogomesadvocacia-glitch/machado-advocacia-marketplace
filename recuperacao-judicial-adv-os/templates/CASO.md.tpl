# CASO — {{CLIENTE}}

> Ficha do caso de recuperacao judicial/falencia. Fonte unica das variaveis de
> **polo**, **classe**, **fato gerador**, **via** e **fase** — todas as skills leem
> estes campos daqui. Vive na pasta unificada de caso `<CASE_ROOT>/{{CASO_SLUG}}/CASO.md`
> (Code: `<acervo>/Casos-Ativos`; fallback Cowork: `<COWORK>/recuperacao-judicial/casos`),
> com `CASO.md`, `MEMORY.md`, `arquivos/` e `pecas/`. Pasta COMPARTILHADA entre plugins do
> mesmo cliente (ex.: RJ + trabalhista). Compartimentado por cliente (sigilo OAB + LGPD — PA-22).

---

## Triagem 4D (triagem-rj)

- **Polo do cliente:** {{POLO}}
  <!-- credor | credor-trabalhista | devedor-recuperando | administrador-judicial | consultivo
       — variavel-mae; toda tese/pedido/tom flipa por ela. Lexico trabalhista -> MODO CTH. -->
- **Classe do credito (se polo = credor):** {{CLASSE}}
  <!-- I (trabalhista/acidente — teto 150 SM, art. 83 I) | II (garantia real) |
       III (quirografario) | IV (ME/EPP). Excedente do teto da Classe I migra para Classe III. -->
- **Fato gerador / Concursalidade:** {{FATO_GERADOR}}
  <!-- data/periodo do fato gerador -> concursal (anterior ao pedido — sujeito ao plano) x
       extraconcursal (posterior — art. 67/84). Cravar SEMPRE antes de classificar. -->
- **Via processual:** {{VIA}}
  <!-- divergencia (art. 7 §1 — administrativa ao AJ) | impugnacao (art. 8 — judicial) |
       habilitacao retardataria (art. 10) | reserva (art. 6 §2 — credito iliquido/em discussao) -->
- **Fase do processo:** {{FASE}}
  <!-- pre-pedido | peticao inicial (art. 51) | stay period (art. 6) | janela do edital (art. 7 §1) |
       relacao consolidada (art. 7 §2) | QGC homologado (art. 14) | plano | AGC | execucao | encerramento -->
- **Tipo de tarefa:** {{TAREFA}}
  <!-- habilitacao | divergencia | impugnacao | retardataria | reserva | contestacao | plano
       | tutela | recurso | calculo | parecer | acordo extrajudicial -->

---

## Partes

| Parte | Qualificacao | Polo | Observacao |
|-------|-------------|------|------------|
| {{PARTE_CLIENTE}} | {{QUALIF_CLIENTE}} | {{POLO}} | cliente |
| {{PARTE_ADVERSA}} | {{QUALIF_ADVERSA}} | {{POLO_ADVERSO}} | {{OBS_ADVERSA}} |
| {{ADMINISTRADOR_JUDICIAL}} | AJ | administrador-judicial | nome + contato |

---

## Credito do Cliente (se polo = credor)

- **Natureza:** {{NATUREZA_CREDITO}}
  <!-- trabalhista | garantia real | quirografario | ME/EPP | financeiro | fornecedor -->
- **Origem:** {{ORIGEM_CREDITO}}
  <!-- sentenca da JT | acordo homologado | certidao de credito trabalhista (CH) | contrato | NF -->
- **Valor historico:** {{VALOR_HISTORICO}}
- **Valor atualizado (ate a data do pedido de RJ — congelamento art. 9 II):** {{VALOR_ATUALIZADO}}
- **Classe(s) e valor por classe:** {{CLASSE_VALORES}}
  <!-- ex.: Classe I R$ ... (ate 150 SM) / Classe III R$ ... (excedente) -->
- **Teto de 150 SM (art. 83 I) aplicado:** {{TETO_150SM}}
  <!-- sim/nao + valor do SM de referencia + excedente migrado para Classe III -->

---

## Cruzamento Justica do Trabalho x RJ (Protocolo P8 — se houver origem trabalhista)

- **Processo trabalhista de origem:** {{PROCESSO_TRABALHISTA}}
- **Fase na JT:** {{FASE_JT}}
  <!-- conhecimento | liquidacao | execucao | arquivado com CH expedida -->
- **Certidao de credito trabalhista (CH) expedida:** {{CH_EXPEDIDA}}
- **Prescricao verificada:** {{PRESCRICAO}}
  <!-- bienal (art. 7 XXIX CF) | intercorrente (art. 11-A CLT) | da habilitacao | pos-encerramento (art. 61) -->

---

## Localizacao e Competencia (Protocolo P5)

- **Processo de RJ n.:** {{PROCESSO_RJ}}
- **Vara empresarial/falimentar / Comarca:** {{VARA}}
  <!-- Juizo do principal estabelecimento (art. 3 LFRJ); juizo universal p/ constricao (Sum. 480 STJ). -->
- **Administrador Judicial:** {{ADMINISTRADOR_JUDICIAL}}

---

## Validacao de Norma Vigente (P1)

- **Status:** {{SELO_STATUS}}
  <!-- PENDENTE | EMITIDO -->
- **Normas validadas:** {{SELO_NORMAS}}
  <!-- L11.101/2005 + L14.112/2020 (conferir redacao pre/pos reforma) + CLT (se trabalhista) +
       sumulas/Temas STJ (480, 581, 1.051, IAC 13 — sempre [VERIFICAR]) -->
- **Data:** {{SELO_DATA}}

> Nenhuma skill de producao roda sem a Validacao de Norma Vigente (L11.101 + L14.112) emitida.

---

## Prazos Criticos

| Tipo | Marco | Vencimento | Observacao |
|------|-------|------------|------------|
| {{PRAZO_TIPO}} | {{PRAZO_MARCO}} | {{PRAZO_FIM}} | {{PRAZO_OBS}} |

<!-- Divergencia (art. 7 §1): 15 dias da publicacao do edital. Impugnacao (art. 8): 10 dias da
     relacao consolidada. Stay period (art. 6 §4): 180 dias prorrogaveis. Plano: 60 dias do
     deferimento. Objecoes ao plano e prazos da AGC. Sempre conferir caso a caso. -->

---

## Documentos do caso

{{ARQUIVOS}}

<!-- sentenca/acordo da JT, certidao de credito, calculo de liquidacao, edital de credores,
     relacao do art. 7 §2, QGC, plano, balancos (art. 51). Numerados "doc. N". -->

---

## Linha de trabalho / Historico

{{LINHA_TRABALHO}}

<!-- Triagem, Validacao de Norma, documentos analisados, via definida, classe e fato gerador
     cravados, calculo do credito, peca produzida, habilitacao/impugnacao protocolada, AGC,
     decisao de QGC, recurso. -->

---

**Plugin:** `recuperacao-judicial-adv-os` v{{PLUGIN_VERSION}}
**Caso aberto em:** {{GENERATED_AT}}
