---
name: credor-trabalhista-rj
description: >
  CREDOR-TRABALHISTA-RJ — Tier 2 (Produção) / Eixo Prioritário. Acionada
  AUTOMATICAMENTE quando o caso envolver crédito trabalhista em recuperação
  judicial: sentença da JT, reclamatória, acordo homologado, liquidação,
  certidão de crédito, verbas rescisórias, FGTS, vínculo, execução
  trabalhista, honorários sucumbenciais trabalhistas. Coleta 22 campos,
  decide via (divergência / impugnação / retardatária / art. 6º §2º),
  classifica concursal x extraconcursal pelo fato gerador, aplica teto de
  150 SM (excedente Classe III), verifica prescrição e entrega peça +
  cálculo + índice. Foco: REPRESENTAÇÃO DO CREDOR TRABALHISTA.
---

# CREDOR-TRABALHISTA-RJ — EIXO PRIORITÁRIO

> Tier 2 | L11.101/2005 (arts. 6º §2º, 7º-10, 41, 49, 83, 84) +
> L14.112/2020 + CLT + Tema 1.051 STJ + Súm. 480 STJ + IAC 13 STJ

## 0. ATIVAÇÃO AUTOMÁTICA

DISPARADA AUTOMATICAMENTE ao detectar léxico trabalhista (lista completa
no MODO CTH da `rj-master` e na description acima). A `rj-master` roteia
para cá. Assume PRIORIDADE sobre o pipeline genérico da `rj-master`.

## 1. PRIMEIRA PERGUNTA — SEMPRE

Confirme o polo: cliente é **CREDOR** (titular do crédito) ou
**RECUPERANDA** (devedora)? Esta skill opera só do lado do CREDOR — se
for recuperanda, rotear para `contestacao-rj`. Sem confirmação explícita
do polo CREDOR, NÃO avance.

## 2. COLETA OBRIGATÓRIA — 22 CAMPOS

Peça todos em bloco único. NÃO produza peça enquanto qualquer campo
crítico (⛔) estiver em branco.

```
A — RECUPERANDA
 1.⛔ Razão social / CNPJ   2.⛔ Processo de RJ (CNJ)   3.⛔ Juízo/comarca
 4.⛔ Data do pedido de RJ (marco art. 9º II)   5. Deferimento (art. 52)
 6. Edital art. 52 §1º (publicado? data?)   7. Relação do AJ art. 7º §2º
 (publicada? data?)   8. QGC homologado art. 14? (data?)

B — CREDOR
 9.⛔ Nome   10.⛔ CPF/CNPJ   11.⛔ Natureza (trabalhista puro/honorários/
 FGTS/misto)   12.⛔ Origem (sentença/acordo/liquidação/CH)   13.⛔ Consta
 na relação? (sim c/ valor+classe / sim mas valor ou classe errados / não)

C — PROCESSO TRABALHISTA
14.⛔ Nº do processo trab. (CNJ, se houver)   15. Fase (conhecimento/
 liquidação/execução/arquivado)   16. Sentença: data + trânsito?
17. Acordo homologado? data?   18. Liquidação encerrada? valor? data?
19. CH já expedida pela JT?

D — VALORES
20.⛔ Valor histórico   21.⛔ Valor atualizado + data-base   22.⛔ Período
 do fato gerador (início → fim do contrato ou do dano)
```

Para cada campo em branco, pergunte de forma dirigida explicando por que
é necessário (não bombardear).

## 3. DECISÃO DE CONCURSALIDADE — ART. 49 vs. ART. 84

Aplique SEM EXCEÇÃO antes da via. Critério é o **FATO GERADOR** (período
laborado / data do dano), não a data da sentença, do trânsito ou da
liquidação (IAC 13 STJ; REsp 1.634.046 — confirmar `jurisprudencia-rj`).

- **Caso 1 — fato gerador 100% ANTERIOR ao pedido** → CONCURSAL;
  submete-se ao plano; Classe I (até 150 SM/credor) + III (excedente);
  art. 49 caput + 41 I + 83 I.
- **Caso 2 — 100% POSTERIOR** → EXTRACONCURSAL; NÃO se submete (PA-15);
  pago no curso normal, com preferência na convolação em falência (art.
  84 I-B/I-C); art. 49 caput a contrario.
- **Caso 3 — a cavaleiro do pedido** → SEGREGAR pro rata temporis:
  parcela anterior CONCURSAL, posterior EXTRACONCURSAL; art. 49 caput.

⚠️ **ALERTA A2/A3**: dispare antes da redação.

## 4. DECISÃO DE VIA — DELEGAR A `via-processual-rj`

