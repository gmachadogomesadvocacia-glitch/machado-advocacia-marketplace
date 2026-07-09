---
description: Aciona a governanca central (Tier 0) do plugin imobiliario-adv-os.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [pergunta ou contexto opcional]
---

Voce foi acionado pelo comando `/imobiliario-master` do plugin imobiliario-adv-os.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** carregar a governanca de 4 Camadas, mostrar a configuracao ativa e rotear a demanda para a skill correta.

## PROTOCOLO
1. **Carregar estado** — procurar `imobiliario/cowork-state.json` subindo a arvore; ler `IMOB_PERSONA` (persona.md) e a config (frentes, polos, polo do cliente, tom). Se ausente, sugerir `/start-imobiliario`.
2. **Acionar a skill `imobiliario-master`** (Tier 0) — aplicar as 4 Camadas de Governanca, as 13 Proibicoes Absolutas e os Protocolos (Selo P1 — PA-11; Suprema Corte R1-R4 — PA-13; P4 cruzamento extrajudicial-judicial; P5 localizacao/foro/registro).
3. **Resumir a config ativa** — advogado/escritorio, polo do cliente (locador x locatario, comprador x vendedor, possuidor x esbulhador, condominio x condomino, fiduciante x credor fiduciario — PA-10) e frentes (locacao / contratos imobiliarios / direitos reais e posse / consultivo).
4. **Lembrar as travas centrais** — norma vigente no contrato/fato (PA-04); posse x propriedade x dominio (PA-05); liminar de despejo so art. 59 §1º + caucao (PA-06); prazo decadencial da renovatoria art. 51 §5º (PA-07); cumulacao de garantias vedada art. 37 (PA-08); rito da alienacao fiduciaria Lei 9.514/97 (PA-09).
5. **Rotear** — diante do `$ARGUMENTS`, indicar a porta de entrada (`/triagem`) ou a skill de producao adequada (despejo, renovatoria, possessoria, condominio, compra-venda, fiduciaria, due-diligence).
6. Nunca produzir peca sem passar pela triagem e, ao final, pela Revisao R1-R4.

**Skill a acionar:** `imobiliario-master`.
