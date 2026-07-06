# MAPA DE COBERTURA DOS PLUGINS (achar lacunas como a do RPPS, sistematicamente)

> A lacuna do RPPS estadual/municipal (caso-piloto) foi achada por acaso, batendo num caso real.
> Este mapa transforma isso em **auditoria**: para cada plugin, os eixos que ele DEVE cobrir × o que
> esta coberto por skill. Revisar junto com a re-auditoria mensal (C5). Marcar lacuna candidata com
> **[GAP?]** — confirmar com o advogado antes de construir (pode estar coberta implicitamente).

Legenda: ✓ coberto por skill dedicada · ~ coberto de forma transversal/parcial · **[GAP?]** candidata a lacuna.

---

## isencao-ir-doenca-adv-os (16 skills)
Eixos: fonte pagadora × via × doença do rol × manutenção.
- Fonte INSS (RGPS) ✓ · RPPS estadual ✓ · RPPS municipal ✓ (corrigido no piloto) · EFPC/fundo de pensão ✓
- Via administrativa (fonte + retificação DIRPF) ✓ · judicial (declaratória + repetição) ✓ · MS ✓
- Indébito no ajuste anual/DIRPF (União) vs. retenção na fonte (ente) ✓ (lição do piloto)
- Manutenção/renovação da isenção ✓ · doença fora do rol → analogia/recusa ~
- **[GAP?]** isenção de IR sobre **complementação de aposentadoria privada** (PGBL/VGBL) — confirmar se a `requerimento-administrativo` cobre a EFPC com a especificidade do art. 6º XIV.

## tributario-adv-os (20 skills)
Eixos: 3 frentes (administrativa/judicial/consultiva) × 3 esferas (federal/estadual/municipal).
- Impugnação ao auto ✓ · recurso CARF/CSRF ✓ · TIT/conselhos estaduais/municipais ~ (mesma skill, validar rito do ente)
- Execução fiscal: embargos ✓ · exceção de pré-executividade ✓ · anulatória ✓ · MS ✓ · repetição/compensação ✓
- Consultivo: planejamento ✓ · parcelamento/transação ✓ · Reforma CBS/IBS ✓
- **[GAP?]** **ITCMD** (esfera estadual) e **contribuições previdenciárias patronais** — confirmar profundidade; tributos citados focam ICMS/ISS/IR/PIS/COFINS.

## consumidor-adv-os (35 skills)
Eixos: polo × 12+ eixos materiais × 4 esferas (judicial/PROCON/consumidor.gov/BACEN-ANATEL-ANAC/extrajudicial).
- Bancário/negativação/telecom/transporte aéreo/vícios/e-commerce/publicidade/cláusulas/superendividamento/imobiliário-consumo ✓
- **[GAP?]** **plano de saúde / ANS** (negativa de cobertura, reajuste abusivo) — não há skill dedicada; é litígio de altíssimo volume. Confirmar se cai em `acao-vicio-fato-produto`/`acao-telecom-servicos` ou merece skill própria.

## civel-adv-os (20 skills)
Eixos: 4 frentes (responsabilidade civil / contratos / cobrança-execução / obrigações-tutelas).
- Responsabilidade civil (+ Estado) ✓ · acidente de trânsito cível ✓ · contratos/anulação ✓ · monitória/cobrança ✓ · execução de título extrajudicial ✓
- **[GAP?]** **família/sucessões e consumidor** são plugins próprios (bom — cross-routing); confirmar que a triagem cível encaminha em vez de duplicar.

## criminal-adv-os (20 skills)
Eixos: 6 fases (investigação → júri → recursos → execução → acordos) × lado (defesa/assistência).
- Investigação/flagrante ✓ · resposta à acusação ✓ · júri ✓ · recursos ✓ · execução penal ✓ · acordos despenalizadores (ANPP/transação) ✓ · HC ✓
- **[GAP?]** **violência doméstica / Lei Maria da Penha** (medidas protetivas, lado vítima/assistência) — confirmar se `assistencia-de-acusacao` cobre.

## familia-sucessoes-adv-os (25 skills)
Eixos: família × sucessões × polos múltiplos.
- Divórcio/separação ✓ · guarda/alimentos ✓ · união estável ✓ · interdição/curatela ✓ · inventário/arrolamento ✓ · planejamento sucessório/holding ✓
- **[GAP?]** **alienação parental** (Lei 12.318) e **reconhecimento/dissolução de união homoafetiva** — confirmar se caem em `guarda-alimentos`/`uniao-estavel`.

## imobiliario-adv-os (20 skills)
Eixos: 4 frentes (locação / contratos / direitos reais-posse / consultivo) × lados.
- Locação (despejo/renovatória/revisional/consignatória) ✓ · compra-venda/distrato ✓ · possessórias ✓ · adjudicação ✓ · alienação fiduciária ✓ · condomínio ✓ · due diligence ✓
- Usucapião → plugin próprio (cross-routing) ✓.

