#!/usr/bin/env python3
"""Client de l'API Judilibre (jurisprudence judiciaire française, via PISTE).

Ce script est appelé par le skill « judilibre ». L'utilisateur ne le lance pas
à la main : Claude l'exécute en coulisses puis met en forme le résultat.

Authentification (par ordre de priorité) :
  1. Argument --key (KeyId passé directement)
  2. Variable d'environnement JUDILIBRE_KEY_ID
  3. Fichier config.json placé à côté de ce script
  4. À défaut, mode OAuth2 (avancé) : JUDILIBRE_CLIENT_ID + JUDILIBRE_CLIENT_SECRET
     (ou les champs équivalents de config.json)

Le mode KeyId suffit dans l'immense majorité des cas : il s'agit simplement de
ta clé d'API placée dans l'en-tête HTTP « KeyId ». OAuth2 n'est qu'un repli.

Sortie : JSON sur stdout (pour que Claude puisse le lire), ou format lisible
avec --pretty.
"""

import argparse
import json
import os
import sys
import tempfile
import time

try:
    import requests
except ImportError:
    print(json.dumps({"error": "module 'requests' manquant",
                      "fix": "Demande à Claude d'exécuter : pip install requests"}))
    sys.exit(2)

HERE = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(HERE, "config.json")

ENVIRONMENTS = {
    "sandbox": {
        "api": "https://sandbox-api.piste.gouv.fr/cassation/judilibre/v1.0",
        "token": "https://sandbox-oauth.piste.gouv.fr/api/oauth/token",
    },
    "prod": {
        "api": "https://api.piste.gouv.fr/cassation/judilibre/v1.0",
        "token": "https://oauth.piste.gouv.fr/api/oauth/token",
    },
}

# Lien public vers le texte de la décision sur le site de la Cour de cassation.
PUBLIC_DECISION_URL = "https://www.courdecassation.fr/decision/{id}"

NETWORK_FIX = ("Dans les paramètres réseau de l'exécution de code de Claude, "
               "autorise au minimum « api.piste.gouv.fr » (et, seulement si tu "
               "utilises le bac à sable ou le mode OAuth : sandbox-api.piste.gouv.fr, "
               "oauth.piste.gouv.fr, sandbox-oauth.piste.gouv.fr).")


def load_config():
    """Charge les identifiants depuis env puis config.json (env prioritaire)."""
    cfg = {}
    if os.path.exists(CONFIG_PATH):
        try:
            with open(CONFIG_PATH, encoding="utf-8") as f:
                cfg = json.load(f)
        except Exception:
            cfg = {}
    env = os.getenv("JUDILIBRE_ENV") or cfg.get("env") or "prod"
    return {
        "env": env,
        "key_id": os.getenv("JUDILIBRE_KEY_ID") or cfg.get("key_id"),
        "client_id": os.getenv("JUDILIBRE_CLIENT_ID") or cfg.get("client_id"),
        "client_secret": os.getenv("JUDILIBRE_CLIENT_SECRET") or cfg.get("client_secret"),
    }


