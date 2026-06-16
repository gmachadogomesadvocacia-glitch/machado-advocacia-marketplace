---
name: analise-posse-usucapiao
description: >
  ANALISE POSSE USUCAPIAO — Skill Tier 1 (Protocolo P4), o coracao do plugin. Verifica a POSSE ad
  usucapionem e DEFINE a MODALIDADE cabivel. Checa tempo de posse (com accessio possessionis), qualidade
  (mansa, pacifica, continua, ininterrupta, com animus domini), a distincao POSSE x DETENCAO
  (comodatario/locatario/permissionario nao usucapem), justo titulo + boa-fe (ordinaria), metragem e
  destinacao (250 m2 urbana / 50 ha rural / moradia) e o requisito de nao ser proprietario de outro
  imovel (especiais). Acione quando o usuario pedir para analisar a posse, definir a modalidade, saber
  qual usucapiao cabe, conferir tempo/metragem/animus domini, ou distinguir posse de detencao.
metadata:
  version: "0.1.0"
  area: "Usucapiao (Judicial e Extrajudicial)"
  tier: 1
---

# ANALISE POSSE USUCAPIAO (P4) — o coracao

> Skill **Tier 1** — operacionaliza o Protocolo P4. Verifica a posse ad usucapionem e **define a modalidade**. Tudo a jusante (estrategia, peca) depende daqui. Roda apos a analise documental.

---

## 0. PRE-CHECK
- Caso triado + documentos inventariados (`analise-documental-usucapiao`).
- Nada inventado sobre tempo/metragem/atos possessorios (PA-03). Bem publico → nao usucape (PA-04).

## 1. TEMPO DE POSSE
- Quanto tempo o cliente possui? Desde quando, comprovado por quais docs ("doc. N")?
- **Accessio possessionis** (CC art. 1.243): soma das posses dos **antecessores** (sucessao/contrato) para completar o prazo — verificar a cadeia sem lacunas.

## 2. QUALIDADE DA POSSE (PA-08)
Posse ad usucapionem = **mansa, pacifica, continua, ininterrupta**, com **animus domini** (possuir como dono). Houve oposicao judicial/extrajudicial, esbulho repelido, ou interrupcao? → quebra a continuidade e zera/suspende o prazo.

## 3. POSSE x DETENCAO (PA-09) — filtro eliminatorio
**Detentor nao usucape.** Quem tem a coisa por relacao de dependencia ou permissao **nao** tem posse ad usucapionem:
- **comodatario, locatario, permissionario, caseiro, servidor da posse** — detem em nome alheio, sem animus domini.
- Se a origem e detencao, so usucape se houver **interversao** comprovada do titulo (mudanca inequivoca para posse propria, oponivel ao antigo possuidor). Sem isso → **nao cabe usucapiao**, sinaliza e para.

## 4. MODALIDADE (a definicao final e aqui)
| Modalidade | Base | Tempo | Requisitos |
|-----------|------|-------|-----------|
| Extraordinaria | CC 1.238 | 15 (10 c/ moradia/obra) | dispensa justo titulo e boa-fe (**Sum. 391 STF** — `[VERIFICAR]`) |
| Ordinaria | CC 1.242 | 10 (5 qualificada) | **justo titulo + boa-fe** |
| Especial urbana | CC 1.240 / CF 183 | 5 | ate **250 m2** · moradia · **nao ter outro imovel** |
| Especial rural | CC 1.239 / CF 191 | 5 | ate **50 ha** · moradia + produtividade · nao ter outro imovel |
| Familiar | CC 1.240-A | **2** | ex-conjuge/companheiro que abandonou o lar; ate 250 m2 |
| Coletiva | L10.257 art. 10 | 5 | nucleo urbano informal, baixa renda |

- **Justo titulo + boa-fe** so importam para a **ordinaria**; verificar titulo habil (ainda que com vicio) e boa-fe.
- **Metragem e destinacao:** medir contra o teto (250 m2 / 50 ha) e a exigencia de **moradia/produtividade** nas especiais.
- **Nao ser proprietario de outro imovel:** requisito das especiais (urbana/rural/familiar) — confirmar com o cliente.

> Errar a modalidade ou seus requisitos e violacao (**PA-05**). Pode caber **mais de uma** modalidade — apontar a principal e as subsidiarias.

## 5. SAIDA
```
ANALISE DE POSSE
- Tempo: [anos · desde · accessio? quem]
- Qualidade: [mansa/pacifica/continua? · animus domini? · interrupcao/oposicao?]
- Posse x detencao: [posse propria / detencao + interversao? / NAO CABE]
- Metragem/destinacao: [m2 ou ha · moradia/produtividade?]
- Outro imovel? [sim/nao]
- MODALIDADE(S) cabivel(eis): [principal + subsidiarias]
- Requisitos ATENDIDOS / FALTANTES: [...]
- Tempo necessario x cumprido: [...]
```

## 6. ENCERRAMENTO
Entrega a posse qualificada e a **modalidade definida** com requisitos atendidos/faltantes. Jurisprudencia citada vai validada por `jurisprudencia-usucapiao` (Selo P1). Alimenta `analise-trilateral-usucapiao` e a producao; toda peca termina em `revisao-final-usucapiao`.
