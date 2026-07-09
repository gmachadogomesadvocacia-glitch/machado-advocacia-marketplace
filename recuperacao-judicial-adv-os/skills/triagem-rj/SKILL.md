---
name: triagem-rj
description: >
  TRIAGEM-RJ — Tier 1 (Porta de Entrada). Realiza o enquadramento jurídico-estratégico inicial de casos de insolvência empresarial. Primeira pergunta SEMPRE: o cliente é CREDOR ou DEVEDORA? Para CREDOR TRABALHISTA, roteia imediatamente para `credor-trabalhista-rj` (eixo prioritário do plug-in). Para credor não-trabalhista, segue com `habilitacao-credito-rj`. Para devedora ou AJ, faz a triagem clássica (art. 48, art. 51, viabilidade). Cria o CASO.md credor-centric ou devedor-centric conforme o polo.
---

# TRIAGEM-RJ

> Tier 1 | Enquadramento Inicial | Polo / Modalidade / Requisitos / Competência

---

## 0. ESCOPO

Ponto de entrada obrigatório para qualquer novo caso. Ela:
- **Pergunta o polo PRIMEIRO** (credor / devedora / AJ / consultor).
- Detecta léxico trabalhista para ativar MODO CTH automaticamente.
- Para credor trabalhista: roteia para `credor-trabalhista-rj`.
- Para credor não-trabalhista: roteia para `habilitacao-credito-rj`.
- Para devedora: verifica art. 48 + mapeia art. 51 + competência.
- Para AJ: identifica fase + tarefa.
- Cria o CASO.md adequado ao polo.

Não produz peças. Produz: CASO.md + diagnóstico + roteamento.

---

## 1. POSIÇÃO NA ORQUESTRA

```
Usuário descreve o caso
        ↓
   [triagem-rj]  ← Tier 1
        ↓
  ┌─────────────────────────────────────────┐
  │ Pergunta única e obrigatória:           │
  │  "Cliente = CREDOR ou DEVEDORA?"        │
  └─────────────────────────────────────────┘
        ↓
  ┌──────────────────┬──────────────────────────┐
  │ CREDOR           │ DEVEDORA / AJ / CONSULTOR│
  └──────────────────┴──────────────────────────┘
        ↓                       ↓
  léxico trabalhista?     triagem clássica
        ↓                       ↓
  SIM → credor-trabalhista-rj   auditoria-documental-rj
  NÃO → habilitacao-credito-rj  + analise-viabilidade-rj
```

---

## 2. PROTOCOLO DE TRIAGEM

### 2.0 PRIMEIRA PERGUNTA — INVIOLÁVEL

```
"Antes de qualquer coisa, confirme:

(a) o cliente do escritório é o CREDOR (alguém a quem a empresa em
    RJ deve dinheiro) ou a RECUPERANDA (a própria empresa em RJ)?

(b) se for credor: o crédito tem origem TRABALHISTA (sentença da
    Justiça do Trabalho, acordo homologado na JT, FGTS, verbas
    rescisórias, reclamatória, certidão de crédito da JT)?"
```

Sem essas duas respostas, NÃO avance.

### 2.1 ROTEAMENTO IMEDIATO

```
SE (a) = CREDOR  E  (b) = SIM:
    → MODO CTH ativado
    → encerrar triagem clássica
    → repassar para `credor-trabalhista-rj` (coleta dos 22 campos)
    → criar CASO.md credor-centric (estrutura §3.2)

SE (a) = CREDOR  E  (b) = NÃO:
    → repassar para `habilitacao-credito-rj`
    → criar CASO.md credor-centric (estrutura §3.2)

SE (a) = RECUPERANDA:
    → seguir triagem clássica (§2.2 a §2.6)
    → criar CASO.md devedor-centric (estrutura §3.3)

SE (a) = AJ ou CONSULTOR:
    → identificar tarefa específica
    → criar CASO.md de papel-específico (estrutura §3.4)
```

---

## 2.2 TRIAGEM CLÁSSICA — POLO DEVEDORA

Apenas se (a) = RECUPERANDA.

### Coleta

**Sobre o cliente:**
1. Razão social, CNPJ, forma societária (LTDA, S.A., ME, EPP).
2. Tempo de atividade regular (mínimo 2 anos — art. 48).
3. Já houve pedido de RJ/RE/falência anterior?
4. Grupo econômico? Outras empresas envolvidas?

**Sobre a situação financeira:**
5. Passivo estimado total. Composição (trabalhistas, financeiros,
   fornecedores, fiscais).
6. Ativos relevantes.
7. A empresa ainda opera? Faturamento mensal?
8. Execuções fiscais, protestos, ações em andamento?

**Sobre o contexto processual:**
9. Processo de RJ ou falência em trâmite?
10. Urgência (leilão, penhora, despejo)?

### Verificação de Elegibilidade — art. 48 LFRJ

| Requisito | Status |
|-----------|--------|
| Exercício regular há mais de 2 anos | Sim / Não / Verificar |
| Não obteve RJ há menos de 5 anos | Sim / Não / Verificar |
| Não obteve RJ especial (ME/EPP) há menos de 5 anos | Sim / Não / Verificar |
| Não condenado por crime falimentar | Sim / Não / Verificar |
| (S.A.) Administradores não condenados | Sim / Não / Verificar |

⚠️ **PA-18**: se requisito negativo → RJ inviável → avaliar RE ou autofalência.

### Modalidade

| Modalidade | Quando indicar |
|-----------|----------------|
| RJ (art. 47) | Devedor elegível; viabilidade demonstrável |
| RE (art. 161) | Credores específicos; negociação direta |
| Falência requerida | Devedor sem viabilidade |
| Medidas preventivas | Stay urgente, arbitragem |

