---
name: memoria-de-caso-imobiliario
description: >
  Memoria de caso imobiliario Tier 1 — Protocolo P3. Cria e mantem o CASO.md compartimentado por
  cliente: partes e polo, imovel (matricula, endereco, area), contrato (tipo, data, garantia), fatos e
  datas, documentos numerados "doc. N", prazos com datas (decadencia da renovatoria, purgacao da mora,
  fases da alienacao fiduciaria), fase atual, pecas produzidas, proximos passos e decisoes
  estrategicas. Pasta de caso gitignored por sigilo (PA-12 / LGPD). Nomenclatura de arquivos
  "AAAA-MM-DD - Cliente - tipo.ext" e entrega em .txt. Atualizar apos cada entrega. Ative ao abrir,
  retomar ou listar caso, ao registrar documento/prazo, ou no comando /caso-imobiliario.
metadata:
  version: "0.1.0"
  area: "Direito Imobiliario e Locacao"
  tier: 1
---

# MEMORIA DE CASO IMOBILIARIO

> Tier 1. **Protocolo P3.** O CASO.md e o estado vivo do caso. Compartimentado por cliente, **gitignored** (sigilo OAB + LGPD — PA-12). Atualizar **apos cada entrega**.

---

## 0. PASTA UNIFICADA DO CASO

Cada caso vive em **`<CASE_ROOT>/<slug>/`** — pasta **UNIFICADA e compartilhada** entre os plugins Adv-OS do mesmo cliente. Estrutura:

```
<CASE_ROOT>/<slug>/
├── CASO.md        # estado vivo (esta skill)
├── MEMORY.md      # decisoes e historico
├── arquivos/      # documentos recebidos (matricula, contrato, certidoes)
└── pecas/         # produzidos — toda peca vai em <slug>/pecas/
```

- **CASE_ROOT** = `{{CASE_ROOT}}` (lido do config). No **Code** com acervo configurado: `<acervo>/Casos-Ativos`. **Fallback** (Cowork ou sem acervo): `<COWORK>/imobiliario/casos`.
- O estado interno do plugin (`cowork-state.json`) NAO muda — fica em `<COWORK>/imobiliario/`.

---

## 1. ESTRUTURA DO CASO.md

```
# CASO — <Cliente>

## PARTES E POLO
- Cliente: <nome> — polo: locador/locatario | comprador/vendedor | possuidor/esbulhador | condominio/condomino | fiduciante/credor
- Parte adversa: <nome>

## IMOVEL
- Endereco: ...
- Matricula: <no> / <cartorio>
- Area: ...  | Urbano/Rural: ...
- Onus reais: ...

## CONTRATO
- Tipo: locacao / promessa / compra e venda
- Data de celebracao: DD/MM/AAAA  (define a norma — PA-04)
- Valor / indice de reajuste: ...
- Garantia: <unica> (cumulada? S/N — PA-08)

## FATOS E DATAS
- DD/MM — <fato>

## DOCUMENTOS
- doc.1 — <tipo> (DD/MM)
- doc.2 — ...

## PRAZOS
| Prazo | Vence em | Fonte |
|-------|----------|-------|
| Decadencia renovatoria | DD/MM | art. 51 §5º |
| Purgacao da mora | DD/MM | art. 62 |
| Fase fiduciaria (consolidacao/leilao) | DD/MM | art. 26-27 Lei 9.514 |

## FASE ATUAL
...

## PECAS PRODUZIDAS
- AAAA-MM-DD - <Cliente> - <tipo>.txt

## PROXIMOS PASSOS
...

## DECISOES ESTRATEGICAS
- <data> — <decisao + motivo>
```

## 2. REGRAS

- **Numerar documentos "doc. N"** uma unica vez; as pecas citam pelo numero.
- **Datar tudo** — prazos decadenciais (renovatoria), purgacao e fases da fiduciaria sao fatais.
- Registrar a **norma vigente** na data do contrato/fato (PA-04).
- Nao copiar dados sensiveis para fora da pasta do caso (PA-12).

## 3. NOMENCLATURA E ENTREGA

- Arquivos: **`AAAA-MM-DD - Cliente - tipo da peca.ext`**.
- Entrega padrao em **.txt** (nao gerar .docx/.pdf salvo pedido); pecas gravadas em `<slug>/pecas/`.
- Pasta do caso gitignored; alertar se o workspace for pasta sincronizada (OneDrive/Drive/iCloud).

## 4. OPERACOES

| Acao | Efeito |
|------|--------|
| Abrir caso | criar `<CASE_ROOT>/<slug>/` (CASO.md + MEMORY.md + arquivos/ + pecas/) |
| Retomar | ler o CASO.md e situar a fase |
| Listar | enumerar casos existentes |
| Atualizar | apos cada entrega: nova peca, novo doc, novo prazo, decisao |

## 5. SAIDA

Confirmar caminho do CASO.md, fase atual e o **proximo prazo critico** com data. Toda producao do pipeline le e atualiza este arquivo.
