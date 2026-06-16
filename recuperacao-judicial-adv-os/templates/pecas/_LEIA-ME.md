MODELOS DE PEÇA (CHASSIS) — recuperacao-judicial-adv-os

Esta pasta traz CHASSIS de peça genéricos e de-identificados (sem dado de cliente),
no PADRÃO ENXUTO da casa. As skills de produção apontam para cá: antes de redigir,
o operador abre o chassi correspondente e substitui os placeholders `[____]`.

ARQUIVOS
- habilitacao-retardataria-trabalhista.md — habilitação retardatária de crédito
  trabalhista (art. 10 da LFRE). Opções A/B/C de rescisão + módulo de SUCESSÃO
  opcional. Usado por `credor-trabalhista-rj` (MODO CTH) e `habilitacao-credito-rj`.
- impugnacao-credito-qgc.md — impugnação de crédito / à relação de credores
  (art. 8º da LFRE). Usado por `habilitacao-credito-rj` (§B impugnação judicial).

REGRAS (valem para todo chassi)
1. Estilo: peça curta (~5 págs), texto corrido, CAIXA ALTA só para destaque.
   Documentos "Doc. nº N" numerados e citados pelo número, ANTES do protocolo;
   Seção de Documentos em SEQUÊNCIA (parágrafo único), não em lista vertical;
   procuração e documentos pessoais por ÚLTIMO. Sem seção autônoma de juros/correção.
2. Antecipação adversarial: derrubar a defesa provável já no corpo.
3. Tokens `{{ADVOGADO_NOME}}` / `{{OAB_UF}}` / `{{OAB_NUMERO}}` são resolvidos pela
   persona em runtime — não preencher à mão.
4. PA-01: a jurisprudência dos chassis é âncora; validar/atualizar em `jurisprudencia-rj`
   antes de citar (ex.: REsp 1.851.692/RS, Súmulas 330 e 463 do TST).
5. Honorários sucumbenciais: NÃO incluir, salvo pedido do operador.
6. Estes chassis NÃO contêm dados de caso. O caso concreto mora em
   `<cwd>/recuperacao-judicial/casos/` (gitignored — sigilo OAB + LGPD).

MANUTENÇÃO: ao evoluir o padrão da casa, atualizar o chassi aqui (fonte única) —
não duplicar modelo dentro das skills (que têm limite de 11.264 bytes).
