MODELOS DE PEÇA (CHASSIS) — usucapiao-adv-os

Esta pasta traz CHASSIS de peça genéricos e de-identificados (sem dado de cliente),
no PADRÃO ENXUTO da casa. As skills Tier 2 de produção apontam para cá: antes de
redigir, o operador abre o chassi correspondente e substitui os placeholders `[____]`.

ARQUIVOS
- acao-usucapiao.md — petição inicial da ação de usucapião (rito comum). Cobre
  extraordinária (CC art. 1.238) e ordinária (CC art. 1.242); especial urbana
  (CC 1.240/CF 183) e rural (CC 1.239/CF 191) entram como VARIAÇÃO em nota.
  Requisitos da posse (mansa/pacífica/contínua + animus domini + prazo), acessão
  da posse (CC art. 1.243), foro da situação do imóvel (CPC art. 47), planta e
  memorial com ART, e o rol COMPLETO de citações/intimações (PA-06): titular e
  confrontantes pessoalmente (Súm. 391 e 263 STF), réus incertos por edital
  (CPC art. 259, III) e intimação de União/Estado/Município (CPC art. 246, §3º).
  Usado pela skill `acao-usucapiao`.
- contestacao-usucapiao.md — defesa do confrontante/réu/ente. Preliminares
  (CPC art. 337) e mérito para DESCARACTERIZAR a posse do autor: detenção/falta de
  animus domini/vício/interrupção (PA-08/09), prazo não cumprido (PA-05), impugnação
  de metragem/confrontações, BEM PÚBLICO ou área non aedificandi (PA-04; Súm. 340
  STF), título/registro e posse do próprio contestante. Side-aware (PA-10).
  Usado pela skill `contestacao-usucapiao`.

REGRAS (valem para todo chassi)
1. Estilo: peça curta (~5 págs), TEXTO CORRIDO, CAIXA ALTA só para destaque.
   Documentos "Doc. nº N" numerados e citados pelo número, ANTES do protocolo;
   Seção de Documentos em SEQUÊNCIA (parágrafo único), não em lista vertical;
   procuração por ÚLTIMO. Sem seção autônoma de juros.
2. Antecipação adversarial no corpo: derrubar a defesa/ataque provável já no texto
   (detenção, falta de animus domini, interrupção, metragem, bem público).
3. Tokens `{{ADVOGADO_NOME}}` / `{{OAB_UF}}` / `{{OAB_NUMERO}}` são resolvidos pela
   persona em runtime — não preencher à mão.
4. PA-01 (jurisprudência/súmula = âncora marcada "(validar)"; confirmar em
   `jurisprudencia-usucapiao` antes de citar):
   - art. 1.238 do CC = a extraordinária DISPENSA justo título e boa-fé (a dispensa
     vem do próprio artigo, NÃO da Súm. 391 STF — não confundir);
   - Súm. 391 STF = citação PESSOAL do confinante/confrontante;
   - Súm. 263 STF = citação pessoal do possuidor;
   - Súm. 340 STF = bem público NÃO é usucapível.
5. PA-04: bem PÚBLICO não é usucapível — conferir matrícula/natureza antes de ajuizar.
6. PA-05: acertar a MODALIDADE e seus requisitos (tempo, metragem, justo título/boa-fé,
   não-propriedade de outro imóvel) via `analise-posse-usucapiao` antes de redigir.
7. PA-06: no judicial, citar SEMPRE confrontantes + titulares + edital de réus incertos
   e intimar União/Estado/Município (CPC art. 246, §3º). Não omitir nenhuma.
8. PA-08/09: posse ad usucapionem (animus domini), nunca mera detenção.
9. Honorários sucumbenciais: incluídos no pedido padrão; ajustar a pedido do operador.
10. Estes chassis NÃO contêm dados de caso. O caso concreto mora em
    `<cwd>/usucapiao/casos/` (gitignored — sigilo OAB + LGPD).

MANUTENÇÃO: ao evoluir o padrão da casa, atualizar o chassi aqui (fonte única) —
não duplicar modelo dentro das skills (limite de 11.264 bytes por SKILL.md). Ao criar
chassi novo: adicionar arquivo aqui, registrar em ARQUIVOS e apontar a skill que o usa.
