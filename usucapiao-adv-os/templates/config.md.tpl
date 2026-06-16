# Configuracao — usucapiao-adv-os

> Configuracao operacional do plugin no ambiente do escritorio. Vive em
> `<COWORK>/usucapiao/config.md`. Gerada pelo `/start-usucapiao`. Editavel
> manualmente — mudancas valem na proxima sessao.

---

## Localizacao

- **Municipio-sede:** {{CIDADE}}
- **UF-sede:** {{UF}}

> Eixo do Protocolo P5 (Localizacao e Rito). No usucapiao, a competencia segue a **situacao do
> imovel** (foro rei sitae — art. 47 CPC) e, no extrajudicial, o **Registro de Imoveis da
> circunscricao** do imovel (Lei 6.015 art. 216-A). A `triagem-usucapiao` confirma a praca correta
> e eventual deslocamento para a Justica Federal (Uniao/autarquia/EP) caso a caso e grava no `CASO.md`.

---

## Acervo e casos

- **Raiz dos casos:** {{CASE_ROOT}}
  <!-- No Code, com acervo do escritorio: `<acervo>/Casos-Ativos`. Sem acervo (FALLBACK):
       `<COWORK>/usucapiao/casos`. Cada caso = `<CASE_ROOT>/<slug>/` com CASO.md, MEMORY.md,
       arquivos/, pecas/. Pasta UNIFICADA e COMPARTILHADA entre os plugins Adv-OS. -->

---

## Polos e Frentes de Atuacao

- **Polos:** {{POLOS}}
  <!-- usucapiente | confrontante | ambos -->
- **Frentes:** {{EIXOS}}
  <!-- usucapiao-judicial | usucapiao-extrajudicial | defesa-confrontante | consultivo-regularizacao -->

> Define os polos (side-awareness) e as frentes do usucapiao que o escritorio atende. A
> `triagem-usucapiao` confirma polo, via, modalidade e esfera caso a caso.

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
  <!-- sistema juridico, peticionamento eletronico, CRM, nuvem, assinatura digital,
       consulta de matricula, georreferenciamento — campos livres -->

---

**Plugin:** `usucapiao-adv-os` v{{PLUGIN_VERSION}}
**Gerado em:** {{GENERATED_AT}}
**State source:** `{{COWORK_PATH}}/usucapiao/cowork-state.json`
