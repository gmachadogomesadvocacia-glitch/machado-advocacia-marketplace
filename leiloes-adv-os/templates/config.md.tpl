# Configuracao — leiloes-adv-os

> Configuracao operacional do plugin no ambiente do escritorio. Vive em
> `<COWORK>/leiloes/config.md`. Gerada pelo `/start-leiloes`. Editavel
> manualmente — mudancas valem na proxima sessao.

---

## Localizacao

- **Municipio-sede:** {{CIDADE}}
- **UF-sede:** {{UF}}

> Eixo do Protocolo P5 (Via, Rito e Juizo do leilao). No leilao **judicial**, o ato corre no
> **juizo da execucao** onde se deu a penhora — vara civel, execucao fiscal ou Vara do Trabalho —,
> e cada rito tem prazos proprios (CPC 879-908; Lei 6.830/80 arts. 22-23; CLT 888). No leilao
> **extrajudicial fiduciario**, o procedimento corre no **registro de imoveis da circunscricao do
> imovel** (Lei 9.514/97) e o litigio vai ao **foro da situacao do imovel**. A `triagem-leiloes`
> confirma via, rito e juizo caso a caso e grava no `CASO.md`.

---

## Acervo e casos

- **Raiz dos casos:** {{CASE_ROOT}}
  <!-- Code: <acervo>/Casos-Ativos (acervo informado pelo operador no /start-leiloes).
       Fallback (Cowork): <COWORK>/leiloes/casos. -->

> Cada caso vive em `{{CASE_ROOT}}/<slug>/` com estrutura unificada (CASO.md, MEMORY.md, arquivos/,
> pecas/). Pasta COMPARTILHADA entre plugins do mesmo cliente. O estado interno
> (`cowork-state.json`) NAO usa esta raiz — segue em `<COWORK>/leiloes/`.

---

## Polo e Frentes de Atuacao

- **Polo do cliente:** {{POLO_CLIENTE}}
  <!-- arrematante consumado | pretendente a arrematante (pre-lance)
       — o plugin so atua por quem COMPRA -->
- **Pares de polo atendidos:** {{POLOS}}
  <!-- arrematante | pretendente. Executado, devedor fiduciante, exequente e credor fiduciario
       NAO sao atendidos aqui: rotear ao plugin da relacao-base (PA-12). -->
- **Frentes:** {{FRENTES}}
  <!-- due-diligence-pre-lance | leilao-judicial | leilao-extrajudicial-fiduciario |
       imissao-e-desocupacao | defesa-da-arrematacao | invalidacao-desistencia-eviccao |
       registro-e-baixa-de-onus -->

> Define o polo (side-awareness — sempre o lado de quem compra) e as frentes que o escritorio
> atende. A `triagem-leiloes` confirma polo, via, rito, fase, obstaculo e demanda caso a caso.
> O mesmo leilao gera casos em plugins diferentes conforme o polo: e o POLO que decide.

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
  <!-- sistema juridico, peticionamento eletronico (PJe/eproc/ESAJ), portais de leilao eletronico
       do tribunal, consulta de matricula e certidoes de RI, CRM, nuvem, certificado digital
       ICP-Brasil — campos livres -->

---

**Plugin:** `leiloes-adv-os` v{{PLUGIN_VERSION}}
**Gerado em:** {{GENERATED_AT}}
**State source:** `{{COWORK_PATH}}/leiloes/cowork-state.json`
