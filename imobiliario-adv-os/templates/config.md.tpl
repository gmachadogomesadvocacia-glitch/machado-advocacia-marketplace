# Configuracao — imobiliario-adv-os

> Configuracao operacional do plugin no ambiente do escritorio. Vive em
> `<COWORK>/imobiliario/config.md`. Gerada pelo `/start-imobiliario`. Editavel
> manualmente — mudancas valem na proxima sessao.

---

## Localizacao

- **Municipio-sede:** {{CIDADE}}
- **UF-sede:** {{UF}}

> Eixo do Protocolo P5 (Localizacao, Rito e Foro competente). No imobiliario o foro segue a
> **situacao do imovel** para acoes de direito real (art. 47 CPC — possessorias, reivindicatoria,
> adjudicacao compulsoria, usucapiao); locacao/contratos seguem foro do contrato/domicilio/eleicao;
> registro corre no **registro de imoveis** da circunscricao do imovel (Lei 6.015/73). A
> `triagem-imobiliaria` confirma foro/rito/orgao caso a caso e grava no `CASO.md`.

---

## Polo e Frentes de Atuacao

- **Polo do cliente:** {{POLO_CLIENTE}}
  <!-- locador | locatario | comprador | vendedor | possuidor | condominio | condomino
       | fiduciante | credor-fiduciario | ambos -->
- **Pares de polo atendidos:** {{POLOS}}
  <!-- locador x locatario | comprador x vendedor | possuidor x esbulhador
       | condominio x condomino | fiduciante x credor fiduciario -->
- **Frentes:** {{FRENTES}}
  <!-- locacao | contratos-imobiliarios | direitos-reais-posse | consultivo -->

> Define o polo (side-awareness) e as frentes (locacao / contratos imobiliarios / direitos reais e
> posse / consultivo) que o escritorio atende. A `triagem-imobiliaria` confirma polo, frente,
> imovel (matricula/endereco/area) e contrato/tipo de demanda caso a caso. Usucapiao = interface
> -> rotear ao plugin de usucapiao.

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
  <!-- sistema juridico, peticionamento eletronico (PJe/eproc/Projudi/ESAJ/SEI), CRM, nuvem,
       certificado digital ICP-Brasil — campos livres -->

---

**Plugin:** `imobiliario-adv-os` v{{PLUGIN_VERSION}}
**Gerado em:** {{GENERATED_AT}}
**State source:** `{{COWORK_PATH}}/imobiliario/cowork-state.json`
