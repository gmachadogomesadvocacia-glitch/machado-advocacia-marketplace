---
name: revisao-final-familia
description: >
  REVISAO-FINAL-FAMILIA — Tier 3 (Auditoria Pré-entrega). Executa a auditoria obrigatória
  R1-R4 em todas as peças produzidas antes do protocolo ou entrega ao cliente. Verifica: base
  normativa (CC/2002 + CPC/2015 + ECA + leis especiais), coerência de polo, validade de
  jurisprudência, prazos, consistência com o CASO.md, e qualidade da redação. Esta skill é
  OBRIGATÓRIA antes de qualquer protocolo — é o Protocolo P6 do sistema. Acionar sempre que
  uma peça de família ou sucessões estiver pronta para entrega ou protocolo.
metadata:
  version: "1.0.0"
---

# REVISAO-FINAL-FAMILIA
> Tier 3 | Auditoria Pré-entrega R1-R4 | Protocolo P6 | Obrigatória para toda peça

---

## 0. ESCOPO

Auditoria de quatro etapas (R1-R4) aplicada a toda peça do pipeline de família e sucessões.
Emite veredito: **APROVADO** / **APROVADO COM RESSALVAS** / **REPROVADO**.

⚠️ **PA-20**: Nenhuma peça é entregue ao cliente ou protocolada sem aprovação R1-R4.

---

## 1. AUDITORIA R1 — COLETA E DOCUMENTAÇÃO

```
R1.1 CASO.md disponível e atualizado?
  □ Polo do cliente identificado
  □ Tipo do caso definido (divórcio / guarda / inventário / etc.)
  □ Fase processual atual correta
  □ Processo nº e vara corretos (se aplicável)
  □ Dados do núcleo familiar completos

R1.2 Documentos de suporte verificados?
  □ Certidões (casamento, nascimento, óbito) anexadas
  □ Documentos de patrimônio (escrituras, CRLV, extratos) conferidos
  □ Comprovante de renda do alimentante (em casos de alimentos)
  □ Laudos / estudos sociais considerados (quando existentes)

R1.3 Lacunas identificadas e sinalizadas?
  □ Itens com [VERIFICAR] foram confirmados ou mantidos como alerta?
  □ Dados ausentes indicados explicitamente na peça?

RESULTADO R1: □ APROVADO  □ APROVADO COM RESSALVAS  □ REPROVADO
```

---

## 2. AUDITORIA R2 — BASE JURÍDICA E NORMATIVA

```
R2.1 Artigos do CC/2002 citados estão na versão vigente?
  □ Lei nº 14.382/2022 (desjudicialização — inventário + divórcio)
  □ Lei nº 13.058/2014 (guarda compartilhada obrigatória)
  □ Lei nº 13.146/2015 (LBI — curatela e TDA)
  □ Lei nº 11.804/2008 (alimentos gravídicos)
  □ Lei nº 12.318/2010 (alienação parental)

R2.2 Jurisprudência do STJ:
  □ Nenhum julgado inventado ou não localizado (PA-01)
  □ Súmulas corretamente enunciadas (ex: Súm. 1, 309 STJ; Súm. 377 STF — regime de separação legal)
  □ Temas repetitivos aplicáveis verificados
  □ Itens com [VERIFICAR] não incluídos como tese definitiva

R2.3 Prazos processuais corretos?
  □ Resposta do réu em ação de família: 30 dias (art. 335 CPC)
  □ Prazo para abertura de inventário: 60 dias da ciência do óbito (PA-08)
  □ Recursos (apelação): 15 dias (art. 1.003 §5º CPC)
  □ Agravo de instrumento: 15 dias (art. 1.003 §5º CPC)
  □ Embargos de declaração: 5 dias (art. 1.023 CPC)
  □ Alimentos provisionais: prazo para cumprimento (3 dias — art. 528 CPC)
  □ Prazo para impugnar partilha: 15 dias (art. 1.000 CPC)

R2.4 Competência correta?
  □ Vara de Família — {{CIDADE}}/{{UF}} (PA-05 / Súm. 1 STJ para alimentos)
  □ Extrajudicial: tabelionato competente identificado
  □ ITCMD: SEFAZ/{{UF}} — alíquota 4% verificada (PA-13)
  □ ITBI: Prefeitura Municipal de {{CIDADE}} (PA-14)

RESULTADO R2: □ APROVADO  □ APROVADO COM RESSALVAS  □ REPROVADO
```

