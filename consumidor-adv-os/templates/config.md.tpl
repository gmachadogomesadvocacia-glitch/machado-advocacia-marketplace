# Configuracao — consumidor-adv-os

> Configuracao operacional do plugin no ambiente do escritorio. Vive em
> `<COWORK>/consumidor/config.md`. Gerada pelo `/start-consumidor`. Editavel
> manualmente — mudancas valem na proxima sessao.

---

## Localizacao

- **Municipio-sede:** {{CIDADE}}
- **UF-sede:** {{UF}}

> Eixo do Protocolo P5 (Localizacao e Rito). No consumo, a competencia favorece o consumidor
> (foro do domicilio — art. 101, I CDC). A `triagem-consumidor` confirma JEC x vara comum x
> coletiva caso a caso e grava no `CASO.md`.

---

## Polos e Eixos de Atuacao

- **Polos:** {{POLOS}}
  <!-- consumidor | fornecedor | ambos -->
- **Eixos:** {{EIXOS}}
  <!-- bancario | negativacao | telecom | servicos-essenciais | aereo | vicio-fato-produto
       | e-commerce | publicidade | clausula-abusiva | cobranca-indevida
       | superendividamento | consumo-imobiliario -->

> Define os polos (side-awareness) e os eixos do consumo que o escritorio atende. A
> `triagem-consumidor` confirma polo, eixo, esfera e rito caso a caso.

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

**Plugin:** `consumidor-adv-os` v{{PLUGIN_VERSION}}
**Gerado em:** {{GENERATED_AT}}
**State source:** `{{COWORK_PATH}}/consumidor/cowork-state.json`
