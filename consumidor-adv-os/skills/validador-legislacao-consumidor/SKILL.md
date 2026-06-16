---
name: validador-legislacao-consumidor
description: >
  VALIDADOR DE LEGISLACAO CONSUMERISTA — Skill Tier 1 (Protocolo P1). Emite o Selo de Validacao
  Legal Previa antes de qualquer producao: confirma a vigencia do CDC e da lei especial aplicavel
  (telecom/ANATEL, aereo/ANAC e Montreal, bancario/BACEN, L14.181 superendividamento, e-commerce),
  valida sumulas e Temas do STJ pelo marco temporal do fato gerador e sinaliza o que precisa de
  verificacao viva. Acione ANTES de qualquer peca, defesa, calculo ou parecer; quando o usuario
  pedir para conferir norma/sumula/Tema; ou quando houver duvida de vigencia. Nenhuma skill de
  producao roda sem o Selo EMITIDO.
metadata:
  version: "0.1.0"
  area: "Direito do Consumidor e Bancario"
  tier: 1
---

# VALIDADOR DE LEGISLACAO CONSUMERISTA (Selo P1)

> Skill **Tier 1** — operacionaliza o **Protocolo P1**. Nenhuma producao comeca sem o **Selo de Validacao Legal Previa** emitido aqui. Combate a alucinacao normativa e jurisprudencial (PA-01, PA-02).

---

## 0. FUNCAO

Travar a base normativa do caso ANTES de redigir: (a) qual lei rege o eixo; (b) ela estava vigente no fato gerador; (c) quais sumulas/Temas se aplicam e estao atuais; (d) o que exige verificacao viva. Saida = um **Selo** gravado no `CASO.md`.

## 1. MARCO TEMPORAL (fato gerador)

Identifique a **data do fato** (contratacao, cobranca, inscricao, voo, compra, defeito). A norma vigente a epoca rege o caso (regra geral). Atencao a alteracoes do CDC (ex.: L14.181/2021 — superendividamento) e a teses moduladas pelo STJ.

## 2. CHECKLIST POR EIXO

| Eixo | Normas a confirmar |
|------|--------------------|
| Bancario | CDC + Sum. 297 (CDC aplica-se a bancos), 379/530/382 (taxa media BACEN), 539/541 (capitalizacao), 472 (comissao de permanencia); MP 2.170-36; resolucoes CMN/BACEN |
| Negativacao | CDC art. 43; Sum. 323/359/385/404 STJ; Lei 12.414 (cadastro positivo) |
| Telecom | CDC + Lei 9.472 + regulamentos ANATEL; Sum. 356 |
| Serv. essenciais | CDC + Lei 8.987 (corte) + jurisprudencia (essencialidade) |
| Aereo | CDC + Codigo Brasileiro de Aeronautica + Res. ANAC 400 + Conv. Montreal (Tema 210 STF — Montreal prevalece sobre CDC no extravio material) |
| Vicio/fato produto | CDC art. 12-27 (decadencia 26 / prescricao 27) |
| E-commerce | CDC art. 49 + Decreto 7.962/2013 |
| Publicidade | CDC art. 36-38 |
| Clausula abusiva | CDC art. 51 (rol exemplificativo) |
| Cobranca/indebito | CDC art. 42 + Tema 929 STJ (dobro independe de ma-fe, exige engano injustificavel — EAREsp 676.608) |
| Superendividamento | L14.181/2021 + Decreto 11.150/2022 (minimo existencial) |

## 3. CLASSIFICACAO DA JURISPRUDENCIA (3 niveis)

1. **VALIDADA** — sumula/Tema/precedente conferido e vigente → pode citar.
2. **`[VERIFICAR]`** — provavel mas nao confirmado nesta sessao → marcar e acionar `jurisprudencia-consumidor` para busca viva; nunca citar como certo (PA-01).
3. **IMPOSSIBILIDADE** — nao ha base segura → nao inventar; reformular a tese.

Hierarquia: STF (repercussao geral) > STJ (repetitivo/sumula) > STJ turmas > TJ local > demais TJs.

## 4. O SELO

Emita e grave no `CASO.md`:

```
SELO DE VALIDACAO LEGAL PREVIA — P1
- Status: EMITIDO
- Fato gerador: [data]
- Eixo: [...]
- Normas-base vigentes: [CDC arts. ...; lei especial ...]
- Sumulas/Temas validados: [...]
- Pendencias [VERIFICAR]: [... -> jurisprudencia-consumidor]
- Data: [hoje]
```

Status **PENDENTE** bloqueia a producao. Apenas o Selo **EMITIDO** (ainda que com pendencias `[VERIFICAR]` sinalizadas) libera o Tier 2.

## 5. ENCERRAMENTO

Entrega o Selo e a lista de normas/sumulas para as skills de producao usarem. Sem Selo, o `consumidor-master` nao avanca (Camada 2, Protocolo P1).
