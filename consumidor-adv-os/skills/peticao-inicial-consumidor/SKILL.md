---
name: peticao-inicial-consumidor
description: >
  PETICAO INICIAL CONSUMIDOR — Skill Tier 2 (lado consumidor/autor). Redige a peticao inicial
  consumerista completa e enxuta: enderecamento, qualificacao, dos fatos, do direito (FIRAC, com
  inversao do onus art. 6 VIII), tutela de urgencia quando cabivel, pedidos determinados (declaratorio
  + condenatorio + dano moral quantificado), valor da causa e requerimentos. E a peca-base que as
  acoes especificas de cada eixo reaproveitam. Acione quando o cliente e o consumidor e o usuario pede
  peticao inicial, acao, processar a empresa, ajuizar, reclamar judicialmente. Exige Selo P1 emitido.
metadata:
  version: "0.1.0"
  area: "Direito do Consumidor e Bancario"
  tier: 2
---

# PETICAO INICIAL CONSUMIDOR

> Skill **Tier 2** — lado consumidor. Peca-base de toda inicial consumerista. As skills `acao-*` especializam esta estrutura por eixo. So roda apos a triagem, o Selo P1 e a linha estrategica.

---

## 0. PRE-REQUISITOS

- Polo do cliente = **consumidor** (PA-05). Se fornecedor → `contestacao-consumidor`.
- **Selo de Validacao Legal Previa EMITIDO** (P1). Sem ele, nao redigir.
- CASO.md com partes, eixo, esfera, rito e documentos. Falta de doc essencial → `[INFORMAR]` (PA-15).

## 1. ESCOLHA DE RITO E FORO

- Foro: domicilio do consumidor (art. 101, I CDC).
- Rito: JEC (ate 40 SM) → `peticao-jec`; vara comum (acima de 40 SM, pericia, estrategia).
- Confirmados pela `linha-estrategica-consumidor` (Protocolo P5).

## 2. ESTRUTURA DA PECA (FIRAC + estilo do escritorio)

1. **Enderecamento** — Juizo competente (Vara Civel / Juizado).
2. **Qualificacao** — autor (consumidor) e reu (fornecedor; CNPJ).
3. **Dos Fatos** — narrativa enxuta e cronologica; cada documento citado como **"doc. N"**.
4. **Do Direito** — um bloco FIRAC por tese:
   - Relacao de consumo (art. 2/3) e vulnerabilidade.
   - **Inversao do onus** (art. 6, VIII) — fundamentar verossimilhanca ou hipossuficiencia (PA-12).
   - Tese de merito do eixo (vicio/fato, cobranca indevida, negativacao, etc.).
   - **Antecipacao adversarial** — neutralizar a melhor defesa do reu ja aqui (Sumula 385, taxa media, engano justificavel, excludentes).
5. **Da Tutela de Urgencia** (se houver) — probabilidade do direito + perigo de dano (art. 300 CPC): retirar negativacao, religar servico, suspender cobranca/desconto, impedir busca e apreensao.
6. **Dos Pedidos** — determinados:
   - declaratorio (inexistencia/nulidade de debito ou clausula — indicar inciso do art. 51, PA-13);
   - condenatorio (repeticao de indebito — simples ou **dobro** so com engano injustificavel, art. 42 + Tema 929; obrigacao de fazer);
   - **dano moral quantificado** (valor com ancoragem em precedente — nunca "a arbitrar" puro);
   - inversao do onus; gratuidade se cabivel; juros e correcao.
7. **Do Valor da Causa** — soma dos pedidos economicos + dano moral estimado.
8. **Requerimentos finais** — citacao, provas, intimacoes.

## 3. PROVA E ONUS

Indicar as provas (documental ja anexada, e eventual pericial/depoimento). Distribuir o onus: ao consumidor cabe o verossimil; ao fornecedor, o fato impeditivo/modificativo. Pleitear a inversao quando presentes os requisitos.

## 4. CHECKLIST ANTES DE ENTREGAR

- [ ] Polo coerente (PA-05) · Selo P1 citado · relacao de consumo demonstrada
- [ ] Inversao do onus fundamentada · dano moral quantificado · pedidos determinados
- [ ] Antecipacao adversarial presente · docs numerados "doc. N"
- [ ] Prazos conferidos (decadencia art. 26 / prescricao art. 27)
- [ ] Submeter a `revisao-final-consumidor` (R1-R4) antes da entrega (PA-22)

## 5. ENCERRAMENTO

Entrega a inicial enxuta, FIRAC, com tutela (se cabivel), pedidos determinados e dano moral quantificado, pronta para a Suprema Corte R1-R4.
