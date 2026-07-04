#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
benchmark_datajud.py — Modulo B (benchmark publico) do plugin jurimetria-adv-os.

Consulta a API Publica do DataJud (CNJ) por CLASSE + ASSUNTO + ORGAO JULGADOR
(em vez de por numero de processo) e devolve estatisticas DESCRITIVAS de duracao
da amostra: N, mediana, quartis, min-max. Serve de regua publica para comparar
com o acervo proprio (coletar_acervo.py), unindo pela classificacao CNJ.

FREIOS (Proibicoes Estatisticas do plugin):
- A amostra e o que o DataJud INDEXOU e a pagina retornada — nao e a populacao.
  O relatorio DEVE declarar N retornado vs. total de hits (vies de selecao, PE-05).
- DataJud so tem capa + movimentos: duracao/andamentos SIM, quantum/merito NAO (PE-07).
- Saida carimba data da coleta (PE-10) e o metodo (PE-01).
- Janela default de ajuizamento (4 anos -> 1 ano atras): sem ela, o sort pega
  ajuizados ha dias e a "duracao" e ruido. Override --ajuizado-de/--ate/--sem-janela.

Uso CLI:
  py benchmark_datajud.py --tribunal tjrj --classe "Procedimento Comum Civel"
  py benchmark_datajud.py --tribunal trt1 --classe "Acao Trabalhista - Rito Ordinario" \
      --assunto "Verbas Rescisorias" --orgao "Vara do Trabalho de Campos" --size 200
  py benchmark_datajud.py --tribunal tjrj --classe-codigo 7 --assunto-codigo 9999
