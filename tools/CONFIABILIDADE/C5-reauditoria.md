# CAMADA 5 — ATUALIDADE LEGISLATIVA (re-auditoria periódica)

> A lei muda e a súmula é cancelada (o Tema 987 é o exemplo). Sem re-auditoria, o livro-razão
> envelhece e a confiabilidade cai. Esta é a rotina que mantém tudo vivo.

## O que a rotina faz (a cada execução)
1. **Worklist** — rodar `py tools/CONFIABILIDADE/listar-pendencias-juris.py` para obter SÓ o que
   precisa de atenção: entradas `VALIDAR`, tribunal `?` e `SUPERADO` (a reconfirmar). O que já é
   `CONFIRMADO` não se re-faz — a re-auditoria é barata.
2. **Verificar na WEB** cada pendência contra fonte oficial (STF/STJ/TST/TNU): a súmula/tema
   EXISTE? número e tribunal certos? enunciado bate? está vigente ou foi cancelada/superada?
   (mesma disciplina da auditoria do Eixo 1 — nunca de memória; sem fonte → mantém VALIDAR.)
3. **Atualizar a curadoria** — editar `curadoria-jurisprudencia.json`: VALIDAR→CONFIRMADO (com
   enunciado + fonte + data), resolver os `?` de tribunal, marcar novas cancelações como SUPERADO.
4. **Regenerar** o livro: `py tools/CONFIABILIDADE/gerar-livro-razao.py`.
5. **Revalidar o legislacao_watch** de cada plugin (state-schema.json): os tópicos quentes
   (Reforma CBS/IBS, Lei 14.071, Revisão da Vida Toda etc.) tiveram mudança? Se sim, abrir tarefa.
6. **Suíte** — `py tools/CONFIABILIDADE/pre-publicacao.py`; se passar, commit + push.
7. **Relatar** o que mudou (quantas viraram CONFIRMADO, o que foi cancelado, o que exige correção
   de skill) — e, se uma cancelação afetar peça/skill, gerar a correção (vira regra em regressoes.json).

## Cadência recomendada
**Mensal** é o ponto certo para jurisprudência (STF/STJ publicam súmulas/Temas em ritmo que não
justifica semanal, mas trimestral já arrisca usar precedente superado). Picos legislativos (ex.:
virada da Reforma Tributária 2026-2027) pedem checagem pontual extra.

## Como ligar (decisão do operador)
A rotina é um agente agendado (roda sozinho, periodicamente — é um compromisso recorrente). NÃO
deve ser ligado sem o OK do operador. Para ligar: agendar a execução deste protocolo (mensal),
com saída = atualização da curadoria + regeneração do livro + relatório. Enquanto não ligado, a
re-auditoria pode ser feita manualmente a qualquer tempo rodando os passos 1-7 acima.
