---
name: acao-vicio-fato-produto
description: >
  ACAO VICIO/FATO DO PRODUTO OU SERVICO — Skill Tier 2 (lado consumidor). Acione quando o consumidor reclama de produto/servico com defeito, garantia, troca, conserto, devolucao do dinheiro, recall, ou dano causado por produto defeituoso. Exige Selo P1.
metadata:
  version: "0.1.0"
  area: "Direito do Consumidor e Bancario"
  tier: 2
---

# ACAO VICIO / FATO DO PRODUTO OU SERVICO

> Skill **Tier 2** — lado consumidor, eixo produto/servico. Especializa a `peticao-inicial-consumidor`. So roda apos triagem, Selo P1 e linha estrategica.

---

## 0. PRE-REQUISITOS

- Polo do cliente = **consumidor** (PA-05). Se fornecedor → `contestacao-consumidor`.
- **Selo P1 EMITIDO** (`validador-legislacao-consumidor`). Sem ele, nao redigir.
- CASO.md com produto/servico, data da compra, data da ciencia do vicio, nota fiscal, garantia e protocolos de atendimento. Falta de doc essencial → `[INFORMAR]` (PA-15).

## 1. A DISTINCAO-MAE: VICIO x FATO (PA-10)

Primeiro passo obrigatorio. Errar aqui muda artigo, saida e PRAZO.

| | **VICIO** (art. 18 a 20) | **FATO / DEFEITO** (art. 12 a 14) |
|---|---|---|
| O que e | Produto/servico **improprio, inadequado ou de valor diminuido** | **Acidente de consumo** — defeito que causa dano alem do produto |
| Atinge | O proprio produto/servico | A incolumidade do consumidor (saude, seguranca, patrimonio) |
| Norma | art. 18 (produto) / art. 20 (servico) | art. 12 (produto) / art. 14 (servico) |
| Prazo | **Decadencia** art. 26: **30 dias** nao duravel · **90 dias** duravel | **Prescricao** art. 27: **5 anos** da ciencia do dano e da autoria |

**Regra de ouro:** se o problema fica contido no produto → vicio. Se o produto causou dano a algo ou alguem → fato. Nao confundir os prazos (PA-11).

## 2. VICIO — SAIDAS E RESPONSABILIDADE

- **Prazo de saneamento:** 30 dias para o fornecedor sanar (art. 18, §1; art. 20 para servico). Nao sanado, o consumidor escolhe:
  1. **substituicao** do produto / reexecucao do servico;
  2. **restituicao** imediata da quantia paga, corrigida;
  3. **abatimento** proporcional do preco.
- Vicio de **quantidade** → art. 19. Vicio de **servico** → art. 20.
- **Solidariedade no vicio (art. 18):** toda a cadeia (fabricante, distribuidor, comerciante) responde solidariamente — diferente do fato.

## 3. FATO DO PRODUTO/SERVICO — RESPONSABILIDADE

- **Fabricante/produtor/importador:** responsabilidade **objetiva** (art. 12) — independe de culpa.
- **Comerciante:** responde **subsidiariamente** (art. 13) — so quando o fabricante nao for identificado, o produto for sem identificacao, ou nao conservar adequadamente os perecíveis.
- **Prestador de servico:** responsabilidade objetiva (art. 14); **profissional liberal** so com culpa (art. 14, §4).
- **Excludentes (art. 12, §3 / art. 14, §3):** nao colocou o produto no mercado; defeito inexistente; culpa exclusiva do consumidor ou de terceiro. Antecipar e neutralizar.

## 4. GARANTIA, VICIO OCULTO E RECALL

- **Garantia legal** (art. 24): inafastavel, independe de termo. **Garantia contratual** (art. 50): complementar, soma-se a legal — contar a partir dela.
- **Vicio oculto (art. 26, §3):** o prazo decadencial conta da **ciencia do vicio**, nao da compra. Fundamentar a data da ciencia (PA-11).
- **Recall:** dever de informar e reparar (art. 10, §1); descumprimento reforca o dano e pode caracterizar fato do produto.

## 5. ESTRUTURA (delega a `peticao-inicial-consumidor`)

Enderecamento → qualificacao → **Dos Fatos** (cronologia: compra, surgimento do vicio/dano, atendimento sem solucao; docs "doc. N") → **Do Direito** (FIRAC: relacao de consumo art. 2/3; vicio art. 18/20 OU fato art. 12/14; solidariedade ou subsidiariedade; **inversao do onus** art. 6 VIII, PA-12; antecipacao adversarial das excludentes e do prazo) → **Tutela** se houver → **Pedidos** (escolha do art. 18 §1 / reparacao do fato; **dano moral quantificado**; obrigacao de fazer; juros e correcao) → valor da causa → requerimentos.

Sumula/Tema (ex.: vicio oculto, contagem de prazo) sempre `[VERIFICAR]` via `jurisprudencia-consumidor` (PA-01).

## 6. CHECKLIST

- [ ] Vicio x fato corretamente classificado (PA-10) · prazo certo (decadencia art. 26 / prescricao art. 27, PA-11)
- [ ] Responsabilidade alocada (objetiva art. 12 / subsidiaria art. 13 / solidaria art. 18)
- [ ] Vicio oculto: data da ciencia fundamentada · garantia legal+contratual somadas
- [ ] Inversao do onus fundamentada (PA-12) · dano moral quantificado · pedidos determinados
- [ ] Sumula/Tema com `[VERIFICAR]` (PA-01) · docs "doc. N"
- [ ] Submeter a `revisao-final-consumidor` (R1-R4) antes da entrega (PA-22)

## 7. ENCERRAMENTO

Entrega a acao do eixo produto/servico com a distincao vicio/fato cravada, prazo correto, responsabilidade bem alocada e dano moral quantificado, pronta para a Suprema Corte R1-R4.
