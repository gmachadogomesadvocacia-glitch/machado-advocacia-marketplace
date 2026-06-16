---
name: revisao-final-tributaria
description: >
  Revisao final Tier 3 — Suprema Corte R1-R4. Ultima barreira antes de qualquer entrega de peca,
  parecer ou calculo tributario. R1 valida fundamentos (CTN, lei do tributo vigente no fato gerador,
  LEF, Dec. 70.235) e jurisprudencia (Sumula/Tema STF/STJ/CARF) contra alucinacao (PA-01/PA-02/PA-04);
  R2 audita fatos, valores, CDA, datas, decadencia x prescricao (PA-03/PA-05); R3 verifica coerencia
  de polo, via processual e estrategia (PA-07/PA-08/PA-10); R4 confere forma, prazo, enderecamento,
  sigilo fiscal e LGPD (PA-12). Ative SEMPRE antes de entregar qualquer produto tributario ao usuario.
metadata:
  version: "0.1.0"
  area: "Direito Tributario"
  tier: 3
---

# REVISAO FINAL TRIBUTARIA — SUPREMA CORTE R1-R4

> Tier 3. **Nenhum** produto tributario sai sem passar pelas 4 instancias. Falha em qualquer R = retorna para correcao, nao entrega. Executa o protocolo P6 e fecha as Proibicoes Absolutas.

---

## R1 — FUNDAMENTOS E JURISPRUDENCIA (PA-01, PA-02, PA-04)

- [ ] Todo dispositivo citado existe e diz o que se afirma (CTN, lei do tributo, LEF 6.830, Dec. 70.235, LC 118, Lei 13.988).
- [ ] Norma aplicada e a **vigente no fato gerador** (tempus regit actum) — checar transicao da Reforma (CBS/IBS) se o periodo alcanca 2026+.
- [ ] Toda Sumula/Tema (STF/STJ) e sumula/precedente CARF foi **confirmado** — sem numero inventado, sem tese atribuida a precedente que nao a sustenta.
- [ ] Distincao decadencia (CTN 173/150 §4º) x prescricao (CTN 174) corretamente fundamentada.

## R2 — FATOS, VALORES E PRAZOS (PA-03, PA-05, PA-09)

- [ ] Valores, competencias, fatos geradores e dados da CDA conferem com os documentos.
- [ ] Calculos de decadencia/prescricao **refeitos**, nao presumidos (`calculos-tributarios`).
- [ ] Prazos em curso corretos (impugnacao 30d, embargos art. 16, repeticao 5 anos CTN 168).
- [ ] Nenhum pleito de repeticao/compensacao alem de 5 anos (LC 118).
- [ ] Datas e nomes das partes corretos; sem fato nao comprovado nos autos.

## R3 — POLO, VIA E ESTRATEGIA (PA-06, PA-07, PA-08, PA-10)

- [ ] Peca coerente com o polo do cliente (contribuinte/Fazenda).
- [ ] Via processual correta — excecao de pre-executividade so para materia de ordem publica sem dilacao (Sum. 393); senao, embargos com garantia.
- [ ] Redirecionamento ao socio tratado com art. 135 CTN / Sum. 435 / Tema 962, nao por mero inadimplemento (Sum. 430).
- [ ] Nenhuma orientacao que configure evasao/sonegacao (PA-06) — so elisao licita.
- [ ] Estrategia administrativo x judicial coerente (suspensao da exigibilidade — CTN 151).

## R4 — FORMA, FORO E SIGILO (PA-11, PA-12, PA-13)

- [ ] Enderecamento/orgao correto (vara de execucoes fiscais; DRJ/CARF; SEFAZ/TIT; Fazenda municipal).
- [ ] Estrutura completa, pedidos especificos, valor da causa, provas indicadas.
- [ ] Identidade do operador resolvida (sem tokens `{{...}}` vazando) e OAB correta.
- [ ] Sigilo fiscal (CTN art. 198) + LGPD: nenhum dado sensivel do contribuinte exposto indevidamente.
- [ ] Selo P1 foi registrado antes da producao; entrega em **.txt** por padrao.

---

## SAIDA

```
R1 fundamentos/jurisprudencia: OK / CORRIGIR — [notas]
R2 fatos/valores/prazos:       OK / CORRIGIR — [notas]
R3 polo/via/estrategia:        OK / CORRIGIR — [notas]
R4 forma/foro/sigilo:          OK / CORRIGIR — [notas]
VEREDITO: LIBERADO / RETIDO
```
**RETIDO** em qualquer R → volta a skill de origem. Nunca entregar com R pendente (PA-13). Apos LIBERADO → atualizar `CASO.md` (memoria-de-caso-tributario).
