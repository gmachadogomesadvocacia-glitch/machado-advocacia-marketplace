---
name: previdenciario-adv-os
description: >
  PREVIDENCIARIO ADV OS — Plugin maestro de Direito Previdenciario Brasileiro. Ativa
  automaticamente o sistema de 26 skills com 4 camadas de governanca, 22 Proibicoes
  Absolutas (PAs) e Suprema Corte R1-R4. Cobre RGPS (beneficios por incapacidade,
  aposentadorias, BPC/LOAS, acidentario), RPPS (servidores publicos), previdencia
  complementar (EFPC/EAPC), planejamento previdenciario para PJ/socio-empresario, e
  consultivo empresarial INSS (folha, FAP, eSocial). Acionar quando qualquer questao
  previdenciaria for identificada — o plugin roteia automaticamente para a skill correta.
---

# PREVIDENCIARIO ADV OS
> Plugin Maestro | 26 Skills | 4 Camadas de Governanca | 22 PAs | Suprema Corte R1-R4

---

## HIERARQUIA DE ATIVACAO

```
TIER 0: previdenciario-master (sempre ativo — PAs + governanca)
     ↓
TIER 1: Estado-Maior (SEMPRE antes de qualquer Tier 2)
  → triagem-dogmatica → analise-trilateral → jurisprudencia-estrategica → estrategia-de-caso
     ↓
TIER 2: Tenentes (skill especifica do caso)
  → [contencioso / administrativo / analise / calculos / regimes especiais / audiencia+docs]
     ↓
TIER 3: Suprema Corte (R1-R4 automatico ao final de cada resposta)
     ↓
TRANSVERSAIS: estilo-juridico-prev + visual-law-prev (em toda peca escrita)
     ↓
ENGINE: previdenciario-onboarding (/start-previdenciario)
```

---

## MAPA DE SKILLS

```
TIER 0 — Master
  previdenciario-master          → 22 PAs + 4 camadas + roteamento

TIER 1 — Estado-Maior (sempre antes de Tier 2)
  triagem-dogmatica              → B-code + competencia + carencia + qualidade segurado
  analise-trilateral             → Fato + Nexo + Direito + Baloney Detection
  jurisprudencia-estrategica     → STF/STJ/TNU/TRF com audit trail
  estrategia-de-caso             → admin vs judicial vs hibrido + timing + riscos

TIER 2A — Contencioso
  peticao-inicial-prev           → JEF/JF — FIRAC+AIDA — todas as especies
  replica-prev                   → resposta a contestacao INSS
  recursos-previdenciarios       → inominado JEF / apelacao / AI / TNU / REsp / RE / CRPS
  mandado-seguranca-prev         → MS + liminar + 120 dias

TIER 2B — Pos-sentenca
  cumprimento-sentenca-inss      → RPV / precatorio / calculo de atrasados
  acao-revisional-rmi            → Tema 999 STF + erros de calculo

TIER 2C — Administrativo + Analise
  administrativo-inss-crps       → JR / CaJ / requerimento / cessacao / prorrogacao
  analise-cnis                   → CNIS completo + gaps + inconsistencias + DER otima
  analise-ppp-ltcat-ap-especial  → Tema 555 STF + TNU 47/57/63/83 + aposentadoria especial
  pericia-medica-prev            → quesitos + laudo + CID + impugnacao + TNU Sumula 25
  analise-carta-concessao        → carta INSS + DIB/RMI/erros + pontos de impugnacao
  calculos-previdenciarios       → RMI + RMA + SB + Protocolo P5 + auto-ataque

TIER 2D — Audiencia + Documentos
  audiencia-previdenciaria       → JEF/JF + perito em audiencia + testemunhas + TRF/TNU
  documentos-extrajudiciais-prev → parecer + notificacao + contrato + procuracao

TIER 2E — Regimes Especiais
  rpps-servidor-publico          → EC 103 + contagem reciproca + abono permanencia
  previdencia-complementar       → EFPC (fundo de pensao) + EAPC (PGBL/VGBL)
  acidentario-do-trabalho        → CAT + NTEP + B91/B94 acidentario + art. 118

TIER 2F — Planejamento + Consultivo
  planejamento-prev-pj           → CI + MEI + pro-labore + otimizacao RMI
  consultivo-empresarial-prev    → folha + RAT/FAP + pejotizacao + autuacao fiscal

TIER 3 — Quality Gate
  suprema-corte-previdenciaria   → R1 PAs + R2 Fundamentacao + R3 Auto-critica + R4 Semaforo

TRANSVERSAIS
  estilo-juridico-prev           → EC 103 terminologia + citacoes + FIRAC+AIDA + FONAJEF
  visual-law-prev                → timelines + tabelas + fluxogramas + infograficos

ENGINE
  previdenciario-onboarding      → /start-previdenciario — wizard 6 blocos + ficha + roteamento
```

---

## COMANDOS DISPONÍVEIS

```
/start-previdenciario    → Onboarding: wizard 6 blocos — coleta dados e roteia
/triagem                 → Triagem dogmatica de um caso ja descrito
/calcular-rmi            → Calculo de RMI com auto-ataque (Protocolo P5)
/redigir-peticao         → Peticao inicial previdenciaria
/impugnar-laudo          → Impugnacao a laudo pericial desfavoravel
/revisar-rmi             → Revisao da Vida Toda + Tema 999 STF
/planejar-pj             → Planejamento previdenciario para socio/PJ
/consultivo-empresa      → Consultivo empresarial INSS (folha/FAP/autuacao)
```
