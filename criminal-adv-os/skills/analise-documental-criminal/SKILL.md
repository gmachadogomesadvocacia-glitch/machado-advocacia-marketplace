---
name: analise-documental-criminal
description: >
  Analise documental criminal Tier 1 — Protocolo P2. Checklist de integridade dos autos penais:
  inquerito policial (portaria, oitivas, indiciamento), auto de prisao em flagrante (APF), boletim de
  ocorrencia, denuncia/queixa (aptidao — CPP 41; inepcia), laudos periciais (local, IML/necropsia,
  toxicologico, balistico, exame de corpo de delito — CPP 158), FAC/antecedentes/certidoes,
  interceptacoes e quebras (legalidade), decisoes e sentenca, guia de execucao. Extrai tipificacao,
  materialidade, autoria e verifica a cadeia de custodia (CPP 158-A). Marca lacunas, nulidades e provas
  ilicitas. Ative para analisar autos, IP, BO, laudos, FAC, denuncia ou apos a triagem.
metadata:
  version: "0.1.0"
  area: "Direito Penal e Processo Penal"
  tier: 1
---

# ANALISE DOCUMENTAL CRIMINAL (Protocolo P2)

> Tier 1. Segundo passo, apos a triagem. Verifica a **integridade dos autos**, extrai os elementos do crime e mapeia **lacunas e ilicitudes**. Nada de merito se produz sem este checklist. Side-aware (defesa x assistencia).

---

## 1. CHECKLIST DE INTEGRIDADE DOS AUTOS

| Peca | Conferir |
|------|----------|
| **Inquerito policial** | Portaria de instauracao; oitivas (vitima, testemunhas, indiciado); indiciamento fundamentado; relatorio final |
| **APF** (auto de prisao em flagrante) | Comunicacao ao juiz em 24h (CPP 306); nota de culpa; especie de flagrante (proprio/improprio/presumido); audiencia de custodia |
| **Boletim de ocorrencia** | Versao inicial dos fatos; divergencias com depoimentos posteriores |
| **Denuncia / queixa** | **Aptidao (CPP 41)**: fato, circunstancias, qualificacao, classificacao, rol; inepcia (CPP 395 III); justa causa |
| **Laudos periciais** | Local; **IML/necropsia**; toxicologico (drogas); balistico; **exame de corpo de delito** (CPP 158 — vestigios); assinatura de perito oficial |
| **FAC / antecedentes** | Folha de antecedentes; certidoes; transito em julgado (Sum. 444 STJ — validar) |
| **Interceptacoes / quebras** | Autorizacao judicial; Lei 9.296; prazo; fundamentacao; degravacao |
| **Decisoes / sentenca** | Recebimento da denuncia; cautelares; dosimetria; transito |
| **Guia de execucao** | Definitiva/provisoria; calculo de pena; datas |

## 2. EXTRAIR OS ELEMENTOS DO CRIME

- **Tipificacao** — capitulacao da denuncia x fatos provados; possivel desclassificacao/emendatio.
- **Materialidade** — existencia do crime: corpo de delito (CPP 158), laudos, exames. Crime que deixa vestigio exige exame (CPP 158); sua falta e lacuna.
- **Autoria** — prova que liga o cliente ao fato; indicios x prova; reconhecimento (CPP 226 — formalidade).

## 3. CADEIA DE CUSTODIA (CPP 158-A a 158-F)

- Rastrear o vestigio do reconhecimento a coleta, acondicionamento, transporte, recebimento, processamento, armazenamento e descarte.
- **Quebra da cadeia** → fragiliza/contamina a prova; sinalizar como tese de nulidade (PA-07).

## 4. MAPA DE LACUNAS E ILICITUDES (defesa)

- Prova **ilicita** (CF 5º LVI) e derivada (teoria dos frutos da arvore envenenada) → inadmissibilidade.
- Vicios: flagrante forjado/preparado; busca sem mandado/fundamento; interceptacao sem autorizacao; confissao sob coacao; reconhecimento irregular.
- Lacunas: ausencia de exame de corpo de delito; laudo sem perito oficial; quebra de custodia; denuncia inepta.

## 5. SAIDA

```
TIPIFICACAO: ... (denunciada x sustentavel)
MATERIALIDADE: ... (provada? laudos?)
AUTORIA: ... (prova x indicios)
CADEIA DE CUSTODIA: integra / quebrada em ...
LACUNAS: ...
ILICITUDES / NULIDADES: ...
DOCS RELEVANTES: doc. 1 ..., doc. 2 ...
```

## 6. PROIBICOES E INTEGRACAO

- **PA-03** — nao inventar data, tipificacao, pena, antecedente ou situacao prisional; so o que esta nos autos.
- **PA-07** — toda ilicitude/nulidade ancorada na garantia violada.
- **PA-12** — dado penal sensivel: sigilo reforçado, sem vazamento.
- Numerar documentos **"doc. N"**. Converter PDFs antes de analisar.
- Saida alimenta `analise-trilateral-criminal`, `calculos-criminais` e `linha-estrategica-criminal`.
