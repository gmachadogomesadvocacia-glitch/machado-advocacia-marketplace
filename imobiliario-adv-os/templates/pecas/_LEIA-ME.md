MODELOS DE PEÇA (CHASSIS) — imobiliario-adv-os

Esta pasta traz CHASSIS de peça genéricos e de-identificados (sem dado de cliente),
no PADRÃO ENXUTO da casa. As skills Tier 2 de produção apontam para cá: antes de
redigir, o operador abre o chassi correspondente e substitui os placeholders `[____]`.

ARQUIVOS
- acao-despejo-cobranca.md — despejo por falta de pagamento c/c cobrança
  (Lei 8.245/91, art. 9º, III + art. 62). Liminar do art. 59, §1º, IX (sem garantia)
  + caução de 3 aluguéis; valor da causa = 12 aluguéis (art. 58, III).
  Usado pela skill `despejo`.
- reintegracao-posse.md — reintegração de posse (esbulho; arts. 560-566 CPC).
  Força nova (< ano e dia) → liminar do art. 558; requisitos do art. 561; vedação de
  discutir domínio (PA-05; art. 557 CPC; Súm. 487 STF). Usado por `acoes-possessorias`.
- cobranca-cotas-condominiais.md — cobrança de cotas (propter rem). Duas vias:
  execução de título extrajudicial (art. 784, X, CPC) OU cobrança comum; multa de 2%
  (art. 1.336, §1º, CC); penhora da unidade (Lei 8.009, art. 3º, IV).
  Usado por `cobranca-condominial`.

REGRAS (valem para todo chassi)
1. Estilo: peça curta (~5 págs), TEXTO CORRIDO, CAIXA ALTA só para destaque.
   Documentos "Doc. nº N" numerados e citados pelo número, ANTES do protocolo;
   Seção de Documentos em SEQUÊNCIA (parágrafo único), não em lista vertical;
   procuração por ÚLTIMO. Sem seção autônoma de juros/correção (o valor já entra
   atualizado, com remissão à memória de cálculo de `calculos-imobiliarios`).
2. Antecipação adversarial no corpo: derrubar a defesa provável já no texto
   (purgação da mora; exceptio proprietatis; titularidade/edital do arrematante).
3. Tokens `{{ADVOGADO_NOME}}` / `{{OAB_UF}}` / `{{OAB_NUMERO}}` são resolvidos pela
   persona em runtime — não preencher à mão.
4. PA-01: a jurisprudência/súmula dos chassis é âncora marcada "(validar)";
   confirmar em `jurisprudencia-imobiliaria` antes de citar (Súm. 487 STF — posse com
   base no domínio; Temas do STJ sobre propter rem/arrematante).
5. PA-05 (armadilha central): separar posse, propriedade e domínio. Nunca deduzir
   domínio na possessória. Locatário que não devolve = despejo, não esbulho.
6. Honorários sucumbenciais: NÃO incluir, salvo pedido do operador.
7. Estes chassis NÃO contêm dados de caso. O caso concreto mora em
   `<cwd>/imobiliario/casos/` (gitignored — sigilo OAB + LGPD).

MANUTENÇÃO: ao evoluir o padrão da casa, atualizar o chassi aqui (fonte única) —
não duplicar modelo dentro das skills (limite de 11.264 bytes por SKILL.md).
