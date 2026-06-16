---
name: reclamacao-administrativa
description: >
  RECLAMACAO ADMINISTRATIVA — Skill Tier 2, esfera administrativa, side-aware. Redige a reclamacao
  nos orgaos de protecao e agencias reguladoras: PROCON, consumidor.gov.br, BACEN (registro de
  demanda bancaria), ANATEL (telecom), ANAC (aereo) e demais agencias. Cobre a estrutura da
  reclamacao, pedido claro, documentos, prazos de resposta do fornecedor/orgao, e o uso da reclamacao
  e do silencio/recusa como prova pre-constituida na futura acao. Opera o Protocolo P4 (Cruzamento
  Judicial-Administrativo). Acione quando o usuario pede reclamacao no PROCON, consumidor.gov.br,
  abrir demanda no BACEN, reclamar na ANATEL/ANAC, via administrativa, notificar a agencia reguladora.
  Exige Selo P1 emitido.
metadata:
  version: "0.1.0"
  area: "Direito do Consumidor e Bancario"
  tier: 2
---

# RECLAMACAO ADMINISTRATIVA

> Skill **Tier 2** — esfera administrativa. Produz a reclamacao no orgao/agencia certo e a coordena com a frente judicial pelo **Protocolo P4**. **Side-aware:** normalmente pelo consumidor; pelo fornecedor, estrutura a **resposta** a reclamacao. So roda apos a triagem e o Selo P1.

---

## 0. PRE-REQUISITOS

- Polo do cliente travado (PA-05). **Selo de Validacao Legal Previa EMITIDO** (P1).
- CASO.md com partes, eixo, esfera (administrativa, eventualmente em paralelo a judicial) e documentos. Falta de doc essencial → `[INFORMAR]` (PA-15).

## 1. ESCOLHA DO ORGAO / AGENCIA

| Eixo / tema | Orgao ou agencia |
|-------------|------------------|
| Geral de consumo | **PROCON** (estadual/municipal); **consumidor.gov.br** (plataforma oficial, resposta direta do fornecedor) |
| Bancario / financeiro / cartao | **BACEN** — *registro de demanda* (RDR); reclamacao contra instituicao financeira |
| Telecom / internet / TV | **ANATEL** |
| Transporte aereo / voo / bagagem | **ANAC** |
| Energia, agua, saude suplementar, etc. | Agencia reguladora setorial (ANEEL, ANS via plugin medico, etc.) |

> **Plano de saude** (negativa de cobertura, OPME, home care, TEA, reajuste): **encaminhar ao plugin de direito medico** — esta skill so roteia.

## 2. NATUREZA E LIMITES DE CADA VIA

- **PROCON:** pode instaurar processo administrativo, aplicar sancao ao fornecedor e mediar; a CIP (Carta de Informacoes Preliminares) abre prazo de resposta.
- **consumidor.gov.br:** mediacao direta monitorada pela Senacon; **nao** aplica sancao, mas registra a resposta/recusa oficialmente.
- **BACEN:** o *registro de demanda* nao resolve o caso individual nem condena ao pagamento — gera indicador regulatorio e pressao; util como prova de que o consumidor procurou a via.
- **ANATEL/ANAC:** abrem protocolo, fixam prazo de resposta da prestadora e podem fiscalizar/multar.

## 3. ESTRUTURA DA RECLAMACAO

1. **Identificacao** — consumidor e fornecedor (CNPJ), contrato/numero de cliente.
2. **Relato dos fatos** — objetivo, cronologico, com **protocolos de atendimento** anteriores; cada documento como **"doc. N"**.
3. **Fundamento** — dispositivo do CDC e da norma setorial (resolucoes ANATEL/ANAC, normas BACEN) — validados via `validador-legislacao-consumidor`.
4. **Pedido claro e determinado** — exatamente o que se quer do fornecedor (estorno, religar, cancelar cobranca, reembolso, baixa de negativacao), com valor quando houver.
5. **Documentos** — contrato, faturas, extratos, prints, protocolos, negativacao.
6. **Prazo** — requerer resposta no prazo do orgao/plataforma.

## 4. PRAZOS DE RESPOSTA

- **consumidor.gov.br:** o fornecedor responde em ate ~10 dias (prazo da plataforma).
- **PROCON:** prazo fixado na CIP/notificacao (varia por unidade).
- **BACEN / ANATEL / ANAC:** prazo regulamentar do orgao para manifestacao da instituicao/prestadora.

> Validar os prazos vigentes com `validador-legislacao-consumidor` (PA-11) — variam por resolucao e por unidade.

## 5. RECLAMACAO COMO PROVA PRE-CONSTITUIDA

- O **protocolo, a resposta, a recusa ou o silencio** do fornecedor tornam-se **prova pre-constituida** na futura acao: demonstram a tentativa de solucao, o esgotamento da via amigavel e — no silencio/recusa — reforcam dano moral e ma-fe.
- Anexar a reclamacao e a resposta (ou a certidao de silencio) a peticao inicial como "doc. N".

## 6. PROTOCOLO P4 — CRUZAMENTO JUDICIAL-ADMINISTRATIVO

- A **tese administrativa NAO pode contradizer a tese judicial** (PA-05 por extensao). Coordenar as duas frentes: mesmos fatos, mesmo pedido essencial, mesma narrativa.
- Quando houver acao em paralelo, a reclamacao administrativa **alimenta a prova** e nao cria fato/admissao que enfraqueca a acao.
- Registrar no CASO.md as duas frentes e seus protocolos (Protocolo P3 / `memoria-de-caso-consumidor`).

## 7. CHECKLIST ANTES DE ENTREGAR

- [ ] Orgao/agencia correto para o eixo · plano de saude roteado ao plugin medico
- [ ] Polo coerente (PA-05) · Selo P1 citado · pedido claro e determinado
- [ ] **P4:** tese administrativa nao contradiz a judicial · frentes coordenadas no CASO.md
- [ ] Norma setorial e Sumula/Tema como `[VERIFICAR]` + `jurisprudencia-consumidor` (PA-01)
- [ ] Prazos do orgao conferidos (PA-11) · docs numerados "doc. N"
- [ ] Submeter a `revisao-final-consumidor` (R1-R4) antes da entrega (PA-22)

## 8. ENCERRAMENTO

Entrega a reclamacao no orgao certo, com pedido claro e documentos numerados, coordenada com a frente judicial pelo Protocolo P4 e pronta para servir de prova pre-constituida, apos a Suprema Corte R1-R4.
