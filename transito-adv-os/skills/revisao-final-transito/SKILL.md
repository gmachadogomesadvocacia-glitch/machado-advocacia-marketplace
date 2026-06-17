---
name: revisao-final-transito
description: >
  Revisao final Tier 3 — Suprema Corte R1-R4. Ultima barreira antes de qualquer entrega de defesa,
  recurso, peca judicial ou parecer de transito. R1 valida fundamentos (CTB, Lei 14.071, Resolucoes
  CONTRAN vigentes na infracao) e jurisprudencia (Sumula/Tema STF/STJ) contra alucinacao (PA-01/PA-02/
  PA-04); R2 audita fatos do auto (placa, codigo, data/local, pontuacao) e os prazos preclusivos
  (PA-03/PA-05); R3 verifica a instancia correta, a dupla notificacao, a vedacao etica (PA-06/PA-07/
  PA-08/PA-09) e a coerencia de defesa (PA-10); R4 confere forma, orgao competente, sigilo e LGPD
  (PA-12). Ative SEMPRE antes de entregar qualquer produto de transito ao usuario.
metadata:
  version: "0.1.0"
  area: "Direito de Transito"
  tier: 3
---

# REVISAO FINAL DE TRANSITO — SUPREMA CORTE R1-R4

> Tier 3. **Nenhum** produto de transito sai sem passar pelas 4 instancias. Falha em qualquer R = retorna para correcao, nao entrega. Executa o protocolo P6 e fecha as Proibicoes Absolutas.

---

## R1 — FUNDAMENTOS E JURISPRUDENCIA (PA-01, PA-02, PA-04)

- [ ] Todo dispositivo citado existe e diz o que se afirma (CTB Lei 9.503/97, Lei 14.071/2020, Resolucoes CONTRAN).
- [ ] Norma aplicada e a **vigente na data da infracao** (tempus regit actum) — atencao as mudancas da Lei 14.071 (pontuacao, validade da CNH).
- [ ] Toda Sumula/Tema (STF/STJ — ex. Sum. 312, 127) foi **confirmada** — sem numero inventado, sem tese atribuida a precedente que nao a sustenta.

## R2 — FATOS DO AUTO E PRAZOS (PA-03, PA-05)

- [ ] Placa, RENAVAM, codigo da infracao, natureza, data/local, orgao e pontuacao conferem com o auto/notificacoes.
- [ ] **Prazos preclusivos** corretos (defesa previa, JARI, CETRAN — 30 dias da notificacao); a peca e tempestiva.
- [ ] Pontuacao e limite (20/30/40) calculados corretamente (`calculos-transito`).
- [ ] Nenhum fato afirmado sem respaldo no auto/documentos.

## R3 — INSTANCIA, ETICA E DEFESA (PA-06, PA-07, PA-08, PA-09, PA-10)

- [ ] **Instancia correta** e respectivo efeito (defesa previa × JARI × CETRAN × judicial) — sem confundir (PA-08).
- [ ] **Dupla notificacao** verificada e arguida quando cabivel (Sum. 312 STJ; PA-07).
- [ ] **Nada** que oriente fraude de pontuacao ou indicacao falsa de condutor (PA-06) — checagem inegociavel.
- [ ] Se o fato e crime de transito (306, 302/303) → roteado ao `criminal-adv-os` (PA-09), nao tratado como mera infracao.
- [ ] Peca coerente com a defesa do cliente (PA-10).

## R4 — FORMA, ORGAO E SIGILO (PA-11, PA-12, PA-13)

- [ ] Enderecamento/orgao correto (orgao autuador; JARI; CETRAN; Vara da Fazenda Publica / Juizado da Fazenda no judicial).
- [ ] Estrutura completa, teses ordenadas (preliminares de nulidade → merito), pedidos especificos (arquivamento/cancelamento da multa, restituicao de pontos, efeito suspensivo/liminar), provas requeridas.
- [ ] Identidade do operador resolvida (sem tokens `{{...}}` vazando) e OAB correta.
- [ ] Sigilo OAB + LGPD: dados do cliente e do veiculo protegidos.
- [ ] Selo P1 foi registrado antes da producao; entrega em **.txt** por padrao.

---

## R5 — VERIFICACAO ADVERSARIAL (RED-TEAM)

**Mude de chapeu: voce AGORA e o orgao autuador / o juizo cetico.** Unica missao: DERROTAR a peca. Achou UMA falha real → REPROVADO.

- [ ] **PRAZOS** — o prazo preclusivo (defesa previa/JARI/CETRAN, 30 dias) esta correto e tempestivo? (o erro mais fatal.)
- [ ] **INSTANCIA/INSTRUMENTO** — a peca e da instancia certa (defesa previa × JARI × CETRAN × judicial)? sem confundir efeitos.
- [ ] **VALORES/PONTUACAO** — pontos e limite (20/30/40) conferem com `calculos-transito`? norma vigente NA DATA da infracao (Lei 14.071)?
- [ ] **CITACOES** — Sum. 312 (dupla notificacao) e demais batem?
- [ ] **DUPLA NOTIFICACAO** — a tese da NA+NP foi conferida (vicio mais comum)?
- [ ] **ETICA (PA-06)** — nada que oriente fraude de pontuacao ou indicacao falsa de condutor.

**Veredito R5:** PASSOU / REPROVADO (eixo+falha+correcao).

---

## SAIDA

```
R1 fundamentos/jurisprudencia: OK / CORRIGIR — [notas]
R2 fatos do auto/prazos:       OK / CORRIGIR — [notas]
R3 instancia/etica/defesa:     OK / CORRIGIR — [notas]
R4 forma/orgao/sigilo:         OK / CORRIGIR — [notas]
R5 adversarial (red-team):     PASSOU / REPROVADO — [eixo+falha+correcao]
VEREDITO: LIBERADO / RETIDO
```
**RETIDO** em qualquer R (R1-R5) → volta a skill de origem. Nunca entregar com R pendente (PA-13), e jamais liberar peca que toque a PA-06. Apos LIBERADO → sai com a **FICHA DE CONFERENCIA** anexa e atualizar `CASO.md` (memoria-de-caso-transito).

## FICHA DE CONFERENCIA (acompanha a entrega, nao integra a peca)

```
FICHA DE CONFERENCIA — pre-protocolo
- PREMISSAS: ...
- DADOS DO AUTO (placa/codigo/data/orgao) conferidos: ...
- PRAZO (vence em): ...
- CITACOES (cada uma → status): Sum. 312 STJ — CONFIRMADO | VALIDAR
- LACUNAS [INFORMAR]: ...
- RISCOS / PONTOS ADVERSARIAIS: ...
- VEREDITO: R1 _ · R2 _ · R3 _ · R4 _ · R5 _
- PENDE O OK INFORMADO DO ADVOGADO antes do protocolo.
```
