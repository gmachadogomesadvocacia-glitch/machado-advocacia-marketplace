---
name: memoria-de-caso-transito
description: >
  Memoria de caso de transito Tier 1 — Protocolo P3. Estrutura e mantem o CASO.md em
  transito/casos/<slug>/ (pasta gitignored, sigilo + LGPD). Registra cliente/polo, veiculo (placa,
  RENAVAM), auto (AIT, codigo, data/local, orgao), fase atual, pontuacao e situacao da CNH, documentos
  numerados "doc. N", prazos com datas (defesa previa, JARI, CETRAN), pecas produzidas, proximos passos e
  teses/estrategia. Atualiza apos cada entrega. Nomenclatura de arquivos AAAA-MM-DD - Cliente - tipo.ext e
  entrega em .txt. Ative ao abrir um caso novo, retomar caso, registrar documentos/prazos, atualizar o
  CASO.md ou no comando /caso-transito.
metadata:
  version: "0.1.0"
  area: "Direito de Transito"
  tier: 1
---

# MEMORIA DE CASO DE TRANSITO (P3)

> Tier 1. Operacionaliza o **Protocolo P3**. O **CASO.md** e o estado vivo do caso — fonte unica da verdade entre sessoes. Compartimentado por cliente, **gitignored** por default (sigilo OAB + LGPD — PA-12). Atualizado **apos cada entrega**.

---

## 1. ESTRUTURA DE PASTAS

```
transito/casos/<slug>/
  CASO.md          (estado vivo)
  MEMORY.md        (decisoes e historico — opcional)
  arquivos/        (AIT, NA, NP, fotos, afericao, CRLV, prontuario)
  pecas/           (produzidos: defesa, recursos, peticoes)
```
Alertar se `<cwd>` for pasta sincronizada (OneDrive/iCloud/Google Drive/Dropbox): dados de cliente nao devem espelhar sem ciencia (PA-12).

## 2. ESTRUTURA DO CASO.md

```
# CASO — <Cliente> / <slug>

## Cliente / polo
- Nome, contato; e condutor, proprietario ou ambos.

## Veiculo
- Placa, RENAVAM, marca/especie; EAR (atividade remunerada)?

## Auto de infracao
- AIT (numero), codigo CTB + descricao, natureza, data/hora/local, orgao autuador, equipamento (radar)?

## Fase atual
- autuacao | penalidade | JARI | CETRAN | judicial | suspensao | cassacao

## Pontuacao / CNH
- pontos nos 12 meses, gravissimas, limite aplicavel (20/30/40), situacao da CNH, suspensao/cassacao em curso.

## Documentos (numerados)
- doc. 1 — <descricao> (arquivos/<nome>)
- doc. 2 — ...

## Prazos (com datas)
- defesa previa: NA em DD/MM → vence DD/MM
- JARI: NP em DD/MM → vence DD/MM
- CETRAN: decisao JARI em DD/MM → vence DD/MM

## Pecas produzidas
- AAAA-MM-DD - <Cliente> - <tipo>.txt

## Teses / estrategia
- tese central, subsidiarias, instancia escolhida (de linha-estrategica-transito).

## Proximos passos
- [ ] ...
```

## 3. DOCUMENTOS NUMERADOS

- Numerar todo documento como **"doc. N"** e citar nas pecas por esse numero (estilo do escritorio).
- Manter a correspondencia doc. N ↔ arquivo em `arquivos/`.

## 4. NOMENCLATURA E ENTREGA

- Arquivos: **`AAAA-MM-DD - Cliente - tipo.ext`** (ex.: `2026-06-16 - Joao Silva - defesa previa.txt`).
- Entrega em **.txt** por padrao (economia de tokens); .docx/.pdf so a pedido.

## 5. CICLO DE ATUALIZACAO

1. Ao **abrir** caso: criar pasta + CASO.md (preencher do que ja se sabe).
2. Ao **receber documentos**: numerar doc. N, registrar prazos com datas.
3. Apos **cada entrega**: registrar a peca, mover prazos, atualizar proximos passos e a estrategia.
4. Ao **retomar**: ler o CASO.md antes de qualquer acao.

## 6. INTEGRACAO

- `analise-documental-transito` → alimenta documentos e dados-chave.
- `calculos-transito` → prazos e pontuacao.
- `linha-estrategica-transito` → grava a decisao estrategica.
- `/caso-transito` → abre/retoma; `/status-transito` → lista casos.

## 7. CHECKLIST DE SAIDA

- [ ] CASO.md criado/atualizado em transito/casos/<slug>/
- [ ] Polo, veiculo, auto, fase, pontuacao/CNH preenchidos
- [ ] Documentos numerados "doc. N" e mapeados aos arquivos
- [ ] Prazos com datas de vencimento (PA-05)
- [ ] Pecas e proximos passos atualizados
- [ ] Pasta gitignored; alerta de sincronizacao se aplicavel (PA-12)
