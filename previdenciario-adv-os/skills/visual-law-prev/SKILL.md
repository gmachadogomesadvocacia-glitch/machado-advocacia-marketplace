---
name: visual-law-prev
description: >
  VISUAL LAW PREVIDENCIARIO — Skill Tier 2 F. Produz resumos visuais, cronogramas,
  timelines de beneficio, tabelas comparativas de regras de aposentadoria, diagramas
  de fluxo de processo previdenciario, e infograficos de calculo de RMI para uso
  em apresentacoes ao cliente, peticoes enriquecidas e material didatico. Usa ASCII/
  Markdown estruturado (sem dependencia de biblioteca grafica). Protocolo Camada 2
  (AIDA — Atencao/Interesse/Desejo/Acao). Acionar quando o usuario pedir um resumo
  visual, timeline, tabela comparativa, fluxograma, ou qualquer saida visualmente
  organizada sobre materia previdenciaria.
---

# VISUAL LAW PREVIDENCIARIO
> Tier 2 — Visual | ASCII/Markdown | AIDA | Timelines + Fluxos + Tabelas

---

## 0. PROTOCOLO CAMADA 2 — AIDA APLICADO AO VISUAL

```
A — Atencao: o visual deve capturar o ponto mais importante no topo (nao enterrar a tese)
I — Interesse: estrutura clara, categorias visuais, comparativos lado-a-lado
D — Desejo: demonstrar o beneficio financeiro ou o ganho de tempo da estrategia
A — Acao: terminar sempre com "O proximo passo e [X]" — nao deixar o cliente sem roteiro
```

---

## 1. TIMELINE DE PROCESSO PREVIDENCIARIO

```
Modelo ASCII — Timeline horizontal:

DER          45d         +30d          +60d         +180d         SENTENCA
 |            |            |             |              |              |
 ●────────────●────────────●─────────────●──────────────●──────────────●
 |            |            |             |              |              |
Protocolo   Prazo      Indeferimento  Recurso JR    Acao JEF      Concessao
 INSS        INSS          APS         (CRPS)       proposta      esperada
           (art.41-A)   (se negh.)   (30 dias)      (+pericia)

OBS: adaptar os marcos ao caso concreto — retirar as etapas nao aplicaveis
```

---

## 2. TABELA COMPARATIVA — REGRAS DE APOSENTADORIA EC 103

```
Modelo para apresentar ao cliente:

╔══════════════════════════╦══════════════════╦═══════════════╦══════════════╗
║ REGRA                    ║ REQUISITO        ║ PROVENTOS     ║ ELEGIVEL?    ║
╠══════════════════════════╬══════════════════╬═══════════════╬══════════════╣
║ Pontos Progressivos      ║ 102 pts (2026)   ║ 100% do SB    ║ [SIM/NAO]   ║
║ (transicao)              ║ 35 anos TC (H)   ║               ║             ║
╠══════════════════════════╬══════════════════╬═══════════════╬══════════════╣
║ Idade + Aliquota         ║ 65 anos + 15 TC  ║ 60%+2%/ano    ║ [SIM/NAO]   ║
║ (regra permanente)       ║ (H)              ║               ║             ║
╠══════════════════════════╬══════════════════╬═══════════════╬══════════════╣
║ Pedagio 50%              ║ Faltava < 2 anos ║ 100% do SB    ║ [SIM/NAO]   ║
║ (transicao rapida)       ║ em 13/11/2019    ║               ║             ║
╠══════════════════════════╬══════════════════╬═══════════════╬══════════════╣
║ Especial (B46)           ║ 25 anos (ruido)  ║ 100% do SB    ║ [SIM/NAO]   ║
║                          ║ 15/20 anos*      ║               ║             ║
╚══════════════════════════╩══════════════════╩═══════════════╩══════════════╝

MELHOR OPCAO PARA [NOME]: [indicar com seta ou asterisco]
VALOR ESTIMADO: R$ [X.XXX,00] / mes
```

---

## 3. DIAGRAMA DE FLUXO — DECISAO DE BENEFICIO

