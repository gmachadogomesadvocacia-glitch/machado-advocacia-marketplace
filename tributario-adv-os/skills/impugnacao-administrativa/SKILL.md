---
name: impugnacao-administrativa
description: >
  Redige impugnacao administrativa (defesa de 1a instancia) contra auto de
  infracao ou lancamento de oficio. Aciona quando o cliente recebeu auto de
  infracao, notificacao de lancamento, NFLD, AIIM, ou quer impugnar/contestar
  cobranca fiscal na esfera administrativa antes de ir ao Judiciario. Federal:
  Dec. 70.235/72 (PAF), prazo 30 dias, julgamento pela DRJ. Estadual/municipal:
  conferir lei do ente (validar). Efeito: suspende a exigibilidade do credito
  (CTN 151, III). Nao exige garantia/deposito. Cobre teses de nulidade do auto,
  vicio de motivacao, erro na base de calculo, decadencia, ilegitimidade e
  denuncia espontanea (CTN 138).
metadata:
  version: "0.1.0"
  area: "Direito Tributario"
  tier: 2
---

# Impugnacao Administrativa

Defesa do contribuinte na **1a instancia administrativa** contra auto de
infracao ou lancamento de oficio. Lado padrao: **contribuinte (defesa)**.

## Marco normativo
- **Federal:** Decreto 70.235/72 (Processo Administrativo Fiscal — PAF).
  Prazo de impugnacao: **30 dias** da ciencia do lancamento (art. 15).
  Julgamento em 1a instancia pela **DRJ** (Delegacia da Receita Federal de
  Julgamento). 2a instancia = CARF (ver `recurso-administrativo-carf`).
- **Estadual/Municipal:** o rito varia por ente — **conferir a lei do
  processo administrativo tributario do Estado/Municipio** (prazo, orgao
  julgador, nome da peca). **Marcar "validar conforme ente"** (PA-04). Nunca
  presumir que o prazo de 30 dias federal se aplica.

## Efeito imediato (CTN 151, III)
A impugnacao **tempestiva** suspende a exigibilidade do credito tributario.
Consequencias: nao corre a inscricao em divida ativa, nao ha execucao fiscal,
e o contribuinte tem direito a **CPD-EN** (certidao positiva com efeito de
negativa, CTN 206). **Nao se exige deposito, garantia ou arrolamento** para
impugnar (PA-11 — alertar o cliente que isso e vantagem da via administrativa).

## Estrutura da impugnacao
1. **Enderecamento** — ao Delegado/autoridade julgadora competente (DRJ no
   federal; orgao do ente no estadual/municipal — validar).
2. **Qualificacao** do impugnante (contribuinte autuado) e do auto/processo
   (numero do auto de infracao, processo administrativo, valor lancado).
3. **Tempestividade** — demonstrar a data da ciencia e o protocolo no prazo.
4. **Sintese factica** — o que foi autuado, tributo, periodo, fundamento do
   Fisco.
5. **Fundamentos / teses** (abaixo).
6. **Pedidos** — improcedencia do lancamento / cancelamento do auto /
   reducao; subsidiariamente, exclusao de multa ou juros indevidos.
7. **Provas** — documentos juntados, requerimento de pericia/diligencia.

## Teses recorrentes (defesa)
- **Nulidade do auto de infracao** — vicio formal: ausencia de requisitos do
  art. 10 do Dec. 70.235/72 (descricao do fato, capitulacao legal,
  determinacao da exigencia, assinatura do autuante).
- **Vicio de motivacao** — auto que nao demonstra o criterio de apuracao,
  impedindo o exercicio da defesa (cerceamento). Fundamentar no dever de
  motivacao do ato administrativo.
- **Erro na base de calculo / quantum** — apurar o valor correto; juntar
  memoria de calculo (acionar `calculos-tributarios`).
- **Decadencia (CTN 173, I, ou 150, §4o)** — o Fisco perdeu o prazo de 5 anos
  para **constituir** o credito (lancar). Distinguir rigorosamente
  **decadencia** (constituicao do credito) de **prescricao** (cobranca do
  credito ja constituido) — ver PA-05. Lancamento por homologacao com
  pagamento antecipado: termo inicial = fato gerador (CTN 150, §4o); sem
  pagamento ou com dolo/fraude/simulacao: CTN 173, I (1o dia do exercicio
  seguinte). **Validar a regra aplicavel ao caso.**
- **Ilegitimidade passiva** — autuacao contra quem nao e o sujeito passivo;
  ou responsabilizacao indevida de socio/administrador sem os requisitos do
  art. 135 do CTN (ver PA-08 e `defesa-execucao-fiscal` se ja houver redirec.).
- **Denuncia espontanea (CTN 138)** — se o contribuinte confessou e pagou o
  tributo + juros **antes** de qualquer procedimento fiscal, afasta-se a
  **multa**. Atencao: a Sumula 360/STJ (validar) afasta a espontaneidade para
  tributos sujeitos a lancamento por homologacao **declarados e nao pagos**.

## Onus probatorio
O **lancamento goza de presuncao de legitimidade**, mas o auto deve estar
motivado e instruido. A impugnacao deve trazer **prova pre-constituida** do
alegado (documentos contabeis, fiscais, notas). Requerer pericia/diligencia
quando o ponto for tecnico-contabil — fundamentar a necessidade.

## Pedidos tipicos
- Improcedencia do lancamento e **cancelamento integral** do auto.
- Subsidiariamente: reducao do credito ao valor correto; exclusao de multa
  (denuncia espontanea / multa confiscatoria) e revisao dos juros.
- Producao de prova pericial/documental.

## Proibicoes Absolutas aplicaveis
- **PA-01 / PA-02:** nao inventar jurisprudencia nem fundamentacao. Sumulas
  (ex.: 360/STJ) e Temas citados apenas se consagrados e marcados "validar".
- **PA-03:** nao alucinar fatos — so o que estiver nos documentos do cliente.
- **PA-04:** aplicar a norma vigente no fato gerador (tempus regit actum).
- **PA-05:** decadencia (CTN 173) x prescricao (CTN 174) — nao confundir.
- **PA-10:** coerencia de polo — peca de **defesa** do contribuinte.
- **PA-12:** sigilo fiscal (CTN 198) + LGPD nos dados juntados.

## Integracao e saida
- Calculo do quantum e da decadencia → **calculos-tributarios**.
- Sumulas/Temas/precedentes → **jurisprudencia-tributaria** (validar, PA-01).
- Redacao e tom → **estilo-juridico-tributario** (tokens de persona literais).
- Antes de entregar → **revisao-final-tributaria** (Selo P1 + R1-R4).

### Checklist de saida
- [ ] Tempestividade demonstrada (data de ciencia x protocolo).
- [ ] Enderecamento e orgao julgador corretos (ente validado).
- [ ] Teses de nulidade/decadencia/merito articuladas com prova.
- [ ] Pedidos claros (improcedencia + subsidiarios).
- [ ] Provas/diligencias requeridas.
- [ ] Coerencia de polo (defesa) e sigilo fiscal preservados.

**Lembrete:** aplicar **Selo P1** e auditoria **R1-R4** antes da entrega.
