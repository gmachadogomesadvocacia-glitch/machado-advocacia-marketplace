---
name: recursos-criminais
description: >
  Skill Tier 2 — sistema recursal penal. Cobre apelacao (CPP 593 — sentenca condenatoria/absolutoria; interposicao em 5 dias, razoes em 8), recurso em sentido estrito / RESE (CPP 581 — rol taxativo: rejeicao da denuncia, pronuncia, decisoes interlocutorias; 5 dias + razoes em 2), embargos de declaracao (CPP 619 — omissao, contradicao, ambiguidade, obscuridade; 2 dias), embargos infringentes e de nulidade (CPP 609 § unico — quando ha voto vencido pro reu), recurso ordinario em HC (RHC) e nota sobre REsp/RE e agravo em recurso especial/extraordinario. Ative em apelacao, RESE, embargos, recurso criminal, prazo recursal, voto vencido, reformatio in pejus.
metadata:
  version: "0.1.0"
  area: "Direito Penal e Processo Penal"
  tier: 2
---

# RECURSOS CRIMINAIS

> Tier 2. Mapeia o recurso cabivel, o prazo e o efeito. Erro de via ou de prazo e fatal. Polo conforme o cliente (PA-10). Selo P1 antes de produzir; prazo recursal e materia critica.

---

## 1. QUADRO DOS RECURSOS

| Recurso | Cabimento | Prazo (interp. / razoes) | Base |
|---------|-----------|--------------------------|------|
| **Apelacao** | Sentenca definitiva (cond./absolut.); decisoes do juri | **5 / 8 dias** | CPP 593, 600 |
| **RESE** | Rol taxativo do CPP 581 (rejeicao denuncia, pronuncia, etc.) | **5 / 2 dias** | CPP 581, 588 |
| **Embargos de declaracao** | Omissao, contradicao, ambiguidade, obscuridade | **2 dias** | CPP 619-620 |
| **Embargos infringentes/nulidade** | Acordao **nao unanime** desfavoravel ao reu | **10 dias** | CPP 609 § unico |
| **RHC** | Denegacao de HC por tribunal | **5 dias** | CF 105 II a / CPP 30 RISTJ |
| **REsp / RE** | Violacao a lei federal / Constituicao (acordao final) | **15 dias** | CF 105 III / 102 III |
| **Agravo em REsp/RE** | Inadmissao na origem | **15 dias** | art. 1.042 CPC |

## 2. APELACAO (CPP 593)

- Cabe da **sentenca** condenatoria ou absolutoria (I) e das decisoes definitivas/com forca de definitiva (II); contra **decisao do juri**, so nas hipoteses do III (a-d).
- **Efeito**: devolutivo amplo (tantum devolutum quantum appellatum); a condenatoria, em regra, **nao impede** a execucao apos transito (presuncao de inocencia — PA-07).
- Interposicao por petição/termo (5 dias); razoes em 8 dias (CPP 600). Possivel apresentar razoes na superior instancia (CPP 600 §4º).

## 3. RECURSO EM SENTIDO ESTRITO (CPP 581)

- **Rol taxativo** (interpretacao estrita) — ex.: I rejeicao da denuncia; IV pronuncia; decisoes que decretam/denegam prisao, julgam incidentes, etc.
- **Juizo de retratacao** (CPP 589) — o juiz pode reformar a decisao.
- Sobe **por instrumento ou nos proprios autos** conforme a hipotese.

## 4. EMBARGOS DE DECLARACAO (CPP 619)

- Sanam **omissao, contradicao, ambiguidade ou obscuridade**; **2 dias**.
- **Prequestionam** materia para REsp/RE. Interrompem o prazo dos demais recursos.
- Efeitos infringentes so excepcionalmente.

## 5. EMBARGOS INFRINGENTES E DE NULIDADE (CPP 609 § unico)

- Cabem **so para a defesa**, contra **acordao nao unanime** desfavoravel ao reu; limitados a **materia objeto da divergencia** (voto vencido pro reu).
- Prazo de 10 dias.

## 6. REFORMATIO IN PEJUS (CPP 617)

- **Vedada** a agravacao da pena em recurso **exclusivo da defesa**.
- **Reformatio in pejus indireta**: anulada a sentenca por recurso so da defesa, a nova nao pode ser mais gravosa (Sum. - validar).
- No juri, a soberania dos veredictos relativiza (tema controverso — validar).

## 7. RHC, REsp E RE

- **RHC**: denegada a ordem de HC por TJ/TRF → STJ; por STJ → STF. Via mais ampla que REsp para materia de liberdade.
- **REsp/RE**: cabem do acordao de unica/ultima instancia; exigem **prequestionamento** e demonstracao de violacao a lei federal (REsp) ou a CF + repercussao geral (RE). Inadmitidos → **agravo** (art. 1.042 CPC).

## 8. ESTRUTURA (cada recurso)

Peticao de **interposicao** (enderecada ao juizo a quo, tempestiva) + **razoes** (enderecadas ao tribunal ad quem): sintese · tempestividade e cabimento · do direito (erro in judicando/in procedendo) · pedido (reforma/anulacao) · prequestionamento quando for REsp/RE.

## 9. INTEGRACAO

- `calculos-criminais` → prazos, prescricao, redimensionamento de pena.
- `jurisprudencia-criminal` → validar sumulas/teses (PA-01).
- `analise-documental-criminal` → sentenca/acordao recorrido, autos.
- `estilo-juridico-criminal` → forma · `revisao-final-criminal` → R1-R4.

## 10. CHECKLIST DE SAIDA

- [ ] Via recursal correta (apelacao x RESE x embargos)
- [ ] Prazo de interposicao e de razoes controlado
- [ ] Efeito identificado (suspensivo/devolutivo/regressivo)
- [ ] Reformatio in pejus observada (CPP 617) quando recurso so da defesa
- [ ] Prequestionamento, se REsp/RE
- [ ] Embargos infringentes so com voto vencido pro reu (CPP 609)
- [ ] Polo coerente (PA-10) · Selo P1 feito · R1-R4 pendente
