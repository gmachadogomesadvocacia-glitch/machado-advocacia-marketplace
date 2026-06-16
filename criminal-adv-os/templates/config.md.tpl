# Configuracao — criminal-adv-os

> Configuracao operacional do plugin no ambiente do escritorio. Vive em
> `<COWORK>/criminal/config.md`. Gerada pelo `/start-criminal`. Editavel
> manualmente — mudancas valem na proxima sessao.

---

## Localizacao

- **Municipio-sede:** {{CIDADE}}
- **UF-sede:** {{UF}}

> Eixo do Protocolo P5 (Localizacao, Rito e Foro/Competencia). No penal a competencia segue, em
> regra, o **lugar da infracao** (art. 70 CPP); crimes dolosos contra a vida vao ao **Tribunal do
> Juri**; define-se ainda **Justica Estadual x Federal** (art. 109 CF), a **vara criminal**, o
> **JECrim** (Lei 9.099) para infracoes de menor potencial ofensivo e a **Vara de Execucoes Penais
> (VEP)** na fase de execucao. A `triagem-criminal` confirma foro/rito/orgao caso a caso e grava no
> `CASO.md`.

---

## Polo e Frentes de Atuacao

- **Polo do cliente:** {{POLO_CLIENTE}}
  <!-- defesa (investigado | reu | acusado | sentenciado) | assistencia-de-acusacao (vitima | ofendido)
       | ambos -->
- **Pares de polo atendidos:** {{POLOS}}
  <!-- defesa (investigado/reu/sentenciado) x assistencia de acusacao (vitima/ofendido) -->
- **Frentes:** {{FRENTES}}
  <!-- investigacao-inquerito | acao-penal | tribunal-do-juri | recursos | execucao-penal
       | acordos-despenalizadores -->

> Define o polo (side-awareness) e as frentes (investigacao/inquerito / acao penal / Tribunal do
> Juri / recursos / execucao penal / acordos despenalizadores) que o escritorio atende. A
> `triagem-criminal` confirma polo, fase/frente, crime/tipificacao e situacao prisional/demanda
> caso a caso.

---

## Acervo e casos

- **Raiz dos casos:** {{CASE_ROOT}}

<!-- CASE_ROOT = pasta unificada de caso, COMPARTILHADA entre os plugins Adv-OS.
     No Code: `<acervo>/Casos-Ativos`; senao (fallback): `<COWORK>/criminal/casos`.
     Cada caso vive em `<CASE_ROOT>/<slug>/` com CASO.md, MEMORY.md, arquivos/ e pecas/
     (peca produzida em `<slug>/pecas/`). O estado interno do plugin NAO muda:
     continua em `<COWORK>/criminal/`. LGPD — dado penal sensivel (art. 11): a pasta
     de casos e gitignored; se a raiz estiver em pasta sincronizada (OneDrive/iCloud/
     Google Drive/Dropbox), alertar sobre sigilo reforcado. -->

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
  <!-- sistema juridico, peticionamento eletronico (PJe/eproc/Projudi/ESAJ/SEEU), CRM, nuvem,
       certificado digital ICP-Brasil — campos livres -->

---

**Plugin:** `criminal-adv-os` v{{PLUGIN_VERSION}}
**Gerado em:** {{GENERATED_AT}}
**State source:** `{{COWORK_PATH}}/criminal/cowork-state.json`
