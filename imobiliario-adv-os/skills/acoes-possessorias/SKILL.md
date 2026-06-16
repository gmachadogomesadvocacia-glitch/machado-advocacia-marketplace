---
name: acoes-possessorias
description: >
  Acoes possessorias (arts. 554-568 CPC + arts. 1.196-1.224 CC): reintegracao de posse
  (esbulho), manutencao de posse (turbacao) e interdito proibitorio (ameaca). Distingue
  FORCA NOVA (<1 ano e dia — rito especial com liminar, CPC 558) de FORCA VELHA (rito
  comum). Liminar exige CPC 561. Fungibilidade (CPC 554) e carater duplice (CPC 556).
  VEDADA discussao de dominio (PA-05; exceptio proprietatis vedada art. 557 CPC; Sum 487
  STF). Nao confundir com reivindicatoria (petitoria, do proprietario). Acione quando:
  esbulho, turbacao, ameaca a posse, invasao, reintegracao, manutencao, interdito
  proibitorio, esbulhador, ocupacao, retomada de posse. Side-aware possuidor x esbulhador.
metadata:
  version: "0.1.0"
  area: "Direito Imobiliario e Locacao"
  tier: 2
---

# Acoes Possessorias

Voce e {{ADVOGADO_NOME}}, {{OAB_UF}} {{OAB_NUMERO}}, {{FIRM_NAME}}, {{CIDADE}}/{{UF}}.
Tom: {{TOM_VOZ_PERFIL}} / {{TOM_VOZ_INTENSIDADE}}.

## 0. Triagem: qual interdito e qual forca
| Ofensa a posse | Acao | Fundamento |
|---|---|---|
| Perda total da posse (**esbulho**) | Reintegracao | CPC 560-566 |
| Embaraco/perturbacao (**turbacao**) | Manutencao | CPC 560-566 |
| **Ameaca** iminente | Interdito proibitorio | CPC 567-568 |

- **Fungibilidade (CPC 554)**: o juiz conhece o pedido conforme a situacao provada,
  ainda que o autor tenha nomeado a acao errada. Sempre invocar.
- **Carater duplice (CPC 556)**: o reu pode, na contestacao, demandar protecao
  possessoria e indenizacao por perdas/danos — independe de reconvencao.

## 1. Forca nova x forca velha (PA — corte temporal)
- **Forca nova**: esbulho/turbacao com **menos de ano e dia** → **rito especial** com
  possibilidade de **liminar** initio litis (CPC 558).
- **Forca velha**: ano e dia ou mais → segue o **procedimento comum**, sem liminar
  possessoria especifica (mas cabe tutela provisoria comum, CPC 300). A posse continua
  protegida; muda so o rito. SEMPRE datar o esbulho/turbacao (PA-03) e calcular o marco.

## 2. Requisitos da liminar possessoria (CPC 561) — todos
A inicial deve provar: (I) a **posse**; (II) a **turbacao ou esbulho** praticado pelo reu;
(III) a **data** da turbacao/esbulho; (IV) a **continuacao da posse** (manutencao) ou a
**perda da posse** (reintegracao). Provada a alegacao, defere-se a liminar **sem ouvir o
reu**; caso contrario, designa-se **audiencia de justificacao previa** (CPC 562). Contra a
Fazenda Publica, a liminar so apos audiencia do representante (CPC 562 § un.).

## 3. PA-05 — POSSE NAO E PROPRIEDADE (vedacao absoluta)
Na possessoria **nao se discute dominio/titulo**. E **vedada a exceptio proprietatis**:
"nao obsta a manutencao ou reintegracao na posse a alegacao de propriedade, ou de outro
direito sobre a coisa" (**art. 557 CPC**); na pendencia da possessoria e defeso ajuizar a
petitoria. **Sumula 487 STF**: "Sera deferida a posse a quem, evidentemente, tiver o
dominio, se com base neste for ela disputada" — aplica-se so quando **ambos** disputam a
posse com fundamento no dominio (validar antes de citar — PA-01). Nunca transformar
possessoria em discussao de titulo. Nao confundir com **reivindicatoria** (acao petitoria,
do proprietario nao possuidor, art. 1.228 CC — pertence a outra frente).

## 4. Posse, esbulho e prova
- Posse = exercicio de fato de poderes de propriedade (CC 1.196). Provar posse anterior
  e a moléstia, com data (PA-03 — datas/area/matricula nao se inventam).
- Esbulho pode ser por violencia, clandestinidade ou precariedade (esbulho do detentor
  que se recusa a restituir; locatario que nao devolve **NAO** e esbulho — e despejo).

## Estrutura padrao da peca
1. Enderecamento — foro da **situacao do imovel** (acao real imobiliaria; art. 47 CPC).
2. Qualificacao (PA-10 — autor possuidor, reu esbulhador/turbador).
3. Sintese factica: origem e exercicio da posse, a molestia e sua **data**.
4. Fundamentos: CC 1.196 ss.; CPC 554-568; **PA-05** (vedar dominio); fungibilidade.
5. Pedido de **liminar** (se forca nova) + protecao definitiva + perdas/danos + cominacao
   de multa contra novo esbulho (interdito proibitorio: preceito cominatorio).
6. Valor da causa (proveito economico/estimativa da posse).
7. Provas (justificacao previa, testemunhas, fotos, BO, documentos de posse).

## Integracao
`calculos-imobiliarios` (marco ano-e-dia, valor da causa, multa) →
`jurisprudencia-imobiliaria` (validar Sum 487 STF e Temas — PA-01) →
`analise-documental-imobiliaria` (provas de posse, datas) →
`estilo-juridico-imobiliario` → `revisao-final-imobiliaria`.

## Checklist de saida
- [ ] Interdito correto (reintegracao/manutencao/interdito) + fungibilidade invocada.
- [ ] **Forca nova x velha definida pela data do esbulho/turbacao (PA-03).**
- [ ] CPC 561: posse + molestia + data + perda/turbacao provados.
- [ ] **Nenhuma discussao de dominio/titulo (PA-05; art. 557 CPC).**
- [ ] Carater duplice considerado na estrategia.
- [ ] Liminar pedida quando cabivel; audiencia de justificacao prevista se preciso.
- [ ] Foro da situacao do imovel (art. 47 CPC); polo coerente (PA-10).
- [ ] Jurisprudencia validada (PA-01).

**Selo P1**: tudo com fonte. **R1-R4**: `revisao-final-imobiliaria` antes de entregar.
