---
name: defesa-radar-equipamentos
description: >
  Skill Tier 2 — defesa especifica de multas por EQUIPAMENTO MEDIDOR DE VELOCIDADE (radar) e afins, a categoria de maior volume. Ative em multa de radar, excesso de velocidade, lombada eletronica, aferição do equipamento, margem de tolerancia ou fiscalizacao eletronica.
metadata:
  version: "0.1.0"
  area: "Direito de Transito"
  tier: 2
---

# DEFESA DE RADAR E EQUIPAMENTOS MEDIDORES

> Tier 2. O **maior volume** de autuacoes. Defesa tecnica focada na validade do equipamento e do registro. Alimenta defesa previa, JARI, CETRAN, anulatoria e MS. Persona: {{ADVOGADO_NOME}} ({{OAB_UF}} {{OAB_NUMERO}}), {{FIRM_NAME}}. Tom: {{TOM_VOZ_PERFIL}} / {{TOM_VOZ_INTENSIDADE}}.

---

## 1. CATALOGO DE TESES

**A. Aferição / verificacao (nucleo)** — todo instrumento de medicao deve ter **verificacao metrologica** do **INMETRO** (ou IPEM delegado) **valida na data da autuacao**. Exigir a **certidao de aferição/verificacao** correspondente ao equipamento (nº de serie) e ao periodo. Ausencia, vencimento ou divergencia de nº de serie → **nulidade** (PA-04 — regra vigente na infracao; validar Resolucoes CONTRAN/INMETRO aplicaveis, PA-02).

**B. Homologacao do modelo** — equipamento deve ser **homologado/aprovado** pelo INMETRO e autorizado pelo orgao de trânsito. Modelo nao homologado → invalida a medicao.

**C. Margem de tolerancia** — sobre a velocidade medida aplica-se a **margem/desconto** (em regra: ate 100 km/h, abate-se 7 km/h; acima, 7% — **validar** a Resolucao vigente, PA-02). Se a velocidade considerada nao descontou a margem, a faixa de penalidade pode estar errada → reenquadramento ou nulidade.

**D. Sinalizacao da fiscalizacao eletronica** — a via deve ter **sinalizacao de advertencia** da fiscalizacao por equipamento, conforme CONTRAN. Ausencia/inadequacao → nulidade (validar a resolucao de sinalizacao vigente).

**E. Registro/imagem** — foto ilegivel, sem placa visivel, sem data/hora/local, ou que nao identifica o veiculo → prova imprestavel.

**F. Regulamentacao da velocidade no local** — o limite deve estar **regulamentado e sinalizado** (placa R-19). Trecho sem regulamentacao valida → descabe a autuacao por excesso.

**G. Equipamento movel/estatico/fixo** — conferir as exigencias proprias de cada tipo (operador habilitado, posicionamento — validar normas).

## 2. COMO REQUERER A CERTIDAO DE AFERICAO

- Na **propria defesa/recurso**, requerer ao orgao autuador a juntada da **certidao de verificacao metrologica (INMETRO/IPEM)** do equipamento (nº de serie) **vigente na data da autuacao**, sob pena de nulidade por cerceamento de defesa.
- Subsidiariamente, requerer copia das imagens e do laudo de homologacao. O onus de comprovar a regularidade do equipamento e do orgao (inversao logica do ato administrativo).

## 3. ESTRUTURA DA DEFESA/RECURSO DE RADAR

1. **Enderecamento** — orgao autuador / JARI / CETRAN ou juizo, conforme a fase (PA-08).
2. **Identificacao** — nº AIT, placa, data/local, velocidade medida e considerada, equipamento (nº serie).
3. **Tempestividade** (PA-05).
4. **Preliminares / Nulidades** — aferição invalida, homologacao, sinalizacao, regulamentacao do local.
5. **Merito** — margem de tolerancia / reenquadramento; imagem imprestavel.
6. **Pedidos** — arquivamento/anulacao; subsidiariamente reenquadramento na faixa correta; juntada da certidao de aferição.
7. **Provas** — requerimento da certidao de aferição, imagens, laudo de homologacao, fotos da (ausente) sinalizacao.
8. Fecho, {{ADVOGADO_NOME}}, {{OAB_UF}} {{OAB_NUMERO}}.

## 4. INTEGRACAO

- `analise-vicios-auto-infracao` → integra o catalogo geral de nulidades.
- `analise-documental-transito` → conferir AIT, certidao de aferição, imagens.
- `jurisprudencia-transito` → validar Resolucoes CONTRAN/INMETRO e precedentes (PA-01/PA-02).
- `calculos-transito` → recalculo com margem de tolerancia, faixa de penalidade, pontos.
- Encaminha para a peca da fase: `defesa-autuacao`, `recursos-administrativos`, `anulatoria-transito`, `mandado-seguranca-transito`.
- `estilo-juridico-transito`; `revisao-final-transito` → R1-R4.

## 5. CHECKLIST DE SAIDA

- [ ] Certidao de aferição (INMETRO/IPEM) requerida; nº de serie e data conferidos
- [ ] Homologacao do modelo verificada
- [ ] Margem de tolerancia aplicada e faixa de penalidade conferida (validar Resolucao — PA-02)
- [ ] Sinalizacao da fiscalizacao e regulamentacao do local checadas
- [ ] Norma/Resolucao vigente na data da infracao (PA-04); nada inventado (PA-01/PA-02)
- [ ] Fatos/numeros ancorados no auto (PA-03); fase e enderecamento corretos (PA-08)
- [ ] Selo P1 feito · R1-R4 pendente
