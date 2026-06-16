# CASO — {{CLIENTE}}

> Ficha do caso de familia/sucessoes. Fonte unica das variaveis de **polo**, **area**,
> **tipo**, **regime de bens** e **rito** — todas as skills leem estes campos daqui. Vive em
> `<CASE_ROOT>/{{CASO_SLUG}}/CASO.md` — pasta unificada de caso COMPARTILHADA entre os
> plugins Adv-OS (CASE_ROOT = `<acervo>/Casos-Ativos` no Code; fallback `<COWORK>/familia/casos`).
> Estrutura do caso: `<CASE_ROOT>/{{CASO_SLUG}}/` com `CASO.md`, `MEMORY.md`, `arquivos/` e
> `pecas/` (as pecas produzidas ficam em `<CASE_ROOT>/{{CASO_SLUG}}/pecas/`). Compartimentado
> por cliente (sigilo OAB + LGPD — dados sensiveis do nucleo familiar).

---

## Triagem 4D (triagem-familia)

- **Polo do cliente:** {{POLO}}
  <!-- requerente | requerido | inventariante | herdeiro | meeiro | consultor
       — variavel-mae; toda tese/pedido/tom flipa por ela. Nunca redigir contra o polo do cliente. -->
- **Area:** {{AREA}}
  <!-- familia | sucessoes | ambas -->
- **Tipo:** {{TIPO}}
  <!-- divorcio | separacao | guarda | alimentos | uniao estavel | alienacao parental
       | violencia domestica | interdicao/curatela | inventario | arrolamento | testamento
       | sonegados/colacao | sobrepartilha | planejamento sucessorio | pacto antenupcial -->
- **Esfera:** {{ESFERA}}
  <!-- judicial | extrajudicial (cartorio — Lei 11.441/2007 + Resolucao 35 CNJ) | administrativa
       — pode haver judicial + extrajudicial (Protocolo P4) -->
- **Rito:** {{RITO}}
  <!-- procedimento de familia (arts. 693-699 CPC) | inventario (arts. 610-673 CPC)
       | arrolamento sumario/comum | jurisdicao voluntaria | escritura publica -->
- **Tipo de tarefa:** {{TAREFA}}
  <!-- peticao inicial | contestacao | replica | tutela | recurso | calculo (alimentos/partilha)
       | acordo | escritura | parecer -->

---

## Nucleo Familiar / Partes

| Parte | Qualificacao | Vinculo | Polo | Observacao |
|-------|-------------|---------|------|------------|
| {{PARTE_CLIENTE}} | {{QUALIF_CLIENTE}} | {{VINCULO_CLIENTE}} | {{POLO}} | cliente |
| {{PARTE_ADVERSA}} | {{QUALIF_ADVERSA}} | {{VINCULO_ADVERSA}} | {{POLO_ADVERSO}} | {{OBS_ADVERSA}} |

> **Vinculo:** conjuge, companheiro(a), ex-conjuge, genitor(a), filho(a), herdeiro(a), de cujus,
> inventariante, meeiro(a), etc. Mapear o nucleo familiar completo e o vinculo entre as partes.

---

## Regime de Bens / Vinculo Conjugal

- **Regime de bens:** {{REGIME_BENS}}
  <!-- comunhao parcial (regra desde 1977) | comunhao universal | separacao total/convencional
       | separacao obrigatoria (art. 1.641 CC) | participacao final nos aquestos
       | uniao estavel (presuncao de comunhao parcial — art. 1.725 CC, salvo contrato) -->
- **Data do casamento / inicio da uniao:** {{DATA_VINCULO}}
- **Pacto antenupcial / contrato de convivencia:** {{PACTO}}

---

## Filhos Menores / Incapazes

| Nome | Idade | Menor/Incapaz | Guarda atual | Observacao |
|------|-------|---------------|--------------|------------|
| {{FILHO_NOME}} | {{FILHO_IDADE}} | {{FILHO_INCAPAZ}} | {{FILHO_GUARDA}} | {{FILHO_OBS}} |

