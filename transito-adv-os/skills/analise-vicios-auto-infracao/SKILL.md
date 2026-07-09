---
name: analise-vicios-auto-infracao
description: >
  Skill flagship Tier 2 — analise de vicios e nulidades do auto de infracao de transito (CTB 280-281; Resolucao CONTRAN). Ative ao analisar um auto de infracao, montar a defesa ou identificar nulidades.
metadata:
  version: "0.1.0"
  area: "Direito de Transito"
  tier: 2
---

# ANALISE DE VICIOS DO AUTO DE INFRACAO (CTB 280-281)

> Tier 2 flagship. O **motor da defesa**: as teses aqui levantadas alimentam todas as pecas (defesa previa, JARI, CETRAN, anulatoria, MS). Toda tese deve ser validada (PA-01/PA-02) e ancorada no documento (PA-03).

---

## 1. CATALOGO DE NULIDADES (checklist)

**A. Vicios formais do AIT (CTB 280)** — o auto deve conter:
- tipificacao da infracao; local, data e hora; caracteristicas do veiculo (placa, marca/especie); orgao/entidade e agente autuador (identificacao/assinatura); e, quando exigido, registro do equipamento.
- Falta/erro de dado essencial que impeca a defesa → nulidade. Mero erro material irrelevante nao anula (verificar a relevancia).

**B. Dupla notificacao (a tese mais comum) — Sum. 312 STJ**
- Sao DUAS notificacoes obrigatorias: **Notificacao de Autuacao (NA)** (abre prazo de defesa previa) e **Notificacao de Penalidade (NP)** (abre prazo de recurso).
- Ausencia de qualquer delas, ou envio fora do prazo, gera nulidade por cerceamento de defesa.
- **Prazo da NA:** a expedicao deve respeitar o prazo legal (CTB 281 § unico — em regra 30 dias; ultrapassado, **arquivamento** do auto).

**C. Cerceamento de defesa / ampla defesa (CTB 280-281; CF 5º LV)** — negativa de acesso, ausencia de motivacao na decisao, indeferimento imotivado de provas.

**D. Identificacao** — erro de placa, veiculo diverso, condutor nao identificado quando exigido (infracoes de responsabilidade do condutor).

**E. Equipamento/medidor (radar)** — ausencia de **certidao de aferição valida (INMETRO/IPEM)**, equipamento nao homologado, foto ilegivel, margem de tolerancia nao aplicada (ver `defesa-radar-equipamentos`).

**F. Sinalizacao** — ausencia/inadequacao da sinalizacao (velocidade, proibicao) exigida pelo CTB e CONTRAN.

**G. Competencia** — agente/orgao sem atribuicao para a via/infracao; bis in idem (dupla autuacao pelo mesmo fato).

**H. Decadencia/prescricao administrativa** — extrapolacao dos prazos do orgao para notificar/julgar.

## 2. METODO DE ANALISE

1. Conferir o AIT contra o rol do CTB 280 (dado a dado).
2. Verificar as DUAS notificacoes e suas datas/prazos (Sum. 312 — nucleo).
3. Checar equipamento → exigir aferição (se aplicavel).
4. Conferir sinalizacao e competencia.
5. Mapear a fase e o prazo (com `triagem-transito`).
6. Listar as teses por ordem de forca; separar **preliminares de nulidade** (formais) do **merito** (inexistencia do fato).

## 3. SAIDA

```
TESES DE NULIDADE (por forca):
1. [tese] — fundamento (CTB/Sum.) — onde no auto
2. ...
MERITO (se houver): ...
PROVAS A REQUERER: (aferição, imagens, sinalizacao)
INSTANCIA/PECA RECOMENDADA: ...
```

## 4. INTEGRACAO

- `analise-documental-transito` → conferir os documentos que embasam cada tese.
- `jurisprudencia-transito` → validar Sumulas (312, 127) e precedentes (PA-01).
- `calculos-transito` → prazos e pontuacao.
- Alimenta: `defesa-autuacao`, `recursos-administrativos`, `anulatoria-transito`, `mandado-seguranca-transito`.
- `revisao-final-transito` → R1-R4 antes de entregar.

## 5. CHECKLIST DE SAIDA

- [ ] AIT conferido contra o CTB 280 (dado a dado)
- [ ] Dupla notificacao verificada (NA + NP, datas/prazos — Sum. 312)
- [ ] Equipamento: aferição exigida quando cabivel
- [ ] Teses ordenadas por forca; preliminares x merito separados
- [ ] Nenhuma tese inventada (PA-01/PA-02) nem fato sem respaldo no auto (PA-03)
- [ ] Selo P1 feito · R1-R4 pendente
