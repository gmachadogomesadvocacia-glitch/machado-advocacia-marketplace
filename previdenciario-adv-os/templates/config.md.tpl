# Configuracao — previdenciario-adv-os

> Configuracao operacional do plugin no ambiente do escritorio. Vive em
> `<COWORK>/previdenciario/config.md`. Gerada pelo `/start-previdenciario`. Editavel
> manualmente — mudancas valem na proxima sessao.

---

## Localizacao

- **Municipio-sede:** {{CIDADE}}
- **UF-sede:** {{UF}}

> Eixo do Protocolo P5 (Localizacao e Foro). No previdenciario, a acao contra o INSS corre na
> Justica Federal (foro do domicilio do segurado; JEF ate 60 SM), com competencia delegada a
> Justica Estadual onde nao houver vara federal. RPPS segue o foro do ente (estadual/federal).
> A `triagem-dogmatica` confirma JEF x JF x delegada caso a caso e grava no `CASO.md`.

---

## Frentes e Sujeitos de Atuacao

- **Frentes:** {{FRENTES}}
  <!-- RGPS | RPPS | previdencia-complementar | acidentario | planejamento-prev-PJ | consultivo-empresarial -->
- **Sujeitos:** {{SUJEITOS}}
  <!-- segurado | dependente | servidor-publico | empresa-PJ -->

> Define as frentes (side-awareness) e os sujeitos que o escritorio atende. A
> `triagem-dogmatica` confirma sujeito, regime, fase e especie de beneficio caso a caso.

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

**Plugin:** `previdenciario-adv-os` v{{PLUGIN_VERSION}}
**Gerado em:** {{GENERATED_AT}}
**State source:** `{{COWORK_PATH}}/previdenciario/cowork-state.json`