---

## 3. AUDITORIA R3 — COERÊNCIA ESTRATÉGICA E DE POLO

```
R3.1 Coerência de polo (PA-02):
  □ A peça está redigida pelo polo correto?
  □ As teses não conflitam com a posição do cliente?
  □ Os pedidos são favoráveis ao cliente, não ao adversário?

R3.2 Coerência com o CASO.md:
  □ Nome e qualificação das partes corretos?
  □ Número do processo correto?
  □ Regime de bens correto? (PA-03)
  □ Data de casamento / início da união correta?
  □ Nome(s) e data(s) de nascimento dos filhos corretos?

R3.3 Estrutura FIRAC verificada:
  □ F (Fato): situação descrita com precisão, cronologia e documentação?
  □ I (Issue): interesse jurídico do cliente claramente identificado?
  □ R (Regra): base legal e jurisprudencial correta e vigente?
  □ A (Aplicação): tese aplicada especificamente ao caso concreto?
  □ C (Conclusão): pedido preciso, viável e coerente?

R3.4 Proibições Absolutas (PA-01 a PA-20):
  □ PA-04: Binômio necessidade-possibilidade verificado (alimentos)?
  □ PA-05: Melhor interesse da criança considerado (guarda)?
  □ PA-06: Meação vs. herança não confundidos?
  □ PA-07: Cálculo de partilha com regime de bens correto?
  □ PA-09: Extrajudicial só sem filhos menores / incapazes / litígio?
  □ PA-10: Testamento com legítima preservada?
  □ PA-17: Planejamento sucessório sem fraude à legítima?
  □ PA-18: Acordo de guarda com alimentos, visitas e reajuste?

RESULTADO R3: □ APROVADO  □ APROVADO COM RESSALVAS  □ REPROVADO
```

---

## 4. AUDITORIA R4 — QUALIDADE TÉCNICA E COMPLETUDE

```
R4.1 Endereçamento e qualificação:
  □ Cabeçalho correto (Vara / Tribunal / Processo)?
  □ Qualificação das partes completa (CPF, profissão, endereço, advogado, OAB)?
  □ Filhos identificados com nome e data de nascimento?

R4.2 Estrutura da peça:
  □ Divisão em capítulos/seções adequada ao tipo de peça?
  □ Numeração de itens consistente?
  □ Pedidos organizados em alíneas (a, b, c)?
  □ Valor da causa indicado (quando obrigatório)?

R4.3 Padrão de redação (estilo-juridico-familia):
  □ Tom ajustado ao tipo de peça?
  □ Terminologia correta (ver Seção 2 do estilo)?
  □ Parágrafos com tamanho adequado?
  □ Fatos narrados cronologicamente?

R4.4 Completude processual:
  □ Documentos a anexar indicados (rol de documentos)?
  □ Procuração mencionada (ad judicia et extra)?
  □ Pedido de intimação via portal eletrônico (sistema do TJ{{UF}})?
  □ Local: "{{CIDADE}}/{{UF}}, [data]"?
  □ Assinatura: "{{ADVOGADO_NOME}} — OAB/{{OAB_UF}} {{OAB_NUMERO}} — {{FIRM_NAME}}"?

R4.5 Revisão final:
  □ Ortografia e gramática corretas?
  □ Nenhum trecho de template não preenchido ("[...]", "[NOME]")?
  □ Datas e valores grafados corretamente por extenso?
  □ Gênero gramatical consistente com a parte (ele/ela, o(a) Requerente)?

RESULTADO R4: □ APROVADO  □ APROVADO COM RESSALVAS  □ REPROVADO
```

---

## 4-B. R5 — VERIFICACAO ADVERSARIAL (RED-TEAM)

