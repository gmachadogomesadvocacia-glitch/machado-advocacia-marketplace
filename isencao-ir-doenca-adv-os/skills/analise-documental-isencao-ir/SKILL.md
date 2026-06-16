---
name: analise-documental-isencao-ir
description: >
  ANALISE DOCUMENTAL ISENCAO-IR — Skill Tier 1 (Protocolo P2). Inventaria e checa a integridade dos
  documentos do caso: laudo medico (data, CID, doenca do rol, se e de servico medico oficial), carta
  de concessao do beneficio, informes de rendimentos / comprovantes de IR retido (base do calculo da
  restituicao) e DIRPF dos ultimos 5 anos. Monta o mapa "doc. N", sinaliza faltante [INFORMAR] e nao
  analisa sem doc essencial. NAO opina sobre o diagnostico (PA-04). Protege dado de saude sensivel
  (PA-10). Acione apos a triagem, para preparar calculo, trilateral e producao. Gatilhos: laudo, CID,
  informe de rendimentos, comprovante de IR retido, carta de concessao, DIRPF, documentos do caso.
metadata:
  version: "0.1.0"
  area: "Isencao de IRPF por Doenca Grave"
  tier: 1
---

# ANALISE DOCUMENTAL ISENCAO-IR

> Skill **Tier 1** — Protocolo P2 (Integridade Documental). Inventaria os documentos, checa integridade, monta o mapa "doc. N". Sem documento essencial, **nao analisa** — sinaliza o que falta.

---

## 0. PRE-CHECK
- `CASO.md` aberto pela `triagem-isencao-ir`? Senao, retornar a triagem.
- Converter PDFs do processo/laudo antes de ler (ferramenta `pdf-para-md`), para economia de tokens.
- PDFs (laudo/informe de rendimentos): no Code, converter com `ferramentas/pdf-para-md/` antes de analisar.

## 1. DOCUMENTOS ESSENCIAIS (inventario)

### D1 — LAUDO MEDICO
- **Data**, **CID** e **doenca**: a moléstia esta no rol do art. 6, XIV? (conferir com a triagem — R1).
- E de **servico medico oficial** (Uniao/Estado/Municipio)? **Exigencia da via administrativa**; no judicial e **dispensavel** (Sum. 598 STJ — PA-07). Registrar qual.
- **NAO opinar sobre o diagnostico nem sobre a conduta clinica** (PA-04) — o laudo e do medico; aqui so se afere a presenca e a forma do documento.

### D2 — CARTA DE CONCESSAO DO BENEFICIO
Comprova que o rendimento e **provento** de aposentadoria/pensao/reforma (PA-06) e identifica a **fonte pagadora** (INSS/RPPS/fundo/ex-empregador) e o inicio do beneficio.

### D3 — INFORMES DE RENDIMENTOS / COMPROVANTES DE IR RETIDO
**Base do calculo da restituicao.** Sem eles, `calculos-isencao-ir` NAO calcula. Conferir competencia a competencia o IR retido na fonte.

### D4 — DIRPF (ultimos 5 anos)
Declaracoes do periodo restituivel (CTN art. 168 — PA-09). Suportam a retificacao na via administrativa e delimitam o indebito.

## 2. MAPA "doc. N"
Numerar os documentos presentes na ordem de citacao da peca:
```
doc. 1 — laudo medico [data / CID / oficial? S-N]
doc. 2 — carta de concessao [fonte / inicio]
doc. 3 — informes de rendimento / IR retido [competencias]
doc. 4 — DIRPF [anos]
```

## 3. FALTANTES E INTEGRIDADE
- Documento essencial ausente → `[INFORMAR]` explicito; **nao prosseguir** para calculo/producao sem ele (PA-11). Nunca inventar dado (PA-03).
- Apontar inconsistencias (CID divergente do informado, periodo sem informe, laudo posterior ao marco pretendido).

## 4. PROTECAO DO DADO SENSIVEL (PA-10)
Diagnostico/CID = dado de saude **sensivel** (LGPD art. 11). Manusear o minimo necessario; sinalizar segredo de justica na producao; nao replicar CID fora do indispensavel.

## 5. ENCERRAMENTO
Entrega o inventario com o mapa "doc. N", o status de integridade e a lista de `[INFORMAR]`. Encaminha para `calculos-isencao-ir` (se ha comprovantes de retencao) e `analise-trilateral-isencao-ir`. Para producao, passar por `revisao-final-isencao-ir`.
