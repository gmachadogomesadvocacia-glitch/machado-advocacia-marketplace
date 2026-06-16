---
name: onboarding-tributario
description: >
  Onboarding Tier 1 — configura o escritorio/persona do plugin tributario. Explica o fluxo
  /start-tributario que gera persona.md a partir do template e coleta os dados do operador (nome,
  OAB/UF, numero, firma, cidade, UF, email, tom de voz e intensidade). Mostra como o estado de caso e
  criado (CASO.md, MEMORY-caso) e aponta para /status-tributario e /caso-tributario. Ative na primeira
  vez, quando o usuario disser configurar plugin tributario, instalar, comecar a usar, configurar
  escritorio, persona, ou digitar /start-tributario.
metadata:
  version: "0.1.0"
  area: "Direito Tributario"
  tier: 1
---

# ONBOARDING TRIBUTARIO

> Tier 1 (Insumo). Primeira execucao do plugin no ambiente do operador. Cria a **persona local** e prepara o **estado de caso**. Nada se produz antes de a persona existir.

---

## 1. FLUXO `/start-tributario`

O comando conduz um wizard curto e grava a persona em `tributario/persona.md` (fora do plugin distribuido — nunca versionar). Os tokens de persona ficam **literais** no template e sao resolvidos so na geracao:

- `{{ADVOGADO_NOME}}`
- `{{OAB_UF}}` e `{{OAB_NUMERO}}`
- `{{FIRM_NAME}}`
- `{{CIDADE}}` e `{{UF}}`
- `{{EMAIL}}`
- `{{TOM_VOZ_PERFIL}}` e `{{TOM_VOZ_INTENSIDADE}}` (escala 0-10)

## 2. DADOS COLETADOS

| Campo | Uso |
|-------|-----|
| Nome do advogado | assinatura, qualificacao |
| OAB/UF + numero | rodape e procuracao |
| Firma / escritorio | papel timbrado |
| Cidade / UF | enderecamento, eixo de foro (JF x estadual) |
| Email | contato |
| Tom de voz (perfil) | camada de estilo (`estilo-juridico-tributario`) |
| Intensidade (0-10) | combatividade dirigida a teses |

> A UF e **eixo critico**: define competencia (Justica Federal para tributo federal; Justica Estadual para ICMS/IPVA/ISS), foro da execucao fiscal e o ente exequente.

## 3. RAIZ DOS CASOS (CASE_ROOT)

O wizard **pergunta o caminho do acervo** (pasta "Gustavo Machado Advocacia" ou diretamente "Casos-Ativos") e define a raiz dos casos:

- **Code (acervo informado):** `CASE_ROOT = <acervo>/Casos-Ativos` — pasta unificada por caso, **compartilhada entre plugins** do mesmo cliente.
- **Nuvem / sem acervo (FALLBACK):** `CASE_ROOT = <cwd>/tributario/casos`.

Cria a pasta de casos se acessivel e grava `{{CASE_ROOT}}` no `config.md`. O estado interno (`cowork-state.json`) fica sempre em `<cwd>/tributario/`.

## 4. ESTADO DE CASO

Apos a persona, cada caso novo gera em `<CASE_ROOT>/<slug>/` (ver `memoria-de-caso-tributario`, Protocolo P3):

- `CASO.md` — estado vivo (partes, tributo, esferas, fatos geradores, prazos, fase, pecas).
- `MEMORY.md` — decisoes estrategicas e historico.
- `arquivos/` — documentos recebidos (auto, CDA, SPED, guias).
- `pecas/` — pecas produzidas (compartilhadas entre plugins do mesmo cliente).

A pasta de caso e **gitignored por default** (sigilo fiscal — PA-12: CTN art. 198 + LGPD).

## 5. COMANDOS

- `/start-tributario` — cria/atualiza a persona (este onboarding).
- `/status-tributario` — mostra o estado do caso ativo e os prazos em curso.
- `/caso-tributario` — abre, retoma ou lista casos em `<CASE_ROOT>/` (Code: `<acervo>/Casos-Ativos`; FALLBACK: `tributario/casos/`).

## 6. ALERTAS

- Se o workspace for pasta sincronizada (OneDrive/Google Drive/iCloud), avisar que dados fiscais sao sigilosos (PA-12) e nao devem ser versionados.
- Persona ausente → rodar `/start-tributario` antes de qualquer triagem ou producao.
- Concluido o onboarding, seguir para `triagem-tributaria`.
