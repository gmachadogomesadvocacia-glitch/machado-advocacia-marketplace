---
name: triagem-consumidor
description: >
  TRIAGEM CONSUMIDOR — Skill Tier 1, porta de entrada de toda demanda consumerista/bancaria.
  Executa a triagem 4D (polo x eixo x esfera x rito), identifica a relacao de consumo e o polo do
  cliente, abre ou atualiza o CASO.md e sugere as proximas skills. Acione quando chegar um caso novo
  de consumidor, quando o usuario pedir para classificar/enquadrar uma demanda, abrir caso, ou antes
  de qualquer producao quando o CASO.md ainda nao existe. Gatilhos: novo caso, cliente novo, analisar
  demanda, qual a via, JEC ou vara comum, e qualquer relato de cobranca, negativacao, revisional,
  voo, produto com defeito, conta de luz/telefone, compra online, divida, plano de pagamento.
metadata:
  version: "0.1.0"
  area: "Direito do Consumidor e Bancario"
  tier: 1
---

# TRIAGEM CONSUMIDOR

> Skill **Tier 1** — porta de entrada. Classifica o caso em 4 dimensoes, le/pergunta o polo, abre o `CASO.md` e roteia. Nenhuma producao comeca sem passar por aqui (e pelo Selo P1).

---

## 0. QUANDO ACIONAR

Toda demanda nova; sempre que o `CASO.md` nao existir; quando o usuario pede enquadramento, escolha de via ou abertura de caso. Consultas rapidas e pontuais dispensam a triagem completa (mas ainda exigem identificar o polo antes de qualquer peca).

## 1. PRE-CHECK

1. Procurar `consumidor/cowork-state.json` (subir a arvore). Ausente → sugerir `/start-consumidor`; se o operador declinar, seguir em modo fallback.
2. Procurar `CASO.md` do cliente em `consumidor/casos/<slug>/`. Existe → leia antes de tudo. Nao existe → criar ao fim desta triagem (via `memoria-de-caso-consumidor`).

---

## 2. A TRIAGEM 4D

Classifique o caso nas 4 dimensoes simultaneas e registre cada uma:

### Dimensao 1 — POLO (variavel-mae)
- **Consumidor** — destinatario final, vulneravel (autor).
- **Fornecedor** — banco, financeira, loja, operadora, cia aerea, prestador (defesa).

> Verifique a **relacao de consumo** (PA-04): destinatario final + vulnerabilidade (art. 2/3 CDC, finalista mitigada). Se for insumo da cadeia produtiva (PJ-PJ), justifique a vulnerabilidade ou afaste o CDC (PA-16). **Sem polo definido, pare e pergunte** — produzir contra o polo do cliente e violacao nuclear (PA-05).

### Dimensao 2 — EIXO
bancario/financeiro · negativacao · telecom · servicos-essenciais · aereo · vicio-fato-produto · e-commerce · publicidade · clausula-abusiva · cobranca-indevida · superendividamento · consumo-imobiliario. (Pode haver mais de um.)

### Dimensao 3 — ESFERA
- **Judicial** — acao perante JEC ou vara comum.
- **Administrativa** — PROCON, consumidor.gov.br, BACEN, ANATEL, ANAC, agencia.
- **Extrajudicial** — notificacao, negociacao direta, acordo.

> Esferas podem correr em **paralelo** (ex.: reclamacao no BACEN + acao judicial). Coordene pelo **Protocolo P4 (Cruzamento Judicial-Administrativo)** — a via administrativa vira prova; nunca produza teses contraditorias entre as frentes.

### Dimensao 4 — RITO
- **JEC** (Lei 9.099) — ate 40 SM; ate 20 SM dispensa advogado; rito rapido.
- **Vara civel comum** — acima de 40 SM, prova pericial complexa, ou estrategia.
- **Acao coletiva** — interesse coletivo/difuso (legitimados do art. 82 CDC).

> Decisao de rito e do **Protocolo P5** (Localizacao e Rito). Competencia: foro do domicilio do consumidor (art. 101, I CDC).

---

## 3. CHECKPOINT 1

Apresente ao advogado o enquadramento e confirme antes de prosseguir:

```
ENQUADRAMENTO 4D
- Polo:   [consumidor | fornecedor]
- Eixo:   [...]
- Esfera: [judicial | administrativa | extrajudicial] (+ paralelas?)
- Rito:   [JEC | vara comum | coletiva]
- Tarefa: [inicial | contestacao | tutela | calculo | reclamacao adm. | acordo | parecer]
- Urgencia: [sim/nao] (corte de servico, negativacao a remover, bloqueio?)
- Documentos essenciais presentes? [contrato, fatura, extrato, print, protocolo, negativacao]
```

Faltando dado essencial → sinalizar Ponto de Omissao `[INFORMAR]`, nunca inventar (PA-03).

---

## 4. GRAVAR NO CASO.md

Acione `memoria-de-caso-consumidor` para criar/atualizar o `CASO.md` com: polo, eixo(s), esfera, rito, partes, localizacao/foro, prazos (decadencia art. 26 / prescricao art. 27 / arrependimento art. 49), documentos e status do Selo P1.

---

## 5. ROTEAMENTO (sugerir proximas skills)

| Enquadramento | Proxima(s) skill(s) |
|---------------|---------------------|
| Insumos sempre | `validador-legislacao-consumidor` (Selo P1) → `analise-documental` + `analise-contratual` |
| Estrategia | `analise-trilateral-consumidor` → `jurisprudencia-consumidor` → `linha-estrategica-consumidor` |
| Bancario (consumidor) | `revisional-bancaria` · `acao-repeticao-indebito` · `acao-negativacao-indevida` · `calculos-consumidor` |
| Bancario (fornecedor) | `defesa-instituicao-financeira` · `defesa-busca-apreensao` |
| Negativacao | `acao-negativacao-indevida` · `tutela-urgencia-consumidor` |
| Telecom/energia/aereo | `acao-telecom-servicos` · `acao-transporte-aereo` · `reclamacao-administrativa` |
| Produto/servico | `acao-vicio-fato-produto` |
| Superendividamento | `acao-superendividamento` |
| Publicidade/clausula | `acao-publicidade-abusiva` · `analise-contratual-consumidor` |
| Fornecedor (geral) | `contestacao-consumidor` |
| Administrativo | `reclamacao-administrativa` |
| JEC | `peticao-jec` |

> Toda peca produzida passa pela `revisao-final-consumidor` (R1-R4) antes da entrega (PA-22).

---

## 6. ENCERRAMENTO

A triagem entrega: as 4 dimensoes definidas, o polo travado, o CASO.md aberto e o roteiro de skills. Nunca avance para producao sem o **Selo de Validacao Legal Previa** (P1) emitido pelo `validador-legislacao-consumidor`.
