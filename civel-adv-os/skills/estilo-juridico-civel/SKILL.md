---
name: estilo-juridico-civel
description: >
  Estilo juridico civel Tier 1 — Camada 3. Define o estilo das pecas civeis: enxuto, tecnico, objetivo.
  Estrutura padrao (enderecamento, qualificacao das partes, dos fatos, do direito, dos pedidos, valor da
  causa, requerimento de provas). Documentos numerados "doc. N" e citados por numero. Linguagem civil
  correta — nao confundir prescricao/decadencia, responsabilidade contratual/extracontratual, dano
  emergente/lucro cessante, nulidade/anulabilidade. Tom {{TOM_VOZ_PERFIL}} intensidade
  {{TOM_VOZ_INTENSIDADE}}/10, combatividade dirigida a teses e nunca a pessoas. Ative ao redigir ou
  revisar a forma de qualquer peca civel, ou quando o usuario pedir para ajustar o estilo, o tom ou a
  estrutura da peca.
metadata:
  version: "0.1.0"
  area: "Direito Civil e Processo Civil"
  tier: 1
---

# ESTILO JURIDICO CIVEL

> Tier 1 — **Camada 3**. Padroniza a forma de toda peca civel. Peca curta, tecnica e objetiva; combatividade dirigida a **teses**, nunca a pessoas. Aplica-se a toda producao antes da `revisao-final-civel`.

---

## 1. PRINCIPIOS DE REDACAO

- **Enxuto:** ~5 paginas quando o caso permitir; um argumento por paragrafo; sem citacao decorativa.
- **Tecnico e objetivo:** afirmar e fundamentar; evitar adjetivacao vazia e retorica.
- **Antecipacao adversarial:** rebater a tese adversa mais forte dentro do "Do Direito".
- **Tom:** {{TOM_VOZ_PERFIL}}, intensidade {{TOM_VOZ_INTENSIDADE}}/10.

## 2. ESTRUTURA PADRAO (peca de conhecimento)

1. **Enderecamento** — juizo/vara competente (CPC 46/53; foro de eleicao valido).
2. **Qualificacao das partes** — autor e reu (CPC 319, II).
3. **Dos Fatos** — narrativa cronologica, ancorada nos documentos ("conforme doc. N").
4. **Do Direito** — fundamento legal (CC/CPC vigentes — PA-02/PA-04) + jurisprudencia **validada** (PA-01); regime correto (contratual x extracontratual — PA-07).
5. **Dos Pedidos** — claros, determinados, na ordem; cumulacao compativel (CPC 327); tutela se cabivel.
6. **Valor da causa** (CPC 292).
7. **Das Provas / Requerimentos** — protesto por provas, citacao do reu.
8. Local, data, advogado, OAB.

> Adaptar para defesa (contestacao — preliminares CPC 337, merito, impugnacao especificada), monitoria, execucao.

## 3. DOCUMENTOS

- Numerar os documentos como **"doc. N"** e cita-los **pelo numero** no corpo ("conforme doc. 3").
- Anexar na ordem citada; espelhar o inventario de `analise-documental-civel`/`CASO.md`.

## 4. LINGUAGEM CIVIL CORRETA (nao confundir)

| Nao confundir | Distincao |
|---------------|-----------|
| **Prescricao x decadencia** | pretensao (CC 205/206) x direito potestativo (CC 178) — PA-05 |
| **Contratual x extracontratual** | regimes, onus e prazos distintos; muda o termo dos juros — PA-07 |
| **Dano emergente x lucro cessante** | o que se perdeu x o que se deixou de ganhar (CC 402) |
| **Nulidade x anulabilidade** | vicio insanavel/de oficio (CC 166) x sanavel/a requerimento (CC 171) |
| **Mora x inadimplemento absoluto** | atraso ainda util x prestacao inutil |
| **Juros x correcao** | remuneram a mora x recompoem o valor |

## 5. IDENTIDADE NA ASSINATURA

```
{{CIDADE}}/{{UF}}, <data>.
{{ADVOGADO_NOME}}
OAB/{{OAB_UF}} {{OAB_NUMERO}}
{{FIRM_NAME}} — {{EMAIL}}
```

## 6. ENTREGA

- Saida em **.txt** por padrao (economia de tokens); .docx/.pdf so a pedido.
- Nomear `AAAA-MM-DD - Cliente - tipo.ext` (ver `memoria-de-caso-civel`).
- Gatilho "gera docx": converter .txt em .docx timbrado via `gerador-peticoes` — Code.

## 7. ALERTAS

- Coerencia de polo (PA-10): toda a peca fala pelo lado do cliente.
- Nao citar lei/sumula sem validar (PA-01/PA-02); norma vigente no fato (PA-04).
- Pedido coerente com a via (PA-08); nada de fato sem prova (PA-03).
- Materia de outro plugin → nao redigir, rotear (PA-09). Depois da redacao: `revisao-final-civel` (PA-13).
