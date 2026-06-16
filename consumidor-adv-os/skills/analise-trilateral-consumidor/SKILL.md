---
name: analise-trilateral-consumidor
description: >
  ANALISE TRILATERAL CONSUMIDOR — Skill Tier 1. Antes de definir a linha estrategica, analisa o caso
  por tres prismas obrigatorios: Cliente (o que sustenta a tese — flipa conforme o polo), Adversario
  (a melhor defesa ou ataque da parte contraria) e Juiz (como o caso aparece para quem decide). Gera
  a matriz pontos fortes x fragilidades x contra-teses e pre-carrega o arsenal adversarial consumerista
  (Sumula 385, taxa media BACEN, engano justificavel do art. 42, decadencia art. 26, ausencia de
  relacao de consumo, excludentes do fornecedor, inexistencia de defeito). Acione apos a triagem e
  antes da linha estrategica; quando o usuario pedir analise de forcas e fraquezas, simular a defesa
  adversa, antecipacao adversarial, pontos fracos do caso, riscos da tese, ou como o juiz vera a causa.
metadata:
  version: "0.1.0"
  area: "Direito do Consumidor e Bancario"
  tier: 1
---

# ANALISE TRILATERAL CONSUMIDOR

> Skill **Tier 1**. Olha o caso por **tres olhos** antes de qualquer estrategia: o do **Cliente**, o do **Adversario** e o do **Juiz**. Entrega a matriz forcas x fragilidades x contra-teses. **Side-aware:** o prisma Cliente flipa conforme o polo lido no `CASO.md` (PA-05).

---

## 0. QUANDO ACIONAR

Apos a `triagem-consumidor` e antes da `linha-estrategica-consumidor`. Sempre que o advogado pedir analise de forcas/fraquezas, simulacao da defesa adversa, antecipacao adversarial, riscos da tese ou prognostico. Pressupoe o **Selo P1** emitido e os documentos lidos (Protocolo P2). Sem polo definido no `CASO.md`, **pare e pergunte** (PA-05).

## 1. PRE-CHECK

1. Ler o `CASO.md` em `consumidor/casos/<slug>/` — **polo**, eixo, esfera, rito, partes, documentos.
2. Confirmar Selo P1 emitido e insumos (P2) lidos. Faltando documento essencial, sinalizar `[INFORMAR]` (PA-15) e seguir marcando a lacuna — nunca inventar fato (PA-03).

---

## 2. OS TRES PRISMAS

### Prisma 1 — CLIENTE (flipa pelo polo)
O que **sustenta** a tese do cliente. Identifique fato-nexo-direito e os melhores fundamentos.

- **Polo consumidor:** vulnerabilidade (art. 4, I), inversao do onus (art. 6, VIII), responsabilidade objetiva do fornecedor (art. 12/14), dano moral in re ipsa na negativacao indevida, abusividade de clausula (art. 51), repeticao em dobro (art. 42 § un.).
- **Polo fornecedor:** regularidade da contratacao e da cobranca, exercicio regular de direito, ausencia de defeito, excludentes do art. 12 §3 / 14 §3, decadencia/prescricao, Sumula 385, taxa media BACEN dentro do mercado.

### Prisma 2 — ADVERSARIO (o melhor ataque/defesa da parte contraria)
Monte a **melhor peca do outro lado**. Use o arsenal da secao 3. Para cada fragilidade do cliente, antecipe a contra-tese e ja prepare a resposta. Este e o exercicio de *baloney detection* da Camada 3: ataque a propria tese como faria o adversario.

### Prisma 3 — JUIZ (como o caso aparece para quem decide)
Como o juiz do **JEC ou da vara comum** le a causa: o que convence, o que cansa, o que gera desconfianca. Pondere o onus probatorio efetivo, a praxe local, a tendencia do tribunal (a confirmar na `jurisprudencia-consumidor`), a proporcionalidade do dano moral pedido e a credibilidade documental. Evite excesso de pedido e dano moral inflado — sinaliza fragilidade ao julgador.

