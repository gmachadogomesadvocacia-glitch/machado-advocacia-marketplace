---
name: triagem-civel
description: >
  Triagem civel Tier 1 — primeiro contato com a demanda. PRIMEIRO confirma que a materia e civel
  residual (e nao de consumidor/familia/imovel/medico/fiscal/penal/trabalho/INSS — senao roteia). Depois
  classifica em 5 eixos: (1) FRENTE (responsabilidade civil/indenizatorias, contratos/obrigacoes,
  cobranca/execucao, obrigacoes/tutelas), (2) POLO (autor — credor/lesado — x reu — devedor/causador),
  (3) RELACAO/FATO (contrato? ato ilicito? titulo de credito? acidente?), (4) VALOR/QUANTUM pretendido,
  (5) PRAZO em curso (prescricao CC 206, decadencia, contestacao 15 dias). Define a porta de saida.
  Ative no inicio de qualquer caso civel.
metadata:
  version: "0.1.0"
  area: "Direito Civil e Processo Civil"
  tier: 1
---

# TRIAGEM CIVEL

> Tier 1. Primeira skill operacional. **Passo zero: e civel residual?** Se a materia pertence a outro plugin, ROTEIE (PA-09). Confirmado o cabimento, classifica em **5 eixos**, identifica o prazo e roteia. Nada se produz antes da triagem + Selo P1.

---

## 0. PASSO ZERO — E CIVEL RESIDUAL? (PA-09)

Antes de tudo, verifique se a materia NAO e de plugin especializado:

| Se a demanda for... | Roteie para |
|---------------------|-------------|
| Relacao de consumo / banco | `consumidor-adv-os` |
| Divorcio, guarda, alimentos, inventario | `familia-sucessoes-adv-os` |
| Erro/responsabilidade medica | `direito-medico-adv-os` |
| Locacao, despejo, posse, imovel, condominio | `imobiliario-adv-os` |
| Usucapiao | `usucapiao-adv-os` |
| Tributo / fisco | `tributario-adv-os` |
| Crime | `criminal-adv-os` |
| Trabalho / INSS | `trabalhista-adv-os` / `previdenciario-adv-os` |

So prossiga se for **civel residual** (resp. civil geral, contratos/obrigacoes civis, cobranca/execucao, tutelas).

## 1. OS 5 EIXOS

**Eixo 1 — FRENTE**
- Responsabilidade civil & indenizatorias · Contratos & obrigacoes · Cobranca & execucao · Obrigacoes & tutelas (ver `civel-master` §0).

**Eixo 2 — POLO**
- **Autor** (credor/lesado/demandante) × **Reu** (devedor/causador/demandado). Toda peca coerente com o polo (PA-10).

**Eixo 3 — RELACAO / FATO**
- Contrato (qual tipo, data); ato ilicito (qual dano, nexo); titulo de credito (cheque/NP/duplicata — prazos); acidente; negocio juridico viciado.

**Eixo 4 — VALOR / QUANTUM**
- Valor do contrato/divida; quantum indenizatorio pretendido (material — dano emergente/lucro cessante; moral; estetico); base do calculo (`calculos-civeis`).

**Eixo 5 — PRAZO EM CURSO**

| Prazo | Marco | Fonte |
|-------|-------|-------|
| **Prescricao — reparacao civil** | 3 anos do dano (actio nata) | CC 206 §3º, V |
| **Prescricao — geral** | 10 anos | CC 205 |
| **Prescricao — cobranca de divida liquida (instrumento)** | 5 anos | CC 206 §5º, I |
| **Execucao de cheque** | 6 meses apos prazo de apresentacao | Lei 7.357 |
| **Decadencia** (anulacao por vicio) | 4 anos | CC 178 |
| **Contestacao** | 15 dias uteis | CPC 335 |

> Datar pela norma vigente no fato/contrato (PA-04); distinguir prescricao x decadencia (PA-05).

## 2. PERGUNTAS DE ABERTURA (faca as que faltarem)

1. Qual o fato/documento que originou a procura? (contrato, dano, titulo, citacao)
2. Qual a relacao juridica e as partes? Ha contrato? De que tipo?
3. Houve dano? Qual (material/moral/estetico)? Qual o nexo?
4. Datas: fato/contrato, inadimplemento/evento danoso, notificacao, citacao.
5. Valor envolvido / quantum pretendido.
6. O cliente e autor ou reu?

## 3. SAIDA DA TRIAGEM

```
[CABIMENTO: civel residual — OK / ROTEAR para <plugin>]
FRENTE: ...
POLO: ...
RELACAO/FATO: ...
VALOR/QUANTUM: ...
PRAZO MAIS URGENTE: ... (vence em DD/MM)
PORTA DE SAIDA: <skill>
PENDENCIAS DOCUMENTAIS: ...
```
Depois: **Selo P1** → `analise-documental-civel` → porta de producao.

## 4. ALERTAS DE TRIAGEM

- Confirmar SEMPRE o passo zero (PA-09) — civel residual e a maior fonte de erro de roteamento.
- Reparacao civil → conferir prescricao de 3 anos IMEDIATAMENTE (CC 206 §3º, V; PA-05).
- Definir responsabilidade contratual × extracontratual desde a triagem (muda regime/prazo — PA-07).
- Titulo de credito → conferir prazo de execucao × cabimento de monitoria/cobranca (PA-08).
- Dano → exigir prova do dano e do nexo (P2) antes de prometer quantum.
