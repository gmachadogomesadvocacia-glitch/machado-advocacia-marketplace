# templates/pecas — chassis de peça (Eixo 3, consumidor-adv-os)

Modelos de peça no estilo da casa. São **chassis** (esqueleto + nota de uso),
não peças prontas: o LLM os especializa a partir da skill correspondente, do
Selo P1 e dos dados do caso, e submete à `revisao-final-consumidor` (R1-R4).

## Arquivos
- `acao-indenizatoria-negativacao.md` — ação declaratória de inexistência de
  débito c/c indenização por inscrição indevida (lado consumidor).
  Skill: `acao-negativacao-indevida`.
- `revisional-bancaria.md` — ação revisional de contrato bancário (lado
  consumidor). Skill: `revisional-bancaria`.
- `contestacao-fornecedor.md` — contestação pelo fornecedor (lado réu).
  Skill: `contestacao-consumidor`.

## Convenções de estilo (padrão da casa)
- Peça **curta** (~5 págs), **texto corrido**; CAIXA ALTA só em destaque pontual.
- **Sem seção autônoma de juros** — cada encargo/tese em parágrafo próprio.
- **Documentos numerados "Doc. nº N"**, citados pelo número no corpo; relação em
  **sequência** num parágrafo único, **antes do protocolo**; **procuração por último**.
- **Antecipação adversarial no corpo** (não em tópico isolado).
- Placeholders `[____]`; tokens `{{ADVOGADO_NOME}}` / `{{OAB_UF}}` /
  `{{OAB_NUMERO}}` permanecem literais no disco (resolvem em runtime via persona).
- **Súmulas/Temas sempre com "(validar)"** (PA-01) — conferir em
  `jurisprudencia-consumidor` antes de fixar. Consagradas usadas: Súm. 297
  (CDC aos bancos), Súm. 385 (negativação preexistente), Súm. 382 (juros >12%
  não é per se abusivo), Súm. 530 (taxa média BACEN), Súm. 539/541
  (capitalização), Súm. 472 (comissão de permanência), Súm. 359 (notificação),
  Tema 929 (dobro independe de má-fé).

## Manutenção
- Cada chassi começa com **NOTA DE USO** (4-8 linhas) — manter atualizada.
- Estes arquivos vivem em `templates/` (não em `skills/<nome>/`, que só aceita
  `SKILL.md` — vide CLAUDE.md, "Proibições de manutenção").
- Ao criar novo chassi: novo `.md` aqui + pointer curto na skill de produção
  correspondente. Nunca embutir dado real de cliente.
- Saída final ao operador em `.txt` (convenção do escritório).
