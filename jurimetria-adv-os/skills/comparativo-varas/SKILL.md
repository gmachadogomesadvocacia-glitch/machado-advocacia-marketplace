---
name: comparativo-varas
description: >
  COMPARATIVO ENTRE VARAS — Skill Tier 2, extensao do Modulo B. Acione para: comparar varas, por que esta vara demora mais, ritmo da 1a x 3a vara, mesma tese andamentos diferentes, expectativa de tempo por unidade.
metadata:
  version: "0.1.0"
  area: "Jurimetria"
  tier: 2
---

# COMPARATIVO ENTRE VARAS (Modulo B por orgao julgador)

> Skill **Tier 2**. Nasceu de padrao real do acervo: o MESMO executado, com a MESMA tese, andando em ritmos opostos em duas varas da mesma comarca. O comparativo transforma essa percepcao em numero carimbado — e delimita com rigor o que o numero NAO diz.

---

## 0. QUANDO ACIONAR

(a) Caso ja distribuido: "quanto tempo costuma levar NESTA vara?"; (b) carteira com casos gemeos em varas diferentes andando em ritmos distintos; (c) retrato gerencial da comarca para expectativa de duracao. Confirmar a pergunta analitica na `triagem-jurimetrica` antes de rodar.

## 1. FRONTEIRA ETICA (antes de qualquer numero)

- **NAO se escolhe vara.** Distribuicao e por sorteio; direcionar distribuicao e fraude. A skill RECUSA pedido com esse fim (Camada 1) e diz o porque.
- **Descritivo, nunca preditivo** (PE-02/PE-03): "a mediana da vara X e maior" NAO vira "seu caso vai demorar X" nem "a vara Y decide a favor".
- Ritmo diferente tem causas invisiveis ao DataJud (acervo herdado, forca de trabalho, complexidade da carteira) — a leitura registra isso SEMPRE (PE-05).

## 2. PROCEDIMENTO

1. **Recorte harmonizado (PE-09):** mesma classe CNJ + mesmo assunto + mesma janela de ajuizamento (default do `benchmark_datajud.py`: 4a->1a atras) para TODAS as unidades comparadas. Comparar vara de rito diverso e maca com laranja.
2. **Rodar o Modulo B POR ORGAO:** uma execucao de `py scripts/benchmark_datajud.py` por unidade, variando so o orgao julgador (mesmos demais filtros). Nao paralelizar (throttling da chave publica).
3. **Freio de N (PE-04):** unidade com N < {{N_MINIMO}} sai da comparacao quantitativa — vira nota qualitativa ("N insuficiente"). Dizer quantas sairam.
4. **Metricas por unidade:** N retornado x total do indice; mediana e quartis de duracao (concluidos separados de vivos — censura declarada); movimentos/ano como proxy de ritmo. Mediana compara com mediana (PE-11).
5. **Cruzar com o acervo proprio** quando houver casos gemeos: duracao dos NOSSOS casos em cada vara (bloco jurimetrico) ao lado da regua publica — N proprio quase sempre pequeno: leitura qualitativa.

## 3. SAIDA (quadro comparativo carimbado)

```
PERGUNTA: ...
RECORTE: classe X + assunto Y | comarca Z | ajuizados AAAA-AAAA | fonte DataJud (consulta DD/MM)
| Unidade | N (ret/total) | Mediana duracao | Q1-Q3 | Movs/ano | Obs |
LIMITACOES: censura a direita; composicao de acervo nao observavel; indexacao parcial
LEITURA: o que os numeros permitem dizer — e o que NAO permitem
```

Todo numero com N + metodo + fonte + data (PE-01); relatorio no template padrao (`estilo-relatorio-jurimetrico`); R1-R5 antes da entrega (PE-14). Se o comparativo subsidiar peca (ex.: justificar urgencia pela demora concreta da unidade), o numero viaja com carimbo PE-13.

## 4. INTEGRACAO

Acionada por: `jurimetria-master`, `triagem-jurimetrica` (Dimensao tempo/orgao). Usa: `benchmark_datajud.py` (Modulo B), `coletar_acervo.py`/blocos dos casos gemeos, `tempo-processual` (leitura de censura). Entrega para: `revisao-final-jurimetria` (R5 red-team ataca por N, censura e comparacao desarmonizada).
