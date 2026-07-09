---
name: via-processual-rj
description: >
  VIA-PROCESSUAL-RJ — Tier 1 (Insumo / Decisora). Acionada por `credor-trabalhista-rj` e `habilitacao-credito-rj` antes de qualquer redação.
---

# VIA-PROCESSUAL-RJ — DECISORA DE VIA

> Tier 1 | L11.101/2005 (arts. 6º §2º, 7º §1º, 8º, 10, 14) | Insumo puro

---

## 0. ESCOPO

Decisora pura. Recebe um conjunto de dados e devolve um VEREDITO
sobre a via correta. NÃO redige peça. NÃO atualiza CASO.md. Apenas
decide e devolve para a skill chamadora prosseguir.

---

## 1. ENTRADAS NECESSÁRIAS

```
1. data_pedido_rj           (data — marco do art. 9º, II)
2. fato_gerador_inicio      (data — primeiro dia do período)
3. fato_gerador_fim         (data — último dia do período/dano)
4. edital_art52_publicado   (sim/não + data, se sim)
5. relacao_aj_publicada     (sim/não + data, se sim) — art. 7º §2º
6. consta_na_relacao        (sim+correto / sim+erro / não)
7. valor_e_classe_relacao   (se consta: qual valor, qual classe)
8. qgc_homologado           (sim/não + data, se sim) — art. 14
9. liquidacao_jt_concluida  (sim/não)
10. ch_expedida             (sim/não) — certidão de crédito
11. tipo_credor             (trabalhista / quirografário / outro)
12. data_atual              (para cálculo de tempestividade)
```

Se faltar dado essencial → PARAR e pedir ao chamador.

---

## 2. ÁRVORE DE DECISÃO — PASSO A PASSO

### Passo A — Concursalidade

```
SE fato_gerador_fim < data_pedido_rj
    → CONCURSAL (puro) → ir para Passo B
SE fato_gerador_inicio > data_pedido_rj
    → EXTRACONCURSAL → VEREDITO E
SE fato_gerador a cavaleiro do pedido
    → CONCURSAL parcial + EXTRACONCURSAL parcial
    → segregar pro rata temporis → VEREDITO F
```

### Passo B — Liquidez

```
SE tipo_credor == trabalhista
   E liquidacao_jt_concluida == NÃO
   E ch_expedida == NÃO
    → VEREDITO V (Reserva art. 6º §2º — paralelo às demais vias)
    [observação: a reserva NÃO substitui a habilitação;
     ao final da liquidação, expedida a CH, retorna-se à árvore]
```

### Passo C — Via pelo estágio do processo de RJ

```
SE NÃO consta na relação E NÃO há relação do AJ publicada ainda:
    → habilitação direta perante o AJ
    → fundamento: art. 7º §1º (apresentação de habilitação)
    → endereçamento: ADMINISTRADOR JUDICIAL
    → prazo: 15 dias da publicação do edital do art. 52 §1º
    → forma: requerimento administrativo + documentos
    → VEREDITO I

SE relação do AJ JÁ publicada (art. 7º §2º) E QGC NÃO homologado:
    SE não consta:
        → IMPUGNAÇÃO judicial — pleiteia INCLUSÃO
        → fundamento: art. 8º
        → endereçamento: JUÍZO DA RJ (autos em apartado)
        → prazo: 10 dias da publicação da relação consolidada
        → VEREDITO III-A
    SE consta com erro (valor ou classe):
        → IMPUGNAÇÃO judicial — pleiteia RETIFICAÇÃO
        → mesmo regime do art. 8º
        → VEREDITO III-B

SE QGC já homologado (art. 14):
    SE crédito não está no QGC:
        → HABILITAÇÃO RETARDATÁRIA
        → fundamento: art. 10
        → endereçamento: JUÍZO DA RJ (ação autônoma)
        → custas pelo credor (art. 10, §3º)
        → SEM direito a voto na AGC (art. 10, §1º)
        → VEREDITO IV
    SE crédito está no QGC mas com erro:
        → ação revocatória do art. 19 (ou rescisão do julgado, se
          o QGC foi homologado por sentença com trânsito)
        → VEREDITO IV-bis (raro; sinalizar)
```

### Passo D — Tempestividade

```
data_atual − data_publicacao_edital  ≤ 15 dias  → divergência cabe
data_atual − data_publicacao_relacao ≤ 10 dias  → impugnação cabe
                                  caso contrário → retardatária

⚠️ Atenção a prazos em dobro (Fazenda Pública — art. 183 CPC),
   eventual suspensão de prazos por feriado forense e por decisão
   do juízo da RJ.
```

---

## 3. VEREDITOS POSSÍVEIS

