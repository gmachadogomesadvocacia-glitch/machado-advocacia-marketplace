---
name: due-diligence-lote
description: >
  DUE DILIGENCE DO LOTE — skill FLAGSHIP Tier 2. Parecer de viabilidade PRE-LANCE com veredito ARREMATAR / NAO ARREMATAR / ARREMATAR COM RESSALVA e custo real de aquisicao. Acione sempre que o cliente perguntar se vale a pena dar lance num lote.
metadata:
  version: "0.1.0"
  area: "Leiloes e Arrematacao"
  tier: 2
---

# DUE DILIGENCE DO LOTE (FLAGSHIP)

> O produto central do plugin. Entrega **decisao**, nao ensaio. O cliente vai dar um lance com dinheiro proprio e precisa saber o que esta comprando, quanto vai pagar de verdade e o que pode dar errado.

**Pre-requisitos:** `triagem-leiloes` feita, Selo P1 emitido, edital e matricula em maos. Sem edital ou sem matricula atualizada, **nao se emite parecer** — entrega-se a lista do que falta.

---

## 1. OS SEIS EXAMES

### Exame 1 — O EDITAL
Ler inteiro, nunca o resumo do site do leiloeiro. Extrair: datas do 1º e 2º leiloes, **data de divulgacao** (decide a modulacao do Tema 1.134), preco minimo, comissao, forma de pagamento, condicoes especiais e, sobretudo:

> **O edital menciona onus, recurso ou processo pendente (CPC 886, VI)?**

Se **nao menciona** e a matricula acusa onus, isso e simultaneamente um **risco** e uma **protecao**: o art. 903, § 5º, I, garante desistencia com devolucao integral em 10 dias apos a arrematacao. Registrar como salvaguarda.

### Exame 2 — A MATRICULA E OS ONUS
Certidao atualizada. Listar **um a um**, nunca em bloco (PA-06): hipoteca (extingue-se — CC 1.499, VI), penhoras (sub-rogam-se no preco — CPC 908), usufruto, servidao, indisponibilidade, alienacao fiduciaria, penhoras de outros juizos, acoes reais. Para cada um: **sobrevive a arrematacao ou nao, e com que base**.

### Exame 3 — OS DEBITOS
- **Tributos**: sub-rogacao no preco (CTN 130, p.u.) + **Tema 1.134** — conferir a **data do edital** por causa da modulacao.
- **Condominio**: pedir declaracao de debito ao sindico. **Zona cinzenta** (CC 1.345 x CPC 908, § 1º; Tema 886 em revisao). Entra no parecer como **risco quantificado com ressalva**, nunca como isencao.
- Taxas, foro, laudemio, multas ambientais, IPTU parcelado.

### Exame 4 — A OCUPACAO (o risco mais subestimado)
Diligencia no local sempre que possivel. Quem esta dentro?

| Ocupante | Consequencia |
|----------|--------------|
| Desocupado | melhor cenario; confirmar com foto e data |
| Executado e familia | imissao na posse; prazo e resistencia variaveis |
| Locatario | **conferir os TRES requisitos do art. 8º da L8.245**: prazo determinado + clausula de vigencia + **averbacao na matricula**. Cumulativos. Faltando um, denuncia com 90 dias |
| Posseiro / invasor | acao propria, prazo imprevisivel |
| Usucapiente com acao em curso | **risco alto** — pode inviabilizar o negocio |
| Bem de familia | eleva o custo e o tempo da desocupacao |

Nunca afirmar desocupacao automatica (PA-09).

### Exame 5 — O PROCESSO DE ORIGEM
Ler os autos, nao so o edital. Ha embargos pendentes? O executado foi **regularmente intimado** (CPC 889)? Ha nulidade que possa derrubar a arrematacao depois? Ha recurso com efeito suspensivo? Penhora anterior de outro juizo? Na via fiduciaria: a **notificacao pessoal do devedor** e regular? Esse e o unico vicio que, pelo art. 30, paragrafo unico, da Lei 9.514, ainda obsta a reintegracao.

### Exame 6 — O CLIENTE
Ele pode arrematar (CPC 890 — inclusive a vedacao aos **advogados das partes**)? Tem o dinheiro no prazo do rito (**24 horas** no trabalhista)? Vai precisar do parcelamento do art. 895? Quer morar, revender ou alugar? A resposta muda o peso da ocupacao e do prazo.

