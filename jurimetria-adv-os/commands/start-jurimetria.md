---
description: Wizard de configuracao inicial do plugin jurimetria-adv-os — cria a persona do escritorio, aponta o acervo (CASE_ROOT), os tribunais de referencia e grava JURI_PERSONA no settings.local.json. Rode na primeira vez.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [opcional]
---

Voce foi acionado pelo comando `/start-jurimetria` do plugin jurimetria-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** conduzir o wizard de configuracao do plugin no ambiente do operador, gravando a identidade do escritorio fora do plugin distribuido.

## PROTOCOLO

1. **Verificar estado** — se ja existir `jurimetria/cowork-state.json`, avisar que o plugin esta configurado e oferecer reconfigurar; senao, seguir o wizard.
2. **Acionar a skill `onboarding-jurimetria`** — perguntas estruturadas: advogado (nome, OAB, UF), escritorio, cidade/UF, **raiz do acervo (CASE_ROOT)**, **tribunais de referencia** (aliases DataJud), N minimo, revisao R1-R4, modo de saida.
3. **Inicializar o estado** — `python scripts/state.py init` para criar `jurimetria/cowork-state.json`.
4. **Gerar artefatos** — `jurimetria/persona.md` e `jurimetria/config.md` (com CASE_ROOT e tribunais).
5. **Apontar a persona** — gravar `JURI_PERSONA` no `settings.local.json`.
6. **Primeira coleta (opcional)** — oferecer rodar `py scripts/coletar_acervo.py "<CASE_ROOT>"` para o retrato inicial da instrumentacao (quantos CASO.md tem bloco jurimetrico).
7. **Confirmar** a identidade gravada e sugerir `/coletar-acervo` para o primeiro relatorio.

**Skill a acionar:** `onboarding-jurimetria`.
