---
name: onboarding-imobiliario
description: >
  Onboarding imobiliario Tier 1 — wizard de configuracao do escritorio e da persona no plugin de
  Direito Imobiliario e Locacao. Conduz o comando /start-imobiliario: coleta nome, OAB/UF/numero,
  firma, cidade/UF, email, tom de voz e intensidade, e as frentes de atuacao (locacao, contratos
  imobiliarios, direitos reais e posse, consultivo). Gera persona.md a partir do template e prepara o
  estado de caso (CASO.md). Aponta /start-imobiliario, /status-imobiliario e /caso-imobiliario. Ative
  na primeira utilizacao, ao configurar o escritorio, criar persona ou trocar dados do advogado.
metadata:
  version: "0.1.0"
  area: "Direito Imobiliario e Locacao"
  tier: 1
---

# ONBOARDING IMOBILIARIO

> Tier 1. Wizard de configuracao. Cria a **persona** do escritorio e prepara o estado de caso. Roda antes de qualquer producao quando a persona ainda nao existe.

---

## 1. COMANDOS

| Comando | Funcao |
|---------|--------|
| **/start-imobiliario** | Configura/atualiza o escritorio (este wizard) |
| **/status-imobiliario** | Mostra persona ativa, frentes e caso em curso |
| **/caso-imobiliario** | Abre/retoma o CASO.md (ver `memoria-de-caso-imobiliario`) |

## 2. DADOS COLETADOS

Pergunte um a um (ou aceite tudo de uma vez). Cada campo alimenta um token de persona:

| Campo | Token |
|-------|-------|
| Nome do advogado | `{{ADVOGADO_NOME}}` |
| UF da OAB | `{{OAB_UF}}` |
| Numero da OAB | `{{OAB_NUMERO}}` |
| Nome do escritorio | `{{FIRM_NAME}}` |
| Cidade de atuacao | `{{CIDADE}}` |
| UF de atuacao | `{{UF}}` |
| Email | `{{EMAIL}}` |
| Perfil de tom | `{{TOM_VOZ_PERFIL}}` |
| Intensidade do tom (0-10) | `{{TOM_VOZ_INTENSIDADE}}` |

**Frentes ativas** (uma ou mais):
- Locacao · Contratos imobiliarios · Direitos reais e posse · Consultivo.

> A UF importa para o foro (situacao do imovel — art. 47 CPC) e para o cartorio de registro. Confirme cidade/UF com atencao.

## 3. GERACAO DA PERSONA

1. Ler o template de persona do plugin.
2. Substituir os tokens pelos dados coletados.
3. Gravar `persona.md` na pasta de trabalho do operador (fora do plugin distribuido).
4. Nunca versionar a persona junto ao plugin publico (sigilo — PA-12).

## 4. PASTA UNIFICADA DE CASO (CASE_ROOT)

Pergunte se ha **acervo** do escritorio configurado e defina a raiz dos casos:

- **Code com acervo:** `CASE_ROOT = <acervo>/Casos-Ativos`.
- **Fallback** (Cowork ou sem acervo): `CASE_ROOT = <COWORK>/imobiliario/casos`.

Criar a pasta `CASE_ROOT` e gravar `{{CASE_ROOT}}` no `config.md`. Cada caso = `<CASE_ROOT>/<slug>/` (CASO.md, MEMORY.md, arquivos/, pecas/), **UNIFICADO e compartilhado** entre os plugins Adv-OS do mesmo cliente. O estado interno (`cowork-state.json`) NAO muda — fica em `<COWORK>/imobiliario/`.

## 5. ESTADO DE CASO

Apos a persona, preparar o `CASO.md` do primeiro caso em `<CASE_ROOT>/<slug>/` (delegar a `memoria-de-caso-imobiliario`, Protocolo P3). O CASO.md guarda partes, polo, imovel, contrato, prazos e documentos numerados; pecas em `<slug>/pecas/`. Pasta de caso gitignored.

## 6. SAIDA

```
PERSONA: {{ADVOGADO_NOME}} — OAB/{{OAB_UF}} {{OAB_NUMERO}} — {{FIRM_NAME}} ({{CIDADE}}/{{UF}})
TOM: {{TOM_VOZ_PERFIL}} / {{TOM_VOZ_INTENSIDADE}}
FRENTES: ...
PROXIMO: /caso-imobiliario para abrir o primeiro caso
```

> Ao concluir, oriente o operador a rodar a triagem (`triagem-imobiliaria`) no primeiro caso. Sem persona, nenhuma peca e produzida.
