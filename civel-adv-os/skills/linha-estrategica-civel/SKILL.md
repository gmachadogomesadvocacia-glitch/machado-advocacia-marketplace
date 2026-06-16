---
name: linha-estrategica-civel
description: >
  Linha estrategica civel Tier 1 — consolida a trilateral, a jurisprudencia e os calculos e define a VIA
  e o PEDIDO. Eixos: notificacao previa/constituicao em mora, via adequada (processo de conhecimento x
  monitoria x execucao; acao declaratoria, condenatoria, constitutiva), tutela provisoria cabivel
  (urgencia/evidencia), cumulacao de pedidos (CPC 327), valor da causa, foro (CPC 46/53), custo
  (sucumbencia) e prescricao. Decide quando notificar antes de ajuizar e entre monitoria, cobranca e
  execucao. Produz a decisao estrategica documentada e aponta a porta de producao. Ative apos a analise
  trilateral, quando o usuario pedir a estrategia, a melhor via, qual acao propor, a tese central ou a
  linha de defesa.
metadata:
  version: "0.1.0"
  area: "Direito Civil e Processo Civil"
  tier: 1
---

# LINHA ESTRATEGICA CIVEL

> Tier 1 (Insumo). Fecha a fase de analise. Consolida `analise-trilateral-civel` + `jurisprudencia-civel` + `calculos-civeis` e decide **via** e **pedido**, documentando a escolha. Aponta a porta de producao. Side-aware (autor x reu).

---

## 1. EIXOS DE DECISAO

### Eixo 1 — Notificacao previa / constituicao em mora
- Mora **ex re** (vencimento — CC 397): dispensa notificacao.
- Mora **ex persona** (sem termo): exige interpelacao/notificacao (CC 397 par. unico).
- Quando notificar antes de ajuizar: pre-constituir prova, abrir negociacao, evitar sucumbencia. Documentar AR.

### Eixo 2 — Via adequada (PA-08)
| Situacao | Via |
|----------|-----|
| Titulo executivo (cheque/NP/duplicata; contrato com 2 testemunhas) **nao prescrito** | **Execucao** (CPC 784) |
| Prova escrita **sem** eficacia de titulo executivo | **Monitoria** (CPC 700) |
| Sem prova escrita / discussao do debito / dano a apurar | **Conhecimento — cobranca/indenizatoria** |
| Declarar (in)existencia de relacao/divida | **Declaratoria** |
| Condenar a pagar/fazer/nao fazer/dar | **Condenatoria** |
| Constituir/desconstituir (rescisao, anulacao) | **Constitutiva** |

> Cheque/titulo prescrito p/ execucao → migra p/ monitoria ou cobranca. Conferir prazo (`calculos-civeis`).

### Eixo 3 — Tutela provisoria (CPC 294+)
- **Urgencia** (probabilidade + perigo): antecipada ou cautelar (arresto, busca e apreensao).
- **Evidencia** (CPC 311): prova documental robusta + tese de repetitivo.

### Eixo 4 — Cumulacao de pedidos (CPC 327)
- So cumular pedidos **compativeis**, mesmo juizo competente e mesmo procedimento (PA-08).
- Cumulacoes tipicas: material + moral (Sum. 37); estetico + moral (Sum. 387) — validar.

### Eixo 5 — Valor da causa
- Proveito economico pretendido (CPC 292): principal + acessorios; no moral, valor pretendido (atencao Sum. 326 — arbitrar a menor nao gera sucumbencia ao autor; validar).

### Eixo 6 — Foro / competencia (CPC 46/53)
- Regra geral: **domicilio do reu** (CPC 46).
- Reparacao de dano: **lugar do ato/fato** (CPC 53, IV, a).
- Acidente de veiculo: **domicilio do autor ou local do fato** (CPC 53, V).
- Respeitar **foro de eleicao** valido do contrato (CPC 63).

### Eixo 7 — Custo e prescricao
- Avaliar sucumbencia/risco; conferir **prescricao/decadencia** (PA-05) — nao ajuizar prescrito sem ressalva.

## 2. DECISAO DOCUMENTADA (saida)

```
POLO: autor / reu
NOTIFICACAO PREVIA: necessaria? sim/nao — motivo
VIA ESCOLHIDA: execucao / monitoria / conhecimento — fundamento
NATUREZA: declaratoria / condenatoria / constitutiva
PEDIDOS (cumulacao CPC 327): ...
TUTELA PROVISORIA: cabivel? qual?
VALOR DA CAUSA: R$ ...
FORO COMPETENTE: ... (CPC __)
PRESCRICAO: OK / risco (vence DD/MM)
PORTA DE PRODUCAO: <skill de producao>
```

## 3. PORTA DE PRODUCAO

Encaminha para a skill de redacao conforme a frente (responsabilidade-civil, contratos, cobranca-monitoria, execucao, obrigacoes-e-tutelas, defesa-civel), aplicando `estilo-juridico-civel` e, ao final, `revisao-final-civel` (R1-R4).

## 4. ALERTAS

- Via errada = extincao sem merito (PA-08): conferir titulo x prova x prazo.
- Notificacao: confirmar se a mora exige interpelacao antes de cobrar.
- Foro: nao confundir regra geral com regra especial de reparacao/acidente.
- Conferir prescricao antes de fixar a estrategia (PA-05). Materia de outro plugin → rotear (PA-09).
