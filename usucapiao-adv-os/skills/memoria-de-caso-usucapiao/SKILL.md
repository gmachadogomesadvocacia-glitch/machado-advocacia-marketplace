---
name: memoria-de-caso-usucapiao
description: >
  MEMORIA DE CASO USUCAPIAO — Skill Tier 1 invariante (Protocolo P3). Gerencia o CASO.md (estado vivo)
  e o MEMORY.md (decisoes) compartimentados por cliente em `<cwd>/usucapiao/casos/<slug>/`. Opera o
  PA-12 (sigilo OAB + LGPD): pasta gitignored, alerta se o workspace for sincronizado (OneDrive/iCloud/
  Google Drive/Dropbox). Suporta novo, retomar, listar e arquivar. Acione ao abrir caso novo, retomar
  caso, atualizar o CASO.md, registrar decisao, ou ao fim de cada fase do pipeline. Gatilhos: novo caso
  usucapiao, abrir caso, retomar caso, CASO.md, memoria do caso, listar casos, arquivar caso.
metadata:
  version: "0.1.0"
  area: "Usucapiao (Judicial e Extrajudicial)"
  tier: 1
---

# MEMORIA DE CASO USUCAPIAO (P3)

> Skill **Tier 1** invariante. Mantem o **CASO.md** (estado vivo) e o **MEMORY.md** (decisoes/historico) de cada cliente, compartimentados. Operacionaliza **PA-12** (sigilo OAB + LGPD). Atualizada ao fim de cada fase.

---

## 0. COMPARTIMENTACAO + SIGILO (PA-12)
- Um caso = uma pasta: `<cwd>/usucapiao/casos/<slug>/` com `CASO.md`, `MEMORY.md`, `arquivos/`, `pecas/`.
- **Nunca** misturar dados de clientes distintos (vazamento entre casos = PA-12).
- Pasta `casos/` **gitignored** por default. Se o workspace estiver em pasta **sincronizada** (OneDrive/iCloud/Google Drive/Dropbox), **alertar** o operador (dado de cliente sai da maquina — sigilo OAB + LGPD).

## 1. OPERACOES
- **novo `<slug>`** — cria a pasta e os arquivos a partir de `templates/CASO.md.tpl` e `templates/MEMORY-caso.md.tpl`. Slug = nome curto do cliente/imovel (sem espacos/acentos).
- **`<slug>` (retomar)** — le `CASO.md` + `MEMORY.md` e devolve o estado atual e o proximo passo.
- **listar** — enumera as pastas em `usucapiao/casos/`.
- **arquivar `<slug>`** — move para `usucapiao/casos/_arquivados/` (mantem sigilo).

## 2. ESTRUTURA DO CASO.md
```
# CASO — [cliente] · [slug]
- Polo: [usucapiente / confrontante]
- Via: [judicial / extrajudicial]
- Modalidade: [extraordinaria / ordinaria / especial urbana / rural / familiar / coletiva]
## Imovel
- Urbano/rural · matricula nº [..] OU sem registro · metragem [..] · confrontantes [..]
## Posse
- Inicio [data] · tempo [..] · qualidade (mansa/pacifica/continua/ininterrupta/animus domini)
- Justo titulo? boa-fe? · detencao descartada? (PA-09)
## Entes a citar / anuir
- Titulares · confrontantes · Uniao/Estado/Municipio · reus incertos (edital) · MP se cabivel
## Foro / RI
- [foro da situacao do imovel] OU [RI da circunscricao]
## Prazos
- [..]
## Estado
- Fase atual · Selo P1 [sim/nao] · ultima atualizacao
```

## 3. ESTRUTURA DO MEMORY.md
Registro append-only de **decisoes** (via, modalidade, teses escolhidas, riscos aceitos), com data e motivo. Cada decisao da `linha-estrategica-usucapiao` entra aqui.

## 4. CICLO DE ATUALIZACAO
- Abertura: criada na **triagem-usucapiao**.
- Atualizar ao fim de **cada fase**: pos-Selo P1, pos-analise de posse/documental, pos-linha estrategica, pos-producao, pos-revisao R1-R4.
- Nunca inventar dado faltante → `[INFORMAR]` (PA-03).

## 5. CHECKLIST
- [ ] Pasta `<cwd>/usucapiao/casos/<slug>/` correta · sem mistura de clientes (PA-12)
- [ ] Gitignore verificado · alerta de pasta sincronizada emitido se for o caso
- [ ] CASO.md com polo/via/modalidade/imovel/posse/entes/foro/prazos
- [ ] MEMORY.md com as decisoes datadas

## 6. ENCERRAMENTO
Entrega o CASO.md atualizado e o MEMORY.md com as decisoes, prontos para a proxima fase. Toda producao termina em `revisao-final-usucapiao` (PA-13).