Opcoes: --ajuizado-de/--ajuizado-ate AAAA-MM-DD, --sem-janela, --grau, --size, --json <arquivo>.
"""
import argparse
import datetime
import io
import json
import statistics
import sys
import urllib.request

sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import datajud_client as dj

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

MAX_SIZE = 1000  # teto de uma pagina; acima disso declarar paginacao nao implementada


def janela_ajuizamento(args):
    """Janela default de ajuizamento: entre 4 anos e 1 ano atras.

    Sem janela, o sort por mais recentes devolve processos ajuizados ha dias e a
    'duracao' vira ruido (mediana de 2 dias no teste real). Janela da tempo de a
    amostra maturar. Override: --ajuizado-de/--ajuizado-ate ou --sem-janela.
    """
    if args.sem_janela:
        return None, None
    hoje = datetime.date.today()
    de = args.ajuizado_de or (hoje - datetime.timedelta(days=4 * 365)).isoformat()
    ate = args.ajuizado_ate or (hoje - datetime.timedelta(days=365)).isoformat()
    return de, ate


def montar_query(args):
    must = []
    if args.classe_codigo:
        must.append({"match": {"classe.codigo": args.classe_codigo}})
    elif args.classe:
        must.append({"match_phrase": {"classe.nome": args.classe}})
    if args.assunto_codigo:
        must.append({"match": {"assuntos.codigo": args.assunto_codigo}})
    elif args.assunto:
        must.append({"match_phrase": {"assuntos.nome": args.assunto}})
    if args.orgao:
        must.append({"match_phrase": {"orgaoJulgador.nome": args.orgao}})
    if args.grau:
        must.append({"match": {"grau": args.grau}})
    if not must:
        raise SystemExit("informe ao menos --classe/--classe-codigo (senao a amostra nao e comparavel — PE-09)")
    de, ate = janela_ajuizamento(args)
    if de or ate:
        # dataAjuizamento e string compacta yyyyMMddHHmmss no indice (nao ISO)
        faixa = {}
        if de:
            faixa["gte"] = de.replace("-", "") + "000000"
        if ate:
            faixa["lte"] = ate.replace("-", "") + "235959"
        must.append({"range": {"dataAjuizamento": faixa}})
    return {
        "size": min(args.size, MAX_SIZE),
        "query": {"bool": {"must": must}},
        "sort": [{"dataAjuizamento": {"order": "desc"}}],
    }


def consultar(alias, query, max_tentativas=5):
    url = dj.BASE % alias
    body = json.dumps(query).encode()
    chave = dj.get_chave()
    esperas = [0, 3, 8, 15, 25][:max_tentativas]
    ultimo = None
    for w in esperas:
        if w:
            __import__("time").sleep(w)
        req = urllib.request.Request(url, data=body, method="POST")
        req.add_header("Authorization", "APIKey " + chave)
        req.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            ultimo = "HTTP %s" % e.code
            if e.code != 429:
                raise
        except Exception as e:
            ultimo = type(e).__name__
    raise RuntimeError("esgotou %d tentativas (alias %s): %s" % (len(esperas), alias, ultimo))


def _quantis(valores):
    v = sorted(valores)
    n = len(v)
    if n == 0:
        return {}
    q = {
        "min": v[0],
        "mediana": round(statistics.median(v), 1),
        "max": v[-1],
    }
    if n >= 4:
        qs = statistics.quantiles(v, n=4)
        q["p25"], q["p75"] = round(qs[0], 1), round(qs[2], 1)
    return q


def estatisticas(hits, filtros, total_hits, alias, janela=None):
    duracoes = []
    graus = {}
    classes = {}
    sem_data = 0
    for h in hits:
        src = h.get("_source", {})
        r = dj.resumo(src)
        graus[r.get("grau") or "?"] = graus.get(r.get("grau") or "?", 0) + 1
        c = r.get("classe") or "?"
        classes[c] = classes.get(c, 0) + 1
        if r.get("duracao_dias") is not None:
            duracoes.append(r["duracao_dias"])
        else:
            sem_data += 1
    return {
        "fonte": "DataJud/CNJ (API Publica) — alias %s" % alias,
        "coletado_em": datetime.date.today().isoformat(),
        "filtros": filtros,
        "metodo": ("uma pagina de ate %d processos, ordenada por dataAjuizamento desc; "
                   "janela de ajuizamento %s; duracao = dataAjuizamento -> ultimo movimento; "
                   "amostra != populacao (PE-05)")
                   % (MAX_SIZE, janela or "NENHUMA (--sem-janela: recentes dominam e a duracao fica subestimada)"),
        "total_hits_no_indice": ("%s (teto do indice; ha mais)" % total_hits
                                 if total_hits == 10000 else total_hits),
        "N_retornado": len(hits),
        "N_com_duracao_calculavel": len(duracoes),
        "N_sem_data": sem_data,
        "duracao_dias": _quantis(duracoes),
        "por_grau": graus,
        "por_classe": classes,
        "avisos": [
            "DataJud NAO traz quantum/merito — so capa e movimentos (PE-07).",
            "Duracao de processos em andamento e censurada a direita (subestima o total).",
        ],
    }


def main():
    ap = argparse.ArgumentParser(description="Benchmark descritivo via DataJud (classe+assunto+orgao)")
    ap.add_argument("--tribunal", required=True, help="tjrj | trt1 | trf2 | api_publica_xxx")
    ap.add_argument("--classe")
    ap.add_argument("--classe-codigo", type=int)
    ap.add_argument("--assunto")
    ap.add_argument("--assunto-codigo", type=int)
    ap.add_argument("--orgao")
    ap.add_argument("--grau", help="G1 | G2")
    ap.add_argument("--size", type=int, default=100)
    ap.add_argument("--ajuizado-de", help="AAAA-MM-DD (default: 4 anos atras)")
    ap.add_argument("--ajuizado-ate", help="AAAA-MM-DD (default: 1 ano atras)")
    ap.add_argument("--sem-janela", action="store_true",
                    help="desliga a janela de ajuizamento (duracao ficara subestimada)")
    ap.add_argument("--json", dest="json_out")
    args = ap.parse_args()

    alias = args.tribunal if args.tribunal.startswith("api_publica_") else "api_publica_" + args.tribunal.lower()
    query = montar_query(args)
    filtros = {k: v for k, v in vars(args).items()
               if v and k in ("tribunal", "classe", "classe_codigo", "assunto", "assunto_codigo", "orgao", "grau")}

    d = consultar(alias, query)
    hits = d.get("hits", {}).get("hits", [])
    total = d.get("hits", {}).get("total", {})
    total_hits = total.get("value") if isinstance(total, dict) else total

    de, ate = janela_ajuizamento(args)
    janela = "%s a %s" % (de, ate) if (de or ate) else None
    if janela:
        filtros["ajuizamento"] = janela
    stats = estatisticas(hits, filtros, total_hits, alias, janela)
    print(json.dumps(stats, ensure_ascii=False, indent=2))
    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as fh:
            json.dump({"estatisticas": stats,
                       "amostra": [dj.resumo(h.get("_source", {})) for h in hits]},
                      fh, ensure_ascii=False, indent=2)
        print("\n  amostra salva em", args.json_out)


if __name__ == "__main__":
    main()
