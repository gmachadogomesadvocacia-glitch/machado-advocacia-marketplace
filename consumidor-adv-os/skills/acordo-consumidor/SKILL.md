---
name: acordo-consumidor
description: >
  ACORDO CONSUMIDOR — Skill Tier 2 transversal e side-aware. Redige a transacao/conciliacao judicial
  ou extrajudicial em materia de consumo: minuta de termo de acordo com clausulas essenciais (objeto,
  valor/forma de pagamento, quitacao, obrigacoes de fazer, multa por descumprimento, confidencialidade),
  homologacao judicial como titulo executivo, acordo em audiencia (JEC/conciliacao) e, no
  superendividamento, o plano de pagamento. Calibra teor e tom conforme o polo (consumidor x fornecedor)
  e alerta os riscos de renuncia e de quitacao ampla. Acione quando o usuario pede acordo, transacao,
  conciliacao, minuta de termo, proposta de acordo, homologacao, fechar com a outra parte. Exige Selo
  P1 emitido.
metadata:
  version: "0.1.0"
  area: "Direito do Consumidor e Bancario"
  tier: 2
---

# ACORDO CONSUMIDOR

> Skill **Tier 2** transversal. Produz a minuta de transacao judicial/extrajudicial. **Side-aware:** as clausulas e o tom **flipam** conforme o polo — protetivo e cauteloso pelo consumidor; abrangente e blindado pelo fornecedor (sem jamais atacar o polo do cliente, PA-05). So roda apos a triagem e o Selo P1.

---

## 0. PRE-REQUISITOS

- Polo do cliente travado (PA-05). **Selo de Validacao Legal Previa EMITIDO** (P1).
- CASO.md com partes, objeto do litigio, valores e fase (extrajudicial / judicial / audiencia / superendividamento). Falta de dado essencial → `[INFORMAR]` (PA-15).

## 1. MODALIDADES

- **Extrajudicial:** termo firmado entre as partes; pode ser levado a homologacao para virar titulo executivo judicial (CPC art. 515, III; escritura/instrumento como titulo extrajudicial).
- **Judicial:** acordo nos autos, **homologado por sentenca** → titulo executivo judicial; extingue o processo com resolucao de merito.
- **Em audiencia (JEC / conciliacao):** acordo lavrado em ata e homologado no ato — via mais comum no consumo (integra `peticao-jec`).
- **No superendividamento:** o plano de pagamento global do art. 104-A e a forma do acordo — coordenar com `acao-superendividamento` (minimo existencial preservado, PA-14).

## 2. CLAUSULAS ESSENCIAIS DA MINUTA

1. **Qualificacao das partes** e referencia ao processo/litigio.
2. **Objeto** — exatamente o que se transaciona (debito, vicio, negativacao, dano).
3. **Valor e forma de pagamento** — montante, parcelas, vencimentos, meio, indice de correcao; consequencia do inadimplemento.
4. **Obrigacoes de fazer/nao fazer** — baixa da negativacao em prazo certo, religacao, troca/reparo, cancelamento de cobranca, abstencao de nova cobranca.
5. **Quitacao** — delimitar o alcance. **Cuidado com a quitacao ampla, geral e irrestrita** (ver § 4).
6. **Multa por descumprimento** — clausula penal liquida por evento/atraso, com gatilho objetivo.
7. **Confidencialidade** — quando do interesse das partes; calibrar conforme o polo.
8. **Foro e custas/honorarios** — divisao e eventual renuncia reciproca.

## 3. CALIBRACAO POR POLO (side-aware)

| Clausula | Pelo **consumidor** | Pelo **fornecedor** |
|----------|---------------------|---------------------|
| Quitacao | **restrita ao objeto**; ressalvar danos futuros/desconhecidos | ampla sobre o objeto, fechando o litigio |
| Obrigacoes de fazer | prazos curtos + multa robusta a favor | prazos exequiveis, multa proporcional |
| Confidencialidade | so se houver contrapartida | proteger imagem/precedente |
| Pagamento | garantias, vencimento antecipado a favor | parcelamento, sem reconhecimento de culpa |

> O tom segue o perfil do escritorio e a intensidade combativa do master, dirigida a clausulas e nao a pessoas (PA-17).

## 4. RISCOS DE RENUNCIA E QUITACAO AMPLA (alerta obrigatorio)

- **Quitacao ampla, geral e irrestrita** pode extinguir pretensoes que o consumidor sequer conhece (danos futuros, parcelas/cobrancas nao discutidas). **Pelo consumidor, alertar e preferir quitacao restrita ao objeto**; ressalvar expressamente o que nao se renuncia.
- Renuncia a direito indisponivel ou a tutela coletiva nao se opera por acordo individual — sinalizar.
- **Nao prometer resultado** nem fixar valor estimativo silencioso (PA-20). Sempre registrar a recomendacao e a ciencia do cliente sobre o alcance da quitacao.

## 5. HOMOLOGACAO E EXEQUIBILIDADE

- Requerer **homologacao judicial** para conferir forca de **titulo executivo** e viabilizar execucao direta em caso de descumprimento.
- No extrajudicial, garantir os requisitos de titulo executivo extrajudicial (assinaturas; conforme a forma exigida).
- Indicar no termo o **rito de execucao** do descumprimento (multa + saldo).

## 6. CHECKLIST ANTES DE ENTREGAR

- [ ] Polo coerente (PA-05) · Selo P1 citado · clausulas calibradas ao polo
- [ ] **Quitacao** com alcance definido · alerta de renuncia registrado (pelo consumidor, quitacao restrita)
- [ ] Valor/forma de pagamento, obrigacoes de fazer e multa liquidos e objetivos
- [ ] Homologacao prevista (titulo executivo) · superendividamento → plano art. 104-A (PA-14)
- [ ] Sem promessa de resultado (PA-20) · Sumula/Tema como `[VERIFICAR]` + `jurisprudencia-consumidor` (PA-01) · docs "doc. N"
- [ ] Submeter a `revisao-final-consumidor` (R1-R4) antes da entrega (PA-22)

## 7. ENCERRAMENTO

Entrega a minuta de acordo calibrada ao polo, com quitacao de alcance controlado, obrigacoes e multa liquidas e previsao de homologacao como titulo executivo, com os riscos de renuncia advertidos, pronta para a Suprema Corte R1-R4.
