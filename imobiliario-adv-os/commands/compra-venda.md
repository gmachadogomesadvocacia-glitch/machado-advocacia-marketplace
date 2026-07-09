---
description: Compra e venda / promessa de compra e venda / arras / distrato (Lei 13.786/2018) / vicios redibitorios e eviccao.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao do caso]
---

Voce foi acionado pelo comando `/compra-venda` do plugin imobiliario-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** estruturar a demanda de compra e venda imobiliaria (promessa, arras, distrato, vicios), conforme o polo do cliente.

## PROTOCOLO
1. **Conferir a triagem** — `CASO.md` com o contrato (promessa/escritura), o polo (comprador x vendedor — PA-10), o objeto (matricula/area), o estagio de pagamento e os prazos.
2. **Qualificar a demanda** — execucao de promessa, rescisao/resolucao por inadimplemento, distrato, devolucao de valores, arras (confirmatorias x penitenciais — CC art. 417-420), vicios redibitorios (CC art. 441-446) ou eviccao (CC art. 447-457).
3. **Distrato e Lei 13.786/2018** — quando aplicavel a incorporacao/loteamento, aplicar o regime de retencao e devolucao do distrato. **Atencao a interface:** se a relacao for de consumo (imovel na planta, incorporadora x adquirente), rotear ao plugin `consumidor-adv-os`; esta frente cobre o negocio entre particulares.
4. **Norma vigente no contrato** (PA-04) — aplicar a lei do tempo do contrato/fato, nao a superveniente. Nao confundir posse x propriedade x dominio (PA-05).
5. **Travas** — jurisprudencia validada (PA-01); coerencia de polo (PA-10). Se o pedido for de outorga de escritura/registro recusado, considerar a adjudicacao compulsoria (`/due-diligence` ou skill propria).
6. **Acionar a skill `compra-venda-promessa-distrato`** para redigir a peca escolhida.
7. Ao final, submeter a `revisao-final-imobiliaria` (R1-R4).

**Skill a acionar:** `compra-venda-promessa-distrato`.
