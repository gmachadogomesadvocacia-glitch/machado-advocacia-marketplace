---
name: cruzamento-jt-rj
description: >
  CRUZAMENTO-JT-RJ — Protocolo Técnico P8 (transversal). Toda vez que
  houver crédito de origem trabalhista, cruza o caso do plug-in
  `recuperacao-judicial-adv-os` com o caso correspondente no plug-in
  `trabalhista-adv-os`: identifica o mesmo cliente, o mesmo processo
  trabalhista, o mesmo crédito; reaproveita memoria-de-caso-trabalhista;
  verifica reciprocamente o status (sentença, trânsito, liquidação, CH,
  execução suspensa); garante coerência entre o que está habilitado na
  RJ e o que está em curso na JT. Sem cruzamento, há risco de duplicidade,
  contradição estratégica e prejuízo ao crédito.
---

# CRUZAMENTO-JT-RJ — PROTOCOLO P8

> Transversal | Ponte recuperacao-judicial-adv-os ↔ trabalhista-adv-os
> Acionado sempre que houver origem trabalhista em caso de RJ

---

## 0. ESCOPO

Esta skill garante a **coerência entre dois universos processuais
paralelos** que afetam o mesmo crédito: o processo trabalhista (JT)
e o processo de recuperação judicial (juízo empresarial). Quando o
mesmo escritório atua nos dois, perdas de coerência são comuns:

  - Execução trabalhista prossegue indevidamente (violando o stay)
  - Crédito habilitado por valor diferente do liquidado na JT
  - CH expedida e não comunicada ao juízo da RJ
  - Acordo na JT que altera o crédito sem reflexo no QGC
  - Cessão de crédito que afeta a classe (art. 83 §4º)

O P8 elimina essas falhas.

---

## 1. QUANDO ACIONAR

Aciona-se automaticamente quando:

- O CASO.md de RJ tem polo "CREDOR TRABALHISTA".
- O CASO.md de RJ menciona um processo trabalhista nº [...].
- Existe pasta de caso correspondente no plug-in `trabalhista-adv-os`
  com o mesmo cliente ou o mesmo processo trabalhista.
- O usuário menciona ambos os mundos em uma mesma conversa.

---

## 2. DETECÇÃO

```
PASSO 1 — Verificar se trabalhista-adv-os está instalado
   Ler: C:/Users/gusta/.claude/plugins/installed_plugins.json
   Procurar chave: "trabalhista-adv-os@trabalhista-adv-os-marketplace"

PASSO 2 — Localizar a pasta do caso trabalhista
   Padrão: <cwd>/trabalhista/casos/<slug>/CASO.md
   Ou em qualquer subdiretório indicado pelo operador.

PASSO 3 — Casar pelo número do processo CNJ
   Comparar nº processo trabalhista do CASO.md de RJ com:
     - nº do processo trabalhista do CASO.md trabalhista
     - nome das partes (reclamante e reclamada)

PASSO 4 — Confirmar com o operador
   Antes de cruzar, perguntar:
   "Encontrei pasta de caso trabalhista correspondente em
    <caminho>. Confirma que é o mesmo caso?"
```

---

## 3. CAMPOS A CRUZAR

| Campo | No CASO.md RJ | No CASO.md trabalhista |
|-------|---------------|-----------------------|
| Cliente | nome do credor | nome do reclamante |
| Parte adversa | recuperanda | reclamada |
| Processo trabalhista | nº CNJ | nº CNJ |
| Fase atual | conhecimento/liquidação/execução | idem |
| Sentença | data + trânsito | data + trânsito |
| Acordo homologado | sim/não + valor | sim/não + valor |
| Liquidação | concluída? valor? | concluída? valor? |
| CH expedida | sim/não | sim/não |
| Valor histórico | R$ | R$ |
| Período (fato gerador) | início → fim | início → fim |
| Execução suspensa | sim/não | sim/não |
| Reserva no juízo RJ | sim/não + valor | n/a |
| Polo do cliente no caso trabalhista | (info) | reclamante / reclamada |

---

## 4. DIVERGÊNCIAS QUE DISPARAM ALERTA

