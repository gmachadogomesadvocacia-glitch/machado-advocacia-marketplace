# Configuracao — recuperacao-judicial-adv-os

> Configuracao operacional do plugin no ambiente do escritorio. Vive em
> `<COWORK>/recuperacao-judicial/config.md`. Gerada pelo `/start-rj`. Editavel
> manualmente — mudancas valem na proxima sessao.

---

## Localizacao

- **Municipio-sede:** {{CIDADE}}
- **UF-sede:** {{UF}}

> Eixo do Protocolo P5 (Localizacao e Vara). Na insolvencia, a competencia e do juizo do
> principal estabelecimento do devedor (art. 3 LFRJ), em vara empresarial/falimentar quando
> existente, com juizo universal para constricao (Sum. 480 STJ). A `triagem-rj` confirma a
> vara competente caso a caso e grava no `CASO.md`.

---

## Acervo e casos

- **Raiz dos casos:** {{CASE_ROOT}}
  <!-- Pasta unica de caso, COMPARTILHADA entre plugins do mesmo cliente (ex.: RJ +
       trabalhista do mesmo credor). No Claude Code = `<acervo>/Casos-Ativos`; no fallback
       Cowork = `<COWORK>/recuperacao-judicial/casos`. Cada caso vive em
       `<CASE_ROOT>/<slug>/` com CASO.md, MEMORY.md, arquivos/ e pecas/. O estado interno
       do plugin (cowork-state.json) NAO muda — continua em recuperacao-judicial/. -->

---

## Polos e Frentes de Atuacao

- **Polos:** {{POLOS}}
  <!-- credor | credor-trabalhista | devedor-recuperando | administrador-judicial | consultivo -->
- **Frentes:** {{EIXOS}}
  <!-- credor-trabalhista | credor-geral | devedor-recuperando | administrador-judicial | consultivo -->

> Define os polos (side-awareness) e as frentes que o escritorio atende. Eixo prioritario
> absoluto = credor trabalhista. A `triagem-rj` confirma polo, via, esfera e fase caso a caso.

---

## Tom de voz

- **Perfil:** {{TOM_VOZ_PERFIL}}
  <!-- tecnico-objetivo | tecnico-didatico | tecnico-cordial | personalizado -->
- **Intensidade:** {{TOM_VOZ_INTENSIDADE}}/10
- **Postura default:** {{POSTURA_DEFAULT}}

---

## Modo de melhor saida estrategica

- **Modo:** {{MODO_MELHOR_SAIDA}}
  <!-- recomendar-e-listar (default) | apenas-listar -->

---

## Revisao Tecnica

- **Auditoria R1-R4:** {{REVISAO_TECNICA_STATUS}}
  <!-- ATIVA (default) | DESATIVADA -->
- Bypass por demanda: `--no-revisao`, `--quick`, `/revisao off`.

---

## Ferramentas declaradas

- **Ferramentas:** {{FERRAMENTAS}}
  <!-- sistema juridico, peticionamento eletronico, CRM, nuvem, assinatura digital — campos livres -->

---

**Plugin:** `recuperacao-judicial-adv-os` v{{PLUGIN_VERSION}}
**Gerado em:** {{GENERATED_AT}}
**State source:** `{{COWORK_PATH}}/recuperacao-judicial/cowork-state.json`
