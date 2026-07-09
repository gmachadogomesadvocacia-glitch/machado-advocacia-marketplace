---
name: analise-documental-usucapiao
description: >
  ANALISE DOCUMENTAL USUCAPIAO — Tier 1 (P2). Inventaria e testa a integridade dos documentos (matricula/RI, planta e memorial com ART, comprovantes de posse, certidoes, confrontantes/anuencias); monta o mapa 'doc. N' e marca faltantes. Acione quando o usuario entregar documentos, mencionar matricula, planta, memorial, ART, IPTU, anuencia de confrontante, ou pedir para conferir a documentacao.
metadata:
  version: "0.1.0"
  area: "Usucapiao (Judicial e Extrajudicial)"
  tier: 1
---

# ANALISE DOCUMENTAL USUCAPIAO (P2)

> Skill **Tier 1** — operacionaliza o Protocolo P2 (Integridade Documental). Inventaria, testa a integridade e monta o mapa "doc. N". Roda apos a triagem e alimenta a analise de posse e a producao.

---

## 0. PRE-CHECK
- Caso triado (`triagem-usucapiao`) e `CASO.md` aberto.
- Converter PDFs com `pdf-para-md` antes de analisar (economia de tokens). PDFs/matricula: no Code, converter com `ferramentas/pdf-para-md/` antes de analisar.
- Nada inventado (PA-03): documento ausente vira `[INFORMAR]`, nunca presumido.

## 1. INVENTARIO (o que precisa existir)
1. **Matricula / certidao do RI** — quem e o **titular registral**? ha **onus** (hipoteca, penhora, indisponibilidade)? o imovel **tem registro** ou e nao registrado? **e BEM PUBLICO?** (PA-04 — se publico, nao usucape; sinaliza e para).
2. **Planta e memorial descritivo** com **ART/RRT** do profissional (essencial em ambas as vias; indispensavel no extrajudicial — PA-07).
3. **Comprovantes de posse:** IPTU em nome do possuidor, **contas de luz/agua**, benfeitorias (notas, fotos), contratos, declaracoes de vizinhos.
4. **Certidoes dos distribuidores** (acoes possessorias/reivindicatorias que toquem a posse — interrupcao/oposicao?).
5. **Confrontantes** — identificacao de cada um (e respectivos conjuges) e suas **anuencias** (decisivo no extrajudicial; rol de citacao no judicial — PA-06).

## 2. TESTE DE INTEGRIDADE
- Coerencia entre **matricula × planta × memorial** (metragem, confrontacoes, descricao).
- Posse coberta no tempo pelos comprovantes (cadeia sem lacunas; ha **accessio possessionis**?).
- Titular registral resiste ou anuiu? Confrontantes anuiram?
- Documento ilegivel/parcial → `[INFORMAR]`.

## 3. MAPA "doc. N"
Numerar cada documento e citar por numero (sem rol; docs numerados antes do protocolo):
```
doc. 1 — matricula nº ... (titular: ...; onus: ...)
doc. 2 — planta + memorial + ART nº ...
doc. 3 — IPTU 20xx–20xx
doc. 4 — contas de luz/agua
doc. 5 — certidoes dos distribuidores
doc. N — anuencia do confrontante ...
```

## 4. CHECKPOINT 2 (parcial)
```
INTEGRIDADE DOCUMENTAL
- Matricula/RI: [titular · onus · registrado? · BEM PUBLICO? sim-nao]
- Planta+memorial+ART: [presente / INFORMAR]
- Comprovantes de posse: [IPTU · contas · benfeitorias · ...]
- Distribuidores: [oposicao? · interrupcao?]
- Confrontantes: [identificados? · anuencias?]
- Faltantes: [INFORMAR ...]
```

## 5. ENCERRAMENTO
Entrega o inventario, o teste de integridade e o mapa "doc. N", com faltantes marcados. Bem publico ou titular resistente sinalizado. Alimenta `analise-posse-usucapiao`. Producao so depois do Selo P1; ao final, toda peca vai a `revisao-final-usucapiao`.