## previdenciario-adv-os (27 skills)
Eixos: RGPS × RPPS × benefícios × fases.
- Aposentadorias/incapacidade/especial/BPC-LOAS ✓ · acidentário ✓ · RPPS servidor ✓ · previdência complementar ✓ · revisional RMI ✓ · administrativo CRPS ✓
- **RVT (Tema 1102 STF / 999 STJ)** — sinalizada como INCONSTITUCIONAL (2024); rever estratégia (ver alerta no endurecimento).
- **[GAP?]** **auxílio-reclusão** e **pensão por morte** com habilitação de dependentes — confirmar se há skill ou cai em `peticao-inicial-prev`.

## recuperacao-judicial-adv-os (19 skills)
Eixos: RJ + extrajudicial × polos (credor[prioritário CTH]/devedor/AJ) × fases.
- Habilitação/impugnação/divergência ✓ · credor trabalhista (MODO CTH) ✓ · cruzamento JT ✓ · plano/assembleia ✓ · viabilidade ✓ · acordo extrajudicial ✓
- **[GAP?]** **falência** (pedido, habilitação na falência, classificação art. 83) — o plugin foca RJ; confirmar se falência está no escopo ou é deliberadamente fora.

## transito-adv-os (20 skills)
Eixos: 3 eixos (administrativo / CNH / judicial) + vícios do auto.
- Defesa prévia ✓ · recurso JARI/CETRAN ✓ · suspensão/cassação CNH ✓ · indicação de condutor ✓ · radar/equipamentos ✓ · anulatória/MS ✓
- Cobertura aderente ao CTB + Lei 14.071/2020.

## usucapiao-adv-os (15 skills)
Eixos: 2 vias (judicial/extrajudicial) × 6 modalidades.
- Extraordinária/ordinária/especial urbana/especial rural/familiar/coletiva ✓ · extrajudicial (cartório) ✓ · impugnação ✓ · possessórias ✓.

---

## Síntese das lacunas candidatas (a confirmar com o advogado — C7)
1. **consumidor** — plano de saúde / ANS (alto volume; provável skill nova).
2. **criminal** — violência doméstica / Maria da Penha.
3. **familia** — alienação parental.
4. **previdenciario** — auxílio-reclusão / pensão por morte (habilitação de dependentes).
5. **tributario** — ITCMD estadual.
6. **recuperacao** — falência (se estiver no escopo desejado).
7. **isencao** — complementação privada (EFPC/PGBL) com especificidade do art. 6º XIV.

> Nenhuma destas é erro: são candidatas. Confirmar caso a caso; se confirmada, vira item de roadmap
> (skill nova) e, depois de construída, um **caso-ouro** em `casos-ouro/`.

---

## Plugins consolidados em 06/07/2026 (mapeados nos pilotos em caso real)

## trabalhista-adv-os (32 skills)
Eixos: 2 polos × fases (conhecimento/recursal/liquidação-execução) × consultivo.
- Conhecimento (inicial/contestação/réplica/audiência/razões finais) ✓ · recursal completo (RO/RR/AIRR/ED/embargos SDI/RE + pareceres de viabilidade) ✓ · CCT ✓ · perícia + quesitos ✓
- Liquidação/execução: impugnação/embargos ✓ · **execução frustrada/redirecionamento (855 CPC, IDPJ/Tema 1232, 448-A, 792, interposta pessoa) ✓ (adicionada na v0.2.1, lição do piloto)**
- Consultivo: contratos preventivos ✓ · medidas disciplinares ✓ · documentos extrajudiciais ✓
- Execução contra a Fazenda (precatório/RPV, art. 535 CPC, OJ 382) ✓ `execucao-fazenda-publica-trabalhista` (construída 06/07/2026, C7 aprovou). · **[GAP adiado]** ação rescisória como peça própria — advogado decidiu não priorizar (raro no acervo).

## direito-medico-adv-os (37 skills)
Eixos: sujeito × modo × esfera × subdomínio (triagem 4D).
- Defesa multi-frente do profissional (cível/criminal/PED CRM-CRO) ✓ · ações contra operadora (oncológico, home care, OPME, TEA, reajuste, rescisão de coletivo) ✓ · consultivo (sociedade, contratos, LGPD, publicidade) ✓ · rol ANS pós-ADI 7.265 ✓ (corrigido 06/07/2026)
- Especificação de provas ✓ `especificacao-de-provas-medica` (inclui o custeio de perícia do réu — CPC 95 §3º/98 §5º/99 §3º, item 4) · actio nata fracionada ✓ `dano-fracionado-actio-nata` · ato de enfermagem ✓ `ato-de-enfermagem-lei7498` (todas construídas 06/07/2026, C7 aprovou; custeio como skill própria foi dispensado — coberto na especificação).

## jurimetria-adv-os (13 skills, analítico)
Eixos: fontes (DataJud × acervo) × módulos (A caso/B benchmark/C portfólio) × ciclo de vida do caso.
- Consulta/benchmark/coleta ✓ · quantum bifásico ✓ · tempo com censura ✓ · viabilidade ✓ · instrumentação no nascimento ✓ · **encerramento com desfecho + arquivamento ✓ (v0.2.0)**
- Comparativo entre varas ✓ `comparativo-varas` (Modulo B por órgão, construída 06/07/2026, C7 aprovou). · **[GAP adiado]** relatório gerencial agendado — advogado decidiu não priorizar por ora.
