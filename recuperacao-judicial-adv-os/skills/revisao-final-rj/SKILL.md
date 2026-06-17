---
name: revisao-final-rj
description: >
  REVISAO-FINAL-RJ — Tier 3 (Auditoria Pré-entrega). Executa a auditoria obrigatória R1-R4
  em todas as peças produzidas pelo pipeline de recuperação judicial antes do protocolo.
  Verifica: base normativa (L11.101/2005 + L14.112/2020), coerência de polo, validade de
  jurisprudência, prazos, consistência com o CASO.md, e qualidade da redação jurídica.
  Esta skill é OBRIGATÓRIA antes de qualquer protocolo — é o Protocolo P6 do sistema.
  Acionar sempre que uma peça de RJ estiver pronta para entrega ou protocolo.
---

# REVISAO-FINAL-RJ
> Tier 3 | Auditoria Pré-entrega R1-R4 | Protocolo P6 | Obrigatória para toda peça

---

## 0. ESCOPO

Auditoria de quatro etapas (R1-R4) aplicada a toda peça produzida no pipeline de RJ.
Emite veredito: **APROVADO** / **APROVADO COM RESSALVAS** / **REPROVADO**.

⚠️ **PA-24**: Nenhuma peça é entregue ao cliente ou protocolada sem aprovação R1-R4.

---

## 1. AUDITORIA R1 — COLETA E DOCUMENTAÇÃO

Verificar se os insumos do caso estão completos e atualizados:

```
R1.1 CASO.md disponível e atualizado?
  □ Polo do cliente identificado
  □ Fase processual atual correta
  □ Processo nº e vara corretos (se aplicável)
  □ Administrador Judicial identificado (se nomeado)

R1.2 Documentos de suporte analisados?
  □ Auditoria documental (RAD) concluída
  □ Laudo de viabilidade aprovado (para plano)
  □ QGC/relação de credores disponível (para peças que requerem)

R1.3 Lacunas identificadas e sinalizadas?
  □ Itens com [VERIFICAR] foram confirmados ou mantidos como alerta?
  □ Dados ausentes indicados explicitamente na peça?

RESULTADO R1: □ APROVADO  □ APROVADO COM RESSALVAS  □ REPROVADO
```

---

## 2. AUDITORIA R2 — BASE JURÍDICA E NORMATIVA

Verificar a correção da base legal e jurisprudencial:

```
R2.1 Artigos da LFRJ citados estão na versão vigente?
  □ Verificar se os artigos refletem a L14.112/2020 (reforma de dez/2020)
  □ Artigos alterados pela reforma: 6º, 33, 39, 41, 45, 47, 48, 50, 54, 56, 58,
    67, 69-G a 69-L, 84, 94, 95, 98, 100, 104, 129, 130, 133, 161-167
  □ Verificar se a referência é à versão original ou à emenda

R2.2 Jurisprudência do STJ:
  □ Nenhum julgado inventado ou não localizado (PA-01)
  □ Súmulas corretamente enunciadas
  □ Temas repetitivos aplicáveis foram verificados
  □ Itens com [VERIFICAR] não foram incluídos como tese definitiva

R2.3 Prazos processuais corretos?
  □ Agravo de instrumento: 15 dias (art. 17 LFRJ)
  □ Habilitação de crédito: 15 dias (impróprio — [VERIFICAR])
  □ Apresentação do plano: 60 dias + possível prorrogação (PA-06)
  □ Stay: 180 dias prorrogáveis (PA-09)
  □ Impugnação ao plano: 30 dias (art. 55)
  □ Contestação ao pedido de falência: 10 dias (art. 98)
  □ Mandado de segurança: 120 dias

R2.4 Competência correta?
  □ Vara empresarial / falimentar identificada
  □ Súm. 480 STJ verificada para competência territorial
  □ Conflito de competência entre juízos verificado (grupos econômicos)

RESULTADO R2: □ APROVADO  □ APROVADO COM RESSALVAS  □ REPROVADO
```

---

## 3. AUDITORIA R3 — COERÊNCIA ESTRATÉGICA E DE POLO

Verificar consistência interna da peça com o caso concreto:

```
R3.1 Coerência de polo (PA-02):
  □ A peça está redigida pelo polo correto (devedor / credor / AJ)?
  □ As teses não conflitam com a posição processual do cliente?
  □ Os pedidos são favoráveis ao cliente, não ao adversário?

R3.2 Coerência com o CASO.md:
  □ Nome e qualificação do devedor corretos?
  □ Número do processo correto?
  □ Classe de crédito do cliente correta?
  □ Valor do crédito consistente com o mapeado no CASO.md?

R3.3 Estrutura FIRAC verificada:
  □ F (Fato): situação descrita com precisão e completude?
  □ I (Issue): problema jurídico claramente identificado?
  □ R (Regra): base legal e jurisprudencial correta e vigente?
  □ A (Aplicação): tese aplicada especificamente ao caso?
  □ C (Conclusão): pedido preciso, viável e coerente com a tese?

R3.4 Ausência de contradições internas:
  □ Afirmações do exórdio não contradizem o mérito?
  □ Pedidos são compatíveis entre si?
  □ Valores citados são consistentes ao longo da peça?

R3.5 Classes de credores (PA-07):
  □ Classificação do crédito está correta?
  □ O limite de 150 SM para trabalhistas foi respeitado (PA-08)?
  □ Créditos extraconcursais estão segregados (PA-15)?

RESULTADO R3: □ APROVADO  □ APROVADO COM RESSALVAS  □ REPROVADO
```

