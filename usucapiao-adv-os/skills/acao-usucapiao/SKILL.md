---
name: acao-usucapiao
description: >
  ACAO USUCAPIAO — Skill Tier 2 (lado usucapiente), peca principal da via judicial. Redige a peticao
  inicial da acao de usucapiao em qualquer modalidade, com a qualificacao do imovel, a causa de pedir
  (posse ad usucapionem + modalidade), o rol de citacoes obrigatorias (confrontantes, titulares,
  Uniao/Estado/Municipio + reus incertos por edital — CPC art. 246 §3 e 259 III), a planta/memorial e
  os pedidos (declaracao do dominio + registro no RI). Acione quando a via for judicial e o cliente e o
  usucapiente. Exige Selo P1, matricula/certidoes e a analise de posse.
metadata:
  version: "0.1.0"
  area: "Usucapiao (Judicial e Extrajudicial)"
  tier: 2
---

# ACAO USUCAPIAO (judicial)

> Skill **Tier 2** — lado usucapiente. Peca-base da via judicial. So roda apos triagem, Selo P1, analise de posse e linha estrategica.

---

## 0. PRE-REQUISITOS
- Via = judicial. Polo = usucapiente.
- **Selo P1** emitido. Modalidade definida (`analise-posse-usucapiao`).
- Matricula/certidao do RI, planta e memorial com **ART**, comprovantes de posse. Falta → `[INFORMAR]` (PA-03). **Bem publico → nao cabe** (PA-04).

## 1. FORO E CITACOES (PA-06 — nao omitir nenhuma)
- **Foro:** situacao do imovel (CPC art. 47).
- **Citar:** (a) o(s) titular(es) registral(is) e os confrontantes (e respectivos conjuges); (b) **a Uniao, o Estado e o Municipio** (CPC art. 246 §3); (c) os **reus em lugar incerto e eventuais interessados por EDITAL** (CPC art. 259, III). Intimar o **MP** quando houver interesse de incapaz/ente publico.

## 2. ESTRUTURA (FIRAC)
1. **Dos Fatos** — descricao do imovel (matricula/confrontacoes/metragem — doc. N), o inicio e a continuidade da posse (atos possessorios: moradia, IPTU, benfeitorias — doc. N), e a cadeia possessoria (acessio possessionis se houver).
2. **Do Direito:**
   - **Modalidade** e seus requisitos (tempo + qualidade da posse + metragem/justo titulo conforme o caso). Ex.: extraordinaria (art. 1.238, 15/10 anos, dispensa justo titulo — Sum. 391 STF); especial urbana (art. 1.240/CF 183, 250 m2, moradia, nao proprietario).
   - **Posse ad usucapionem**: mansa, pacifica, continua, ininterrupta, com **animus domini** (PA-08) — distinta de detencao (PA-09).
3. **Da prova** — planta/memorial com ART, certidoes, comprovantes, prova testemunhal da posse.
4. **Dos Pedidos:**
   - **declaracao do dominio** por usucapiao (com a descricao exata do imovel para registro);
   - citacao dos confrontantes/titulares/entes + edital;
   - **registro da sentenca no Registro de Imoveis** (abertura de matricula);
   - gratuidade se cabivel; valor da causa (valor do imovel).

## 3. CHECKLIST
- [ ] Modalidade e requisitos corretos (PA-05) · bem nao e publico (PA-04)
- [ ] TODAS as citacoes (confrontantes + titulares + Uniao/Estado/Municipio + edital — PA-06)
- [ ] Posse ad usucapionem demonstrada (PA-08), nao detencao (PA-09)
- [ ] Planta/memorial com ART · descricao para registro
- [ ] `revisao-final-usucapiao` R1-R4 (PA-13)

## 4. ENCERRAMENTO
Entrega a inicial com a modalidade correta, a posse demonstrada e o rol completo de citacoes, pronta para a Suprema Corte R1-R4.
