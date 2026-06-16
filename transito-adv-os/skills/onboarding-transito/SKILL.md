---
name: onboarding-transito
description: >
  Onboarding de transito Tier 1 — configura o escritorio e a persona do operador no plugin de Direito
  de Transito. Fluxo /start-transito: coleta identidade (nome, OAB/UF/numero, firma, cidade/UF, email),
  tom de voz (perfil + intensidade) e os eixos de atuacao (administrativo, CNH/habilitacao, judicial,
  analise de vicios); gera o persona.md a partir do template e inicializa o estado de caso. Aponta para
  /start-transito (configurar), /status-transito (estado atual) e /caso-transito (abrir/retomar caso).
  Ative quando o usuario disser configurar transito, instalar, primeira vez, onboarding, /start-transito,
  configurar escritorio, persona.
metadata:
  version: "0.1.0"
  area: "Direito de Transito"
  tier: 1
---

# ONBOARDING DE TRANSITO

> Tier 1. Wizard de configuracao do plugin no ambiente do operador. Cria a **persona** local (fora do plugin distribuido) e inicializa o estado de caso. Curto e direto: pergunte o que falta, grave, confirme.

---

## 1. O QUE ESTE FLUXO FAZ

`/start-transito` conduz a configuracao inicial:
1. coleta os dados da identidade e do estilo;
2. gera `<cwd>/transito/persona.md` a partir do template, substituindo os tokens;
3. registra os **eixos ativos**;
4. inicializa o estado de caso (pasta de casos vazia).

## 2. DADOS COLETADOS (pergunte os que faltarem)

| Token | Campo |
|-------|-------|
| {{ADVOGADO_NOME}} | Nome do advogado |
| {{OAB_UF}} | UF da OAB |
| {{OAB_NUMERO}} | Numero da OAB |
| {{FIRM_NAME}} | Nome do escritorio |
| {{CIDADE}} | Cidade de atuacao |
| {{UF}} | UF de atuacao |
| {{EMAIL}} | E-mail de contato |
| {{TOM_VOZ_PERFIL}} | Perfil de tom (ex.: tecnico-combativo, sobrio) |
| {{TOM_VOZ_INTENSIDADE}} | Intensidade 0-10 |

**Eixos de atuacao** (marque os ativos):
- **Administrativo** — defesa previa/da autuacao, recurso JARI, recurso CETRAN.
- **CNH / Habilitacao** — suspensao do direito de dirigir, cassacao, reabilitacao, indicacao de condutor.
- **Judicial** — anulatoria de multa/auto, mandado de seguranca.
- **Analise** — vicios e nulidades do auto de infracao.

## 3. PERGUNTAS DO WIZARD (sequencia)

1. Nome completo e OAB (UF + numero)?
2. Nome do escritorio? Cidade/UF de atuacao? E-mail?
3. Tom de voz (perfil) e intensidade (0-10)?
4. Quais eixos voce atende (administrativo / CNH / judicial / analise / todos)?
5. Modo de fluxo: `checkpoint` (default, pausa nos pontos) ou `--continuo`?

## 4. GERACAO DA PERSONA

- Le o template de persona, substitui cada token pelos dados coletados e grava em `<cwd>/transito/persona.md`.
- Os tokens `{{...}}` ficam **literais** no template; so a gravacao do persona.md os resolve.
- A pasta `transito/` fica **fora** do plugin distribuido (sigilo + LGPD — PA-12).
- Alerta se `<cwd>` for pasta sincronizada (OneDrive/iCloud/Google Drive/Dropbox): dados de cliente nao devem persistir em copia espelhada sem ciencia do operador.

## 5. ESTADO DE CASO

Apos a persona, o plugin mantem o estado por caso em `<cwd>/transito/casos/<slug>/` (ver `memoria-de-caso-transito`). O onboarding apenas garante a existencia da pasta base; nao cria caso.

## 6. SAIDA

```
PERSONA GRAVADA: transito/persona.md
ADVOGADO: {{ADVOGADO_NOME}} — OAB/{{OAB_UF}} {{OAB_NUMERO}}
EIXOS ATIVOS: ...
TOM: {{TOM_VOZ_PERFIL}} / {{TOM_VOZ_INTENSIDADE}}
MODO: checkpoint | continuo
PROXIMO: /caso-transito (abrir caso) · /status-transito (conferir)
```

## 7. COMANDOS

- `/start-transito` — (re)configura a persona e os eixos.
- `/status-transito` — mostra a persona, os eixos e os casos abertos.
- `/caso-transito` — abre ou retoma um caso (`memoria-de-caso-transito`).

> Sem persona configurada, as demais skills usam os tokens literais. Rode `/start-transito` antes de produzir.
