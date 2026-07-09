---
name: memoria-de-caso-tributario
description: >
  Protocolo P3 — memoria de caso tributario. Ative ao abrir/retomar caso, criar CASO.md, registrar decisao, ou /caso-tributario.
metadata:
  version: "0.1.0"
  area: "Direito Tributario"
  tier: 1
---

# MEMORIA DE CASO TRIBUTARIO (Protocolo P3)

> Tier 1 (Insumo). O **CASO.md** e o estado vivo do caso. Atualizado apos **cada** entrega. Pasta gitignored — sigilo fiscal (PA-12). Caso na raiz configuravel `<CASE_ROOT>/<slug>/` (Code: `<acervo>/Casos-Ativos`; FALLBACK nuvem/sem acervo: `tributario/casos/`).

---

## 1. ESTRUTURA DO CASO.md

```
# CASO — <Cliente> — <tributo/esfera>

## PARTES
- Contribuinte/cliente: ... (CPF/CNPJ)
- Responsavel/socio: ...
- Fazenda exequente: Uniao / Estado / Municipio

## OBJETO
- Tributo(s): ...
- Esfera(s): federal / estadual / municipal
- Fatos geradores / competencias: ...
- Valor: originario + multa + juros/SELIC

## DOCUMENTOS (numerados)
- doc. 1 — auto de infracao (DD/MM/AAAA)
- doc. 2 — CDA n. ...
- doc. 3 — ...

## PRAZOS (com datas)
- Decadencia: vence DD/MM (CTN 173/150)
- Prescricao: vence DD/MM (CTN 174)
- Impugnacao / recurso / embargos: vence DD/MM

## FASE ATUAL
- (pre-lancamento / auto / contencioso adm / divida ativa / execucao / pos-transito)

## PECAS PRODUZIDAS
- AAAA-MM-DD - <Cliente> - <tipo>.txt

## DECISOES ESTRATEGICAS
- via escolhida, fundamento, data

## PROXIMOS PASSOS
- ...
```

## 2. ATUALIZACAO

Apos cada entrega: registrar a peca em PECAS, mover prazos cumpridos, anotar nova decisao em DECISOES, atualizar FASE e PROXIMOS PASSOS. Datas de prazos saem de `calculos-tributarios` (nao presumir — PA-05).

## 3. PASTAS DO CASO

Raiz configuravel **`<CASE_ROOT>/<slug>/`** (gravada no config como `CASE_ROOT`):
no Code = `<acervo>/Casos-Ativos`; FALLBACK (nuvem / sem acervo) = `tributario/casos/`.
Estrutura unificada, **compartilhada entre plugins do mesmo cliente**:

- `CASO.md` — estado vivo.
- `MEMORY.md` — decisoes e historico narrativo.
- `arquivos/` — documentos recebidos (auto, CDA, SPED, guias).
- `pecas/` — pecas produzidas (varios plugins gravam no mesmo `<slug>/pecas/`).

## 4. SIGILO (PA-12)

- Pasta **gitignored por default**; dados fiscais nunca entram no plugin distribuido (CTN 198 + LGPD).
- Se o workspace for pasta sincronizada (OneDrive/Google Drive/iCloud), alertar e manter a regra de editar so no mestre.

## 5. NOMENCLATURA E ENTREGA

- Arquivos novos: `AAAA-MM-DD - Cliente - tipo.ext` (ex.: `2026-06-16 - Fulano - excecao de pre-executividade.txt`).
- Entrega em **.txt** por padrao (economia de tokens); .docx/.pdf so a pedido.
- Documentos citados nas pecas por numero ("doc. N"), sem rol ao final (ver `estilo-juridico-tributario`).
