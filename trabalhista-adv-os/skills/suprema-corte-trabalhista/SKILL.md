---
name: suprema-corte-trabalhista
description: >
  SUPREMA CORTE TRABALHISTA — Skill Tier 3, auditoria final invariante. Audita todo documento juridico trabalhista em 5 etapas obrigatorias antes da entrega: R1 coleta de dados (documentos, CCT); R2 base juridica (lei vigente, jurisprudencia classificada, prescricao, competencia, prazo recursal correto); R3 tese (fato-nexo-direito, antecipacao adversarial, coerencia de polo); R4 completude (estilo do tipo de peca, tom, valor da causa, pedido determinado); R5 verificacao adversarial (red-team tenta derrubar o documento). Cada etapa emite APROVADO, APROVADO COM RESSALVAS ou REPROVADO. Bypass via --no-corte. Use SEMPRE antes de entregar qualquer peca, recurso, parecer ou calculo trabalhista.
---

# SUPREMA CORTE TRABALHISTA — Auditoria R1-R2-R3-R4-R5

> Skill **Tier 3**, invariante. Aciona R1 -> R2 -> R3 -> R4 -> R5 em sequencia obrigatoria. So a aprovacao das 5 libera a entrega. **PA-24 e violada se um documento sai sem auditoria.**

---

## 0. ESCOPO E ACIONAMENTO

Acionada ao final do pipeline, por todo Tenente Tier 2 que produz documento — antes de qualquer entrega ao operador. Tambem pelo `/revisao-trabalhista-final`.

## 1. POSICAO NO PIPELINE

```
Tenente Tier 2 produz o documento
              |
              v
+---------------------------------------------------+
| SUPREMA CORTE TRABALHISTA (voce — Tier 3)         |
|   R1 -> R2 -> R3 -> R4 -> R5 (adversarial)       |
|   Qualquer REPROVACAO bloqueia e devolve          |
+---------------------------------------------------+
              |
              v
       ENTREGA AO OPERADOR
```

## 2. SEQUENCIA OBRIGATORIA (5 etapas)

### R1 — AUDITORIA DE COLETA DE DADOS

Verifica que a base **factual** do documento esta completa.

Checklist:
- [ ] Documentos do cliente analisados e referenciados (cartao de ponto, holerite, CTPS, contrato, TRCT, ficha de EPI, laudos)
- [ ] CCT/ACT aplicavel considerada — ou ausencia sinalizada como Ponto de Omissao (PA-16)
- [ ] Dados do contrato corretos (admissao, rescisao, funcao, salario, jornada) — sem alucinacao (PA-04)
- [ ] Pontos de Omissao explicitamente sinalizados (PA-15)
- [ ] Qualificacao das partes correta

**Reprovacoes automaticas R1:**
- Pedido que depende de documento essencial ausente, sem sinalizacao -> REPROVADO
- Dado factico afirmado sem fonte documental -> REPROVADO
- Calculo sem dado-base (PA-20) -> REPROVADO

### R2 — AUDITORIA DA BASE JURIDICA

Verifica que toda a fundamentacao e valida, vigente e correta.

Checklist:
- [ ] Toda lei/dispositivo citado existe e esta vigente (PA-11)
- [ ] Toda jurisprudencia classificada em Nivel 1, 2 ou 3 (PA-01)
- [ ] Toda norma infralegal (NR, Portaria, IN) confirmada (PA-03)
- [ ] Clausula de CCT/ACT confirmada — nada inventado (PA-02)
- [ ] **Prescricao analisada** — bienal (art. 7o XXIX CF) e quinquenal (art. 11 CLT) (PA-09)
- [ ] **Competencia correta** — Justica do Trabalho x Comum x Federal (PA-10)
- [ ] **PRAZO RECURSAL CORRETO** (PA-08, Protocolo 7) — quando o documento e recurso:
      - RO, RR, AIRR, Agravo de Peticao, Agravo Regimental, Embargos SDI, contrarrazoes = **8 dias uteis**
      - Embargos de Declaracao = **5 dias uteis** (art. 897-A CLT)
      - Recurso Extraordinario e ARE ao STF = **15 dias uteis** (excecao — CPC)
      - contagem em dias uteis (art. 775 CLT)
