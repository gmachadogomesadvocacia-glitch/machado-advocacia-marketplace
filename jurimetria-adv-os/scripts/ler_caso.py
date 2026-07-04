#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ler_caso.py — extrai o bloco jurimetrico de um CASO.md (schema em caso-md-jurimetrico.md)
e, opcionalmente, enriquece com duracao/andamentos do DataJud (via datajud_client).

Sem dependencias externas (parser proprio chave: valor).

Uso:
  py ler_caso.py <caminho/CASO.md>
  py ler_caso.py <caminho/CASO.md> --datajud     # tambem puxa duracao/andamentos do DataJud
"""
import re, sys, io, json

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

INI = "<!-- jurimetria:inicio -->"
FIM = "<!-- jurimetria:fim -->"


def _conv(v):
    v = v.strip()
    if v == "" or v.lower() in ("null", "none", "-"):
        return None
    if re.fullmatch(r"-?\d+", v):
        return int(v)
    if re.fullmatch(r"-?\d+\.\d+", v):
        return float(v)
    return v


def parse_bloco(texto):
    """Le o miolo entre os marcadores; retorna dict {chave: valor}."""
    if INI not in texto or FIM not in texto:
        return None
    miolo = texto.split(INI, 1)[1].split(FIM, 1)[0]
    d = {}
    for linha in miolo.splitlines():
        linha = linha.split("#", 1)[0]  # remove comentario inline
        if ":" not in linha:
            continue
        k, v = linha.split(":", 1)
        k = k.strip()
        if k:
            d[k] = _conv(v)
    return d


def calcular_exito(d):
    """percentual_exito = obtido/pretendido, se ambos presentes e pretendido > 0."""
    p, o = d.get("quantum_pretendido"), d.get("quantum_obtido")
    if isinstance(p, (int, float)) and isinstance(o, (int, float)) and p > 0:
        return round(o / p, 3)
    return d.get("percentual_exito")


def enrich_datajud(d):
    """Acrescenta duracao/andamentos do DataJud usando numero_processo."""
    try:
        import datajud_client as dj
    except Exception as e:
        return {"erro_datajud": "import falhou: %s" % e}
    num = d.get("numero_processo")
    if not num:
        return {"erro_datajud": "sem numero_processo no bloco"}
    trib = d.get("tribunal")
    override = ("api_publica_" + trib.lower()) if trib else None
    try:
        src = dj.consultar(num, override if dj.alias_do_numero(num) is None else None)
    except Exception as e:
        return {"erro_datajud": str(e)[:120]}
    if not src:
        return {"datajud": "processo nao encontrado (nao indexado ou segredo)"}
    return {"datajud": dj.resumo(src)}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print("uso: py ler_caso.py <CASO.md> [--datajud]")
        sys.exit(2)
    texto = open(args[0], encoding="utf-8", errors="replace").read()
    d = parse_bloco(texto)
    if d is None:
        print("Nenhum bloco jurimetrico encontrado (faltam os marcadores jurimetria:inicio/fim).")
        sys.exit(1)
    d["percentual_exito"] = calcular_exito(d)
    saida = {"acervo (CASO.md)": d}
    if "--datajud" in sys.argv:
        saida.update(enrich_datajud(d))
    print(json.dumps(saida, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
