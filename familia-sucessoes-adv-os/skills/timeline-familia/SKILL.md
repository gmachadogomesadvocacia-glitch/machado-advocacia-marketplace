---
name: timeline-familia
description: >
  TIMELINE-FAMILIA — Tier 2 (Produção). Constrói a linha do tempo fática e processual de
  casos de família e sucessões: cronologia da relação conjugal, fatos relevantes para a
  partilha, histórico de convivência parental, evolução do inventário, datas de transmissão
  de bens, e timeline processual com prazos e marcos. Essencial para casos complexos com
  muitos eventos. Acionar quando o caso tiver muitos fatos temporalmente relevantes ou quando
  o advogado precisar organizar a narrativa cronológica do caso.
metadata:
  version: "1.0.0"
---

# TIMELINE-FAMILIA
> Tier 2 | Produção | Linha do Tempo Fática + Processual | Família e Sucessões

---

## 0. ESCOPO

Organiza os fatos em ordem cronológica clara. Serve para:
- Construir a narrativa da petição inicial (FIRAC-F)
- Identificar bens adquiridos antes × durante × após a relação
- Mapear prazos decorridos e futuros
- Detectar atos de dilapidação patrimonial com data
- Demonstrar alienação parental com histórico

---

## 1. TIMELINE FÁTICA — DISSOLUÇÃO CONJUGAL

```
LINHA DO TEMPO — CASO [NOME]

📅 [DATA] — Início da relação (namoro / início da convivência)
📅 [DATA] — Início formal da união estável (se formalizada) / Casamento
           Regime de bens: [X]
📅 [DATA] — Aquisição do [BEM] — [comum / exclusivo de X]
📅 [DATA] — Nascimento de [FILHO 1]
📅 [DATA] — Aquisição do [BEM 2]
📅 [DATA] — Nascimento de [FILHO 2]
📅 [DATA] — Separação de fato
           → A partir daqui: bens adquiridos são exclusivos (CC art. 1.659)
           → Alimentos retroagem a esta data (verificar)
📅 [DATA] — [Evento relevante — venda de bem suspeita, mudança, etc.]
📅 [DATA] — Distribuição da ação
📅 [DATA] — Citação do requerido
📅 [DATA] — Contestação
📅 [DATA] — Audiência de conciliação
📅 [DATA] — Audiência de instrução
📅 [DATA] — Sentença
📅 [DATA — PROJETADA] — Recurso (apelação)
📅 [DATA — PROJETADA] — Trânsito em julgado
```

---

## 2. TIMELINE FÁTICA — INVENTÁRIO

```
LINHA DO TEMPO — INVENTÁRIO [NOME DO FALECIDO]

📅 [DATA] — Falecimento de [NOME] — [local]
📅 [DATA] — Ciência do óbito pelo herdeiro/inventariante
           → PRAZO FATAL: 60 dias para abrir o inventário (PA-08)
           → Prazo vence em: [DATA]
📅 [DATA] — Levantamento inicial dos bens
📅 [DATA] — Obtenção das certidões necessárias
📅 [DATA] — Pagamento do ITCMD (ou planejamento de pagamento)
📅 [DATA] — Abertura do inventário (judicial ou extrajudicial)
📅 [DATA] — Primeiras declarações
📅 [DATA] — Avaliação dos bens (se judicial)
📅 [DATA] — Últimas declarações / esboço de partilha
📅 [DATA] — Pagamento do ITCMD (se não pago antes)
📅 [DATA] — Homologação da partilha (judicial) / Lavratura da escritura (extrajudicial)
📅 [DATA] — Registro dos bens (imóveis no CRI, veículos no DETRAN)
📅 [DATA — PROJETADA] — Encerramento do inventário
```

---

## 3. TIMELINE DE CONVIVÊNCIA PARENTAL (para casos de guarda)

```
LINHA DO TEMPO — GUARDA DE [NOME DO FILHO]

📅 [DATA] — Nascimento — quem registrou, quem estava presente
📅 [DATA] — Início da vida com ambos os pais
📅 [DATA] — Separação dos pais — quem ficou com a criança?
📅 [DATA] — Primeira regulamentação informal de visitas
📅 [DATA] — Evento relevante [mudança de escola, mudança de cidade, etc.]
📅 [DATA] — Episódio relevante [negação de visitas, denúncia, conflito]
📅 [DATA] — Distribuição da ação de guarda
📅 [DATA] — Estudo psicossocial (se realizado)
📅 [DATA] — Oitiva do menor (se realizada)
📅 [DATA] — Decisão atual
📅 [DATA] — Recurso / revisão
```

---

## 4. TIMELINE PROCESSUAL (prazos)

```
CRONOGRAMA PROCESSUAL — [CASO] — atualizar em todo CASO.md

EVENTO                          | DATA          | STATUS
-------------------------------|---------------|--------
Protocolo da petição inicial   | [data]        | ✅ Concluído
Despacho de citação            | [data]        | ✅ Concluído
Citação do(a) Requerido(a)     | [data]        | ✅ / ⏳ Pendente
Prazo para contestação         | [data]        | ⏳ [X dias restantes]
Audiência de conciliação       | [data + hora] | ⏳
Audiência de instrução         | [data + hora] | ⏳
Sentença                       | [data estimada] | ⏳
Prazo para apelação            | [data]        | ⏳
```

---

## 5. IDENTIFICAÇÃO DE ATOS SUSPEITOS NA TIMELINE

Ao montar a linha do tempo, destacar em vermelho atos que ocorreram próximos à separação:

```
🔴 ALERTA: [AÇÃO SUSPEITA]
   Data: [data]
   O quê: [venda de imóvel / transferência de cotas / doação a terceiro]
   Contexto: [X dias / meses antes ou após a separação de fato]
   Risco: Alienação de bens comuns antes da partilha
   Fundamento: art. 1.674-1.676 CC (administração dos bens comuns durante o processo)
   Ação recomendada: requerer anulação + tutela cautelar de indisponibilidade
```

---

## 6. FORMATO DE SAÍDA

A timeline pode ser apresentada como:
- **Tabela cronológica** (default — clara e objetiva)
- **Narrativa fluida** (para inserção na petição inicial)
- **Diagrama simplificado** (para uso em audiência ou explicação ao cliente)

Após montar a timeline, integrar ao CASO.md e à peça processual (FIRAC-F da petição inicial).
