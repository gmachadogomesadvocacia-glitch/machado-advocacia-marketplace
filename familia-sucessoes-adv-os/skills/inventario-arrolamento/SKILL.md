---
name: inventario-arrolamento
description: >
  INVENTARIO-ARROLAMENTO — Tier 2 (Produção). Conduz o processo de inventário judicial e
  extrajudicial, arrolamento comum e arrolamento sumário em casos de família e sucessões.
  Cobre: abertura do inventário judicial (CPC arts. 610-673), inventário extrajudicial
  (Res. 35/2007 CNJ), arrolamento comum (art. 664 CPC), arrolamento sumário (art. 659 CPC),
  primeiras declarações, partilha, pagamento de ITCMD/{{UF}}, colação, sonegados e sobrepartilha.
  Acionar sempre que houver falecimento e necessidade de transmitir o patrimônio aos herdeiros.
metadata:
  version: "1.0.0"
---

# INVENTARIO-ARROLAMENTO
> Tier 2 | Produção | Inventário Judicial / Extrajudicial / Arrolamento

> **CHASSI DE PEÇA**: para abertura de inventário judicial, abrir o modelo-base
> `templates/pecas/inventario.md` (CPC 610+; abertura em 2 meses — art. 611;
> primeiras declarações; meação e quinhões; ITCMD; via extrajudicial se todos
> capazes e concordes — art. 610, §1º). Ver `templates/pecas/_LEIA-ME.md`.

---

## 0. FLUXO DECISÓRIO INICIAL

```
FALECIMENTO
    ↓
Há testamento? → SIM → Inventário Judicial (art. 610 §1º CPC)
    ↓ NÃO
Há herdeiro menor/incapaz? → SIM → Inventário Judicial obrigatório
    ↓ NÃO
Há litígio entre herdeiros? → SIM → Inventário Judicial
    ↓ NÃO
Todos os herdeiros são capazes e concordes?
    ↓ SIM
Valor total do espólio ≤ 2.000 salários mínimos? → SIM → Arrolamento Sumário (art. 659 CPC)
    ↓ NÃO (ou qualquer credor)
Inventário Extrajudicial (Res. 35/2007 CNJ) — todos com advogado
    OU
Inventário Judicial com procedimento comum (arts. 610-658 CPC)
```

---

## 1. PRAZO FATAL — PA-08

```
⚠️ PRAZO: 60 dias da ciência do óbito para abertura do inventário
   (art. 611 CPC) — caso contrário, multa na transmissão do ITCMD
   → No {{UF}}: multa de 20% sobre o ITCMD após o prazo

Se o prazo estiver vencendo ou vencido:
→ Requerer abertura imediatamente + justificativa de atraso
→ No extrajudicial: verificar acréscimo de ITCMD com SEFAZ/{{UF}}
```

---

## 2. INVENTÁRIO JUDICIAL

### 2.1 Petição de Abertura (art. 615 CPC)

**Conteúdo obrigatório**:
- Qualificação completa do falecido (nome, CPF, data e local do óbito)
- Qualificação de todos os herdeiros e do cônjuge/companheiro
- Regime de bens do casamento/união
- Relação de bens estimada (primeiras declarações completas virão depois)
- Nomeação do inventariante proposto (com justificativa na ordem do art. 617 CPC)

**Ordem de preferência do inventariante (art. 617 CPC)**:
1. Cônjuge/companheiro sobrevivente (se conviviam ao tempo do óbito)
2. Herdeiro que estava na posse e administração dos bens
3. Qualquer herdeiro
4. Testamenteiro (se nomeado)
5. Credor do espólio
6. Administrador judicial (se nenhum dos anteriores aceitar)

### 2.2 Primeiras Declarações (art. 620 CPC)

Documento central do inventário — inventariante presta sob juramento:
```
I — Identificação do falecido
II — Relação dos herdeiros (com qualificação e grau de parentesco)
III — Regime de bens e data do casamento/união
IV — Relação de bens (imóveis, veículos, investimentos, empresas, créditos)
V — Relação de dívidas do espólio (PA-07: incluir passivos!)
VI — Colação de bens doados em vida (art. 2.002 CC — filhos que receberam doações)
```

### 2.3 Avaliação e ITCMD

