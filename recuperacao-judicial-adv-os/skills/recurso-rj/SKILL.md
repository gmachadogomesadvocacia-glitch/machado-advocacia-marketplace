---
name: recurso-rj
description: >
  RECURSO-RJ — Tier 2 (Produção). Redige recursos em processos de recuperação judicial e falência: agravo de instrumento (principal recurso em RJ — art. Acionar quando o usuário precisar recorrer de decisão em processo de RJ, falência ou RE, independentemente do polo (devedor ou credor). Verificar prazos com urgência — decisões em RJ têm prazos curtos.
---

# RECURSO-RJ
> Tier 2 | Recursos em Insolvência | Agravo + Apelação + REsp + MS | Art. 17 LFRJ + CPC

---

## 0. ESCOPO

Redige recursos em processos de insolvência. Verifica cabimento, prazo e adequação do recurso
antes de redigir. Emite alerta se prazo estiver crítico.

⚠️ **PA-01**: Verificar jurisprudência antes de citar no recurso.
⚠️ **PA-06**: Prazos em RJ são curtos — verificar IMEDIATAMENTE.

---

## 1. MAPA DE RECURSOS EM INSOLVÊNCIA

| Decisão recorrida | Recurso cabível | Prazo | Efeito suspensivo |
|-------------------|-----------------|-------|-------------------|
| Interlocutória no juízo da RJ | Agravo de instrumento (art. 17 LFRJ) | 15 dias | Regra: não tem (CPC 995) |
| Sentença na RJ (rara — ex: convolação) | Apelação | 15 dias | CPC 1.009 |
| Decisão do relator no TJ | Agravo interno | 15 dias | CPC 1.021 |
| Acórdão do TJ | REsp (STJ) / RE (STF) | 15 dias | CPC 1.029 |
| Ato judicial abusivo / MS | Mandado de segurança | 120 dias | Liminar |
| Decisão sobre habilitação | Agravo interno (art. 17 LFRJ) | 15 dias | Não tem |
| Homologação do plano negada | Apelação | 15 dias | CPC 1.009 |

⚠️ O **Agravo de Instrumento** é o recurso-padrão em RJ (art. 17 LFRJ proclama especificamente).

---

## 2. AGRAVO DE INSTRUMENTO — ART. 17 LFRJ

### 2.1 Decisões mais recorridas via AI em RJ

- Indeferimento do processamento da RJ
- Deferimento do processamento (pelo credor contrário)
- Decisão sobre habilitação/classificação de crédito
- Decisão sobre stay (extensão ou negativa)
- Decisão sobre afastamento dos administradores
- Negativa de DIP financing
- Aprovação do plano (pelo credor contrário)
- Negativa de cram down pelo juiz

### 2.2 Template — Agravo de Instrumento

```
AGRAVO DE INSTRUMENTO
Processo de origem nº [...] | Vara: [...] | Tribunal: [TJ... / TRF...]

AGRAVANTE: [qualificação]
AGRAVADO: [qualificação]

I — CABIMENTO E TEMPESTIVIDADE
Trata-se de agravo de instrumento interposto com fundamento no art. 17 da
L11.101/2005 e no art. 1.015 do CPC, contra decisão interlocutória proferida
em [data], na qual Vossa Excelência [decisão resumida].

A decisão foi disponibilizada em [data], dentro do prazo legal de 15 dias.

II — DO EFEITO SUSPENSIVO (se aplicável)
"Demonstrada a probabilidade do provimento do recurso e o risco de dano grave
(CPC 1.019, I), requer-se a concessão de EFEITO SUSPENSIVO, pois [razão: leilão
iminente / convolação pendente / outro dano irreversível]."

III — DOS FATOS
[Contextualização da RJ + decisão agravada + impacto]

IV — DO DIREITO

4.1 [Tese principal — ex: violação do art. 6º / art. 58 / art. 48]

"A decisão agravada viola frontalmente o art. [X] da L11.101/2005, que estabelece [...]."

4.2 [Jurisprudência — validada por jurisprudencia-rj]

"Nesse sentido, o Superior Tribunal de Justiça já decidiu que [...]
(REsp nº [...], [Turma], Rel. Min. [...], j. [...])."

4.3 [Doutrina — se relevante]

V — DO PEDIDO
a) Seja recebido e processado o presente agravo;
b) Seja concedido efeito suspensivo [se aplicável];
c) Seja notificado o agravado para resposta;
d) Seja provido o recurso para reformar a decisão agravada, determinando [...].
```

---

## 3. RECURSO ESPECIAL AO STJ

### 3.1 Cabimento em RJ

- Violação de lei federal (LFRJ, CPC, CC) — art. 105, III-a CF
- Divergência jurisprudencial entre TJs — art. 105, III-c CF
- Temas repetitivos do STJ em matéria falimentar

### 3.2 Requisitos de admissibilidade

```
□ Prequestionamento: matéria federal deve ter sido discutida no acórdão recorrido
□ Artigos da lei federal violados devem estar expressamente indicados
□ Divergência: acórdãos paradigma devem ser citados com ementas completas
□ Sem reexame de fatos: Súm. 7 STJ é o maior obstáculo em RJ
□ Questão federal não é constitucional (STF): verificar competência
```

### 3.3 Estratégia anti-Súm. 7 STJ

"A pretensão recursal não demanda reexame de fatos e provas, mas apenas
a correta aplicação do art. [X] da LFRJ aos fatos incontroversos reconhecidos
no acórdão recorrido, quais sejam: [fatos já fixados pelo TJ]."

---

## 4. MANDADO DE SEGURANÇA EM MATÉRIA FALIMENTAR

Cabível quando:
- Não há recurso próprio adequado
- Há ato judicial abusivo com ofensa a direito líquido e certo
- Decisão viola frontalmente a LFRJ de forma clara (direito líquido e certo)

Situações típicas em RJ:
- Inclusão/exclusão arbitrária de crédito no QGC sem contraditório
- Deliberação assemblear presidida irregularmente
- Intimação insuficiente para AGC (< 15 dias)

Prazo: 120 dias da ciência do ato (Lei 12.016/2009, art. 23).

---

## 5. ANÁLISE DE EFEITO SUSPENSIVO

Em RJ, o efeito suspensivo é a exceção, não a regra. Para obtê-lo:

```
□ Demonstrar fumus boni iuris: probabilidade de provimento do recurso
□ Demonstrar periculum in mora: dano de difícil reparação se a decisão produzir efeitos
□ Identificar a norma processual: CPC 1.019, I (AI) ou CPC 1.012, §4º (apelação)
□ Protocolar conjuntamente com o recurso ou antes, como medida cautelar
```

Situações que justificam ES em RJ:
- Leilão de bem essencial à atividade
- Convolação em falência (dano imediato aos empregos e credores)
- Aprovação de plano com vício formal grave

---

## 6. VEDAÇÕES

- **PA-01**: Nunca citar jurisprudência sem validar (usar jurisprudencia-rj)
- **PA-06**: Verificar prazo IMEDIATAMENTE — recursos intempestivos não são conhecidos
- **PA-24**: Revisao-final-rj antes de protocolar
