# CHANGELOG — marketplace Machado Advocacia

Histórico do conjunto de plugins jurídicos (Adv-OS). Datas em AAAA-MM-DD.

## 2026-07-09

### Redução de tokens — descrições dos slash-commands encurtadas (patch em todos os 15 plugins)
Corte de contexto fixo por turno: cada `description:` de command foi reduzida ao resumo que
aparece no menu `/` (corte no primeiro travessão " — " ou na primeira frase). 164 de 172
descrições encurtadas; **o corpo dos comandos não mudou — nenhuma alteração de comportamento.**
Economia de ~4,4k tokens de contexto fixo por turno com os 15 plugins ativos.
- Bump de patch em todos: consumidor 0.1.1, previdenciario 0.2.2, familia-sucessoes 2.0.2,
  recuperacao-judicial 0.3.1, isencao-ir-doenca 0.1.2, usucapiao 0.1.1, tributario 0.1.2,
  imobiliario 0.1.1, criminal 0.1.1, civel 0.1.1, transito 0.1.1, roteador 1.0.1,
  jurimetria 0.3.1, trabalhista 0.3.1, direito-medico 0.3.1.
- Ressincronizados familia e previdenciario, cujo `plugin.json` estava à frente do
  `marketplace.json` (2.0.1/0.2.0 e 0.2.1/0.2.0) por release anterior incompleta.

## 2026-07-06

### Lacunas C7 aprovadas pelo advogado — 5 skills novas (médico 0.3.0, trabalhista 0.3.0, jurimetria 0.3.0)
Das 8 lacunas candidatas dos pilotos, o advogado aprovou 5 (C7); construídas no mesmo dia:
- **direito-medico (40 skills):** `dano-fracionado-actio-nata` (teste de autonomia do dano ×
  fracionamento artificial; termo inicial por pretensão), `especificacao-de-provas-medica`
  (peça própria, com as 2 regras de ouro da R5: perícia como prova própria subsidiária +
  custeio do réu hipossuficiente CPC 95 §3º/98 §5º/99 §3º) e `ato-de-enfermagem-lei7498`
  (fato de terceiro/dever institucional × ato médico próprio, com cautelas PA-07/PA-08).
- **trabalhista (33 skills):** `execucao-fazenda-publica-trabalhista` — devedora subsidiária
  ente público (Súm. 331 V/VI), rito do art. 535 CPC, precatório × RPV (tetos locais
  [VERIFICAR]), OJ 382 SDI-1, tabela de impugnações típicas da Fazenda + espelho defensivo.
- **jurimetria (14 skills, 14 commands):** `comparativo-varas` + `/comparativo-varas` —
  Módulo B por órgão julgador (mesma comarca, recorte harmonizado PE-09, freio PE-04 por
  unidade), com fronteira ética explícita: nunca para escolher vara.
- Adiados pelo advogado: ação rescisória própria e relatório gerencial agendado; custeio de
  perícia como skill própria dispensado (incorporado à especificação de provas).

### C4 estendido aos 3 consolidados — casos-ouro + regressões + cobertura
- **4 casos-ouro novos** (15 no total, 1+ por plugin com engine): execução frustrada/penhora
  de crédito 855 CPC (trabalhista, do piloto real), MS contra conselho CF 109 VIII e rol ANS
  pós-ADI 7.265 (médico, da auditoria), encerrar-caso com parcelas em aberto (jurimetria).
- **5 regras novas de regressão** (17 no total, todas verdes): 855 I/II na skill de execução,
  ADI 7.265 no validador, CF 109 VIII no MS, marcação de cancelamento da 469, mover-nunca-apagar
  no encerrar-caso.
- **cobertura.md** ganhou os mapas de trabalhista/médico/jurimetria com 8 lacunas candidatas
  vindas dos pilotos (p/ o advogado confirmar — C7).

