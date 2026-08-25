# Modelos de peca — leiloes-adv-os

Chassi de partida, **nunca** texto final. Toda peca gerada a partir daqui passa por:

1. `estilo-juridico-leiloes` (voz + anti-rastro de IA)
2. `revisao-final-leiloes` (R1-R4)
3. linter de peticoes (ERRO zera)

**Regras do escritorio que valem para todos os modelos:**

- `.txt` com **1 paragrafo = 1 linha** (linha unica e longa, sem quebra no meio).
- Datas, valores, Id e index em **negrito**.
- Documentos citados como "doc. N".
- Nome do arquivo terminando com a data de criacao `DD-MM-AAAA`.
- Campos entre `[[ ]]` sao de preenchimento obrigatorio; lacuna vira `[INFORMAR]`, nunca invencao.

## Modelos disponiveis

| Arquivo | Quando usar |
|---------|-------------|
| `imissao-na-posse.md` | arrematou, carta expedida, quer a posse (CPC 901, § 1º) |
| `desistencia-onus-oculto.md` | **prazo de 10 dias** — onus real ou gravame nao mencionado no edital (CPC 903, § 5º, I) |
| `reintegracao-fiduciaria.md` | adquirente em leilao da Lei 9.514 (art. 30, liminar, 60 dias) |
