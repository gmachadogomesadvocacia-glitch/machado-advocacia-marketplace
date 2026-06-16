# PREVIDENCIARIO ADV OS

Plugin Claude Cowork especializado em **Direito Previdenciario Brasileiro** para advogados previdenciaristas.

## Visão Geral

**26 skills** organizadas em hierarquia de 4 camadas com governança técnica para análise, cálculo, redação e planejamento previdenciário — RGPS, RPPS, Previdência Complementar e Consultivo Empresarial.

## Como Começar

Use `/start-previdenciario` para o wizard de onboarding completo (6 blocos de coleta + ficha de caso + roteamento automático).

## Arquitetura

```
Tier 0: previdenciario-master (22 PAs + 4 camadas de governança)
Tier 1: Estado-Maior (triagem → análise → jurisprudência → estratégia)
Tier 2: 19 skills especializadas (contencioso / administrativo / cálculos / regimes)
Tier 3: Suprema Corte R1-R4 (quality gate automático)
Transversais: estilo-jurídico + visual-law
Engine: onboarding wizard
```

## Comandos Rápidos

| Comando | Função |
|---------|--------|
| `/start-previdenciario` | Onboarding — wizard completo |
| `/triagem` | Triagem dogmática de caso |
| `/calcular-rmi` | Cálculo RMI com auto-ataque |
| `/redigir-peticao` | Petição inicial JEF/JF |
| `/impugnar-laudo` | Impugnação a laudo pericial |
| `/revisar-rmi` | Revisão da Vida Toda (Tema 999) |
| `/planejar-pj` | Planejamento para sócio/PJ |
| `/consultivo-empresa` | Consultivo empresarial INSS |

## Governança

- **22 Proibições Absolutas (PAs)**: bloqueios técnicos para as falhas mais comuns em previdenciário
- **Suprema Corte R1-R4**: quality gate automático em toda resposta substantiva
- **LGPD**: dados sensíveis (CPF, NIT, CID, laudos) tratados com restrição PA-21
- **`--no-corte`**: bypass da Suprema Corte apenas para rascunhos

## Base Legal

Lei 8.213/91 · Lei 8.212/91 · Decreto 3.048/99 · EC 103/2019 · IN INSS 128/2022  
TNU Súmulas 6/25/47/57/63/83 · STF Temas 555/709/999 · LC 108/109/2001

---

*Plugin desenvolvido para uso por advogados especializados em Direito Previdenciário Brasileiro.*
