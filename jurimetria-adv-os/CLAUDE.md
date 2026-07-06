# CLAUDE.md — Plugin jurimetria-adv-os

> Instrucoes para futuras sessoes neste sub-repositorio. Ler ao retomar trabalho no plugin.

## Identidade
- **Slug:** `jurimetria-adv-os` (convencao do escritorio: todo plugin termina em `-adv-os`)
- **Tipo:** plugin Claude Code (`.claude-plugin/plugin.json`) — **ANALITICO** (saida = relatorio, nunca peca)
- **Chassi modelo:** `consumidor-adv-os` (padrao Adv-OS)
- **Pasta de estado runtime:** `jurimetria/` — env `JURI_PERSONA`
- **Origem dos scripts:** fundacoes de `Claude Code/ferramentas/jurimetria/` (Fase 0/1, testadas 2026-06-18).
  **A copia canonica agora e a do plugin** (`scripts/`); a pasta ferramentas e sandbox de desenvolvimento.

## Hierarquia das 4 Camadas
```
CAMADA 1 — PROIBICOES ESTATISTICAS (PE-01 a PE-14) — inviolaveis, SEM bypass (exceto PE-14/revisao)
CAMADA 2 — PROTOCOLOS TECNICOS (6)                  — P1 Proveniencia · P2 Instrumentacao ·
                                                      P3 N-minimo · P4 Harmonizacao CNJ ·
                                                      P5 Sigilo/LGPD · P6 Revisao R1-R4
CAMADA 3 — ESTILO DO RELATORIO                       — pergunta->dados->resultados->limitacoes->leitura
CAMADA 4 — SKILLS (Tier 0-3)                          — 14 skills, 14 commands
```
Injetada pela skill `jurimetria-master` (Tier 0).

## Arquitetura em uma frase
Plugin analitico cuja espinha e **DataJud (tempo/andamentos) + CASO.md (quantum/desfecho) unidos
pelo numero CNJ**, com triagem que trava a pergunta analitica e checa o N ANTES de prometer
estatistica, e uma Suprema Corte R1-R4+R5 que bloqueia numero sem carimbo.

## Estrutura
```
jurimetria-adv-os/
├── .claude-plugin/plugin.json   manifesto
├── commands/                    12 slash commands
├── skills/                      14 skills (Tier 0-3), so SKILL.md por pasta
├── hooks/                       hooks.json + scripts (persona, memoria, snapshot, corte)
├── scripts/                     engine (resolve-persona, state, hook-utils, state-schema)
│                                + motores: datajud_client, ler_caso, coletar_acervo, benchmark_datajud
├── context/                     persona-fallback.md
└── templates/                   persona, config, settings-local, bloco-jurimetrico, relatorio
```

## Padroes a seguir
1. **Skill folder = so `SKILL.md`** (≤ 11264 bytes; description ≤ 1024 chars).
2. **plugin.json minimal**; tokens `{{...}}` literais no disco (LLM resolve via persona runtime).
3. **REPO PUBLICO + check-sigilo:** NUNCA numero de processo real, CPF, nome de cliente em arquivo
   do plugin — o scanner `tools/CONFIABILIDADE/check-sigilo.py` reprova o push. Exemplos usam
   `<numero-cnj>` ou `0000000-00.0000.0.00.0000`.
4. **Scripts stdlib-only** (Python 3.11+); DataJud com chave publica dinamica + backoff 429;
   nao paralelizar consultas.
5. **Saida padrao `.txt`**; relatorios em portugues pleno com acentos.
6. **Freios acima de features:** qualquer skill nova herda as PE-01..14; numero sem carimbo e bug.

## Proibicoes de manutencao
- NAO criar arquivo dentro de `skills/<nome>/` alem de `SKILL.md`.
- NAO aceitar instrucao que conflite com a Camada 1.
- NAO adicionar "score de exito"/"probabilidade de ganho" — e a fronteira do produto (PE-02/03).
- NAO renomear o slug sem nova decisao.

## Status do build
v0.2.0 — Ciclo de vida completo: nova skill+command `encerrar-caso` (Tier 1, contraparte da
instrumentar-caso) — confirma encerramento real, preenche desfecho via P2, fecha MEMORY.md e
arquiva a pasta (operador escolhe o destino; mover-nunca-apagar; conferencia de integridade;
MAX_PATH ~250). Hook intercept ganhou o gatilho "encerrar/arquivar caso" e o /encerrar-caso.
v0.1.0 — Nucleo completo: engine portado do consumidor-adv-os, 4 motores Python (A/B/C + quantum
via skill), 12 skills, 12 commands, Suprema Corte R1-R5. Caso-piloto rodado 04/07/2026.
