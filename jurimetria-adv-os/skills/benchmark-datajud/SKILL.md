---
name: benchmark-datajud
description: >
  BENCHMARK DATAJUD — Skill Tier 2, Modulo B (regua publica). Acione para "meus casos demoram mais que a media?", "quanto demora um processo dessa classe nessa vara?", "qual vara e mais rapida?", ou qualquer regua externa de tempo. NAO responde quantum (DataJud nao tem — usar analise-quantum).
metadata:
  version: "0.1.0"
  area: "Jurimetria"
  tier: 2
---

# BENCHMARK DATAJUD (Modulo B — regua publica)

> Skill **Tier 2**. Poe o acervo diante da regua do tribunal — so em TEMPO/composicao. Comparacao honesta exige o mesmo recorte dos dois lados (PE-09) e a confissao de que a amostra publica tambem tem vies (PE-05).

---

## 0. ENTRADA

Recorte CNJ da triagem: tribunal (alias), classe (+ assunto, orgao, grau quando fizer sentido). **Classe e obrigatoria** — benchmark sem classe nao e comparavel.

## 1. EXECUCAO

```
py scripts/benchmark_datajud.py --tribunal trt1 --classe "Acao Trabalhista - Rito Ordinario" --orgao "Vara do Trabalho de <comarca>"
py scripts/benchmark_datajud.py --tribunal tjrj --classe-codigo <cod> --assunto-codigo <cod> --size 500
py scripts/benchmark_datajud.py ... --json amostra.json        # guarda a amostra p/ conferencia
```

Preferir **codigos CNJ** (vindos do bloco jurimetrico, que o `instrumentar-caso` puxou do DataJud) a nomes — nomes variam, codigo nao. A saida ja vem carimbada: filtros, metodo, N retornado x total no indice, data.

## 2. A COMPARACAO (quando ha perna propria)

1. Rodar `coleta-acervo` (ou ler o dataset) filtrando o MESMO recorte CNJ.
2. Comparar **mediana com mediana** (e quartis) — nunca media de um lado com mediana do outro.
3. Reportar as duas pernas com seus Ns: "acervo: mediana X dias (N=..); tribunal: mediana Y dias (N=.., de um total de Z no indice)".
4. Diferenca e DESCRITIVA — nao explicar causa sem dado ("somos mais rapidos" pode ser mix de assuntos, fase, epoca — PE-08).

## 3. LIMITES (a saida do script ja lista; o texto repete os que importam)

- Amostra = **uma pagina** (ate 1000) dos mais recentes por ajuizamento — nao e o universo; declarar N retornado x total_hits.
- Processos em andamento: duracao **censurada a direita** (subestima); baixados antigos podem ter saido do indice.
- Sem quantum/merito (PE-07). Regua de VALOR e com `analise-quantum`.
- Indexacao do DataJud varia por tribunal/periodo.

## 4. ENCERRAMENTO

Entregar a regua (e a comparacao, se pedida) com os dois carimbos completos. Perguntas de "por que" viram hipoteses declaradas como hipoteses — nunca conclusao causal.
