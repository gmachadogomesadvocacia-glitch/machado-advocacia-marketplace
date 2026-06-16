---
name: mandado-seguranca-isencao
description: >
  MANDADO DE SEGURANCA ISENCAO — Skill Tier 2 (lado contribuinte). Redige o MS contra ato coator
  (retencao indevida ou negativa ilegal da isencao de IRPF por doenca grave) quando ha DIREITO LIQUIDO E
  CERTO demonstravel de plano (laudo claro + doenca inequivocamente no rol). Inclui pedido de LIMINAR para
  cessar a retencao, o prazo decadencial de 120 dias e a orientacao de quando preferir MS x acao ordinaria
  (MS = prova pre-constituida, sem dilacao; ordinaria = quando precisa de pericia/instrucao). Acione na via
  judicial pelo contribuinte quando a prova for documental e robusta. Exige Selo P1, laudo e comprovantes.
metadata:
  version: "0.1.0"
  area: "Isencao de IRPF por Doenca Grave"
  tier: 2
---

# MANDADO DE SEGURANCA — ISENCAO DE IRPF

> Skill **Tier 2** — lado contribuinte, via judicial de rito celere. MS contra a retencao/negativa ilegal quando o direito e liquido e certo. So roda apos triagem, Selo P1 e linha estrategica.

---

## 0. PRE-REQUISITOS
- Polo = contribuinte/beneficiario. **Selo P1** emitido (Lei 7.713/88 art. 6 XIV + Sum. 598/627).
- **Direito liquido e certo:** prova **documental e pre-constituida** — laudo claro (doenca/CID/data) + doenca **inequivocamente no rol** (PA-05) + comprovantes de IR retido. Sem isso, NAO usar MS (ver secao 4). Falta → `[INFORMAR]` (PA-11). Nao opinar sobre o diagnostico (PA-04).

## 1. ATO COATOR, AUTORIDADE E FORO
- **Ato coator:** a retencao indevida do IRPF na fonte **ou** a negativa/silencio ilegal do pedido de isencao.
- **Autoridade coatora:** o agente que ordena a retencao (ex.: Delegado da Receita; dirigente do INSS/RPPS/EFPC conforme quem retem). Litisconsorte: a Uniao (Fazenda Nacional).
- **Foro:** sede da autoridade coatora — **Justica Federal** (Lei 12.016/2009).

## 2. PRAZO DECADENCIAL — 120 DIAS
- O MS deve ser impetrado em **120 dias** do ato coator (art. 23, Lei 12.016/2009).
- Em **retencao mensal continuada**, o desconto se renova a cada competencia — ato de trato sucessivo: cabe ao menos quanto as parcelas dentro dos 120 dias. Registrar o marco no CASO.md.

## 3. ESTRUTURA E LIMINAR
1. **Fatos:** aposentado/pensionista (doc. N) portador de [doenca do rol] (laudo — doc. N); retencao indevida desde [data] (doc. N).
2. **Direito:** art. 6, XIV, Lei 7.713/88; **Sum. 598** (prova flexivel — PA-07) e **Sum. 627** (manutencao/contemporaneidade — PA-08); **so proventos** (PA-06).
3. **Liminar (art. 7, III):** *fumus* (laudo + enquadramento) + *periculum* (desconto mensal continuado) → **cessacao imediata** da retencao.
4. **Pedidos:** concessao da seguranca para **declarar a isencao** e **cessar a retencao**; protecao do dado de saude — **segredo de justica** (PA-10).
> A repeticao do **indebito passado** (5 anos) em regra **nao** se cobra na via mandamental (Sum. 269/271 STF) — para o passado, usar `acao-isencao-ir` ou retificadora. No MS, focar a cessacao e a isencao a partir da impetracao.

## 4. MS x ACAO ORDINARIA
- **MS** quando: prova **documental** suficiente, doenca claramente no rol, sem necessidade de pericia — celeridade e liminar.
- **Acao ordinaria** (`acao-isencao-ir`) quando: precisa de **pericia/instrucao** (enquadramento controverso, laudo fragil) ou quer **cobrar o indebito dos 5 anos** no mesmo feito.

## 5. CHECKLIST
- [ ] Direito liquido e certo (prova documental) · doenca no rol (PA-05) · so proventos (PA-06)
- [ ] 120 dias observados · autoridade/foro corretos · liminar de cessacao
- [ ] Sum. 598/627 invocadas · dado de saude sob segredo (PA-10)
- [ ] CASO.md atualizado · `revisao-final-isencao-ir` R1-R4 (PA-14)

## MODELO DE PECA
Chassi: `templates/pecas/mandado-seguranca-isencao.md` (padrao enxuto da casa). Abrir, ler a NOTA DE USO e substituir os `[____]`; nao copiar o texto para ca (limite de 11264 bytes — fonte unica no chassi).

## 6. ENCERRAMENTO
Entrega o MS com liminar para cessar a retencao, ancorado no direito liquido e certo e nas Sum. 598/627, com a opcao MS x ordinaria explicitada, pronto para a Suprema Corte R1-R4.
