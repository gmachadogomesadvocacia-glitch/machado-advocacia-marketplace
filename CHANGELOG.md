# CHANGELOG — marketplace Machado Advocacia

Histórico do conjunto de plugins jurídicos (Adv-OS). Datas em AAAA-MM-DD.

## 2026-06-16

### Eixo 2 — Harmonização e manutenção
- **`.gitattributes`** — normaliza quebras de linha (LF), silencia os avisos CRLF.
- **`tools/check-engine.py`** — guarda de consistência: verifica que os 5 arquivos de encanamento do engine são idênticos (módulo tokens) entre os 11 plugins; acusa drift futura.
- **`ARCHITECTURE.md`** — documenta a arquitetura: encanamento × domínio, tabela de tokens por plugin, regras de manutenção.
- **Engine normalizado** — `resolve-persona.py` passou a usar a forma específica `rode /start-<área>` em todos; docstring de `post-edit-evolve-memory.py` unificado. Baseline do verificador agora verde nos 11.

### Eixo 1 — Auditoria de jurisprudência
- Verificadas 117 citações distintas (90 súmulas + 4 vinculantes + 23 temas) contra fonte (STF/STJ/TNU/TST). ~20 correções em 9 plugins. Destaques: Tema 962 STF→STJ (tributário, 9×); Súm. 380/619 (imobiliário, teses trocadas); 6 súmulas TNU (previdenciário); Tema 692 (família); Súm. 391/263 (usucapião); Tema 987 cancelado (recuperação). Regra: número errado → remover, nunca inventar.

### Plugins construídos / publicados (Etapas A–F)
- **Etapa A** — `consumidor-adv-os` v0.1.0 (Consumidor & Bancário).
- **Etapa B** (migração dos legados ao chassi Adv-OS) — `previdenciario-adv-os` v0.2.0, `familia-sucessoes-adv-os` v2.0.0, `recuperacao-judicial-adv-os` v0.3.0.
- **Antecipado** — `isencao-ir-doenca-adv-os` v0.1.0 (isenção de IRPF por doença grave).
- **Etapa C** — `usucapiao-adv-os` v0.1.0 (judicial + extrajudicial).
- **Etapa D** — `tributario-adv-os` v0.1.1 (3 frentes × 3 esferas; skill dedicada Reforma CBS/IBS).
- **Interface** — cross-routing bidirecional `tributario` ↔ `isencao-ir-doenca`.
- **Etapa E** — `imobiliario-adv-os`, `criminal-adv-os`, `civel-adv-os` (todos v0.1.0).
- **Etapa F** — `transito-adv-os` v0.1.0 (multas e CNH).

Total: **11 plugins**, mesmo chassi Adv-OS (4 Camadas, Selo P1, Suprema Corte R1-R4, persona em runtime), ativos em Code + Cowork + Chat.

## Próximos (não iniciados)
- Eixo 1 (resta): caso-piloto real ponta a ponta + exercitar o engine numa sessão real.
- Eixos 3-5: modelos de peça embarcados, integração com o acervo (Casos-Ativos), atualidade legislativa, decisão público×privado.
- Ideia: `administrativo-adv-os` (servidores, licitações Lei 14.133, atos administrativos; resp. do Estado migraria do cível).
