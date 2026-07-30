# Polskie Umowy Gospodarcze

**Przykład jak może wyglądać Claude w polskich umowach.**
Może stanowić punkt wyjścia, jak powinny wyglądać praktyczne narzędzia AI dla prawników.

Powstał w naszej kancelarii (**Kancelaria Radców Prawnych Żurawska Piotrowski i Wspólnicy**, [ktzr.pl](https://ktzr.pl)), na bazie codziennej praktyki przy umowach B2B, IP i IT.

> ⚠️ **Zastrzeżenie:** Skill nie zastępuje porady prawnej, jest narzędziem operacyjnym wspomagającym pracę prawnika, a każda konkretna sprawa wymaga indywidualnej weryfikacji przez uprawnioną osobę.

## Po co to publikujemy

O AI w polskim Legaltech mówi się bardzo dużo, szczególnie na konferencjach i w postach w social mediach, ale realnych wdrożeń, które faktycznie pomagają w codziennej praktyce kancelarii, jest znacznie mniej.

Naszym zdaniem najlepsze narzędzia nie powstają z prezentacji konferencyjnych ani z konsultingowych PoC'ów, ale z codziennego użycia. Robimy coś dla siebie, używamy, poprawiamy w trakcie i — gdy zaczyna działać — dzielimy się z innymi.

Tu zaczęliśmy od konkretu, czyli od redakcji umów B2B, IP i IT, którą zapakowaliśmy w skilla Claude'a i pokazujemy publicznie — nie po to, żeby ogłosić *„produkcyjne narzędzie KTZR"*, tylko żeby pokazać jeden z możliwych sposobów podejścia do tematu, otwarty na krytykę, fork i dyskusję.

Może komuś:
- da pomysł, jak zbudować własny skill dla innego obszaru prawa albo innej kancelarii
- skłoni do rozmowy *„jak powinno wyglądać claude-for-legal po polsku"*, bo na razie ekosystem Anthropic to przede wszystkim US/UK common law

Jeśli zechcesz w to wejść (issues, PR-y, komentarze, fork, własna wersja dla innej dziedziny), wszystko mile widziane.

## Co warto wiedzieć, zanim zaczniesz

Żeby uniknąć rozczarowań, kilka uczciwych zastrzeżeń:

- **Skill zawiera tylko część naszej bazy wiedzy i workflow.** Pełna wersja zostaje wewnętrznie, ponieważ tajemnica zawodowa radcy prawnego (art. 3 ustawy o radcach prawnych) wymaga, żeby wszystko, co dotyczy konkretnych spraw klientów, case studies czy profili klientów, nie wyszło na zewnątrz. **To, co publikujemy, to przykłady, nie wzorce *„jedynie słuszne"*.**

- **Skill jest tak dobry, jak Twoja własna praca z nim** — klasyczne *garbage in, garbage out* działa tu szczególnie mocno, więc najlepsze efekty daje iteracyjne ulepszanie pod własną praktykę, w której dorzucasz własne klauzule do `references/baza-klauzul/`, własne reguły do `references/zlote-reguly.md` i własne workflowy. Nasz zestaw stanowi tylko punkt startowy.

- **Skill nie jest wzorcem uniwersalnym** — opiera się na decyzjach projektowych jednej kancelarii, więc jeśli pracujesz inaczej, śmiało forkuj i dostosuj go pod swoją praktykę.

- **Zakres ograniczony** do umów B2B, IP i IT, bez prawa karnego, administracyjnego, podatkowego, rodzinnego ani postępowań sądowych.

- **Skill nie jest jeszcze w `claude-plugins-community`** — na razie instalujesz go prosto z naszego repo.

## Co w środku

Skill ma pięć warstw merytorycznych:

| Warstwa | Co zawiera | Plik |
|---|---|---|
| **Złote Reguły** | 12 reguł redakcji polskich umów: kontrola definicji, struktury, języka | `references/zlote-reguly.md` |
| **Styl redakcyjny KTZR** | Konkretne wzorce stylistyczne wyciągnięte z praktyki: kiedy *„W przypadku"* zamiast *„Jeżeli"*, para stron dla typu stosunku, typografia | `references/style-redakcyjny.md` |
| **Taksonomia kategorii klauzul** | 7 kategorii klauzul, polski odpowiednik MSCD Adamsa | `references/kategorie-klauzul.md` |
| **Baza klauzul** | 20 plików tematycznych z wzorcami klauzul: strony, preambuły, definicje, IP, RODO, kary umowne, ugody, regulaminy SaaS/hosting i inne | `references/baza-klauzul/` |
| **Baza wiedzy doktrynalnej** | 13 plików z analizą prawno-doktrynalną: *lucrum cessans*, RODO, prawa autorskie, open source copyleft, wykładnia oświadczeń woli, regulaminy u.ś.u.d.e./DSA/AI i inne | `references/baza-wiedzy/` |

Plus 8 gotowych workflow'ów do typowych zadań:

| Workflow | Kiedy używać |
|---|---|
| `pelna-analiza.md` | Pełna analiza umowy z perspektywy klienta |
| `triage-szybki.md` | Szybka kategoryzacja GREEN / YELLOW / RED w 5-10 minut |
| `generator-umow.md` | Generowanie nowej umowy od zera |
| `popraw-fragment.md` | Doprecyzowanie konkretnej klauzuli |
| `audyt-ryzyk.md` | Identyfikacja ryzyk w umowie kontrahenta |
| `ocena-2-strony.md` | Analiza umowy oczami drugiej strony (devil's advocate) |
| `cold-start-klienta.md` | Onboarding nowego klienta, 10-15 minutowy wywiad |
| `weryfikacja-spojnosci-odeslan.md` | Sprawdzenie spójności odesłań § / ust. / pkt |

## Komplementarne narzędzie: legal-cite-pl

Skill działa najlepiej w parze z **[legal-cite-pl](https://github.com/apiotrowski-afk/legal-cite-pl)** — serwerem MCP, który pobiera **dokładne, aktualne brzmienie cytowanego przepisu** prosto ze źródła (Sejm ELI / EUR-Lex), zwracając **tekst jednolity**, nie pierwotny.

Gdy podłączysz go w Claude (stdio lokalnie albo jeden URL na Cloud Run), skill cytuje przepisy (k.c., RODO, pr. aut., u.ś.u.d.e. itd.) **z weryfikacją ze źródła zamiast z pamięci modelu** — mniej halucynacji w cytatach:

```
verify_article("art. 385¹ KC")   → dosłowny tekst przepisu (niedozwolone postanowienia umowne)
verify_article("art. 28 ust. 3 RODO")
```

Instalacja i szczegóły: **[github.com/apiotrowski-afk/legal-cite-pl](https://github.com/apiotrowski-afk/legal-cite-pl)**.

**Pozostałe z ekosystemu** (otwarte narzędzia LegalTech PL):
- **[anon-legal-pl](https://github.com/apiotrowski-afk/anon-legal-pl)** — lokalna anonimizacja akt prawnych (PESEL/NIP, sygnatury) na bazie Presidio.
- **[kancelaria-dms](https://github.com/apiotrowski-afk/kancelaria-dms)** — DMS/CRM dla kancelarii (Google Workspace).

## Dla kogo

W praktyce skill najlepiej sprawdza się dla:

- **radców prawnych i adwokatów** obsługujących umowy B2B, IP i IT
- **in-house counsel** w firmach IT, startupach, działach prawnych
- **prawników korzystających z Claude'a** w codziennej pracy nad umowami
- **autorów innych skilli legal** — jako referencyjny przykład struktury

Studenci prawa też skorzystają, ale to nie zastąpi podręcznika; narzędzie jest do pracy nad konkretnymi klauzulami.

## Quick start

### Wymagania

Jedno z:
- Konto [Claude.ai](https://claude.ai/) (Pro lub Team) do użycia jako skill w Claude.ai
- API key Anthropic do użycia programistycznego
- [Claude Code](https://www.anthropic.com/claude-code) do użycia lokalnie

### Instalacja

**Opcja 0 — CLI (najszybciej, 40+ agentów)**

```bash
npx skills add apiotrowski-afk/commercial-legal-pl
```

Działa z Claude Code, Cursor, Codex i innymi. Instaluje wprost z repo.

**Opcja 1 — Claude.ai (web)**

```bash
git clone https://github.com/apiotrowski-afk/commercial-legal-pl.git
```

Następnie: Claude.ai → Settings → Skills → Import skill → wskaż katalog → aktywuj w sesji.

**Opcja 2 — Claude Code (CLI)**

```bash
git clone https://github.com/apiotrowski-afk/commercial-legal-pl.git \
  ~/.claude/skills/commercial-legal-pl
```

Skill załaduje się automatycznie przy nowej sesji Claude Code.

**Opcja 3 — Manualne wskazanie**

Sklonuj repo do dowolnego katalogu i w sesji Claude'a wskaż ścieżkę do `SKILL.md` jako kontekst startowy.

### Pierwsze użycie

Trzy typowe scenariusze startowe:

**Analiza umowy od kontrahenta:**
> *„Klient dostał umowę od kontrahenta. Pomóż mi ją przeanalizować i zidentyfikować ryzyka."*

Claude załaduje `workflows/pelna-analiza.md` lub — przy bardziej standardowej umowie — `workflows/triage-szybki.md`.

**Generowanie nowej umowy:**
> *„Potrzebuję wygenerować NDA dla startupu (strony, czas, kary umowne 50k PLN)."*

Claude załaduje `workflows/generator-umow.md` + odpowiednie pliki z `baza-klauzul/`.

**Doprecyzowanie klauzuli:**
> *„Mam taką klauzulę odpowiedzialności. Co można poprawić?"*

Claude załaduje `workflows/popraw-fragment.md` + `style-redakcyjny.md` + relewantne pliki bazy wiedzy.

## Architektura

```
commercial-legal-pl/
├── SKILL.md                              ← Główny plik wejściowy dla Claude
├── README.md                             ← Ten plik
├── LICENSE                               ← Apache 2.0
├── NOTICE                                ← Standardowa nota Apache
├── .gitignore                            ← Wykluczenia poufnych materiałów
│
├── references/
│   ├── zlote-reguly.md                   ← 12 reguł redakcji
│   ├── style-redakcyjny.md               ← Warstwa 1 + 2 stylu KTZR
│   ├── kategorie-klauzul.md              ← Taksonomia (polski Adams)
│   ├── legal-design.md                   ← Typografia i layout
│   ├── essentialia-mapowanie.md          ← Essentialia negotii dla typów umów
│   │
│   ├── baza-klauzul/                     ← 20 plików tematycznych + INDEX
│   │   ├── 01-oznaczenie-stron.md
│   │   ├── 02-preambuly.md
│   │   ├── 03-definicje.md
│   │   ├── ...
│   │   └── 20-regulamin-usdde-aup.md
│   │
│   └── baza-wiedzy/                      ← 13 plików doktrynalnych + INDEX
│       ├── 01-maintenance-art750-kc.md
│       ├── 02-przeniesienie-praw-oprogramowanie.md
│       ├── ...
│       └── 13-regulamin-usdde-hosting-ai.md
│
├── workflows/                            ← 8 gotowych workflow'ów
│   ├── pelna-analiza.md
│   ├── triage-szybki.md
│   └── ...
│
└── scripts/
    ├── pre-commit-sanitizer.py           ← Hook chroniący przed wyciekiem danych
    └── install-hooks.sh                  ← Bash installer
```

## Inspiracje i metoda

Skill nie powstał z niczego — korzystamy z:

- **Ken Adams**, *A Manual of Style for Contract Drafting* (5. wyd. ABA 2023) — koncepcja *„categories of contract language"* zaadaptowana do polskiego systemu prawnego
- **Polskie Zasady Techniki Prawodawczej** (Rozp. Prezesa RM z 20.06.2002) — krajowy odpowiednik MSCD dla aktów prawnych, hierarchia struktury (artykuł → ustęp → punkt → litera)
- **Bryan Garner** i **Joseph Kimble** — plain-language movement zaaplikowany do polskiego języka prawniczego
- **Praktyka naszej kancelarii** — wzorce wypracowane w codziennej obsłudze klientów z obszaru B2B, IP i IT

## Changelog

| Wersja | Data | Co nowego |
|---|---|---|
| **v0.2** | 4 czerwca 2026 | Nowe pliki bazy wiedzy: wykładnia oświadczeń woli (SN 2024–2025), regulaminy u.ś.u.d.e./DSA/AI. Nowe klauzule: gwarancja czystości IP, warranty AI-generated code, SLA, exit plan IT, zakaz konkurencji IT z miesięcznym compliance, regulamin hosting/SaaS/domeny/AI. Baza klauzul: 19 → 20 plików, baza wiedzy: 11 → 13 plików. |
| **v0.1** | 31 maja 2026 | Pierwsze publiczne wydanie — Złote Reguły, baza klauzul (19 plików), baza wiedzy (11 plików), 8 workflow'ów. |

## Co dalej

Mamy wersję 0.x, czyli pierwszą publiczną iterację, w której wiele rzeczy zostało jeszcze do zrobienia — niektóre z nich mogą być świetnym punktem wyjścia, jeśli chcesz dorzucić swój wkład:

| Wersja | Status | Zakres |
|---|---|---|
| **0.x** | ✅ Wydana | Polski skill, umowy B2B, IP i IT (Złote Reguły, baza klauzul, baza wiedzy, 8 workflow'ów) |
| **1.0** | 🟡 Plan 2026 Q3 | Plugin manifest format Anthropic (weryfikacja zgodności), submisja do `claude-plugins-community` |
| **1.1** | 🟢 Plan 2026 Q4 | Rozszerzenie bazy klauzul (sektor finansowy, employment B2B, e-commerce); baza orzeczeń z linkami do SIP publicznych |
| **2.0** | 🟢 Long-term | Multi-language framework, szablon adaptowalny do innych jurysdykcji civil law (Niemcy, Francja, Włochy, Hiszpania) |

Pominięte (świadomie, na razie):
- prawo karne, administracyjne, podatkowe, rodzinne — to inne obszary praktyki
- postępowania sądowe — skill jest zaprojektowany pod redakcję i analizę umów, nie litigation support
- test-suite dla skilla — jest na liście planów, ale jeszcze nie uruchomiony

## Jak współtworzyć

Wkład każdej osoby jest dla nas wartościowy, niezależnie od formy:

- **Zauważyłeś brak lub błąd?** Otwórz issue. Szczególnie cenne są konkretne klauzule, nowsze orzeczenia, błędne odesłania.
- **Masz pomysł na nowy workflow albo całą warstwę?** PR mile widziany.
- **Po prostu chcesz zapytać czy podyskutować?** GitHub Discussions albo bezpośredni kontakt.

Każdy PR przed merge'em sprawdzamy ręcznie, przede wszystkim pod kątem braku poufnych danych. Pre-commit hook (`scripts/pre-commit-sanitizer.py`) pomoże to wyłapać u Ciebie lokalnie. Plus dobrze, jeśli styl trzyma się [Złotych Reguł](./references/zlote-reguly.md) i [Stylu redakcyjnego](./references/style-redakcyjny.md), choć jeśli proponujesz coś zupełnie innego, otwarci jesteśmy na dyskusję.

## Licencja

**Apache License 2.0** (zobacz [LICENSE](./LICENSE)).

Możesz używać swobodnie, komercyjnie i niekomercyjnie. Zachowaj notę o licencji w plikach, które wykorzystujesz lub modyfikujesz.

## Autor i utrzymanie

**Adam Piotrowski** — radca prawny, specjalizacja LegalTech, AI i prawo umów IT.

Kancelaria Radców Prawnych **Żurawska Piotrowski i Wspólnicy** ([ktzr.pl](https://ktzr.pl))

GitHub: [@apiotrowski-afk](https://github.com/apiotrowski-afk)

## Zastrzeżenie zawodowe

Skill **nie stanowi porady prawnej**. Jest narzędziem operacyjnym wspomagającym pracę uprawnionego prawnika (radcy prawnego, adwokata lub doradcy podatkowego), odpowiednio do zakresu konkretnego zlecenia.

Każda sprawa wymaga indywidualnej analizy przez uprawnioną osobę. Kancelaria KTZR oraz Adam Piotrowski nie ponoszą odpowiedzialności za jakiekolwiek skutki użycia skilla bez stosownej weryfikacji prawniczej.
