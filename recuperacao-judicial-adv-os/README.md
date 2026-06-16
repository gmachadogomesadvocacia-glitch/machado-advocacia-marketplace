# recuperacao-judicial-adv-os

> v0.2.1 — Eixo prioritário **CREDOR TRABALHISTA** (MODO CTH)
> Prescrição fundida em `credor-trabalhista-rj` §5-BIS

Plug-in jurídico de recuperação judicial e falência (L11.101/2005 +
L14.112/2020), com foco prioritário absoluto na **representação de
credores, especialmente CREDORES TRABALHISTAS**, em habilitação de
crédito.

## O que mudou da v0.1.0

- Plug-in reposicionado para o **lado do credor**, com prioridade
  absoluta ao crédito trabalhista.
- 4 skills novas: `credor-trabalhista-rj`, `via-processual-rj`,
  `calculo-credito-trabalhista-rj`, `cruzamento-jt-rj`.
- Verificação de **prescrição** integrada à `credor-trabalhista-rj`
  como seção §5-BIS (bienal CF, intercorrente CLT, prescrição da
  habilitação, pós-encerramento art. 61).
- Refatoração da `habilitacao-credito-rj` em 4 sub-fluxos explícitos
  (§A divergência / §B impugnação / §C retardatária / §D art. 6º §2º).
- `rj-master` com **gatilho automático trabalhista** (MODO CTH).
- `triagem-rj` com **pergunta de polo PRIMEIRO** e bifurcação para
  credor/devedora.
- +11 Proibições Absolutas específicas do MODO CTH (PA-CTH-01 a 11).
- +1 Protocolo Técnico: **P8 — Cruzamento JT × RJ**.

## 19 Skills incluídas

### Eixo prioritário — credor trabalhista (4 skills)

| Tier | Skill | Função |
|------|-------|--------|
| 2 — Produção | **credor-trabalhista-rj** | Eixo central — coleta 22 campos, concursalidade, redige peça por via, prescrição §5-BIS interna |
| 1 — Insumo | **via-processual-rj** | Decisora pura: divergência × impugnação × retardatária × art. 6º §2º |
| 2 — Produção | **calculo-credito-trabalhista-rj** | Cálculo: atualização até pedido + teto 150 SM + segregação de verbas |
| Transversal (P8) | **cruzamento-jt-rj** | Ponte recuperacao-judicial-adv-os ↔ trabalhista-adv-os |

### Skills gerais (15 skills)

| Tier | Skill | Função |
|------|-------|--------|
| 0 — Master | rj-master | Orquestração + roteamento + MODO CTH |
| 1 — Insumo | triagem-rj | Polo primeiro, depois enquadramento, CASO.md |
| 1 — Insumo | auditoria-documental-rj | Documentos do art. 51 + sentenças + CH |
| 1 — Insumo | analise-viabilidade-rj | Laudo de viabilidade (art. 53, II) |
| 1 — Insumo | jurisprudencia-rj | STJ, STF, TST, súmulas, temas, IACs |
| 2 — Produção | plano-recuperacao-rj | Plano completo (arts. 50, 53, 54) |
| 2 — Produção | assembleia-credores-rj | AGC: quóruns e estratégia de votação |
| 2 — Produção | habilitacao-credito-rj | QGC e crédito **não-trabalhista** (4 sub-fluxos) |
| 2 — Produção | contestacao-rj | Impugnação ao pedido, plano e falência |
| 2 — Produção | tutela-urgencia-rj | Stay period, liminares, DIP financing |
| 2 — Produção | acordo-extrajudicial-rj | RE arts. 161-167 LFRJ |
| 2 — Produção | recurso-rj | AI (art. 17), apelação, REsp, MS |
| 3 — Auditoria | revisao-final-rj | R1-R4 obrigatório pré-protocolo |
| Transversal | memoria-de-caso-rj | CASO.md — estado vivo do processo |
| Transversal | estilo-juridico-rj | Padrão de redação em insolvência |

## Arquitetura

- **25 Proibições Absolutas** gerais (PA-01 a PA-25)
- **11 Proibições Absolutas do MODO CTH** (PA-CTH-01 a PA-CTH-11)
- **8 Protocolos Técnicos** (P1 a P8 — P8 é novo)
- **FIRAC Insolvência** — identidade técnica
- **Side-Awareness** — estratégia adapta ao polo (credor/devedora/AJ)
- **CASO.md por processo** — credor-centric ou devedor-centric, LGPD-compliant
- **Gatilho automático trabalhista** — detecção de léxico ativa MODO CTH

## Como usar

1. Descreva o caso ou invoque `rj-master`.
2. Responda à pergunta de polo (credor / devedora / AJ).
3. Se for credor trabalhista, o **MODO CTH** assume o controle e
   conduz coleta + decisão de via + cálculo + redação.
4. Se for outro credor, segue por `habilitacao-credito-rj`.
5. Se for a recuperanda, a triagem clássica do art. 48 / art. 51 é executada.
6. Toda peça passa por `revisao-final-rj` (R1-R4) antes da entrega.

## Integração

- Casa naturalmente com o plug-in **`trabalhista-adv-os`** (via P8 —
  `cruzamento-jt-rj`).
- Casa com **`calculos-pjecalc`** para liquidação trabalhista delegada
  ao PjeCalc (quando configurado para parar na data do pedido de RJ).