1. Nomeação de avaliador judicial ou concordância com valores declarados
2. Cálculo do ITCMD: 4% sobre valor de mercado (PA-13)
3. Pagamento das guias (SEFAZ/{{UF}}) antes da partilha
4. Quitação de dívidas do espólio (art. 643 CPC — pagamentos autorizados pelo juízo)

### 2.4 Esboço de Partilha (art. 647 CPC)

Apresentado pelo inventariante após quitação de dívidas e ITCMD:
- Identifica o monte-mor líquido
- Atribui bens a cada herdeiro (e ao meeiro)
- Compensações em dinheiro (tornas) se não houver divisão exata

### 2.5 Formal de Partilha (art. 655 CPC)

Documento final homologado pelo juiz — título hábil para registro nos cartórios.
Contém: auto de orçamento, partilha com quinhões individualizados, termo de quitação.

---

## 3. INVENTÁRIO EXTRAJUDICIAL (Res. 35/2007 CNJ)

**Requisitos** (PA-09):
- Todos os herdeiros maiores e capazes
- Consenso unânime
- Ausência de testamento (ou testamento caducado/revogado — verificar)
- Todos com advogado (pode ser o mesmo, se não houver conflito)
- Sem herdeiro ausente / incerto

**Procedimento**:
1. Escolha do tabelionato (qualquer comarca — livre escolha)
2. Apresentação dos documentos (certidões, matrículas, extratos, IR)
3. Pagamento do ITCMD antes da escritura
4. Lavratura da escritura pública de inventário e partilha
5. Registro nos cartórios competentes (CRI, DETRAN, B3, etc.)

**Documentos para o tabelionato**:
- Certidão de óbito
- RG/CPF/certidão de casamento do falecido
- RG/CPF/certidão civil de todos os herdeiros
- Certidão de matrícula dos imóveis (atualizada)
- CRLV dos veículos
- Extratos de investimentos e contas
- Declaração de IR (últimos 2 anos)
- CND federal, estadual e municipal (quando exigida)
- Guia quitada do ITCMD

**Custas** (tabelionato de {{CIDADE}}):
- Tabela do TJ{{UF}} (Lei de Custas do {{UF}}) — calculada sobre o valor do espólio
- Em geral: mais barato e rápido que o judicial

---

## 4. ARROLAMENTO SUMÁRIO (art. 659 CPC)

**Quando usar**: todos os herdeiros capazes + consenso + sem credor habilitado

**Diferencial**: dispensa avaliação judicial — os próprios herdeiros fixam os valores
dos bens (sujeito a revisão pelo fisco para fins de ITCMD)

**Prazo**: muito mais curto que o inventário comum

**Fluxo**:
1. Petição com qualificação das partes + relação de bens + esboço de partilha
2. Recolhimento do ITCMD
3. Homologação da partilha pelo juiz (sem outras provas formais)
4. Formal de Partilha

---

## 5. ARROLAMENTO COMUM (art. 664 CPC)

**Quando usar**: monte-mor até 1.000 salários mínimos (verificar Lei)
**Diferencial do sumário**: pode haver credor habilitado; requer avaliação

---

## 6. COLAÇÃO E SONEGADOS

**Colação (art. 2.002 CC)**:
- Filhos que receberam doações em vida do falecido devem trazer à colação esses bens
  (para igualar os quinhões) — salvo se o falecido dispensou expressamente
- Prazo: nas primeiras declarações

**Sonegados (art. 1.992 CC)**:
- Inventariante que omite bens do espólio perde o direito ao quinhão do bem sonegado
- Qualquer herdeiro pode arguir sonegação a qualquer tempo durante o inventário
- Peça: "Petição de Arguição de Sonegados" — ver contestacao-familia se o cliente é
  o herdeiro prejudicado

---

## 7. CHECKLIST PARA ENCERRAMENTO DO INVENTÁRIO

```
□ ITCMD pago (4% sobre valor de mercado)?
□ Dívidas do espólio quitadas?
□ Colação conferida?
□ Formal de Partilha / Escritura Pública assinados?
□ Imóveis registrados no CRI da comarca?
□ Veículos transferidos no DETRAN?
□ Contas bancárias/investimentos transferidos?
□ Participações societárias alteradas no contrato social / Junta Comercial do {{UF}}?
□ Benefícios do INSS (pensão por morte) requeridos?
□ Cancelamento do CPF do falecido (opcional — Receita Federal)?
```
