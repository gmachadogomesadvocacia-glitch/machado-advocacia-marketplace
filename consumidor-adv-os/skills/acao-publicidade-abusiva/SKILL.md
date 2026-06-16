---
name: acao-publicidade-abusiva
description: >
  ACAO PUBLICIDADE E PRATICAS ABUSIVAS — Skill Tier 2 (lado consumidor). Trata publicidade enganosa
  e abusiva (art. 37), o principio da VINCULACAO DA OFERTA (art. 30/35 — cumprimento forcado da oferta
  veiculada), venda casada e demais praticas abusivas (art. 39), com inversao do onus da prova da
  veracidade da publicidade (art. 38 — onus de quem patrocina). Pedidos: cumprimento da oferta /
  perdas e danos / dano moral (e coletivo quando cabivel). Tem recorte individual ou coletivo. Acione
  quando o consumidor reclama de propaganda enganosa, oferta nao cumprida, preco anunciado e nao
  honrado, venda casada, brinde condicionado, ou pratica comercial abusiva. Exige Selo P1.
metadata:
  version: "0.1.0"
  area: "Direito do Consumidor e Bancario"
  tier: 2
---

# ACAO PUBLICIDADE E PRATICAS ABUSIVAS

> Skill **Tier 2** — lado consumidor, eixos publicidade + praticas abusivas. Especializa a `peticao-inicial-consumidor`. So roda apos triagem, Selo P1 e linha estrategica.

---

## 0. PRE-REQUISITOS

- Polo do cliente = **consumidor** (PA-05). Se fornecedor → `contestacao-consumidor`.
- **Selo P1 EMITIDO**. Sem ele, nao redigir.
- CASO.md com: prova da publicidade/oferta (print, panfleto, anuncio, e-mail, screenshot datado), comprovante da recusa de cumprimento, eventual pagamento. Falta de doc essencial → `[INFORMAR]` (PA-15).

## 1. PUBLICIDADE ENGANOSA E ABUSIVA (art. 37)

- **Enganosa (art. 37, §1):** informacao falsa ou capaz de induzir o consumidor a erro sobre produto/servico, preco, qualidade. Enganosa **por omissao** (§3) quando deixa de informar dado essencial.
- **Abusiva (art. 37, §2):** discriminatoria, que explora medo/superticao, incita violencia, se aproveita de crianca, ou e prejudicial a saude/seguranca.
- Distinguir a publicidade do mero exagero tolerado (puffing) — mas o exagero verificavel vincula.

## 2. VINCULACAO DA OFERTA (art. 30 e 35) — TESE-MAE

- **Art. 30:** toda informacao ou publicidade suficientemente precisa **integra o contrato** e **obriga** o fornecedor.
- **Art. 35** — descumprida a oferta, o consumidor escolhe:
  1. **exigir o cumprimento forcado** da oferta, nos termos anunciados;
  2. **aceitar outro** produto/servico equivalente;
  3. **rescindir** o contrato, com restituicao + perdas e danos.
- A oferta veiculada (preco anunciado, condicao prometida) deve ser honrada ainda que por "erro" do fornecedor — o risco e dele.

## 3. PRATICAS ABUSIVAS (art. 39)

- **Venda casada (art. 39, I):** condicionar o fornecimento de um produto/servico a outro, ou a limites quantitativos sem justa causa.
- Demais incisos: enviar produto sem solicitacao (amostra gratis — art. 39, III), prevalecer-se da fraqueza do consumidor, elevar preco sem justa causa, recusar atendimento a demanda na medida do estoque.

## 4. ONUS DA PROVA DA PUBLICIDADE (art. 38)

**Regra propria, mais forte que a do art. 6 VIII:** o onus de provar a **veracidade e correcao** da publicidade e **de quem a patrocina** — independe dos requisitos da inversao comum. Invocar o art. 38 diretamente, sem precisar demonstrar verossimilhanca/hipossuficiencia.

## 5. RECORTE INDIVIDUAL x COLETIVO

- **Individual:** o consumidor lesado pleiteia cumprimento da oferta / perdas e danos / dano moral.
- **Coletivo:** publicidade massiva atinge a coletividade → cabe **dano moral coletivo** e tutela coletiva (legitimados do art. 82). Sinalizar a via coletiva quando o impacto for difuso e orientar o encaminhamento adequado.

## 6. ESTRUTURA E PEDIDOS (delega a `peticao-inicial-consumidor`)

Enderecamento → qualificacao → **Dos Fatos** (a oferta/publicidade, sua precisao, a recusa de cumprimento; docs "doc. N") → **Do Direito** (FIRAC: relacao de consumo; enganosidade/abusividade art. 37 ou vinculacao art. 30/35 ou pratica abusiva art. 39; **onus da publicidade art. 38**; antecipacao adversarial — alegacao de erro/puffing/oferta ja encerrada) → **Tutela** se houver (suspender publicidade, garantir o preco) → **Pedidos**:
- **cumprimento forcado da oferta** (art. 35, I) OU produto equivalente OU rescisao + restituicao;
- **perdas e danos**;
- **dano moral quantificado** (individual e/ou **coletivo** quando cabivel);
- juros e correcao.

→ valor da causa → requerimentos.

Sumula/Tema (vinculacao, dano moral coletivo) sempre `[VERIFICAR]` via `jurisprudencia-consumidor` (PA-01).

## 7. CHECKLIST

- [ ] Prova da oferta/publicidade datada e precisa juntada (doc. N)
- [ ] Tese certa: enganosa/abusiva (art. 37) · vinculacao (art. 30/35) · pratica abusiva (art. 39)
- [ ] **Onus da publicidade pelo art. 38** invocado (alem do art. 6 VIII)
- [ ] Recorte individual x coletivo definido · dano moral coletivo so quando cabivel
- [ ] Pedidos determinados · dano moral quantificado · Sumula/Tema `[VERIFICAR]` (PA-01)
- [ ] Submeter a `revisao-final-consumidor` (R1-R4) antes da entrega (PA-22)

## 8. ENCERRAMENTO

Entrega a acao de publicidade/praticas abusivas com a oferta vinculada, o onus do art. 38 explorado, recorte individual/coletivo definido e dano moral quantificado, pronta para a Suprema Corte R1-R4.