---

## 2. O CUSTO REAL DE AQUISICAO

Nunca apresentar o lance como preco. Somar, via `calculos-leiloes`:

```
  lance pretendido
+ comissao do leiloeiro          (edital manda; faixa 5% x 3% — ver calculos-leiloes)
+ ITBI                           (aliquota do municipio)
+ custas, emolumentos e registro da carta
+ debitos que NAO sub-rogam ou cuja sub-rogacao e duvidosa (condominio)
+ custo estimado de desocupacao  (acao + tempo + eventual acordo)
+ reforma e regularizacao
+ carrego (IPTU e condominio ate a revenda)
= CUSTO REAL
```

Comparar com o valor de mercado **liquido**, nao com a avaliacao judicial. Declarar as premissas: o que e numero conferido em documento e o que e estimativa.

---

## 3. O VEREDITO

O parecer termina com **um** dos tres, em negrito, sem hedge:

- **ARREMATAR** — riscos mapeados, quantificados e aceitaveis; custo real com folga sobre o mercado.
- **ARREMATAR COM RESSALVA** — viavel **se** cumpridas condicoes objetivas, listadas uma a uma (teto de lance, reserva para condominio, confirmar averbacao da locacao, etc.).
- **NAO ARREMATAR** — ha risco que nao se resolve com dinheiro ou tempo (usucapiao em curso, nulidade grave na origem, ocupacao inviavel, custo real acima do mercado).

Cada risco recebe **probabilidade** (alta/media/baixa), **impacto em R$** quando quantificavel e **o que fazer com ele**.

---

## 4. VEDACOES ESPECIFICAS

- **PA-07**: nada de rentabilidade, "agio de X%", "lucro certo" ou percentual de exito. O parecer avalia **risco juridico**. Se o cliente pedir projecao de retorno, dizer que isso e decisao de investimento dele.
- **PA-02**: fato sem documento sai marcado `[sem lastro documental]`.
- **PA-01**: nada de Tema ou tese fora da curadoria.
- Prazo de validade: o parecer vale para **aquele edital e aquela data**. Adiado o leilao ou alterado o edital, refazer.

---

## 5. ESTRUTURA DE ENTREGA — O PARECER E PARA O CLIENTE

Os seis exames sao o **trabalho**. O parecer e o que o cliente **le para decidir**, e por
isso se escreve para ele: objetivo, enxuto, em linguagem que ele entende. Alvo de **1 a 2
paginas**.

1. **A RESPOSTA** — veredito em uma frase, no topo, seguido do porque em tres ou quatro
   linhas. O cliente nao pode ter de rolar o documento para saber se compra ou nao.
2. **O LOTE EM QUATRO LINHAS** — o que e, onde fica, quando e o leilao, qual o lance minimo.
3. **QUANTO CUSTA DE VERDADE** — tabela simples, total destacado, premissas em uma linha.
4. **O QUE PODE DAR ERRADO** — cada risco em **consequencia pratica**, com valor quando der
   para calcular e o que fazer a respeito. Nao em categoria juridica.
5. **O QUE FALTA SABER** — o que nao foi possivel conferir e se isso muda a resposta.
6. **O QUE VOCE PRECISA DECIDIR E PROVIDENCIAR** — fechamento acionavel.
7. **BASE LEGAL** — bloco final curto, so o que sustenta de fato. Fora do texto principal.

**Linguagem:** nada de propter rem, eviccao, sub-rogacao, adjudicacao, remicao ou preco vil
soltos. Se o termo for inevitavel, explicar entre parenteses na primeira vez e seguir com a
palavra comum. "Voce pode ficar com uma divida de condominio de R$ X", nao "risco de
responsabilidade propter rem".

**O que NAO muda:** a checagem na fonte, o veredito fechado, a ressalva honesta quando a
jurisprudencia e aberta e a vedacao de prometer resultado (PA-07). Muda a entrega, nao o
trabalho. Se o caso pedir, o detalhamento tecnico vai em **anexo separado**, nunca no corpo.

Estilo (`estilo-juridico-leiloes`), passada anti-rastro e **Revisao R1-R4** antes de entregar.