---

## 3. ARSENAL ADVERSARIAL CONSUMERISTA (pre-carregado)

Catalogo das defesas/ataques tipicos da parte contraria. Pelo polo **consumidor**, sao os riscos a neutralizar; pelo polo **fornecedor**, sao as teses a deduzir.

| # | Tese adversa | Base | Como neutraliza (lado consumidor) |
|---|--------------|------|------------------------------------|
| A | **Sumula 385 STJ** — negativacao preexistente legitima afasta dano moral | Sum. 385 | Provar que a inscricao anterior tambem e indevida/discutida (PA-07) |
| B | **Taxa media BACEN** — juros nao abusivos por estarem na media de mercado | Sum. 530/382 | So alegar abuso com desvio relevante da media; nao por mero comparativo (PA-08) |
| C | **Engano justificavel** — afasta a repeticao em DOBRO do art. 42 | art. 42 § un. + Tema 929 STJ | Demonstrar ma-fe ou culpa do fornecedor; dobro exige engano injustificavel (PA-06) |
| D | **Decadencia do vicio** — 30/90 dias ja escoados | art. 26 | Provar obstativo da decadencia (reclamacao comprovada) ou tratar como fato (art. 27) (PA-10) |
| E | **Prescricao do fato** — 5 anos do conhecimento do dano | art. 27 | Aferir o termo inicial; ciencia do dano e da autoria |
| F | **Ausencia de relacao de consumo** — finalista, insumo da cadeia | art. 2/3 (PA-04) | Provar destinatario final + vulnerabilidade (finalista mitigada) |
| G | **Excludentes do fornecedor** — culpa exclusiva do consumidor/terceiro, fortuito | art. 12 §3 / 14 §3 | Afastar excludente; fortuito interno nao exonera |
| H | **Inexistencia de defeito** — produto/servico adequado | art. 12/14 | Prova pericial / verossimilhanca + inversao do onus (art. 6, VIII) |
| I | **Capitalizacao/clausula valida** — previsao contratual expressa | Sum. 539/541 | Conferir pactuacao expressa; sem ela, afastar (PA-09) |

> Pelo polo **fornecedor**, esta tabela e o roteiro de defesa: eleger as teses cabiveis e ordena-las (preliminares → prejudiciais → merito), sempre dentro das PA (sem ataque pessoal — PA-17).

---

## 4. MATRIZ DE SAIDA

Entregue uma matriz consolidada:

```
MATRIZ TRILATERAL — <cliente> (polo: <consumidor|fornecedor>)

PONTOS FORTES (prisma Cliente)
- F1 ...  (fato/prova/fundamento)
- F2 ...

FRAGILIDADES (prisma Adversario)
- V1 ...  → contra-tese provavel: ...  → resposta: ...
- V2 ...  → contra-tese provavel: ...  → resposta: ...

VISAO DO JUIZ (prisma Juiz)
- Como tende a ler a causa; o que convence; riscos de excesso/credibilidade.

CONTRA-TESES A ANTECIPAR NA PECA
- [arsenal A..I aplicaveis] — ja com a refutacao embutida.

LACUNAS [INFORMAR]
- documentos/dados ausentes que mudam a forca da tese (PA-15).
```

---

## 5. CHECKPOINT

Apresente a matriz ao advogado para validacao. Confirmado, encaminhe para a `linha-estrategica-consumidor`, que consolida trilateral + jurisprudencia e define a linha mais benefica ao polo. Nao avance para producao sem este passo (pipeline Camada 4 — CHECKPOINT 3).

---

## 6. ENCERRAMENTO

A trilateral entrega: os tres prismas analisados, a matriz forcas x fragilidades x contra-teses e o arsenal adversarial mapeado e ja refutado. Atualize o `CASO.md` (linha de trabalho) via `memoria-de-caso-consumidor`. Tudo coerente com o polo do cliente (PA-05); nenhuma alucinacao fatica ou jurisprudencial (PA-01/PA-03).
