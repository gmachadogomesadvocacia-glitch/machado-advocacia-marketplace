---
name: revisao-final-criminal
description: >
  Revisao final Tier 3 — Suprema Corte R1-R4. Ultima barreira antes de qualquer entrega de peca,
  parecer ou calculo penal. R1 valida fundamentos (CP, CPP, LEP, leis especiais vigentes + lei penal
  no tempo) e jurisprudencia (Sumula/Tema/Vinculante STF/STJ) contra alucinacao (PA-01/PA-02/PA-04);
  R2 audita fatos, tipificacao, pena, datas, prescricao e dosimetria (PA-03/PA-05/PA-06); R3 verifica
  coerencia de polo, garantias constitucionais e a vedacao etico-penal (PA-07/PA-08/PA-09/PA-10); R4
  confere forma, competencia, situacao prisional, sigilo e LGPD (PA-12). Ative SEMPRE antes de entregar
  qualquer produto criminal ao usuario.
metadata:
  version: "0.1.0"
  area: "Direito Penal e Processo Penal"
  tier: 3
---

# REVISAO FINAL CRIMINAL — SUPREMA CORTE R1-R4

> Tier 3. **Nenhum** produto penal sai sem passar pelas 4 instancias. Falha em qualquer R = retorna para correcao, nao entrega. Executa o protocolo P6 e fecha as Proibicoes Absolutas.

---

## R1 — FUNDAMENTOS E JURISPRUDENCIA (PA-01, PA-02, PA-04)

- [ ] Todo dispositivo citado existe e diz o que se afirma (CP, CPP, LEP, lei especial).
- [ ] **Lei penal no tempo** correta: aplicada a do fato, salvo a posterior mais benefica (retroage) — CF 5º XL, CP 2º.
- [ ] Toda Sumula/Tema/Sumula Vinculante (STF/STJ) foi **confirmada** — sem numero inventado, sem tese atribuida a precedente que nao a sustenta.
- [ ] Tipificacao correta (elementos do tipo, dolo/culpa, consumacao/tentativa).

## R2 — FATOS, PENA E PRESCRICAO (PA-03, PA-05, PA-06)

- [ ] Datas, tipificacao, pena cominada, antecedentes e situacao prisional conferem com os autos.
- [ ] **Prescricao** calculada corretamente (punitiva x executoria; pela pena; marcos CP 117) — `calculos-criminais`.
- [ ] **Dosimetria** pelo metodo trifasico (CP 68); atenuante nao abaixo do minimo (Sum. 231 STJ); detracao/remicao corretas.
- [ ] Nenhum fato afirmado sem prova nos autos; prova ilicita nao utilizada em favor de tese fragil.

## R3 — POLO, GARANTIAS E ETICA (PA-07, PA-08, PA-09, PA-10)

- [ ] Peca coerente com o polo do cliente (defesa x assistencia de acusacao).
- [ ] Garantias preservadas — presuncao de inocencia, contraditorio/ampla defesa, vedacao de prova ilicita, nao autoincriminacao.
- [ ] **Nada** que oriente crime, destruicao/ocultacao de prova, fuga ou coacao de testemunha (PA-08) — checagem inegociavel.
- [ ] Sigilo profissional preservado — a peca nao prejudica o cliente nem revela o que o incrimine (PA-09).

## R4 — FORMA, COMPETENCIA E SIGILO (PA-11, PA-12, PA-13)

- [ ] Enderecamento/competencia correta (juizo do lugar do crime; juri; JECrim; tribunal conforme coator no HC; foro por prerrogativa).
- [ ] Estrutura completa, pedidos especificos (liberdade, absolvicao, nulidade, recurso), provas/diligencias indicadas.
- [ ] Identidade do operador resolvida (sem tokens `{{...}}` vazando) e OAB correta.
- [ ] Sigilo + LGPD: dado penal sensivel (antecedentes, processo) protegido.
- [ ] Selo P1 foi registrado antes da producao; entrega em **.txt** por padrao.

---

## R5 — VERIFICACAO ADVERSARIAL (RED-TEAM)

Mude de chapeu: voce **AGORA** e o Ministerio Publico / o juizo cetico. Unica missao: **DERROTAR** a peca. Achou UMA falha → **REPROVADO**.

- [ ] **DOSIMETRIA/VALORES** — pena fechada pelo trifasico (CP 68)? Atenuante nao desce abaixo do minimo (Sum. 231 STJ)? Os numeros vem do `calculos-criminais`? Lei penal no tempo aplicada (mais benefica retroage)?
- [ ] **PRESCRICAO** — punitiva x executoria bem calculada (CP 109/110/117)?
- [ ] **INSTRUMENTO/VIA** — peca e instancia certas (HC x apelacao x RESE; absolvicao CPP 386 x impronuncia)?
- [ ] **COMPETENCIA** — juiz natural respeitado (juri p/ doloso contra a vida; JECrim; foro por prerrogativa)?
- [ ] **CITACOES** — sumulas/vinculantes batem (Sum. 691 STF; Sum. 231 STJ; SV 24)?
- [ ] **ETICA (PA-08)** — NADA que oriente crime/destruicao de prova/fuga/coacao; sigilo da defesa preservado.

**Veredito R5:** PASSOU / REPROVADO (eixo + falha + correcao).

---

## SAIDA

```
R1 fundamentos/jurisprudencia: OK / CORRIGIR — [notas]
R2 fatos/pena/prescricao:      OK / CORRIGIR — [notas]
R3 polo/garantias/etica:       OK / CORRIGIR — [notas]
R4 forma/competencia/sigilo:   OK / CORRIGIR — [notas]
R5 adversarial (red-team):     PASSOU / REPROVADO — [eixo+falha+correcao]
VEREDITO: LIBERADO / RETIDO
```
**RETIDO** em qualquer R1-R5 → volta a skill de origem. Nunca entregar com R pendente (PA-13), e jamais liberar peca que toque a PA-08. Apos LIBERADO → emitir a FICHA DE CONFERENCIA e atualizar `CASO.md` (memoria-de-caso-criminal).

## FICHA DE CONFERENCIA (acompanha a entrega, nao integra a peca)

```
FICHA DE CONFERENCIA — pre-protocolo
- PREMISSAS: ...
- DOSIMETRIA/PRAZOS (origem calculos-criminais): ...
- CITACOES (cada uma → status): ... — CONFIRMADO | VALIDAR
- LACUNAS [INFORMAR]: ...
- RISCOS / PONTOS ADVERSARIAIS: ...
- CHECAGEM PA-08 (nada de obstrucao): OK
- VEREDITO: R1 _ · R2 _ · R3 _ · R4 _ · R5 _
- PENDE O OK INFORMADO DO ADVOGADO antes do protocolo.
```
