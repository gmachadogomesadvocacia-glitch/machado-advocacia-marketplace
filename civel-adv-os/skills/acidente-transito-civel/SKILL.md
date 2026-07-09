---
name: acidente-transito-civel
description: >
  Tier 2 — reparacao civil por acidente de transito (esfera CIVEL). Ative em batida, colisao, acidente de transito, atropelamento, indenizacao de veiculo, DPVAT, pensao por morte no transito ou defesa do condutor.
metadata:
  version: "0.1.0"
  area: "Direito Civil e Processo Civil"
  tier: 2
---

# ACIDENTE DE TRANSITO — REPARACAO CIVEL (CC 186/927/948-950)

> Tier 2. Side-aware: **AUTOR/vitima** (pleiteia reparacao) x **REU/condutor ou proprietario** (defesa). O tom e a peca mudam conforme o polo (PA-10).
> **Recorte (PA-09):** so a reparacao CIVEL. Crime de transito (homicidio/lesao culposa, embriaguez) → penal. Multa/suspensao CNH/CTB → administrativo. Nao redigir aqui.

---

## 1. RESPONSABILIDADE

- Regra: **subjetiva** (CC 186/927) — provar conduta culposa, dano e nexo.
- **Presuncoes de culpa** (relativas, invertem o onus):
  - **Colisao traseira** — presume-se culpa de quem bate atras (dever de distancia/atencao).
  - **Conversao / mudanca de faixa / saida de garagem** — culpa de quem manobra.
  - **Contramao, avanco de sinal, preferencial** — culpa de quem viola a regra.
- **Responsabilidade do proprietario** pelo dano causado por terceiro a quem confiou o veiculo (culpa in eligendo/in vigilando) — responde **solidariamente** com o condutor.
- Atividade de transporte/risco pode atrair objetiva (CC 927 § unico), mas transporte de passageiros remunerado e relacao consumo → rotear (PA-09).

## 2. DANOS INDENIZAVEIS

- **Materiais** — *dano emergente*: conserto (orcamentos/NF) ou perda total (valor de mercado — tabela FIPE); **desvalorizacao** do veiculo (depreciacao pos-reparo, exige prova/pericia); *lucros cessantes*: dias parados de taxi/app/frete (diaria liquida x dias).
- **Morais** — lesao a vitima ou, em caso de morte, aos familiares (dano por ricochete).
- **Esteticos** — autonomos e cumulaveis com o moral (Sum. 387 STJ — validar).
- **Pensionamento (CC 948-950):**
  - **Morte** (CC 948 II) — pensao aos dependentes (2/3 dos rendimentos ate idade-limite; 1/3 presume-se gasto do falecido), 13o, constituicao de capital ou inclusao em folha (CPC 533).
  - **Incapacidade** (CC 950) — pensao correspondente a depreciacao da capacidade laboral; arbitramento por percentual de invalidez (laudo).

## 3. DPVAT E REGRESSO

- **DPVAT** — seguro obrigatorio; valor recebido **deduz-se** da indenizacao por morte/invalidez (Sum. 246 STJ — **validar**). Nao deduz do dano moral.
- **Regresso da seguradora** que pagou o segurado — sub-roga-se contra o causador (Sum. 188 STF — **validar**).
- **Regresso do segurado** que arcou alem da cobertura.

## 4. JUROS, CORRECAO E PRESCRICAO

- Juros de mora desde o **evento danoso** (extracontratual — Sum. 54 STJ — PA-06).
- Correcao do dano material desde o desembolso; do moral desde o arbitramento (Sum. 362 STJ).
- **Prescricao: 3 anos** (CC 206 §3º, V — reparacao civil — PA-05). Regresso da seguradora/sub-rogacao segue o mesmo prazo da vitima.

## 5. PROVA

BO/registro de ocorrencia, fotos do local e dos veiculos, laudo pericial de transito, orcamentos (3) ou NF, FIPE, comprovantes de renda (lucros cessantes/pensao), prova testemunhal, croqui, video.

## 6. ESTRUTURA DA PECA

**Acao indenizatoria (autor):**
1. Enderecamento (foro — CPC 53 V: domicilio do autor ou local do fato, ou 46: reu) · 2. Qualificacao (autor + condutor **e** proprietario, se distintos) · 3. Dos fatos (dinamica do acidente) · 4. Do direito (culpa/presuncao, nexo, solidariedade proprietario) · 5. Dos danos (materiais discriminados, moral, estetico, pensao) e quantum · 6. DPVAT (deducao, se houve) · 7. Tutela, se cabivel · 8. Pedidos (condenacao, pensao/constituicao de capital CPC 533, juros desde o evento, correcao, sucumbencia) · 9. Valor da causa (soma) · 10. Provas.

**Defesa (reu):** negar/atribuir culpa (recolocar a dinamica), excludentes (culpa exclusiva da vitima, fato de terceiro, fortuito), impugnar quantum e nexo, deducao do DPVAT, ilegitimidade (se nao e proprietario/condutor), prescricao.

## 7. INTEGRACAO

- `calculos-civeis` → liquidacao (conserto, lucros cessantes, pensao, capital), juros, correcao, prescricao (PA-06/PA-05).
- `jurisprudencia-civel` → validar Sumulas (54, 187, 188 STF, 246, 362, 387 — PA-01).
- `analise-documental-civel` → BO, laudo, orcamentos, prova do nexo.
- `estilo-juridico-civel` → forma · `revisao-final-civel` → R1-R4.

## 8. CHECKLIST DE SAIDA

- [ ] Recorte civel (nao penal/administrativo — PA-09)
- [ ] Culpa/presuncao definida; proprietario incluido se for o caso
- [ ] Danos discriminados e provados; pensao com criterio (CC 948-950)
- [ ] DPVAT deduzido (Sum. 246 — validar) · Regresso bem fundado (Sum. 188 STF — validar)
- [ ] Juros desde o evento (Sum. 54) · Prescricao 3 anos (PA-05)
- [ ] Foro correto (P5) · Polo coerente (PA-10) · Selo P1 feito · R1-R4 pendente
