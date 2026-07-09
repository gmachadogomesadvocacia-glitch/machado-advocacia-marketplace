---
name: execucao-penal
description: >
  Skill Tier 2 — execucao penal (LEP 7.210/84). Ative em progressao, regressao, livramento condicional, remicao, falta grave, detracao, saida temporaria, indulto, agravo em execucao, LEP.
metadata:
  version: "0.1.0"
  area: "Direito Penal e Processo Penal"
  tier: 2
---

# EXECUCAO PENAL (LEP 7.210/84)

> Tier 2. Fase de cumprimento da pena. Competencia do **juizo da execucao** (LEP 66). Recurso proprio: **agravo em execucao** (LEP 197), sem efeito suspensivo, prazo 5 dias. Polo: defesa. Selo P1 antes de produzir.

---

## 1. PROGRESSAO DE REGIME (LEP 112, red. Lei 13.964/2019)

Requisito **objetivo** (lapso por fracao) **+** subjetivo (**bom comportamento carcerario** atestado pelo diretor). Fracoes principais:

| Fracao | Situacao |
|--------|----------|
| **16%** | Crime sem violencia/grave ameaca, **primario** |
| **20%** | Crime sem violencia/grave ameaca, **reincidente** |
| **25%** | Crime **com** violencia/grave ameaca, primario |
| **30%** | Crime com violencia/grave ameaca, reincidente |
| **40%** | **Hediondo/equiparado**, primario |
| **50%** | Hediondo primario com resultado morte (vedado livramento); reincidente nao especifico em hediondo |
| **60%** | Hediondo reincidente |
| **70%** | Hediondo reincidente com resultado morte (vedado livramento) |

> Progressao e ato judicial, vedada progressao por salto (Sum. 491 STJ — validar). Exame criminologico pode ser exigido por decisao fundamentada (Sum. Vinc. 26 STF / Sum. 439 STJ — validar).

## 2. REGRESSAO (LEP 118)

- Pratica de fato definido como crime doloso, **falta grave**, ou frustracao do fim da execucao; condenacao por crime anterior cuja pena somada torne incabivel o regime.
- Exige **oitiva previa** do sentenciado (LEP 118 §2º — contraditorio).

## 3. LIVRAMENTO CONDICIONAL (CP 83)

- Pena ≥ 2 anos; cumprido **mais de 1/3** (primario, bons antecedentes), **mais de 1/2** (reincidente doloso), **mais de 2/3** (hediondo, vedado a reincidente especifico); reparacao do dano salvo impossibilidade; bom comportamento; (para crime com violencia) constatacao de cessada periculosidade.

## 4. REMICAO (LEP 126)

- **Trabalho**: 1 dia de pena a cada 3 dias trabalhados. **Estudo**: 1 dia a cada 12 horas (3 dias). **Leitura**: parametros do CNJ/jurisprudencia (validar). Cumulaveis trabalho + estudo.
- **Falta grave**: o juiz **pode** revogar ate **1/3** do tempo remido (**LEP art. 127**, pos-Lei 12.433/2011), recomecando a contagem.

## 5. SAIDAS TEMPORARIAS E TRABALHO EXTERNO

- **Saida temporaria** (LEP 122-125): regime semiaberto, 1/6 da pena (primario) ou 1/4 (reincidente), bom comportamento, compatibilidade.
- **Trabalho externo** (LEP 36-37): inclusive no fechado em obra/servico publico, com 1/6 cumprido.

## 6. FALTA GRAVE (LEP 50-52)

- Rol: fuga, posse de instrumento de crime, descumprimento de trabalho/ordem, posse de celular, etc.
- **Consequencias**: regressao, perda de ate 1/3 da remicao, alteracao da data-base para **novos** beneficios (Sum. 534/535 STJ — validar; falta grave **nao** interrompe lapso para livramento, indulto e comutacao — validar). Exige **PAD** e oitiva (contraditorio).

## 7. DETRACAO, UNIFICACAO, INDULTO

- **Detracao** (CP 42): desconta na pena o tempo de prisao provisoria, administrativa e internacao.
- **Unificacao/soma** (CP 75; LEP 111): limite de cumprimento (40 anos — Lei 13.964/19); unificacao de penas e crimes continuados.
- **Indulto/comutacao**: decreto presidencial anual — conferir requisitos do decreto vigente (PA-02/PA-03 — nao presumir).

## 8. ESTRUTURA DO PEDIDO / AGRAVO

**Pedido incidental**: enderecamento (juizo da execucao) · qualificacao e dados da execucao (autos, pena, regime, data-base) · do direito (requisito objetivo demonstrado por calculo + subjetivo por atestado) · pedido · documentos (guia, atestado de conduta, calculo de pena).
**Agravo em execucao** (LEP 197): interposicao + razoes em 5 dias, sem efeito suspensivo (rito do RESE).

## 9. INTEGRACAO

- `calculos-criminais` → **calculo de pena, lapsos, detracao, remicao** (eixo central).
- `jurisprudencia-criminal` → validar sumulas (491, 534, 535, Vinc. 26 — PA-01).
- `analise-documental-criminal` → guia de execucao, atestados, PAD.
- `estilo-juridico-criminal` → forma · `revisao-final-criminal` → R1-R4.

## 10. CHECKLIST DE SAIDA

- [ ] Fracao do art. 112 correta (tipo de crime x reincidencia)
- [ ] Requisito subjetivo (bom comportamento/atestado) demonstrado
- [ ] Calculo de pena/data-base conferido (calculos-criminais)
- [ ] Efeito da falta grave aplicado corretamente (Sum. 535 — PA-01)
- [ ] Competencia do juizo da execucao (LEP 66)
- [ ] Indulto/comutacao conferidos no decreto vigente (PA-03)
- [ ] Polo coerente (PA-10) · Selo P1 feito · R1-R4 pendente