Após classificar, invoque **`via-processual-rj`** com os dados; ela
devolve a via certa com fundamento. Sumário-espelho:

- **[I] EXTRACONCURSAL** → NÃO habilita; cobra no curso normal.
- **[II] Concursal + NÃO consta na relação do AJ** → DIVERGÊNCIA /
  habilitação administrativa (art. 7º §1º); 15d do edital; AO
  ADMINISTRADOR JUDICIAL (não ao juízo).
- **[III] Concursal + consta com ERRO (após relação art. 7º §2º)** →
  IMPUGNAÇÃO JUDICIAL (art. 8º); 10d da relação consolidada; AO JUÍZO
  (apartado).
- **[IV] Concursal fora dos prazos II/III, ou QGC homologado** →
  RETARDATÁRIA (art. 10); ação autônoma + custas; SEM voto na AGC (A13);
  AO JUÍZO.
- **[V] Crédito em LIQUIDAÇÃO na JT** → art. 6º §2º: JT liquida, juízo da
  RJ RESERVA o estimado; após a CH habilita pela via II/III/IV; execução
  SUSPENSA (stay, art. 6º caput).

⚠️ **ALERTA A5**: divergência (administrativa) ≠ impugnação (judicial);
peça mal endereçada → rejeição liminar e perda da via.

## 5. CÁLCULO — DELEGAR A `calculo-credito-trabalhista-rj`

Havendo valor a habilitar, invoque
**`calculo-credito-trabalhista-rj`**: **(1)** atualizar até a DATA DO
PEDIDO DE RJ (art. 9º II); **(2)** teto Classe I = 150 × SM da data do
pedido, excedente em Classe III (art. 83 I); **(3)** segregar verbas de
tratamento próprio — FGTS (Tema 1.051 STJ, [VERIFICAR]); multa 477 CLT →
Classe I; multa 467 CLT → cabimento controverso; honorários
sucumbenciais trab. → natureza alimentar, equiparados a crédito
trabalhista (Tema 637 STJ, REsp 1.152.218/RS), classe controversa; INSS
empregado descontado/não recolhido → crédito do INSS, NÃO habilita pelo
credor; contribuição sindical → crédito do sindicato; **(4)** planilha
verba × classe × valor; **(5)** se `calculos-pjecalc` instalado, delegar
o passo 1.

## 5-BIS. PRESCRIÇÃO — VERIFICAÇÃO OBRIGATÓRIA

**INVIOLÁVEL antes de retardatária (art. 10) e de orientar sobre crédito
antigo.** Quatro hipóteses-núcleo:

- **Bienal trabalhista** (art. 7º XXIX CF + art. 11 CLT): 2 anos da
  extinção do contrato; interrompida pelo ajuizamento da reclamatória
  (Súm. 268 TST). Quinquenal: parcelas dos últimos 5 anos. Sem
  reclamatória e >2 anos da extinção → BIENAL CONSUMADA, sem pretensão →
  PRESCRITO.
- **Intercorrente** (art. 11-A CLT): 2 anos de paralisação imputável ao
  exequente. ⚠️ NÃO corre no stay da RJ — paralisação não imputável ao
  credor (PA-CTH-11); o stay SUSPENDE a contagem.
- **Prescrição de habilitar**: discussão viva — Linha 1: 2 anos
  pós-trânsito (paralelo à bienal); Linha 2: 5 anos (art. 206 §5º I CC);
  Linha 3: enquanto não encerrada a RJ (regra do art. 10). CONFIRMAR via
  `jurisprudencia-rj` antes de afirmar prescrição, sobretudo com QGC.
- **Pós-encerramento** (art. 61 c/c art. 59): crédito não habilitado em
  regra não se extingue (Súm. 372 TST, varia por tribunal), mas cobra
  direto da recuperanda, com risco maior.

O deferimento da RJ NÃO suspende o prazo prescricional — suspende
execuções (stay, art. 6º caput); o ato interruptivo é a HABILITAÇÃO.

**Saída** `[VEREDITO PRESCRIÇÃO]`: hipótese, status (PRESCRITO / NÃO
PRESCRITO / EM RISCO / VERIFICAR JP), fundamento, marco
interruptivo/suspensivo, tempo decorrido, se pode habilitar; dispara A18
+ A6. **Rodar SEMPRE que**: via = IV (retardatária); crédito antigo (>2
anos do fato gerador) sem reclamatória; execução parada >2 anos; RJ
encerrada e crédito não habilitado.

## 6. ALERTAS AUTOMÁTICOS — CHECKLIST DE TOPO

Percorra TODOS e dispare os aplicáveis em checklist no topo do output:

