---
description: Desfaz o negocio: desistencia, invalidacao ou eviccao.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [caso]
---

Voce foi acionado pelo comando `/invalidacao` do plugin leiloes-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** sair do arremate ou reaver o que o cliente pagou.

## PROTOCOLO
1. Acionar `invalidacao-arrematacao`.
2. **Primeiro, o prazo:** ha onus real ou gravame nao mencionado no edital? Entao a via mais rapida e a **desistencia do art. 903, § 5º, I** — devolucao integral e imediata, provada em **10 dias**. Cravar a data-limite antes de qualquer outra coisa.
3. Nao cabendo desistencia, distinguir **invalidacao** (preco vil ou outro vicio), **ineficacia** (art. 804) e **resolucao** (preco nao pago) — art. 903, § 1º, I a III.
4. Perdido o bem para terceiro, ir a **eviccao**: CC 447 (subsiste em hasta publica), 450 (restituicao integral, frutos, despesas, custas e honorarios; preco pelo valor **ao tempo da eviccao**), 453 e 455. Conferir o art. 457 (quem sabia que a coisa era litigiosa) e registrar que **contra quem se volta o arrematante evicto nao tem tese consolidada** — questao aberta, a pesquisar no caso (PA-01).
5. **Limite etico:** nao inventar vicio para sair de mau negocio — art. 903, § 6º, pune com multa de ate 20%.
6. Comparar as vias com `linha-estrategica-leiloes`. Revisao R1-R4 antes de entregar.

**Skill a acionar:** `invalidacao-arrematacao`.
