---
description: Consultivo empresarial INSS.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [demanda da empresa]
---

Voce foi acionado pelo comando `/consultivo-empresa` do plugin previdenciario-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** orientar a empresa nas obrigacoes e contingencias previdenciarias.

## PROTOCOLO
1. **Acionar a skill `consultivo-empresarial-prev`** — folha e contribuicoes, RAT/FAP, risco de pejotizacao (Sumula 331 TST na interface), eSocial, e defesa em autuacao/NFLD.
2. Datar a analise pela norma vigente no periodo do fato gerador.
3. Sinalizar interface com outras areas (trabalhista/tributario) quando extrapolar o previdenciario — slot generico, sem cross-sell.
4. Submeter a `suprema-corte-previdenciaria` (R1-R4) se virar parecer.

**Skill a acionar:** `consultivo-empresarial-prev`.
