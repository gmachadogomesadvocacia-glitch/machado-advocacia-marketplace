---
name: acao-isencao-ir
description: >
  ACAO ISENCAO-IR — Skill Tier 2 (lado contribuinte), peca principal. Redige a acao declaratoria de
  isencao de IRPF por doenca grave cumulada com repeticao de indebito dos ultimos 5 anos e tutela de
  urgencia para cessar a retencao. Fundamenta no art. 6 XIV Lei 7.713/88 + Sumulas 598 e 627 STJ;
  trata a nao-extensao a rendimentos de ativo (so proventos) e a restituicao quinquenal (CTN 168).
  Acione quando a via for judicial e o cliente e o contribuinte/beneficiario. Exige Selo P1, laudo e os
  comprovantes de IR retido.
metadata:
  version: "0.1.0"
  area: "Isencao de IRPF por Doenca Grave"
  tier: 2
---

# ACAO ISENCAO-IR (judicial)

> Skill **Tier 2** — lado contribuinte. Declaratoria de isencao + repeticao de indebito + tutela. So roda apos triagem, Selo P1 e linha estrategica.

---

## 0. PRE-REQUISITOS
- Via = judicial. Polo = contribuinte/beneficiario.
- **Selo P1** emitido (Lei 7.713/88 + Sum. 598/627 vigentes).
- Laudo medico (doenca do rol, CID, data) + comprovantes de IR retido + carta de concessao. Falta → `[INFORMAR]` (PA-11). **Nao opinar sobre o diagnostico** (PA-04).

## 1. FORO E PARTES
- **Reu:** Uniao (Fazenda Nacional); quando a retencao e na fonte, pode incluir a fonte pagadora (INSS/RPPS/fundo) para cessar o desconto.
- **Foro:** domicilio do contribuinte — Justica Federal. Ate 60 SM → **JEF Federal** (Lei 10.259).

## 2. ESTRUTURA (FIRAC)
1. **Dos Fatos** — o autor e aposentado/pensionista (doc. N), portador de [doenca do rol] conforme laudo (doc. N), e sofre retencao indevida de IR sobre os proventos desde [data].
2. **Do Direito:**
   - **Isencao — art. 6, XIV, Lei 7.713/88**: proventos de aposentadoria/pensao/reforma de portador de doenca grave sao isentos.
   - **Prova da doenca — Sumula 598 STJ**: desnecessario laudo medico OFICIAL; a doenca pode ser demonstrada por outros meios (PA-07).
   - **Manutencao — Sumula 627 STJ**: a isencao independe da contemporaneidade dos sintomas ou da recidiva; vale mesmo em remissao (PA-08).
   - **So PROVENTOS** (PA-06): nao se estende a rendimento de ativo — delimitar o pedido.
3. **Da Tutela de Urgencia** (art. 300 CPC) — probabilidade (laudo + lista) + perigo (desconto mensal continuado): determinar a **cessacao imediata da retencao** na fonte.
4. **Dos Pedidos:**
   - **declaratorio** da isencao (com efeitos a partir do [marco — laudo/inicio da doenca]);
   - **repeticao de indebito** dos valores retidos nos **ultimos 5 anos** (CTN art. 168 — PA-09), com correcao (Selic);
   - **tutela** para cessar a retencao + isencao das parcelas futuras;
   - protecao do dado de saude (segredo de justica se necessario — PA-10).
5. **Valor da causa** — restituicao pretendida + 12 parcelas isentas (referencia).

## 3. CALCULO
Acionar `calculos-isencao-ir` para apurar o indebito dos 5 anos + Selic. Sem comprovantes de retencao, nao calcular (PA-03) — sinalizar o que falta.

## 4. CHECKLIST
- [ ] Doenca no rol (PA-05) · laudo presente · so proventos (PA-06)
- [ ] Sum. 598 (prova) e 627 (manutencao) invocadas · restituicao limitada a 5 anos (PA-09)
- [ ] Tutela para cessar retencao · dado de saude protegido (PA-10)
- [ ] `revisao-final-isencao-ir` R1-R4 (PA-14)

## MODELO DE PECA
Chassi: `templates/pecas/acao-declaratoria-repeticao.md` (padrao enxuto da casa). Abrir, ler a NOTA DE USO e substituir os `[____]`; nao copiar o texto para ca (limite de 11264 bytes — fonte unica no chassi).

## 5. ENCERRAMENTO
Entrega a inicial com isencao + restituicao quinquenal + tutela, ancorada nas Sumulas 598/627, pronta para a Suprema Corte R1-R4.
