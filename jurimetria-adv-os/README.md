# jurimetria-adv-os

Plugin **analitico** de jurimetria no padrao Adv-OS: transforma o acervo do escritorio + dados
publicos do DataJud/CNJ em relatorios descritivos disciplinados. **Nao produz peca** — produz
numero com carimbo (N, metodo, fonte, data).

## A espinha

| Fonte | Da | Nao da |
|-------|----|--------|
| **DataJud/CNJ** (API publica, gratis) | capa + movimentos: duracao, andamentos, classe/assunto/orgao oficiais | quantum, merito, teor |
| **Acervo proprio** (bloco jurimetrico nos `CASO.md`) | quantum pretendido/obtido, resultado, taxa de exito | o que nao foi instrumentado |

Unidas pelo **numero CNJ**. O bloco jurimetrico (schema em `templates/bloco-jurimetrico.md.tpl`)
e a materia-prima — a skill `instrumentar-caso` o preenche, puxando a classificacao oficial do DataJud,
e a skill `encerrar-caso` fecha o ciclo (desfecho + arquivamento) quando o caso termina.

## Motores (Tier 2)

- **Modulo A** `consulta-datajud` — um processo: duracao, ritmo, ultimo andamento
- **Modulo B** `benchmark-datajud` — regua publica por classe+assunto+orgao (mediana/quartis)
- **Modulo C** `coleta-acervo` — retrato do portfolio (composicao, quantum, taxa de exito)
- `analise-quantum` — faixa de valor bifasica (procedencia x valor), acervo + jurisprudencia
- `tempo-processual` — duracao/fases/parados, com censura a direita declarada
- `viabilidade-jurimetrica` — quadro de apoio a decisao (sem probabilidade de exito)

## Governanca

- **Camada 1:** 14 **Proibicoes Estatisticas** (PE-01 a PE-14) — sem bypass. Nucleo: nenhum numero
  sem N+metodo+fonte+data; descritivo != preditivo; **nunca promessa de resultado** (veda OAB);
  N < limiar → so qualitativo; PII fora de agregados (LGPD + sigilo OAB).
- **Camada 2:** 6 Protocolos (Proveniencia, Instrumentacao, N-minimo, Harmonizacao CNJ, Sigilo, Revisao).
- **Camada 3:** estilo do relatorio (pergunta → dados → resultados → limitacoes → leitura).
- **Camada 4:** 13 skills (Tier 0-3) + 13 commands. Suprema Corte `revisao-final-jurimetria` (R1-R4 + R5 red-team).

## Instalar / comecar

1. Instalar o plugin (marketplace `machado-advocacia-marketplace`).
2. `/start-jurimetria` — aponta o acervo (CASE_ROOT), tribunais de referencia e o N minimo.
3. `/coletar-acervo` — o primeiro retrato do portfolio (e a lista do que falta instrumentar).

Scripts em `scripts/` (stdlib only, Python 3.11+): `datajud_client.py`, `ler_caso.py`,
`coletar_acervo.py`, `benchmark_datajud.py`.
