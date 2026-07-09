---
name: estilo-relatorio-jurimetrico
description: >
  ESTILO RELATORIO JURIMETRICO — Skill Tier 2 transversal, invariante. Acione sempre que redigir relatorio, analise, quadro ou qualquer texto com numero jurimetrico — inclusive respostas curtas em chat.
metadata:
  version: "0.1.0"
  area: "Jurimetria"
  tier: 2
---

# ESTILO RELATORIO JURIMETRICO

> Skill **Tier 2 transversal**, invariante. O estilo aqui nao e estetica — e a Camada 3 fazendo a Camada 1 aparecer no texto. Um relatorio bonito sem carimbo e um relatorio reprovado.

---

## 0. A ESTRUTURA FIXA (template `relatorio-jurimetrico.md.tpl`)

1. **Pergunta** — uma frase, a mesma travada na triagem. Um relatorio = uma pergunta.
2. **Dados e metodo** — fontes (com data de coleta), recorte por extenso, N total e por subgrupo, estatisticas usadas.
3. **Resultados** — cada numero no formato-carimbo (abaixo). Tabelas para enumeracao; prosa para leitura.
4. **Limitacoes e vieses** — NUNCA vazio (PE-05): amostra != populacao, censura a direita, cobertura de instrumentacao, DataJud sem quantum, epoca dos valores.
5. **Leitura** — o que os dados permitem dizer (descritivo) e o que NAO permitem (preditivo/promessa). As duas metades sao obrigatorias.
6. **Rodape** — disclaimer padrao do template + plugin/versao.

Resposta curta em chat: dispensa as secoes, NUNCA dispensa o carimbo.

## 1. O CARIMBO (PE-01 em formato)

```
<valor> (<estatistica>, N=<n>, <fonte>, <recorte se nao obvio>, coleta <AAAA-MM-DD>)
Ex.: mediana de 412 dias (N=87 concluidos, DataJud/TRT1 classe X, coleta 2026-07-04)
```

- **Mediana e quartis antes de media** (PE-11); media so acompanhada e so com N >= limiar (PE-04).
- N < limiar: sem agregado — listar os casos qualitativamente ("dos 3 casos fechados: 2 acordos de R$ .., 1 improcedente").
- Vivos x concluidos sempre separados; "ja dura" != "durou".
- Percentual sempre com a base ("40% (N=10)" — 4 casos, dizer isso).

## 2. LINGUAGEM

- Sobria, direta, portugues pleno **com acentos** (convencao do escritorio — o conteudo do relatorio e acentuado; nomes de arquivo sem acento).
- Verbos descritivos: "os casos fechados terminaram em", "a faixa observada foi". PROIBIDOS: "chance de", "probabilidade de exito", "tendencia garante", "historicamente ganhamos" (PE-03).
- Hipotese e rotulada como hipotese; correlacao nunca vira causa no texto (PE-08).
- Numero redondo honesto: nao reportar "412,37 dias" de uma amostra de 12 — precisao falsa e forma de mentir.

## 3. ENTREGA (convencao Adv-OS)

- **`.txt` por padrao** (sem docx/pdf salvo pedido explicito).
- Relatorio que sai do escritorio: scanner de sigilo antes (P5); numeros de processo sao publicos, nomes de cliente NUNCA em agregado (PE-06).
- Nome de arquivo: `AAAA-MM-DD - <tema> - relatorio jurimetrico.txt` (padrao geral do escritorio; nao e peticao, nao usa data-sufixo).
- Caminho final <= ~250 caracteres (MAX_PATH).

## 4. ENCERRAMENTO

Antes de passar a `revisao-final-jurimetria`: reler cada numero perguntando "carimbo completo? mediana? N basta? limitacao dita?". O estilo e a primeira auditoria.
