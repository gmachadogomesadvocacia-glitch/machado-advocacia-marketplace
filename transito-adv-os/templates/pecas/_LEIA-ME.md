# MODELOS DE PECA — transito-adv-os (Eixo 3)

Chassis de peca prontos para preencher. **Fonte unica**: estes arquivos sao a
referencia canonica das pecas administrativas e judiciais de transito. As skills
de producao (`defesa-autuacao`, `recursos-administrativos`, `anulatoria-transito`)
apontam para ca — nao duplicar o texto da peca dentro da skill.

## Arquivos

| Arquivo | Peca | Momento / via | Skill |
|---------|------|---------------|-------|
| `defesa-previa-autuacao.md` | Defesa previa / da autuacao (CTB 281-282) | apos a Notificacao de Autuacao (NA), antes da penalidade | `defesa-autuacao` |
| `recurso-jari-cetran.md` | Recurso a JARI (1ª inst.) **e** ao CETRAN (2ª inst.) | apos a Notificacao de Penalidade (NP) | `recursos-administrativos` |
| `anulatoria-multa.md` | Acao anulatoria judicial (Vara da Fazenda / JEFP) | via judicial, com tutela de urgencia | `anulatoria-transito` |

## Convencoes de estilo (padrao da casa — OBRIGATORIO)

1. **Peca curta** e em **TEXTO CORRIDO**: a peca final nao leva markdown
   (sem `#`, `-`, `**`). O `.md` aqui e so o chassi com as marcacoes de NOTA DE USO.
2. **CAIXA ALTA** apenas para destaque pontual (ex.: pedido de ARQUIVAMENTO).
3. **Documentos**: numerar "Doc. nº N" e cita-los **pelo numero** no corpo
   (ex.: "conforme doc. 3"). A relacao de documentos vem **ANTES do protocolo**,
   em **um unico paragrafo, em sequencia** (nao em lista). A **procuracao vem por
   ULTIMO** na relacao.
4. **Antecipacao adversarial no corpo**: enfrentar a tese contraria mais forte
   dentro do proprio texto, nao em topico separado.
5. **Placeholders** `[____]` para dados a preencher. **Qualificacao e assinatura**
   usam tokens de persona: `{{ADVOGADO_NOME}}`, `{{OAB_UF}}`, `{{OAB_NUMERO}}`
   (resolvidos a partir de `transito/persona.md`).
6. **PA-01 — sumulas/jurisprudencia**: citar somente as consagradas e seguir do
   marcador "(validar)". **Nao inventar** sumula, numero ou precedente.
7. Cada chassi abre com **4-8 linhas de NOTA DE USO** (fora da peca final).

## Regra de manutencao (FONTE UNICA)

- Mudou a tese, a estrutura ou um fundamento? **Edite o chassi aqui** — nao a skill.
- As skills `defesa-autuacao`, `recursos-administrativos` e `anulatoria-transito`
  trazem apenas um **POINTER** para o arquivo correspondente. Mantenha o ponteiro
  e o nome do arquivo em sincronia (se renomear um `.md`, atualize a skill).
- Respeitar as Proibicoes Absolutas: **PA-01** (nada inventado), **PA-04** (norma
  vigente na data da infracao), **PA-05** (prazo preclusivo de 30 dias),
  **PA-06** (jamais fraude de pontuacao), **PA-08** (nao confundir instancias).
- Antes de entregar, passar pela `revisao-final-transito` (R1-R4).
