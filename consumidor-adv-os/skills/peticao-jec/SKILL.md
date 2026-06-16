---
name: peticao-jec
description: >
  PETICAO JEC — Skill Tier 2 transversal e side-aware. Redige a peticao para o Juizado Especial Civel
  (Lei 9.099/95) quando a triagem definiu o rito JEC. Cobre competencia e teto (ate 40 SM; ate 20 SM
  dispensa advogado), pedido simplificado e liquido, foro, vedacao a causas que exijam pericia complexa,
  conciliacao obrigatoria, revelia, recurso inominado e embargos de declaracao. Qualquer eixo
  (bancario, negativacao, telecom, aereo, produto) pode usa-la como a forma da peca no JEC. Acione
  quando o rito definido for JEC, o usuario pede peticao no juizado especial, causa de pequeno valor,
  acao no JEC, recurso inominado. Exige Selo P1 emitido.
metadata:
  version: "0.1.0"
  area: "Direito do Consumidor e Bancario"
  tier: 2
---

# PETICAO JEC

> Skill **Tier 2** transversal. E a **forma da peca** quando a triagem definiu rito **JEC** (Protocolo P5). **Side-aware:** redige pelo consumidor (autor) ou estrutura a defesa do fornecedor no juizado. So roda apos a triagem, o Selo P1 e a linha estrategica. A tese de merito vem do eixo (`acao-*` / `revisional-bancaria` / etc.); aqui mora o **rito**.

---

## 0. PRE-REQUISITOS

- **Rito = JEC** confirmado pela `linha-estrategica-consumidor` / triagem (Protocolo P5).
- **Selo de Validacao Legal Previa EMITIDO** (P1). Sem ele, nao redigir.
- Polo do cliente travado (PA-05). CASO.md com partes, valor da causa e documentos; falta de doc essencial → `[INFORMAR]` (PA-15).

## 1. COMPETENCIA E TETO (Lei 9.099)

- **Teto:** ate **40 salarios minimos** (art. 3º). Acima disso → vara comum (`peticao-inicial-consumidor`).
- **Capacidade postulatoria:** ate **20 SM** o autor **dispensa advogado** (art. 9º); acima de 20 ate 40 SM, advogado obrigatorio. Conferir e registrar.
- **Vedacao a pericia complexa:** causas que exijam **prova pericial complexa** sao incompativeis com o rito e vao a vara comum (art. 3º + art. 51, II — extincao sem merito se a complexidade aparecer no curso). Avaliar antes de optar pelo JEC (PA-19).
- **Foro (art. 4º):** domicilio do reu; foro do lugar do cumprimento da obrigacao; ou domicilio do autor/local do fato em reparacao de dano. Em relacao de consumo prevalece o **domicilio do consumidor** (art. 101, I CDC) — escolher a sede mais favoravel.

## 2. ESTRUTURA DA PECA (enxuta, estilo do escritorio)

1. **Enderecamento** — Juizado Especial Civel competente.
2. **Qualificacao** — autor e reu (CNPJ do fornecedor).
3. **Dos Fatos** — narrativa **simplificada e cronologica**; cada documento como **"doc. N"**.
4. **Do Direito** — FIRAC enxuto por tese (relacao de consumo art. 2/3; inversao do onus art. 6, VIII com verossimilhanca/hipossuficiencia — PA-12; tese de merito do eixo; **antecipacao adversarial** — Sumula 385, taxa media, engano justificavel, excludentes).
5. **Da Tutela de Urgencia** (se houver) — art. 300 CPC c/c art. 6º da Lei 9.099 (criterios de equidade): retirar negativacao, religar servico, suspender cobranca/desconto.
6. **Dos Pedidos** — **liquidos e determinados** (o JEC exige pedido certo e valor): declaratorio (com inciso do art. 51 se nulidade — PA-13); condenatorio (repeticao simples ou **dobro** so com engano injustificavel, art. 42 + Tema 929 — PA-06); **dano moral quantificado** (nunca "a arbitrar" puro); inversao do onus; juros e correcao.
7. **Do Valor da Causa** — soma dos pedidos; **deve respeitar o teto de 40 SM** sob pena de incompetencia.
8. **Requerimentos** — citacao, designacao da **audiencia de conciliacao**, provas.

## 3. PROCEDIMENTO E PRAZOS NO JEC

- **Conciliacao obrigatoria:** sessao de conciliacao e fase necessaria (arts. 21-26). Nao havendo acordo, segue a instrucao.
- **Revelia (art. 20):** ausencia do reu a sessao/audiencia → presumem-se verdadeiros os fatos, salvo conviccao em contrario.
- **Recurso inominado (art. 41-42):** prazo de **10 dias** da sentenca, ao **colegio/turma recursal**; preparo no ato (salvo gratuidade); contrarrazoes em 10 dias.
- **Embargos de declaracao (art. 48-50):** prazo de **5 dias**, interrompem o prazo recursal (redacao vigente). Validar prazos com `validador-legislacao-consumidor` (PA-11).

## 4. CHECKLIST ANTES DE ENTREGAR

- [ ] Rito JEC adequado (sem pericia complexa) · valor ate 40 SM (PA-19)
- [ ] Capacidade postulatoria conferida (≤20 SM dispensa advogado)
- [ ] Polo coerente (PA-05) · Selo P1 citado · inversao do onus fundamentada (PA-12)
- [ ] Pedidos liquidos e determinados · dano moral quantificado · dobro so com engano injustificavel (PA-06)
- [ ] Sumula/Tema como `[VERIFICAR]` + `jurisprudencia-consumidor` (PA-01) · prazos (PA-11) · docs "doc. N"
- [ ] Submeter a `revisao-final-consumidor` (R1-R4) antes da entrega (PA-22)

## 5. ENCERRAMENTO

Entrega a peca no formato do Juizado Especial — enxuta, pedido liquido dentro do teto, conciliacao requerida, com o rito e os prazos (recurso inominado 10 dias, ED 5 dias) corretos, pronta para a Suprema Corte R1-R4.
