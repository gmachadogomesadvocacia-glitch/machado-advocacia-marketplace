---
name: memoria-de-caso-consumidor
description: >
  MEMORIA DE CASO CONSUMIDOR — Skill Tier 1, Protocolo P3. Gatilhos: novo caso, abrir caso, CASO.md, memoria do caso, retomar, /caso-consumidor, sigilo LGPD compartimentacao.
metadata:
  version: "0.1.0"
  area: "Direito do Consumidor e Bancario"
  tier: 1
---

# MEMORIA DE CASO CONSUMIDOR

> Skill **Tier 1**, **Protocolo P3**. Mantem o `CASO.md` (estado vivo) e o `MEMORY.md` (decisoes/historico) **compartimentados por cliente**. E a fonte unica das variaveis de **polo/eixo/esfera/rito** que todas as skills leem. Faz cumprir o **PA-21** (sigilo OAB + LGPD).

---

## 0. QUANDO ACIONAR

Ao abrir caso novo (chamada pela `triagem-consumidor`), retomar, listar ou arquivar caso; sempre que houver de gravar/atualizar a ficha. Toda skill de producao atualiza o `CASO.md` por aqui ao fim da sua fase.

## 1. LOCAL E COMPARTIMENTACAO (PA-21)

- Raiz: **`<CASE_ROOT>/<slug>/`** — pasta unificada e **COMPARTILHADA** entre os plugins Adv-OS, uma pasta por cliente, isolada.
- **CASE_ROOT** vem do `config.md` (campo `Raiz dos casos`). No Claude Code, e o acervo do escritorio: `<acervo>/Casos-Ativos`. Fora do Code (**fallback**), `<COWORK>/consumidor/casos`.
- `<slug>` = nome do cliente em minusculas-com-hifen (ex.: `joao-da-silva`).
- Estrutura unificada:

```
<CASE_ROOT>/<slug>/
  CASO.md        # estado vivo (triagem 4D, partes, foro, Selo, prazos, docs, linha)
  MEMORY.md      # decisoes, quantum, pecas, historico fatico-processual
  arquivos/      # contrato, faturas, extratos, prints, protocolos, negativacao
  pecas/         # produtos do caso (iniciais, contestacoes, reclamacoes, recursos)
```

- As pecas produzidas vao em **`<slug>/pecas/`**.

- **Nunca** misturar dados de clientes diferentes na mesma pasta ou peca (PA-21 — vazamento entre casos e violacao nuclear).

### Sigilo e sincronizacao
- No fallback, a pasta `consumidor/casos/` deve estar **gitignored** por default (dados de cliente nunca entram no plugin distribuido). No Code, o `CASE_ROOT` aponta para o acervo controlado do escritorio (`<acervo>/Casos-Ativos`), fora do plugin.
- Se o `cwd` estiver em pasta **sincronizada** (OneDrive, iCloud, Google Drive, Dropbox), **alertar** o operador: dados de cliente sao sigilosos (Estatuto OAB) e pessoais (LGPD). Confirmar que a sincronizacao e do acervo controlado do escritorio antes de gravar. Nunca persistir dado de cliente fora da pasta do caso.

---

## 2. OPERACOES

### 2.1 NOVO CASO
1. Definir `<slug>` a partir do cliente; criar `<CASE_ROOT>/<slug>/` + `arquivos/` + `pecas/`.
2. Instanciar **`CASO.md`** a partir de **`templates/CASO.md.tpl`** e **`MEMORY.md`** a partir de **`templates/MEMORY-caso.md.tpl`**, preenchendo as variaveis disponiveis e deixando as ausentes como `[INFORMAR]` (PA-15 — nunca inventar, PA-03).
3. Gravar o resultado da triagem 4D (polo, eixo, esfera, rito) e o status do Selo P1 (PENDENTE ate o validador emitir).

### 2.2 RETOMAR
Localizar a pasta do `<slug>`, **ler o `CASO.md` e o `MEMORY.md` antes de qualquer acao**, e reportar o estado executivo (polo, fase, proximo passo, prazos, Selo).

### 2.3 LISTAR
Varrer `<CASE_ROOT>/*/CASO.md` e apresentar tabela: cliente, polo, eixo, fase, proximo prazo critico. Nao expor conteudo sensivel alem do necessario.

### 2.4 ARQUIVAR
Marcar a fase como encerrada no `MEMORY.md`, registrar a data e o desfecho, e mover/sinalizar a pasta como arquivada. Manter o sigilo (PA-21).

---

## 3. ESTRUTURA DO CASO.md (campos-chave)

Segue o `CASO.md.tpl`. Blocos:

- **Triagem 4D** — `Polo do cliente` (variavel-mae, PA-05), eixo, esfera, rito, tipo de tarefa.
- **Partes** — qualificacao + polo de cada parte; nota da relacao de consumo (PA-04 — destinatario final + vulnerabilidade).
- **Localizacao e Competencia (P5)** — domicilio do consumidor, foro/vara/JEC (art. 101, I CDC), n. do processo.
- **Selo de Validacao Legal Previa (P1)** — status (PENDENTE/EMITIDO), normas validadas, data.
- **Prazos Criticos** — decadencia art. 26 (30/90 d), prescricao art. 27 (5 anos), arrependimento art. 49 (7 d, so fora do estabelecimento), recurso JEC 10 d (PA-11).
- **Documentos** — numerados "doc. N".
- **Linha de trabalho / Historico** — triagem, Selo, analises, tese, pecas, audiencia, sentenca.

## 4. ESTRUTURA DO MEMORY.md (campos-chave)

Segue o `MEMORY-caso.md.tpl`. Blocos: **estado executivo** (polo, eixo, fase, proximo passo, Selo); **linha estrategica adotada**; **log de decisoes** (data/decisao/motivo/autor); **quantum e calculos**; **pecas produzidas** (status + revisao R1-R4); **historico fatico-processual**.

---

## 5. ATUALIZACAO POR FASE

Ao fim de **cada fase** do pipeline, gravar:

| Fase | O que registrar |
|------|------------------|
| Triagem | 4D + abertura do caso |
| Selo P1 | status EMITIDO + normas + data |
| Insumos (P2) | documentos analisados (numerados) |
| Estrategia | matriz trilateral + linha estrategica adotada |
| Producao | peca em `pecas/` + status + revisao R1-R4 |
| Protocolo/audiencia/recurso | evento no historico + novos prazos |

> O `CASO.md` e a **fonte da verdade** do polo. Se houver contradicao de polo entre fontes, **pare e pergunte** (PA-05) antes de qualquer producao.

---

## 6. ENCERRAMENTO

Entrega o `CASO.md` e o `MEMORY.md` criados/atualizados, compartimentados e sob PA-21, com a triagem 4D, partes, foro, Selo, prazos, documentos e linha de trabalho gravados. Nenhum dado inventado (PA-03/PA-15); nenhum vazamento entre casos (PA-21).
