#!/usr/bin/env python3
"""
check-engine.py — guarda de consistencia do "motor" dos plugins Adv-OS.

Os 11 plugins compartilham um mesmo ENCANAMENTO (engine generico). Cada plugin
so deve diferir nos TOKENS de dominio (STATE_DIR, prefixo de env, slug, sufixo do
/start). Este script normaliza esses tokens e verifica se os arquivos de
encanamento sao identicos entre todos os plugins. Se alguem mexer no engine de um
plugin so, este guarda acusa a drift — e a hora de propagar a mesma correcao aos demais.

Uso:  py tools/check-engine.py
Saida: 0 se consistente; 1 se ha drift.

NAO modifica nada. Para os arquivos de DOMINIO (lexico, templates, schema, state.py),
a divergencia e legitima e NAO e verificada aqui — ver ARCHITECTURE.md.
"""
import os, re, sys, hashlib, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Arquivos de ENCANAMENTO (genericos, devem ser identicos modulo tokens):
PLUMBING = [
    "scripts/hook-utils.py",
    "scripts/resolve-persona.py",
    "hooks/scripts/post-edit-evolve-memory.py",
    "hooks/scripts/pre-compact-snapshot.py",
    "hooks/hooks.json",
]

def plugins():
    return sorted(d for d in os.listdir(ROOT)
                  if d.endswith("-adv-os") and os.path.isdir(os.path.join(ROOT, d)))

def tokens(plug):
    """Descobre (state_dir, env_prefix, start_suffix) lendo os proprios arquivos."""
    sd = ep = ss = None
    p = os.path.join(ROOT, plug, "scripts/state.py")
    if os.path.isfile(p):
        t = open(p, encoding="utf-8", errors="replace").read()
        m = re.search(r'STATE_DIR\s*=\s*[\'"]([^\'"]+)[\'"]', t)
        sd = m.group(1) if m else None
    for f in ("templates/settings-local.json.tpl", "scripts/resolve-persona.py"):
        q = os.path.join(ROOT, plug, f)
        if os.path.isfile(q):
            m = re.search(r'([A-Z]{2,6})_PERSONA', open(q, encoding="utf-8", errors="replace").read())
            if m:
                ep = m.group(1); break
    # start suffix: procura /start-<algo> nos arquivos de comando
    for cmd in os.listdir(os.path.join(ROOT, plug, "commands")) if os.path.isdir(os.path.join(ROOT, plug, "commands")) else []:
        if cmd.startswith("start-"):
            ss = cmd[len("start-"):].replace(".md", ""); break
    return sd, ep, ss

def normalize(txt, plug, sd, ep, ss):
    txt = txt.replace("\r\n", "\n")
    if ss: txt = txt.replace("/start-" + ss, "/start-__SS__")
    # slug ANTES do STATE_DIR: em plugins multi-palavra (familia-sucessoes, isencao-ir-doenca)
    # o STATE_DIR e prefixo do slug; tokenizar o slug primeiro evita drift cosmetico.
    txt = txt.replace(plug, "__SLUG__")
    if sd: txt = re.sub(r'\b' + re.escape(sd) + r'\b', "__SD__", txt)
    if ep: txt = re.sub(r'\b' + re.escape(ep) + r'_', "__EP___", txt)
    # nomes de skill por dominio (memoria-de-caso-<short>) -> token
    txt = re.sub(r'memoria-de-caso-[a-z\-]+', "memoria-de-caso-__SHORT__", txt)
    return txt

def main():
    plugs = plugins()
    print(f"Plugins: {len(plugs)}\n")
    drift = False
    for f in PLUMBING:
        groups = collections.defaultdict(list)
        missing = []
        for p in plugs:
            path = os.path.join(ROOT, p, f)
            if not os.path.isfile(path):
                missing.append(p); continue
            sd, ep, ss = tokens(p)
            n = normalize(open(path, encoding="utf-8", errors="replace").read(), p, sd, ep, ss)
            groups[hashlib.md5(n.encode()).hexdigest()[:8]].append(p)
        if len(groups) == 1 and not missing:
            print(f"  OK   {f}")
        else:
            drift = True
            print(f"  DRIFT {f}" + (f"  (faltando: {missing})" if missing else ""))
            for h, ps in sorted(groups.items(), key=lambda x: -len(x[1])):
                print(f"        [{h}] {', '.join(s.replace('-adv-os','') for s in ps)}")
    print()
    if drift:
        print("DRIFT detectada — o engine de algum plugin divergiu. Propague a correcao canonica a todos.")
        return 1
    print("Engine consistente em todos os plugins (modulo tokens de dominio).")
    return 0

if __name__ == "__main__":
    sys.exit(main())