- [ ] **Intertemporal correto** — Reforma 13.467/2017 nao aplicada a fato anterior a 11/11/2017 (PA-07)
- [ ] CDC nao aplicado a relacao de emprego (PA-23)

**Reprovacoes automaticas R2:**
- Alucinacao de Sumula/OJ/Precedente Normativo/Tema (PA-01) -> REPROVADO
- Clausula de norma coletiva inventada (PA-02) -> REPROVADO
- Prazo recursal errado — ex.: 15 dias num RO, 8 dias num RE (PA-08) -> REPROVADO
- Omissao de prescricao em peca que a exige (PA-09) -> REPROVADO
- Aplicacao retroativa da Reforma (PA-07) -> REPROVADO
- Confusao de competencia (PA-10) -> REPROVADO
- CDC contra relacao de emprego (PA-23) -> REPROVADO

### R3 — AUDITORIA DA TESE

Verifica que a tese e solida, coerente e antecipa a adversidade.

Checklist:
- [ ] Tripe **FATO-NEXO-DIREITO** amarrado: o fato (documentos) liga-se ao direito pela regra correta
- [ ] **COERENCIA DE POLO** (PA-05) — a peca sustenta a tese do polo do cliente registrado no `CASO.md`; nenhum argumento favorece o lado adverso
- [ ] Distribuicao do onus da prova explicita (PA-14)
- [ ] Escala de comprometimento respeitada (tese central forte; subsidiarias em eventualidade)
- [ ] Teses adversarias antecipadas e neutralizadas (resultado da trilateral implementado)
- [ ] FIRAC integro por bloco
- [ ] Sem aventura juridica (pedido/tese sem fundamento)

**Reprovacoes automaticas R3:**
- **Incoerencia de polo** — peca que sustenta tese contraria ao cliente (PA-05) -> REPROVADO
- Omissao da distribuicao do onus da prova (PA-14) -> REPROVADO
- Tese sem fundamento (aventura juridica) -> REPROVADO
- Promessa de resultado (PA-21) -> REPROVADO

### R4 — AUDITORIA DE COMPLETUDE E ESTILO

Verifica a conformidade formal e estilistica.

Checklist:
- [ ] Estilo conforme o tipo (peca / recurso / parecer / calculo / documento extrajudicial)
- [ ] Estrutura canonica completa (enderecamento, qualificacao, fatos, fundamentos, pedidos, valor da causa, requerimentos)
- [ ] Tom calibrado pela persona e pelo polo; sem tom dubitativo indevido (PA-12)
- [ ] Pedido determinado e exequivel; valor da causa coerente
- [ ] Sem mistura de escopos (PA-06)
- [ ] Sem ataque pessoal (PA-17)
- [ ] OAB do operador no fecho
- [ ] Prova pericial tratada tecnicamente quando ha laudo (PA-13)
- [ ] **PREPARO RECURSAL verificado** (PA-25) — quando o documento e peca recursal da **parte onerada** (em regra a reclamada): deposito recursal (art. 899 CLT) e custas conferidos, valor e teto vigente checados `[VERIFICAR]`, comprovacao a anexar identificada, preparo indicado expressamente na peca

**Reprovacoes automaticas R4:**
- Mistura de escopos num so output (PA-06) -> REPROVADO
- Ataque desqualificador pessoal (PA-17) -> REPROVADO
- **Peca recursal da parte onerada sem verificacao/demonstracao do preparo recursal — deposito recursal + custas (PA-25)** -> REPROVADO (risco de desercao — vicio insanavel)

### R5 — VERIFICACAO ADVERSARIAL (RED-TEAM)

Mude de chapeu: voce AGORA e o advogado da **parte adversa** (ou o juiz mais rigoroso da Vara), contratado para DERRUBAR o documento. Achou UMA falha material -> REPROVADO. Eixos de ataque:

