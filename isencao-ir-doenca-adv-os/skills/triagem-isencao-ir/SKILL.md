---
name: triagem-isencao-ir
description: >
  TRIAGEM ISENCAO-IR — Skill Tier 1, porta de entrada. Verifica os 4 requisitos da isencao de IRPF
  por doenca grave (doenca no rol do art. 6 XIV; rendimento e PROVENTO de aposentadoria/pensao/reforma;
  fonte pagadora; periodo de retencao indevida) e a via (administrativa x judicial), abrindo o CASO.md.
  Acione em todo caso novo, quando o usuario pedir para enquadrar/analisar um caso de isencao de IR,
  ou antes de qualquer producao. Gatilhos: cliente aposentado com cancer/cardiopatia/doenca grave,
  IR retido no beneficio, quero pedir isencao, restituir o IR, parar o desconto do IR na aposentadoria.
metadata:
  version: "0.1.0"
  area: "Isencao de IRPF por Doenca Grave"
  tier: 1
---

# TRIAGEM ISENCAO-IR

> Skill **Tier 1** — porta de entrada. Confirma os 4 requisitos, decide a via e abre o `CASO.md`. Nenhuma producao comeca sem passar por aqui e pelo Selo P1.

---

## 0. PRE-CHECK
1. Procurar `isencao-ir/cowork-state.json` (subir a arvore). Ausente → sugerir `/start-isencao-ir`.
2. Procurar `CASO.md` do cliente em `isencao-ir/casos/<slug>/`. Existe → leia. Nao → criar ao fim.

## 1. OS 4 REQUISITOS (verificar TODOS)

### R1 — DOENCA no rol do art. 6, XIV
A moléstia esta na **lista taxativa**? (neoplasia maligna/cancer, cardiopatia grave, cegueira, Parkinson, esclerose multipla, nefropatia/hepatopatia grave, AIDS, hanseniase, paralisia irreversivel, etc.)
- **Fora do rol** → nao ha isencao por esta via (PA-05). Sinalizar.
- Conferir o **laudo medico** (data, CID, doenca). **Nao opinar sobre o diagnostico** (PA-04).

### R2 — RENDIMENTO e PROVENTO
A isencao so alcanca **proventos de aposentadoria, pensao ou reforma** (PA-06). 
- Rendimento de **trabalho ATIVO** → NAO isento (mesmo com a doenca). Sinalizar.
- Complementacao de aposentadoria (fundo de pensao) → isenta tambem.

### R3 — FONTE PAGADORA
Quem paga e retem o IR? INSS · RPPS (servidor) · fundo de pensao (EFPC) · ex-empregador. Define o requerimento administrativo e o polo passivo (a fonte + a Uniao/Fazenda Nacional).

### R4 — PERIODO DE RETENCAO INDEVIDA
Desde quando o IR foi retido apos o inicio da doenca? Define a **restituicao dos ultimos 5 anos** (CTN art. 168 — PA-09) e a cessacao futura.

## 2. VIA (Protocolo P5)
- **Administrativa:** requerimento de isencao a fonte pagadora + retificacao da DIRPF na Receita (restituicao). Mais rapida; depende de laudo de servico medico oficial.
- **Judicial:** declaratoria de isencao + repeticao de indebito (5 anos) + tutela para cessar a retencao. Sum. 598 STJ dispensa laudo oficial. Foro: domicilio do contribuinte (Justica Federal; JEF ate 60 SM).
- **Ambas (P4):** administrativa primeiro; recusa/silencio vira prova no judicial.

## 3. CHECKPOINT 1
```
ENQUADRAMENTO
- Doenca: [qual / no rol? sim-nao] · Laudo: [data/CID presentes? sim-nao]
- Rendimento: [provento aposentadoria/pensao/reforma? sim-nao]
- Fonte pagadora: [INSS/RPPS/fundo/ex-empregador]
- Retencao indevida desde: [data] → restituicao ~ [ultimos 5 anos]
- Via sugerida: [administrativa / judicial / ambas]
- Documentos presentes: [laudo · carta de concessao · informes de rendimento/IR retido · DIRPF]
```
Faltando dado essencial → `[INFORMAR]`, nunca inventar (PA-03).

## 4. GRAVAR + ROTEAR
Acione `memoria-de-caso-isencao-ir` para criar/atualizar o `CASO.md`. Depois: `validacao da norma (Selo P1)` → `analise-documental-isencao-ir` → `analise-trilateral-isencao-ir` + `jurisprudencia-isencao-ir` → `linha-estrategica-isencao-ir` → skill de producao da via.

## 5. ENCERRAMENTO
Entrega os 4 requisitos checados, a via definida e o CASO.md aberto. Sem Selo P1, nao avanca para producao.
