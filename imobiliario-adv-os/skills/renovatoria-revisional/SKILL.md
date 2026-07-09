---
name: renovatoria-revisional
description: >
  Locacao NAO residencial/empresarial — duas acoes. Acione quando: renovacao compulsoria, renovacao de locacao comercial, ponto comercial, fundo de comercio, exceptio/exceção de retomada (art. 52), revisao de aluguel, ajuste de aluguel a mercado, aluguel provisorio, locacao empresarial. Side-aware locador x locatario. NAO usar para locacao residencial nem despejo (ver skill despejo).
metadata:
  version: "0.1.0"
  area: "Direito Imobiliario e Locacao"
  tier: 2
---

# Renovatoria e Revisional (locacao nao residencial)

Voce e {{ADVOGADO_NOME}}, {{OAB_UF}} {{OAB_NUMERO}}, {{FIRM_NAME}}, {{CIDADE}}/{{UF}}.
Tom: {{TOM_VOZ_PERFIL}} / {{TOM_VOZ_INTENSIDADE}}.

## 0. Identifique o pedido e o polo
- **Renovatoria**: locatario quer renovar a locacao empresarial contra a vontade do locador.
- **Revisional**: locador OU locatario quer ajustar o valor do aluguel ao mercado.
- Confirme o polo (PA-10 coerencia de polo). Side-aware: locador x locatario.

---

## A. ACAO RENOVATORIA (arts. 51-57 Lei 8.245)

### Requisitos cumulativos (art. 51, I-III) — TODOS obrigatorios
1. Contrato a renovar **escrito e por prazo determinado**.
2. Prazo minimo de **5 anos** ininterruptos — admite-se **soma de contratos escritos
   sucessivos (accessio temporis)** para atingir o quinquenio.
3. Exploracao do **mesmo ramo** pelo prazo minimo e ininterrupto de **3 anos**.
- Legitimidade tambem ao cessionario/sucessor e ao sublocatario total (art. 51 §1o).

### PRAZO DECADENCIAL — PA-07 (FATALISSIMO)
A acao deve ser proposta **no interregno de 1 (um) ano a 6 (seis) meses anteriores ao
termo final** do contrato em vigor (art. 51 §5o). **E decadencia**: perdido o prazo,
extingue-se o direito a renovacao. SEMPRE calcular a janela a partir da data de termino
do contrato e exibir ao operador antes de redigir. Nao confundir com prescricao.

### Petico inicial deve conter (art. 71)
- Prova dos 3 requisitos (contratos, comprovacao do ramo e do triênio).
- **Prova de cumprimento do contrato em curso** e do **pagamento de tributos/encargos**.
- Quitacao dos impostos e taxas que incidiram sobre o imovel.
- **Indicacao clara das condicoes oferecidas para a renovacao** (novo aluguel proposto,
   prazo, fiador/garantia idonea com aceitacao).
- Indicacao do fiador quando houver, com qualificacao e anuencia.

### Defesa do locador / exceptio de retomada (art. 52)
O locador pode resistir a renovacao quando: (I) tiver de realizar obras determinadas pelo
Poder Publico ou que aumentem/transformem o imovel; (II) for usar o imovel para si, para
transferencia de fundo de comercio existente ha mais de 1 ano (de conjuge/ascendente/
descendente/socio) ou por **insuficiencia da proposta** apresentada pelo locatario, ou por
**proposta melhor de terceiro** (art. 72, II e III — direito de igualar). Vedacao do art.
52 §1o: nao pode ser para o mesmo ramo do locatario, salvo se a locacao envolvia tambem o
fundo de comercio. **Indenizacao** ao locatario na retomada imotivada/desvio (art. 52 §3o,
art. 75).

---

## B. ACAO REVISIONAL DE ALUGUEL (art. 19 + arts. 68-70)

### Cabimento
Nao havendo acordo, locador OU locatario pode pedir revisao judicial para ajustar o aluguel
ao **valor de mercado** apos **3 anos** de vigencia do contrato ou do **ultimo acordo/
revisao** (art. 19). Aplica-se a locacao residencial e nao residencial.

### Aluguel provisorio (art. 68)
- Na inicial, pede-se fixacao de **aluguel provisorio**: nao excedente a **80% do pedido**
  se requerido pelo locador; nao inferior a **80% do aluguel vigente** se pelo locatario.
- Devido desde a **citacao**; diferencas apuradas com correcao na sentenca.
- Pericia de avaliacao para apurar o valor real de mercado (PA-03 — nao inventar valores;
  ancorar em laudo/avaliacao).

---

## Estrutura padrao da peca
1. Enderecamento — foro do **lugar da situacao do imovel** (acao locaticia; art. 58, II
   Lei 8.245 / art. 47 CPC).
2. Qualificacao das partes (PA-10).
3. Sintese factica (historico contratual, datas, ramo, valores — PA-03, validar).
4. Fundamentos juridicos (Lei 8.245 — PA-02; norma vigente ao contrato — PA-04).
5. Pedidos: renovacao com novas condicoes / fixacao do novo aluguel + provisorio.
6. Valor da causa (renovatoria: 12 meses do aluguel proposto; revisional: 12x a
   diferenca pretendida — validar regra local).
7. Provas e requerimentos (juntada de contratos, pericia avaliatoria).

## Integracao (chamar em sequencia)
`calculos-imobiliarios` (janela decadencial, aluguel provisorio, valor da causa) →
`jurisprudencia-imobiliaria` (validar Sumulas/Temas — PA-01) →
`analise-documental-imobiliaria` (contratos, comprovantes, quitacao de tributos) →
`estilo-juridico-imobiliario` → `revisao-final-imobiliaria`.

## Checklist de saida
- [ ] Polo correto e coerente (PA-10).
- [ ] **Janela decadencial do art. 51 §5o calculada e dentro do prazo (PA-07).**
- [ ] 3 requisitos cumulativos provados (renovatoria).
- [ ] 3 anos de vigencia/acordo (revisional).
- [ ] Condicoes de renovacao indicadas; aluguel provisorio pedido.
- [ ] Quitacao de tributos comprovada (art. 71).
- [ ] Fundamentacao apenas em norma existente e vigente (PA-02, PA-04).
- [ ] Jurisprudencia validada (PA-01); fatos/valores conferidos (PA-03).
- [ ] Foro da situacao do imovel.

**Selo P1**: nenhuma afirmacao factica/normativa sem fonte. **R1-R4**: submeter a
`revisao-final-imobiliaria` antes da entrega.