### Piloto em caso real + ajustes — `trabalhista-adv-os` v0.2.1 e `direito-medico-adv-os` v0.2.1
Validação da v0.2.0 em dois casos reais do escritório (execução trabalhista frustrada e
responsabilidade médica), por agentes auditores independentes. **Ambos APROVADOS COM
RESSALVAS** — e a rodada R5 adversarial provou valor imediato: no caso trabalhista achou
2 falhas materiais na petição real (base legal da penhora de crédito e enquadramento
temporal de fraude à execução) que R1-R4 estruturalmente não pegariam; no médico, expôs
lacuna estratégica na especificação de provas (adesão à perícia sem pedido subsidiário).
Ajustes aplicados:
- **trabalhista:** R5 + FICHA propagados em TODAS as referências residuais "R1-R4"
  (description, README, commands, integrações das skills, hooks, templates, CLAUDE.md);
  `liquidacao-execucao-trabalhista` ganhou a seção **"Execução frustrada e
  redirecionamento"** (penhora de crédito art. 855 CPC ≠ 854 ≠ 860; IDPJ 855-A CLT +
  Tema 1232 STF com ônus do art. 50 CC; sucessão 448-A; fraude à execução 792 CPC com o
  requisito temporal da ação pendente; interposta pessoa) — a lacuna que teria evitado a
  falha da petição real.
- **médico:** últimos resíduos removidos (Sum. 469 na `medico-master`, Sum. 105 no
  `commands/ped.md`, Tema 990 no `commands/plano-saude.md`, 469 no README, contradição
  3/5 anos no frontmatter da `prescricao-erro-medico`, duplicata e fragmento solto).

### Migrar-legados CONCLUÍDO — `trabalhista-adv-os` v0.2.0 e `direito-medico-adv-os` v0.2.0 — PRÉ-PUBLICAÇÃO VERDE
Os dois plugins consolidados passaram pelos mesmos refinos dos outros 13. **Todas as travas
do `pre-publicacao.py` agora passam** (estrutura, engine, regressão, jurisprudência, tokens,
sigilo, smoke).

- **Engine harmonizado (Eixo 2):** `resolve-persona.py`, `pre-compact-snapshot.py` e
  `hooks/hooks.json` do trabalhista regenerados do canônico; `resolve-persona.py` do médico
  recuperou o `/start-medico` na mensagem de fallback. **Prefixo de env do trabalhista
  renomeado `TRABALHISTA_*` → `TRAB_*`** (o guarda exige prefixo ≤ 6 maiúsculas) — o
  `settings.local.json` do escritório ganhou as chaves novas (antigas mantidas na transição).
- **Auditoria de jurisprudência (Eixo 1, 3 agentes web em 06/07/2026):** 36 citações órfãs
  verificadas → 42 entradas novas na curadoria (total 186; livro-razão com 204 distintas,
  0 órfãs). Correções de TEXTO nos dois plugins, destaque:
  - **Súmula 105 STJ** (~25 usos no médico): é sobre honorários em MS — competência de MS
    contra conselho profissional corrigida para **CF art. 109 VIII + Tema 258 STF**;
    competência criminal para CF art. 109 IV.
  - **Súmula 469 STJ** (~52 usos): CANCELADA em 2018 — substituída pela **608** em massa,
    com rótulos da 597/608 corrigidos.
  - **Rol ANS:** a fórmula "Tema 990 pós-Lei 14.454 = rol exemplificativo" estava dupla-
    mente errada (Tema 990 = medicamento sem registro ANVISA) e desatualizada — reescrita
    como **EREsp 1.886.929 + Lei 14.454 + ADI 7.265 STF (set/2025: taxativo mitigado, 5
    requisitos cumulativos)** em todo o plugin médico.
  - **Inexistentes removidas:** "Súmula 14 CFM" (→ Lei 9.784 art. 2º + Lei 3.268/57 art. 22)
    e "Súmula Normativa 91 ANS" (→ RN 565/2022 + RN 563/2022); entradas-sentinela na
    curadoria impedem reaparição.
  - **Outras atribuições corrigidas:** Sum 17 STJ (→ CC 935 + CPP 66/67), Sum 470 STJ
    (cancelada; migração forçada → Lei 9.656 art. 35), Temas 1061/1069/1094/1095 STJ
    (teores reais registrados; usos substituídos pelas bases corretas), Tema 1118 STF
    (é Adm. Pública; pejotização → **Tema 1389 STF, suspensão nacional, mérito pendente**),
    Sum 74/278/244/437/90/338 TST (nuances da Reforma/OJ 142/Tema 497 anotadas).
