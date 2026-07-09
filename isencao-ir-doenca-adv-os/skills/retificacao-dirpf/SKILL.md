---
name: retificacao-dirpf
description: >
  RETIFICACAO DIRPF — Skill Tier 2 (lado contribuinte). Acione quando o cliente ja recolheu/teve IR retido em anos anteriores e quer restituir. Exige Selo P1, laudo e informes de IR.
metadata:
  version: "0.1.0"
  area: "Isencao de IRPF por Doenca Grave"
  tier: 2
---

# RETIFICACAO DA DIRPF (restituicao dos 5 anos)

> Skill **Tier 2** — lado contribuinte. Reclassifica proventos como rendimentos ISENTOS nas declaracoes passadas para restituir o IR retido. So roda apos triagem, Selo P1 e linha estrategica.

---

## 0. PRE-REQUISITOS
- Polo = contribuinte/beneficiario. **Selo P1** emitido (Lei 7.713/88 art. 6 XIV + IN RFB 1500/2014).
- Laudo (doenca do rol, CID, data) + **informes de rendimento/comprovantes de IR retido** de cada ano. Falta → `[INFORMAR]` (PA-11). Nao opinar sobre o diagnostico (PA-04).

## 1. PRAZO — ULTIMOS 5 ANOS (PA-09)
- A restituicao do indebito so alcanca os **ultimos 5 anos** (CTN art. 168). Anos anteriores estao **prescritos** — nao pleitear (PA-09).
- Mapear, ano a ano, quais exercicios ainda estao no quinquenio a partir da data atual; priorizar os que vencem antes.
- A reclassificacao vale a partir do **marco da doenca/laudo**; antes desse marco nao ha isencao.

## 2. PASSO A PASSO DA RETIFICADORA
1. Localizar a declaracao **original** de cada ano (recibo/numero).
2. Abrir a **retificadora** do exercicio (mesmo modelo da original) no programa/ e-CAC da Receita.
3. Mover os **proventos** da ficha de rendimentos **tributaveis** para **rendimentos ISENTOS e nao tributaveis** (portador de molestia grave).
4. Conferir o recalculo: o imposto devido cai → gera **saldo a restituir** (ou reduz o pago).
5. Transmitir; guardar o **recibo da retificadora** (doc. N).
6. Acompanhar o processamento e a inclusao em lote de restituicao no e-CAC.

## 3. RISCO DE MALHA FINA — COMO INSTRUIR
- A reclassificacao tende a **reter em malha** ("pendencia"). Instruir desde ja: **laudo** (doc. N), **carta de concessao** (doc. N), **informes** (doc. N).
- Se cair em malha, responder a intimacao no e-CAC com a documentacao; se a Receita negar, a recusa vira prova para a via judicial (P4).
- Dado de saude sob sigilo — expor CID so no indispensavel (PA-10).

## 4. COMPLEMENTARIDADE
- O **requerimento administrativo** (`requerimento-administrativo-isencao`) cessa a retencao **futura** na fonte; a **retificadora** recupera o **passado** (5 anos). Sao complementares.
- Se a Receita resistir, escalar para `acao-isencao-ir` (repeticao de indebito) ou `mandado-seguranca-isencao`. So PROVENTOS (PA-06); doenca do rol (PA-05).

## 5. CHECKLIST
- [ ] Exercicios dentro dos 5 anos mapeados (PA-09) · marco da doenca definido
- [ ] Proventos movidos p/ rendimentos ISENTOS · recibos guardados
- [ ] Documentacao pronta p/ malha (laudo+carta+informes) · dado protegido (PA-10)
- [ ] CASO.md atualizado · `revisao-final-isencao-ir` R1-R4 (PA-14)

## 6. ENCERRAMENTO
Entrega o roteiro das retificadoras dos 5 anos com a reclassificacao para isentos, a instrucao contra a malha fina e a articulacao com a via administrativa/judicial, pronto para a Suprema Corte R1-R4.