### Competência — Súm. 480 STJ

```
Competência → Juízo do local do PRINCIPAL estabelecimento
             (maior volume de negócios)
             ≠ sede estatutária / ≠ domicílio dos sócios

Grupo econômico com consolidação → competência unitária no juízo
do devedor principal (PA-14).
Verificar se a comarca tem vara especializada empresarial.
```

### Documentos — art. 51 LFRJ

| Doc | Artigo | Prioridade |
|-----|--------|-----------|
| Exposição das causas | art. 51, I | Alta |
| Demonstrações contábeis (3 anos) | art. 51, II | Alta |
| Relação nominal de credores | art. 51, III | Alta |
| Relação de empregados | art. 51, IV | Alta |
| Certidão na Junta Comercial | art. 51, V | Alta |
| Relação de bens do ativo | art. 51, VI | Alta |
| Extratos bancários | art. 51, VII | Alta |
| Relação de ações/processos | art. 51, VIII | Média |
| Certidões de protesto | art. 51, IX | Média |
| Relação de administradores | art. 51, X | Média |

⚠️ **PA-06**: Plano em **60 dias** após o deferimento (prorrogável por
mais 60 — L14.112).

---

## 2.3 TRIAGEM POLO CREDOR (NÃO-TRABALHISTA)

Apenas se (a) = CREDOR e (b) = NÃO.

### Coleta

1. Nome do credor + CPF/CNPJ.
2. Natureza do crédito (fornecedor / bancário / locatício / cível / outro).
3. Origem (contrato, NF, sentença cível, CCB, contrato de locação).
4. Valor histórico + atualizado + data-base.
5. Período / fato gerador.
6. Recuperanda — razão social + CNPJ.
7. Processo de RJ — nº, juízo, comarca.
8. Data do pedido de RJ.
9. Edital do art. 52 §1º publicado? Quando?
10. Relação consolidada do AJ publicada? Quando?
11. Credor consta na relação? Como?
12. QGC homologado?

### Roteamento

→ `habilitacao-credito-rj` (sub-fluxos §A/§B/§C/§D).

---

## 2.4 TRIAGEM POLO CREDOR TRABALHISTA

→ Repassar TUDO para `credor-trabalhista-rj` (que tem a coleta dos
22 campos e os roteamentos próprios). A `triagem-rj` apenas confirma
o roteamento e cria o CASO.md.

---

## 3. CRIAÇÃO DO CASO.md

### 3.1 Identificador

```
Padrão de nomeação:
RJ_<recuperanda-slug>_<credor-slug-se-credor>_<ano>.md

Exemplos:
RJ_INDUSTRIA_X_2026.md
RJ_INDUSTRIA_X_FULANO_DE_TAL_2026.md
```

### 3.2 CASO.md credor-centric (polo CREDOR)

```markdown
# CASO: [RJ_DEVEDOR_CREDOR_ANO]

**Data de abertura:** [data]
**Polo do cliente:** CREDOR ([trabalhista / outro])
**Modo:** [CTH / padrão]
**Modalidade:** RJ
**Fase atual:** Triagem
**Processo RJ nº:** [...]
**Vara/Comarca:** [...]
**Administrador Judicial:** [...]

## 1. Recuperanda
- Razão social / CNPJ:
- Data do pedido de RJ:
- Data do deferimento (art. 52):
- Edital art. 52 §1º — data:
- Relação consolidada (art. 7º §2º) — data:
- QGC homologado — data:

## 2. Crédito do Cliente
- Natureza: [trabalhista / fornecedor / financeiro / ...]
- Origem: [...]
- Fato gerador: [início → fim]
- Concursalidade: [a definir]
- Valor histórico: R$ [...]
- Valor atualizado (até data do pedido): R$ [...]
- Classe(s) pretendida(s): [...]
- Via: [a definir via `via-processual-rj`]
- Documentos disponíveis: [lista]
- Processo trabalhista correlato (se trabalhista): nº [...] fase [...]
- CH expedida: sim / não

## 3. Status na Relação
- [ ] Consta na relação do art. 7º §2º
- [ ] Consta no QGC homologado
- Valor atribuído: R$ [...]
- Classe atribuída: [...]

## 4. Alertas Ativos
- ⚠️ [...]

## 5. Histórico
| Data | Evento | Responsável |
|------|--------|-------------|
| [hoje] | Triagem inicial | [advogado] |
```

### 3.3 CASO.md devedor-centric

Manter estrutura prévia (§3 do antigo SKILL.md), conservada em
`memoria-de-caso-rj`.

### 3.4 CASO.md AJ / consultor

Variante simplificada com foco no papel.

---

## 4. CHECKPOINT 1

Ao final, apresente ao advogado:

```
CHECKPOINT 1 — VALIDAÇÃO DE TRIAGEM

✅ Polo identificado: [...]
✅ Modo: [CTH / padrão]
✅ Modalidade: [...]
✅ Competência: [...]
⚠️ Requisitos pendentes: [...]
⚠️ Documentos faltantes: [...]
⚠️ Urgências identificadas: [...]

Próximos passos:
1. [ação imediata]
2. [skill a acionar a seguir]

CONFIRMAR para prosseguir?
```

Só avança após confirmação do advogado (PA-02).

---

## 5. INTEGRAÇÃO

- **Detecção de léxico trabalhista** → ativar MODO CTH e migrar.
- **Após triagem** → `credor-trabalhista-rj` ou `habilitacao-credito-rj`
  ou `auditoria-documental-rj` (devedora).
- **CASO.md** sempre criado/atualizado via `memoria-de-caso-rj`.
