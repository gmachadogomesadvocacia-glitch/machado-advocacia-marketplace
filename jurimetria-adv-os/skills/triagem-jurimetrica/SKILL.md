---
name: triagem-jurimetrica
description: >
  TRIAGEM JURIMETRICA — Skill Tier 1, porta de entrada de toda demanda jurimetrica. Transforma o
  pedido em uma PERGUNTA ANALITICA precisa e classifica em 4 dimensoes: tipo de analise (caso unico x
  portfolio x benchmark x quantum x tempo x viabilidade) x fonte (acervo/DataJud/jurisprudencia) x
  recorte (area, classe/assunto CNJ, orgao, periodo) x destino (uso interno, proposta, subsidio de
  peca). Verifica o N disponivel ANTES de prometer estatistica. Acione quando chegar pedido de
  numeros, estatistica, relatorio do acervo, benchmark, ou quando a pergunta analitica ainda nao
  esta definida.
metadata:
  version: "0.1.0"
  area: "Jurimetria"
  tier: 1
---

# TRIAGEM JURIMETRICA

> Skill **Tier 1** — porta de entrada. Jurimetria boa comeca com pergunta bem posta; pergunta vaga gera numero enganoso. Nenhum motor Tier 2 roda sem passar por aqui.

---

## 0. QUANDO ACIONAR

Todo pedido jurimetrico novo; sempre que a pergunta analitica nao estiver definida; quando o usuario pede "estatisticas" genericamente. Consulta pontual de um processo (so duracao/andamentos) dispensa a triagem completa — vai direto a `consulta-datajud`.

## 1. PRE-CHECK

1. Procurar `jurimetria/cowork-state.json` (subir a arvore). Ausente → sugerir `/start-jurimetria`; se o operador declinar, seguir em modo fallback (sem CASE_ROOT, so DataJud manual).
2. Ler `jurimetria/config.md` — CASE_ROOT, tribunais, N_MINIMO.

---

## 2. A TRIAGEM 4D

### Dimensao 1 — TIPO DE ANALISE (define o motor Tier 2)

| Tipo | Pergunta-exemplo | Motor |
|------|------------------|-------|
| **Caso unico** | "quanto tempo este processo esta levando?" | `consulta-datajud` (Modulo A) |
| **Portfolio** | "qual a taxa de exito do acervo em habilitacoes?" | `coleta-acervo` (Modulo C) |
| **Benchmark** | "meus casos demoram mais que a media da vara?" | `benchmark-datajud` (Modulo B) + `coleta-acervo` |
| **Quantum** | "qual a faixa de condenacao em dano moral por negativacao?" | `analise-quantum` |
| **Tempo** | "quanto costuma demorar da sentenca ao transito?" | `tempo-processual` |
| **Viabilidade** | "vale pegar este caso? que proposta fazer?" | `viabilidade-jurimetrica` |

### Dimensao 2 — FONTE

- **Acervo proprio** (blocos nos CASO.md) — quantum, desfecho, exito. Exige P2 (instrumentacao).
- **DataJud** — duracao/andamentos/classes. So capa + movimentos (PE-07).
- **Jurisprudencia** — faixas de quantum em temas (qualitativo estruturado).
- Combinacoes sao a regra (a espinha: DataJud + CASO.md unidos pelo numero).

### Dimensao 3 — RECORTE

Area · classe CNJ · assunto CNJ · comarca/orgao · grau · periodo · status (em andamento x fechados). **Registrar o recorte por extenso** — ele e parte do carimbo PE-01 e da harmonizacao PE-09.

### Dimensao 4 — DESTINO

- **Uso interno** (gestao do escritorio) — formato livre, freios integrais.
- **Proposta/cliente** — freios integrais + linguagem sem promessa (PE-03) + scanner de sigilo (P5).
- **Subsidio de peca** (outro plugin) — numero viaja com carimbo completo (PE-13).

---

## 3. CHECAGEM DE N (antes de prometer)

Antes do CHECKPOINT, estimar o N disponivel no recorte:

- Portfolio: rodar `coletar_acervo.py` em modo rapido (sem `--datajud`) e ler `N_total_com_bloco` + a contagem do recorte.
- Benchmark: rodar `benchmark_datajud.py` com os filtros e ler `total_hits_no_indice`.

**Se N < {{N_MINIMO}}** no recorte: avisar JA NA TRIAGEM que a resposta sera qualitativa (PE-04) — e perguntar se o operador quer alargar o recorte (trocando precisao por comparabilidade — registrar o trade-off).

---

## 4. CHECKPOINT 1

```
ENQUADRAMENTO JURIMETRICO
- Pergunta:  [uma frase, respondivel com dados]
- Tipo:      [caso unico | portfolio | benchmark | quantum | tempo | viabilidade]
- Fonte(s):  [acervo (N=~..) | DataJud (hits=~..) | jurisprudencia]
- Recorte:   [area/classe/assunto/orgao/periodo]
- Destino:   [interno | proposta | subsidio de peca]
- N previsto: [numero] -> [quantitativo | SO QUALITATIVO (PE-04)]
- Casos sem bloco no recorte: [n] -> instrumentar antes? [sim/nao]
```

Confirmar com o operador antes de rodar o motor (default `checkpoint`).

---

## 5. ROTEAMENTO

Apos confirmacao: `instrumentar-caso` se houver bloco faltando/desatualizado (P2) → motor Tier 2 da Dimensao 1 → `estilo-relatorio-jurimetrico` na redacao → `revisao-final-jurimetria` (PE-14).

## 6. ENCERRAMENTO

A triagem entrega: pergunta travada, fonte(s), recorte harmonizado, destino e expectativa honesta de N. Pergunta que nao pode ser respondida com os dados disponiveis e dita como tal — oferecer o que E respondivel no lugar.
