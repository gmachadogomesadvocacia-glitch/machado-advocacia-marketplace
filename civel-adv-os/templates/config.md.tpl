# Configuracao — civel-adv-os

> Configuracao operacional do plugin no ambiente do escritorio. Vive em
> `<COWORK>/civel/config.md`. Gerada pelo `/start-civel`. Editavel
> manualmente — mudancas valem na proxima sessao.

---

## Localizacao

- **Municipio-sede:** {{CIDADE}}
- **UF-sede:** {{UF}}

> Eixo do Protocolo P5 (Localizacao, Rito e Foro/Competencia). No civel a competencia segue, em
> regra, o **domicilio do reu** (art. 46 CPC); ha foros especiais — **lugar do ato/fato** na
> responsabilidade civil (art. 53, IV, CPC) e **lugar do cumprimento da obrigacao** nos contratos.
> Define-se ainda **Justica Estadual x Federal** (art. 109 CF — Fazenda Publica federal), a **vara
> civel** e o **juizado especial civel** (Lei 9.099, ate 40 SM). A `triagem-civel` confirma
> foro/rito/orgao caso a caso e grava no `CASO.md`.

---

## Acervo e casos

- **Raiz dos casos:** {{CASE_ROOT}}
  <!-- Pasta unificada de caso, COMPARTILHADA entre os plugins Adv-OS. No Claude Code,
       CASE_ROOT = <acervo>/Casos-Ativos; sem acervo (Cowork/Chat), FALLBACK =
       <COWORK>/civel/casos. Cada caso = <CASE_ROOT>/<slug>/ com CASO.md, MEMORY.md,
       arquivos/, pecas/ (peças produzidas em <slug>/pecas/). O estado interno do plugin
       (cowork-state.json) continua em <COWORK>/civel/ — nao muda. -->

---

## Polo e Frentes de Atuacao

- **Polo do cliente:** {{POLO_CLIENTE}}
  <!-- autor (credor | lesado | demandante) | reu (devedor | causador do dano | demandado)
       | ambos -->
- **Pares de polo atendidos:** {{POLOS}}
  <!-- autor (credor/lesado/demandante) x reu (devedor/causador do dano/demandado) -->
- **Frentes:** {{FRENTES}}
  <!-- responsabilidade-civil-indenizatorias | contratos-obrigacoes | cobranca-execucao
       | obrigacoes-tutelas -->

> Define o polo (side-awareness) e as frentes (responsabilidade civil & indenizatorias / contratos
> & obrigacoes / cobranca & execucao / obrigacoes & tutelas) que o escritorio atende. A
> `triagem-civel` confirma polo, frente, relacao juridica/fato e demanda caso a caso.

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
  <!-- sistema juridico, peticionamento eletronico (PJe/eproc/Projudi/ESAJ), CRM, nuvem,
       certificado digital ICP-Brasil — campos livres -->

---

**Plugin:** `civel-adv-os` v{{PLUGIN_VERSION}}
**Gerado em:** {{GENERATED_AT}}
**State source:** `{{COWORK_PATH}}/civel/cowork-state.json`
