---
name: acao-plano-de-saude
description: >
  Producao para litigios de PLANO DE SAUDE / saude suplementar (Lei 9.656/98 + CDC + normas ANS). Ative em: negativa de cobertura (tratamento, medicamento, cirurgia, home care, protese/ortese, terapia), reajuste abusivo (faixa etaria, anual, sinistralidade em coletivo), rescisao/cancelamento unilateral, carencia, doenca preexistente, rol da ANS, internacao. Lado beneficiario (padrao) ou operadora. So roda apos triagem + Selo + linha estrategica. Encerra em revisao-final-consumidor (R1-R5).
---

# ACAO DE PLANO DE SAUDE (saude suplementar)

> Skill **Tier 2** (producao), lado consumidor por padrao. So apos `triagem-consumidor`,
> Selo de Validacao Legal Previa e `linha-estrategica-consumidor`. Dado de saude e
> SENSIVEL (LGPD art. 11): juntar laudos sob sigilo, expor CID so no indispensavel.

## 0. PRE-REQUISITOS
- Polo, eixo (negativa / reajuste / rescisao), esfera (judicial / ANS / extrajudicial), rito.
- **Selo P1**: Lei 9.656/98 vigente + CDC (Sum. 608 STJ — CDC aplica a planos, salvo
  AUTOGESTAO) + norma ANS aplicavel + jurisprudencia cruzada com o livro-razao (PA-01).
- Documentos: contrato/carteirinha, negativa POR ESCRITO da operadora, prescricao/relatorio
  medico fundamentado, comprovantes de pagamento, historico de reajustes. Falta → `[INFORMAR]`.
- Nao opinar sobre conduta clinica; a prescricao do medico ASSISTENTE e que define a necessidade.

## 1. TESES POR EIXO

### 1.1 Negativa de cobertura
- **Prescricao do medico assistente prevalece** sobre a recusa da operadora (a via/tecnica
  do tratamento e decisao medica, nao da operadora).
- **Rol da ANS e EXEMPLIFICATIVO** apos a **Lei 14.454/2022** (alterou a Lei 9.656/98):
  cobertura fora do rol e devida havendo eficacia comprovada (evidencia cientifica) ou
  recomendacao de orgao de avaliacao tecnica. Constitucionalidade na ADI 7.265 STF (com criterios).
- **Sum. 302 STJ** — abusiva a clausula que limita no tempo a internacao.
- **Sum. 597 STJ** — carencia para urgencia/emergencia abusiva se ultrapassar 24h.
- **Sum. 609 STJ** — recusa por doenca preexistente ilicita sem exame previo nem prova de ma-fe.
- Negativa de medicamento (inclusive off-label/importado registrado na ANVISA), home care,
  protese ligada ao ato cirurgico, terapia (multidisciplinar — TEA): cobertura devida.

### 1.2 Reajuste abusivo
- **Faixa etaria (Tema 1016 STJ)**: valido so se previsto em contrato, conforme normas da ANS
  e **sem percentuais desarrazoados**; vedado reajuste que configure barreira a permanencia do idoso
  (Estatuto do Idoso art. 15 §3). Em coletivo, aplicar as balizas do Tema 1016 STJ.
- **Anual/sinistralidade (coletivo)**: exigir memoria de calculo e base atuarial; sem transparencia,
  presume-se abusivo. Reajuste de plano individual segue o teto ANS.

### 1.3 Rescisao / cancelamento unilateral
- Individual/familiar: rescisao unilateral pela operadora so por fraude ou inadimplencia
  qualificada (60 dias + notificacao ate o 50 dia — Lei 9.656 art. 13). Coletivo: notificacao
  previa e vedacao de descontinuidade durante internacao/tratamento.

## 2. INSTRUMENTO E TUTELA
- **Tutela de urgencia** (CPC 300) e a alma do caso: negativa + risco a saude = perigo de dano;
  pedir liminar para cobertura IMEDIATA, sob multa diaria (astreintes). Quantum da multa proporcional.
- Acao: obrigacao de fazer (cobertura) + declaratoria de nulidade da clausula + danos.
- Via ANS (consumidor.gov / NIP) cabe em paralelo; o silencio/recusa e prova pre-constituida.

## 3. DANOS — CUIDADO (regra atualizada)
- **PA-VALORES**: dano material (o que o beneficiario gastou) vem de `calculos-consumidor`.
- **Dano moral NAO e automatico por negativa**: o **Tema 1.365 STJ (2026)** afastou o dano moral
  **in re ipsa** pela recusa de cobertura — exige **prova do dano concreto** (agravamento, exposicao,
  sofrimento qualificado). Pedir dano moral so com a circunstancia que o caracterize; nunca como presumido.

## 4. CHECKLIST
- [ ] Selo P1 (Lei 9.656 + CDC Sum. 608 + ANS) · negativa por escrito · prescricao medica fundamentada
- [ ] Rol exemplificativo (Lei 14.454/2022) quando fora do rol · tese do eixo correta
- [ ] Tutela de urgencia com multa proporcional · dano material do calculo
- [ ] Dano moral so com prova concreta (Tema 1.365 STJ — NAO presumir) · dado de saude sob sigilo (LGPD)
- [ ] Citacoes conferidas no livro-razao (PA-01) · `revisao-final-consumidor` R1-R5

## 5. ENCERRAMENTO
Entrega a peca (cobertura + nulidade + danos) com tutela de urgencia, pronta para a
`revisao-final-consumidor` (R1-R5 + ficha). Nada protocola sem o OK informado do advogado (C7).
