---
name: memoria-de-caso-familia
description: >
  MEMORIA-DE-CASO-FAMILIA — Transversal (Estado Vivo do Processo). Cria, lê, atualiza e
  consolida o CASO.md de cada caso de família ou sucessões. Deve ser consultada no início
  de toda sessão de trabalho e atualizada ao final. Armazena: polo, fase, patrimônio mapeado,
  filhos, acordos parciais, prazos, histórico de peças e alertas ativos. Acionar quando o
  usuário pedir para "salvar o caso", "atualizar o status", "onde estamos no processo",
  "registrar o acordo parcial" ou ao iniciar uma nova sessão sobre um caso já triado.
metadata:
  version: "1.0.0"
---

# MEMORIA-DE-CASO-FAMILIA
> Transversal | Estado Vivo do Processo | CASO.md por caso | LGPD-compliant

---

## 0. ESCOPO

O CASO.md é o estado persistente de cada caso. Esta skill:
- Lê o CASO.md ao início de cada sessão
- Atualiza o CASO.md após cada fase concluída
- Registra peças produzidas, acordos parciais, decisões, prazos
- Emite alertas de prazos críticos
- Mantém confidencialidade por caso (PA-19)

---

## 1. OPERAÇÕES

### 1.1 Ao iniciar sessão
```
INÍCIO DE SESSÃO — verificar:
1. Existe CASO.md para este caso?
   SIM → ler + resumir estado atual em 3-5 linhas
   NÃO → acionar triagem-familia para criar

2. Apresentar ao advogado:
   "Retomando o caso [NOME]:
    - Fase: [atual]
    - Última ação: [data + o que foi feito]
    - Prazos críticos: [se houver]
    - Pendências: [lista]"
```

### 1.2 Após produção de peça
```
ATUALIZAÇÃO PÓS-PEÇA:
1. Registrar no Histórico: data + tipo de peça + status (rascunho/protocolada/entregue)
2. Atualizar a Fase atual se houver progressão
3. Registrar novos documentos juntados
4. Atualizar prazos próximos
5. Marcar alertas resolvidos / adicionar novos
```

### 1.3 Após audiência ou acordo parcial
```
REGISTRO DE AUDIÊNCIA/ACORDO:
1. Resumir o resultado em até 5 itens
2. Registrar qualquer acordo parcial com valor/condição
3. Atualizar fase
4. Registrar nova data de audiência ou prazo processual
```

---

## 2. MODELO DO CASO.md

```markdown
# CASO: [NOME DO CLIENTE] — [REFERÊNCIA INTERNA]

**Criado em:** [data]
**Última atualização:** [data]
**Advogado:** {{ADVOGADO_NOME}} — OAB/{{OAB_UF}} {{OAB_NUMERO}}

---

## IDENTIFICAÇÃO

**Polo do cliente:** [Requerente / Requerido / Inventariante / Herdeiro / Consultor]
**Área:** [Família / Sucessões / Ambas]
**Tipo:** [Divórcio Litigioso / Inventário Extrajudicial / Guarda / etc.]
**Fase atual:** [Triagem / Petição / Contestação / Instrução / Acordo / Recurso / Execução / Encerrado]
**Processo nº:** [quando disponível]
**Vara/Comarca:** [Vara de Família — {{CIDADE}}/{{UF}} / Extrajudicial — Tabelionato X]
**Juiz(a):** [quando identificado]

---

## NÚCLEO FAMILIAR

| Parte | Nome | CPF | Qualificação | Vínculo |
|-------|------|-----|-------------|---------|
| Cliente | | | | |
| Contraparte | | | | |
| Filho(a) 1 | | | [idade] | |
| Filho(a) 2 | | | [idade] | |

**Regime de bens:** [comunhão parcial / universal / separação total / participação]
**Início do casamento/união:** [data]
**Separação de fato:** [data, se houver]
**Dissolução formal:** [data, se houver]

---

## PATRIMÔNIO MAPEADO

| Bem | Tipo | Natureza | Valor estimado | Observação |
|----|------|----------|----------------|------------|
| | Imóvel | Comum | | |
| | Veículo | Exclusivo | | |
| | Investimento | Comum | | |
| | Empresa | | | |
| **TOTAL COMUM** | | | | |
| **MEAÇÃO** (50%) | | | | |

---

## FILHOS E MENORES

| Nome | DN | Guarda atual | Alimentos atuais | Escola/plano |
|------|-----|-------------|-----------------|-------------|

---

## DOCUMENTOS

| Documento | Status | Data de obtenção |
|-----------|--------|-----------------|
| Certidão de casamento/óbito | [ ] Recebido / [ ] Pendente | |
| RG e CPF das partes | [ ] Recebido / [ ] Pendente | |
| Escritura/matrícula imóvel | [ ] Recebido / [ ] Pendente | |
| CRLV veículo | [ ] Recebido / [ ] Pendente | |
| IR últimos 2 anos | [ ] Recebido / [ ] Pendente | |
| Holerites / extratos | [ ] Recebido / [ ] Pendente | |
| Certidão de nascimento filhos | [ ] Recebido / [ ] Pendente | |

---

## ACORDOS PARCIAIS / DECISÕES

| Data | Tema | Resultado | Observação |
|------|------|-----------|------------|

---

## ALERTAS E PRAZOS CRÍTICOS

| Prazo | Data limite | Status |
|-------|-------------|--------|
| | | |

---

## HISTÓRICO

| Data | Evento / Fase | Peça produzida | Status |
|------|--------------|----------------|--------|
| [criação] | Triagem inicial | CASO.md | Concluído |
```

---

## 3. GESTÃO DE MÚLTIPLOS CASOS

Cada caso tem seu próprio CASO.md. Nomear o arquivo com referência única:
`CASO_[SOBRENOME_CLIENTE]_[ANO]_[TIPO].md`

Exemplos:
- `CASO_SILVA_2026_DIVORCIO.md`
- `CASO_MARTINS_2026_INVENTARIO.md`
- `CASO_FERREIRA_2026_GUARDA.md`

⚠️ **PA-19**: Nunca mesclar informações de casos distintos. LGPD — sigilo absoluto.

---

## 4. ALERTAS AUTOMÁTICOS

Ao atualizar o CASO.md, sempre verificar:

```
□ Prazo de inventário: 60 dias da ciência do óbito (PA-08)
□ Prazo de recurso: 15 dias da publicação da decisão
□ Prazo de alimentos provisionais: verificar ordem de pagamento
□ Data de audiência próxima: preparar com 7 dias de antecedência
□ Necessidade de laudo pericial (guarda / patrimônio): solicitar com antecedência
□ Pendência de documentos: cobrar antes de protocolo
```
