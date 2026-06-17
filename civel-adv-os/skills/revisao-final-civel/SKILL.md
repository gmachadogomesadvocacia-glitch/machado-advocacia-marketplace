---
name: revisao-final-civel
description: >
  Revisao final Tier 3 — Suprema Corte R1-R4. Ultima barreira antes de qualquer entrega de peca,
  contrato, parecer ou calculo civel. R1 valida fundamentos (CC, CPC, leis civis vigentes no fato/
  contrato) e jurisprudencia (Sumula/Tema STF/STJ) contra alucinacao (PA-01/PA-02/PA-04); R2 audita
  fatos, valores, quantum, juros, correcao, prescricao e decadencia (PA-03/PA-05/PA-06); R3 verifica
  coerencia de polo, via/pedido, responsabilidade contratual x extracontratual e o cabimento civel
  residual (PA-07/PA-08/PA-09/PA-10); R4 confere forma, foro, valor da causa, sigilo e LGPD (PA-12).
  Ative SEMPRE antes de entregar qualquer produto civel ao usuario.
metadata:
  version: "0.1.0"
  area: "Direito Civil e Processo Civil"
  tier: 3
---

# REVISAO FINAL CIVEL — SUPREMA CORTE R1-R4

> Tier 3. **Nenhum** produto civel sai sem passar pelas 4 instancias. Falha em qualquer R = retorna para correcao, nao entrega. Executa o protocolo P6 e fecha as Proibicoes Absolutas.

---

## R1 — FUNDAMENTOS E JURISPRUDENCIA (PA-01, PA-02, PA-04)

- [ ] Todo dispositivo citado existe e diz o que se afirma (CC, CPC, leis civis especiais — DL 911).
- [ ] Norma aplicada e a **vigente no fato/contrato** (direito intertemporal — CC/2002 x CC/1916; art. 2.035).
- [ ] Toda Sumula/Tema (STF/STJ) foi **confirmada** — sem numero inventado, sem tese atribuida a precedente que nao a sustenta.
- [ ] Regime correto (subjetiva × objetiva; contratual × extracontratual).

## R2 — FATOS, QUANTUM E PRAZOS (PA-03, PA-05, PA-06)

- [ ] Valores, datas, partes, clausulas e titulo conferem com os documentos.
- [ ] **Quantum, juros e correcao** refeitos (dano emergente × lucro cessante; juros — Sum. 54 extracontratual / citacao no contratual; correcao do moral — Sum. 362) — `calculos-civeis`.
- [ ] **Prescricao × decadencia** corretas (CC 205/206; reparacao civil 3 anos; decadencia anulacao 4 anos; termo inicial/actio nata).
- [ ] Nenhum dano afirmado sem prova; nexo demonstrado.

## R3 — POLO, VIA E CABIMENTO (PA-07, PA-08, PA-09, PA-10)

- [ ] Peca coerente com o polo do cliente (autor × reu).
- [ ] **Responsabilidade contratual × extracontratual** nao confundidas (regime, onus, prazo).
- [ ] Via/pedido adequados (monitoria × cobranca × execucao; cumulacao compativel — CPC 327); valor da causa correto.
- [ ] **Cabimento civel residual confirmado** — a materia nao pertence a outro plugin (PA-09); se pertencer, rotear.

## R4 — FORMA, FORO E SIGILO (PA-11, PA-12, PA-13)

- [ ] Foro/competencia correta — domicilio do reu (CPC 46); reparacao de dano (CPC 53 IV); acidente de veiculo (CPC 53 V).
- [ ] Estrutura completa, pedidos especificos, valor da causa, provas indicadas, tutela quando cabivel.
- [ ] Identidade do operador resolvida (sem tokens `{{...}}` vazando) e OAB correta.
- [ ] Sigilo OAB + LGPD: dados do cliente protegidos.
- [ ] Selo P1 foi registrado antes da producao; entrega em **.txt** por padrao.

---

## R5 — VERIFICACAO ADVERSARIAL (RED-TEAM)

Mude de chapeu: voce AGORA e a parte contraria / o juizo cetico. Unica missao: DERROTAR a peca. Achou UMA falha → REPROVADO.

- [ ] **VALORES** — dano (emergente x cessante), juros (Sum. 54 evento x citacao) e correcao (Sum. 362) vem do `calculos-civeis`? quantum fundamentado?
- [ ] **INSTRUMENTO/VIA** — peca certa (monitoria x cobranca x execucao; declaratoria x condenatoria)? cumulacao compativel (CPC 327)?
- [ ] **RESP. CONTRATUAL x EXTRACONTRATUAL** — regime certo (onus/prazo)?
- [ ] **COMPETENCIA/FORO** — domicilio do reu (CPC 46); reparacao de dano (CPC 53 IV/V)?
- [ ] **PRESCRICAO x DECADENCIA** — CC 205/206 bem aplicados (reparacao 3 anos)?
- [ ] **CABIMENTO CIVEL RESIDUAL** — a materia nao pertence a outro plugin (consumo/familia/imovel/medico)?

**Veredito R5:** PASSOU / REPROVADO (eixo+falha+correcao).

---

## SAIDA

```
R1 fundamentos/jurisprudencia: OK / CORRIGIR — [notas]
R2 fatos/quantum/prazos:       OK / CORRIGIR — [notas]
R3 polo/via/cabimento:         OK / CORRIGIR — [notas]
R4 forma/foro/sigilo:          OK / CORRIGIR — [notas]
R5 adversarial (red-team):     PASSOU / REPROVADO — [eixo+falha+correcao]
VEREDITO: LIBERADO / RETIDO
```
**RETIDO** em qualquer R (R1-R5) → volta a skill de origem. Nunca entregar com R pendente (PA-13). Apos LIBERADO → emitir a FICHA DE CONFERENCIA junto da entrega e atualizar `CASO.md` (memoria-de-caso-civel).

## FICHA DE CONFERENCIA (acompanha a entrega, nao integra a peca)

```
FICHA DE CONFERENCIA — pre-protocolo
- PREMISSAS: ...
- VALORES (cada R$ → fonte): R$ __ — origem calculos-civeis
- CITACOES (cada uma → status): Sum. 54/362 STJ — CONFIRMADO | VALIDAR
- LACUNAS [INFORMAR]: ...
- RISCOS / PONTOS ADVERSARIAIS: ...
- VEREDITO: R1 _ · R2 _ · R3 _ · R4 _ · R5 _
- PENDE O OK INFORMADO DO ADVOGADO antes do protocolo.
```
