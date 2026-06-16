# Configuracao — transito-adv-os

> Configuracao operacional do plugin no ambiente do escritorio. Vive em
> `<COWORK>/transito/config.md`. Gerada pelo `/start-transito`. Editavel
> manualmente — mudancas valem na proxima sessao.

---

## Localizacao

- **Municipio-sede:** {{CIDADE}}
- **UF-sede:** {{UF}}

> Eixo do Protocolo P5 (Esfera, Orgao Autuador, Instancia e Foro). No transito a via e primeiro
> **administrativa**: o **orgao autuador** (DETRAN, municipio, PRF, DER) emite o auto e a impugnacao
> sobe pelas instancias **JARI -> CETRAN** (ou CONTRANDIFE no ambito federal). Na **via judicial**
> (anulatoria, mandado de seguranca), a competencia segue o **domicilio do condutor/proprietario**
> ou o **local da infracao**, definindo-se **Justica Estadual x Federal** (art. 109 CF — autuador
> federal, ex.: PRF). A `triagem-transito` confirma esfera/instancia/orgao/foro caso a caso e grava
> no `CASO.md`.

---

## Polo e Frentes de Atuacao

- **Polo do cliente:** {{POLO_CLIENTE}}
  <!-- condutor | proprietario do veiculo | indicacao do real condutor
       — defesa: o Estado autua, nao ha outro lado simetrico -->
- **Pares de polo atendidos:** {{POLOS}}
  <!-- condutor | proprietario do veiculo | indicacao do real condutor -->
- **Frentes:** {{FRENTES}}
  <!-- administrativo-defesa-recursos | cnh-habilitacao | judicial-anulatoria-ms
       | analise-vicios-do-auto -->

> Define o polo (side-awareness — defesa do condutor/proprietario) e as frentes (Administrativo —
> defesa/autuacao, JARI, CETRAN / CNH-Habilitacao — suspensao, cassacao, indicacao / Judicial —
> anulatoria, MS / Analise — vicios do auto) que o escritorio atende. A `triagem-transito` confirma
> polo, eixo, dados do auto/infracao e demanda caso a caso.

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
  <!-- sistema juridico, protocolo/peticionamento eletronico (portais DETRAN/SNE, SEI, PJe/eproc/ESAJ),
       consulta de pontuacao/CNH, CRM, nuvem, certificado digital ICP-Brasil — campos livres -->

---

**Plugin:** `transito-adv-os` v{{PLUGIN_VERSION}}
**Gerado em:** {{GENERATED_AT}}
**State source:** `{{COWORK_PATH}}/transito/cowork-state.json`
