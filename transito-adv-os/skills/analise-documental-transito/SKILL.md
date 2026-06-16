---
name: analise-documental-transito
description: >
  Analise documental de transito Tier 1 — Protocolo P2 (Integridade Documental). Checklist de integridade
  dos documentos do caso: auto de infracao (AIT — dados do CTB 280), Notificacao de Autuacao (NA) e
  Notificacao de Penalidade (NP) com datas e prazos, foto/registro do equipamento, certidao de afericao
  do radar (INMETRO/IPEM), CRLV/documento do veiculo, extrato/prontuario de pontuacao, comprovante de
  envio das notificacoes (AR), decisoes da JARI/CETRAN e instauracao de processo de suspensao/cassacao.
  Extrai os dados-chave (codigo, natureza, data/local, orgao, pontos) e marca lacunas e vicios. Ative ao
  receber documentos, conferir o auto, montar o dossie ou checar prazos das notificacoes.
metadata:
  version: "0.1.0"
  area: "Direito de Transito"
  tier: 1
---

# ANALISE DOCUMENTAL DE TRANSITO (P2)

> Tier 1. Operacionaliza o **Protocolo P2 — Integridade Documental**. Antes de qualquer tese, conferir o que existe, o que falta e o que esta viciado. Todo dado vem do documento (PA-03); nada se presume.

---

## 1. CHECKLIST DE INTEGRIDADE

| Documento | O que conferir |
|-----------|----------------|
| **AIT (auto de infracao)** | Dados obrigatorios do CTB 280: tipificacao; local, data e hora; veiculo (placa, marca/especie); orgao e agente autuador (identificacao/assinatura); registro do equipamento quando exigido. |
| **Notificacao de Autuacao (NA)** | Data de expedicao e de recebimento; abre o prazo de **defesa previa**. Conferir o **prazo de expedicao** (CTB 281 § unico — em regra 30 dias; ultrapassado → arquivamento). |
| **Notificacao de Penalidade (NP)** | Data; abre o prazo de **recurso a JARI**. Confirmar que houve **as duas** notificacoes (Sum. 312 STJ — PA-07). |
| **Foto / registro do equipamento** | Legibilidade, placa visivel, data/hora, faixa/local; coerencia com o AIT. |
| **Certidao de afericao do radar (INMETRO/IPEM)** | Existencia, validade na data da infracao, equipamento homologado, margem de tolerancia. Ausencia = tese forte. |
| **CRLV / documento do veiculo** | Titularidade, especie, coerencia da placa/RENAVAM com o AIT. |
| **Extrato / prontuario de pontuacao** | Pontos nos 12 meses, naturezas, situacao da CNH, EAR (atividade remunerada). |
| **Comprovante de envio (AR)** | Prova de que NA e NP foram efetivamente enviadas/entregues; endereco correto. |
| **Decisoes JARI / CETRAN** | Motivacao, data, intimacao, prazo do proximo recurso. |
| **Instauracao de suspensao/cassacao** | Portaria/intimacao, prazo de defesa, ampla defesa. |

## 2. EXTRACAO DE DADOS-CHAVE

Do AIT e anexos, extrair literalmente (sem inventar — PA-03):
- **Codigo** da infracao (CTB) e descricao;
- **Natureza** (leve/media/grave/gravissima) e multiplicador;
- **Data / hora / local**;
- **Orgao autuador** (DETRAN/municipal/DER/PRF);
- **Pontos** e **valor** da multa;
- **Veiculo** (placa, RENAVAM) e condutor/proprietario;
- **Equipamento** (sim/nao; numero/serie).

## 3. MAPA DE LACUNAS E VICIOS

Marcar cada item como **OK / FALTA / VICIO**:
- FALTA → pendencia documental a solicitar (ao cliente ou via vista do processo).
- VICIO → alimentar `analise-vicios-auto-infracao` (ex.: NA fora do prazo, ausencia de afericao, dado essencial faltante).

## 4. SAIDA

```
DADOS-CHAVE: codigo / natureza / data-local / orgao / pontos / valor
DOCUMENTOS: [OK | FALTA | VICIO] por item
DUPLA NOTIFICACAO: NA (data) + NP (data) — Sum. 312 [confirmar]
EQUIPAMENTO: afericao INMETRO [OK/ausente]
LACUNAS A SOLICITAR: ...
VICIOS DETECTADOS → analise-vicios-auto-infracao
```

## 5. INTEGRACAO

- `triagem-transito` → fase e prazo.
- `analise-vicios-auto-infracao` → converte vicios em teses.
- `calculos-transito` → prazos das notificacoes e pontuacao.
- `memoria-de-caso-transito` → numerar documentos "doc. N".
- Sigilo OAB + LGPD em todo manuseio (PA-12).
- PDFs de processo: no Code, converter com `ferramentas/pdf-para-md/` antes de analisar (economia de tokens).

## 6. CHECKLIST DE SAIDA

- [ ] AIT conferido contra o CTB 280
- [ ] NA e NP localizadas, com datas e prazos (Sum. 312 — PA-07)
- [ ] Afericao do radar verificada (quando ha equipamento)
- [ ] Dados-chave extraidos do documento (PA-03), sem presumir
- [ ] Lacunas listadas; vicios encaminhados
- [ ] Sigilo/LGPD observados (PA-12)