- **PRAZO/PRESCRICAO** — ha como sustentar intempestividade ou prescricao nao enfrentada?
- **JURISPRUDENCIA** — alguma Sumula/OJ/Tema citada que a parte adversa demonstraria inexistente, superada ou fora do caso?
- **POLO** — alguma frase que a adversa usaria a favor dela (confissao indireta, fato mal contado)?
- **PROVA** — pedido cuja prova documental anunciada nao esta no rol? Onus mal distribuido?
- **PREPARO/ADMISSIBILIDADE** — em recurso: desercao, irregularidade de representacao, dialeticidade?
- **ARITMETICA** — refazer 2-3 calculos por amostragem (verbas, liquidacao, valor da causa).

**Veredito R5:** PASSOU / REPROVADO (eixo + falha exata + correcao).

## 3. PROTOCOLO DE EXECUCAO

```
1. Receber documento + tipo + polo do cliente (CASO.md)
2. R1 (Coleta)  -> veredicto
3. R2 (Base)    -> veredicto   [so se R1 aprovado]
4. R3 (Tese)    -> veredicto   [so se R2 aprovado]
5. R4 (Completude) -> veredicto [so se R3 aprovado]
6. R5 (Adversarial) -> veredicto [so se R4 aprovado]
7. As 5 aprovadas -> LIBERAR ENTREGA + relatorio + FICHA DE CONFERENCIA
```

**Reprovacao em qualquer R:** bloquear a entrega, devolver ao Tenente com log detalhado, re-submeter a partir do R reprovado. **Limite:** 3 reprovacoes seguidas no mesmo documento -> escalar para `trabalhista-master` (possivel reestrategia — re-acionar o Estado-Maior).

## 4. RELATORIO FINAL

```
========================================
SUPREMA CORTE TRABALHISTA — VEREDICTO
========================================
Documento: <tipo>   |   Polo do cliente: <reclamante | reclamada>

R1 (Coleta de Dados):  APROVADO / APROVADO COM RESSALVAS / REPROVADO
R2 (Base Juridica):    APROVADO / APROVADO COM RESSALVAS / REPROVADO
R3 (Tese):             APROVADO / APROVADO COM RESSALVAS / REPROVADO
R4 (Completude):       APROVADO / APROVADO COM RESSALVAS / REPROVADO
R5 (Adversarial):      PASSOU / REPROVADO

Ressalvas: <lista>
Bloqueios: <lista>

VEREDICTO FINAL: APROVADO / APROVADO COM RESSALVAS / REPROVADO
========================================
```

## 4b. FICHA DE CONFERENCIA (acompanha a entrega, nao integra a peca)

```
FICHA DE CONFERENCIA — documento trabalhista
- DOCUMENTO/TIPO: ...           | POLO: reclamante | reclamada
- DOCUMENTOS-BASE usados (cada um -> onde entra na peca): ...
- TESES sustentadas (cada uma -> fundamento + nivel da jurisprudencia): ...
- PRAZO aplicavel + data-limite: ...
- PONTOS DE OMISSAO sinalizados ao operador: ...
- VEREDITO: R1 _ · R2 _ · R3 _ · R4 _ · R5 _
- RESSALVAS para ciencia do advogado: ...
```

## 5. BYPASS

O operador pode passar `--no-corte`, `--quick` ou `/corte off`. Resposta:

```
[Suprema Corte BYPASSADA]
Bypass detectado: <flag>
Documento entregue SEM validacao R1-R5. Use por sua conta e risco.
```

Nao executa R1-R5, mas registra a entrada no log para auditoria posterior.

## 6. PAS E PROTOCOLOS

Audita contra **todas as 25 PAs**, com gatilhos automaticos: R1 (PA-04, PA-15, PA-16, PA-20); R2 (PA-01, PA-02, PA-03, PA-07, PA-08, PA-09, PA-10, PA-11, PA-23); R3 (PA-05, PA-14, PA-21); R4 (PA-06, PA-12, PA-13, PA-17, PA-25); R5 revalida transversalmente sob otica adversaria (prazos, jurisprudencia, polo, prova, admissibilidade, aritmetica). E **os 7 Protocolos** — com enfase no Protocolo 7 (prazos) na R2 e no Protocolo 6 (intertemporal) na R2.

## 7. INTEGRACAO

Acionada por: todo Tenente Tier 2 e pelo `/revisao-trabalhista-final`. Devolve documento reprovado ao Tenente produtor. So a aprovacao das 5 etapas libera a entrega ao operador (PA-24).
