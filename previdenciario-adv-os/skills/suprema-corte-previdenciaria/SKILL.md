---
name: suprema-corte-previdenciaria
description: >
  SUPREMA CORTE PREVIDENCIARIA — Skill Tier 3 (Quality Gate). Acionar automaticamente ao final de cada resposta substantiva previdenciaria.
---

# SUPREMA CORTE PREVIDENCIARIA
> Tier 3 — Quality Gate | R1 PAs | R2 Fundamentacao | R3 Auto-critica | R4 Semaforo

---

## ATIVACAO

Este gate roda AUTOMATICAMENTE ao final de toda resposta substantiva previdenciaria,
a menos que o usuario tenha incluido `--no-corte` no pedido (rascunho = permitido).

Nao e necessario o usuario pedir — e automatico como uma revisao interna.

---

## R1 — VERIFICACAO DAS 22 PROIBICOES ABSOLUTAS

```
Percorrer mentalmente as 22 PAs do previdenciario-master:

PA-01: Citei jurisprudencia sem numero + data + tribunal? → BLOQUEADO
PA-02: Afirmei que uma lei "nao existe" sem verificar? → BLOQUEADO
PA-03: Revisao de RMI sem verificar decadencia (10 anos)? → BLOQUEADO
PA-04: Apliquei EC 103 retroativamente a DER anterior a 13/11/2019? → BLOQUEADO
PA-05: Aceitei EPI eficaz como afastamento de especial por ruido? → BLOQUEADO
PA-06: Afirmei que desaposentacao e possivel (Tema 709 STF)? → BLOQUEADO
PA-07: Ignorei DIB posterior a DER (retroativos perdidos)? → BLOQUEADO
PA-08: Misturei regras RGPS e RPPS sem distinção? → BLOQUEADO
PA-09: Confundi carencia com tempo de contribuicao? → BLOQUEADO
PA-10: Orientei segurado a nao requerer DER urgente? → BLOQUEADO
PA-11: Afirmei que MEI tem RMI igual ao CLT? → BLOQUEADO
PA-12: Calculei RMI sem apresentar calculo comparativo (auto-ataque)? → BLOQUEADO
PA-13: Afirmei tese juridica sem base legal ou contraria a sumula TNU? → BLOQUEADO
PA-14: Ignorei alegacao de doenca preexistente sem preparar rebuttal? → BLOQUEADO
PA-15: Indiquei acao judicial sem verificar se via administrativa e mais rapida? → BLOQUEADO
PA-16: Confundi competencia JEF com JT (acidentario)? → BLOQUEADO
PA-17: Nao alertei sobre prazo decadencial de 30 dias para recurso JR? → BLOQUEADO
PA-18: Afirmei que BPC e acumulavel com salario sem verificar? → BLOQUEADO
PA-19: Orientei calculo sem identificar o regime do segurado (RGPS/RPPS/Complementar)? → BLOQUEADO
PA-20: Produzi peca processual sem identificar competencia territorial? → BLOQUEADO
PA-21: Inclui dados sensiveis (CPF/NIT/CID) em resposta que pode ser compartilhada? → BLOQUEADO
PA-22: Recomendei Revisao da Vida Toda sem analise individual obrigatoria? → BLOQUEADO

RESULTADO R1:
□ Todas as PAs verificadas: prosseguir para R2
□ Alguma PA violada: PARAR — reformular antes de entregar
```

---

## R2 — VERIFICACAO DE FUNDAMENTACAO LEGAL

```
Para cada afirmacao juridica da resposta, verificar:

□ Ha norma legal citada? (art. X, Lei 8.213/91 / art. Y, EC 103/2019 / etc.)
□ Ha precedente jurisprudencial se necessario? (Sumula TNU + numero / Tema STF + numero)
□ A norma citada esta vigente? (verificar se foi revogada por EC 103/2019 ou outra)
□ O periodo de vigencia esta correto? (ex: teto de ruido variou por periodo)

Se algum ponto carecede fundamento: incluir ou sinalizar que nao foi possivel verificar.
Nao afirmar fatos juridicos sem base (PA-02 + PA-13).

RESULTADO R2:
□ Fundamentacao suficiente: prosseguir para R3
□ Lacuna de fundamentacao: completar antes de entregar
```

---

## R3 — AUTO-CRITICA (ARGUMENTO MAIS FORTE CONTRA A TESE)

