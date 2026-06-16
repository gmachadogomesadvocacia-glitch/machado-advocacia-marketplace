---
name: analise-documental-civel
description: >
  Analise documental civel Tier 1 — Protocolo P2. Checklist de integridade dos documentos antes de
  qualquer producao: contrato (partes, objeto, valor, prazo, foro de eleicao, assinaturas/testemunhas),
  titulos de credito (cheque, nota promissoria, duplicata — requisitos, endosso, prazos de
  apresentacao/prescricao), prova do dano (notas, orcamentos, laudos, fotos) e do nexo, BO/registro de
  acidente, notificacoes extrajudiciais, comprovantes de pagamento, instrumento particular/publico.
  Extrai dados-chave (partes, datas, valores) e marca lacunas. Ative quando o usuario enviar contrato,
  titulo, cheque, nota promissoria, duplicata, comprovante, BO, laudo, notificacao, ou pedir analise de
  documentos civeis. PA-03, PA-12.
metadata:
  version: "0.1.0"
  area: "Direito Civil e Processo Civil"
  tier: 1
---

# ANALISE DOCUMENTAL CIVEL

> Tier 1 (Insumo). Operacionaliza **P2 — Integridade Documental**. Antes de afirmar qualquer fato, valor ou data, confira o documento. **Nunca inferir o que nao esta no documento (PA-03).** Sigilo + LGPD (PA-12). PDFs de processo: no Code, converter com `ferramentas/pdf-para-md/` antes de analisar.

---

## 1. CHECKLIST POR TIPO

### Contrato / instrumento
- Partes (qualificacao completa) e capacidade.
- Objeto (licito, possivel, determinado).
- Valor, forma e prazo de pagamento; obrigacoes de cada parte.
- Clausulas: multa/clausula penal, juros, correcao, vencimento antecipado, **foro de eleicao** (CPC 63), rescisao.
- Assinaturas das partes + **2 testemunhas** (titulo executivo extrajudicial — CPC 784, III).
- Instrumento **particular** x **publico** (escritura — exigencia de forma, CC 108/166).
- Data — define a **norma vigente** (PA-04; CC/2002 x CC/1916, art. 2.035).

### Titulos de credito
| Titulo | Requisitos essenciais | Apresentacao | Prescricao da execucao |
|--------|----------------------|--------------|------------------------|
| **Cheque** | Lei 7.357/85 art. 1º | 30 dias (mesma praca) / 60 (outra) | 6 meses apos o prazo de apresentacao (validar) |
| **Nota promissoria** | LUG / Dec. 57.663 | — | 3 anos do vencimento (validar) |
| **Duplicata** | Lei 5.474/68; aceite/comprovante de entrega | — | 3 anos do vencimento (validar) |

- Conferir **endosso** (cadeia), aval, vencimento, valor por extenso.
- Vencido o prazo de execucao → avaliar **monitoria** ou **cobranca** (PA-08; ver `linha-estrategica-civel`).

### Prova do dano e do nexo (responsabilidade civil)
- **Dano emergente:** notas fiscais, orcamentos, recibos, comprovantes de despesa.
- **Lucro cessante:** prova do que razoavelmente deixou de ganhar (CC 402) — historico, fluxo, contratos.
- **Dano moral/estetico:** laudos, fotos, prontuario (se medico → rotear PA-09), documentos do abalo.
- **Nexo causal:** o documento liga a conduta ao dano? Marcar lacuna se nao houver.
- **BO / registro de ocorrencia** (acidente): boletim, laudo pericial, fotos do local.

### Outros
- **Notificacao extrajudicial** (constituicao em mora — CC 397 par. unico): data, recebimento, AR.
- **Comprovantes de pagamento** (quitacao — CC 320; consignacao).
- **Procuracao** e documentos pessoais das partes.

## 2. EXTRACAO DE DADOS-CHAVE

Para cada documento, registre: **tipo · partes · datas (assinatura/vencimento/fato) · valor · status**. Alimenta `memoria-de-caso-civel` (docs numerados "doc. N") e `calculos-civeis`.

## 3. SAIDA

```
INVENTARIO DOCUMENTAL
doc. 1 — <tipo> — partes — data — valor — [OK / LACUNA]
...
DADOS-CHAVE: partes / datas / valores confirmados
LACUNAS CRITICAS: <o que falta para a tese / o quantum / o titulo>
PROXIMO PEDIDO AO CLIENTE: ...
```

## 4. ALERTAS

- Documento ilegivel/incompleto → marcar **LACUNA**, nunca presumir conteudo (PA-03).
- Titulo sem requisito essencial → executoriedade comprometida (rever via — PA-08).
- Contrato sem 2 testemunhas → nao e titulo executivo; avaliar monitoria.
- Data do fato/contrato define a lei aplicavel (PA-04) e dispara a contagem de prescricao/decadencia (PA-05).
- Sigilo: nao expor dados sensiveis fora do caso (PA-12, LGPD).
