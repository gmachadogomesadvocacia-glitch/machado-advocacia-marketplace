---
name: triagem-usucapiao
description: >
  TRIAGEM USUCAPIAO — Tier 1, porta de entrada. Classifica a demanda em 4 dimensoes (polo; judicial x extrajudicial; modalidade; urbano/rural) e faz o pre-check da posse, abrindo o CASO.md. Acione em todo caso novo, quando o usuario pedir para enquadrar a demanda ou decidir a via. Gatilhos: quero usucapir, moro ha anos num terreno sem documento, regularizar imovel, usucapiao em cartorio, confrontante quer me processar.
metadata:
  version: "0.1.0"
  area: "Usucapiao (Judicial e Extrajudicial)"
  tier: 1
---

# TRIAGEM USUCAPIAO

> Skill **Tier 1** — porta de entrada. Classifica em 4 dimensoes, faz o pre-check da posse e abre o `CASO.md`. Nenhuma producao comeca sem passar por aqui e pelo Selo P1.

---

## 0. PRE-CHECK
1. Procurar `usucapiao/cowork-state.json` (subir a arvore). Ausente → sugerir `/start-usucapiao`.
2. Procurar `CASO.md` do cliente em `usucapiao/casos/<slug>/`. Existe → leia. Nao → criar ao fim.

## 1. CLASSIFICACAO 4D

### Dimensao 1 — POLO
- **Usucapiente** (autor) — quem pede o reconhecimento da propriedade pela posse.
- **Confrontante / oponente / reu** — quem se opoe (defesa).
> Sem polo, pare e pergunte (PA-10).

### Dimensao 2 — VIA
- **Judicial** — quando ha **litigio/oposicao**, reu incerto, ente publico envolvido, ou falta de anuencia dos confrontantes.
- **Extrajudicial (cartorio)** — CPC art. 1.071 + Lei 6.015 art. 216-A + Provimento CNJ: exige **consenso** (anuencia dos confrontantes e titulares), ata notarial, planta+ART. Havendo oposicao → vai para judicial (PA-07).

### Dimensao 3 — MODALIDADE (define os requisitos)
Extraordinaria (1.238) · Ordinaria (1.242 — justo titulo+boa-fe) · Especial urbana (1.240/CF 183 — 250m2) · Especial rural (1.239/CF 191 — 50ha) · Familiar (1.240-A — 2 anos) · Coletiva (Estatuto da Cidade). A definicao final e da `analise-posse-usucapiao`.

### Dimensao 4 — IMOVEL
Urbano x rural · com matricula (e de quem?) x sem registro · metragem · confrontantes (quem sao?) · ha registro publico/bem publico? (**bem publico nao e usucapivel — PA-04**).

## 2. PRE-CHECK DA POSSE (P4)
- **Tempo** de posse (suficiente para a modalidade?).
- **Qualidade:** mansa, pacifica, continua, ininterrupta, com **animus domini**? (PA-08)
- **Nao e mera detencao** (comodato/locacao/permissao nao usucapem — PA-09)?
- Justo titulo e boa-fe (se ordinaria)?
- Atos possessorios comprovaveis (IPTU, contas, benfeitorias, testemunhas)?

## 3. CHECKPOINT 1
```
ENQUADRAMENTO
- Polo: [usucapiente / confrontante]
- Via: [judicial / extrajudicial] (+ motivo)
- Modalidade provavel: [...]
- Imovel: [urbano/rural · matricula? · metragem · bem publico? sim-nao]
- Posse: [tempo · animus domini? · detencao? · justo titulo/boa-fe?]
- Confrontantes/entes a citar/anuir: [...]
- Documentos presentes: [matricula · planta+ART · comprovantes de posse · anuencias]
```
Faltando dado essencial → `[INFORMAR]`, nunca inventar (PA-03).

## 4. GRAVAR + ROTEAR
Acione `memoria-de-caso-usucapiao` (CASO.md). Depois: Selo P1 → `analise-documental-usucapiao` + `analise-posse-usucapiao` → `analise-trilateral-usucapiao` + `jurisprudencia-usucapiao` → `linha-estrategica-usucapiao` → producao da via.

## 5. ENCERRAMENTO
Entrega as 4 dimensoes, o pre-check da posse e o CASO.md aberto. Sem Selo P1, nao avanca.
