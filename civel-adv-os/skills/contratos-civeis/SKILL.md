---
name: contratos-civeis
description: >
  Tier 2 — teoria geral dos contratos e contratos tipicos civis (prestacao de servico, mutuo/emprestimo,
  comodato, mandato, doacao, fianca civil, locacao de coisas moveis). Cobre os dois polos: AUTOR
  (cobranca/revisao/resolucao) e REU (defesa). Principios (autonomia da vontade, funcao social — CC 421,
  boa-fe objetiva — CC 422). Inadimplemento absoluto x mora (CC 394-401), clausula penal (CC 408-416),
  exceptio non adimpleti contractus (CC 476), revisao por onerosidade excessiva e teoria da imprevisao
  (CC 478), resolucao/rescisao, distrato (CC 472), vicios redibitorios (CC 441-446) e evicção (CC
  447-457) em contratos civis. Acoes: revisional, de rescisao/resolucao contratual, de obrigacao de
  fazer/dar contratual, consignatoria. Ative em contrato, inadimplemento, mora, clausula penal, multa
  contratual, revisao de contrato, rescisao, distrato, comodato, mutuo, mandato, doacao, fianca civil
  ou vicio redibitorio. NAO trata contrato de consumo, locacao predial urbana (Lei 8.245) nem imovel —
  rotear (PA-09).
metadata:
  version: "0.1.0"
  area: "Direito Civil e Processo Civil"
  tier: 2
---

# CONTRATOS CIVEIS — TEORIA GERAL E TIPICOS (CC 421 e ss.)

> Tier 2. Side-aware: **AUTOR** (exige cumprimento, revisa, resolve, cobra) x **REU** (defesa). Peca e tom mudam conforme o polo (PA-10).
> **Recorte (PA-09):** contrato **civil** entre particulares paritarios. Relacao de consumo (CDC), locacao predial urbana (Lei 8.245), compra e venda de imovel/incorporacao → rotear.

---

## 1. PRINCIPIOS E REQUISITOS

- **Autonomia da vontade** mitigada pela **funcao social** (CC 421) e **boa-fe objetiva** (CC 422 — deveres anexos: lealdade, informacao, cooperacao).
- Validade: agente capaz, objeto licito/possivel/determinavel, forma prescrita ou nao defesa (CC 104).
- **Pacta sunt servanda** x revisao (CC 478) e onerosidade excessiva.

## 2. INADIMPLEMENTO

| Figura | Conteudo | Efeito |
|--------|----------|--------|
| **Mora** (CC 394-401) | Atraso/cumprimento imperfeito ainda util | Purgacao possivel; perdas + juros |
| **Inadimplemento absoluto** | Prestacao inutil ou impossivel | Resolucao + perdas e danos |

- Mora do devedor: CC 397 — termo certo constitui de pleno direito (*dies interpellat pro homine*); sem termo, exige interpelacao.
- **Clausula penal** (CC 408-416): moratoria (reforco) ou compensatoria (prefixacao de perdas — alternativa, CC 410); reducao equitativa (CC 413) se excessiva ou cumprimento parcial; teto = valor da obrigacao principal (CC 412).

## 3. DEFESAS CONTRATUAIS

- **Exceptio non adimpleti contractus** (CC 476) — nao pode exigir quem nao cumpriu a propria prestacao (contratos bilaterais).
- **Revisao / onerosidade excessiva** (CC 478) — fato superveniente, extraordinario e imprevisivel torna a prestacao excessivamente onerosa com extrema vantagem a outra parte → resolucao (ou revisao por oferta de modificacao, CC 479). Teoria da imprevisao.

## 4. EXTINCAO

- **Resolucao** — por inadimplemento (CC 474-475; clausula resolutiva expressa opera de pleno direito, tacita exige interpelacao judicial).
- **Resilicao** — unilateral (denuncia, quando admitida) ou bilateral (**distrato** — CC 472, mesma forma do contrato).
- **Rescisao** — genero (resolucao por lesao/inadimplemento).

## 5. GARANTIAS DO ADQUIRENTE

- **Vicios redibitorios** (CC 441-446) — defeito oculto que torna a coisa impropria/diminui valor; acoes edilicias: **redibitoria** (desfaz) ou **quanti minoris/estimatoria** (abate preco). Prazos **decadenciais** CC 445 (movel 30 dias, imovel 1 ano; vicio so detectavel depois: 180 dias/1 ano — PA-05).
- **Evicção** (CC 447-457) — perda da coisa por decisao judicial/ato administrativo a terceiro; evicto exige restituicao + perdas; denunciacao da lide ao alienante.

## 6. CONTRATOS TIPICOS (notas)

- **Prestacao de servico** (CC 593-609) · **Mutuo** (CC 586 — emprestimo de fungivel; juros CC 591) · **Comodato** (CC 579 — gratuito, infungivel) · **Mandato** (CC 653) · **Doacao** (CC 538; revogacao por ingratidao CC 555) · **Fianca civil** (CC 818 — beneficio de ordem CC 827; forma escrita) · **Locacao de moveis** (CC 565).

## 7. ESTRUTURA DA PECA

**Acao (autor):** 1. Enderecamento (foro de eleicao/CPC 53 III "d" ou domicilio do reu CPC 46) · 2. Qualificacao · 3. Dos fatos (contrato + inadimplemento) · 4. Do direito (vinculo, dever violado, clausula aplicavel) · 5. Pedidos (cumprimento/resolucao + perdas/clausula penal + juros + correcao + sucumbencia) · 6. Valor da causa (CPC 292 II — valor do contrato) · 7. Provas.
**Vias:** revisional, resolucao/rescisao, obrigacao de fazer/dar contratual, consignatoria (se a duvida e o pagamento).
**Defesa (reu):** exceptio (CC 476), negar mora/constituicao, reducao da clausula penal (CC 413), impugnar perdas, prescricao/decadencia, distrato/quitacao.

## 8. INTEGRACAO

- `calculos-civeis` → saldo, clausula penal, juros, correcao, prescricao (PA-06/PA-05).
- `jurisprudencia-civel` → teses de revisao/onerosidade, redibitoria (PA-01).
- `analise-documental-civel` → contrato, notificacoes, comprovantes.
- `estilo-juridico-civel` → forma · `revisao-final-civel` → R1-R4.

## 9. CHECKLIST DE SAIDA

- [ ] Recorte civel (nao consumo/imovel/locacao predial — PA-09)
- [ ] Norma vigente ao tempo do contrato (PA-04) · Contratual x extracontratual (PA-07)
- [ ] Mora/inadimplemento bem caracterizado (interpelacao quando exigida)
- [ ] Via/pedido adequados (revisional x resolucao x cobranca — PA-08) · cumulacao CPC 327
- [ ] Clausula penal no teto (CC 412) · Prescricao x decadencia (PA-05)
- [ ] Foro/eleicao conferido (P5) · Polo coerente (PA-10) · Selo P1 · R1-R4 pendente
