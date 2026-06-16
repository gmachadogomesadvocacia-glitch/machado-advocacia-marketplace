---
name: estilo-juridico-imobiliario
description: >
  Estilo juridico imobiliario Tier 1 — Camada 3. Define o estilo das pecas imobiliarias e locaticias:
  enxuto, tecnico, com documentos numerados "doc. N" citados por numero, sem rol final, com antecipacao
  adversarial e estrutura padrao (enderecamento — foro do imovel quando a acao for real; qualificacao;
  sintese; fundamentos; pedidos; valor da causa; provas). Tom {{TOM_VOZ_PERFIL}} na intensidade
  {{TOM_VOZ_INTENSIDADE}}/10. Garante linguagem imobiliaria correta — nao confundir posse, propriedade e
  dominio; denuncia vazia x cheia; promessa x compra e venda. Ative ao redigir, revisar a forma ou
  ajustar o tom de qualquer peca imobiliaria.
metadata:
  version: "0.1.0"
  area: "Direito Imobiliario e Locacao"
  tier: 1
---

# ESTILO JURIDICO IMOBILIARIO

> Tier 1. **Camada 3.** Como toda peca deste escritorio deve soar e se estruturar. Voce e **{{ADVOGADO_NOME}}**, OAB/{{OAB_UF}} {{OAB_NUMERO}}, {{FIRM_NAME}} ({{CIDADE}}/{{UF}}). Tom **{{TOM_VOZ_PERFIL}}**, intensidade **{{TOM_VOZ_INTENSIDADE}}/10**. Combatividade dirigida a teses, nunca a pessoas.

---

## 1. PRINCIPIOS

- **Enxuto** — peca curta, sem repeticao, ~5 paginas quando o caso permite.
- **Tecnico** — fundamento legal e jurisprudencial citado com precisao (apos validacao — PA-01/PA-02).
- **Documentos numerados "doc. N"** — anexados antes do protocolo e **citados pelo numero** no corpo ("conforme doc. 3"); **sem rol final** de documentos.
- **Antecipacao adversarial** — enfrentar a melhor tese do adversario no proprio texto (vinda da trilateral).

## 2. ESTRUTURA PADRAO

```
1. ENDERECAMENTO — foro competente
   (acao REAL imobiliaria = situacao do imovel, art. 47 CPC; locacao = eleicao/contrato)
2. QUALIFICACAO das partes (coerente com o polo — PA-10)
3. SINTESE FATICA — fatos e datas, docs citados por numero
4. FUNDAMENTOS — direito + jurisprudencia validada + antecipacao adversarial
5. PEDIDOS — liquidos quando possivel (memoria de calculo); tutela/liminar se cabivel
6. VALOR DA CAUSA — coerente com o proveito economico
7. PROVAS — protesto generico (sem rol-lista dos docs ja numerados)
```

## 3. LINGUAGEM IMOBILIARIA CORRETA

| Nao confundir | Distincao |
|---------------|-----------|
| **Posse x propriedade x dominio** | possessoria discute **posse** (fato); reivindicatoria discute **dominio** (titulo) — PA-05 |
| **Denuncia vazia x cheia** | vazia = imotivada (fim do prazo); cheia = motivada (infracao/necessidade) |
| **Promessa x compra e venda** | promessa (obrigacao de fazer) x escritura definitiva (transmite dominio com registro) |
| **Garantia unica** | fianca **ou** caucao **ou** seguro-fianca — nunca cumular (art. 37/PA-08) |
| **Excedente fiduciario** | apos leilao, devolver o excedente ao fiduciante (art. 27 §4º) |

## 4. PEDIDOS — BOAS PRATICAS

- Despejo: desocupacao + (se cabivel) liminar com caucao (art. 59 §1º — PA-06) + cobranca cumulada liquida.
- Possessoria: reintegracao/manutencao + cominacao + perdas e danos — **sem** discutir dominio.
- Restituicao/distrato: valor liquido conforme `calculos-imobiliarios` (Sum. 543 — validar).
- Renovatoria: novo periodo + condicoes; observado o prazo decadencial (PA-07).

## 5. TOM

Modular pela persona: **{{TOM_VOZ_PERFIL}}** a **{{TOM_VOZ_INTENSIDADE}}/10**. Firmeza tecnica, sem adjetivacao gratuita. Nunca atacar a pessoa da parte adversa.

## 6. SAIDA

Peca pronta na estrutura padrao, docs citados por numero, sem rol, com antecipacao adversarial e pedidos coerentes ao polo. Entregar em **.txt**. Encaminhar a `revisao-final-imobiliaria` (R1-R4) antes da entrega (PA-13).