class Judilibre:
    MAX_PAGE_SIZE = 50          # plafond imposé par l'API
    MAX_RETRIES = 3             # tentatives sur 429 / 5xx
    RETRY_BACKOFF = 2.0         # secondes, doublé à chaque tentative

    def __init__(self, conf, key_override=None):
        env = conf["env"]
        if env not in ENVIRONMENTS:
            raise SystemExit(json.dumps({
                "error": f"env invalide: {env!r}",
                "fix": "Mets 'prod' ou 'sandbox' dans config.json (champ 'env').",
            }, ensure_ascii=False))
        self.env = env
        self.urls = ENVIRONMENTS[env]
        self.key_id = key_override or conf["key_id"]
        self.client_id = conf["client_id"]
        self.client_secret = conf["client_secret"]
        self._token = None
        self._token_exp = 0
        # Cache de jeton OAuth partagé entre invocations (process distincts).
        self._token_cache = os.path.join(
            tempfile.gettempdir(),
            f"judilibre_token_{env}_{(self.client_id or '')[:12]}.json",
        )
        if not self.key_id and not (self.client_id and self.client_secret):
            raise SystemExit(json.dumps({
                "error": "Aucune clé configurée.",
                "fix": "Renseigne ta clé Judilibre (KeyId) : indique-la à Claude "
                       "pour qu'il la sauvegarde dans scripts/config.json (champ "
                       "'key_id'). Le mode KeyId suffit.",
            }, ensure_ascii=False))

    # --- Authentification -------------------------------------------------

    def _headers(self):
        if self.key_id:
            return {"KeyId": self.key_id, "accept": "application/json"}
        return {"Authorization": f"Bearer {self._bearer()}",
                "accept": "application/json"}

    def _load_cached_token(self):
        try:
            with open(self._token_cache, encoding="utf-8") as f:
                tok = json.load(f)
            if tok.get("access_token") and time.time() < tok.get("exp", 0) - 30:
                return tok["access_token"], tok["exp"]
        except Exception:
            pass
        return None, 0

    def _bearer(self):
        if self._token and time.time() < self._token_exp - 30:
            return self._token
        cached, exp = self._load_cached_token()
        if cached:
            self._token, self._token_exp = cached, exp
            return cached
        try:
            r = requests.post(self.urls["token"], timeout=30, data={
                "grant_type": "client_credentials",
                "client_id": self.client_id,
                "client_secret": self.client_secret,
            })
        except requests.exceptions.ConnectionError as e:
            raise SystemExit(json.dumps({
                "error": "Connexion impossible au serveur OAuth PISTE.",
                "fix": NETWORK_FIX, "detail": str(e),
            }, ensure_ascii=False))
        if r.status_code in (400, 401):
            raise SystemExit(json.dumps({
                "error": "OAuth refusé (client_id / client_secret invalides).",
                "fix": "Vérifie tes identifiants OAuth, ou utilise plutôt le mode "
                       "KeyId (champ 'key_id'), bien plus simple.",
            }, ensure_ascii=False))
        r.raise_for_status()
        tok = r.json()
        self._token = tok["access_token"]
        self._token_exp = time.time() + tok.get("expires_in", 3600)
        try:
            with open(self._token_cache, "w", encoding="utf-8") as f:
                json.dump({"access_token": self._token, "exp": self._token_exp}, f)
        except Exception:
            pass
        return self._token

    # --- Requêtes ---------------------------------------------------------

    def _get(self, path, params=None):
        url = f"{self.urls['api']}{path}"
        last_exc = None
        for attempt in range(self.MAX_RETRIES):
            try:
                r = requests.get(url, headers=self._headers(),
                                 params=params, timeout=30)
            except requests.exceptions.ConnectionError as e:
                raise SystemExit(json.dumps({
                    "error": "Connexion impossible à piste.gouv.fr.",
                    "cause": "Le domaine n'est probablement pas autorisé dans les "
                             "réglages réseau de l'exécution de code.",
                    "fix": NETWORK_FIX, "detail": str(e),
                }, ensure_ascii=False))

            if r.headers.get("x-deny-reason") or (
                r.status_code == 403 and "allowlist" in r.text.lower()
            ):
                raise SystemExit(json.dumps({
                    "error": "Domaine réseau non autorisé.",
                    "cause": "Le proxy de l'exécution de code bloque piste.gouv.fr.",
                    "fix": NETWORK_FIX,
                }, ensure_ascii=False))
            if r.status_code == 401:
                raise SystemExit(json.dumps({
                    "error": "401 — clé refusée.",
                    "fix": "Vérifie la clé (KeyId) et qu'elle correspond au bon "
                           "environnement : une clé sandbox ne marche pas sur prod, "
                           "et inversement.",
                }, ensure_ascii=False))
            if r.status_code == 403:
                raise SystemExit(json.dumps({
                    "error": "403 — accès interdit.",
                    "fix": "Dans PISTE : valide les CGU Judilibre (chercher "
                           "« Judilibre ») et rattache l'API Judilibre à ton "
                           "application.",
                }, ensure_ascii=False))
            if r.status_code == 429 or r.status_code >= 500:
                # Quota atteint ou erreur serveur : on retente avec backoff.
                last_exc = f"HTTP {r.status_code}"
                if attempt < self.MAX_RETRIES - 1:
                    delay = self.RETRY_BACKOFF * (2 ** attempt)
                    retry_after = r.headers.get("Retry-After")
                    if retry_after and retry_after.isdigit():
                        delay = max(delay, int(retry_after))
                    time.sleep(delay)
                    continue
                raise SystemExit(json.dumps({
                    "error": f"{r.status_code} — quota ou serveur indisponible.",
                    "fix": "Quota PISTE atteint ou API momentanément indisponible. "
                           "Réessaie dans quelques instants ou réduis le rythme "
                           "des requêtes.",
                }, ensure_ascii=False))
            r.raise_for_status()
            return r.json()
        raise SystemExit(json.dumps(
            {"error": f"Échec après {self.MAX_RETRIES} tentatives ({last_exc})."},
            ensure_ascii=False))

    def search(self, query, **filters):
        params = {"query": query}
        for k, v in filters.items():
            if v is None:
                continue
            if k == "page_size":
                v = min(int(v), self.MAX_PAGE_SIZE)
            params[k] = v
        data = self._get("/search", params)
        # On enrichit chaque résultat d'un lien public cliquable.
        for res in data.get("results", []):
            if res.get("id"):
                res["url"] = PUBLIC_DECISION_URL.format(id=res["id"])
        return data

    def decision(self, decision_id):
        data = self._get("/decision", {"id": decision_id})
        if data.get("id"):
            data["url"] = PUBLIC_DECISION_URL.format(id=data["id"])
        return data

    def taxonomy(self, tax_id):
        return self._get("/taxonomy", {"id": tax_id})

    def auth_test(self):
        """Vraie vérification d'authentification : une recherche minimale.

        /healthcheck répond même sans clé valide ; on fait donc un /search
        réel pour confirmer que la clé est acceptée.
        """
        data = self._get("/search", {"query": "test", "page_size": 1})
        return {"ok": True, "env": self.env,
                "total_visible": data.get("total"),
                "mode": "KeyId" if self.key_id else "OAuth2"}


