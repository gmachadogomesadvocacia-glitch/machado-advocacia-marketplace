# isencao-ir-doenca-adv-os

Sistema operacional do advogado para **Isenção de IRPF por Doença Grave** (art. 6º, XIV, Lei 7.713/88), no padrão Adv-OS.

A isenção recai sobre os **proventos de aposentadoria, pensão e reforma** de portadores das doenças graves listadas — **não** sobre rendimento de trabalho ativo. Side-aware: contribuinte (autor) × Fazenda/fonte pagadora.

## Doenças cobertas (art. 6º, XIV — rol taxativo)
Neoplasia maligna (câncer) · cardiopatia grave · cegueira · doença de Parkinson · esclerose múltipla · nefropatia/hepatopatia grave · AIDS · hanseníase · paralisia irreversível · tuberculose ativa · alienação mental · espondiloartrose anquilosante · fibrose cística · doença de Paget · contaminação por radiação.

## Teses-âncora
- **Súmula 598 STJ** — desnecessário laudo médico oficial no judicial; doença provável por outros meios.
- **Súmula 627 STJ** — isenção mantida mesmo em remissão / sem contemporaneidade dos sintomas.
- **Restituição dos últimos 5 anos** (CTN art. 168). Isenção só sobre **proventos** (não ativo).

## Vias
- **Administrativa** — requerimento à fonte pagadora (INSS/RPPS/fundo) + retificação da DIRPF na Receita.
- **Judicial** — declaratória de isenção + repetição de indébito (5 anos) + tutela para cessar a retenção.

## Commands (10)
`/isencao-ir-master` · `/triagem` · `/start-isencao-ir` · `/status-isencao-ir` · `/caso-isencao-ir` · `/revisao-final` · `/requerimento` · `/acao-judicial` · `/mandado-seguranca` · `/calculos`

## Primeiro uso
1. `/start-isencao-ir` — configura o escritório (gera `isencao-ir/persona.md`, `casos/`).
2. `/triagem` — verifica os 4 requisitos e abre o `CASO.md`.
3. Produza pela via (administrativa ou judicial); tudo passa pela `revisao-final-isencao-ir`.

## ⚠️ Privacidade reforçada
Lida com **dado de saúde** (sensível — LGPD art. 11 + sigilo). Laudo/CID/diagnóstico ficam só na pasta local do caso (gitignored). Nunca opinar sobre conduta clínica — o laudo é do médico.

---
Uso interno — Machado Advocacia. Saída padrão em `.txt`.
