---
name: encerrar-caso
description: >
  ENCERRAR CASO — Skill Tier 1, fecha o ciclo de vida do caso no acervo (contraparte da instrumentar-caso, que abre). Acione em: encerrar caso, arquivar caso, caso transitou em julgado, acordo cumprido/quitado, desistencia homologada, baixa definitiva.
metadata:
  version: "0.1.0"
  area: "Jurimetria"
  tier: 1
---

# ENCERRAR CASO (ciclo de vida — fechamento)

> Skill **Tier 1** — o espelho da `instrumentar-caso`: ela abre o caso instrumentado, esta fecha. Um acervo em que os casos nascem instrumentados mas nao registram desfecho vira estatistica de casos eternamente "em andamento" — a taxa de exito do Modulo C depende DESTA skill rodar em todo encerramento.

---

## 0. QUANDO ACIONAR

(a) Operador pede para "encerrar" ou "arquivar" um caso; (b) transito em julgado com obrigacoes cumpridas; (c) acordo homologado E cumprido/quitado; (d) desistencia/extincao homologada; (e) baixa definitiva. Na duvida se e encerramento ou so mudanca de fase, perguntar — nunca presumir.

## 1. PRE-CONDICOES (o caso encerrou DE VERDADE?)

Antes de qualquer coisa, confirmar com o operador **o que** encerrou o caso e **quando**:

| Situacao | Encerra? |
|----------|----------|
| Transito em julgado + nada a executar (ou execucao ja satisfeita) | SIM |
| Acordo homologado e integralmente cumprido | SIM |
| Desistencia/extincao sem recurso pendente | SIM |
| Sentenca com prazo recursal correndo | NAO — atualizar so `status` |
| Transitado mas com execucao/cumprimento em curso | NAO — `status: transitado`; o `quantum_obtido` ainda vai mudar |
| Acordo homologado com parcelas em aberto | NAO — aguardar quitacao |

Se NAO encerra: oferecer apenas a atualizacao do `status` no bloco (via `instrumentar-caso`) e parar aqui. Encerrar caso com quantum ainda em movimento grava desfecho mentiroso (PE-12).

## 2. ETAPA 1 — DESFECHO NO BLOCO JURIMETRICO (P2)

Acionar a skill `instrumentar-caso` em modo encerramento sobre o `CASO.md`:

1. Preencher o grupo **desfecho**: `status` final (`transitado`/`acordo`/`extinto`/`arquivado`), `resultado` (`procedente`/`parcial`/`improcedente`/`acordo`/`extinto`), `quantum_obtido` (o que o cliente **efetivamente** obteve — acordo conta), `forma_encerramento`, `data_encerramento`.
2. `percentual_exito`: deixar o leitor calcular — nao digitar na mao.
3. Rodar a sincronizacao final do DataJud (`py scripts/ler_caso.py "<CASO.md>" --datajud`) e carimbar `datajud_sync` (PE-10) — e a ultima foto oficial dos andamentos.
4. Validar com `py scripts/ler_caso.py "<CASO.md>"` — parser sem erro = caso entra na estatistica.
5. Regras herdadas: nunca sobrescrever desfecho ja preenchido sem confirmacao; dado desconhecido = vazio + `[PREENCHER]` (PE-12); nome do cliente fora do bloco (PE-06).

**Caso sem bloco jurimetrico:** instrumentar primeiro (identificacao + classificacao + caso), depois o desfecho — o caso encerrado e justamente o mais valioso para a estatistica.

## 3. ETAPA 2 — FECHAR A MEMORIA DO CASO

No `MEMORY.md` do caso (se existir; senao, no proprio `CASO.md`), registrar o fechamento:

- **Resumo final:** o que se pedia, o que se obteve, em quanto tempo (datas de abertura e encerramento).
- **Licoes do caso:** teses que funcionaram/falharam, armadilhas processuais — material bruto para os casos-ouro e para a proxima `viabilidade-jurimetrica` de caso parecido.
- **Destino do arquivamento** (preenchido na Etapa 3): caminho novo da pasta.
- Marcar o cabecalho como `ENCERRADO em AAAA-MM-DD`.

## 4. ETAPA 3 — ARQUIVAMENTO FISICO DA PASTA

O caso sai da raiz de casos ativos (`CASE_ROOT`) para o acervo formal do escritorio.

1. **PERGUNTAR o destino — sempre.** O operador escolhe a serie/pasta do acervo formal. Para ajudar, listar as series existentes no acervo como candidatas (ex.: por area, por tipo de peca, por grupo de casos). **Nunca decidir o destino sozinho.**
2. **Checar o caminho antes de mover:** calcular o caminho completo do arquivo mais fundo da pasta no destino. Se algum passar de ~250 caracteres (limite MAX_PATH do Windows), encurtar o nome da pasta de destino ANTES de mover — nao repetir o nome do cliente em pasta e arquivo.
3. **Mover, nunca apagar.** Mover a pasta INTEIRA do caso (CASO.md, MEMORY.md, arquivos, pecas) preservando a estrutura interna.
4. **Conferir a integridade:** contagem de arquivos e bytes na origem antes == no destino depois. So dar por movido apos a conferencia. Se a origem e o destino estao em espelho/backup, lembrar o operador de que mover = remocao na origem no proximo ciclo de espelhamento.
5. Se o `CASE_ROOT` do config apontar para a raiz ativa, o caso arquivado **sai da varredura de casos ativos** e passa a contar como encerrado nas coletas que varrerem o acervo formal — registrar o caminho novo na ficha para a `coleta-acervo` do futuro.

## 5. ETAPA 4 — FICHA DE ENCERRAMENTO

Entregar `.txt` curto com:

- **Desfecho registrado:** resultado, quantum pretendido x obtido (com carimbo: fonte = bloco do caso + DataJud, data do sync), forma e data de encerramento.
- **Pendencias `[PREENCHER]`** que ficaram no bloco (e o que falta para resolver cada uma).
- **Arquivamento:** caminho antigo → caminho novo, integridade conferida (N arquivos).
- **Estatistica:** confirmacao de que o parser leu o bloco sem erro — o caso agora conta no Modulo C (portfolio/taxa de exito/quantum).

## 6. REGRAS DE OURO

- Esta skill **nao produz numero agregado** — ela alimenta a materia-prima. Analise e com os motores Tier 2 (que herdam PE-01..14).
- Encerramento parcial nao existe: ou o caso fecha (todas as 4 etapas) ou fica ativo com `status` atualizado.
- Se o operador pedir para encerrar em lote, processar caso a caso com checkpoint — desfecho e decisao juridica, nao operacao mecanica.
- A pasta do caso NUNCA e apagada, em nenhuma hipotese — encerrar e mover para o acervo formal, nao destruir.
