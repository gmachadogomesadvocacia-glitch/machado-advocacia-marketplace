---
name: linha-estrategica-isencao-ir
description: >
  LINHA ESTRATEGICA ISENCAO-IR — Skill Tier 1. Consolida a analise trilateral e a jurisprudencia e
  define: a VIA (administrativa x judicial x ambas em paralelo — Protocolo P4), o rito (JEF Federal ate
  60 SM x vara federal), se cabe tutela de urgencia (cessar a retencao) ou MS, o marco da isencao (data
  do laudo/inicio da doenca) e a extensao da restituicao (ultimos 5 anos — CTN 168). Respeita o
  modo_melhor_saida. Saida: linha estrategica para o advogado validar. Acione apos a trilateral, quando
  o usuario pede a estrategia, a melhor via, o caminho do caso, administrativo ou judicial, se cabe
  liminar.
metadata:
  version: "0.1.0"
  area: "Isencao de IRPF por Doenca Grave"
  tier: 1
---

# LINHA ESTRATEGICA ISENCAO-IR

> Skill **Tier 1** — consolida trilateral + jurisprudencia e define a **via, o rito, a tutela, o marco e a extensao da restituicao**. Saida e proposta para o advogado validar; respeita `{{MODO_MELHOR_SAIDA}}`.

---

## 0. PRE-REQUISITOS
- `analise-trilateral-isencao-ir` e `jurisprudencia-isencao-ir` concluidas; **Selo P1** em vista.
- Calculo do indebito (`calculos-isencao-ir`) disponivel ou pendente sinalizado.

## 1. A VIA (Protocolo P4)
- **Administrativa** — requerimento de isencao a fonte pagadora + retificacao da DIRPF na Receita. Mais rapida; **depende de laudo de servico medico oficial** (IN RFB 1500/2014). Boa quando o laudo oficial existe.
- **Judicial** — declaratoria de isencao + repeticao de indebito (5 anos) + tutela. **Sum. 598** dispensa laudo oficial; cabe quando ha recusa/silencio ou falta laudo oficial.
- **Ambas em paralelo (P4)** — administrativa primeiro; a **recusa/silencio vira prova** no judicial. Decidir conforme urgencia e existencia do laudo oficial.

## 2. O RITO
- Foro: **domicilio do contribuinte**, Justica Federal (Uniao/Fazenda Nacional + eventualmente a fonte).
- **JEF Federal** ate **60 SM** (Lei 10.259) x **vara federal** acima disso. O valor da causa (restituicao + parcelas) define o rito.

## 3. TUTELA / MS
- **Tutela de urgencia** (art. 300 CPC) para **cessar a retencao** mensal: probabilidade (laudo + rol) + perigo (desconto continuado).
- **Mandado de Seguranca** quando o direito for liquido e certo e a ilegalidade da retencao estiver documentada — avaliar contra a acao ordinaria (cabimento de restituicao por precatorio/RPV no MS).

## 4. MARCO E EXTENSAO
- **Marco da isencao**: data do laudo / **inicio da doenca** — define desde quando a retencao e indevida e os efeitos da declaratoria.
- **Extensao da restituicao**: **ultimos 5 anos** (CTN art. 168 — PA-09), so sobre **proventos** (PA-06). Competencias anteriores = prescritas.

## 5. SAIDA (respeita MODO_MELHOR_SAIDA)
```
LINHA ESTRATEGICA
- Via: [administrativa / judicial / ambas em paralelo] — justificativa
- Rito: [JEF ate 60 SM / vara federal] · Foro: [domicilio]
- Tutela/MS: [cabe? fundamento]
- Marco da isencao: [data] · Restituicao: [periodo de 5 anos / valor calculado]
- Riscos antecipados (Fazenda): [da trilateral]
- Proxima skill de producao: [acao / requerimento / MS / manutencao]
```
Em `recomendar-e-listar`: recomenda uma via e lista as alternativas. Em `apenas-listar`: so lista, sem recomendar.

## 6. ENCERRAMENTO
Entrega a linha estrategica para o **advogado validar** e roteia para a skill de producao da via escolhida. Toda peca produzida em seguida passa por `revisao-final-isencao-ir` (R1-R4).
