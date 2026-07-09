---
name: memoria-de-caso-rj
description: >
  MEMORIA-DE-CASO-RJ — Transversal (Estado Vivo). Acionar quando o usuário quiser salvar o estado atual do caso, registrar uma decisão, atualizar prazos, ou consultar o histórico de um processo de RJ. Protocolo P3 obrigatório.
---

# MEMORIA-DE-CASO-RJ
> Transversal | Estado Vivo do Caso | CASO.md | Protocolo P3

---

## 0. ESCOPO

Gerencia o estado persistente de cada caso de insolvência. Um CASO.md por processo.
Nunca mistura dados entre casos diferentes (PA-22 + LGPD).

Produz: CASO.md criado / atualizado + alertas de prazo + histórico de decisões.

### Onde mora o caso — pasta unificada

Cada caso vive em `<CASE_ROOT>/<slug>/`, com `CASO.md`, `MEMORY.md`, `arquivos/` e
`pecas/` (peças produzidas em `<slug>/pecas/`). Pasta COMPARTILHADA entre plugins do
mesmo cliente (ex.: RJ + trabalhista do mesmo credor) — um só caso por cliente.

`CASE_ROOT` vem do `config.md`:
- **Claude Code:** `<acervo>/Casos-Ativos` (acervo do escritório).
- **Fallback (Cowork):** `<COWORK>/recuperacao-judicial/casos`.

O estado interno do plugin (`recuperacao-judicial/cowork-state.json`) NÃO muda.

---

## 1. ESTRUTURA CANÔNICA DO CASO.md

```markdown
# CASO: [IDENTIFICADOR — ex: RJ_EMPRESA_NOME_2025]
**Versão:** [número]   **Última atualização:** [data]

---

## 1. IDENTIFICAÇÃO

| Campo | Dado |
|-------|------|
| Razão social do devedor | |
| CNPJ | |
| Forma societária | |
| Polo do cliente | Devedor / Credor: [nome + classe] / AJ / Consultor |
| Modalidade | RJ / RE / Falência / Consultivo |
| Processo nº | |
| Vara/Comarca | |
| Juiz | |
| Administrador Judicial | |
| Data do deferimento | |
| Fim do stay (180 dias) | |
| Prazo do plano (60 dias) | |

---

## 2. COMPOSIÇÃO DO PASSIVO

| Classe | Descrição | Valor estimado | % |
|--------|-----------|---------------|---|
| I — Trabalhistas | | | |
| II — Garantia real | | | |
| III — Quirografários | | | |
| IV — ME/EPP | | | |
| Extraconcursais (art. 84) | | | |
| Fiscais (não sujeitos) | | | |
| **TOTAL** | | | 100% |

---

## 3. MAPA DE CREDORES ESTRATÉGICOS

| Credor | Classe | Valor | % da classe | Posição (favorável/contrário/neutro) |
|--------|--------|-------|-------------|--------------------------------------|

---

## 4. DOCUMENTOS

### Recebidos e Analisados
- [ ] Exposição das causas (art. 51, I)
- [ ] Demonstrações contábeis 3 anos (art. 51, II)
- [ ] Relação de credores (art. 51, III)
- [ ] Relação de empregados (art. 51, IV)
- [ ] Certidão Junta Comercial (art. 51, V)
- [ ] Relação de bens do ativo (art. 51, VI)
- [ ] Extratos bancários (art. 51, VII)
- [ ] Relação de processos (art. 51, VIII)
- [ ] Certidões de protesto (art. 51, IX)
- [ ] Relação de administradores (art. 51, X)
- [ ] Laudo de viabilidade (art. 53, II)
- [ ] Laudo de avaliação de ativos (art. 53, III)

---

## 5. PRAZOS CRÍTICOS

| Prazo | Data-limite | Status |
|-------|------------|--------|
| Fim do stay (art. 6º, §4º) | | Ativo / Expirado / Prorrogado |
| Apresentação do plano (60 dias) | | Pendente / Cumprido / Atrasado |
| AGC (após publicação do plano) | | Agendada para: |
| Recursos pendentes | | |
| Habilitações pendentes | | |

---

## 6. PEÇAS PRODUZIDAS

| Data | Tipo de peça | Skill usada | Status | Protocolo nº |
|------|-------------|-------------|--------|--------------|

---

## 7. DECISÕES JUDICIAIS

| Data | Decisão | Dispositivo | Impacto | Recurso |
|------|---------|-------------|---------|---------|

---

## 8. ALERTAS ATIVOS

⚠️ [Prazo crítico / PA violada em potencial / Crédito disputado / Irregularidade]

---

## 9. ESTRATÉGIA ATUAL

[Linha estratégica adotada, objetivos de curto/médio prazo, pontos de atenção]

---

## 10. HISTÓRICO

| Data | Evento | Responsável | Observação |
|------|--------|-------------|------------|
```

---

## 2. OPERAÇÕES DO CASO.md

### 2.1 Criar novo CASO.md

Acionado por: triagem-rj (ao final do CHECKPOINT 1).
Preencher todos os campos disponíveis. Campos desconhecidos deixar em branco com "A preencher".

### 2.2 Atualizar após protocolo de peça

```
Adicionar em "6. Peças Produzidas":
| [data] | [tipo] | [skill] | Protocolada | [nº protocolo se disponível] |

Adicionar em "10. Histórico":
| [data] | Peça protocolada: [tipo] | [advogado] | [observação] |
```

### 2.3 Atualizar após decisão judicial

```
Adicionar em "7. Decisões Judiciais":
| [data] | [resumo da decisão] | [art. aplicado] | [impacto] | [recurso cabível?] |

Revisar "5. Prazos Críticos" — novas datas podem ter surgido da decisão.
Revisar "8. Alertas" — decisão cria novos riscos ou elimina alertas anteriores?
```

### 2.4 Atualizar após AGC

```
Registrar:
- Data e local da AGC
- Quórum atingido por classe
- Resultado da votação (aprovado / rejeitado / adiado)
- Cram down necessário?
- Próximos passos
```

### 2.5 Atualizar composição do passivo

Quando o QGC for homologado ou atualizado, registrar o passivo definitivo e
atualizar a coluna "Posição" dos credores estratégicos.

---

## 3. REGRAS DE INTEGRIDADE (LGPD + PA-22)

```
□ Cada processo tem seu próprio CASO.md — nunca reutilizar
□ Dados de clientes diferentes nunca cruzam skills
□ Documentos sensíveis (prontuários, extratos, contratos) referenciados por caminho,
  nunca copiados para o CASO.md
□ CASO.md deve ser armazenado em local seguro, não em repositórios públicos
□ Ao encerrar o caso: arquivar, não apagar — prazo prescricional pode requerer consulta
```

---

## 4. LEITURA DO CASO.md

Toda skill do pipeline de RJ DEVE ler o CASO.md antes de iniciar a produção.
Conflito entre o que está no CASO.md e o que o usuário diz? → Perguntar ao advogado.
CASO.md desatualizado? → Acionar memoria-de-caso-rj para atualização antes de prosseguir.
