---
name: jurisprudencia-criminal
description: >
  Jurisprudencia criminal Tier 1 — validacao jurisprudencial (PA-01). Ative para sumula, tema, precedente ou fundamentar peca penal.
metadata:
  version: "0.1.0"
  area: "Direito Penal e Processo Penal"
  tier: 1
---

# JURISPRUDENCIA CRIMINAL (PA-01)

> Tier 1. Localiza, **valida** e classifica a jurisprudencia penal antes da citacao. **Nunca** citar sumula/tema/precedente sem confirmar numero, orgao, teor e vigencia. Vetor interpretativo: presuncao de inocencia e garantias.

---

## 1. HIERARQUIA (peso decrescente)

```
STF — Sumula Vinculante (vincula todos) > Repercussao Geral (Tema) > Sumula simples
STJ — Recurso Repetitivo (Tema) > Sumula > acordao de Turma/Secao
TJ / TRF — precedente local (persuasivo)
```

- Sumula **vinculante** obriga juizes e administracao (CF 103-A).
- Tema de **repercussao geral** / **repetitivo** orienta as instancias (CPC 927 aplicado).
- Conflito de teses → prevalece o orgao superior e o enunciado mais recente.

## 2. PROTOCOLO DE VALIDACAO (antes de citar)

1. Confirmar **numero + orgao** (SV / Sum. STF / Sum. STJ / Tema).
2. Conferir o **teor literal** e se nao foi cancelada/superada.
3. Verificar **pertinencia** ao caso concreto (nao forcar enquadramento).
4. Marcar **"validar"** quando houver qualquer duvida.
5. Em divergencia entre fontes → registrar e usar a de maior hierarquia.

> **PA-01:** alucinacao jurisprudencial e vedacao absoluta. Sem confirmacao, nao cita.

## 3. SUMULAS CONSAGRADAS (sempre validar antes de usar)

| Enunciado | Tema | Uso |
|-----------|------|-----|
| **SV 11 STF** | Algemas | uso excepcional e fundamentado; nulidade/responsabilidade se abusivo |
| **SV 14 STF** | Acesso do defensor | direito de acesso aos elementos ja documentados do IP |
| **SV 24 STF** | Crime tributario material | so apos lancamento definitivo do tributo (Lei 8.137 I) |
| **Sum. 691 STF** | HC | nao cabe HC contra indeferimento de liminar — salvo flagrante ilegalidade |
| **Sum. 231 STJ** | Dosimetria | atenuante nao reduz a pena abaixo do minimo legal |
| **Sum. 444 STJ** | Pena-base | inqueritos/acoes em curso nao agravam (presuncao de inocencia) |
| **Sum. 269 STJ** | Regime | admite regime semiaberto a reincidente, pena ate 4 anos, favoraveis as CJ |
| **Sum. 440 STJ** | Regime | vedado regime mais gravoso so pela gravidade abstrata do crime |

> Lista de apoio — confirmar teor e vigencia caso a caso. Nao presumir Tema/numero nao listado.

## 4. COMO PESQUISAR E APRESENTAR

- Buscar pelo **instituto** (ex.: dosimetria → Sum. 231/444; regime → Sum. 440/719; HC → Sum. 691).
- Apresentar: **orgao + numero + teor + pertinencia** ao caso; sinalizar "validar".
- Distinguir enunciado **vigente** de **superado**; conferir overruling.

## 5. PROIBICOES E INTEGRACAO

- **PA-01** — sem validacao, nao cita. **PA-04** — respeitar lei penal no tempo na escolha do precedente.
- Vetor: in dubio pro reo e presuncao de inocencia (PA-07).
- Alimenta `analise-trilateral-criminal`, `linha-estrategica-criminal` e as skills de producao.
- Passa por `revisao-final-criminal` (R2) antes da entrega.
