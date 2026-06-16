---
name: recuperacao-judicial-adv-os
description: >
  RECUPERACAO-JUDICIAL-ADV — Plug-in jurídico especializado em
  recuperação judicial e falência, com EIXO PRIORITÁRIO ABSOLUTO na
  REPRESENTAÇÃO DO CREDOR, especialmente o CREDOR TRABALHISTA, em
  habilitação de crédito. Cobre toda a L11.101/2005 + L14.112/2020 +
  CLT + jurisprudência STJ/STF/TST. Acionado quando o assunto envolver
  empresa em crise, RJ, RE, falência, AGC, QGC, stay period, plano de
  recuperação, administrador judicial, habilitação, divergência,
  impugnação, retardatária, ou crédito trabalhista a habilitar.
  Detecção automática de léxico trabalhista → MODO CTH (Credor
  Trabalhista Habilitando). Orquestra 19 skills especializadas com 25
  Proibições Absolutas + 11 PA-CTH e 8 Protocolos Técnicos. Para
  começar: use `rj-master` ou descreva o caso.
---

# RECUPERACAO-JUDICIAL-ADV
> Plug-in | Insolvência Empresarial | L11.101/2005 + L14.112/2020
> EIXO PRIORITÁRIO: Credor Trabalhista (MODO CTH)

Para usar, invoque a skill adequada. Em caso de dúvida, comece por
`rj-master` ou descreva o caso — o léxico trabalhista ativa o MODO CTH
automaticamente.

## Skills do eixo prioritário (credor trabalhista)

| Necessidade | Skill |
|-------------|-------|
| **Habilitar / impugnar / divergir / retardatária — crédito trabalhista** | **`credor-trabalhista-rj`** |
| Decidir VIA (divergência × impugnação × retardatária × art. 6º §2º) | `via-processual-rj` |
| Calcular crédito trabalhista (150 SM + verbas) | `calculo-credito-trabalhista-rj` |
| Cruzar caso JT × caso RJ (Protocolo P8) | `cruzamento-jt-rj` |
| Verificar prescrição (bienal / intercorrente / habilitação) | `credor-trabalhista-rj` §5-BIS (interno) |

## Skills gerais

| Necessidade | Skill |
|-------------|-------|
| Começar um novo caso / orientação geral | `rj-master` |
| Triagem inicial e enquadramento | `triagem-rj` |
| Análise de documentos do art. 51 | `auditoria-documental-rj` |
| Laudo de viabilidade econômica | `analise-viabilidade-rj` |
| Pesquisa de jurisprudência STJ/STF/TST | `jurisprudencia-rj` |
| Elaborar plano de recuperação | `plano-recuperacao-rj` |
| Preparar para a AGC | `assembleia-credores-rj` |
| Habilitar / impugnar crédito não-trabalhista | `habilitacao-credito-rj` |
| Contestar pedido ou impugnar plano | `contestacao-rj` |
| Urgências (stay, liminares) | `tutela-urgencia-rj` |
| Recuperação extrajudicial | `acordo-extrajudicial-rj` |
| Recursos (AI, apelação, REsp) | `recurso-rj` |
| Revisar peça antes de protocolar | `revisao-final-rj` |
| Salvar / atualizar estado do caso | `memoria-de-caso-rj` |
| Padrão de redação | `estilo-juridico-rj` |
