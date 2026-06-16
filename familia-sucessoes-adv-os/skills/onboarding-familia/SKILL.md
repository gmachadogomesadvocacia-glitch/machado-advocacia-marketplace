---
name: onboarding-familia
description: >
  ONBOARDING-FAMILIA — Tier 1 (Insumos). Configura o escritório e o cliente no plugin de
  família e sucessões: cadastra dados do advogado ({{ADVOGADO_NOME}}, OAB/{{OAB_UF}} {{OAB_NUMERO}},
  {{FIRM_NAME}}), preferências de estilo, tom e fluxo de trabalho. Também realiza o
  onboarding do cliente novo: cadastro inicial de dados pessoais, do caso e expectativas.
  Acionar no início de cada novo caso para garantir que todos os dados essenciais estão
  registrados antes de iniciar qualquer trabalho processual.
metadata:
  version: "1.0.0"
---

# ONBOARDING-FAMILIA
> Tier 1 | Insumos | Cadastro do Escritório + Cliente | Primeira Sessão do Caso

---

## 0. ESCOPO

Esta skill garante que o plugin está configurado corretamente e que o novo caso
tem todos os dados essenciais antes de qualquer trabalho.

---

## 1. DADOS FIXOS DO ESCRITÓRIO

```
ESCRITÓRIO: {{FIRM_NAME}}
ADVOGADO: {{ADVOGADO_NOME}}
OAB: OAB/{{OAB_UF}} {{OAB_NUMERO}}
COMARCA PRINCIPAL: {{CIDADE}}/{{UF}}
VARA DE FAMÍLIA: Vara de Família — {{CIDADE}}/{{UF}}
TOM DEFAULT: 7/10 combativo (ajustar conforme o tipo de peça)
METODOLOGIA: FIRAC Família + 20 Proibições Absolutas
E-MAIL: {{EMAIL}}
```

---

## 2. ONBOARDING DO CLIENTE NOVO

Ao receber um novo cliente, coletar:

```
FICHA DO CLIENTE

DADOS PESSOAIS:
Nome completo: ___________________
Data de nascimento: _______________
CPF: _______________
RG: _______________
Profissão: _______________
Renda aproximada: R$ _______________
Endereço completo: ___________________
Telefone / WhatsApp: _______________
E-mail: _______________

ESTADO CIVIL E SITUAÇÃO FAMILIAR:
Estado civil atual: _______________
Data do casamento / início da união estável: _______________
Regime de bens (se casado/UE): _______________
Separado(a) de fato desde: _______________ (se aplicável)
Nome do cônjuge/companheiro(a): _______________
CPF do cônjuge/companheiro(a): _______________
Filhos: [ ] Sim  [ ] Não
  Filho 1: Nome _________ DN _________ Mora com: ___________
  Filho 2: Nome _________ DN _________ Mora com: ___________

TIPO DO CASO:
[ ] Divórcio / Separação
[ ] Guarda / Alimentos
[ ] União estável
[ ] Inventário / Arrolamento
[ ] Planejamento sucessório
[ ] Interdição / Curatela
[ ] Outro: _______________

OBJETIVO PRINCIPAL DO CLIENTE:
___________________

URGÊNCIAS IDENTIFICADAS:
[ ] Sim — qual: _______________ [ ] Não

COMO CHEGOU AO ESCRITÓRIO:
[ ] Indicação  [ ] Internet  [ ] Outro: _______________

HONORÁRIOS (uso interno):
Modalidade: [ ] Fixo  [ ] Êxito  [ ] Misto
Valor combinado: R$ _______________
Contrato assinado: [ ] Sim  [ ] Não
```

---

## 3. VERIFICAÇÃO DE CONFLITO DE INTERESSE

Antes de aceitar o caso:
```
□ O escritório já representa a outra parte neste ou em outro processo?
□ Há algum parente ou sócio do escritório que atue pelo lado contrário?
□ Há algum impedimento do advogado (art. 30 EOAB)?
```

Se houver conflito: declinar do caso e indicar outro advogado.

---

## 4. CONTRATO DE HONORÁRIOS

Elementos essenciais do contrato de honorários (art. 48 EOAB):
- Identificação das partes (advogado + cliente)
- Objeto do contrato (serviços prestados)
- Valor dos honorários e forma de pagamento
- Prazo e rescisão
- Foro competente ({{CIDADE}}/{{UF}})
- Assinatura com testemunhas ou reconhecimento em cartório

---

## 5. RAIZ DOS CASOS (CASE_ROOT) E PASTA UNIFICADA

Antes de abrir o caso, definir onde os casos serão salvos:

```
□ Perguntar: o escritório tem acervo configurado (pasta-mãe do escritório)?
   SIM → CASE_ROOT = <acervo>/Casos-Ativos   (Claude Code)
   NÃO → CASE_ROOT = <COWORK>/familia/casos   (FALLBACK)
□ Criar a raiz `<CASE_ROOT>/` (gitignored — sigilo + LGPD).
□ Gravar {{CASE_ROOT}} no state e renderizar na seção "Acervo e casos" do config.md.
```

A pasta de caso é **compartilhada entre os plugins Adv-OS**. Cada caso vive em
`<CASE_ROOT>/<slug>/` com `CASO.md`, `MEMORY.md`, `arquivos/` e `pecas/` (peças produzidas
em `<CASE_ROOT>/<slug>/pecas/`). O estado interno do plugin (`cowork-state.json`) **não**
muda de lugar — continua em `<COWORK>/familia/` (STATE_DIR `familia`).

---

## 6. CRIAÇÃO DO CASO.md

Após o onboarding, criar a pasta `<CASE_ROOT>/<slug>/` e o `CASO.md` (estrutura em
familia-master, Seção 6) e acionar **triagem-familia** para completar o enquadramento jurídico.

---

## 7. COMUNICAÇÃO COM O CLIENTE

Padrão de comunicação do escritório:
- Canal preferencial: WhatsApp ou e-mail
- Retorno em até 24h úteis
- Relatórios de andamento: mensais (ou conforme acordado)
- Protocolo de peças: informar o cliente com antecedência de 48h

---

## 8. LGPD — SIGILO E PROTEÇÃO DE DADOS

**PA-19**: Os dados do cliente são protegidos pela LGPD (L13.709/2018) e pelo dever
de sigilo profissional (art. 26 EOAB).

- Dados armazenados apenas pelo necessário
- Não compartilhar com terceiros sem autorização
- CASO.md: armazenar apenas em ambiente seguro do escritório
- Não mencionar dados de um caso para outro cliente