```
Formular internamente o melhor argumento que o INSS / juiz poderia usar contra a tese:

Exemplo:
  Tese do advogado: "O periodo rural deve ser reconhecido com base em TNU Sumula 6."
  Auto-critica R3: "O INSS pode arguir que o inicio de prova material e muito fraco
  (apenas uma certidao de nascimento do filho) e que os depoimentos sao de familiares
  — jurisprudencia exige provas nao exclusivamente familiares."

Se o auto-critica identificar um ponto real: incluir na resposta como "Risco identificado"
e sugerir como reforcar a prova ou preparar resposta.

Se o auto-critica for superado pela tese: registrar "Tese robusta — auto-critica superada."

RESULTADO R3:
□ Tese robusta: prosseguir para R4
□ Risco identificado: incluir na resposta antes de entregar
```

---

## R4 — SEMAFORO FINAL

```
🟢 SINAL VERDE — apto para entrega:
   Todas as PAs verificadas sem violacao
   Fundamentacao legal presente
   Auto-critica R3 superada ou riscos sinalizados

🟡 SINAL AMARELO — entregar com ressalva:
   Algum dado incerto (ex: data de jurisprudencia nao verificada)
   Calculos dependem de documentos que o usuario nao forneceu
   → Incluir nota: "Esta analise baseia-se nos dados fornecidos.
     Verificar [X] antes de protocolar."

🔴 SINAL VERMELHO — nao entregar — reformular:
   Violacao de PA identificada em R1
   Afirmacao juridica sem base (PA-02/PA-13)
   Calculo sem comparativo (PA-12)
   → Reformular a resposta antes de entregar ao usuario

FORMATO DA NOTA SUPREMA CORTE (incluir ao final das respostas quando relevante):
---
[🟢 SUPREMA CORTE — R1✓ R2✓ R3✓ R4✓ R5✓ — Apto para entrega + FICHA]
OU
[🟡 SUPREMA CORTE — Ressalva: [descrever] — verificar antes de protocolar + FICHA]
OU
[🔴 SUPREMA CORTE — BLOQUEADO: [R1 PA / R5 eixo+falha] — reformulando]
---
Apos R4, executar R5 (red-team) e anexar a FICHA DE CONFERENCIA a entrega.
```

---

## R5 — VERIFICACAO ADVERSARIAL (RED-TEAM)

```
Mude de chapeu: voce AGORA e o INSS/procuradoria / o juizo cetico.
Unica missao: DERROTAR a peca. Achou UMA falha → REPROVADO.

Eixos (PREVIDENCIARIO):
- VALORES/RMI — a RMI, a renda e os atrasados vem do calculo (data-fim correta)?
  regra de transicao certa (EC 103)?
- REQUISITOS DO BENEFICIO — carencia, qualidade de segurado, tempo/idade/incapacidade
  comprovados?
- INSTRUMENTO/VIA — previo requerimento administrativo (Tema 350 STF)?
  acao x recurso CRPS x MS?
- COMPETENCIA — JEF ate 60 SM; foro do domicilio; Justica Federal
  (ou Estadual delegada)?
- CITACOES — sumulas/temas batem em NUMERO e TRIBUNAL? (atencao: Revisao da Vida Toda
  = Tema 1102 STF / Tema 999 STJ; nao trocar; sumulas TNU com tese correta.)
- PRESCRICAO — parcelas quinquenais (Sum. 85 STJ)?

VEREDITO R5: PASSOU / REPROVADO (eixo + falha + correcao).
```

---

## FICHA DE CONFERENCIA (acompanha a entrega, nao integra a peca)

```
FICHA DE CONFERENCIA — pre-protocolo
- PREMISSAS: ...
- VALORES/RMI (origem calculo, data-fim): ...
- CITACOES (cada uma → status): ... — CONFIRMADO | VALIDAR
- LACUNAS [INFORMAR]: ...
- RISCOS / PONTOS ADVERSARIAIS: ...
- VEREDITO: R1 _ · R2 _ · R3 _ · R4 _ · R5 _
- PENDE O OK INFORMADO DO ADVOGADO antes do protocolo.
```

---

## BYPASSAR COM --no-corte

```
Se o usuario incluir --no-corte no pedido:
  O gate R1-R4 nao e executado formalmente
  A resposta e marcada como: "[RASCUNHO — Suprema Corte desativada]"
  Nao incluir a nota de semaforo

Quando usar --no-corte:
  Rascunhos iniciais que serao revisados pelo advogado
  Brainstorming de argumentos (exploracao, nao entrega final)
  Pedidos de estrutura sem verificacao de conteudo
```

---

## ALERTAS

```
⚠️ O gate e automatico — nao esperar o usuario pedir
⚠️ Sinal vermelho nao bloqueia a resposta para o usuario: bloqueia internamente e reformula
⚠️ --no-corte e para rascunhos: nunca bypassar em peticoes iniciais ou recursos
⚠️ R3 (auto-critica) e a parte mais valiosa: identificar o ponto fraco antes do INSS
```
