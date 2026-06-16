---
name: cumprimento-sentenca-inss
description: >
  CUMPRIMENTO DE SENTENCA INSS — Skill Tier 2 A. Produz peticao de cumprimento de sentenca
  condenatoria do INSS: calculo de parcelas atrasadas com correcao INPC + juros, pedido
  de RPV (Requisicao de Pequeno Valor) ou precatorio, requerimento de implantacao do
  beneficio, e impugnacao a calculo do INSS em fase de liquidacao. Acionar apos transito
  em julgado de sentenca condenatoria ou quando o INSS nao cumpre espontaneamente a
  obrigacao de fazer (implantar beneficio).
---

# CUMPRIMENTO DE SENTENCA INSS
> Tier 2 — Contencioso | Liquidacao + RPV/Precatorio | Implantacao

---

## 1. TIPOS DE CUMPRIMENTO

### 1.1 Obrigacao de Fazer (Implantar Beneficio)

```
Situacao: sentenca determinou a concessao do beneficio mas o INSS nao implantou
Prazo para o INSS implantar: normalmente fixado na sentenca (geralmente 30-60 dias)
Se nao implantou: peticao de cumprimento + multa por descumprimento (art. 536 CPC)

Peticao:
"Vem o Exequente informar que o prazo fixado na sentenca para implantacao do beneficio
transcorreu em [data] sem que o INSS providenciasse a implantacao.
Requer:
a) Intimacao do INSS para implantar o beneficio no prazo de [X] dias, sob pena de multa
   diaria de R$ [X] (art. 536, §1o, CPC);
b) Oficio ao INSS determinando a implantacao."
```

### 1.2 Obrigacao de Pagar (RPV ou Precatorio)

```
Valor ate 60 SM (2026): RPV — pagamento em ate 60 dias
Valor acima de 60 SM: Precatorio — pagamento no exercicio financeiro seguinte

Calculo das parcelas:
1. DIB correta (fixada na sentenca) ate a data do protocolo desta peticao
2. Valor mensal de cada competencia (verificar reajustes anuais do beneficio)
3. Correcao monetaria: INPC (mes a mes, desde o vencimento de cada parcela)
4. Juros de mora: conforme art. 1o-F da Lei 9.494/97 (verificar tese STJ vigente)
5. Honorarios advocaticios: percentual fixado na sentenca

Protocolo P5 obrigatorio: memorial de calculo auditavel com cada competencia discriminada.
```

### 1.3 Impugnacao ao Calculo do INSS

```
Situacao: o INSS apresentou calculo divergente do correto
Prazo: 15 dias para impugnar (art. 525 CPC)

Peticao:
"O calculo apresentado pelo INSS diverge do correto pelos seguintes motivos:
[1. Indice de correcao errado: usou IPCA quando devia ser INPC — fundamento: ...]
[2. DIB incorreta: usou [X] quando a sentenca fixou [Y]]
[3. Competencias omitidas: [lista]]
Requer a prevalencia do calculo do Exequente (Memorial juntado) e a intimacao do INSS
para complementar o pagamento no prazo de [X] dias."
```

---

## 2. MEMORIAL DE CALCULO (Protocolo P5)

```
## MEMORIAL DE CALCULO — [NOME] — [NB] — [DATA]

Periodo: [DIB fixada na sentenca] a [data desta peticao]
Beneficio: [BXX — descricao]
Valor inicial (RMI): R$ [X.XXX,XX] (conforme sentenca/calculo homologado)

| Competencia | Valor Nominal | Indice INPC | Valor Corrigido | Juros |
|-------------|--------------|-------------|-----------------|-------|
| [MM/AAAA] | R$ X.XXX,XX | [indice] | R$ X.XXX,XX | R$ XX,XX |
[...]

TOTAL PARCELAS: R$ [X.XXX.XXX,XX]
HONORARIOS ([X]%): R$ [XX.XXX,XX]
TOTAL GERAL: R$ [X.XXX.XXX,XX]

Modalidade: [RPV — valor ate 60 SM / Precatorio — valor acima de 60 SM]
```

---

## 3. ALERTAS

```
⚠️ Verificar se a sentenca ja transitou em julgado antes de protocolar cumprimento
⚠️ PA-15 (analogia): declarar competencia de referencia para cada indice de correcao
⚠️ Reajustes anuais do beneficio: incluir no calculo (verificar portaria ministerial de cada ano)
⚠️ Se INSS ja pagou parcialmente: subtrair do calculo para evitar duplicidade
⚠️ Prazo prescricional das parcelas: 5 anos (PA-12) — nao incluir competencias anteriores a 5 anos da acao
```
