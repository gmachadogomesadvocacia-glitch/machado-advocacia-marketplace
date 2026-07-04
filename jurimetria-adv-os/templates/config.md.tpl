# Configuracao — jurimetria-adv-os

> Configuracao operacional do plugin no ambiente do escritorio. Vive em
> `<COWORK>/jurimetria/config.md`. Gerada pelo `/start-jurimetria`. Editavel
> manualmente — mudancas valem na proxima sessao.

---

## Acervo e casos

- **Raiz dos casos (CASE_ROOT):** {{CASE_ROOT}}

<!-- CASE_ROOT = raiz unificada e COMPARTILHADA entre os plugins Adv-OS. No Claude Code,
     usar o acervo do escritorio: `<acervo>/Casos-Ativos`. Fora do Code (fallback),
     usar `<COWORK>/jurimetria/casos`. O coletor (`coletar_acervo.py`) varre TODOS os
     CASO.md sob esta raiz. -->

---

## Tribunais de referencia (benchmark DataJud)

- **Tribunais:** {{TRIBUNAIS}}
  <!-- ex.: TJRJ, TRT1, TRF2 — aliases api_publica_tjrj / api_publica_trt1 / api_publica_trf2 -->

---

## Freios estatisticos

- **N minimo para media/taxa:** {{N_MINIMO}}
  <!-- default 5 — abaixo disto, so leitura qualitativa (PE-04) -->
- **Revisao R1-R4:** {{REVISAO_TECNICA_STATUS}}
  <!-- ATIVA (default) | DESATIVADA -->
- Bypass por demanda (so da revisao): `--no-revisao`, `--quick`, `/revisao off`.
- As Proibicoes Estatisticas (PE-01 a PE-14) **nao tem bypass**.

---

## Tom e saida

- **Perfil de tom:** {{TOM_VOZ_PERFIL}}
- **Modo de melhor saida:** {{MODO_MELHOR_SAIDA}}
  <!-- recomendar-e-listar (default) | apenas-listar -->
- **Output preferido:** {{OUTPUT_FORMAT_PREFERIDO}} (default txt)

---

**Plugin:** `jurimetria-adv-os` v{{PLUGIN_VERSION}}
**Gerado em:** {{GENERATED_AT}}
**State source:** `{{COWORK_PATH}}/jurimetria/cowork-state.json`
