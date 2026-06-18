# CASOS-OURO — biblioteca de regressão de saída (Camada 4)

Cada arquivo `.json` é um **caso real DE-IDENTIFICADO** (sem dado de cliente — repo público)
que reproduz o *formato jurídico* de uma situação já validada, com a **saída esperada**
(`deve_concluir` / `nao_pode`). Servem para testar se uma versão nova do plugin ainda
produz a conclusão correta — e para travar a volta de erros já corrigidos.

## Duas verificações
1. **Determinística (automática)** — `../check-regressao.py` + `../regressoes.json`:
   confere, sobre o conteúdo do repo, que os erros corrigidos não reapareceram. Roda em
   segundos, entra na suíte de pré-publicação (Camada 6). É o backbone.
2. **De saída (re-run + julgamento)** — como o plugin é movido por IA, a saída varia; não dá
   para comparar string. Protocolo:
   - Rodar o plugin sobre o `cenario` do caso-ouro (`/start` → `/triagem` → produção → revisão R1-R5).
   - Conferir que a peça/análise satisfaz TODO item de `deve_concluir` e NENHUM de `nao_pode`.
   - O `red_team_deve_pegar` lista o que a rodada R5 (Camada 3) tem obrigação de capturar.
   - Juiz: o advogado (Camada 7) ou um agente revisor independente. Divergência = investigar
     (ou o plugin regrediu, ou o caso-ouro precisa ser atualizado por mudança de lei/jurisprudência).

## Como crescer a biblioteca
Todo caso-piloto novo ou erro encontrado vira um caso-ouro aqui (de-identificado) + uma regra
em `regressoes.json` quando o erro for checável estaticamente. Assim a confiabilidade só sobe.

## Casos atuais
- `isencao-rpps-municipal-ajuste-anual.json` — isenção IRPF; lição do quantum + instrumento (jose-antonio).
- `rj-credor-trabalhista-concursal-integral.json` — habilitação RJ; concursalidade pelo fato gerador (Casa de Farinha).
