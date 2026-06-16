# Arquitetura — marketplace Machado Advocacia (Adv-OS)

Fonte da verdade da arquitetura dos plugins jurídicos do escritório. Leia antes de mexer no "motor".

## Os 11 plugins

| Plugin | Área | STATE_DIR | env prefix | onboarding |
|--------|------|-----------|-----------|-----------|
| `consumidor-adv-os` | Consumidor & Bancário | `consumidor` | `CONSUM_` | `/start-consumidor` |
| `previdenciario-adv-os` | Previdenciário | `previdenciario` | `PREV_` | `/start-previdenciario` |
| `familia-sucessoes-adv-os` | Família & Sucessões | `familia` | `FAM_` | `/start-familia` |
| `recuperacao-judicial-adv-os` | Recuperação Judicial | `recuperacao-judicial` | `RJ_` | `/start-rj` |
| `isencao-ir-doenca-adv-os` | Isenção IRPF (doença grave) | `isencao-ir` | `ISIR_` | `/start-isencao-ir` |
| `usucapiao-adv-os` | Usucapião | `usucapiao` | `USU_` | `/start-usucapiao` |
| `tributario-adv-os` | Tributário | `tributario` | `TRIB_` | `/start-tributario` |
| `imobiliario-adv-os` | Imobiliário & Locação | `imobiliario` | `IMOB_` | `/start-imobiliario` |
| `criminal-adv-os` | Penal & Processo Penal | `criminal` | `CRIM_` | `/start-criminal` |
| `civel-adv-os` | Cível residual | `civel` | `CIV_` | `/start-civel` |
| `transito-adv-os` | Trânsito (multas e CNH) | `transito` | `TRAN_` | `/start-transito` |

Todos seguem o mesmo **chassi Adv-OS**: 4 Camadas de governança (Proibições Absolutas > Protocolos > FIRAC/estilo > skills), Selo de Validação Legal Prévia (P1), Suprema Corte R1-R4, persona em runtime.

## Anatomia de um plugin

```
<plugin>-adv-os/
  .claude-plugin/plugin.json     # manifesto (name, version, description, author)
  skills/<nome>/SKILL.md         # 20 skills (Tier 0-3). name: == nome da pasta. <= 11264 bytes.
  commands/<nome>.md             # 13 slash commands
  scripts/                       # ENGINE (parte plumbing + parte dominio — ver abaixo)
  hooks/                         # ENGINE (hooks.json + 3 hooks python)
  context/persona-fallback.md    # DOMINIO (persona generica da area)
  templates/*.tpl                # DOMINIO (persona/config/CASO/MEMORY/settings)
  README.md  CLAUDE.md  .gitignore
```

## Motor: ENCANAMENTO (genérico) × DOMÍNIO (por área)

O "motor" tem duas naturezas. **Não confunda** ao manter:

### Encanamento — IDÊNTICO em todos (módulo tokens)
Plumbing puro. Uma correção aqui deve ser propagada a **todos os 11**. Verificado por `tools/check-engine.py`:
- `scripts/hook-utils.py`
- `scripts/resolve-persona.py`
- `hooks/scripts/post-edit-evolve-memory.py`
- `hooks/scripts/pre-compact-snapshot.py`
- `hooks/hooks.json`

Só diferem nos **tokens de domínio**: STATE_DIR, prefixo de env, slug, sufixo do `/start` (ver tabela acima).

### Domínio — LEGÍTIMAMENTE diferente por plugin
NÃO unificar — o conteúdo é da área:
- `scripts/state.py` — além do plumbing, carrega config de domínio: STATE_DIR, **lista de skills invariantes** (master, triagem, revisao-final, estilo, memoria-de-caso da área), nome da área, enums.
- `scripts/state-schema.json` — enums de domínio (frente, área_foco, legislacao_watch).
- `hooks/scripts/prompt-intercept-corte.py` — o **léxico de gatilho** da área e as mensagens injetadas (Selo, alertas das Proibições Absolutas).
- `context/persona-fallback.md` e `templates/*.tpl` — persona, polos, frentes, prazos da área.

> Resíduo conhecido (cosmético): variáveis internas herdadas do chassi original (`TRIGGER_MEDICO`, `_is_medico`, `CONSUM_*`) persistem nos hooks de vários plugins — são rótulos internos sem efeito de domínio. Renomear é opcional.

## Manutenção do engine

1. **Corrigiu o encanamento?** Aplique a MESMA correção nos 11 plugins (ou no canônico e propague).
2. **Sempre rode** `py tools/check-engine.py` depois — ele acusa se algum plugin divergiu. Saída esperada: "Engine consistente em todos os plugins".
3. **Canônico de referência:** o cluster novo (`civel`, `criminal`, `transito`, `usucapiao`, `tributario`, `imobiliario`, `consumidor`) representa a versão mais recente do engine.

## Governança e Proibições Absolutas

Cada plugin tem suas **Proibições Absolutas (PA)** próprias da área. O número varia legitimamente: os novos têm ~13 PAs; os legados (previdenciário, família, recuperação) têm esquemas mais ricos (20-25), por terem núcleos especializados (ex.: MODO CTH no RJ). **Não force contagem idêntica** — o que se padroniza é a ESTRUTURA (Camada 1, numeração `PA-NN`, tabela), não a quantidade.

## Interfaces entre plugins

Os plugins se cruzam por **roteamento** (nota de texto no master/triagem), não por dependência de código:
- crimes tributários (Lei 8.137) → `criminal-adv-os`
- crime de trânsito (CTB 306/302) → `criminal-adv-os`
- IPTU/ITBI em execução fiscal → `tributario-adv-os`
- imóvel na planta/CDC → `consumidor-adv-os`
- usucapião → `usucapiao-adv-os`
- reparação civil de acidente / DPVAT → `civel-adv-os`
- responsabilidade do Estado (hoje no `civel`) → futuro `administrativo-adv-os`

## Deploy (3 superfícies)

1. **GitHub** (este repo, público) — fonte da verdade publicada.
2. **Claude Code (local):** cache em `~/.claude/plugins/cache/machado-advocacia-marketplace/<plugin>/<versao>/` + registro em `installed_plugins.json` + flag em `settings.json`. **Exige restart do Code** para recarregar.
3. **Cowork + Chat (conta):** claude.ai → Personalizar → Plugins → aba Pessoal → marketplace → "..." → Verificar atualizações (sync por commit; pode levar 1-2 min). Toggle por plugin.
