---
description: Acionamento direto da triagem de Recuperacao Judicial — polo, classe do credito, fato gerador (concursal x extraconcursal), via e MODO CTH. Porta de entrada.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao do caso]
---

Voce foi acionado pelo comando `/triagem` do plugin recuperacao-judicial-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** enquadrar o caso e gravar o diagnostico no `CASO.md`.

## PROTOCOLO

1. **Acionar `rj-master`** brevemente (configuracao + governanca + deteccao de MODO CTH).
2. **Acionar a skill `triagem-rj`** — classifica:
   - **Polo:** credor · credor-trabalhista · devedor-recuperando · administrador judicial
   - **Classe do credito:** I (trabalhista, ate 150 SM) · II (garantia real) · III (quirografario) · IV (ME/EPP)
   - **Fato gerador:** concursal (anterior ao pedido) x extraconcursal (art. 84)
   - **Via:** divergencia (art. 7 §1) · impugnacao (art. 8) · retardataria (art. 10) · reserva (art. 6 §2)
   - **Fase:** pre-RJ · stay period · QGC · AGC · cumprimento do plano · falencia
3. **Gravar** no `CASO.md` (abrir caso novo se necessario).
4. Se polo = credor trabalhista → rotear para `credor-trabalhista-rj`.

**Skill a acionar:** `triagem-rj`.
