# Configuracao — familia-sucessoes-adv-os

> Configuracao operacional do plugin no ambiente do escritorio. Vive em
> `<COWORK>/familia/config.md`. Gerada pelo `/start-familia`. Editavel
> manualmente — mudancas valem na proxima sessao.

---

## Localizacao

- **Municipio-sede:** {{CIDADE}}
- **UF-sede:** {{UF}}

> Eixo do Protocolo P5 (Localizacao e Foro). Na familia, o foro segue a vara de familia da comarca do
> domicilio (foro do incapaz/alimentando quando aplicavel — art. 50 e 53 CPC). No inventario, foro do
> ultimo domicilio do autor da heranca (art. 48 CPC). A `triagem-familia` confirma a via (judicial x
> extrajudicial-cartorio) e o foro caso a caso e grava no `CASO.md`.

---

## Polos e Frentes de Atuacao

- **Polos:** {{POLOS}}
  <!-- requerente | requerido | inventariante | herdeiro | meeiro | consultor | ambos -->
- **Frentes:** {{EIXOS}}
  <!-- familia-contenciosa | sucessoes-inventario | planejamento-sucessorio | consultivo-familia -->

> Define os polos (side-awareness) e as frentes de familia/sucessoes que o escritorio atende. A
> `triagem-familia` confirma polo, area, esfera e rito caso a caso.

---

## Tom de voz

- **Perfil:** {{TOM_VOZ_PERFIL}}
  <!-- tecnico-objetivo | tecnico-didatico | tecnico-cordial | personalizado -->
- **Intensidade:** {{TOM_VOZ_INTENSIDADE}}/10
- **Postura default:** {{POSTURA_DEFAULT}}

> No direito de familia, a combatividade e calibrada pela sensibilidade humana do caso (luto, filhos
> menores, vulneraveis) e pelo melhor interesse da crianca.

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

**Plugin:** `familia-sucessoes-adv-os` v{{PLUGIN_VERSION}}
**Gerado em:** {{GENERATED_AT}}
**State source:** `{{COWORK_PATH}}/familia/cowork-state.json`