- **A1** data do pedido (corte art. 9º II); **A2** fato gerador define
  concursalidade (art. 49); **A3** concursal × extraconcursal; **A4**
  credor consta na relação do AJ?; **A5** VIA: divergência ≠ impugnação ≠
  retardatária.
- **A6** tempestividade 15d (7º §1º)/10d (8º)/após QGC (10); **A7**
  data-base = data do pedido; **A8** teto 150 SM, excedente Classe III;
  **A9** sem liquidação? art. 6º §2º (JT liquida + reserva); **A10**
  pagamento parcial/acordo/quitação.
- **A11** via inadequada — orientar a mais segura; **A12** docs
  indispensáveis ausentes — listar; **A13** retardatária → SEM voto na
  AGC; **A14** execução SUSPENSA (stay); **A15** duplicidade (habilitação
  + execução individual).
- **A16** FGTS — Tema 1.051 STJ + JP atual; **A17** honorários
  sucumbenciais — classe controversa; **A18** prescrição — §5-BIS; **A19**
  cessão de crédito trab. (art. 83 §4º) rebaixa classe; **A20** plano:
  Classe I paga em 1 ano (art. 54 caput).

## 7. SAÍDA — TRÊS CAMADAS

Entregue três blocos separados:

- **[1 — ANÁLISE]** diagnóstico ~5 linhas; via + fundamento; riscos;
  estratégia subsidiária.
- **[2 — PEÇA]** texto pronto para protocolo; endereçamento correto (AJ
  ou juízo); Fato + Direito + Pedido; lista de documentos anexos.
- **[3 — ANEXOS]** planilha (verba × classe × valor); índice numerado de
  docs; eventual minuta lateral (ex.: reserva ao juízo, art. 6º §2º).

## 8. VIAS DE PEÇA — DELEGAÇÃO

Peça PRODUZIDA por `habilitacao-credito-rj` (§A-D); via DECIDIDA por
`via-processual-rj` (prazos/endereçamento na Seção 4). Esta skill
seleciona a via e fornece os dados — não duplica modelos. Esqueleto
comum: titularidade/fatos → natureza e concursalidade → classificação
(art. 83 I) → documentos → pedido. As 4 vias:

- **§A Divergência adm. (art. 7º §1º)** — pedido de registro.
- **§B Impugnação judicial (art. 8º)** — incluir/retificar/reclassificar
  + sucumbência (Súm. 480/Tema 1.051 se FGTS).
- **§C Retardatária (art. 10)** — abre com justificativa do atraso; SEM
  voto na AGC (§1º), custas pelo habilitante (§3º).
- **§D Reserva (art. 6º §2º)** — reserva + ofício à VT + habilitação
  definitiva pós-CH.

## 9. ATUALIZAÇÃO DO CASO.md

Atualize via `memoria-de-caso-rj` o bloco "Crédito do Cliente":
recuperanda; processo de RJ; polo (CREDOR TRABALHISTA); crédito histórico
e atualizado até a data do pedido; valores por classe (I até 150 SM, III
excedente, extraconcursal se houver); via; data de protocolo; status;
processo trabalhista correlato e fase.

## 10. PROIBIÇÕES ESPECÍFICAS — PA-CTH

Nunca (01-11):

- **01** redigir antes de confirmar polo CREDOR.
- **02** confundir divergência (AJ) com impugnação (juízo).
- **03** atualizar crédito além da data do pedido de RJ.
- **04** habilitar Classe I sem o teto de 150 SM.
- **05** habilitar FGTS sem verificar Tema 1.051 STJ.
- **06** classificar crédito sem cravar fato gerador.
- **07** tratar crédito ilíquido como perdido — aplicar art. 6º §2º.
- **08** produzir peça sem `revisao-final-rj` (R1-R4).
- **09** habilitar INSS empregado em nome do credor (é da União).
- **10** recomendar retardatária sem alertar a perda do voto na AGC.
- **11** recomendar retardatária sem rodar a PRESCRIÇÃO (§5-BIS); aplicar
  intercorrente trab. no stay (não imputável ao exequente); confundir
  bienal (CF) com prescrição da habilitação (CC).

## 11. FECHAMENTO

Termina com `CHECKPOINT CTH ENCERRADO`: polo (CREDOR TRABALHISTA), via,
classe(s), valor habilitado, peça entregue, resultado da revisão R1-R4,
pendências do operador e próximo passo.

## 12. MODELO DE PEÇA

Chassi (padrão enxuto, opções A/B/C + módulo sucessão):
`templates/pecas/habilitacao-retardataria-trabalhista.md` — abrir e
substituir os `[____]` antes de redigir.
