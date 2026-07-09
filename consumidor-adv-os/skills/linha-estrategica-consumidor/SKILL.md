---
name: linha-estrategica-consumidor
description: >
  LINHA ESTRATEGICA CONSUMIDOR — Skill Tier 1. Acione apos a trilateral, quando o usuario pedir a estrategia do caso, a melhor tese, qual via seguir, JEC ou vara comum, se cabe liminar, qual o caminho mais vantajoso, ou a linha de acao/defesa.
metadata:
  version: "0.1.0"
  area: "Direito do Consumidor e Bancario"
  tier: 1
---

# LINHA ESTRATEGICA CONSUMIDOR

> Skill **Tier 1**. Funde a **trilateral** com a **jurisprudencia** e define a linha mais benefica ao **polo do cliente**: tese central, subsidiarias, riscos, **via**, **rito** e **tutela de urgencia**. Saida que o advogado valida no **CHECKPOINT 4** antes da producao. **Side-aware** (PA-05).

---

## 0. QUANDO ACIONAR

Apos `analise-trilateral-consumidor` e `jurisprudencia-consumidor`. Sempre que o usuario pedir a estrategia, a melhor tese, a via a seguir, JEC x vara comum, se cabe liminar, ou o caminho mais vantajoso. Pressupoe **Selo P1** (P1) e insumos (P2). Sem polo no `CASO.md`, **pare e pergunte** (PA-05).

## 1. PRE-CHECK

1. Ler o `CASO.md` — polo, eixo, esfera, rito, partes, foro, prazos.
2. Recolher a **matriz trilateral** (forcas/fragilidades/contra-teses) e a **jurisprudencia classificada** (PA-01 — nada sem validacao).
3. Ler o modo `{{MODO_MELHOR_SAIDA}}` do `cowork-state.json`.

---

## 2. CONSOLIDACAO

Cruze os tres prismas com os precedentes validados e destile a **tese mais defensavel** para o polo do cliente. Amarre **FATO-NEXO-DIREITO** (FIRAC, Camada 3). Para cada fragilidade da matriz, ja embuta a refutacao da contra-tese (antecipacao adversarial). Confirme que nenhuma tese contraria o polo (PA-05) e que cada fundamento legal/sumular existe (PA-01/PA-02).

---

## 3. A LINHA ESTRATEGICA

### 3.1 Tese central + subsidiarias
- **Tese central:** a de maior forca e menor risco para o polo.
- **Teses subsidiarias:** pedidos alternativos/cumulados (ex.: nulidade de clausula → revisao → repeticao; ou declaratoria → dano moral → tutela).
- **Riscos:** o que pode derrubar a tese (Sumula 385, taxa media BACEN, engano justificavel do art. 42, decadencia art. 26, excludentes art. 12 §3/14 §3) e o plano de mitigacao.

### 3.2 VIA (Protocolo P4 — Cruzamento Judicial-Administrativo)
- **Judicial** — quando ha urgencia, dano moral relevante, necessidade de titulo executivo ou prova pericial.
- **Administrativa** — PROCON / consumidor.gov.br / BACEN / ANATEL / ANAC: rapida, sem custo, gera prova documental da resistencia do fornecedor.
- **Ambas em paralelo** — comum e potente: a reclamacao administrativa instrui a acao. **Nunca produza teses contraditorias entre as frentes** (P4). Registre a coordenacao no `CASO.md`.

### 3.3 RITO (Protocolo P5 — Localizacao e Rito)
- **JEC** (Lei 9.099) — ate 40 SM; ate 20 SM dispensa advogado; rito rapido, conciliacao previa (PA-19).
- **Vara civel comum** — acima de 40 SM, prova pericial complexa, ou estrategia (sem teto, ampla instrucao).
- **Acao coletiva** — interesse coletivo/difuso (legitimados do art. 82 CDC).
- **Competencia:** foro do domicilio do consumidor (art. 101, I CDC).

### 3.4 Tutela de urgencia
Avaliar cabimento (art. 300 CPC): probabilidade do direito + perigo de dano. Tipicos no consumidor: remocao de negativacao, restabelecimento de servico essencial cortado, suspensao de cobranca/desconto, abstencao de busca e apreensao. Se cabivel, encaminhar a `tutela-urgencia-consumidor`.

---

## 4. MODO DE MELHOR SAIDA

Respeite `{{MODO_MELHOR_SAIDA}}`:

- **`recomendar-e-listar`** — apresentar as opcoes E **recomendar** a linha otima, justificando.
- **`apenas-listar`** — apresentar as opcoes viaveis (via, rito, teses) **sem** recomendar; a escolha e do advogado.

Em ambos os modos, jamais prometa resultado (PA-20) nem omita o risco relevante.

---

## 5. SAIDA E CHECKPOINT

```
LINHA ESTRATEGICA — <cliente> (polo: <...>)
- Tese central: ...
- Teses subsidiarias: ...
- Riscos + mitigacao: ...
- VIA: [judicial | administrativa | paralela] (P4)
- RITO: [JEC | vara comum | coletiva] — foro: <art.101,I> (P5)
- Tutela de urgencia: [sim/nao] — fundamento art. 300 CPC
- Tarefa Tier 2 sugerida: <skill de producao conforme eixo/polo>
- Pendencias [INFORMAR]: ...
```

Apresente ao advogado (**CHECKPOINT 4**). Validada a linha, roteie para a skill Tier 2 conforme eixo e polo (peticao-inicial / contestacao / revisional-bancaria / acao-negativacao / acao-vicio-fato / reclamacao-administrativa, etc.). Atualize `CASO.md` e `MEMORY.md` (linha estrategica adotada) via `memoria-de-caso-consumidor`.

---

## 6. ENCERRAMENTO

Entrega a linha mais benefica ao polo: tese central, subsidiarias, riscos, via (P4), rito (P5) e tutela. Toda peca subsequente passa pela `revisao-final-consumidor` (R1-R4) antes da entrega (PA-22). Coerencia de polo absoluta (PA-05).
