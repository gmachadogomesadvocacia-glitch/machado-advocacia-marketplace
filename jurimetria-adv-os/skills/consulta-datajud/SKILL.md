---
name: consulta-datajud
description: >
  CONSULTA DATAJUD — Skill Tier 2, Modulo A (caso unico). Acione para "quanto tempo este processo esta levando", "qual o ultimo andamento", "esta parado?", verificacao de fase, ou para sincronizar a duracao de um caso do acervo.
metadata:
  version: "0.1.0"
  area: "Jurimetria"
  tier: 2
---

# CONSULTA DATAJUD (Modulo A — caso unico)

> Skill **Tier 2**. O retrato oficial e gratuito de UM processo: capa + movimentos. O que o DataJud nao tem (quantum, merito, teor), nao sai daqui (PE-07).

---

## 0. ENTRADA

Numero CNJ (`NNNNNNN-DD.AAAA.J.TR.OOOO`) — direto do operador ou lido do bloco jurimetrico de um `CASO.md`.

## 1. EXECUCAO

```
py scripts/datajud_client.py <numero-cnj>                       # processo avulso
py scripts/ler_caso.py "<caminho/CASO.md>" --datajud            # caso do acervo (une as 2 fontes)
py scripts/datajud_client.py <numero> --tribunal api_publica_x  # tribunal fora do mapa de roteamento
```

O cliente busca a chave publica vigente na wiki do CNJ (rotaciona; ha fallback) e faz backoff em 429 — a chave e compartilhada e vem throttled. Nao paralelizar consultas.

## 2. SAIDA (o que reportar)

- **Capa:** classe, assunto principal, orgao julgador, grau — nomenclatura oficial CNJ.
- **Tempo:** data de ajuizamento → ultimo movimento = duracao em dias (e ~meses); numero de movimentos.
- **Ritmo:** movimentos recentes? Ultima movimentacao ha quanto tempo? (Sinal de processo parado — mas "parado no DataJud" pode ser atraso de indexacao: dizer isso.)
- **Cruzamento com o acervo** (se veio de CASO.md): divergencia entre classe/assunto do bloco e do DataJud → apontar e sugerir corrigir o bloco (a fonte oficial vence — PE-09).

Todo numero com o carimbo: fonte DataJud/CNJ + data da consulta (PE-01/PE-10). Ao consultar caso do acervo, oferecer gravar `datajud_sync` via `instrumentar-caso`.

## 3. LIMITES (dizer sempre que relevante)

- **Nao encontrado** ≠ inexistente: pode nao estar indexado ainda, ou estar em **segredo de justica** (filtrado na origem).
- **Duracao** = ajuizamento → ultimo movimento indexado; nao e "tempo ate sentenca" nem "tempo ate transito" — para fases, `tempo-processual`.
- **Movimentos** sao codigos/descricoes da tabela CNJ; nao trazem teor de decisao.
- Processo em curso: duracao e leitura parcial (censura a direita).

## 4. ENCERRAMENTO

Entregar o resumo do processo com os limites declarados. Se a pergunta do operador era na verdade sobre TENDENCIA (varios processos), rotear para `benchmark-datajud` ou `coleta-acervo` via `triagem-jurimetrica`.
