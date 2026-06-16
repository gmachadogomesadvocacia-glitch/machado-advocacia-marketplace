---
name: revisao-final-imobiliaria
description: >
  Revisao final Tier 3 — Suprema Corte R1-R4. Ultima barreira antes de qualquer entrega de peca,
  contrato, parecer ou calculo imobiliario/locaticio. R1 valida fundamentos (Lei 8.245, CC, Lei 9.514,
  Lei 4.591, Lei 6.015, Lei 13.786 vigentes no contrato/fato) e jurisprudencia (Sumula/Tema STF/STJ)
  contra alucinacao (PA-01/PA-02/PA-04); R2 audita fatos, matricula, area, valores, datas e prazos
  (decadencia da renovatoria, purgacao da mora — PA-03/PA-07); R3 verifica coerencia de polo, via
  processual e a distincao posse x propriedade (PA-05/PA-10); R4 confere forma, foro do imovel, garantia,
  sigilo e LGPD (PA-12). Ative SEMPRE antes de entregar qualquer produto imobiliario ao usuario.
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

## SAIDA

```
R1 fundamentos/jurisprudencia: OK / CORRIGIR — [notas]
R2 fatos/imovel/prazos:        OK / CORRIGIR — [notas]
R3 polo/via/posse-propriedade: OK / CORRIGIR — [notas]
R4 forma/foro/sigilo:          OK / CORRIGIR — [notas]
VEREDITO: LIBERADO / RETIDO
```
**RETIDO** em qualquer R → volta a skill de origem. Nunca entregar com R pendente (PA-13). Apos LIBERADO → atualizar `CASO.md` (memoria-de-caso-imobiliario).
