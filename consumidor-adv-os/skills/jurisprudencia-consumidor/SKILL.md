---
name: jurisprudencia-consumidor
description: >
  JURISPRUDENCIA CONSUMIDOR — Skill Tier 1, apoio ao Selo P1. Faz a busca viva, a validacao e a
  classificacao de precedentes consumeristas/bancarios em 3 niveis (VALIDADA / [VERIFICAR] /
  IMPOSSIBILIDADE). PA-01: nunca citar sumula/Tema sem validar — sem confirmacao, marcar [VERIFICAR].
  Acione sempre que uma peca, parecer ou tese precisar de fundamento jurisprudencial, quando o usuario
  pedir sumula/Tema/precedente, ou quando outra skill devolver um [VERIFICAR]. Gatilhos: jurisprudencia,
  sumula, Tema repetitivo, STJ, STF, precedente, entendimento dos tribunais, ha sumula sobre, qual o
  Tema, validar jurisprudencia, Sumula 385/530/539, dobro do art. 42, Convencao de Montreal.
metadata:
  version: "0.1.0"
  area: "Direito do Consumidor e Bancario"
  tier: 1
---

# JURISPRUDENCIA CONSUMIDOR

> Skill **Tier 1** — apoia o **Protocolo P1 (Selo de Validacao Legal Previa)**. Localiza, **valida** e classifica precedentes. Nenhuma sumula ou Tema entra numa peca sem passar por aqui (**PA-01**).

---

## 0. QUANDO ACIONAR

Sempre que uma tese exigir lastro jurisprudencial; quando o usuario pede sumula/Tema/precedente; quando `analise-contratual`, `calculos` ou uma skill de producao devolve um `[VERIFICAR]`. E pre-requisito do Selo P1 para qualquer citacao de tribunal.

## 1. PRINCIPIO — PA-01

**Proibida a alucinacao jurisprudencial.** Numero de sumula, Tema repetitivo, IRDR ou ementa so se citam **apos validacao**. Sem confirmacao da existencia e do teor atual, **marcar `[VERIFICAR]`** e jamais afirmar como assentado. Inventar precedente e violacao nuclear.

---

## 2. BUSCA VIVA

Use **WebSearch / WebFetch** quando disponiveis para confirmar existencia, teor e vigencia (sumula nao cancelada, Tema com tese fixada/transito). Fontes primarias: portais do **STF** e **STJ** (jurisprudencia, repetitivos, sumulas), depois TJ local e demais TJs. Sem ferramenta de busca ou sem confirmacao segura → o item permanece `[VERIFICAR]`; nunca preencher de memoria.

## 3. CLASSIFICACAO EM 3 NIVEIS

- **VALIDADA** — existencia, numero e teor confirmados em fonte confiavel; vigente e pertinente ao caso. Pode citar.
- **`[VERIFICAR]`** — plausivel mas nao confirmada (sem ferramenta, sem fonte, ou teor duvidoso). Entra no texto so com a marca `[VERIFICAR]`; nao serve de fundamento ate validar.
- **IMPOSSIBILIDADE** — buscada e nao encontrada, cancelada ou superada. **Nao citar**; registrar a impossibilidade e buscar fundamento alternativo (lei, principio, doutrina).

## 4. HIERARQUIA (peso do precedente)

```
STF (repercussao geral / vinculante)
  > STJ (recurso repetitivo / sumula)
    > STJ (turmas, sem repetitivo)
      > TJ local (do foro do caso)
        > demais TJs (persuasivo)
```

Priorize o nivel mais alto e o **foro do caso**. Repetitivo/RG tem forca quase normativa; turma e TJ sao persuasivos.

---

## 5. MAPA-BASE POR EIXO (pontos de partida — VALIDAR antes de citar)

> Lista de **rastreamento**, nao de citacao automatica. Cada item exige confirmacao (Secao 2) antes de virar fundamento; ate la, `[VERIFICAR]`.

### Negativacao
- **Sum. 297 STJ** — CDC aplica-se as instituicoes financeiras.
- **Sum. 359** — cabe ao orgao mantenedor do cadastro notificar previamente.
- **Sum. 385** — preexistindo inscricao legitima, nao ha dano moral pela inscricao irregular (so cancelamento). **Cheque sempre (PA-07).**
- **Sum. 404** — desnecessario AR na notificacao previa.

### Bancario / cobranca
- **Sum. 472** — comissao de permanencia nao cumula com correcao/juros/multa.
- **Sum. 479** — responsabilidade objetiva do banco por fraude/fortuito interno.
- **Sum. 530** — taxa media de mercado como parametro de abusividade dos juros.
- **Sum. 539 / 541** — capitalizacao admitida se expressamente pactuada.
- **Tema 929 STJ** — repeticao em **dobro** do art. 42 § un. independe de dolo, mas exige conduta contraria a boa-fe (engano injustificavel). **Cheque (PA-06).**

### Consumo / distrato
- **Sum. 543** — no distrato, restituicao das parcelas pagas (retencao so do razoavel).

### Aereo
- **Tema 210 STF** — Convencao de Montreal prevalece sobre o CDC para indenizacao **material** no transporte aereo **internacional** (extravio/atraso); dano moral segue o CDC.

> Numeros podem mudar (cancelamento/revisao). Trate este mapa como hipotese a confirmar.

---

## 6. SAIDA

Para cada tese do caso, entregue:

```
TESE: [ex.: dano moral por negativacao indevida]
- Precedente: Sum. 385 STJ — NIVEL: STJ/sumula — STATUS: [VALIDADA | [VERIFICAR] | IMPOSSIBILIDADE]
- Teor (validado): ...
- Aplicacao ao caso: favoravel/contraria; como incide; ressalva
```

## 7. ENCERRAMENTO

Devolve precedentes **classificados** (nivel + status) e a leitura de como aplicam ao caso, com tudo nao confirmado marcado `[VERIFICAR]` (PA-01). Alimenta o Selo P1, a `analise-contratual`, a `linha-estrategica` e a redacao; a `revisao-final-consumidor` (R2) confere se nada entrou sem validacao.