```
Modelo para explicar o caminho ao cliente:

                    SEGURADO TEM A DOCUMENTACAO?
                           |
               ┌───────────┴──────────┐
              SIM                    NAO
               |                      |
        REUNE OS REQUISITOS?     QUAL DOCUMENTO FALTA?
               |                      |
       ┌───────┴───────┐         [listar docs]
      SIM              NAO            |
       |                |        COMO OBTER?
   DER IMEDIATA    FALTA QUANTO?  [orientar]
   (protocolar     |
    agora)    ┌────┴────┐
              |         |
          < 1 ANO   > 1 ANO
              |         |
          PLANEJAR   VERIFICAR
          DER FUTURA  REVISAO
                     (outro beneficio?)
```

---

## 4. INFOGRAFICO DE CALCULO DE RMI

```
Modelo simplificado para o cliente:

┌─────────────────────────────────────────────────────────────────┐
│  COMO FOI CALCULADA SUA APOSENTADORIA?                          │
│                                                                 │
│  1. SEUS SALARIOS (PBC)                                         │
│     Media dos 100% dos salarios desde jul/1994                 │
│     = SALARIO DE BENEFICIO (SB): R$ [X.XXX,00]                 │
│                                                                 │
│  2. ALIQUOTA APLICADA                                           │
│     Tempo de contribuicao: [XX] anos                           │
│     Aliquota: [XX]% do SB                                      │
│                                                                 │
│  3. SUA RMI = SB × ALIQUOTA                                     │
│     R$ [X.XXX,00] × [XX]% = R$ [X.XXX,00]                      │
│                                                                 │
│  ⚠️ PODIA SER MAIOR? [SIM — pela Regra da Vida Toda: R$ X.XXX] │
│                     [NAO — este ja e o melhor calculo]          │
│                                                                 │
│  PROXIMO PASSO: [acao de revisao / manter o beneficio]          │
└─────────────────────────────────────────────────────────────────┘
```

---

## 5. CRONOGRAMA DE ACOMPANHAMENTO DO PROCESSO

```
Modelo para entregar ao cliente com o status do processo:

CASO: [NOME] — NB: [numero] / Processo: [numero]
SITUACAO: [fase atual]
ATUALIZADO EM: [data]

[✓] DER protocolada em [data]
[✓] Indeferimento recebido em [data] — fundamento: [X]
[✓] Recurso JR interposto em [data]
[ ] Aguardando decisao do CRPS (prazo medio: 60-90 dias)
[ ] Se mantido o indeferimento: acao JEF a ser proposta
[ ] Pericia judicial (prazo medio: 30-60 dias apos despacho)
[ ] Audiencia / sentenca

PROXIMA ACAO DO ESCRITORIO: [X]
PROXIMA ACAO NECESSARIA DO CLIENTE: [Y — ex: comparecer a pericia na data X]
ALERTA: [prazo critico se houver]
```

---

## 6. COMPARATIVO ANTES/DEPOIS (REVISAO DE RMI)

```
╔═══════════════════════════════╦═══════════════════╦═══════════════════╗
║                               ║ CALCULO INSS       ║ CALCULO REVISADO  ║
╠═══════════════════════════════╬═══════════════════╬═══════════════════╣
║ Regra aplicada                ║ [regra X]          ║ [regra Y]         ║
║ Salario de Beneficio          ║ R$ [X.XXX,00]      ║ R$ [X.XXX,00]     ║
║ Aliquota                      ║ [XX]%              ║ [XX]%             ║
║ RMI                           ║ R$ [X.XXX,00]      ║ R$ [X.XXX,00]     ║
╠═══════════════════════════════╬═══════════════════╬═══════════════════╣
║ DIFERENCA MENSAL              ║        ─           ║ + R$ [XXX,00]     ║
║ RETROATIVOS (5 anos)          ║        ─           ║ + R$ [XX.XXX,00]  ║
╚═══════════════════════════════╩═══════════════════╩═══════════════════╝

→ Vale a pena a acao de revisao? SIM — ganho estimado: R$ [XX.XXX,00]
→ Honorarios de exito ([XX]%): R$ [XX.XXX,00]
→ Ganho liquido estimado: R$ [XX.XXX,00]
```

---

## ALERTAS

```
⚠️ Sempre adaptar os modelos ao caso concreto — nao usar como template generico sem revisar
⚠️ Camada 2 AIDA: finalizar todo visual com o "proximo passo" para o cliente
⚠️ Valores estimados: indicar claramente que sao estimativas — PA-12 (nao simular sem dados)
⚠️ Timelines: usar marcos reais do processo — nao inventar prazos
```
