---
name: jurisprudencia-transito
description: >
  Jurisprudencia de transito Tier 1 — validacao jurisprudencial (PA-01). Define a hierarquia
  (STF > STJ > TJ), o metodo de confirmacao antes de citar e o catalogo de sumulas/teses uteis a defesa
  do condutor/proprietario. Sumulas do STJ consagradas (validar enunciado e vigencia): Sum. 312 (dupla
  notificacao — autuacao e penalidade), Sum. 127 (anotacao de infracao e licenciamento — validar),
  Sum. 434, Sum. 510. Teses do CTB (dupla notificacao, ampla defesa, afericao de equipamento, decadencia
  administrativa). Regra de ferro: NUNCA citar sumula, tema ou precedente sem validar. Ative ao precisar
  de fundamento jurisprudencial, sumula, tese ou precedente para peca de transito.
metadata:
  version: "0.1.0"
  area: "Direito de Transito"
  tier: 1
---

# JURISPRUDENCIA DE TRANSITO

> Tier 1. Guarda do **PA-01** (alucinacao jurisprudencial). Nenhuma sumula, tema repetitivo ou precedente entra em peca sem **validacao** previa do enunciado, do orgao e da vigencia. Em duvida, marca-se "[validar]" e nao se cita como certo.

---

## 1. HIERARQUIA

```
STF (constitucional / repercussao geral)
  > STJ (lei federal — sumulas, temas repetitivos)
    > TJ/TRF (estadual/regional — orientacao local)
```
Precedente vinculante (STF RG; STJ repetitivo) pesa mais que ementa isolada. Sempre indicar o **orgao**, o **numero** e, se possivel, a **data**.

## 2. METODO DE VALIDACAO (antes de citar)

1. Conferir o **enunciado literal** da sumula/tese (nao parafrasear de memoria).
2. Confirmar o **orgao** (STF/STJ/TJ) e que esta **vigente** (nao cancelada/superada).
3. Confirmar **aderencia factica** ao caso (mesma situacao juridica).
4. Aplicar a norma **vigente na data da infracao** (PA-04 — tempus regit actum; atencao a Lei 14.071/2020).
5. Se nao for possivel confirmar → marcar **[validar]** e nao usar como fundamento decisivo.

## 3. SUMULAS DO STJ UTEIS (validar enunciado e vigencia)

| Sumula | Tese (conferir literal) | Uso na defesa |
|--------|-------------------------|---------------|
| **Sum. 312** | Dupla notificacao obrigatoria — **autuacao e penalidade** | Nucleo da defesa por cerceamento (PA-07) |
| **Sum. 127** | Anotacao de infracao e licenciamento (validar enunciado exato) | Impugnar exigencias indevidas |
| **Sum. 434** | (validar enunciado e pertinencia) | Conferir antes de usar |
| **Sum. 510** | (validar enunciado e pertinencia) | Conferir antes de usar |

> As entradas acima sao **pistas**, nao citacoes prontas. Confirmar cada enunciado antes de levar a peca.

## 4. TESES DO CTB (linhas recorrentes)

- **Dupla notificacao** (CTB 280-281; Sum. 312) — ausencia/intempestividade de NA ou NP.
- **Prazo de expedicao da NA** (CTB 281 § unico) — em regra 30 dias; ultrapassado → arquivamento.
- **Ampla defesa / contraditorio** (CF 5º LIV-LV) — motivacao das decisoes, acesso, producao de prova.
- **Afericao do equipamento** — exigencia de certidao valida (INMETRO/IPEM) e margem de tolerancia.
- **Decadencia/prescricao administrativa** — prazos do orgao para notificar/julgar; prescricao quinquenal contra a Fazenda no judicial.

## 5. SAIDA

```
TESE: ...
FUNDAMENTO: Sum./Tema/precedente — orgao + numero [validar]
ENUNCIADO CONFERIDO: sim/nao
ADERENCIA AO CASO: ...
NORMA VIGENTE NA DATA DA INFRACAO: (PA-04)
```

## 6. INTEGRACAO

- `analise-vicios-auto-infracao` → cada tese pede o respaldo daqui.
- `linha-estrategica-transito` → escolha das teses por forca.
- `estilo-juridico-transito` → forma de citar (orgao, numero, enunciado).
- `revisao-final-transito` → R2 reconfere toda citacao (PA-01).

## 7. CHECKLIST DE SAIDA

- [ ] Enunciado literal conferido (nao de memoria)
- [ ] Orgao, numero e vigencia confirmados
- [ ] Aderencia factica ao caso verificada
- [ ] Norma vigente na data da infracao (PA-04)
- [ ] Nenhuma sumula/precedente citado sem validar (PA-01)
- [ ] Itens nao confirmados marcados "[validar]"