- **Tokens (Camada 6):** 51 tokens de template dos dois plugins registrados no
  tokens-registry (total 220; zero órfãos).

### `jurimetria-adv-os` v0.2.0 — ciclo de vida completo do caso
- Nova skill + command **`encerrar-caso`** (Tier 1, contraparte da `instrumentar-caso`):
  confirma que o caso encerrou de verdade (execução pendente NÃO encerra), preenche o
  desfecho do bloco jurimétrico via P2 (com sync DataJud final e validação do parser),
  fecha o MEMORY.md do caso e arquiva a pasta no acervo formal — o operador escolhe o
  destino, mover-nunca-apagar, conferência de integridade e checagem MAX_PATH (~250).
- Hook de intercept: gatilho "encerrar/arquivar caso" + `/encerrar-caso` na lista de commands.
- Fecha a pendência contínua do caso-piloto: desfecho registrado em todo encerramento.

### C3 nos plugins consolidados — `trabalhista-adv-os` v0.1.2 e `direito-medico-adv-os` v0.1.1
- Rodada **R5 adversarial** e **FICHA DE CONFERÊNCIA** adicionadas à `suprema-corte-trabalhista`
  e à `revisao-final-medica`, no estilo de cada casa — as regras de regressão
  `c3-r5-adversarial-todas-revisoes` e `c3-ficha-todas-revisoes` agora passam nos 14 arquivos.
- **Pendência conhecida (pré-publicação ainda REPROVADA nestas travas, confinadas aos 2
  consolidados):** drift de engine do trabalhista (scripts + hooks.json divergem do canônico
  dos outros 13), 54 citações de tema/súmula a conferir contra a curadoria (Eixo 1 nunca
  rodou neles) e tokens de template fora do registro canônico. É o
  pacote "migrar legados": harmonizar engine + auditoria de jurisprudência + registro de tokens.

### Consolidação — `trabalhista-adv-os` v0.1.1 e `direito-medico-adv-os` v0.1.0
- Os dois últimos plugins hospedados fora do marketplace próprio (repositórios
  `sbroggioadv/trabalhista-adv-os-marketplace` e `sbroggioadv/direito-medico-adv-os-marketplace`)
  foram **incorporados sem alteração de conteúdo** (mesmas versões instaladas no CLI).
- Licença MIT de origem preservada (`LICENSE` dentro de cada pasta de plugin);
  autoria original mantida no `marketplace.json`.
- Com isso o marketplace passa a hospedar os **15 plugins** do escritório; os dois
  marketplaces externos podem ser removidos do CLI após a reinstalação apontar para cá.

## 2026-07-04

### Novo plugin — `jurimetria-adv-os` v0.1.0 (analítico)
- Primeiro plugin **analítico** do marketplace: saída = relatório/análise descritiva, nunca peça.
- Espinha: **DataJud/CNJ** (capa+movimentos — duração/andamentos) + **acervo próprio** (bloco
  jurimétrico nos CASO.md — quantum/desfecho), unidos pelo número CNJ.
