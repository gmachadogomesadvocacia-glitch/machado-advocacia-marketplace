---
name: revisao-final-imobiliaria
description: >
  Revisao final Tier 3 — Suprema Corte R1-R4. Ative SEMPRE antes de entregar qualquer produto imobiliario ao usuario.
metadata:
  version: "0.1.0"
  area: "Direito Imobiliario e Locacao"
  tier: 3
---

# REVISAO FINAL IMOBILIARIA — SUPREMA CORTE R1-R4

> Tier 3. **Nenhum** produto imobiliario sai sem passar pelas 4 instancias. Falha em qualquer R = retorna para correcao, nao entrega. Executa o protocolo P6 e fecha as Proibicoes Absolutas.

---

## R1 — FUNDAMENTOS E JURISPRUDENCIA (PA-01, PA-02, PA-04)

- [ ] Todo dispositivo citado existe e diz o que se afirma (Lei 8.245, CC, Lei 9.514, Lei 4.591, Lei 6.015, Lei 13.786).
- [ ] Norma aplicada e a **vigente no contrato/fato** (tempus regit actum) — ex.: Lei 13.786 so para contratos posteriores a 2018.
- [ ] Toda Sumula/Tema (STF/STJ) foi **confirmada** — sem numero inventado, sem tese atribuida a precedente que nao a sustenta.
- [ ] Distincao correta entre acao possessoria (posse) e petitoria (dominio) na fundamentacao.

## R2 — FATOS, IMOVEL E PRAZOS (PA-03, PA-07)

- [ ] Matricula, area, endereco, partes e numero do contrato conferem com os documentos.
- [ ] Valores (alugueis, debito, multa, indice de reajuste, restituicao no distrato) **refeitos**, nao presumidos (`calculos-imobiliarios`).
- [ ] Prazos em curso corretos: **decadencia da renovatoria** (art. 51 §5º — fatal), purgacao da mora (15d, art. 62), contestacao possessoria (15d), purgacao na fiduciaria (15d, art. 26).
- [ ] Datas e qualificacoes corretas; nenhum fato sem prova documental.

## R3 — POLO, VIA E POSSE x PROPRIEDADE (PA-05, PA-06, PA-10)

- [ ] Peca coerente com o polo do cliente (locador/locatario, comprador/vendedor, etc.).
- [ ] Via processual correta — possessoria (forca nova × velha) × reivindicatoria; despejo × cobranca × consignatoria.
- [ ] **Posse nao confundida com propriedade/dominio**; sem *exceptio proprietatis* em possessoria (art. 557 CPC).
- [ ] Liminar de despejo so nas hipoteses do art. 59 §1º + caucao (PA-06).
- [ ] Garantia locaticia unica (art. 37 — PA-08); rito da fiduciaria respeitado (PA-09).

## R4 — FORMA, FORO E SIGILO (PA-11, PA-12, PA-13)

- [ ] Foro correto — situacao do imovel para acoes reais (art. 47 CPC); foro do contrato/eleicao na locacao.
- [ ] Estrutura completa, pedidos especificos, **valor da causa** correto (ex.: 12 alugueis no despejo — art. 58, III), provas indicadas.
- [ ] Identidade do operador resolvida (sem tokens `{{...}}` vazando) e OAB correta.
- [ ] Sigilo OAB + LGPD: dados do cliente e do imovel protegidos.
- [ ] Selo P1 foi registrado antes da producao; entrega em **.txt** por padrao.

---

## R5 — VERIFICACAO ADVERSARIAL (RED-TEAM)

Mude de chapeu: voce AGORA e a parte contraria / o juizo cetico. Unica missao: DERROTAR a peca. Achou UMA falha → REPROVADO.

- **POSSE x PROPRIEDADE** — a peca discute posse onde devia (possessoria nao discute dominio — Sum. 487)? via correta (possessoria x petitoria; despejo x cobranca)?
- **VALORES** — debito/purgacao/quantum vem do `calculos-imobiliarios`? reajuste/multa corretos?
- **LIMINAR/PRAZO** — liminar de despejo so nas hipoteses do art. 59 §1º + caucao? renovatoria no prazo decadencial (art. 51 §5º)?
- **COMPETENCIA/FORO** — foro da situacao do imovel (art. 47 CPC) para acoes reais?
- **CITACOES** — Sum. 380/619 e demais batem em tese? (atencao: 380=mora na revisional; 619=detencao de bem publico.)
- **GARANTIA** — vedada cumulacao de garantia locaticia (art. 37)?

**Veredito R5:** PASSOU / REPROVADO (eixo+falha+correcao).

## FICHA DE CONFERENCIA (acompanha a entrega, nao integra a peca)

```
FICHA DE CONFERENCIA — pre-protocolo
- PREMISSAS: ...
- IMOVEL (matricula/area) e CONTRATO conferidos: ...
- VALORES (cada R$ → fonte): R$ __ — origem calculos-imobiliarios
- CITACOES (cada uma → status): ... — CONFIRMADO | VALIDAR
- LACUNAS [INFORMAR]: ...
- RISCOS / PONTOS ADVERSARIAIS: ...
- VEREDITO: R1 _ · R2 _ · R3 _ · R4 _ · R5 _
- PENDE O OK INFORMADO DO ADVOGADO antes do protocolo.
```

---

## SAIDA

```
R1 fundamentos/jurisprudencia: OK / CORRIGIR — [notas]
R2 fatos/imovel/prazos:        OK / CORRIGIR — [notas]
R3 polo/via/posse-propriedade: OK / CORRIGIR — [notas]
R4 forma/foro/sigilo:          OK / CORRIGIR — [notas]
R5 adversarial (red-team):     PASSOU / REPROVADO — [eixo+falha+correcao]
VEREDITO: LIBERADO / RETIDO
```
**RETIDO** em qualquer R1-R5 (ou REPROVADO no R5) → volta a skill de origem. Nunca entregar com R pendente (PA-13). Toda entrega vai acompanhada da **FICHA DE CONFERENCIA** preenchida. Apos LIBERADO → atualizar `CASO.md` (memoria-de-caso-imobiliario).
