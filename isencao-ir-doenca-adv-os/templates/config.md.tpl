# Configuracao — isencao-ir-doenca-adv-os

> Configuracao operacional do plugin no ambiente do escritorio. Vive em
> `<COWORK>/isencao-ir/config.md`. Gerada pelo `/start-isencao-ir`. Editavel
> manualmente — mudancas valem na proxima sessao.

---

## Localizacao

- **Municipio-sede:** {{CIDADE}}
- **UF-sede:** {{UF}}

> Eixo do Protocolo P5 (Localizacao e Rito). Na isencao de IRPF por doenca grave o reu e a
> **Uniao (Fazenda Nacional)**: competencia da **Justica Federal**, foro do **domicilio do
> contribuinte** (art. 109, §2º CF). A `triagem-isencao-ir` confirma JEF x vara federal comum
> caso a caso e grava no `CASO.md`.

---

## Frentes e Eixos de Atuacao

- **Frentes:** {{POLOS}}
  <!-- isencao-administrativa | acao-judicial-isencao-restituicao | manutencao-isencao | consultivo -->
- **Eixos:** {{EIXOS}}
  <!-- isencao administrativa (fonte + retificacao DIRPF) | acao judicial de isencao + repeticao de indebito
       | mandado de seguranca | manutencao da isencao | consultivo tributario -->

> Define as frentes (side-awareness) e os eixos da isencao de IR que o escritorio atende. A
> `triagem-isencao-ir` confirma polo, via, esfera e tipo de provento caso a caso.

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

**Plugin:** `isencao-ir-doenca-adv-os` v{{PLUGIN_VERSION}}
**Gerado em:** {{GENERATED_AT}}
**State source:** `{{COWORK_PATH}}/isencao-ir/cowork-state.json`
