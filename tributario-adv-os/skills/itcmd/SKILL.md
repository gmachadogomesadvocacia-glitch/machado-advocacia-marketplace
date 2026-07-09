---
name: itcmd
description: >
  Producao e consultivo em ITCMD — imposto estadual sobre transmissao causa mortis e doacao (CF art. Ative em: cobranca/lancamento de ITCMD no inventario ou na doacao, base de calculo (valor venal x mercado), aliquota e progressividade, ITCMD sobre bens/doador/de cujus no EXTERIOR, isencoes, excesso de exacao, planejamento sucessorio (holding/doacao com usufruto). Side-aware: contribuinte (defesa) x Fazenda estadual. Interface com familia-sucessoes (inventario). So apos triagem + Selo. Encerra em revisao-final-tributaria.
---

# ITCMD — TRANSMISSAO CAUSA MORTIS E DOACAO (imposto estadual)

> Skill **Tier 2** (producao/consultivo). So apos `triagem-tributaria` + Selo de Validacao Legal
> Previa. Tributo ESTADUAL: confirmar SEMPRE a **lei do Estado/DF** (aliquota, base, isencoes,
> prazos) — nunca presumir de outro ente (PA-04). Valores de `calculos-tributarios` (PA-03).

## 0. PRE-REQUISITOS
- **Selo P1**: CF art. 155 §1 + CTN arts. 35-42 + **lei estadual do ITCMD** vigente no FATO
  GERADOR (abertura da sucessao / doacao) + jurisprudencia cruzada com o livro-razao (PA-01).
- Documentos: guia/lancamento do ITCMD, avaliacao fazendaria, inventario/escritura de doacao,
  base declarada. Falta → `[INFORMAR]`.

## 1. FATO GERADOR, BASE E ALIQUOTA
- **Fato gerador**: transmissao causa mortis (abertura da sucessao — momento da morte) ou doacao.
- **Aliquota**: a vigente ao tempo da **abertura da sucessao** (**Sum. 112 STF**); teto de 8%
  (Resolucao SF 9/1992). **Progressividade e CONSTITUCIONAL** (**Tema 21 STF / RE 562.045**) e a
  **EC 132/2023 a tornou OBRIGATORIA** (art. 155 §1 VI) — conferir a lei estadual ja adaptada.
- **Base de calculo**: valor dos bens na data da **avaliacao** (**Sum. 113 STF**); discutir
  superavaliacao fazendaria (valor venal x valor de mercado) com laudo.
- **Exigibilidade**: o ITCMD causa mortis **nao e exigivel antes da homologacao do calculo**
  (**Sum. 114 STF**). Morte presumida tambem gera incidencia (**Sum. 331 STF**).

## 2. TESES DE DEFESA DO CONTRIBUINTE
- **Bens/doador/de cujus no EXTERIOR**: enquanto nao houver **lei complementar federal**, o Estado
  **nao pode** exigir ITCMD nessas hipoteses (**Tema 825 STF — RE 851.108**, modulacao a partir de
  20/04/2021). Repeticao do indebito para fatos posteriores a modulacao. *(Acompanhar LC pos-EC 132.)*
- **Decadencia/prescricao**: contar pelo CTN (art. 173/174) conforme o tipo de lancamento da lei estadual.
- **Superavaliacao**: impugnar a base com laudo; o arbitramento fazendario admite contraditorio.
- **Isencao/imunidade**: conferir as hipoteses da lei estadual (ex.: imovel unico de baixo valor,
  entidades imunes art. 150 VI CF).

## 3. CONSULTIVO / PLANEJAMENTO SUCESSORIO (interface familia)
- Doacao em vida com **reserva de usufruto**, **holding familiar**, partilha — antecipam o ITCMD e
  podem reduzir litigio; calcular o imposto da doacao e o residual no obito. Atencao a EC 132/2023
  (progressividade obrigatoria pode elevar a carga). Articular com `planejamento-sucessorio` do
  plugin **familia-sucessoes** (inventario/partilha) — nao duplicar; rotear.

## 4. INSTRUMENTO
- Administrativo: impugnacao ao lancamento/avaliacao (lei do PAF estadual).
- Judicial: anulatoria do lancamento, MS (vicio formal/exterior sem LC), repeticao de indebito/
  compensacao do que foi pago indevidamente (ex.: exterior pos-modulacao).

## 5. CHECKLIST
- [ ] Lei ESTADUAL vigente no fato gerador (PA-04) · aliquota da abertura (Sum. 112 STF) · teto 8%
- [ ] Base na avaliacao (Sum. 113) · nao exigivel antes da homologacao (Sum. 114) · valores do calculo
- [ ] Exterior sem LC → Tema 825 STF · progressividade (Tema 21 STF / EC 132) conferida
- [ ] Instrumento certo · interface familia roteada · citacoes no livro-razao (PA-01)
- [ ] `revisao-final-tributaria` R1-R5 (C7)

## 6. ENCERRAMENTO
Entrega a peca/parecer de ITCMD (defesa, repeticao ou planejamento), pronta para a
`revisao-final-tributaria` (R1-R5 + ficha). Nada protocola sem o OK informado do advogado (C7).
