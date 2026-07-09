---
name: execucao-fazenda-publica-trabalhista
description: >
  EXECUCAO CONTRA A FAZENDA PUBLICA TRABALHISTA. Use quando menciona: executar a Fazenda, devedora subsidiaria ente publico, precatorio, RPV, requisicao de pequeno valor, art. 535 CPC, redirecionamento a tomadora publica, beneficio de ordem.
metadata:
  version: "0.1.0"
  area: "Trabalhista"
  tier: 2
---

# EXECUCAO CONTRA A FAZENDA PUBLICA TRABALHISTA

> Skill **Tier 2** de execucao, lado exequente (com o espelho defensivo no item 6). O cenario-tipo: empresa prestadora some sem bens e o titulo condenou o ente publico tomador de forma subsidiaria. A execucao contra a Fazenda tem rito PROPRIO — quem trata a Fazenda como devedor comum perde meses em atos nulos.

---

## 0. QUANDO ACIONAR

(a) Titulo com condenacao subsidiaria de ente publico (Sumula 331 V/VI TST) e devedora principal insolvente; (b) condenacao direta de ente publico; (c) defesa do exequente contra impugnacao da Fazenda; (d) duvida precatorio x RPV.

## 1. ANTES DO REDIRECIONAMENTO (ordem que evita nulidade)

1. **Ler o titulo:** o alcance da subsidiariedade e o que a sentenca disse — limites temporais (ex.: creditos posteriores ao contrato com o ente), verbas excluidas, e se ja autorizou execucao direta. Nao pedir alem do titulo (coisa julgada).
2. **Esgotar a devedora principal NESTES autos:** citacao para pagamento (art. 880 CLT), SISBAJUD/RENAJUD/INFOJUD frustrados. O beneficio de ordem do subsidiario se esgota com o inadimplemento demonstrado da principal — e cabe A FAZENDA, se quiser afastar a constricao, indicar bens livres da devedora.
3. **Nao rediscutir culpa:** a responsabilidade da tomadora publica (culpa in vigilando — Tema 1118 STF, onus do autor NA FASE DE CONHECIMENTO) ja foi resolvida no titulo transitado. Execucao nao reabre.
4. **Socios da principal NAO sao pre-requisito:** a jurisprudencia iterativa do TST dispensa tanto o IDPJ quanto a execucao previa dos socios para alcancar o responsavel subsidiario QUE CONSTA DO TITULO. (Se a estrategia preferir os socios, ai sim IDPJ — ver `liquidacao-execucao-trabalhista` 5-B.)

## 2. O RITO CONTRA A FAZENDA (art. 535 CPC c/c 769/889 CLT)

- **Sem penhora, sem garantia:** a Fazenda e INTIMADA para, querendo, impugnar em 30 dias (art. 535 CPC). Bens publicos sao impenhoraveis — SISBAJUD contra ente publico e ato nulo/inutil, nao requerer.
- **Nao impugnada ou rejeitada a impugnacao:** expede-se **precatorio** (CF art. 100) ou **RPV** conforme o valor.
- **RPV:** Uniao = ate 60 salarios minimos (Lei 10.259/2001 art. 17 par.1); Estados/DF/Municipios definem teto proprio em lei local (na omissao, 40 SM Estados / 30 SM Municipios — ADCT art. 87) — `[VERIFICAR teto do ente]`. Valor acima do teto: ou precatorio integral, ou RENUNCIA ao excedente para receber por RPV (decisao do OPERADOR, registrar no CASO.md).
- **Discriminar por credor:** credito do reclamante e honorarios do advogado sao requisicoes autonomas — o teto de RPV afere-se por titular.

## 3. JUROS E CORRECAO CONTRA A SUBSIDIARIA

A Fazenda condenada SUBSIDIARIAMENTE responde pelo debito tal como constituido contra a devedora principal — **sem a reducao de juros da Lei 9.494/97 art. 1-F, que e pessoal do ente devedor principal (OJ 382 SDI-1 TST)**. Conferir o que o titulo/liquidacao ja fixou (ADC 58/59 STF: IPCA-E pre-judicial + Selic; pos-Lei 14.905/2024 `[VERIFICAR]` a regra vigente na conta). Apos a expedicao do precatorio, a atualizacao segue o regime constitucional proprio (CF art. 100 par.5 e 12).

## 4. A PECA DO EXEQUENTE (estrutura-tipo)

```
1. Cumprimento da intimacao/decisao (ID, prazo)
2. Insolvencia da devedora principal (SISBAJUD frustrado, revel, BNDT — docs)
3. Diligencias residuais contra a principal (SISBAJUD reiterado etc.)
4. REDIRECIONAMENTO a Fazenda nos limites do titulo (transcrever o alcance)
5. Intimacao na forma do art. 535 CPC; precatorio/RPV conforme o valor
6. (se ha parcela fora da subsidiariedade) contadoria para discriminar
7. Pedidos encadeados + afastamento do art. 11-A CLT (meio efetivo indicado)
```

## 5. IMPUGNACAO TIPICA DA FAZENDA (e a resposta)

| Alegacao | Resposta do exequente |
|----------|----------------------|
| Beneficio de ordem | esgotamento demonstrado; onus DELA de indicar bens livres da principal |
| Rediscutir culpa/fiscalizacao | preclusao/coisa julgada — resolvido no titulo |
| Juros da Lei 9.494 | OJ 382 SDI-1 — subsidiaria responde como o devedor principal |
| Excesso de execucao | conta da liquidacao homologada; apontar item a item o que ja precluiu |
| Verbas fora do alcance | conferir o titulo; se procedente, discriminar na contadoria (nao perder o resto) |

## 6. LADO FAZENDA/RECLAMADA (espelho, PA-05)

Defendendo o ente: exigir a demonstracao real do esgotamento (diligencias meramente formais nao bastam), fiscalizar os limites do titulo (temporais e materiais), impugnar calculos no prazo do art. 535, requerer discriminacao das parcelas fora da subsidiariedade e conferir o enquadramento RPV x precatorio.

## 7. VEDACOES ESPECIFICAS

- **PA-05** — polo confirmado no CASO.md; esta skill serve aos dois lados (itens 4-5 x 6).
- **PA-08** — prazos: impugnacao da Fazenda 30 dias (art. 535); agravo de peticao 8 dias.
- **PA-11/PA-13** — teto de RPV do ente local SEMPRE `[VERIFICAR]` em lei local; nada de teto "de cabeca".
- **PA-20/PA-21** — valores so da conta homologada; nunca prometer prazo de pagamento de precatorio.
- Nunca requerer penhora/SISBAJUD contra o ente publico.

## 8. INTEGRACAO

Acionada por: `trabalhista-master`, `liquidacao-execucao-trabalhista` (quando o titulo tem subsidiario publico). Apoio: `calculos-trabalhistas` (discriminacao), `jurisprudencia-trabalhista`. Entrega para: `suprema-corte-trabalhista` (R1-R5 — R2 confere titulo/limites; R5 ataca por beneficio de ordem e excesso).
