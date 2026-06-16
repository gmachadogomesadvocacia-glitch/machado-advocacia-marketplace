---
name: obrigacoes-e-tutelas
description: >
  Tier 2 — obrigacoes especificas e tutelas provisorias no processo civil civel. Cobre os dois polos:
  AUTOR (pleiteia) e REU (resiste). (a) OBRIGACOES de FAZER/NAO FAZER (CPC 497, 536-537 — tutela
  especifica, multa/astreintes) e de DAR COISA (CPC 538). (b) TUTELA PROVISORIA (CPC 294+): de URGENCIA
  antecipada e cautelar (fumus boni iuris + periculum in mora — CPC 300), de EVIDENCIA (CPC 311 — sem
  urgencia), tutela antecedente e ESTABILIZACAO (CPC 304), arresto e sequestro (cautelares). (c)
  CONSIGNACAO EM PAGAMENTO (CC 334-345; CPC 539-549 — recusa injusta do credor, mora accipiendi, duvida
  sobre quem deve receber). Ative em obrigacao de fazer/nao fazer, astreintes, multa diaria, tutela de
  urgencia, liminar, tutela antecipada, tutela de evidencia, tutela cautelar, arresto, sequestro,
  estabilizacao da tutela ou acao consignatoria. Tutela em materia de outro plugin (saude/familia/
  consumo) → rotear (PA-09).
metadata:
  version: "0.1.0"
  area: "Direito Civil e Processo Civil"
  tier: 2
---

# OBRIGACOES ESPECIFICAS E TUTELAS PROVISORIAS (CPC 294/497/536/539; CC 334)

> Tier 2. Side-aware: **AUTOR** (pleiteia) x **REU** (resiste). Peca e tom mudam (PA-10). Transversal — combina com as demais skills de producao.

---

## 1. OBRIGACOES DE FAZER / NAO FAZER (CPC 497, 536-537)

- Prioridade da **tutela especifica** (resultado pratico equivalente) sobre a conversao em perdas e danos (CC 247-249; CPC 497).
- **Astreintes** (CPC 537) — multa coercitiva (diaria ou por evento); valor e periodicidade fixados de oficio; pode ser modificada (insuficiente/excessiva), sem coisa julgada sobre o quantum; nao se confunde com perdas e danos.
- Meios de apoio (CPC 139 IV, 536 §1º) — busca e apreensao, remocao, impedimento de atividade nociva, requisicao de forca policial.
- **Fazer infungivel** descumprido → perdas e danos (CC 247).

## 2. OBRIGACAO DE DAR COISA (CPC 538)

- Coisa certa/incerta; mandado de busca e apreensao (movel) ou imissao na posse (imovel); astreintes aplicaveis.

## 3. TUTELA PROVISORIA (CPC 294+)

```
Tutela Provisoria
├─ Urgencia (CPC 300) — fumus + periculum
│   ├─ Antecipada (satisfativa) — antecipa o pedido
│   │   ├─ Antecedente (CPC 303) → ESTABILIZACAO (CPC 304)
│   │   └─ Incidental
│   └─ Cautelar (assegura) — arresto, sequestro, arrolamento (CPC 301)
│       └─ Antecedente (CPC 305)
└─ Evidencia (CPC 311) — independe de urgencia
```

- **Urgencia** (CPC 300): probabilidade do direito (**fumus**) + perigo de dano/risco ao resultado util (**periculum**); caucao possivel; cautela com **reversibilidade** (CPC 300 §3º).
- **Antecipada antecedente** (CPC 303) — peticao limitada ao pedido de tutela + indicacao do pedido final; aditamento em 15 dias.
- **ESTABILIZACAO** (CPC 304) — concedida a tutela antecipada antecedente e **nao interposto agravo** pelo reu, o processo extingue-se e a tutela **estabiliza** (nao faz coisa julgada; revisao por acao autonoma em 2 anos).
- **Evidencia** (CPC 311) — abuso de defesa/intuito protelatorio (I); tese firmada em repetitivos/sumula vinculante + prova documental (II); contrato de deposito (III); prova documental suficiente sem contraprova capaz de gerar duvida (IV). Incisos II e IV → **liminar** possivel.
- **Arresto** (bem indeterminado, garante quantia) x **sequestro** (bem determinado litigioso).

## 4. CONSIGNACAO EM PAGAMENTO (CC 334-345; CPC 539-549)

- **Cabimento** (CC 335): recusa injusta do credor em receber/dar quitacao; mora accipiendi; **duvida** sobre quem legitimamente deve receber; credor incapaz/desconhecido/ausente; litigio sobre o objeto.
- Efeito: extingue a obrigacao e exonera o devedor (afasta a mora a partir do deposito valido).
- Procedimento (CPC 539): deposito + citacao do reu; este levanta, contesta (insuficiencia — CPC 544; indica o quanto entende devido — CPC 545) ou aceita.
- Pagamento em consignacao bancaria extrajudicial (CPC 539 §1º) — possivel para obrigacoes em dinheiro.

## 5. ESTRUTURA DAS PECAS

- **Obrigacao de fazer/dar (autor):** enderecamento · qualificacao · fatos (fonte da obrigacao) · direito (CPC 497/536/538) · **pedido de tutela especifica + astreintes** · valor da causa · provas.
- **Tutela provisoria (peticao/topico):** demonstrar fumus + periculum (urgencia) ou hipotese do CPC 311 (evidencia); pedido especifico; caucao/reversibilidade.
- **Consignatoria (autor/devedor):** enderecamento · qualificacao · fatos (recusa/duvida) · direito (CC 335; CPC 539) · pedido de deposito + extincao/quitacao · valor da causa (= debito) · provas.

## 6. INTEGRACAO

- `calculos-civeis` → valor do deposito consignatorio, teto de astreintes, atualizacao (PA-06).
- `jurisprudencia-civel` → limites de astreintes, estabilizacao, evidencia (PA-01).
- `analise-documental-civel` → prova do periculum, da recusa, da obrigacao.
- `estilo-juridico-civel` → forma · `revisao-final-civel` → R1-R4.

## 7. CHECKLIST DE SAIDA

- [ ] Tutela: fumus + periculum (urgencia) OU hipotese CPC 311 (evidencia) demonstrados
- [ ] Reversibilidade/caucao avaliada (CPC 300 §3º) · risco de estabilizacao (CPC 304) ciente
- [ ] Astreintes com valor/periodicidade e teto razoaveis (CPC 537)
- [ ] Consignacao: hipotese do CC 335 + valor integral depositado (PA-06)
- [ ] Via/pedido adequados (PA-08) · materia de outro plugin roteada (PA-09)
- [ ] Foro correto (P5) · Polo coerente (PA-10) · Selo P1 feito · R1-R4 pendente
