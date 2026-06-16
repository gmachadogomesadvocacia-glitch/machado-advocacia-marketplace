---
name: indicacao-condutor
description: >
  Skill Tier 2 — INDICACAO DO REAL CONDUTOR INFRATOR (CTB 257 §7º). Quando a infracao e de
  responsabilidade do condutor e o autuado e o PROPRIETARIO (PJ ou PF), permite transferir a pontuacao a
  quem efetivamente dirigia. Prazo e formalidades: formulario proprio (FICI), copia da CNH e assinaturas
  do proprietario e do condutor indicado, no prazo da Notificacao de Autuacao. Nao indicar → multa ao
  proprietario por nao identificacao (CTB 257 §8º) e a pontuacao recai sobre ele. ALERTA PA-06: a
  indicacao deve ser do condutor REAL — indicacao falsa e CRIME (art. 299 CP, falsidade ideologica);
  JAMAIS orientar fraude de pontuacao. Ative em indicacao de condutor, transferir pontos, real condutor
  infrator, FICI, ou multa de veiculo de empresa.
metadata:
  version: "0.1.0"
  area: "Direito de Transito"
  tier: 2
---

# INDICACAO DO REAL CONDUTOR INFRATOR (CTB 257 §7º)

> Tier 2. Mecanismo legitimo para que a pontuacao recaia sobre quem **realmente** dirigia, nao sobre o proprietario. Persona: {{ADVOGADO_NOME}} ({{OAB_UF}} {{OAB_NUMERO}}), {{FIRM_NAME}}. Tom: {{TOM_VOZ_PERFIL}} / {{TOM_VOZ_INTENSIDADE}}.

---

## ⚠️ ALERTA PA-06 (LIMITE ABSOLUTO E INVIOLAVEL)

- A indicacao deve apontar o **condutor REAL**. Indicar pessoa que **nao** dirigia (para "diluir" pontos, usar CNH de terceiro, "vender" pontos) e **CRIME — falsidade ideologica (art. 299 do Codigo Penal)**, alem de infracao administrativa.
- **NUNCA** orientar, sugerir, redigir ou facilitar indicacao falsa, "esquema de pontos" ou uso de laranja. Se o cliente pedir, **recusar** e alertar sobre a tipificacao penal.
- A atuacao legitima e: orientar a **identificar corretamente** o condutor e instruir o requerimento de forma regular.

## 1. CABIMENTO

- Infracoes de **responsabilidade do condutor** (a maioria das de comportamento ao volante) lavradas contra o **proprietario** (tipico em veiculo de PJ / frota / familia).
- Nao cabe nas infracoes de responsabilidade do **proprietario** (ex.: documentacao do veiculo), pois nelas a pontuacao ja e dele.

## 2. PRAZO E FORMALIDADES (CTB 257 §7º)

- **Prazo:** o da **Notificacao de Autuacao (NA)** — em regra 30 dias (PA-05, preclusivo; conferir a data na NA — PA-03).
- **Documentos:** formulario proprio (FICI — Formulario de Identificacao do Condutor), com:
  - **assinatura do proprietario** e **assinatura do condutor indicado** (anuencia);
  - **copia da CNH** do condutor indicado;
  - dados completos de ambos.
- Falta de qualquer requisito → indicacao **nao processada**, mantendo a pontuacao no proprietario.

## 3. CONSEQUENCIA DA NAO INDICACAO (CTB 257 §8º)

- Nao identificado o condutor no prazo, **alem da multa da infracao**, aplica-se ao **proprietario** a penalidade do **CTB 257 §8º** (multa por nao indicacao) — e, sendo PJ, a pontuacao e convertida em multa (validar regra vigente — PA-04, atencao a Lei 14.071).

## 4. ESTRUTURA DO REQUERIMENTO DE INDICACAO

1. **Enderecamento** — ao orgao/entidade autuador (consta no AIT/NA).
2. **Identificacao do auto** — nº AIT, placa, data/local, infracao.
3. **Qualificacao do proprietario** e **do condutor real indicado** (com CNH).
4. **Declaracao** de que o condutor indicado conduzia o veiculo no momento (verdadeira — PA-03/PA-06).
5. **Pedido** — processamento da indicacao e transferencia da pontuacao ao condutor identificado.
6. **Documentos** — FICI assinado por ambos + copia da CNH do indicado.
7. Fecho, local/data; assinaturas. (O advogado instrui; quem assina e o proprietario/condutor.)

## 5. INTEGRACAO

- `defesa-autuacao` → a indicacao pode acompanhar/preceder a defesa previa no mesmo prazo.
- `suspensao-direito-dirigir` → indicacao regular exclui pontos do proprietario da soma.
- `analise-documental-transito` → conferir FICI, CNH, assinaturas.
- `calculos-transito` → impacto na pontuacao. `jurisprudencia-transito` → validar CTB 257 (PA-01/PA-02).
- `estilo-juridico-transito`; `revisao-final-transito` → R1-R4.

## 6. CHECKLIST DE SAIDA

- [ ] CONDUTOR INDICADO E O REAL — sem fraude (PA-06; art. 299 CP) — confirmado
- [ ] Infracao e de responsabilidade do condutor (cabimento)
- [ ] Prazo da NA conferido (PA-05)
- [ ] FICI com assinatura do proprietario E do condutor + copia da CNH
- [ ] Consequencia da nao indicacao (CTB 257 §8º) explicada ao cliente
- [ ] Regra vigente na infracao (PA-04; Lei 14.071); nada inventado (PA-01/PA-02)
- [ ] Selo P1 feito · R1-R4 pendente
