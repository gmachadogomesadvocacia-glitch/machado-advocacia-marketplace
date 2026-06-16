---
name: onboarding-isencao-ir
description: >
  ONBOARDING ISENCAO-IR — Skill Tier 1, wizard de configuracao do plugin no ambiente do escritorio.
  Conduz perguntas estruturadas para criar a pasta isencao-ir/ com identidade do advogado (nome, OAB,
  cidade/UF), frentes de atuacao (administrativa / judicial / manutencao / consultivo), tom, modo de
  melhor saida e ferramentas. Gera persona.md, config.md, a pasta casos/ e aponta ISIR_PERSONA no
  settings.local.json. Alerta LGPD reforcado — dado de saude e SENSIVEL (art. 11). Acione quando o
  operador disser configurar isencao-ir, instalar, primeira vez, /start-isencao-ir, ou onboarding.
metadata:
  version: "0.1.0"
  area: "Isencao de IRPF por Doenca Grave"
  tier: 1
---

# ONBOARDING ISENCAO-IR (/start-isencao-ir)

> Skill **Tier 1** — wizard que configura o plugin no workspace do operador. Gera a persona em runtime e o estado do plugin, para que todas as skills resolvam os tokens `{{...}}` com a identidade real.

---

## 0. FUNCAO

Capturar a identidade do escritorio e gravar o estado (`isencao-ir/cowork-state.json`), substituindo a persona-fallback pela persona real. Roda **antes** de qualquer triagem/producao.

## 1. PERGUNTAS DO WIZARD (em blocos, confirmando ao fim)

**Bloco 1 — Identidade**
- Nome do advogado responsavel
- OAB (numero) e UF
- Nome do escritorio
- Cidade e UF de atuacao (eixo de foro/competencia — Protocolo P5: domicilio do contribuinte, Justica Federal, JEF ate 60 SM)
- Email/telefone (opcional)

**Bloco 2 — Frentes de atuacao** (multipla escolha)
- **administrativa** — requerimento de isencao a fonte pagadora + retificacao da DIRPF na Receita
- **judicial** — acao declaratoria + repeticao de indebito + tutela/MS
- **manutencao** — defesa da isencao ja concedida (cancelamento/revisao pela fonte ou Receita)
- **consultivo** — pareceres de enquadramento

**Bloco 3 — Estilo e operacao**
- Tom de voz: tecnico-objetivo | tecnico-didatico | tecnico-cordial | personalizado
- Intensidade combativa (0-10; default 4 — area sensivel, cliente doente)
- Modo de melhor saida: recomendar-e-listar (default) | apenas-listar
- Revisao Tecnica R1-R4: ativa (default) | desativada
- Output preferido: txt (default — convencao do escritorio) | docx
- Ferramentas (livre): sistema juridico, peticionamento eletronico, CRM, nuvem, assinatura digital

> Faltando dado essencial, pergunte; nao invente (PA-03). Defaults aplicados so quando o operador autoriza ("pode usar o padrao").

## 2. GRAVACAO

1. Rodar `python scripts/state.py init <cowork_path> --firm-name "<...>" --firm-slug "<slug>" --advogado "<...>"` e depois `state.py set` para cada campo coletado (`identity.*`, `tom_voz.*`, `areas`, `preferences.*`, `tools.*`).
2. **Acervo e CASE_ROOT (pasta unificada de caso)** — perguntar se o escritorio tem acervo. No **Code**, `CASE_ROOT = <acervo>/Casos-Ativos`; senao (Cowork/sem acervo), **fallback** `CASE_ROOT = <COWORK>/isencao-ir/casos`. Gravar `{{CASE_ROOT}}` no state/config. E a pasta de caso **COMPARTILHADA** entre os plugins; o estado interno do plugin segue em `<cwd>/isencao-ir/`.
3. Renderizar `templates/persona.md.tpl` → `<cwd>/isencao-ir/persona.md` resolvendo os tokens `{{...}}`.
4. Renderizar `templates/config.md.tpl` → `<cwd>/isencao-ir/config.md` (resolvendo `{{CASE_ROOT}}`).
5. Criar a pasta `<CASE_ROOT>/` (**gitignored** — sigilo OAB + LGPD art. 11).
6. Fundir o template de settings em `<cwd>/.claude/settings.local.json`, apontando `ISIR_PERSONA` para o `persona.md` gerado.

## 3. AVISO DE SINCRONIZACAO (LGPD REFORCADO)

**Dado de saude e dado SENSIVEL** (LGPD art. 11) — diagnostico, CID e laudo medico exigem cuidado redobrado. Se o workspace ou o `CASE_ROOT` estiver em pasta sincronizada (OneDrive/iCloud/Google Drive/Dropbox), **alertar de forma agressiva**: laudo e CID nao devem ir para nuvem de terceiros sem ciencia e base legal (sigilo OAB + art. 11). Confirmar se o operador aceita ou prefere outro local para `<CASE_ROOT>/` (PA-10).

## 4. ENCERRAMENTO

Confirmar o resumo da configuracao e avisar que a partir da proxima interacao a persona real e injetada (a fallback deixa de ser carregada). Sugerir `/status-isencao-ir` para conferir e `triagem-isencao-ir` para abrir o primeiro caso.
