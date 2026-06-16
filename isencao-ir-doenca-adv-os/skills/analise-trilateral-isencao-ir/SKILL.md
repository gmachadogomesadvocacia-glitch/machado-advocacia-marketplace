---
name: analise-trilateral-isencao-ir
description: >
  ANALISE TRILATERAL ISENCAO-IR — Skill Tier 1. Antes de qualquer producao, analisa o caso por tres
  prismas obrigatorios: Cliente (enquadramento no rol + laudo + retencao indevida), FAZENDA (a melhor
  objecao adversarial: doenca fora do rol; rendimento de ativo nao isento; falta de contemporaneidade/
  laudo; restituicao alem de 5 anos; isencao so a partir do laudo) e Juiz (como o caso aparece para
  quem decide). Gera a matriz forcas x fragilidades x contra-teses. Acionada apos a triagem, antes da
  linha estrategica. Gatilhos: analise do caso, pontos fortes e fracos, o que a Fazenda vai alegar,
  riscos, antes de redigir, trilateral.
metadata:
  version: "0.1.0"
  area: "Isencao de IRPF por Doenca Grave"
  tier: 1
---

# ANALISE TRILATERAL ISENCAO-IR

> Skill **Tier 1** — analisa o caso por **tres prismas** antes de produzir. Gera matriz de forcas, fragilidades e contra-teses. Acionada apos a triagem e a documental, antes da `linha-estrategica`.

---

## 0. PRE-REQUISITOS
- Triagem (4 requisitos) e `analise-documental-isencao-ir` concluidas; `jurisprudencia-isencao-ir` em andamento (ancoras Sum. 598/627).
- **Nao opinar sobre conduta clinica/diagnostico** (PA-04). Proteger dado sensivel (PA-10).

## 1. PRISMA CLIENTE (contribuinte)
O que **sustenta** a tese:
- Doenca **no rol taxativo** do art. 6, XIV (PA-05), com laudo/CID (doc. N).
- Rendimento e **provento** de aposentadoria/pensao/reforma (PA-06).
- **Retencao indevida** comprovada (informes/IR retido — doc. N), desde o marco.
- **Sum. 598** (prova flexivel, dispensa laudo oficial) e **Sum. 627** (manutencao em remissao) a favor.

## 2. PRISMA FAZENDA (a melhor objecao adversarial)
Antecipar a defesa **mais forte** da Uniao/fonte pagadora:
- A **doenca nao se enquadra** no rol taxativo (atacar pelo enquadramento).
- O **rendimento e de ATIVO** (salario/pro labore) — nao isento (PA-06).
- **Falta de contemporaneidade** dos sintomas ou ausencia de **laudo oficial** (rebatido por Sum. 627/598).
- **Restituicao alem de 5 anos** — prescricao quinquenal (CTN 168 — PA-09).
- **Marco da isencao** so a partir do laudo (limitar restituicao e efeitos).

## 3. PRISMA JUIZ
Como o caso aparece para quem decide:
- A prova da doenca esta clara e o pedido **bem delimitado** (so proventos, so 5 anos)?
- Ha sensibilidade humana sem comprometer a tecnica? O laudo convence sem violar sigilo (PA-10)?
- O calculo (`calculos-isencao-ir`) e verificavel? A tutela tem perigo concreto (desconto mensal)?

## 4. MATRIZ
```
PONTO              | FORCA (cliente)        | FRAGILIDADE           | CONTRA-TESE (neutralizar)
enquadramento rol  | doenca listada (doc N) | CID limitrofe         | Sum. 598 + laudo/exames
natureza provento  | carta concessao (docN) | parcela de ativo      | segregar; pedir so proventos
contemporaneidade  | -                      | doenca em remissao    | Sum. 627
periodo restituivel| 5 anos com IR retido   | competencias antigas  | limitar a CTN 168
marco da isencao   | inicio da doenca       | laudo posterior       | prova retroativa por outros meios
```

## 5. ENCERRAMENTO
Entrega a matriz trilateral (forcas x fragilidades x contra-teses) e a lista de objecoes da Fazenda ja antecipadas, insumo direto para a `linha-estrategica-isencao-ir`. Producao subsequente passa por `revisao-final-isencao-ir`.
