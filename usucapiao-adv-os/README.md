# usucapiao-adv-os

Sistema operacional do advogado para **Usucapião** (judicial e extrajudicial), no padrão Adv-OS. As duas vias num só plugin. Side-aware: usucapiente (autor) × confrontante/oponente.

## Modalidades cobertas
| Modalidade | Base | Tempo | Chave |
|-----------|------|-------|-------|
| Extraordinária | CC 1.238 | 15 (10) anos | dispensa justo título/boa-fé (Súm. 391 STF) |
| Ordinária | CC 1.242 | 10 (5) anos | justo título + boa-fé |
| Especial urbana | CC 1.240 / CF 183 | 5 anos | até 250 m², moradia |
| Especial rural | CC 1.239 / CF 191 | 5 anos | até 50 ha, moradia + produção |
| Familiar | CC 1.240-A | 2 anos | ex-cônjuge que abandonou o lar |
| Coletiva | Estatuto da Cidade | 5 anos | núcleo urbano informal |

> **Bem público não é usucapível** (CF 183§3/191§ún; Súm. 340 STF).

## Vias
- **Judicial** — ação de usucapião; citação de confrontantes, titulares e União/Estado/Município + edital (CPC 246§3, 259 III).
- **Extrajudicial/cartório** — usucapião administrativa (CPC art. 1.071 + Lei 6.015 art. 216-A + Provimento CNJ): ata notarial, planta/memorial com ART, anuências, registro.

## Commands (10)
`/usucapiao-master` · `/triagem` · `/start-usucapiao` · `/status-usucapiao` · `/caso-usucapiao` · `/revisao-final` · `/judicial` · `/extrajudicial` · `/contestacao` · `/posse`

## Primeiro uso
1. `/start-usucapiao` — configura o escritório.
2. `/triagem` — classifica (polo, via, modalidade, imóvel) + pré-check da posse.
3. `/posse` — define a modalidade; depois `/judicial` ou `/extrajudicial`; tudo passa pela `revisao-final-usucapiao`.

---
Uso interno — Machado Advocacia. Saída padrão em `.txt`.
