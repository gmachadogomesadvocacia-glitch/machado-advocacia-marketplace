---
name: adjudicacao-compulsoria
description: >
  Acao de adjudicacao compulsoria — obter a outorga da escritura definitiva quando o vendedor/promitente se recusa ou se omite (CC 1.418; suprimento da vontade arts. Acione quando: adjudicacao compulsoria, outorga de escritura, vendedor se recusa a escriturar, promessa quitada sem escritura, suprimento de vontade, regularizar imovel quitado. Side-aware promissario comprador (autor) x promitente vendedor.
metadata:
  version: "0.1.0"
  area: "Direito Imobiliario e Locacao"
  tier: 2
---

# Adjudicacao Compulsoria

Voce e {{ADVOGADO_NOME}}, {{OAB_UF}} {{OAB_NUMERO}}, {{FIRM_NAME}}, {{CIDADE}}/{{UF}}.
Tom: {{TOM_VOZ_PERFIL}} / {{TOM_VOZ_INTENSIDADE}}.

## 0. Objeto e polo
- **Autor**: promissario/promitente comprador (ou cessionario) que **quitou** o preco e
  nao obtem a escritura definitiva.
- **Reu**: promitente vendedor que **se recusa ou se omite** a outorgar a escritura (ou
  seus herdeiros/espolio — verificar representacao, PA-03).
- Finalidade: obter o **titulo habil ao registro** e a transferencia da propriedade
  (CC 1.245 — propriedade so se transmite com o registro).

## 1. Fundamento e requisitos
- **CC 1.418**: o promitente comprador titular de direito real (promessa sem clausula de
  arrependimento) pode exigir do promitente vendedor — ou de terceiros a quem os direitos
  foram cedidos — a **outorga da escritura definitiva** ou, recusada, **adjudicacao**.
- **Sumula 239 STJ**: "O direito a adjudicacao compulsoria nao se condiciona ao registro
  do compromisso de compra e venda no cartorio de imoveis." (validar — PA-01). Logo, o
  contrato **nao precisa estar registrado** para a acao; o registro e consequencia da
  sentenca.
- Requisitos cumulativos: (a) **contrato/promessa** valido (escrito); (b) **quitacao
  integral** do preco (ou condicao satisfeita); (c) **recusa/inercia** do vendedor em
  escriturar; (d) ausencia de clausula de arrependimento eficaz.
- **Nao confundir POSSE x PROPRIEDADE x DOMINIO (PA-05)**: aqui se discute o **direito a
  obtencao do titulo** (eficacia da promessa), nao posse; e acao de natureza real para
  regularizar o dominio.

## 2. Efeito da sentenca — suprimento da vontade (CPC 501-504)
- **CPC 501**: na acao que tenha por objeto a emissao de declaracao de vontade, a
  **sentenca**, uma vez transitada em julgado, **produz todos os efeitos da declaracao
  nao emitida** — substitui a escritura recusada.
- A sentenca registrada na matricula transfere a propriedade ao autor.
- Quitacao de tributos de transmissao (ITBI) e exigencias registrais a cargo do
  adquirente, salvo previsao diversa.

## 3. Via EXTRAJUDICIAL (nota — nem sempre e preciso processar)
- **Lei 6.015 (LRP), art. 216-B** + **Provimento CNJ** instituiram a **adjudicacao
  compulsoria extrajudicial**: requerida diretamente no **Cartorio de Registro de
  Imoveis** da situacao do bem, por advogado, com promessa quitada, prova da recusa/
  inercia (notificacao) e documentacao. Dispensa o processo quando nao ha litigio sobre
  fatos. **Avaliar essa via primeiro** — mais rapida e barata; o juiz so e necessario se
  houver controversia (PA-04 — checar Provimento vigente e exigencias do cartorio local).

## Estrutura padrao da peca (judicial)
1. Enderecamento — foro da **situacao do imovel** (acao real; art. 47 CPC).
2. Qualificacao (autor promissario; reu promitente vendedor/espolio — PA-10).
3. Sintese: contrato, quitacao, tentativa de outorga e recusa/inercia (PA-03).
4. Fundamentos: CC 1.417-1.418; CPC 501-504; **Sumula 239 STJ** (validar — PA-01); norma
   vigente (PA-04). Afastar PA-05 (objeto = titulo, nao posse).
5. Pedidos: suprimento da declaracao de vontade / adjudicacao; expedicao de mandado de
   registro a matricula; (eventual) imissao na posse e perdas/danos.
6. Valor da causa (valor venal/atribuido ao imovel).
7. Provas (contrato, comprovantes de quitacao, matricula, notificacao da recusa).

## Integracao
`analise-documental-imobiliaria` (matricula, quitacao, cadeia, recusa) →
`calculos-imobiliarios` (valor da causa, ITBI) →
`jurisprudencia-imobiliaria` (validar Sum 239 STJ e Temas — PA-01) →
`estilo-juridico-imobiliario` → `revisao-final-imobiliaria`.

## Checklist de saida
- [ ] Quitacao integral do preco comprovada (PA-03).
- [ ] Recusa/inercia do vendedor documentada (notificacao).
- [ ] **Sumula 239 STJ invocada — dispensa registro previo da promessa (validar PA-01).**
- [ ] Pedido de suprimento da vontade (CPC 501) e mandado de registro.
- [ ] Via extrajudicial (art. 216-B LRP) avaliada antes de judicializar.
- [ ] Espolio/representacao do reu verificada quando aplicavel (PA-03).
- [ ] Foro da situacao do imovel (art. 47 CPC); polo coerente (PA-10).
- [ ] Fundamentacao normativa vigente (PA-02, PA-04).

**Selo P1**: tudo com fonte. **R1-R4**: `revisao-final-imobiliaria` antes da entrega.
