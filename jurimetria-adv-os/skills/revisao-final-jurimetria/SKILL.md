---
name: revisao-final-jurimetria
description: >
  REVISAO FINAL JURIMETRIA — Skill Tier 3, a Suprema Corte do plugin. Acione SEMPRE antes de entregar qualquer analise, ou quando o usuario pedir revisar/auditar/conferir. Bypass so com --no-revisao/--quick explicito, registrado (PE-14) — as demais PEs nao tem bypass.
metadata:
  version: "0.1.0"
  area: "Jurimetria"
  tier: 3
---

# REVISAO FINAL JURIMETRIA (Suprema Corte R1-R4)

> Skill **Tier 3**, invariante. Operacionaliza o **Protocolo P6**. Nenhum numero sai sem passar por aqui (PE-14). Jurimetria e onde a IA juridica mais erra por excesso de confianca — esta e a ultima cerca.

---

## 0. ESCOPO

Auditar — nao refazer a analise. Aponta falhas exatas, classifica e devolve. Aplica-se a toda saida com numero: relatorio de acervo, benchmark, faixa de quantum, leitura de tempo, quadro de viabilidade, e ate resposta curta de chat com estatistica.

## 1. R1 — DADOS E PROVENIENCIA

- Toda fonte identificada (acervo/DataJud/jurisprudencia) com **data de coleta** (PE-10)?
- N declarado para CADA numero — total e subgrupos (PE-01)?
- Cobertura de instrumentacao dita (quantos CASO.md sem bloco ficaram fora — PE-12)?
- Nenhum dado inventado ou "de cabeca"? Julgado citado tem identificacao (ou `[VERIFICAR]`)?
- DataJud usado so para o que ele tem (capa+movimentos — PE-07)?

## 2. R2 — METODO

- Estatistica cabivel ao N (media/taxa so com N >= limiar — PE-04)?
- **Mediana/quartis antes de media** (PE-11)? Precisao compativel com a amostra?
- Benchmark harmonizado (mesma classe+assunto+orgao/grau dos dois lados — PE-09)? Mediana comparada com mediana?
- Censura a direita tratada (vivos separados de concluidos; "ja dura" != "durou")?
- Metodo bifasico no quantum (procedencia separada de valor)?

## 3. R3 — INTERPRETACAO

- A saida continua DESCRITIVA (PE-02)? Nenhum "vai durar/vai ganhar/provavel condenacao"?
- **Nenhuma promessa ou insinuacao de resultado** (PE-03 — veda OAB)? Checar tambem sinonimos disfarcados ("cenario muito favoravel", "recuperacao esperada de R$")?
- Correlacao nao virou causalidade (PE-08)? Hipoteses rotuladas?
- Secao de limitacoes presente e substantiva (PE-05)? A "Leitura" diz o que os dados NAO dizem?

## 4. R4 — FORMA E SIGILO

- Estrutura do template (pergunta/dados/resultados/limitacoes/leitura) ou, em resposta curta, carimbo integral?
- **PII zero**: nenhum nome de cliente em agregado/relatorio (PE-06)? Se o material sai do escritorio: scanner de sigilo rodado (P5)?
- Portugues pleno com acentos; `.txt`; disclaimer do rodape presente?
- Se o numero vai para peca/proposta de outro plugin: carimbo PE-13 anexado?

## R5 — VERIFICACAO ADVERSARIAL (RED-TEAM)

Mude de chapeu: voce AGORA e um estatistico cetico contratado para DERRUBAR o relatorio. Achou UMA falha material → REPROVADO. Eixos:

- **N** — algum numero apoiado em amostra que nao o sustenta? Percentual de base minuscula?
- **VIES** — a amostra permite a conclusao? (acervo = casos que o escritorio aceitou; DataJud = pagina unica dos recentes; jurisprudencia = so o que foi recorrido)
- **CENSURA** — processos vivos contaminaram media de duracao?
- **COMPARACAO** — maca com maca? epoca com epoca? mediana com mediana?
- **FRONTEIRA** — alguma frase que um cliente leria como promessa? (teste: "se o cliente perder, esta frase o constrangeria numa reclamacao a OAB?")
- **ARITMETICA** — refazer 2-3 contas por amostragem contra a saida dos scripts.

**Veredito R5:** PASSOU / REPROVADO (eixo + falha + correcao).

## FICHA DE CONFERENCIA (acompanha a entrega, nao integra o relatorio)

```
FICHA DE CONFERENCIA — analise jurimetrica
- PERGUNTA respondida: ...
- FONTES (cada uma -> data de coleta): ...
- NUMEROS-CHAVE (cada um -> N + fonte): ...
- CASOS FORA DA CONTA (sem bloco / sem desfecho): ...
- LIMITACOES DECLARADAS: ...
- VEREDITO: R1 _ · R2 _ · R3 _ · R4 _ · R5 _
- USO PERMITIDO: [interno | proposta (com disclaimer) | subsidio de peca (carimbo PE-13)]
```

## 5. VEREDITO

- **APROVADO** — segue.
- **APROVADO COM RESSALVAS** — segue com as ressalvas registradas para ciencia do advogado.
- **REPROVADO** — bloqueia. Falha exata (rodada + item + PE tocada) e devolve ao produtor; resubmeter apos corrigir.

Encerrar com o quadro R1-R5 + FICHA DE CONFERENCIA.

## 6. BYPASS

Apenas da revisao (PE-14), com `--no-revisao`/`--quick` explicito do operador, registrado. **As Proibicoes Estatisticas em si nao tem bypass** — um relatorio sem R1-R4 ainda nao pode prometer resultado nem esconder N.

## 7. ENCERRAMENTO

So libera a entrega a analise que passa em R1-R5 com a FICHA anexa. Na jurimetria, a credibilidade do escritorio esta em cada carimbo — a Suprema Corte e quem a protege.
