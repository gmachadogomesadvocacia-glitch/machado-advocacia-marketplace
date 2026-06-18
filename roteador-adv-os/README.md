# roteador-adv-os — porta de entrada unica dos plugins Adv-OS

Identifica **automaticamente**, a partir do que voce escreve, qual dos 11 plugins
juridicos do escritorio deve ser usado — sem voce precisar lembrar do `/start-X`.

## Como funciona
Voce descreve o caso ("meu cliente foi negativado pelo banco", "recebi uma execucao
fiscal de ICMS", "quero entrar com divorcio"...) e o roteador:
1. **identifica o tema** entre as 11 areas,
2. **mostra os sinais** que usou para decidir,
3. **confirma** com voce e so entao aciona o plugin certo.

Em caso de fronteira ambigua (ex.: negativacao = consumidor x civel), ele **pergunta**
em vez de adivinhar. Se voce ja disse a area, ele vai direto.

## Acionamento
- **Automatico**: descreva o caso normalmente — o roteador ativa sozinho quando a area
  nao foi dita (skill `roteador-adv-os`, lida em Code, Cowork e Chat).
- **Explicito**: `/rotear [descricao do caso]`.

## Areas cobertas
tributario · previdenciario · familia/sucessoes · recuperacao judicial · consumidor ·
imobiliario · criminal · civel · transito · usucapiao · isencao de IR por doenca.

## O que NAO faz
Nao produz peca, calculo nem analise de merito — isso e do plugin de destino. O
roteador so classifica, confirma e encaminha. Comportamento: **sugerir e confirmar**.
