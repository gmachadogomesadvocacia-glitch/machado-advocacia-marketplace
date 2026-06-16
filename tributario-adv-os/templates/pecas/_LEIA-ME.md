MODELOS DE PEÇA (CHASSIS) — tributario-adv-os

Esta pasta traz CHASSIS de peça genéricos e de-identificados (sem dado de cliente),
no PADRÃO ENXUTO da casa. As skills de produção apontam para cá: antes de redigir,
o operador abre o chassi correspondente e substitui os placeholders `[____]`.

ARQUIVOS
- excecao-pre-executividade.md — exceção de pré-executividade em execução fiscal
  (Súmula 393 do STJ): só matéria de ordem pública, sem dilação, sem garantia.
  Módulos A nulidade CDA / B decadência / C prescrição / D intercorrente /
  E ilegitimidade-redirecionamento. Usado por `defesa-execucao-fiscal`.
- embargos-execucao-fiscal.md — embargos à execução fiscal (LEF, art. 16): defesa
  ampla, EXIGE garantia do juízo; efeito suspensivo pelo art. 919, § 1º, do CPC.
  Módulos A–G (inclui excesso de execução e pagamento/parcelamento). Usado por
  `defesa-execucao-fiscal`.
- impugnacao-auto-infracao.md — impugnação administrativa ao auto/lançamento
  (Dec. 70.235/72 — PAF, prazo 30 dias, DRJ); suspende a exigibilidade (CTN 151,
  III). Estadual/municipal: validar conforme ente. Usado por `impugnacao-administrativa`.
- mandado-seguranca-tributario.md — MS contra ato de autoridade fiscal (Lei
  12.016/2009): direito líquido e certo, liminar, prazo de 120 dias x preventivo/
  continuativo. Usado por `mandado-seguranca-tributario`.

REGRAS (valem para todo chassi)
1. Estilo: peça curta (~5 págs), texto corrido, CAIXA ALTA só para destaque pontual.
   Documentos "Doc. nº N" numerados e citados pelo número no corpo, ANTES do
   protocolo; Seção de Documentos em SEQUÊNCIA (parágrafo único), não em lista
   vertical; procuração e documentos pessoais por ÚLTIMO. Sem seção autônoma de
   juros/correção (o valor já entra atualizado).
2. Antecipação adversarial: derrubar a defesa provável já no corpo.
3. Cada chassi abre com NOTA DE USO (quem usa, base legal, opções, o que substituir).
4. Tokens `{{ADVOGADO_NOME}}` / `{{OAB_UF}}` / `{{OAB_NUMERO}}` são resolvidos pela
   persona em runtime — não preencher à mão.
5. PA-01: a jurisprudência dos chassis é âncora; validar/atualizar em
   `jurisprudencia-tributaria` antes de citar (ex.: Súmulas 393/392/430/435/213/460
   do STJ, 269/271 do STF, Temas 566/962/981). NÃO inventar número.
6. Honorários sucumbenciais: NÃO incluir, salvo pedido do operador.
7. Estes chassis NÃO contêm dados de caso. O caso concreto mora em
   `<cwd>/tributario/casos/` (gitignored — sigilo fiscal CTN 198 + LGPD).

MANUTENÇÃO: fonte ÚNICA. Ao evoluir o padrão da casa, atualizar o chassi aqui —
não duplicar modelo dentro das skills (que têm limite de 11.264 bytes). As skills
apenas APONTAM para o chassi (## MODELO DE PEÇA); não copiam o texto.
