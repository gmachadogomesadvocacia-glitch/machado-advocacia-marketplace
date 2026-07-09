---
name: onboarding-civel
description: >
  Onboarding civel Tier 1 — configura o escritorio e a persona do plugin civel-adv-os (Adv-OS). Ative quando o usuario disser configurar civel, primeira vez, instalar, comecar a usar, /start-civel, onboarding, persona, configurar escritorio.
metadata:
  version: "0.1.0"
  area: "Direito Civil e Processo Civil"
  tier: 1
---

# ONBOARDING CIVEL

> Tier 1 (Insumo). Wizard de configuracao inicial. Grava a **persona local** do escritorio em `<cwd>/civel/persona.md` (fora do plugin distribuido) e inicializa o estado de caso. Roda uma vez por ambiente; reabrir para reconfigurar.

---

## 0. QUANDO RODAR

- Primeiro uso do plugin neste ambiente, comando `/start-civel`, ou quando os tokens de persona ainda estiverem sem valor.
- Se `civel/persona.md` ja existir, oferecer **reconfigurar** ou **manter**.

## 1. DADOS COLETADOS (persona)

Pergunte o que faltar; nao invente (PA-03):

| Token | Campo | Exemplo |
|-------|-------|---------|
| `{{ADVOGADO_NOME}}` | Nome do advogado | — |
| `{{OAB_UF}}` | UF da OAB | RJ |
| `{{OAB_NUMERO}}` | Numero da OAB | 172.089 |
| `{{FIRM_NAME}}` | Escritorio | — |
| `{{CIDADE}}` / `{{UF}}` | Cidade/UF de atuacao | — |
| `{{EMAIL}}` | Email | — |
| `{{TOM_VOZ_PERFIL}}` | Perfil de tom | tecnico-incisivo |
| `{{TOM_VOZ_INTENSIDADE}}` | Intensidade 0-10 | 7 |

> A cidade/UF e o foro-eixo: orienta competencia (CPC 46/53) e tribunal de referencia para jurisprudencia.

## 2. FRENTES ATIVAS

Pergunte quais frentes o escritorio opera (default: todas):

1. **Responsabilidade civil & indenizatorias** (ato ilicito, dano moral/material/estetico).
2. **Contratos & obrigacoes** (teoria geral, contratos tipicos civis, anulacao de negocio juridico).
3. **Cobranca & execucao** (cobranca, monitoria, execucao de titulo, busca e apreensao).
4. **Obrigacoes & tutelas** (fazer/nao fazer/dar, tutela provisoria, consignacao, defesa civel).

## 3. MODO DE FLUXO

- **checkpoint** (default): para em cada CHECKPOINT do pipeline (`civel-master` §5).
- **continuo** (`--continuo`): produz ate a entrega, com revisao R1-R4 ao final.

## 4. ESTADO DE CASO

Inicializa a convencao de memoria (`memoria-de-caso-civel`, P3):
- **Perguntar se ha acervo** do escritorio. Definir **CASE_ROOT**: no Code, `<acervo>/Casos-Ativos`; sem acervo (Cowork/Chat), FALLBACK `<COWORK>/civel/casos`. Criar a pasta `<CASE_ROOT>/` e gravar `{{CASE_ROOT}}` no `config.md`.
- Pasta de caso **unificada e COMPARTILHADA** entre os plugins Adv-OS: `<CASE_ROOT>/<slug>/` com `CASO.md`, `MEMORY.md`, `arquivos/`, `pecas/` (peças em `<slug>/pecas/`). O estado interno (`<COWORK>/civel/`) nao muda.
- Pasta gitignored por default (sigilo + LGPD — PA-12).
- Alertar se `<cwd>` for pasta sincronizada (OneDrive/iCloud/Google Drive): dados de cliente nao devem vazar.

## 5. GRAVACAO

Gerar `civel/persona.md` do template, preenchendo os tokens. Confirmar resumo ao usuario antes de salvar.

```
PERSONA CIVEL CONFIGURADA
Advogado: {{ADVOGADO_NOME}} — OAB/{{OAB_UF}} {{OAB_NUMERO}}
Escritorio: {{FIRM_NAME}} — {{CIDADE}}/{{UF}}
Tom: {{TOM_VOZ_PERFIL}} {{TOM_VOZ_INTENSIDADE}}/10
Frentes: ...
Modo: checkpoint
```

## 6. COMANDOS

| Comando | Acao |
|---------|------|
| `/start-civel` | Roda este onboarding |
| `/status-civel` | Mostra persona + caso ativo |
| `/caso-civel` | Abre/retoma caso (`memoria-de-caso-civel`) |

> Confirme que a materia e **civel residual** (PA-09) — consumo, familia, imovel, medico, fiscal, penal, trabalho e INSS tem plugins proprios. Depois do onboarding, todo caso novo entra por `triagem-civel`.