```
VEREDITO I   — DIVERGÊNCIA / HABILITAÇÃO administrativa
               (art. 7º §1º — perante AJ — 15 dias do edital)

VEREDITO III-A — IMPUGNAÇÃO judicial — pleito de inclusão
                 (art. 8º — perante juízo — 10 dias)

VEREDITO III-B — IMPUGNAÇÃO judicial — pleito de retificação
                 (art. 8º — perante juízo — 10 dias)

VEREDITO IV  — HABILITAÇÃO RETARDATÁRIA
               (art. 10 — ação autônoma — sem voto na AGC)

VEREDITO IV-bis — Caso excepcional pós-QGC homologado com erro
                  (raro; sinalizar e remeter ao juízo da RJ)

VEREDITO V   — RESERVA art. 6º §2º
               (paralela; aguardar liquidação na JT e CH)

VEREDITO E   — EXTRACONCURSAL — NÃO HABILITA
               (cobra no curso normal; art. 84 se convolar)

VEREDITO F   — CRÉDITO CINDIDO
               (segregar pro rata; aplicar via concursal à parcela
                anterior e regime extraconcursal à parcela posterior)
```

---

## 4. FORMATO DE SAÍDA

Sempre devolver à skill chamadora:

```
VEREDITO: [código + nome]
FUNDAMENTO LEGAL: [artigos da LFRJ]
ENDEREÇAMENTO: [AJ / Juízo da RJ]
PRAZO: [...]
TEMPESTIVIDADE NO CASO: [tempestiva / intempestiva / dúvida]
ALERTAS DISPARADOS: [lista]
PRÓXIMA SKILL RECOMENDADA: [credor-trabalhista-rj seção X /
                            habilitacao-credito-rj §A/§B/§C/§D]
```

---

## 5. ALERTAS PADRONIZADOS

- Se tempestividade é "limítrofe" (faltam ≤ 2 dias) → alerta de URGÊNCIA.
- Se retardatária → alerta crítico A13 (sem voto na AGC).
- Se reserva (art. 6º §2º) → alerta A9 + protocolar requerimento de
  reserva no juízo da RJ E pedir CH na JT.
- Se extraconcursal → alerta de NÃO habilitar (PA-15).
- Se crédito cindido → alerta de cálculo pro rata temporis.

---

## 6. EXEMPLOS DE USO

### Exemplo 1 — Credor trabalhista típico, dentro do prazo do edital

Entrada: fato gerador 2020–2024; pedido de RJ em 2025-01-10;
edital do art. 52 §1º publicado em 2025-02-15; data atual
2025-02-20; credor não consta; liquidação ainda na JT.

Saída:
```
VEREDITO: I (divergência/habilitação administrativa) + V (reserva)
FUNDAMENTO: art. 7º §1º + art. 6º §2º
ENDEREÇAMENTO: Administrador Judicial + juízo da RJ (reserva)
PRAZO: 15 dias do edital → vence em 2025-03-02
TEMPESTIVIDADE: tempestiva (5 dias decorridos)
ALERTAS: A1, A2, A3, A5, A9, A14
PRÓXIMA SKILL: credor-trabalhista-rj §8.1 + §8.4
```

### Exemplo 2 — Credor consta com classe errada, após relação do AJ

Entrada: relação do AJ publicada em 2025-03-10; credor consta
como Classe III no valor de R$ 100.000; deveria ser Classe I
até 150 SM + Classe III no excedente.

Saída:
```
VEREDITO: III-B (impugnação judicial — retificação)
FUNDAMENTO: art. 8º + art. 83, I
ENDEREÇAMENTO: juízo da RJ, em apartado
PRAZO: 10 dias da publicação → vence em 2025-03-20
TEMPESTIVIDADE: verificar data atual
ALERTAS: A1, A4, A5, A6, A8
PRÓXIMA SKILL: credor-trabalhista-rj §8.2
```

### Exemplo 3 — QGC já homologado

Entrada: QGC homologado em 2024-11-15; credor descobriu o
crédito agora; sentença trabalhista de 2023.

Saída:
```
VEREDITO: IV (habilitação retardatária)
FUNDAMENTO: art. 10
ENDEREÇAMENTO: juízo da RJ, ação autônoma
PRAZO: enquanto não encerrada a RJ (regra geral)
ALERTAS CRÍTICOS: A13 (SEM VOTO NA AGC), A18 (prescrição)
PRÓXIMA SKILL: credor-trabalhista-rj §5-BIS (prescrição) + §8.3
```

---

## 7. INTEGRAÇÃO

- Chamada por: `credor-trabalhista-rj`, `habilitacao-credito-rj`.
- Antecede a redação. Sempre.
- Após o veredito, atualizar `memoria-de-caso-rj` com a via decidida.
