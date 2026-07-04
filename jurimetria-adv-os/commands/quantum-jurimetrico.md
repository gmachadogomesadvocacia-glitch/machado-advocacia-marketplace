---
description: Constroi a faixa de quantum de um tema pelo metodo bifasico (procedencia + valor entre procedentes), combinando acervo proprio e jurisprudencia. Sem promessa de resultado — saida e faixa descritiva carimbada.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: <tema/recorte>
---

Voce foi acionado pelo comando `/quantum-jurimetrico` do plugin jurimetria-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** a referencia interna de valor de um tema.

## PROTOCOLO

1. Confirmar tema e recorte (tribunal, epoca) — vago → `triagem-jurimetrica` antes.
2. **Acionar a skill `analise-quantum`**: fase 1 (procedencia no recorte) e fase 2 (distribuicao de valor entre procedentes), acervo + jurisprudencia, cada valor com origem.
3. Julgado citado sem conferencia → `[VERIFICAR]`; nunca inventar.
4. Lembrar a fronteira: faixa descritiva para decisao do advogado; NUNCA "provavel condenacao de R$ X" (PE-03). Numero que va a peca viaja com carimbo PE-13.
5. **Auditar com `revisao-final-jurimetria`** antes de entregar.

**Skill a acionar:** `analise-quantum`.
