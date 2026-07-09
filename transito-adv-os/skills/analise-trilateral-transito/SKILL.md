---
name: analise-trilateral-transito
description: >
  Analise trilateral de transito Tier 1 — le o caso pelos 3 vertices antes de qualquer producao: (1) cliente/condutor (o que sustenta a defesa e os pontos fortes), (2) orgao autuador/administracao (a posicao mais provavel do Estado e a presuncao de legitimidade do auto), (3) julgador (JARI, CETRAN ou juizo — como o caso aparece para quem decide). Ative apos a triagem e a analise documental, antes de definir a linha estrategica ou redigir.
metadata:
  version: "0.1.0"
  area: "Direito de Transito"
  tier: 1
---

# ANALISE TRILATERAL DE TRANSITO

> Tier 1. Antes de produzir, ler o caso por **3 vertices**. Aqui a relacao e **assimetrica**: o Estado autua e carrega a presuncao de legitimidade do auto, mas tem o **onus** de comprovar a regularidade do procedimento (auto + dupla notificacao + afericao). O condutor ataca os vicios. O objetivo e antecipar a defesa do auto e calibrar a tese.

---

## 1. OS 3 VERTICES

**V1 — Cliente / condutor-proprietario**
- O que sustenta a defesa: vicios documentais, ausencia de notificacao, equipamento sem afericao, identificacao errada, fato inexistente.
- Pontos fortes e fragilidades da versao do cliente; coerencia com os documentos.

**V2 — Orgao autuador / administracao**
- A posicao provavel: presuncao de legitimidade e veracidade do auto; defesa da regularidade do procedimento.
- **Onus da administracao:** comprovar o auto valido (CTB 280), a **dupla notificacao** (NA + NP — Sum. 312) e, havendo equipamento, a **afericao** (INMETRO).
- Onde a administracao e forte (auto formalmente integro, AR juntado) e onde tende a falhar (NA fora do prazo, ausencia de afericao, motivacao generica).

**V3 — Julgador (JARI / CETRAN / juizo)**
- Como o caso aparece para quem decide: a JARI/CETRAN tende a presumir a regularidade; o juizo afere legalidade do ato.
- O que convence cada instancia: vicio formal demonstrado documentalmente pesa mais que alegacao generica.

## 2. ANTECIPACAO ADVERSARIAL

Para cada tese da defesa, escrever a **melhor resposta da administracao** e a **replica**:
```
TESE (defesa): ...
RESPOSTA PROVAVEL DA ADMINISTRACAO: ...
REPLICA / COMO NEUTRALIZAR: ...
PROVA QUE FECHA A QUESTAO: (AR, certidao de afericao, foto)
```

## 3. QUADRO DE FORCAS

```
        | FORCAS                 | FRAGILIDADES
--------|------------------------|---------------------
Cliente | ...                    | ...
Admin.  | presuncao de legit.    | onus: NA/NP, afericao
Julgador| tende a presumir reg.  | exige vicio demonstrado
```

## 4. SAIDA

```
V1 CLIENTE: pontos fortes / fragilidades
V2 ADMINISTRACAO: posicao provavel / onus nao cumprido
V3 JULGADOR: o que convence nesta instancia
ANTECIPACAO ADVERSARIAL: (tese → resposta → replica) x N
TESE MAIS RESISTENTE: ...
RISCO PRINCIPAL: ...
→ linha-estrategica-transito
```

## 5. INTEGRACAO

- Entra **apos** `triagem-transito` + `analise-documental-transito` + `analise-vicios-auto-infracao`.
- Usa `jurisprudencia-transito` (validacao — PA-01) e `calculos-transito` (prazos/pontos).
- Entrega para `linha-estrategica-transito` o quadro de forcas e a tese mais resistente.

## 6. CHECKLIST DE SAIDA

- [ ] Os 3 vertices analisados (cliente / administracao / julgador)
- [ ] Onus da administracao mapeado (auto, dupla notificacao, afericao)
- [ ] Antecipacao adversarial escrita para cada tese
- [ ] Quadro de forcas montado
- [ ] Coerencia de polo preservada — peca sempre pro cliente (PA-10)
- [ ] Sem fato/sumula inventados (PA-01/PA-03)
