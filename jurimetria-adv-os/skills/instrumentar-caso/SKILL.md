---
name: instrumentar-caso
description: >
  INSTRUMENTAR CASO — Skill Tier 1, operacionaliza o Protocolo P2 (Instrumentacao). Acione ao abrir caso novo, ao encerrar caso (preencher desfecho), quando a coleta apontar casos sem bloco, ou antes de qualquer analise de caso.
metadata:
  version: "0.1.0"
  area: "Jurimetria"
  tier: 1
---

# INSTRUMENTAR CASO (Protocolo P2)

> Skill **Tier 1** — a qualidade de TODA estatistica do plugin depende daqui. Bloco mal preenchido = numero mentiroso na ponta. Dado que nao se sabe, fica vazio (PE-12).

---

## 0. QUANDO ACIONAR

(a) Caso novo aberto (por qualquer plugin Adv-OS) — inserir o bloco com identificacao + classificacao + caso; (b) caso encerrado — preencher o desfecho (quantum_obtido, resultado, forma/data de encerramento); o encerramento COMPLETO (desfecho + memoria + arquivamento) e orquestrado pela skill `encerrar-caso`, que chama esta; (c) `coleta-acervo` listou casos sem bloco; (d) antes de analise que dependa do caso.

## 1. FONTES DE PREENCHIMENTO (nesta ordem)

1. **CASO.md existente** — numero, partes, tese, valores ja registrados no corpo.
2. **DataJud** (`py scripts/ler_caso.py "<CASO.md>" --datajud` ou `py scripts/datajud_client.py <numero>`) — classe, assunto, orgao julgador, data de ajuizamento, grau **oficiais** (usar os do DataJud, nao os "de cabeca" — harmonizacao PE-09 nasce aqui).
3. **Operador** — polo, tese-ancora, quantum pretendido, desfecho. Perguntar o que faltar.

**Nunca** preencher por suposicao. Campo sem fonte = vazio + `[PREENCHER]` no relatorio de instrumentacao.

## 2. PROCEDIMENTO

1. Ler o `CASO.md`. Se ja ha bloco (`<!-- jurimetria:inicio -->`), atualizar so os campos vazios/desatualizados — **nunca sobrescrever desfecho preenchido** sem confirmacao.
2. Sem bloco: copiar o schema de `templates/bloco-jurimetrico.md.tpl` para o fim do `CASO.md`.
3. Rodar o DataJud para trazer classe/assunto/orgao/data oficiais; gravar `datajud_sync: <hoje>` (PE-10).
4. Validar com `py scripts/ler_caso.py "<CASO.md>"` — o parser deve devolver o dict sem erro.
5. `percentual_exito`: deixar o leitor calcular (obtido/pretendido); nao digitar na mao.

## 3. REGRAS DE OURO DO BLOCO

- `numero_processo` e publico; **nome do cliente NAO entra no bloco** (PE-06) — fica no corpo do CASO.md.
- `classe_cnj`/`assunto_cnj` = nomenclatura oficial CNJ vinda do DataJud (chave do benchmark).
- `quantum_obtido` = o que o cliente **efetivamente obteve** (acordo conta; sucumbencia nao desconta — anotar em `obs_jurimetria` se relevante).
- `status` acompanha a fase real; `resultado` so ao fechar.
- Processo em segredo de justica: DataJud nao devolve — anotar `obs_jurimetria: segredo (sem DataJud)` e seguir so com dados proprios.

## 4. MODO LOTE

Quando a coleta apontar varios casos sem bloco: processar um a um (checkpoint por caso, ou `--continuo` para inserir so identificacao+classificacao via DataJud em serie, deixando polo/tese/quantum para o operador confirmar depois). Respeitar o throttling da chave publica (o cliente ja faz backoff — nao paralelizar).

## 5. ENCERRAMENTO

Entregar o resumo: campos preenchidos (e a fonte de cada grupo), campos `[PREENCHER]` pendentes do operador, e `datajud_sync` carimbado. O caso so entra em estatistica quando o parser le o bloco sem erro.
