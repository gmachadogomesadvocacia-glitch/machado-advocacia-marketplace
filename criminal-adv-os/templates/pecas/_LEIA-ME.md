MODELOS DE PEÇA (CHASSIS) — criminal-adv-os

Esta pasta traz CHASSIS de peça genéricos e de-identificados (sem dado de cliente),
no PADRÃO ENXUTO da casa. As skills de produção apontam para cá: antes de redigir,
o operador abre o chassi correspondente e substitui os placeholders `[____]`.

ARQUIVOS
- habeas-corpus.md — HC liberatório ou preventivo (CF 5º, LXVIII; CPP 647-667).
  Cobre as hipóteses do CPP 648 (falta de justa causa/trancamento, excesso de prazo,
  nulidade, extinção da punibilidade), o ataque à preventiva (CPP 312/313), a liminar
  e a Súmula 691 do STF. Usado por `habeas-corpus`.
- resposta-acusacao.md — resposta à acusação (CPP 396 e 396-A, 10 dias). Preliminares
  (inépcia CPP 41, justa causa, nulidades), absolvição sumária (CPP 397) e rol de
  testemunhas. Usado por `resposta-acusacao`.
- alegacoes-finais.md — alegações finais / memoriais (CPP 403, § 3º, e 404). Confronto
  da prova, absolvição (CPP 386, inciso a inciso), in dubio pro reo, desclassificação
  e, subsidiariamente, dosimetria favorável. Usado por `alegacoes-finais`.

REGRAS (valem para todo chassi)
1. Estilo: peça curta (~5 págs), TEXTO CORRIDO, CAIXA ALTA só para destaque pontual.
   Documentos "Doc. nº N" numerados e citados pelo número, ANTES do protocolo; quando
   houver seção de documentos, em SEQUÊNCIA (parágrafo único), não em lista vertical;
   procuração e documentos pessoais por ÚLTIMO.
2. Antecipação adversarial no corpo: já derrubar a tese de acusação provável (no HC,
   atacar concretamente os requisitos da preventiva; nas finais, confrontar a prova).
3. Tokens `{{ADVOGADO_NOME}}` / `{{OAB_UF}}` / `{{OAB_NUMERO}}` são resolvidos pela
   persona em runtime — não preencher à mão.
4. PA-01: a jurisprudência/súmulas dos chassis vêm com "(validar)" — confirmar e
   atualizar em `jurisprudencia-criminal` antes de citar (Súm. 691 STF; SV 11/14/24;
   Súm. 231, 444, 545 STJ; Súm. 718/719 STF).
5. PA-08 — invariante ética: a defesa técnica nunca orienta a prática de crime, a
   destruição de prova, a fuga ou a coação de testemunha. Sem bypass.
6. Estes chassis NÃO contêm dados de caso. O caso concreto mora em
   `<cwd>/criminal/casos/` (gitignored — dado penal sensível, LGPD art. 11 + sigilo
   profissional da defesa).

MANUTENÇÃO: ao evoluir o padrão da casa, atualizar o chassi aqui (fonte única) — não
duplicar modelo dentro das skills (que têm limite de 11.264 bytes). Ao criar um chassi
novo, registrá-lo na lista ARQUIVOS acima e apontar a skill que o consome.
