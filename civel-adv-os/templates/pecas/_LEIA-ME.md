MODELOS DE PEÇA (CHASSIS) — civel-adv-os

Esta pasta traz CHASSIS de peça genéricos e de-identificados (sem dado de cliente),
no PADRÃO ENXUTO da casa. As skills de produção apontam para cá: antes de redigir,
o operador abre o chassi correspondente e substitui os placeholders `[____]`.

ARQUIVOS
- acao-indenizatoria.md — ação de indenização por ato ilícito (CC 186/187/927).
  Dano material discriminado (emergente + lucro cessante — CC 402), dano moral,
  nexo, quantum, juros desde o evento na extracontratual (Súm. 54). Foro CPC 53 IV/V.
  Usado por `responsabilidade-civil`.
- acao-monitoria.md — ação monitória (CPC 700-702). Prova escrita sem eficácia de
  título: cheque/NP prescritos, contrato, duplicata sem aceite. Mandado de pagamento;
  embargos monitórios. Usado por `cobranca-monitoria`.
- contestacao-civel.md — contestação do réu (CPC 335-342). Preliminares (CPC 337),
  prejudiciais (prescrição/decadência), mérito, ônus da impugnação especificada
  (CPC 341), eventualidade (CPC 336). Usado por `defesa-civel`.

CONVENÇÕES (valem para todo chassi)
1. Estilo: peça curta (~5 págs), texto corrido, CAIXA ALTA só para destaque.
   Documentos "Doc. nº N" numerados e citados pelo número, ANTES do protocolo;
   Seção de Documentos em SEQUÊNCIA (parágrafo único), não em lista vertical;
   procuração e documentos pessoais por ÚLTIMO. Sem seção autônoma de juros/correção
   (o valor já entra atualizado, com remissão ao `calculos-civeis`).
2. Antecipação adversarial: derrubar a defesa/excludente provável já no corpo.
3. Tokens `{{ADVOGADO_NOME}}` / `{{OAB_UF}}` / `{{OAB_NUMERO}}` são resolvidos pela
   persona em runtime (lendo `civel/persona.md`) — não preencher à mão.
4. PA-01: a jurisprudência dos chassis é âncora; validar/atualizar em `jurisprudencia-civel`
   antes de citar (Súm. 54 juros desde o evento; Súm. 362 correção do moral desde o
   arbitramento; Súm. 43 correção do material; Súm. 247/299/503/504 da monitória).
5. PA-09 (cível residual): se a matéria for de outro plugin (consumo, família, médica,
   imobiliário, fiscal, trabalho, INSS, criminal), NÃO redigir aqui — rotear.
6. Honorários sucumbenciais: o legal (art. 85 do CPC); não pedir contratual.
7. Estes chassis NÃO contêm dados de caso. O caso concreto mora em
   `<cwd>/civel/casos/` (gitignored — sigilo OAB + LGPD).

MANUTENÇÃO: ao evoluir o padrão da casa, atualizar o chassi aqui (fonte única) —
não duplicar modelo dentro das skills (que têm limite de 11.264 bytes).