> Havendo menor ou incapaz: **intervencao obrigatoria do Ministerio Publico** (art. 178 CPC) e
> **melhor interesse da crianca** (ECA). A via extrajudicial (cartorio) **nao** e admitida quando ha
> incapazes ou nascituro (art. 733 CPC; Resolucao 35 CNJ). Guarda compartilhada e a regra (art. 1.584,
> §2º CC; Lei 13.058/2014).

---

## Patrimonio Mapeado

| Bem | Natureza | Comum/Exclusivo | Valor estimado | Observacao |
|-----|----------|-----------------|----------------|------------|
| {{BEM_DESCRICAO}} | {{BEM_NATUREZA}} | {{BEM_COMUM_EXCLUSIVO}} | {{BEM_VALOR}} | {{BEM_OBS}} |

> **Natureza:** imovel, veiculo, conta/aplicacao, quotas/acoes, semovente, direito. **Comum** = entra
> na partilha/meacao conforme o regime; **exclusivo/particular** = nao se comunica (bem anterior,
> heranca, doacao com clausula). Na sucessao, distinguir meacao (do conjuge/companheiro) da heranca
> (dos herdeiros) e a legitima (art. 1.846 CC).

---

## Localizacao e Competencia (Protocolo P5)

- **Domicilio das partes / do de cujus:** {{CIDADE}}/{{UF}}
  <!-- Familia: foro do domicilio (foro do incapaz/alimentando — art. 50 e 53 CPC).
       Inventario: foro do ultimo domicilio do autor da heranca (art. 48 CPC). -->
- **Vara de Familia / Vara de Sucessoes / Cartorio:** {{FORO}}
- **Processo n.:** {{PROCESSO}}

---

## Validacao de Norma Vigente (P1)

- **Status:** {{SELO_STATUS}}
  <!-- PENDENTE | EMITIDO -->
- **Normas validadas:** {{SELO_NORMAS}}
  <!-- CC/2002 (Livro IV Familia / Livro V Sucessoes) + CPC/2015 + lei especial
       (ECA / Estatuto do Idoso / Estatuto da Pessoa com Deficiencia / Lei 11.340 / Lei 11.441 /
       Lei 13.058 / Lei 12.318 / ITCMD estadual) + jurisprudencia STJ/TJ validada -->
- **Data:** {{SELO_DATA}}

> Nenhuma skill de producao roda sem a Validacao de Norma Vigente (CC/2002 + CPC/2015 + lei especial)
> emitida pela `triagem-familia`. Jurisprudencia (STJ/TJ) so e citada apos validacao — nunca inventar.

---

## Prazos Criticos

| Tipo | Marco | Vencimento | Observacao |
|------|-------|------------|------------|
| {{PRAZO_TIPO}} | {{PRAZO_MARCO}} | {{PRAZO_FIM}} | {{PRAZO_OBS}} |

<!-- Abertura de inventario: 60 dias da ciencia do obito (art. 611 CPC; em alguns estados, multa
     de ITCMD se ultrapassado). ITCMD: prazo e aliquota estaduais. Recursos: conferir prazo (apelacao
     15 dias uteis; agravo de instrumento; recurso em jurisdicao voluntaria). Prescricao da peticao de
     heranca (10 anos). Sempre conferir o prazo concreto. -->

---

## Documentos do caso

{{ARQUIVOS}}

<!-- certidao de casamento/nascimento/obito, pacto antenupcial, escrituras e matriculas de imoveis,
     extratos e comprovantes de patrimonio, certidao de dependentes, holerites/IR (alimentos),
     testamento, estudo psicossocial. Numerados "doc. N". -->

---

## Linha de trabalho / Historico

{{LINHA_TRABALHO}}

<!-- Triagem, Validacao de Norma Vigente, documentos analisados, tese definida, pecas produzidas,
     audiencia de conciliacao/instrucao, parecer do MP, sentenca, partilha/formal, recurso. -->

---

**Plugin:** `familia-sucessoes-adv-os` v{{PLUGIN_VERSION}}
**Caso aberto em:** {{GENERATED_AT}}
