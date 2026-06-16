---
name: plano-recuperacao-rj
description: >
  PLANO-RECUPERACAO-RJ — Tier 2 (Produção). Redige o Plano de Recuperação Judicial completo
  conforme os arts. 53, 54 e 50 da LFRJ. Estrutura: discriminação detalhada dos meios de
  recuperação, laudo de viabilidade econômica, demonstração de cumprimento por classe de
  credores, cláusulas de haircut, carência, correção e garantias. Acionar quando o usuário
  precisar elaborar ou revisar o plano de RJ para o devedor, ou elaborar plano alternativo
  de credores (art. 56, §6º). Requer CASO.md atualizado, RAD (auditoria documental)
  e laudo de viabilidade (analise-viabilidade-rj) concluídos.
---

# PLANO-RECUPERACAO-RJ
> Tier 2 | Produção | Plano de Recuperação Judicial | Arts. 50, 53, 54 LFRJ

---

## 0. ESCOPO

Redige o Plano de Recuperação Judicial. Requer como insumos:
- CASO.md atualizado (polo = Devedor)
- RAD (auditoria-documental-rj) concluído
- Laudo de viabilidade (analise-viabilidade-rj) aprovado
- Relação de credores por classe (QGC ou estimativa)

⚠️ **PA-05**: Plano sem laudo de viabilidade é nulo de pleno direito (art. 53, II).
⚠️ **PA-06**: Prazo de 60 dias após deferimento para protocolo (prorrogável por mais 60 dias).
⚠️ **PA-07**: Classes I, II, III e IV devem ser tratadas em capítulos separados.

---

## 1. POSIÇÃO NA ORQUESTRA

```
auditoria-documental-rj  +  analise-viabilidade-rj
        ↓
  CHECKPOINT 2 (aprovado)
        ↓
  [plano-recuperacao-rj]  ←─ Tier 2
        ↓
  assembleia-credores-rj  →  revisao-final-rj  →  PROTOCOLO
```

---

## 2. REQUISITOS OBRIGATÓRIOS (art. 53)

| Requisito | Art. | Conteúdo mínimo |
|-----------|------|-----------------|
| Discriminação dos meios de recuperação | 53, I | Quais dos meios do art. 50 serão usados |
| Laudo de viabilidade econômica | 53, II | Demonstração técnica de viabilidade |
| Laudo de avaliação dos bens e ativos | 53, III | Avaliação por perito habilitado |
| Demonstração por fluxo de caixa | 53, caput | Projeção de pagamento das obrigações |

---

## 3. MEIOS DE RECUPERAÇÃO — art. 50 LFRJ

Selecionar os meios aplicáveis ao caso. Cada meio deve ser detalhado no plano:

| Meio | Art. 50 | Quando usar |
|------|---------|-------------|
| Concessão de prazos e condições especiais | I | Sempre — base do plano |
| Cisão, incorporação, fusão | II | Reestruturação societária |
| Transformação societária | III | Mudança de tipo societário |
| Alienação de filiais ou unidades produtivas | IV | Desinvestimento de ativos |
| Administração compartilhada | V | Crise de gestão |
| Emissão de valores mobiliários | VI | Captação de recursos |
| Constituição de sociedade de credores | VII | Conversão de dívida em participação |
| Venda parcial de ativos | XI | Liquidez imediata |
| Usufruto de empresa | XII | Credores assumem gestão temporária |
| Administração por terceiros | XIII | Gestão profissional externa |
| Trespasse | XIV | Alienação do estabelecimento |
| Dação em pagamento | XV | Créditos quitados com bens |

---

## 4. ESTRUTURA DO PLANO — TEMPLATE COMPLETO