> Camada 3 | Mude de chapeu: voce AGORA e a parte contraria / o juizo cetico.
> Unica missao: DERROTAR a peca. Achou UMA falha → REPROVADO.

```
EIXOS (FAMILIA / SUCESSOES):

□ VALORES — alimentos calculados pelo binomio necessidade-possibilidade?
  Partilha respeita meacao e regime de bens? O ITCMD vem do cálculo de
  familia (base, alíquota, isencao)?

□ INSTRUMENTO / VIA — e a peca certa? (divorcio x alimentos x inventario;
  judicial x extrajudicial; acao x acordo x tutela). Via compativel com o caso?

□ COMPETENCIA / FORO — foro do alimentando / da guarda observado (art. 53 CPC)?
  Segredo de justica requerido quando devido (art. 189 CPC)?

□ REGIME DE BENS / SUCESSAO — regime correto e ordem de vocacao hereditaria
  certa (art. 1.829 CC; Tema 809 STF para uniao estavel)?

□ CITACOES — sumulas / Temas batem na tese E no tribunal certo?
  (NAO usar Tema 692 em sucessao — e previdenciario.)

□ PRESCRICAO / PRAZO — alimentos pretéritos prescritos? Prazos recursais
  e de abertura observados?

VEREDITO R5: □ PASSOU  □ REPROVADO
  Se REPROVADO → indicar: eixo + falha + correcao.
```

---

## FICHA DE CONFERENCIA (acompanha a entrega, nao integra a peca)

```
FICHA DE CONFERENCIA — pre-protocolo
- PREMISSAS: ...
- VALORES (cada R$ → fonte): ...
- CITACOES (cada uma → status): Tema 809 STF — CONFIRMADO | VALIDAR
- LACUNAS [INFORMAR]: ...
- RISCOS / PONTOS ADVERSARIAIS: ...
- VEREDITO: R1 _ · R2 _ · R3 _ · R4 _ · R5 _
- PENDE O OK INFORMADO DO ADVOGADO antes do protocolo.
```

---

## 5. VEREDITO FINAL

```
╔══════════════════════════════════════════════════════════╗
║  VEREDITO DE REVISÃO FINAL — [TIPO DA PEÇA / CASO]      ║
╠══════════════════════════════════════════════════════════╣
║  R1 (Documentação):     [ APROVADO / RESSALVAS / REPROVADO ] ║
║  R2 (Base jurídica):    [ APROVADO / RESSALVAS / REPROVADO ] ║
║  R3 (Coerência/Polo):   [ APROVADO / RESSALVAS / REPROVADO ] ║
║  R4 (Qualidade):        [ APROVADO / RESSALVAS / REPROVADO ] ║
║  R5 (Adversarial):      [ PASSOU / REPROVADO ]               ║
╠══════════════════════════════════════════════════════════╣
║  VEREDITO GLOBAL:                                        ║
║  [ ] ✅ APROVADO — peça pronta para protocolo            ║
║  [ ] ⚠️  APROVADO COM RESSALVAS — protocolar com         ║
║          atenção a: [lista de ressalvas]                  ║
║  [ ] ❌ REPROVADO — corrigir antes de protocolar:        ║
║          [lista de falhas críticas]                       ║
╚══════════════════════════════════════════════════════════╝
```

**APROVADO**: Peça pode ser protocolada ou entregue ao cliente.

**APROVADO COM RESSALVAS**: Protocolar com ciência do advogado sobre os pontos pendentes.
Ressalvas típicas: valor de bem a confirmar, julgado a verificar, ITCMD a calcular.

**REPROVADO**: NUNCA protocolar. Retornar à skill que gerou a peça com lista de falhas.
Falhas típicas: polo errado, meação/herança confundidas, pedido sem base legal, regime de
bens equivocado, prazo perdido, menor sem proteção adequada. Basta UMA falha em R5
(adversarial) para reprovar.

---

## ENCERRAMENTO

A auditoria so se conclui com as cinco etapas **R1-R5** vencidas e a **FICHA DE
CONFERENCIA** anexada à entrega. A peca NAO e protocolada nem entregue sem o OK
INFORMADO do advogado registrado na FICHA.
