---
name: responsabilidade-estado
description: >
  Tier 2 — responsabilidade civil do ESTADO / Fazenda Publica (Uniao, Estados, Municipios,
  autarquias, fundacoes e prestadoras de servico publico). Cobre os dois polos: AUTOR/lesado (acao
  indenizatoria) e REU/ente publico (defesa). RESPONSABILIDADE OBJETIVA (CF 37 §6º — teoria do RISCO
  ADMINISTRATIVO: conduta + dano + nexo, dispensada a culpa) e suas EXCLUDENTES (culpa exclusiva da
  vitima, caso fortuito/forca maior, fato de terceiro). OMISSAO — responsabilidade subjetiva/faute du
  service x objetiva (controverso — validar). Denunciacao da lide ao agente / acao de regresso (dolo ou
  culpa — CF 37 §6º). PRESCRICAO quinquenal (Decreto 20.910/32 — 5 anos contra a Fazenda; validar tese
  atual). Particularidades: prazos processuais, precatorio/RPV, REEXAME NECESSARIO (CPC 496), juros e
  correcao (Lei 11.960/09; Tema 810 STF / 905 STJ — validar). Ative em indenizacao contra o Estado/
  Municipio/Uniao/INSS/autarquia, responsabilidade do poder publico, erro do Estado, risco
  administrativo, dano por agente publico ou Fazenda Publica. (Pode migrar a plugin administrativo.)
metadata:
  version: "0.1.0"
  area: "Direito Civil e Processo Civil"
  tier: 2
---

# RESPONSABILIDADE CIVIL DO ESTADO (CF 37 §6º; Dec. 20.910/32)

> Tier 2. Side-aware: **AUTOR/lesado** x **REU/Fazenda Publica** (defesa). Peca e tom mudam (PA-10).
> **Atencao (PA-09):** materia limitrofe com o administrativo. Aqui, o recorte e a **reparacao civil** contra o ente. Demanda especificamente administrativa (servidor, licitacao, tributo) → rotear/sinalizar.

---

## 1. REGIME — RISCO ADMINISTRATIVO (CF 37 §6º)

- **Objetiva** para pessoas juridicas de direito publico e de direito privado **prestadoras de servico publico**, por dano que seus **agentes**, nessa qualidade, causarem a terceiros.
- Pressupostos (dispensa-se a culpa): **conduta** do agente + **dano** + **nexo causal**.
- **Teoria do risco administrativo** (nao integral) → admite **excludentes**:
  - culpa **exclusiva** da vitima (culpa concorrente atenua);
  - caso fortuito / forca maior;
  - fato exclusivo de terceiro (conforme o caso).

## 2. OMISSAO (controverso — validar)

- Corrente classica: omissao → responsabilidade **subjetiva** (*faute du service* — falta do servico: nao funcionou, funcionou mal ou tardiamente), exigindo dever juridico de agir + culpa.
- Tendencia do STF em certos casos (dever especifico de protecao, custodia — presos, alunos): **objetiva**. **Validar o estado atual da jurisprudencia (PA-01)** antes de afirmar.

## 3. REGRESSO E DENUNCIACAO DA LIDE

- O ente responde objetivamente perante a vitima; tem **direito de regresso** contra o agente que agiu com **dolo ou culpa** (CF 37 §6º, parte final — responsabilidade **subjetiva** do agente).
- Acao direta contra o agente: discutida (teoria da dupla garantia — STF tende a admitir so contra o ente; **validar**).
- Denunciacao da lide ao agente (CPC 125 II) — admissivel, mas pode ser indeferida para nao introduzir fundamento novo (culpa) na lide objetiva.

## 4. PRESCRICAO

- **Quinquenal** contra a Fazenda Publica (**Decreto 20.910/32** — 5 anos) — prevalece sobre o trienio do CC para o lesado contra o ente (tese consolidada; **validar** — PA-05).
- Termo inicial: do fato/ciencia inequivoca do dano.

## 5. JUROS, CORRECAO E LIQUIDACAO (PA-06)

- **Lei 11.960/09** (alterou a Lei 9.494/97) — regime de juros e correcao das condenacoes contra a Fazenda.
- **Tema 810 STF / Tema 905 STJ** — modulacao dos indices (correcao por IPCA-E em condenacoes nao tributarias; juros conforme o caso). **Validar os indices vigentes** antes de fixar (PA-01/PA-06).

## 6. PARTICULARIDADES PROCESSUAIS

- **Foro:** Justica Federal (CF 109 I) para Uniao/autarquias/empresas publicas federais; Justica Estadual (Fazenda Publica) para Estado/Municipio.
- **Prazos em dobro** para a Fazenda (CPC 183).
- **Reexame necessario** (CPC 496) — sentenca contra a Fazenda nao transita sem confirmacao do tribunal, salvo as excecoes de valor/precedente (CPC 496 §3º/§4º).
- **Pagamento:** precatorio (regra) ou RPV (pequeno valor) — CF 100.
- Citacao da Fazenda; intervencao obrigatoria; contestacao pela procuradoria.

## 7. ESTRUTURA DA PECA

**Acao indenizatoria (autor):** 1. Enderecamento (Vara da Fazenda Publica / Justica Federal — CF 109) · 2. Qualificacao (ente correto no polo passivo) · 3. Dos fatos (conduta do agente + dano) · 4. Do direito (CF 37 §6º — risco administrativo; nexo; afastar excludentes) · 5. Dos danos e quantum · 6. Pedidos (condenacao + juros/correcao Lei 11.960 + sucumbencia) · 7. Valor da causa · 8. Provas.
**Defesa (Fazenda):** excludentes (culpa exclusiva da vitima, fortuito); inexistencia de nexo/dano; em omissao, ausencia de culpa/dever especifico; prescricao quinquenal; impugnar quantum e indices.

## 8. INTEGRACAO

- `calculos-civeis` → liquidacao, juros/correcao (Lei 11.960; Tema 810/905 — validar), prescricao (PA-06/PA-05).
- `jurisprudencia-civel` → validar omissao, dupla garantia, Temas 810/905, prescricao (PA-01).
- `analise-documental-civel` → prova da conduta do agente, do dano e do nexo.
- `estilo-juridico-civel` → forma · `revisao-final-civel` → R1-R4.

## 9. CHECKLIST DE SAIDA

- [ ] Polo passivo correto (ente especifico, nao o agente) · foro (JF x Fazenda estadual — P5/PA-09)
- [ ] Regime: objetivo CF 37 §6º (acao) x omissao (subjetivo — validar PA-01)
- [ ] Excludentes enfrentadas/antecipadas · nexo demonstrado
- [ ] Prescricao quinquenal (Dec. 20.910 — validar PA-05)
- [ ] Juros/correcao Lei 11.960 + Tema 810/905 marcados "validar" (PA-06/PA-01)
- [ ] Reexame necessario e precatorio/RPV considerados · Polo coerente (PA-10) · Selo P1 · R1-R4 pendente
