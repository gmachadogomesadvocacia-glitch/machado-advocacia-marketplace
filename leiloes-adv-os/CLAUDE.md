# CLAUDE.md — leiloes-adv-os

Instrucoes de operacao do plugin. Lidas pelo Claude ao trabalhar neste repositorio.

## Regra numero um

**Antes de qualquer producao, confirme o POLO.** Este plugin atua **somente por quem compra**: arrematante consumado ou pretendente a arrematante. Executado, devedor fiduciante, exequente e credor fiduciario **nao sao atendidos aqui** — roteie (PA-12). O mesmo leilao gera casos em plugins diferentes conforme o polo.

## Ordem de acionamento

`leiloes-master` (governanca + roteamento) -> `triagem-leiloes` (4D + rito + Selo P1 + prazos) -> `analise-documental-leiloes` -> skill da fase -> `revisao-final-leiloes` (R1-R4) -> linter.

**Nada se produz antes da triagem e do Selo.**

## O que nunca pode passar

1. Norma, Tema ou tese fora da curadoria juridica do plugin.
2. Afirmar que a arrematacao extingue **todo** onus. Cada um se analisa **um a um**, com a base.
3. Citar o **Tema 1.134** sem a **modulacao** (vale para editais divulgados apos a ata).
4. Citar o **Tema 886** sem dizer que esta **em revisao**, com suspensao nacional.
5. Aplicar prazo do CPC em leilao **trabalhista** (CLT 888: edital de 20 dias, sinal de 20%, pagamento em **24 horas**).
6. Aplicar instituto do CPC ao leilao **fiduciario** — la nao ha preco vil, auto de arrematacao nem os 10 dias do art. 903.
6-A. Calcular preco vil pelo art. 891 do CPC no rito do **SFH (Lei 5.741/1971)**. La o piso e o **SALDO DEVEDOR** (art. 6º), nao a avaliacao — e, nao havendo licitante, o juiz adjudica ao credor em **48 horas** (art. 7º). Sinais do rito: CEF no polo ativo, Justica Federal, "execucao hipotecaria".
7. Prometer resultado, rentabilidade ou "lucro certo" (PA-07).
8. Orientar autotutela contra ocupante ou afirmar desocupacao automatica (PA-08, PA-09).
9. Orientar lance sem conferir o rol de impedidos do CPC 890 — **inclusive advogados de qualquer das partes**.

## O prazo que mais se perde

**CPC 886, VI** obriga o edital a mencionar onus, recurso ou processo pendente.
**CPC 903, § 5º, I** da ao arrematante **10 dias** para desistir e reaver o deposito **integral** quando o onus nao foi mencionado.

Em todo caso pos-arremate, a primeira providencia e cruzar edital com matricula e **cravar a data-limite no CASO.md**. Depois da carta, a invalidacao so por acao autonoma (art. 903, § 4º).

## Estrutura

```
skills/          20 skills (Tier 0-3)
commands/        13 commands
scripts/         engine (persona em runtime, estado, schema)
hooks/           SessionStart, UserPromptSubmit, PostToolUse, PreCompact
context/         persona-fallback.md
templates/       CASO.md, MEMORY.md, persona, config, pecas/
```

Estado do plugin em `<COWORK>/leiloes/`; casos em `<CASE_ROOT>/<slug>/`.

## Ao editar este plugin

- Skill nova ou alterada: manter a descricao **curta** (titulo + resumo de uma linha + clausula de gatilho). O custo always-on e dominado pelas descricoes.
- Teto de **11.264 bytes** por SKILL.md.
- `name:` do frontmatter **igual** ao nome da pasta.
- Nao escrever regex com `\b` por heredoc de shell: a barra e comida e vira caractere backspace. Use arquivo `.py` ou raw string.
- Publicacao vale em **tres superficies independentes**: git push, `claude plugin update` (CLI) e "Verificar atualizacoes" no claude.ai (**o app so pega pela terceira**).
