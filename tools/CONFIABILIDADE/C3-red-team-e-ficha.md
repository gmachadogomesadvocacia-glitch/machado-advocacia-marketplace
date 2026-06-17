# CAMADA 3 — VERIFICAÇÃO ADVERSARIAL (RED-TEAM) + FICHA DE CONFERÊNCIA

> Especificação canônica do sistema de confiabilidade (defesa em profundidade).
> Esta é a fonte da verdade; o mecanismo roda dentro de cada `revisao-final-<area>`.
> Objetivo: capturar o erro que o R1-R4 (construtivo) deixa passar.

## Por que existe
O R1-R4 audita "está correto?" — olhando a peça com olhos amigos. Mas o produtor e o
revisor compartilham o mesmo raciocínio e os mesmos pontos cegos. O caso-piloto provou:
o R1-R4 aprovou uma peça com **erro de quantum** (restituível ≈ R$ 95 tratado como R$ 335)
e **instrumento errado** (mirou no IRPF municipal de fonte, quando o indébito grande estava
no ajuste anual/DIRPF contra a União). A verificação ADVERSARIAL inverte o ônus: o revisor
vira o ADVERSÁRIO e sua única missão é **derrubar** a peça.

## R5 — VERIFICAÇÃO ADVERSARIAL (rodada extra, após R1-R4)
Mude de chapéu: você AGORA é a parte contrária / o juízo cético / o Fisco. Para cada eixo,
TENTE refutar. Achou UMA falha real → REPROVADO: aponta e devolve. Não passe com dúvida.

1. **VALORES** — algum R$ na peça não tem origem rastreável no bloco de cálculo (`calculos-*`)?
   O período/marco está certo? (REGRA: o valor pleiteado corre do FATO GERADOR do direito,
   não do total bruto — ex.: isenção por doença corre da DATA DA DOENÇA, não do exercício
   inteiro; crédito de RJ atualiza até a DATA DO PEDIDO, não a data atual.)
2. **INSTRUMENTO / VIA** — é a peça certa? O dinheiro/indébito está mesmo ONDE a peça mira?
   (ex.: o IR está na fonte ou no ajuste anual? a discussão é de posse ou de domínio?)
3. **COMPETÊNCIA / FORO / RÉU** — corretos para QUEM praticou o ato/reteve? (federal ×
   estadual/municipal; vara competente; legitimidade passiva.)
4. **CITAÇÕES** — cada súmula/tema/artigo bate em número, tribunal e tese? Algo sem fonte?
   (cruzar com o livro-razão de jurisprudência — Camada 1.)
5. **PRESCRIÇÃO / PRAZO** — algum prazo perdido, mal contado, ou regime errado?
6. **POLO / COERÊNCIA** — algum argumento contra o próprio cliente? Pedido incompatível?
7. **DADO SENSÍVEL** — exposição desnecessária de saúde/fiscal (LGPD)?

Veredito R5: **PASSOU** / **REPROVADO (eixo + falha + correção)**.

## FICHA DE CONFERÊNCIA (acompanha TODA entrega, em bloco separado, "não integra a peça")
Torna a conferência do advogado rápida e segura — ele é a porta final (Camada 7).
```
FICHA DE CONFERÊNCIA — pré-protocolo
- PREMISSAS: [fáticas e jurídicas em que a peça se apoia]
- VALORES (cada R$ → fonte): R$ ___ — origem: bloco de cálculo (calculos-<area>), data ___
- CITAÇÕES (cada uma → status): [Súmula/Tema/art.] — CONFIRMADO (auditoria __) | VALIDAR
- LACUNAS [INFORMAR]: [o que preencher antes do protocolo]
- RISCOS / PONTOS ADVERSARIAIS: [o que a parte contrária explorará]
- VEREDITO: R1 __ · R2 __ · R3 __ · R4 __ · R5 (adversarial) __
- PENDE O OK INFORMADO DO ADVOGADO antes do protocolo.
```

## Como aplicar
- Em cada `revisao-final-<area>`: acrescentar a rodada **R5** e exigir a **FICHA** ao final.
- R5 REPROVADO bloqueia a entrega (igual a qualquer R reprovado — PA de "não entregar sem R1-Rn").
- Nada de bypass silencioso; só `--no-corte`/`--quick` explícito e registrado.

## Demonstração (caso jose-antonio)
R5 aplicado à peça do piloto teria reprovado em DOIS eixos:
- Eixo 1 (VALORES): "restituível por doença = só o retido após 06/11/2025 (~R$ 95), não os
  R$ 335 do exercício". → corrige o quantum.
- Eixo 2 (INSTRUMENTO/COMPETÊNCIA): "o indébito relevante está no ajuste anual (DARF) pago à
  UNIÃO; o requerimento à fonte municipal mira a parcela menor". → corrige a via e o réu.
Esses são exatamente os dois erros que o aprofundamento humano depois apontou.
