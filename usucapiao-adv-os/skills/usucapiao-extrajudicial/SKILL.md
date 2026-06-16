---
name: usucapiao-extrajudicial
description: >
  USUCAPIAO EXTRAJUDICIAL — Skill Tier 2 (lado usucapiente), via cartorio. Conduz o procedimento de
  usucapiao administrativa no Registro de Imoveis (CPC art. 1.071 + Lei 6.015 art. 216-A + Provimento
  CNJ): ata notarial atestando o tempo de posse, planta e memorial descritivo com ART/responsavel
  tecnico, anuencia dos confrontantes e titulares (e o tratamento da falta de anuencia/silencio), o
  requerimento dirigido ao oficial do RI, e o caminho da impugnacao. Acione quando ha CONSENSO e a via
  for extrajudicial. Havendo litigio/oposicao, encaminhar para a via judicial (acao-usucapiao). Exige
  Selo P1.
metadata:
  version: "0.1.0"
  area: "Usucapiao (Judicial e Extrajudicial)"
  tier: 2
---

# USUCAPIAO EXTRAJUDICIAL (cartorio)

> Skill **Tier 2** — lado usucapiente, via administrativa. So roda apos triagem, Selo P1 e a confirmacao de que ha **consenso** (sem litigio).

---

## 0. PRE-REQUISITOS
- Via = extrajudicial. **Sem litigio/oposicao** — havendo, vai para `acao-usucapiao` (PA-07).
- **Selo P1** emitido. Modalidade definida. Bem nao publico (PA-04).
- Imovel com descricao tecnica (planta/memorial + **ART**) e os confrontantes identificados.

## 1. PECAS DO PROCEDIMENTO (Lei 6.015 art. 216-A)
1. **Ata notarial** (tabeliao) atestando o **tempo de posse** do requerente e seus antecessores.
2. **Planta e memorial descritivo** assinados por profissional habilitado (com **ART/RRT**) e pelos titulares dos imoveis confinantes.
3. **Certidoes** negativas dos distribuidores (do imovel e do requerente).
4. **Justo titulo** ou quaisquer documentos que demonstrem a posse e sua origem (IPTU, contas, benfeitorias).
5. **Anuencia** dos titulares de direitos sobre o imovel e dos **confrontantes**.

## 2. ANUENCIA E SILENCIO (ponto critico)
- Confrontante que **assina** a planta = anui.
- Confrontante **notificado** (pelo oficial ou pelo tabeliao) que **NAO responde em 15 dias** → o **silencio e interpretado como CONCORDANCIA** (Lei 6.015 art. 216-A §2º, redacao atual). Verificar a redacao vigente no Selo (PA-01).
- Confrontante que **discorda** → instaura-se litigio → a via vira **judicial**.

## 3. FLUXO NO RI
Requerimento dirigido ao **oficial do Registro de Imoveis** da circunscricao (P5), autuado e prenotado. O oficial pode notificar confrontantes/entes, exigir diligencias, e ao final **registrar** (abrir matricula) ou **rejeitar/encaminhar a impugnacao**.

## 4. ESTRUTURA DO REQUERIMENTO
Qualificacao do requerente · descricao do imovel (matricula/sem registro · metragem · confrontacoes) · **modalidade e tempo de posse** · fundamento (art. 1.071 CPC + 216-A Lei 6.015 + Provimento CNJ) · relacao dos documentos (ata, planta+ART, certidoes, anuencias) · pedido de registro/abertura de matricula.

## 5. CHECKLIST
- [ ] Consenso confirmado (sem litigio — PA-07) · modalidade correta (PA-05)
- [ ] Ata notarial · planta+ART · anuencias (ou silencio = concordancia, verificado)
- [ ] Bem nao publico (PA-04) · RI da circunscricao correta (P5)
- [ ] `revisao-final-usucapiao` R1-R4 (PA-13)

## 6. ENCERRAMENTO
Entrega o requerimento e o conjunto documental para o RI. Surgindo oposicao a qualquer momento, migrar para `acao-usucapiao` (judicial).
