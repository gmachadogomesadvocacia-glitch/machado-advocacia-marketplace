---
name: analise-documental-tributaria
description: >
  Protocolo P2 — analise documental tributaria. Checklist de integridade dos documentos: auto de
  infracao, notificacao de lancamento, CDA (requisitos LEF art. 2º §5º/§6º + CTN art. 202), processo
  administrativo fiscal, guias DARF/DAE, escrituracao (SPED, EFD, ECD, ECF), notas fiscais, DIRPF,
  DCTF, GFIP, comprovantes de pagamento/parcelamento. Extrai os dados-chave (tributo, competencia,
  fato gerador, valor originario, multa, juros/SELIC, fundamento legal, sujeito passivo) e marca
  lacunas. Alimenta calculos e teses. Ative ao receber documentos fiscais para conferir antes de
  produzir. PA-03 (vedada alucinacao fatica) e PA-12 (sigilo fiscal).
metadata:
  version: "0.1.0"
  area: "Direito Tributario"
  tier: 1
---

# ANALISE DOCUMENTAL TRIBUTARIA (Protocolo P2)

> Tier 1 (Insumo). Confere a **integridade** dos documentos e extrai os dados-chave que alimentam `calculos-tributarios` e as teses. Nada de fato entra em peca sem lastro no documento (PA-03).

---

## 1. CHECKLIST POR DOCUMENTO

**Auto de infracao**
- Descricao do fato, capitulacao legal, tributo, competencia, valor, multa de oficio, intimacao valida, prazo de impugnacao.

**Notificacao de lancamento**
- Identificacao do sujeito passivo, criterio do lancamento, valor, data da ciencia (marco da decadencia/constituicao).

**CDA** (LEF art. 2º §5º e §6º; CTN art. 202)
- Nome/CPF-CNPJ do devedor e co-responsaveis; valor originario; termo inicial e forma de calculo dos juros e multa; origem, natureza e fundamento legal; numero do processo administrativo; data da inscricao. Falta de requisito → nulidade (alimenta `defesa-execucao-fiscal`).

**Processo administrativo fiscal**
- Tempestividade das defesas, acordaos DRJ/CARF, intimacoes, transito administrativo (constituicao definitiva → marco da prescricao).

**Guias e recolhimentos** — DARF, DAE, GPS: comprovam pagamento/extincao (CTN 156) ou parcelamento (suspensao, CTN 151 VI).

**Escrituracao** — SPED, EFD-Contribuicoes, EFD ICMS/IPI, ECD, ECF: base do credito, cruzamento com o lancamento.

**Obrigacoes acessorias** — DIRPF, DCTF, GFIP: a entrega de declaracao constitui o credito confessado (Sum. 436 STJ — validar, PA-01).

**Notas fiscais** — base de calculo, creditos, operacoes.

## 2. DADOS-CHAVE A EXTRAIR

```
TRIBUTO/ESFERA: ...
COMPETENCIA(S): ...
FATO GERADOR (data): ...
VALOR ORIGINARIO: ...
MULTA (mora x oficio): ...
JUROS / SELIC: ...
FUNDAMENTO LEGAL: ...
SUJEITO PASSIVO: ... (contribuinte / responsavel / socio)
CONSTITUICAO DEFINITIVA (data): ...
```

> A data do **fato gerador** rege a norma aplicavel (PA-04 — tempus regit actum; atencao a transicao da Reforma CBS/IBS). A data da **constituicao definitiva** abre a prescricao (PA-05).

## 3. LACUNAS

Marcar expressamente o que falta (CDA sem processo administrativo anexo, ausencia de comprovante de ciencia, escrituracao incompleta). Nao preencher por suposicao — PA-03. Listar pendencias para o operador suprir.

## 4. INTEGRACAO E SIGILO

- Saida alimenta `calculos-tributarios` (datas e valores) e o arsenal de teses.
- Documentos numerados "doc. N" e citados por numero (ver `estilo-juridico-tributario`).
- PA-12: dados fiscais sob sigilo (CTN 198 + LGPD) — guardar em `arquivos/`, nao versionar.
