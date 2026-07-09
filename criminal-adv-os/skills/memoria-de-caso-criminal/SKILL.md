---
name: memoria-de-caso-criminal
description: >
  Memoria de caso criminal Tier 1 — Protocolo P3. Ative em novo caso, abrir/retomar caso, CASO.md, memoria do caso, /caso-criminal ou ao registrar prazo/documento de caso penal.
metadata:
  version: "0.1.0"
  area: "Direito Penal e Processo Penal"
  tier: 1
---

# MEMORIA DE CASO CRIMINAL (Protocolo P3)

> Tier 1, invariante. Mantem o **estado vivo** do caso no `CASO.md`, compartimentado por cliente. **Sigilo reforcado**: dado penal e sensivel, pasta **gitignored**, nunca versionada no plugin distribuido. Atualiza apos cada entrega.

---

## 1. LOCAL E COMPARTIMENTACAO

Pasta **unificada de caso**, COMPARTILHADA entre os plugins Adv-OS, na raiz `CASE_ROOT`:

```
<CASE_ROOT>/<slug>/
├── CASO.md          (estado vivo)
├── MEMORY.md        (decisoes e historico)
├── arquivos/        (autos, BO, laudos, FAC — entrada)
└── pecas/           (produzidos — peca em <slug>/pecas/)
```

- **CASE_ROOT**: no Code → `<acervo>/Casos-Ativos`; **fallback** (sem acervo) → `<COWORK>/criminal/casos`. Gravado em `config.md` ({{CASE_ROOT}}).
- O estado interno do plugin NAO muda: continua em `<COWORK>/criminal/`.
- Um caso por pasta. Pasta **gitignored** por default (PA-12 / LGPD art. 11).
- Se o workspace/raiz for sincronizado (OneDrive/iCloud/Drive/Dropbox) → **alertar**: dado penal sensivel.

## 2. ESTRUTURA DO CASO.md

```
# CASO — <Cliente>
- POLO: defesa (investigado/reu/sentenciado) | assistencia de acusacao (vitima)
- CRIME / CAPITULACAO: art. ... (pena cominada)
- PROCESSO / IP: numero ...
- VARA / COMARCA: ...
- SITUACAO PRISIONAL: solto / flagrante / preventiva / temporaria / cumprindo pena
- DATAS: fato DD/MM · flagrante DD/MM · denuncia DD/MM · sentenca DD/MM

## DOCUMENTOS
- doc. 1 — ...
- doc. 2 — ...

## PRAZOS (com data)
- Prescricao: ... (vence DD/MM)
- Recurso: ... (vence DD/MM)

## FASE ATUAL
investigacao / acao penal / juri / recursos / execucao / acordos

## PECAS PRODUZIDAS
- AAAA-MM-DD - Cliente - tipo.txt

## TESES / ESTRATEGIA
- tese central ...
- subsidiarias ...

## PROXIMOS PASSOS
- [ ] ...
```

## 3. ROTINA DE ATUALIZACAO

1. **Apos cada entrega** — registrar a peca, mover prazos, anotar a fase.
2. **Ao receber documento novo** — numerar **"doc. N"** e listar em DOCUMENTOS.
3. **Ao calcular prescricao/prazo** — gravar a data de vencimento.
4. **Ao mudar a estrategia** — registrar a decisao no MEMORY.md (com data e motivo).

## 4. NOMENCLATURA E ENTREGA

- Arquivos: **`AAAA-MM-DD - Cliente - tipo da peca.ext`** (ex.: `2026-06-16 - Cliente - resposta a acusacao.txt`).
- Entregar em **`.txt`** por default; .docx/.pdf so a pedido.
- Documentos citados nas pecas por **"doc. N"**.

## 5. PROIBICOES

- **PA-12** — sigilo reforçado; dado penal nao vaza nem versiona.
- **PA-03** — so registrar fatos/datas reais; nada presumido.
- **PA-09** — a memoria protege o cliente; nada que o prejudique.
- Comandos: `/caso-criminal novo <slug>` · `<slug>` (retomar) · `list` · `arquivar <slug>`.
