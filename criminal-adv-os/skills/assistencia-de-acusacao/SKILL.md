---
name: assistencia-de-acusacao
description: >
  Skill Tier 2 — polo da VITIMA/ofendido: assistente de acusacao (CPP 268-273). Cobre a habilitacao do
  assistente apos recebida a denuncia, os poderes do assistente (propor meios de prova, requerer perguntas
  as testemunhas, aditar/arrazoar, participar dos debates, recorrer subsidiariamente — CPP 271 e 598),
  o interesse na condenacao e na reparacao do dano (efeito civil da sentenca, valor minimo CPP 387 IV) e os
  limites da atuacao. Distingue a assistencia da acao penal privada (queixa-crime) e da acao penal privada
  subsidiaria da publica (CPP 29 — inercia do MP). LADO OPOSTO do plugin: manter rigorosa coerencia de polo
  (PA-10). Estrutura do pedido de habilitacao e da atuacao. Ative em assistente de acusacao, vitima,
  ofendido, habilitacao do assistente, queixa-crime, acao privada subsidiaria, reparacao a vitima.
metadata:
  version: "0.1.0"
  area: "Direito Penal e Processo Penal"
  tier: 2
---

# ASSISTENCIA DE ACUSACAO (CPP 268-273)

> Tier 2. **Polo oposto** ao da defesa: representa a **vitima/ofendido**, em auxilio ao MP. Coerencia de polo e absoluta (PA-10) — nesta skill, todo argumento e pro condenacao/reparacao. Selo P1 antes de produzir.

---

## 1. QUEM PODE SER ASSISTENTE (CPP 268-269)

- O **ofendido** ou seu representante legal; na falta/incapacidade/morte, o **CADI** (conjuge, ascendente, descendente, irmao — CPP 31).
- Atua **ao lado do MP** na **acao penal publica** (jamais contra ele). O reu nao pode intervir como assistente do MP.
- Admissao **enquanto nao transitar em julgado** (CPP 269); recebido o processo no estado em que se acha.
- Decisao que admite/inadmite **nao comporta recurso** (CPP 273), mas cabe mandado de seguranca/HC conforme o caso (validar).

## 2. PODERES DO ASSISTENTE (CPP 271)

- **Propor meios de prova** e requerer perguntas as testemunhas;
- **Aditar** os articulados (nos limites legais), **participar dos debates** orais e apresentar **memoriais**;
- **Arrazoar** os recursos do MP;
- **Recorrer supletivamente** (subsidiariamente) — apelacao quando o MP nao recorre (CPP 598; Sum. 210 STF — validar) e em outras hipoteses reconhecidas (ex.: contra impronuncia/absolvicao — validar).
- Requerer a fixacao do **valor minimo de reparacao** (CPP 387 IV) e ter interesse no efeito civil da condenacao.

## 3. LIMITES

- O assistente **nao** tem iniciativa da acao (que e do MP) nem dispoe do conteudo da imputacao.
- Atuacao **subsidiaria e supletiva** — nao substitui o MP, exceto na hipotese de **inercia** (acao privada subsidiaria, abaixo).
- Sigilo reforçado quanto a dados da vitima (PA-09); vedado uso da posicao para fins estranhos a persecucao (PA-08).

## 4. DISTINCOES IMPORTANTES

| Figura | Natureza | Base |
|--------|----------|------|
| **Assistente de acusacao** | Auxilia o MP na **acao publica** | CPP 268-273 |
| **Querelante (queixa-crime)** | Titular da **acao penal privada** (crimes contra a honra, etc.) | CPP 30, 100 §2º |
| **Acao privada subsidiaria** | Vitima ajuiza **diante da inercia** do MP (nao havendo arquivamento) | CF 5 LIX; CPP 29 |

> Na acao **privada subsidiaria** (CPP 29), o MP retoma poderes de fiscal, pode aditar, repudiar a queixa e oferecer denuncia substitutiva; a negligencia do querelante leva o MP a assumir a acao.

## 5. INTERESSE NA REPARACAO

- A sentenca penal condenatoria e **titulo executivo** no civel (CPP 63; CPC 515 VI); o juiz **fixa valor minimo** de reparacao (CPP 387 IV) — o assistente deve **requerer e instruir** esse pedido com prova do dano.

## 6. ESTRUTURA DO PEDIDO DE HABILITACAO

1. Enderecamento (juizo da acao penal) · 2. Qualificacao do ofendido/legitimado e do advogado · 3. Demonstracao da **legitimidade** (condicao de vitima/CADI) · 4. Fundamento (CPP 268) · 5. Pedido de **admissao como assistente** + intimacao dos atos + requerimento de provas/valor minimo de reparacao · 6. Documentos (procuracao, prova da condicao de ofendido, BO).

## 7. ESTRUTURA DA ATUACAO (manifestacoes/recurso)

- **Manifestacao probatoria/memoriais**: reforco da prova de acusacao, confronto da tese defensiva, pedido de condenacao e de valor minimo de reparacao (CPP 387 IV).
- **Apelacao supletiva** (MP inerte): interposicao + razoes demonstrando o acerto da condenacao buscada ou o desacerto da absolvicao/impronuncia.

## 8. INTEGRACAO

- `calculos-criminais` → suporte a dosimetria e a fixacao do valor minimo de reparacao.
- `jurisprudencia-criminal` → validar Sum. 210 STF e teses de legitimidade recursal (PA-01).
- `analise-documental-criminal` → BO, laudos, prova do dano.
- `estilo-juridico-criminal` → forma · `revisao-final-criminal` → R1-R4.

## 9. CHECKLIST DE SAIDA

- [ ] Legitimidade do assistente demonstrada (ofendido/CADI — CPP 268, 31)
- [ ] Atuacao **ao lado** do MP, sem usurpar a titularidade (limites)
- [ ] Distincao correta: assistencia x queixa-crime x acao subsidiaria (CPP 29)
- [ ] Pedido de valor minimo de reparacao instruido (CPP 387 IV)
- [ ] Recurso supletivo so nas hipoteses cabiveis (Sum. 210 — PA-01)
- [ ] Sigilo da vitima preservado (PA-09)
- [ ] **POLO CORRETO: acusacao** — coerencia integral (PA-10) · Selo P1 feito · R1-R4 pendente
