# MEMORY — {{CLIENTE}}

> Diario de decisoes e historico do caso de recuperacao judicial/falencia. Complementa o
> `CASO.md` (estado vivo). Vive em `<COWORK>/recuperacao-judicial/casos/{{CASO_SLUG}}/MEMORY.md`.
> Atualizado pela skill `memoria-de-caso-rj` ao fim de cada fase (Protocolo P3). Compartimentado
> por cliente — sigilo OAB + LGPD (PA-22).

---

## Estado executivo

- **Polo:** {{POLO}}
  <!-- credor | credor-trabalhista | devedor-recuperando | administrador-judicial | consultivo -->
- **Classe / Via:** {{CLASSE}} / {{VIA}}
  <!-- Classe I/II/III/IV — Via divergencia (art. 7 §1) / impugnacao (art. 8) / retardataria (art. 10) / reserva (art. 6 §2) -->
- **Fato gerador / Concursalidade:** {{FATO_GERADOR}}
- **Fase atual:** {{FASE}}
  <!-- triagem | insumos | estrategia | producao | protocolado | QGC | plano | AGC | execucao | encerramento -->
- **Proximo passo:** {{PROXIMO_PASSO}}
- **Validacao de Norma Vigente (P1):** {{SELO_STATUS}}

---

## Linha estrategica adotada

{{LINHA_ESTRATEGICA}}

<!-- Tese central + teses subsidiarias + riscos. Ex.: credor trabalhista -> habilitar Classe I
     ate 150 SM + excedente Classe III; via = divergencia (dentro do prazo do art. 7 §1);
     risco: objecao do AJ quanto ao fato gerador / concursalidade. -->

---

## Decisoes do caso (log)

| Data | Decisao | Motivo | Quem |
|------|---------|--------|------|
| {{DATA}} | {{DECISAO}} | {{MOTIVO}} | {{AUTOR}} |

<!-- Registrar escolhas relevantes: via (divergencia x impugnacao x retardataria x reserva),
     classe e fato gerador cravados, valor habilitado, segregacao concursal/extraconcursal,
     posicao na AGC, recurso. -->

---

## Quantum e calculos

{{QUANTUM}}

<!-- Memoria dos valores: valor historico, atualizacao ate a data do pedido (congelamento art. 9 II),
     teto de 150 SM (art. 83 I) e excedente migrado para Classe III, segregacao de verbas
     (FGTS, multas, honorarios sucumbenciais, INSS empregado), valor habilitado por classe. -->

---

## Pecas produzidas

| Data | Peca | Status (rascunho/protocolada) | Revisao R1-R4 |
|------|------|-------------------------------|---------------|
| {{DATA_PECA}} | {{PECA}} | {{STATUS_PECA}} | {{REVISAO}} |

---

## Historico fatico-processual

{{HISTORICO}}

<!-- Linha do tempo: fato gerador, processo trabalhista de origem (se CTH) e fase na JT,
     pedido/deferimento da RJ, publicacao do edital (art. 7 §1), relacao consolidada (art. 7 §2),
     habilitacao/divergencia/impugnacao protocolada, QGC homologado, plano, AGC, recurso,
     execucao/encerramento. -->

---

**Plugin:** `recuperacao-judicial-adv-os` v{{PLUGIN_VERSION}}
**Atualizado em:** {{GENERATED_AT}}
