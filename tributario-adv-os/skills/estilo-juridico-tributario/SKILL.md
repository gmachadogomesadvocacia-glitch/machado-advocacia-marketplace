---
name: estilo-juridico-tributario
description: >
  Camada 3 — estilo das pecas tributarias. Ative na formatacao final de qualquer peca tributaria, ao ajustar tom, estrutura ou redacao.
metadata:
  version: "0.1.0"
  area: "Direito Tributario"
  tier: 1
---

# ESTILO JURIDICO TRIBUTARIO (Camada 3)

> Tier 1. Camada de **forma** aplicada na finalizacao de toda peca. Tom `{{TOM_VOZ_PERFIL}}`, intensidade `{{TOM_VOZ_INTENSIDADE}}/10`. Combatividade **dirigida a teses**, nunca a pessoas.

---

## 1. PRINCIPIOS

- **Enxuto** — ~5 paginas quando couber; cortar repeticao e citacao decorativa.
- **Tecnico** — linguagem fiscal precisa; sem floreio.
- **Documentos numerados "doc. N"**, citados por numero no corpo; **sem rol de documentos ao final**.
- **Antecipacao adversarial dura** — enfrentar a tese fazendaria mais forte de frente (vinda da `analise-trilateral-tributaria`).
- **Datas e valores** sempre lastreados (`analise-documental` + `calculos`).

## 2. ESTRUTURA PADRAO DA PECA

1. **Enderecamento** — juizo/orgao competente (eixo de foro: JF para tributo federal; estadual para ICMS/IPVA/ISS; DRJ/CARF no administrativo).
2. **Qualificacao** — partes; assinatura de `{{ADVOGADO_NOME}}`, `{{OAB_UF}}` `{{OAB_NUMERO}}`, `{{FIRM_NAME}}`, `{{CIDADE}}`/`{{UF}}`, `{{EMAIL}}`.
3. **Sintese** — o que e a cobranca/auto/CDA e o que se pede (objetiva).
4. **Fundamentos** — fato (com doc. N) → direito (CTN/LEF + jurisprudencia **validada**, PA-01) → tese.
5. **Pedidos** — determinados (extincao/anulacao, suspensao da exigibilidade, levantamento de garantia, CND).
6. **Valor da causa** — coerente com o proveito economico.
7. **Provas** — documentais pre-constituidas; pericia so quando indispensavel (em excecao, nunca — PA-07).

> Procuracao por ultimo. Documentos numerados antes do protocolo e citados por numero.

## 3. LINGUAGEM FISCAL CORRETA

- **Decadencia x prescricao** (PA-05): decadencia = perda do direito de **constituir** (antes do lancamento, CTN 173/150); prescricao = perda do direito de **cobrar** (apos a constituicao, CTN 174). Nunca trocar.
- **Elisao x evasao** (PA-06): elisao = planejamento licito (ato valido, anterior ao fato gerador); evasao/sonegacao = ilicito. Nunca chamar de elisao o que e evasao.
- **Multa de mora x multa de oficio**; **deposito x penhora x seguro garantia**; **isencao x imunidade x nao incidencia**.
- **Sujeito passivo**: contribuinte x responsavel (CTN 121); coerencia de polo (PA-10).

## 4. TOM E COMBATIVIDADE

- Intensidade `{{TOM_VOZ_INTENSIDADE}}/10` calibra a forca retorica; o alvo e sempre a **tese** fazendaria, com respeito institucional.
- Afirmacao juridica = norma + fato + (quando houver) jurisprudencia validada. Sem afirmacao sem lastro (PA-02/PA-03).

## 5. CHECKLIST DE ESTILO

- [ ] ~5 paginas, sem repeticao
- [ ] doc. N citados por numero, sem rol ao final
- [ ] decadencia/prescricao e elisao/evasao usados corretamente
- [ ] pedidos determinados + valor da causa coerente
- [ ] tom `{{TOM_VOZ_PERFIL}}` na intensidade definida
- [ ] entrega em .txt · pronto para `revisao-final-tributaria` (R1-R4)

> Gatilho "gera docx": converter a peca .txt em .docx no papel timbrado via `gerador-peticoes` (Garamond 12) — Code.