def fmt_results(data):
    lines = []
    total = data.get("total")
    lines.append(f"{total} décision(s) trouvée(s).\n")
    for r in data.get("results", []):
        nums = r.get("number") or ", ".join(r.get("numbers", []) or [])
        lines.append(
            f"• {r.get('jurisdiction', '?')} — {r.get('chamber', '')} "
            f"{r.get('formation', '')}".rstrip()
        )
        lines.append(f"  n° {nums}  |  {r.get('decision_date', '?')}  "
                     f"|  {r.get('solution', '')}".rstrip())
        if r.get("ecli"):
            lines.append(f"  ECLI : {r['ecli']}")
        if r.get("publication"):
            lines.append(f"  Publication : {', '.join(r['publication'])}")
        summ = r.get("summary") or ""
        if summ:
            lines.append(f"  Sommaire : {summ[:300]}{'…' if len(summ) > 300 else ''}")
        if r.get("url"):
            lines.append(f"  Lien : {r['url']}")
        lines.append(f"  id : {r.get('id')}")
        lines.append("")
    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser(description="Client API Judilibre")
    p.add_argument("--key", help="KeyId (sinon env ou config.json)")
    p.add_argument("--pretty", action="store_true", help="sortie lisible")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("search", help="rechercher des décisions")
    s.add_argument("query", help="termes de recherche")
    # Filtres acceptant une ou plusieurs valeurs (paramètres répétés côté API).
    s.add_argument("--chamber", nargs="+")        # soc, civ1, civ2, civ3, comm, crim…
    s.add_argument("--jurisdiction", nargs="+")   # cc (Cour de cassation), ca, tj
    s.add_argument("--type", nargs="+")
    s.add_argument("--theme", nargs="+")
    s.add_argument("--publication", nargs="+")
    s.add_argument("--solution", nargs="+")
    s.add_argument("--field", nargs="+",
                   help="restreint la recherche à certains champs (ex: expose, motivations)")
    s.add_argument("--operator", choices=["and", "or", "exact"],
                   help="opérateur entre les termes de la requête")
    s.add_argument("--date-start", dest="date_start")
    s.add_argument("--date-end", dest="date_end")
    s.add_argument("--page", type=int)
    s.add_argument("--page-size", dest="page_size", type=int, default=10,
                   help="max 50")
    s.add_argument("--sort", default="score")     # score | date
    s.add_argument("--order", default="desc")      # asc | desc

    d = sub.add_parser("decision", help="récupérer une décision par id")
    d.add_argument("id")

    t = sub.add_parser("taxonomy", help="valeurs possibles d'un filtre")
    t.add_argument("id", help="ex: chamber, jurisdiction, field, theme, solution")

    sub.add_parser("test", help="vérifier que la clé est acceptée (recherche réelle)")

    args = p.parse_args()
    jl = Judilibre(load_config(), key_override=args.key)

    if args.cmd == "search":
        data = jl.search(
            args.query, chamber=args.chamber, jurisdiction=args.jurisdiction,
            type=args.type, theme=args.theme, publication=args.publication,
            solution=args.solution, field=args.field, operator=args.operator,
            date_start=args.date_start, date_end=args.date_end,
            page=args.page, page_size=args.page_size,
            sort=args.sort, order=args.order,
        )
    elif args.cmd == "decision":
        data = jl.decision(args.id)
    elif args.cmd == "taxonomy":
        data = jl.taxonomy(args.id)
    elif args.cmd == "test":
        data = jl.auth_test()
        if args.pretty:
            print(f"Authentification OK ✓ (env={data['env']}, mode={data['mode']})")
        else:
            print(json.dumps(data, ensure_ascii=False))
        return

    if args.pretty and args.cmd == "search":
        print(fmt_results(data))
    else:
        print(json.dumps(data, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
