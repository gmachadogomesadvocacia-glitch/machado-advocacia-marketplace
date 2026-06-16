# templates/pecas — Chassis de peças (Família e Sucessões)

Modelos-base ("chassis") de petições do plugin `familia-sucessoes-adv-os`. São pontos
de partida, NÃO peças prontas: cada caso exige adequação aos fatos, à comarca e à prova.

## Arquivos

| Arquivo | Peça | Núcleo |
|---------|------|--------|
| `divorcio-litigioso.md` | Divórcio litigioso c/c partilha, guarda, alimentos e nome | EC 66/2010 (sem prazo/culpa); segredo de justiça (art. 189, II, CPC); tutela de urgência p/ alimentos provisórios |
| `acao-alimentos.md` | Ação de alimentos | Lei 5.478/68 (rito); binômio necessidade-possibilidade; alimentos provisórios (art. 4º); prisão civil (Súm. 309 STJ) |
| `inventario.md` | Inventário / arrolamento (abertura judicial) | CPC 610+; abertura em 2 meses (art. 611); primeiras declarações; meação e quinhões; ITCMD; via extrajudicial (art. 610, §1º) |

## Convenções da casa (obrigatórias)

- **Peça curta, TEXTO CORRIDO.** CAIXA ALTA só em destaque pontual (não em tópicos inteiros).
- **Tom sensível** — são relações familiares; sobriedade, sem dramatização nem ataques pessoais.
- **Documentos numerados "Doc. nº N"** em SEQUÊNCIA (sem rol final), citados pelo número ao
  longo do texto, ANTES do protocolo. A **procuração vem por ÚLTIMO**.
- **Segredo de justiça** (art. 189, II, CPC) em todas as peças de família.
- **Placeholders** `[____]` para dados do caso; **tokens** `{{ADVOGADO_NOME}}`, `{{OAB_UF}}`,
  `{{OAB_NUMERO}}` para a persona — substituir todos antes de protocolar.
- Súmulas/temas consagrados podem entrar marcados "(validar)" quando houver dúvida de vigência.
  **Não usar o Tema 692/STF em sucessão** (é matéria previdenciária); para união estável e
  sucessão usar o **Tema 809/STF** e a **Súmula 358/STJ** (alimentos do maior estudante).

## Manutenção

- Verificar dispositivos do CPC/CC a cada reforma legislativa; conferir súmulas/temas na origem.
- Confrontar com a jurisprudência da skill `jurisprudencia-familia` antes de citar precedente.
- Toda peça gerada a partir destes chassis deve passar pela `revisao-final-familia` (R1-R4).
- Novo chassi = novo `.md` aqui + linha na tabela acima + ponteiro na skill de produção correlata.
