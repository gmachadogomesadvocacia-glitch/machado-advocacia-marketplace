---
name: memoria-de-caso-isencao-ir
description: >
  MEMORIA DE CASO ISENCAO-IR — Skill Tier 1 invariante (Protocolo P3). Gerencia o CASO.md (estado vivo)
  e o MEMORY.md (decisoes) compartimentados por cliente em `<cwd>/isencao-ir/casos/<slug>/`.
  Operacionaliza a PA-10: dado de SAUDE e SENSIVEL (LGPD art. 11 + sigilo) — pasta gitignored e ALERTA
  AGRESSIVO se o workspace for sincronizado (OneDrive/iCloud/Drive/Dropbox). Suporta novo/retomar/listar/
  arquivar. Acione ao abrir caso, retomar caso, atualizar o CASO.md, registrar decisao, ou ao fim de cada
  fase. Gatilhos: novo caso de isencao, abrir CASO.md, memoria do caso, retomar caso, /caso-isencao-ir.
metadata:
  version: "0.1.0"
  area: "Isencao de IRPF por Doenca Grave"
  tier: 1
---

# MEMORIA DE CASO ISENCAO-IR

> Skill **Tier 1** invariante (Protocolo P3). Mantem o estado vivo de cada cliente em pasta compartimentada e **gitignored**. Operacionaliza a **PA-10**: dado de saude (doenca/CID) e SENSIVEL — LGPD art. 11 + sigilo. Nenhum dado de cliente persiste no plugin distribuido.

---

## 0. LOCALIZACAO E COMPARTIMENTACAO
- Raiz: `<cwd>/isencao-ir/casos/<slug>/` — um diretorio por cliente, **isolado** (nunca misturar clientes).
- `<slug>` = nome do cliente em minusculas-com-hifen (ex.: `maria-souza`).
- Conteudo de cada caso:
  - `CASO.md` — estado vivo (secao 3).
  - `MEMORY.md` — decisoes e historico (secao 4).
  - `arquivos/` — laudo, carta de concessao, informes de rendimento, comprovantes de IR retido, DIRPF.
  - `pecas/` — documentos produzidos (requerimento, acao, MS, retificadora).

## 1. PROTECAO DO DADO DE SAUDE (PA-10) — INVARIANTE
- A pasta `isencao-ir/casos/` deve estar **gitignored** por padrao. Garantir entrada em `.gitignore`; se ausente, criar.
- **ALERTA AGRESSIVO:** se o `<cwd>` estiver dentro de pasta sincronizada (caminho contendo `OneDrive`, `iCloud`, `Google Drive`/`GoogleDrive`, `Dropbox`), AVISAR de forma destacada que ha dado de saude SENSIVEL (LGPD art. 11) sendo gravado em nuvem e pedir confirmacao/realocacao antes de persistir.
- Nunca expor CID/diagnostico em nomes de arquivo ou em logs. **Nao opinar sobre o diagnostico** (PA-04).

## 2. OPERACOES
- **novo `<slug>`** — cria a estrutura, instancia `CASO.md` e `MEMORY.md` pelos templates (secoes 3/4), roda o alerta da secao 1.
- **`<slug>` (retomar)** — le e exibe o resumo do `CASO.md`; aponta a fase atual e o proximo passo do pipeline.
- **listar** — lista os `<slug>` existentes em `isencao-ir/casos/` (sem expor CID).
- **arquivar `<slug>`** — marca o `CASO.md` como ARQUIVADO (data) e move para `casos/_arquivados/`.

## 3. TEMPLATE — CASO.md (estado vivo)
```
# CASO — {{CLIENTE}}  (slug: {{slug}})
Status: ATIVO | Atualizado: {{AAAA-MM-DD}}
- Polo: contribuinte/beneficiario
- Doenca / CID / data do laudo: [doenca do rol] · [CID] · [data]
- Fonte pagadora: [INSS / RPPS / fundo de pensao EFPC / ex-empregador]
- Tipo de provento: [aposentadoria / pensao / reforma / complementacao]
- Periodo de retencao indevida: desde [data]
- Valor retido (estimado): [R$ ...]
- Via: [administrativa / judicial / ambas]
- Prazos: restituicao = ultimos 5 anos (CTN art. 168 — PA-09) · MS = 120 dias (se aplicavel)
- Selo P1: [emitido? sim-nao / data]
- Fase atual: [triagem / documental / estrategia / producao / revisao / entregue]
- Proximo passo: [...]
- Documentos: [laudo · carta de concessao · informes/IR retido · DIRPF]
```
> Faltando dado essencial → `[INFORMAR]`, nunca inventar (PA-03).

## 4. TEMPLATE — MEMORY.md (decisoes)
```
# MEMORY — {{CLIENTE}}
## Decisoes
- {{AAAA-MM-DD}} — [decisao + razao]
## Ressalvas da Suprema Corte (R1-R4)
- [...]
## Historico de fases
- [...]
```

## 5. ATUALIZACAO POR FASE
Ao fim de **cada fase** do pipeline (triagem, documental, estrategia, producao, revisao), atualizar `CASO.md` (fase atual + proximo passo) e registrar decisoes/ressalvas no `MEMORY.md`. A `revisao-final-isencao-ir` grava aqui suas ressalvas (PA-14).

## 6. ENCERRAMENTO
Entrega o caso compartimentado, gitignored e protegido (PA-10), com `CASO.md`/`MEMORY.md` atualizados e o proximo passo claro. E a fonte da verdade do estado do caso.
