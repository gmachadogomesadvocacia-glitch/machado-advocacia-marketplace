MODELOS DE PEÇA (CHASSIS) — previdenciario-adv-os

Esta pasta traz CHASSIS de peça genéricos e de-identificados (sem dado de cliente),
no PADRÃO ENXUTO da casa. As skills de produção apontam para cá: antes de redigir,
o operador abre o chassi correspondente e substitui os placeholders `[____]`.

ARQUIVOS
- peticao-inicial-concessao-beneficio.md — ação judicial de concessão/restabelecimento
  de benefício contra o INSS (incapacidade, programada, BPC-LOAS). Prévio requerimento
  administrativo (Tema 350 STF), requisitos do benefício, tutela de urgência, foro do
  domicílio do autor (art. 109, §3º, CF) / JEF se ≤ 60 SM. Usado por `peticao-inicial-prev`.
- recurso-administrativo-crps.md — recurso ordinário à Junta de Recursos do CRPS contra
  indeferimento/cessação administrativa do INSS. Prazo 30 dias, efeito regressivo, rebate
  ponto a ponto da carta, prova nova admitida. Usado por `recursos-previdenciarios`.
- _LEIA-ME.md — este arquivo.

CONVENÇÕES (valem para todo chassi)
1. Estilo: peça curta (~5 págs), texto corrido, CAIXA ALTA só para destaque.
   Documentos "Doc. nº N" numerados e citados pelo número, ANTES do protocolo;
   Seção de Documentos em SEQUÊNCIA (parágrafo único), não em lista vertical;
   procuração e documentos pessoais por ÚLTIMO. Sem seção autônoma de juros/correção
   (os atrasados entram com remissão ao `calculos-previdenciarios`; termos só no PEDIDO).
2. Antecipação adversarial: derrubar a tese provável do INSS já no corpo (qualidade de
   segurado/carência, incapacidade não permanente, DII após a DER, perda da qualidade,
   ausência de início de prova material no rural/híbrido, miserabilidade no BPC).
3. Tokens `{{ADVOGADO_NOME}}` / `{{OAB_UF}}` / `{{OAB_NUMERO}}` são resolvidos pela persona
   em runtime (lendo `previdenciario/persona.md`) — não preencher à mão; ficam literais no disco.
4. PA-01: súmulas e temas dos chassis são âncora — validar número, vigência e TRIBUNAL em
   `jurisprudencia-estrategica` antes de citar (Tema 350 STF requerimento prévio; Temas 810
   STF / 905 STJ correção e juros; Súmula 111 STJ honorários; Súmula 149 STJ e Tema 638 STJ
   prova material rural; Temas 27 TNU / 185 STJ miserabilidade BPC; Tema 555 STF EPI/ruído).
   Nunca inventar número nem trocar o tribunal.
5. Cálculo: a RMI e o valor da causa saem do `calculos-previdenciarios` (Protocolo P5,
   memorial comparativo). Não calcular dentro do chassi.
6. Esgotamento da via: o recurso CRPS é administrativo; esgotada a instância (JR + CaJ) e
   mantido o indeferimento, migra-se ao judicial via `peticao-inicial-concessao-beneficio`.
7. Honorários: só o sucumbencial legal (art. 85 do CPC, Súmula 111 STJ); não pedir contratual.
8. Estes chassis NÃO contêm dados de caso. O caso concreto mora em
   `<cwd>/previdenciario/casos/` (gitignored — sigilo OAB + LGPD).

MANUTENÇÃO: ao evoluir o padrão da casa, atualizar o chassi aqui (fonte única) — não
duplicar modelo dentro das skills (que têm limite de 11.264 bytes). Revisão final R1-R4
(`revisao-final` / `suprema-corte-previdenciaria`) antes de qualquer entrega.
