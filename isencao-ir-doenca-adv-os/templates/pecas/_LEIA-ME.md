MODELOS DE PEÇA (CHASSIS) — isencao-ir-doenca-adv-os

Esta pasta traz CHASSIS de peça genéricos e de-identificados (SEM dado de cliente),
no PADRÃO ENXUTO da casa. As skills de produção apontam para cá: antes de redigir,
o operador abre o chassi correspondente e substitui os placeholders `[____]`.

ARQUIVOS
- acao-declaratoria-repeticao.md — ação declaratória de isenção de IRPF por doença
  grave c/c repetição de indébito + tutela de urgência (via judicial ordinária).
  Base: art. 6º, XIV, Lei 7.713/88; CTN 168 (5 anos); art. 300 CPC. Súm. 598/627
  STJ. Réu: União + fonte pagadora. Foro: domicílio do autor (Justiça Federal/JEF).
  Usado por `acao-isencao-ir`.
- requerimento-administrativo.md — requerimento de isenção à FONTE PAGADORA
  (INSS/RPPS/EFPC) + cessação da retenção + orientação de retificação da DIRPF para
  o passado (5 anos). Base: art. 6º, XIV, Lei 7.713/88 + IN RFB 1500/2014. Exige
  laudo de serviço médico OFICIAL. Usado por `requerimento-administrativo-isencao`.
- mandado-seguranca-isencao.md — MS contra a retenção indevida ou negativa ilegal,
  quando há direito líquido e certo (prova documental, doença no rol). Base: Lei
  12.016/2009 (art. 7º, III liminar; art. 23 — 120 dias). O indébito passado NÃO se
  cobra no MS (Súm. 269/271 STF) — vai pela ação/retificadora. Usado por
  `mandado-seguranca-isencao`.

CONVENÇÕES (valem para todo chassi)
1. Estilo: peça curta (~5 págs), TEXTO CORRIDO, CAIXA ALTA só para destaque pontual.
   Documentos "Doc. nº N" numerados e citados pelo número no corpo, ANTES do
   protocolo; juntada em SEQUÊNCIA (parágrafo único), não em lista vertical;
   procuração e documentos pessoais por ÚLTIMO. Sem seção autônoma de juros/correção
   (o valor já entra atualizado pela Selic, vindo de `calculos-isencao-ir`).
2. Antecipação adversarial no corpo: já derruba "falta laudo oficial" (Súm. 598) e
   "está assintomático / em remissão" (Súm. 627), e delimita o pedido aos PROVENTOS.
3. Cada chassi abre com NOTA DE USO (quem usa, base legal, opções, o que substituir).
4. Tokens `{{ADVOGADO_NOME}}` / `{{OAB_UF}}` / `{{OAB_NUMERO}}` resolvidos pela
   persona em runtime — não preencher à mão.
5. PA-01: a jurisprudência dos chassis é âncora marcada "(validar)" — Súmula 598
   (dispensa laudo OFICIAL) e Súmula 627 (independe da contemporaneidade) do STJ;
   Súmulas 269/271 do STF (MS sem efeito pretérito). Confirmar em
   `jurisprudencia-isencao-ir` antes de citar. NÃO inventar número.
6. LGPD — dado de saúde é SENSÍVEL (art. 11): o laudo/CID vai como DOCUMENTO, sob
   sigilo/segredo de justiça (PA-10); no corpo, só a doença e a data, nunca detalhe
   clínico. PA-04: não opinar sobre o diagnóstico — o laudo é do médico.
7. Só PROVENTOS (PA-06); só doença do rol taxativo (PA-05); restituição só 5 anos
   (PA-09). Quantum sempre de `calculos-isencao-ir` — não estimar (PA-03).
8. Estes chassis NÃO contêm dados de caso. O caso concreto mora em
   `<cwd>/isencao-ir/casos/` (gitignored — sigilo + LGPD art. 11).

MANUTENÇÃO: fonte ÚNICA. Ao evoluir o padrão da casa, atualizar o chassi aqui — não
duplicar modelo dentro das skills (que têm limite de 11.264 bytes). As skills apenas
APONTAM para o chassi (## MODELO DE PEÇA); não copiam o texto. Antes da entrega ao
operador, toda peça passa por `revisao-final-isencao-ir` (R1-R4).