```
PLANO DE RECUPERAÇÃO JUDICIAL
[RAZÃO SOCIAL DO DEVEDOR] — CNPJ: [...]
Processo nº [...] — Vara: [...]
Data de protocolo: [...]

PREÂMBULO
[Contextualização: histórico da empresa, causa da crise, missão do plano]

CAPÍTULO I — IDENTIFICAÇÃO DO DEVEDOR E DO PROCESSO
1.1 Dados da empresa (razão social, CNPJ, sede, atividade)
1.2 Composição societária atual
1.3 Número de empregados
1.4 Administrador Judicial nomeado
1.5 Deferimento do processamento: [data]
1.6 Termo de verificação: [data]

CAPÍTULO II — DIAGNÓSTICO DA CRISE
2.1 Natureza e causas da crise econômico-financeira
2.2 Indicadores financeiros históricos (3 anos)
2.3 Medidas já adotadas antes do pedido

CAPÍTULO III — MEIOS DE RECUPERAÇÃO (art. 53, I + art. 50)
3.1 [Meio 1 escolhido]: descrição detalhada, cronograma, responsáveis
3.2 [Meio 2 escolhido]: [idem]
[...]

CAPÍTULO IV — CONDIÇÕES DE PAGAMENTO POR CLASSE

IV.I — CLASSE I (CREDORES TRABALHISTAS E ACIDENTÁRIOS)
[⚠️ PA-08: Créditos até 150 SM por credor pagos em 1 ano — art. 54, caput]
[Créditos acima de 150 SM: tratamento como quirografário no excedente]

Condições:
- Prazo de carência: [máximo 1 ano após aprovação]
- Pagamento: [parcelas / datas]
- Correção: INPC/IPCA a partir do vencimento original
- Juros: [% a.m. sobre saldo devedor]

IV.II — CLASSE II (CREDORES COM GARANTIA REAL)
[Limite: valor do bem dado em garantia — excedente migra para Classe III]

Condições:
- Prazo de carência: [...]
- Deságio (haircut): [%] — fundamentar com laudo de viabilidade
- Correção: IPCA/IGP-M
- Manutenção das garantias reais existentes

IV.III — CLASSE III (CREDORES QUIROGRAFÁRIOS)
Condições:
- Prazo total: [anos]
- Carência: [meses]
- Haircut: [%] — fundamentado pelo cenário pessimista do laudo
- Correção: IPCA
- Juros: [%] a partir do [mês]

IV.IV — CLASSE IV (MICROEMPRESAS E EPP) [se houver]
[Tratamento diferenciado — L14.112/2020 — condições mais favoráveis]

CAPÍTULO V — CRÉDITOS NÃO SUJEITOS À RECUPERAÇÃO JUDICIAL
5.1 Créditos tributários e fiscais (não se sujeitam — negociar PERT/parcelamento)
5.2 Créditos do proprietário fiduciário (alienação fiduciária)
5.3 Arrendamentos mercantis
5.4 Adiantamentos de Contratos de Câmbio (ACC)
5.5 Créditos em moeda estrangeira com garantia de exportação

CAPÍTULO VI — LAUDO DE VIABILIDADE ECONÔMICO-FINANCEIRA
[Incorporar ou remeter ao Laudo elaborado por analise-viabilidade-rj]

CAPÍTULO VII — LAUDO DE AVALIAÇÃO DOS BENS E ATIVOS (art. 53, III)
[Avaliação por empresa especializada ou perito indicado pelo AJ]

CAPÍTULO VIII — MECANISMOS DE ACOMPANHAMENTO E FISCALIZAÇÃO
8.1 Relatórios periódicos ao Administrador Judicial (trimestral/semestral)
8.2 Comitê de Credores: composição e atribuições
8.3 Cláusula de inadimplemento: efeitos e remédios

CAPÍTULO IX — DISPOSIÇÕES GERAIS
9.1 Vigência: [data de aprovação até cumprimento integral]
9.2 Foro: [vara empresarial competente]
9.3 Alterações: procedimento para modificação do plano
```

---

## 5. REGRAS CRÍTICAS DE REDAÇÃO

**Sobre o art. 54 (trabalhistas):**
- Créditos trabalhistas individuais acima de 150 SM: o excedente é tratado como quirografário
- Prazo máximo de 1 ano para pagamento dos créditos trabalhistas (com autorização judicial de prorrogação em casos específicos — L14.112)
- Nunca oferecer carência superior a 30 dias para trabalhistas sem justificativa robusta

**Sobre cram down (art. 58, §1º — L14.112/2020):**
- Requisito: aprovação por ao menos 1 das 4 classes
- Limite: haircut máximo de 70% (nos termos do §3º — [VERIFICAR texto exato])
- Não caber cram down se a única classe que aprova for a de ME/EPP (§2º — [VERIFICAR])

**Sobre deságio / haircut:**
- Deve ser fundamentado no laudo de viabilidade (cenário pessimista)
- Deságios desproporcionais serão impugnados — documentar premissas

---

## 6. VEDAÇÕES (PA aplicáveis)

- **PA-05**: Nunca protocolar plano sem laudo de viabilidade
- **PA-06**: Verificar prazo de 60 dias a partir do deferimento
- **PA-07**: Nunca misturar classes em cláusula única
- **PA-08**: Nunca ignorar o limite de 150 SM para trabalhistas
- **PA-19**: Verificar regras de votação da L14.112/2020
- **PA-20**: Avaliar cram down antes de concluir que aprovação é necessária por todas as classes
- **PA-24**: Revisar com revisao-final-rj antes de protocolar
