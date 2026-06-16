---
name: requerimento-administrativo-isencao
description: >
  REQUERIMENTO ADMINISTRATIVO ISENCAO — Skill Tier 2 (lado contribuinte). Redige o requerimento de
  isencao de IRPF por doenca grave a FONTE PAGADORA (INSS via Meu INSS / RPPS do orgao / fundo de pensao
  EFPC) e orienta a retificacao da DIRPF na Receita para a restituicao. Inclui a juntada do LAUDO DE
  SERVICO MEDICO OFICIAL (exigencia administrativa), o pedido de cessacao da retencao e de devolucao do
  retido, prazos de resposta e o uso do silencio/recusa como prova pre-constituida (Protocolo P4).
  Acione na via administrativa pelo contribuinte. Exige Selo P1, laudo oficial e comprovantes de IR retido.
metadata:
  version: "0.1.0"
  area: "Isencao de IRPF por Doenca Grave"
  tier: 2
---

# REQUERIMENTO ADMINISTRATIVO DE ISENCAO

> Skill **Tier 2** — lado contribuinte, via administrativa. Pede a isencao a fonte pagadora e prepara a restituicao via Receita. So roda apos triagem, Selo P1 e linha estrategica.

---

## 0. PRE-REQUISITOS
- Via = administrativa (ou primeira etapa da via "ambas" — P4). Polo = contribuinte/beneficiario.
- **Selo P1** emitido (Lei 7.713/88 art. 6 XIV + IN RFB 1500/2014 + Sum. 598/627 vigentes).
- **Laudo de servico medico OFICIAL** (doenca do rol, CID, data) — exigencia ADMINISTRATIVA (diferente do judicial, onde a Sum. 598 dispensa o oficial — PA-07). Comprovantes de IR retido + carta de concessao. Falta → `[INFORMAR]` (PA-11). Nao opinar sobre o diagnostico (PA-04).

## 1. FONTE PAGADORA (canal correto)
- **INSS** → Meu INSS (servico "Isencao de Imposto de Renda") / agencia.
- **RPPS** (servidor) → orgao/unidade de RH ou previdencia do ente.
- **Fundo de pensao (EFPC)** → entidade que paga a complementacao.
- Identificar quem **retem** o IR define onde protocolar a cessacao do desconto.

## 2. ESTRUTURA DO REQUERIMENTO
1. **Qualificacao** do requerente e do beneficio (numero, especie).
2. **Fato:** aposentado/pensionista (doc. N), portador de [doenca do rol] conforme **laudo de servico medico oficial** (doc. N); sofre retencao de IRPF sobre os proventos desde [data].
3. **Direito:** art. 6, XIV, Lei 7.713/88 + IN RFB 1500/2014 — proventos isentos. **So proventos** (PA-06); doenca do **rol taxativo** (PA-05).
4. **Pedidos:**
   - **reconhecimento da isencao** e **cessacao imediata** da retencao na fonte;
   - **devolucao** dos valores retidos no exercicio corrente;
   - protecao do dado de saude (PA-10) — juntar laudo sob sigilo, expor CID so no indispensavel.
5. **Juntada:** laudo oficial (doc. N), carta de concessao (doc. N), informes de rendimento/IR retido (doc. N).

## 3. RESTITUICAO DOS ANOS ANTERIORES (Receita)
A devolucao dos exercicios passados nao se faz pela fonte, e sim pela **retificacao da DIRPF** na Receita — acionar `retificacao-dirpf`. Limite: **ultimos 5 anos** (CTN art. 168 — PA-09).

## 4. PRAZOS E PROVA PRE-CONSTITUIDA (P4)
- Acompanhar o prazo de resposta do orgao/entidade.
- **Silencio** (mora administrativa) ou **recusa** expressa = prova pre-constituida para a via judicial (acao ou MS). Registrar protocolo e datas no CASO.md.

## 5. CHECKLIST
- [ ] Doenca no rol (PA-05) · laudo OFICIAL presente · so proventos (PA-06)
- [ ] Canal correto da fonte · pedido de cessacao + devolucao do exercicio
- [ ] Retificacao DIRPF acionada p/ os 5 anos (PA-09) · dado de saude protegido (PA-10)
- [ ] Protocolo/datas no CASO.md · `revisao-final-isencao-ir` R1-R4 (PA-14)

## 6. ENCERRAMENTO
Entrega o requerimento a fonte (isencao + cessacao + devolucao do exercicio), encaminha a retificadora para os 5 anos e fixa o silencio/recusa como prova, pronto para a Suprema Corte R1-R4.
