# familia-sucessoes-adv-os

Plugin completo de **Direito de Família e Sucessões** para advogados brasileiros.

**Advogado**: Gustavo Machado Gomes — OAB/RJ 172.089 — Machado Advocacia  
**Comarca principal**: Campos dos Goytacazes/RJ — 14ª Vara de Família  
**Versão**: 1.0.0

---

## 25 Skills incluídas

| Tier | Skill | Função |
|------|-------|--------|
| 0 — Master | `familia-master` | Orquestração central + roteamento |
| 1 — Insumo | `triagem-familia` | Enquadramento inicial + CASO.md |
| 1 — Insumo | `onboarding-familia` | Cadastro do cliente + escritório |
| 1 — Insumo | `analise-documental-familia` | Certidões, matrículas, laudos, IR, extratos |
| 1 — Insumo | `jurisprudencia-familia` | STJ / STF / TJRJ — família e sucessões |
| 2 — Produção | `peticao-inicial-familia` | Petição inicial (divórcio, guarda, inventário, etc.) |
| 2 — Produção | `contestacao-familia` | Contestação e resposta |
| 2 — Produção | `replica-familia` | Réplica e resposta à reconvenção |
| 2 — Produção | `tutela-urgencia-familia` | Alimentos provisionais, guarda liminar, MPU, arresto |
| 2 — Produção | `audiencia-familia` | Preparação para audiências de família |
| 2 — Produção | `acordo-familia` | Acordos extrajudiciais e homologação judicial |
| 2 — Produção | `recurso-familia` | Apelação, agravo, REsp, RE |
| 2 — Produção | `embargos-declaracao-familia` | Embargos de declaração + prequestionamento |
| 2 — Produção | `calculos-familia` | Meação, monte-mor, alimentos, ITCMD/RJ, ITBI |
| 2 — Produção | `inventario-arrolamento` | Inventário judicial/extrajudicial, arrolamento |
| 2 — Produção | `planejamento-sucessorio` | Testamento, doação com usufruto, holding familiar |
| 2 — Produção | `divorcio-separacao` | Divórcio judicial e extrajudicial |
| 2 — Produção | `guarda-alimentos` | Guarda, convivência, alimentos, alienação parental |
| 2 — Produção | `uniao-estavel` | Reconhecimento, dissolução, direitos sucessórios |
| 2 — Produção | `interdicao-curatela` | Interdição, curatela, TDA — LBI |
| 2 — Produção | `timeline-familia` | Linha do tempo fática e processual |
| 3 — Auditoria | `revisao-final-familia` | R1-R4 obrigatório pré-protocolo |
| Transversal | `memoria-de-caso-familia` | CASO.md — estado vivo do processo |
| Transversal | `estilo-juridico-familia` | Padrão de redação + escala de tom |
| Transversal | `linha-estrategica-familia` | Estratégia / viabilidade / acordo vs. contencioso |

---

## Arquitetura

- **20 Proibições Absolutas** (PA-01 a PA-20) — invioláveis
- **6 Protocolos Técnicos** (P1-P6)
- **FIRAC Família** — identidade técnica (Fato + Issue + Regra + Aplicação + Conclusão)
- **Side-Awareness** — polo do cliente define toda a estratégia e as teses
- **CASO.md** por processo — LGPD-compliant, atualizado em tempo real
- **Escala de Tom** — 3/10 (acordos) a 9/10 (violência doméstica)

---

## Marco Normativo

| Norma | Cobertura |
|-------|-----------|
| CC/2002 — Livros IV e V | Lei-base do plugin |
| CPC/2015 | Ações de família (arts. 693-699) + inventário (arts. 610-673) |
| ECA (L8.069/1990) | Guarda + melhor interesse |
| L13.146/2015 (LBI) | Interdição + TDA |
| L11.340/2006 (Maria da Penha) | Violência doméstica — interface |
| L12.318/2010 | Alienação parental |
| L11.804/2008 | Alimentos gravídicos |
| Res. 35/2007 CNJ | Divórcio + inventário extrajudicial |
| ITCMD/RJ | 4% sobre valor de mercado |

---

## Como usar

1. Comece com **`/familia-master`** para identificar o tipo de caso e ser roteado
2. Se novo caso: **`/triagem-familia`** para criar o CASO.md
3. Para cada tarefa, use a skill específica conforme a tabela de roteamento
4. Sempre termine com **`/revisao-final-familia`** antes de protocolar qualquer peça

---

## Fluxo típico

```
/familia-master → identifica o caso
/triagem-familia → cria CASO.md
/analise-documental-familia → analisa os documentos
/linha-estrategica-familia → define a estratégia
/peticao-inicial-familia → redige a petição
/revisao-final-familia → auditoria R1-R4
→ PROTOCOLA
```