---

## 4. AUDITORIA R4 — QUALIDADE TÉCNICA E COMPLETUDE

Verificar a excelência da redação jurídica e a completude da peça:

```
R4.1 Endereçamento e qualificação:
  □ Cabeçalho correto (Tribunal / Vara / Processo)?
  □ Qualificação das partes completa (CNPJ, endereço, advogado, OAB)?
  □ Identificação do Administrador Judicial (quando necessário)?

R4.2 Estrutura da peça:
  □ Divisão em capítulos/seções adequada ao tipo de peça?
  □ Numeração de itens consistente?
  □ Pedidos organizados em alíneas (a, b, c)?
  □ Valor da causa indicado (quando obrigatório)?

R4.3 Padrão de redação (estilo-juridico-rj):
  □ Linguagem técnica adequada sem rebuscamento desnecessário?
  □ Ausência de jargões informais?
  □ Parágrafos com tamanho adequado?
  □ Negritos e destaques usados com parcimônia?

R4.4 Completude processual:
  □ Documentos a anexar indicados (lista de documentos)?
  □ Procuração mencionada (ad judicia)?
  □ Pedido de intimação via portal eletrônico?
  □ Local, data e assinatura?

R4.5 Revisão final:
  □ Ortografia e gramática corretas?
  □ Nenhum trecho de template não preenchido ("[...]", "[NOME]")?
  □ Datas e valores grafados corretamente por extenso quando necessário?

RESULTADO R4: □ APROVADO  □ APROVADO COM RESSALVAS  □ REPROVADO
```

---

## R5 — VERIFICACAO ADVERSARIAL (RED-TEAM)

Mude de chapeu: voce AGORA e a recuperanda/AJ / o juizo cetico. Unica missao:
DERROTAR a peca. Achou UMA falha → REPROVADO.

Eixos (RECUPERACAO JUDICIAL):
- **VALORES/CLASSE** — o credito vem do calculo (atualizado ate a DATA DO PEDIDO,
  nao a atual)? Classe I respeitando o teto de 150 SM (excedente p/ Classe III)?
- **FATO GERADOR** — concursal x extraconcursal cravado pela data (Tema 1051 STJ)?
- **INSTRUMENTO/VIA** — via certa (divergencia art. 7 §1 x impugnacao art. 8 x
  retardataria art. 10 x reserva art. 6 §2)?
- **CITACOES** — sumulas/temas batem em tese? (Tema 987 STJ esta CANCELADO; nao
  usar como vigente.)
- **PRESCRICAO** — habilitacao admitida ate o encerramento (REsp 1.851.692); nao
  confundir bienal trabalhista (CF) com a habilitacao (CC).
- **POLO** — coerente (credor x devedor x AJ); FGTS/INSS na classe certa.

**Veredito R5:** PASSOU / REPROVADO (eixo+falha+correcao).

---

## FICHA DE CONFERENCIA (acompanha a entrega, nao integra a peca)

```
FICHA DE CONFERENCIA — pre-protocolo
- PREMISSAS: ...
- VALORES/CLASSE (origem calculo, data do pedido): ...
- CITACOES (cada uma → status): Tema 1051 STJ — CONFIRMADO | VALIDAR
- LACUNAS [INFORMAR]: ...
- RISCOS / PONTOS ADVERSARIAIS: ...
- VEREDITO: R1 _ · R2 _ · R3 _ · R4 _ · R5 _
- PENDE O OK INFORMADO DO ADVOGADO antes do protocolo.
```

---

## 6. VEREDITO FINAL

```
╔══════════════════════════════════════════════════════╗
║  VEREDITO DE REVISÃO FINAL — [NOME DA PEÇA]         ║
╠══════════════════════════════════════════════════════╣
║  R1 (Documentação):     [ APROVADO / RESSALVAS / REPROVADO ] ║
║  R2 (Base jurídica):    [ APROVADO / RESSALVAS / REPROVADO ] ║
║  R3 (Coerência):        [ APROVADO / RESSALVAS / REPROVADO ] ║
║  R4 (Qualidade):        [ APROVADO / RESSALVAS / REPROVADO ] ║
║  R5 (Adversarial):      [ PASSOU / REPROVADO ]              ║
╠══════════════════════════════════════════════════════╣
║  VEREDITO GLOBAL:                                    ║
║  [ ] ✅ APROVADO — peça pronta para protocolo        ║
║  [ ] ⚠️  APROVADO COM RESSALVAS — protocolar com     ║
║          atenção a: [lista de ressalvas]              ║
║  [ ] ❌ REPROVADO — corrigir antes de protocolar:    ║
║          [lista de falhas críticas]                   ║
╚══════════════════════════════════════════════════════╝
```

Anexar sempre a FICHA DE CONFERENCIA junto da entrega (R1-R5 + FICHA).

**APROVADO**: Peça pode ser protocolada / entregue ao cliente.

**APROVADO COM RESSALVAS**: Protocolar com ciência do advogado sobre os pontos pendentes.
Ressalvas típicas: itens com [VERIFICAR] não confirmados, valor da causa a confirmar, etc.

**REPROVADO**: NUNCA protocolar. Retornar à skill que gerou a peça com a lista de falhas.
Falhas típicas: polo errado, prazo perdido, jurisprudência inventada, pedido incongruente.
