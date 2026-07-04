# Bloco jurimetrico do CASO.md (schema)

Bloco padronizado a incluir em cada `CASO.md` do acervo. E a **fonte do que o DataJud NAO da**
(quantum, desfecho, tese) + a **chave de ligacao** (numero do processo) que o `datajud_client.py`
usa para puxar duracao e andamentos. O leitor `ler_caso.py` extrai este bloco automaticamente.

## Regras
- Delimitado por `<!-- jurimetria:inicio -->` e `<!-- jurimetria:fim -->` (o leitor le so o miolo).
- Formato `chave: valor` (uma por linha). Vazio/`null` = ainda nao preenchido — **nunca inventar** (PE-12).
- `numero_processo` e **publico** (registro processual); o **nome do cliente NAO entra aqui** —
  fica no corpo do CASO.md. Agregados que saiam do acervo passam pelo scanner de sigilo (LGPD, PE-06).
- Preencher **identificacao + classificacao + caso** ao abrir; **desfecho** ao encerrar.

## Bloco (copiar para o CASO.md)

```
<!-- jurimetria:inicio -->
numero_processo: 0000000-00.0000.0.00.0000
tribunal:            # TJRJ | TRT1 | TRF2 | STJ | ...
sistema:             # eproc | PJe | fisico
grau:                # G1 | G2
area:                # trabalhista | consumidor | previdenciario | civel | tributario | ...
classe_cnj:          # ex.: Acao Trabalhista - Rito Ordinario
assunto_cnj:         # ex.: Rescisao Indireta
comarca:             # ex.: Campos dos Goytacazes
orgao_julgador:      # ex.: 1a Vara do Trabalho de ...
polo_cliente:        # autor | reu
tese_principal:      # frase curta da tese-ancora
valor_da_causa:      # numero, ex.: 50000.00
data_ajuizamento:    # AAAA-MM-DD
status: em_andamento # em_andamento | sentenca | acordo | transitado | extinto | arquivado
resultado:           # procedente | parcial | improcedente | acordo | extinto (preencher ao fechar)
quantum_pretendido:  # numero
quantum_obtido:      # numero (o que o cliente efetivamente obteve)
percentual_exito:    # numero 0..1 (obtido/pretendido) — o leitor pode calcular
forma_encerramento:  # sentenca | acordo | desistencia | ...
data_encerramento:   # AAAA-MM-DD
datajud_sync:        # AAAA-MM-DD (ultima sincronizacao de andamentos) — preenchido pela ferramenta
obs_jurimetria:      #
<!-- jurimetria:fim -->
```

## Para que serve cada grupo
- **Identificacao** (`numero_processo`, `tribunal`, `sistema`, `grau`) — liga ao DataJud (Modulo A:
  duracao e andamentos vem de la, nao precisam ser digitados).
- **Classificacao** (`area`, `classe_cnj`, `assunto_cnj`, `comarca`, `orgao_julgador`) — agrupa casos
  semelhantes para o **benchmark** (Modulo B: seus casos vs. o tribunal — harmonizacao PE-09).
- **Caso** (`polo_cliente`, `tese_principal`, `valor_da_causa`, `data_ajuizamento`) — contexto.
- **Desfecho** (`status`, `resultado`, `quantum_*`, `percentual_exito`, `forma_encerramento`) — o
  **quantum e a taxa de exito do portfolio** (Modulo C), que o DataJud nao fornece.
