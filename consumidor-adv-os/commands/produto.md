---
description: Acionamento direto do nucleo PRODUTO/SERVICO.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [resumo do vicio ou defeito]
---

Voce foi acionado pelo comando `/produto` do plugin consumidor-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** conduzir a demanda de vicio ou fato do produto/servico pelo pipeline e rotear para a producao da acao correta.

## PROTOCOLO

1. **Verificar configuracao** — procurar `consumidor/cowork-state.json` subindo a arvore. Se ausente, sugerir `/start-consumidor`.
2. **Acionar brevemente `consumidor-master`** (Tier 0) para a governanca.
3. **Acionar a `triagem-consumidor`** (4D) para fixar polo, esfera e rito e gravar no `CASO.md`.
4. **Qualificar a demanda (PA-10):** distinguir **vicio** do produto/servico (art. 18/20, decadencia 30/90 dias, art. 26) de **fato** do produto/acidente de consumo (art. 12/14, prescricao 5 anos, art. 27). Tratar garantia e recall.
5. **Rotear** para `acao-vicio-fato-produto`, com o regime de prazo correto explicitado.
6. **Guardas:** prazo de decadencia/prescricao e arrependimento (art. 49) conferidos (PA-11); sem nota fiscal/garantia/laudo/foto, sinalizar `[INFORMAR]` (PA-15).
7. Antes da entrega, lembrar a Revisao R1-R4 (`revisao-final-consumidor`, PA-22).

**Skill a acionar:** `consumidor-master` -> `triagem-consumidor` -> `acao-vicio-fato-produto`.
