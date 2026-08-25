---
description: Obtem a posse do bem arrematado.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [caso]
---

Voce foi acionado pelo comando `/imissao` do plugin leiloes-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** obter a posse apos a arrematacao judicial.

## PROTOCOLO
1. Acionar `imissao-na-posse-arrematante`.
2. Conferir: preco depositado, comissao do leiloeiro paga, ITBI recolhido e **10 dias do art. 903, § 2º** vencidos (CPC 901, § 1º e § 3º).
3. Identificar quem ocupa o imovel; havendo terceiro, acionar `desocupacao-e-ocupantes` antes de peticionar.
4. Redigir a peticao nos autos: arrematacao aperfeicoada (com a **data do auto**), pagamento integral, pedido de expedicao/cumprimento do mandado e, se houver resistencia, forca policial **fundamentada**.
5. Lembrar que embargos ou recurso do executado nao desfazem a arrematacao (CPC 903, caput) — resolvem-se em perdas e danos.
6. **Nunca** orientar autotutela (PA-08). Revisao R1-R4 antes de entregar.

**Skill a acionar:** `imissao-na-posse-arrematante`.
