---
name: memoria-de-caso-civel
description: >
  Memoria de caso civel Tier 1 — Protocolo P3. Cria e mantem o CASO.md compartimentado por cliente em
  civel/casos/<slug>/. Estrutura: partes e polo, relacao juridica/fato, numero do processo,
  vara/comarca, valor/quantum, datas (fato/contrato, inadimplemento/evento, citacao), documentos
  numerados "doc. N", prazos com datas (prescricao, recursos, contestacao), fase atual, pecas
  produzidas, proximos passos e estrategia. Atualiza apos cada entrega. Sigilo + LGPD (pasta gitignored).
  Nomenclatura AAAA-MM-DD - Cliente - tipo.ext e entrega em .txt por padrao. Ative quando o usuario abrir
  caso novo, retomar caso, pedir CASO.md, memoria do caso, /caso-civel, ou ao final de cada producao para
  registrar o estado.
metadata:
  version: "0.1.0"
  area: "Direito Civil e Processo Civil"
  tier: 1
---

# MEMORIA DE CASO CIVEL

> Tier 1 (invariante). Operacionaliza **P3 — Memoria de Caso**. O `CASO.md` e o estado vivo e a fonte da verdade do caso. Compartimentado por cliente, **gitignored** (sigilo OAB + LGPD — PA-12). Atualizar apos **cada** entrega.

---

## 1. ESTRUTURA DE PASTAS

```
civel/casos/<slug>/
  CASO.md       — estado vivo
  MEMORY.md     — decisoes e historico
  arquivos/     — documentos do cliente (doc. N)
  pecas/        — produzidos (.txt por padrao)
```
- `novo <slug>` cria; `<slug>` retoma; `list` lista; `arquivar <slug>` encerra.
- Alertar se `<cwd>` for pasta sincronizada (OneDrive/iCloud/Google Drive) — dados de cliente nao devem vazar.

## 2. ESTRUTURA DO CASO.md

```
# CASO — <Cliente> x <Adverso>

## PARTES E POLO
- Cliente: <nome/qualif> — POLO: autor (credor/lesado) / reu (devedor/causador)
- Adverso: <nome/qualif>

## RELACAO JURIDICA / FATO
- Contrato? tipo, data. / Ato ilicito? dano, nexo. / Titulo? cheque/NP/duplicata.
- Regime: contratual / extracontratual (PA-07)

## PROCESSO
- Numero: ____  Vara/Comarca: ____  Foro (CPC __): ____

## VALOR / QUANTUM
- Principal: R$ ____  Material (emergente+cessante): R$ ____  Moral/estetico: R$ ____

## DATAS-CHAVE
- Fato/contrato: DD/MM/AAAA
- Inadimplemento / evento danoso: DD/MM/AAAA
- Notificacao: DD/MM/AAAA   Citacao: DD/MM/AAAA

## DOCUMENTOS (numerados)
- doc. 1 — <tipo> — <data>
- doc. 2 — ...

## PRAZOS (com datas)
- Prescricao/decadencia: prazo __ — inicio DD/MM — VENCE DD/MM (PA-05)
- Contestacao: 15 dias uteis — vence DD/MM
- Recurso: __ dias — vence DD/MM

## FASE ATUAL
- <triagem / analise / producao / protocolado / recurso>

## PECAS PRODUZIDAS
- AAAA-MM-DD - <Cliente> - <tipo>.txt

## ESTRATEGIA
- Via, pedido, tese central (de linha-estrategica-civel)

## PROXIMOS PASSOS
- [ ] ...
```

## 3. ATUALIZACAO

Apos cada entrega: registrar a peca em PECAS, mover datas/prazos, atualizar FASE e PROXIMOS PASSOS. Anotar decisoes em `MEMORY.md`.

## 4. NOMENCLATURA E ENTREGA

- Arquivos: `AAAA-MM-DD - Cliente - tipo da peca.ext` (ex.: `2026-06-16 - Fulano - peticao inicial cobranca.txt`).
- Entregar em **.txt** por padrao (economia de tokens); .docx/.pdf so a pedido.
- Documentos do processo citados na peca como **"doc. N"**.

## 5. ALERTAS

- Pasta de caso sempre **gitignored**; nunca versionar dado de cliente (PA-12, LGPD).
- Datas e valores so de documento (PA-03) — espelham `analise-documental-civel`.
- Conferir e manter visivel o **prazo prescricional** (PA-05) no topo dos PRAZOS.
- Coerencia de polo (PA-10): o CASO.md fixa autor x reu para todas as pecas.
