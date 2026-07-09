---
name: estilo-juridico-transito
description: >
  Estilo juridico de transito Camada 3 (Tier 1). Ative ao redigir ou revisar a forma de qualquer peca de transito.
metadata:
  version: "0.1.0"
  area: "Direito de Transito"
  tier: 1
---

# ESTILO JURIDICO DE TRANSITO (Camada 3)

> Tier 1 — Camada 3. Padroniza a **forma** de toda peca de transito. Estilo **objetivo e tecnico**, teses **ordenadas** (preliminares de nulidade antes do merito), linguagem de transito **precisa**. Tom **{{TOM_VOZ_PERFIL}}**, intensidade **{{TOM_VOZ_INTENSIDADE}}/10** — combatividade dirigida a teses, nunca a pessoas.

---

## 1. PRINCIPIOS

- **Objetividade**: frases curtas, uma ideia por paragrafo; sem retorica vazia.
- **Ordenacao**: preliminares/nulidades formais primeiro; merito (inexistencia do fato) depois.
- **Ancoragem**: cada afirmacao remete a um documento ("conforme doc. N") e a um fundamento (CTB/sumula validada).
- **Sobriedade combativa**: firmeza tecnica, sem ataques pessoais ao agente/orgao.

## 2. ESTRUTURA PADRAO DA PECA

```
1. ENDERECAMENTO
   - administrativo: a autoridade/orgao (DETRAN/municipal/DER/PRF), JARI ou CETRAN.
   - judicial: ao Juizo da Vara da Fazenda Publica / Juizado da Fazenda.

2. IDENTIFICACAO
   - do recorrente/impetrante (condutor/proprietario) e do auto (AIT, codigo, data/local, orgao).

3. DAS PRELIMINARES / NULIDADES
   - vicios formais do auto (CTB 280), ausencia/intempestividade da dupla notificacao (NA + NP — Sum. 312),
     cerceamento de defesa, equipamento sem afericao, incompetencia, decadencia.

4. DO MERITO
   - inexistencia/atipicidade do fato; erro de identificacao; insubsistencia da autuacao.

5. DOS PEDIDOS
   - arquivamento do auto; cancelamento da autuacao/penalidade; restituicao/exclusao de pontos;
     efeito suspensivo / tutela (quando cabivel); no MS, a concessao da ordem.

6. DAS PROVAS REQUERIDAS
   - certidao de afericao (INMETRO), imagens/registro do equipamento, comprovantes de notificacao (AR),
     sinalizacao, vista do processo.

7. FECHO
   - data, advogado, OAB; documentos numerados.
```

## 3. LINGUAGEM DE TRANSITO (usar correto — PA-08)

| Nao confundir | Distincao |
|---------------|-----------|
| **NA × NP** | Notificacao de **Autuacao** (abre defesa previa) × Notificacao de **Penalidade** (abre recurso) |
| **autuacao × penalidade** | lavratura do auto × aplicacao da multa/pontos |
| **suspensao × cassacao** | suspensao temporaria do direito de dirigir × cassacao da CNH |
| **defesa previa × recurso** | fase da autuacao × JARI/CETRAN |
| **JARI × CETRAN** | 1ª × 2ª instancia administrativa |

## 4. PEDIDOS POR TIPO DE PECA

- **Defesa previa** → arquivamento do auto / nao aplicacao da penalidade.
- **Recurso JARI/CETRAN** → cancelamento da penalidade; restituicao de pontos; efeito suspensivo.
- **Anulatoria** → declaracao de nulidade do auto/penalidade; restituicao de valores e pontos.
- **Mandado de seguranca** → ordem para cessar o ato ilegal; liminar; direito liquido e certo demonstrado documentalmente.

## 5. DOCUMENTOS

- Numerar todo anexo como **"doc. N"** e cita-lo no corpo por esse numero.
- Entregar em **.txt** por padrao (.docx/.pdf so a pedido).
- Gatilho "gera docx": converter a peca .txt em .docx no papel timbrado via `gerador-peticoes` — Code.

## 6. INTEGRACAO

- Forma aplicada apos `linha-estrategica-transito` definir tese e instancia.
- Citacoes validadas por `jurisprudencia-transito` (PA-01); dados por `analise-documental-transito` (PA-03).
- `revisao-final-transito` (R1-R4) confere estilo, tom, coerencia de polo e pedidos antes da entrega.

## 7. CHECKLIST DE SAIDA

- [ ] Endereçamento correto (orgao/instancia/juizo)
- [ ] Preliminares/nulidades antes do merito
- [ ] Pedidos claros e coerentes com a peca e o polo (PA-10)
- [ ] Provas requeridas listadas (afericao, AR, imagens)
- [ ] Linguagem de transito correta (NA×NP, autuacao×penalidade, suspensao×cassacao — PA-08)
- [ ] Documentos numerados "doc. N"; tom {{TOM_VOZ_PERFIL}} / {{TOM_VOZ_INTENSIDADE}}/10