- 4 motores Python stdlib-only em `scripts/`: `datajud_client.py` (Módulo A), `benchmark_datajud.py`
  (Módulo B — novo: consulta por classe+assunto+órgão com **janela de maturação** de ajuizamento;
  campo `dataAjuizamento` do índice é string compacta `yyyyMMddHHmmss`), `ler_caso.py` e
  `coletar_acervo.py` (Módulo C, freio de N-mínimo). Origem: fundações testadas de
  `Claude Code/ferramentas/jurimetria/` — a cópia canônica agora é a do plugin.
- Governança: **14 Proibições Estatísticas** (PE-01..14, sem bypass) no lugar das PAs; Suprema
  Corte R1-R4 + R5 red-team estatístico; 12 skills, 12 commands; env `JURI_PERSONA`, estado `jurimetria/`.
- Testes: engine (state/persona/hook) em sandbox; Módulos A/B/C ao vivo contra o DataJud
  (TRT-1); `check-engine.py` verde nos 12; `check-sigilo.py` OK (placeholder todo-zeros allowlisted).

## 2026-06-16

### Eixo 2 — Harmonização e manutenção
- **`.gitattributes`** — normaliza quebras de linha (LF), silencia os avisos CRLF.
- **`tools/check-engine.py`** — guarda de consistência: verifica que os 5 arquivos de encanamento do engine são idênticos (módulo tokens) entre os 11 plugins; acusa drift futura.
- **`ARCHITECTURE.md`** — documenta a arquitetura: encanamento × domínio, tabela de tokens por plugin, regras de manutenção.
- **Engine normalizado** — `resolve-persona.py` passou a usar a forma específica `rode /start-<área>` em todos; docstring de `post-edit-evolve-memory.py` unificado. Baseline do verificador agora verde nos 11.

### Eixo 1 — Auditoria de jurisprudência
- Verificadas 117 citações distintas (90 súmulas + 4 vinculantes + 23 temas) contra fonte (STF/STJ/TNU/TST). ~20 correções em 9 plugins. Destaques: Tema 962 STF→STJ (tributário, 9×); Súm. 380/619 (imobiliário, teses trocadas); 6 súmulas TNU (previdenciário); Tema 692 (família); Súm. 391/263 (usucapião); Tema 987 cancelado (recuperação). Regra: número errado → remover, nunca inventar.

### Plugins construídos / publicados (Etapas A–F)
- **Etapa A** — `consumidor-adv-os` v0.1.0 (Consumidor & Bancário).
- **Etapa B** (migração dos legados ao chassi Adv-OS) — `previdenciario-adv-os` v0.2.0, `familia-sucessoes-adv-os` v2.0.0, `recuperacao-judicial-adv-os` v0.3.0.
- **Antecipado** — `isencao-ir-doenca-adv-os` v0.1.0 (isenção de IRPF por doença grave).
- **Etapa C** — `usucapiao-adv-os` v0.1.0 (judicial + extrajudicial).
- **Etapa D** — `tributario-adv-os` v0.1.1 (3 frentes × 3 esferas; skill dedicada Reforma CBS/IBS).
- **Interface** — cross-routing bidirecional `tributario` ↔ `isencao-ir-doenca`.
- **Etapa E** — `imobiliario-adv-os`, `criminal-adv-os`, `civel-adv-os` (todos v0.1.0).
- **Etapa F** — `transito-adv-os` v0.1.0 (multas e CNH).

Total: **11 plugins**, mesmo chassi Adv-OS (4 Camadas, Selo P1, Suprema Corte R1-R4, persona em runtime), ativos em Code + Cowork + Chat.

## Próximos (não iniciados)
- Eixo 1 (resta): caso-piloto real ponta a ponta + exercitar o engine numa sessão real.
- Eixos 3-5: modelos de peça embarcados, integração com o acervo (Casos-Ativos), atualidade legislativa, decisão público×privado.
- Ideia: `administrativo-adv-os` (servidores, licitações Lei 14.133, atos administrativos; resp. do Estado migraria do cível).
