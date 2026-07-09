---
name: coleta-acervo
description: >
  COLETA ACERVO — Skill Tier 2, Modulo C (portfolio proprio). Acione para "relatorio do acervo", "taxa de exito", "quantos casos temos em X", "quanto ja recuperamos", ou como perna propria de um benchmark.
metadata:
  version: "0.1.0"
  area: "Jurimetria"
  tier: 2
---

# COLETA ACERVO (Modulo C — portfolio proprio)

> Skill **Tier 2**. O unico lugar do sistema onde existe quantum e desfecho. Descritivo do MEU acervo — nao e mercado, nao e tribunal, nao e previsao.

---

## 0. ENTRADA

CASE_ROOT (da config) + o recorte da triagem (area, status, periodo...).

## 1. EXECUCAO

```
py scripts/coletar_acervo.py "<CASE_ROOT>"                     # retrato rapido (so acervo)
py scripts/coletar_acervo.py "<CASE_ROOT>" --datajud           # + duracao de cada caso (lento, throttled)
py scripts/coletar_acervo.py "<CASE_ROOT>" --json dataset.json # salva o dataset p/ recortes finos
```

O coletor ja aplica o freio de N-minimo (media/taxa viram `null` com a nota "N<limiar: use so qualitativamente"). **Respeitar o freio no texto** — nao recalcular na mao o que o script se recusou a calcular (PE-04).

Para recortes que o script nao agrega (ex.: quantum por assunto CNJ especifico), usar o `dataset.json` e agregar em cima — aplicando o MESMO freio ao subgrupo.

## 2. SAIDA (o que reportar)

- **Cobertura:** CASO.md encontrados x com bloco x SEM bloco (estes estao FORA da conta — dizer quantos e oferecer `instrumentar-caso`). Cobertura baixa = vies de instrumentacao (PE-05): os casos instrumentados podem nao representar o acervo.
- **Composicao:** N por area, tribunal, status, resultado (fechados).
- **Quantum obtido:** soma sempre; media so com N ≥ limiar; com N que permita, mediana e faixa (PE-11).
- **Taxa de exito** (media de percentual_exito) so com N ≥ limiar.
- Carimbo em tudo: N, recorte, fonte "acervo proprio ({{FIRM_NAME}})", data da coleta.

## 3. LIMITES (declarar no relatorio)

- Acervo proprio ≠ populacao: reflete o perfil de casos que o escritorio aceita (vies de selecao, PE-05).
- Casos em andamento nao tem desfecho — taxa de exito e sobre os FECHADOS instrumentados.
- `--datajud` em acervo grande e lento (backoff da chave compartilhada) — avisar antes.

## 4. SIGILO (P5)

O dataset consolidado contem numeros de processo (publicos), nunca nomes. Antes de qualquer versao do relatorio sair do escritorio: scanner de sigilo. Dataset `.json` fica no workspace local, fora de pasta sincronizada sem ciencia.

## 5. ENCERRAMENTO

Entregar o retrato com cobertura + composicao + desfechos, redigido pela `estilo-relatorio-jurimetrico` e auditado pela `revisao-final-jurimetria`. Se a pergunta pedia comparacao com o tribunal, seguir para `benchmark-datajud` com o MESMO recorte CNJ (PE-09).
