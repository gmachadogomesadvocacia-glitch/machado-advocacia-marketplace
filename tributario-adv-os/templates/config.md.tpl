# Configuracao — tributario-adv-os

> Configuracao operacional do plugin no ambiente do escritorio. Vive em
> `<COWORK>/tributario/config.md`. Gerada pelo `/start-tributario`. Editavel
> manualmente — mudancas valem na proxima sessao.

---

## Localizacao

- **Municipio-sede:** {{CIDADE}}
- **UF-sede:** {{UF}}

> Eixo do Protocolo P5 (Localizacao, Rito e Orgao competente). No tributario o foro/orgao
> depende do ente tributante e da via: execucao fiscal (JF federal x vara estadual x vara da
> Fazenda municipal), acao do contribuinte (domicilio do contribuinte), contencioso
> administrativo (DRJ/CARF, TIT, conselho municipal). A `triagem-tributaria` confirma
> orgao/foro/rito caso a caso e grava no `CASO.md`.

---

## Acervo e casos

- **Raiz dos casos:** {{CASE_ROOT}}

<!-- CASE_ROOT define onde vivem as pastas de caso. No Code (com acervo informado):
     `<acervo>/Casos-Ativos` — pasta unificada por caso (CASO.md, MEMORY.md, arquivos/, pecas/),
     compartilhada entre plugins do mesmo cliente. Na nuvem / sem acervo informado:
     `<COWORK>/tributario/casos` (FALLBACK). O estado interno do plugin (cowork-state.json)
     permanece sempre em `<COWORK>/tributario/`, independente da CASE_ROOT. -->

---

## Polo, Frentes e Esferas de Atuacao

- **Polo:** {{POLOS}}
  <!-- contribuinte | fazenda-publica | ambos -->
- **Frentes:** {{EIXOS}}
  <!-- contencioso-administrativo | contencioso-judicial | consultivo-planejamento
       | execucao-fiscal-defesa -->
- **Esferas:** {{ESFERAS}}
  <!-- federal | estadual | municipal -->

> Define o polo (side-awareness), as frentes (administrativa/judicial/consultiva) e as esferas
> (federal/estadual/municipal) que o escritorio atende. A `triagem-tributaria` confirma polo,
> frente, esfera e tributo/tipo de demanda caso a caso.

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
  <!-- sistema juridico, peticionamento eletronico (PJe/eproc/e-CAC/e-Processo/SEI), CRM, nuvem,
       certificado digital ICP-Brasil — campos livres -->

---

**Plugin:** `tributario-adv-os` v{{PLUGIN_VERSION}}
**Gerado em:** {{GENERATED_AT}}
**State source:** `{{COWORK_PATH}}/tributario/cowork-state.json`