```
[D1] Valor liquidado na JT diferente do valor habilitado na RJ
     → atualizar habilitação ou solicitar retificação do QGC

[D2] CH expedida pela JT, mas não juntada aos autos da RJ
     → providenciar juntada urgente; pleitear conversão da reserva
       em habilitação definitiva

[D3] Execução trabalhista não suspensa apesar do stay (art. 6º)
     → requerer suspensão no juízo da RJ + comunicar à JT

[D4] Acordo homologado na JT após o pedido de RJ
     → verificar se respeitou competência da JT para crédito anterior
     → verificar reflexo no plano

[D5] Cessão de crédito trabalhista
     → atenção ao art. 83 §4º LFRJ — classe pode rebaixar

[D6] Crédito habilitado na RJ E execução individual ainda em curso
     → risco de duplicidade — paralisar execução ou retirar habilitação

[D7] Cliente é reclamante na JT e CREDOR na RJ — coerência total
     Cliente é reclamada na JT e DEVEDORA na RJ — coerência total
     Outras combinações → REVISAR (pode haver conflito de interesses
     ou polo trocado)

[D8] Polo do escritório no plug-in trabalhista (reclamante/reclamada)
     deve casar com o polo no plug-in RJ (credor/devedora)
     → PA-23 (não atuar pelos dois lados no mesmo processo) — confirmar
```

---

## 5. AÇÕES PADRONIZADAS

### 5.1 Quando JT tem sentença sem liquidação

→ Aplicar art. 6º §2º (ver `credor-trabalhista-rj` §8.4):
   - Pedir RESERVA no juízo da RJ
   - Pedir prosseguimento da liquidação na JT (não suspende — art. 6º §2º)
   - Após CH → habilitar definitivamente

### 5.2 Quando JT tem CH expedida

→ Habilitação definitiva no juízo da RJ:
   - Anexar CH à habilitação/impugnação
   - Se reserva já constituída, requerer conversão da reserva no valor
     definitivo do crédito
   - Atualizar valor até a data do pedido de RJ (art. 9º, II)

### 5.3 Quando JT prossegue execução violando stay

→ Imediatamente:
   1. Petição ao juízo da RJ requerendo intimação da JT (art. 6º caput)
   2. Petição à JT noticiando o stay e requerendo suspensão
   3. Atualizar ambos os CASOs

### 5.4 Quando JT homologa acordo após pedido de RJ

→ Validar:
   - O acordo respeita a competência da RJ para crédito concursal?
   - O valor acordado vai a habilitação ou pagamento direto?
   - Atenção: acordo entre credor e recuperanda fora do plano pode
     ser nulo ou inoponível aos demais credores.

---

## 6. SAÍDA

```
[RELATÓRIO DE CRUZAMENTO P8]
Caso RJ: [...]
Caso trabalhista: [...]
Casamento: ✅ confirmado / ⚠️ a confirmar

Campos coerentes:
- [...]

Divergências detectadas:
- [D1 — ...] → ação: [...]
- [D2 — ...] → ação: [...]

Próximos passos:
1. [...]
2. [...]

Atualizações sugeridas em CASO.md (RJ):
- [...]
Atualizações sugeridas em CASO.md (trabalhista):
- [...]
```

---

## 7. PROIBIÇÕES

- **PA-P8-01**: Nunca cruzar sem confirmação do operador (LGPD + PA-22).
- **PA-P8-02**: Nunca habilitar sem checar o estado atual da JT.
- **PA-P8-03**: Nunca prosseguir se P8 detectar conflito de interesses
  (cliente em polos antagônicos nos dois plug-ins) — escalar ao operador.
- **PA-P8-04**: Nunca importar dados sensíveis do outro plug-in sem
  necessidade (LGPD — princípio da necessidade).

---

## 8. INTEGRAÇÃO COM A MEMÓRIA DO OPERADOR

O operador atual tem em memória:

  - [[trabalhista_plugin_install]] — plug-in trabalhista instalado
    em Downloads em 2026-05-26
  - [[direito_medico_plugin_install]] — outro plug-in jurídico
  - [[pjecalc_zip_fix]] — fix no gerador .PJC, relevante quando
    cálculo trabalhista for delegado ao PjeCalc
  - [[quezia_caso]] — caso trabalhista ativo

Sempre que P8 detectar referência a [[quezia_caso]] ou similar,
respeitar a memória persistente do operador e não duplicar trabalho.

---

## 9. POSIÇÃO NO PIPELINE

```
[credor-trabalhista-rj]
       ↓
  acionar [cruzamento-jt-rj]  ← P8
       ↓
  relatório + ajustes
       ↓
[via-processual-rj] e [calculo-credito-trabalhista-rj] (com dados
                                                          consolidados)
```
