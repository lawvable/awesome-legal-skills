# Workflow: Weryfikacja spójności odesłań i powiązań


> _Reguły globalne: `references/rdzen-ktzr.md` (R1 cytowania · R2 bramka · R3 role · R4 profil · R5 format)._

Dedykowany dwuetapowy workflow do wykrywania **błędów odesłań i niespójności wewnętrznych** w długich umowach (typowo 15+ stron). Adresuje typowy problem: model dobrze czyta każdy paragraf osobno, ale gorzej widzi **relacje pomiędzy odległymi fragmentami** — efekt attention dilution w długim kontekście.

## Kiedy uruchomić ten workflow

**Automatycznie** (Claude sam decyduje):
- Umowa ma > 15 stron lub > 5 000 słów
- Umowa ma > 15 paragrafów
- Umowa zawiera > 10 odesłań międzyparagrafowych ("§ X ust. Y")
- Wstępna analiza (etap 3 pełnej analizy) wykazała > 3 niespójności

**Na żądanie użytkownika**:
- "Sprawdź odesłania w tej umowie"
- "Czy paragrafy się zgadzają"
- "Sprawdź spójność wewnętrzną"
- "Czy nie ma błędów w numeracji"

**Jako standalone** (bez pełnej analizy) — pełna procedura
**Jako wbudowany etap 3** (w ramach `pelna-analiza.md`) — uproszczona prezentacja, ale ta sama metoda

## Dlaczego dwuetapowość

Problem **attention dilution** w długim kontekście nie znika nawet przy oknach 200K. Model "widzi" całą umowę, ale jego uwaga **nie jest jednolita** — relacje między odległymi fragmentami (np. odesłanie w § 18 do definicji w § 2) są gorzej śledzone niż treść pojedynczego paragrafu.

Rozwiązanie: **rozdzielenie inwentaryzacji od weryfikacji**.

- **PASS 1** to czysta lista — model nie analizuje, tylko wymienia. Zmusza go do **pełnego przejścia** przez dokument bez próby wnioskowania.
- **PASS 2** to weryfikacja pojedyncza — model sprawdza **każde odesłanie osobno**, w formie tabeli wymuszającej eksplicytną weryfikację każdego punktu (nie ufanie pamięci kontekstowej).

To podejście wymusza, że jeśli odesłanie "§ 8 ust. 3" jest błędne, model **musi to zobaczyć**, bo musi wpisać do tabeli, co konkretnie znajduje się w § 8 ust. 3.

---

## PASS 1: INWENTARYZACJA (lista, nie analiza)

### Krok 1.1: Inwentaryzacja struktury umowy

Wypisz **wszystkie paragrafy** umowy z krótkim opisem (max 1 zdanie) co regulują. Plus załączniki.

**Format wyjścia:**

```
## INWENTARYZACJA STRUKTURY

### Paragrafy
| § | Tytuł | Liczba ustępów | Krótki opis (1 zdanie) |
|---|-------|----------------|------------------------|
| § 1 | Definicje | 12 | Słownik 12 terminów używanych w umowie |
| § 2 | Przedmiot umowy | 4 | Świadczenie usług IT przez Usługodawcę na rzecz Usługobiorcy |
| § 3 | Wynagrodzenie | 6 | Stawka godzinowa 250 PLN, faktury miesięczne, termin 14 dni |
| ... | ... | ... | ... |

### Załączniki
| Nr | Tytuł | Wzmiankowany w § | Obecny w pakiecie? |
|----|-------|------------------|--------------------|
| 1 | Specyfikacja techniczna | § 2 ust. 1 | ✅ TAK |
| 2 | Wzór timesheet | § 4 ust. 3 | ❓ Niejasne (nie widzę w przekazanym materiale) |
| ... | ... | ... | ... |
```

### Krok 1.2: Inwentaryzacja odesłań

Wypisz **wszystkie odesłania** w umowie — międzyparagrafowe, do załączników, semantyczne.

**Trzy kategorie:**

**A. Odesłania jednoznaczne** (wskazujące konkretną jednostkę redakcyjną):
- "§ X", "§ X ust. Y", "§ X ust. Y pkt Z"
- "Załącznik nr X"

**B. Odesłania semantyczne** (wymagające interpretacji):
- "powyższe postanowienia"
- "niniejszy paragraf"
- "wskazane wyżej"
- "z zastrzeżeniem § X"
- "z wyłączeniem przypadków, o których mowa w..."

**C. Odesłania do definicji** (terminy z wielkiej litery):
- "Strona", "Wykonawca", "Usługodawca", "Specjalista", "System", "Utwór" itd.

**Format wyjścia:**

```
## INWENTARYZACJA ODESŁAŃ

### A. Odesłania jednoznaczne (suma: N)

| # | Lokalizacja źródłowa | Tekst odesłania |
|---|---------------------|-----------------|
| 1 | § 4 ust. 2 | "zgodnie z § 3 ust. 1" |
| 2 | § 5 ust. 3 | "Wynagrodzenie określone w § 3" |
| 3 | § 8 ust. 4 | "Załącznik nr 2 (Wzór Timesheet)" |
| ... | ... | ... |

### B. Odesłania semantyczne (suma: N)

| # | Lokalizacja źródłowa | Tekst odesłania |
|---|---------------------|-----------------|
| 1 | § 5 ust. 4 | "Powyższe nie wyłącza..." |
| 2 | § 9 ust. 2 | "z zastrzeżeniem ust. 3" |
| ... | ... | ... |

### C. Odesłania do definicji (suma: N)

Lista wszystkich terminów z wielkiej litery używanych w treści (z liczbą wystąpień):
- "Strona" (12×), "Wykonawca" (45×), "Specjalista" (8×), "System" (23×) itd.
```

### Krok 1.3: Inwentaryzacja definicji

Z § Definicje (lub innych miejsc) wypisz **wszystkie zdefiniowane terminy**:

**Format wyjścia:**

```
## INWENTARYZACJA DEFINICJI

| # | Termin | Lokalizacja definicji | Definicja (skrót) |
|---|--------|----------------------|-------------------|
| 1 | "Strona" | § 1 ust. 1 | Usługodawca lub Usługobiorca |
| 2 | "Specjalista" | § 1 ust. 5 | Pracownik Usługodawcy oddelegowany na podstawie umowy |
| 3 | "System" | § 1 ust. 8 | Oprogramowanie objęte Umową |
| ... | ... | ... | ... |
```

### STOP 1 — Potwierdzenie inwentaryzacji

> **Pytanie do użytkownika:** *"Inwentaryzacja zakończona. Czy lista załączników jest kompletna? Czy są jakieś dokumenty, które powinienem uwzględnić, a których nie widzę? Przechodzimy do weryfikacji (Pass 2)?"*

Bez tego STOPu można sprawdzać odesłania do nieistniejących załączników, które faktycznie są — tylko nie zostały przekazane Claude'owi.

---

## PASS 2: WERYFIKACJA (każdy element osobno)

### Krok 2.1: Weryfikacja odesłań jednoznacznych

Dla **każdego** odesłania z tabeli A z Pass 1 — weryfikacja w tabeli:

```
## WERYFIKACJA ODESŁAŃ JEDNOZNACZNYCH

| # | Źródło | Odesłanie | Cel istnieje? | Treść celu (skrót) | Pasuje do kontekstu? | Status |
|---|--------|-----------|---------------|--------------------|--------------------|--------|
| 1 | § 4 ust. 2 | "zgodnie z § 3 ust. 1" | ✅ TAK | "Wynagrodzenie netto wynosi 250 PLN za godzinę" | ✅ TAK | ✅ OK |
| 2 | § 5 ust. 3 | "Wynagrodzenie określone w § 3" | ✅ TAK | § 3 reguluje wynagrodzenie (cały paragraf) | ✅ TAK | ✅ OK |
| 3 | § 8 ust. 4 | "Załącznik nr 2 (Wzór Timesheet)" | ❓ Załącznik wzmiankowany, ale nie w pakiecie | — | — | ⚠️ DO POTWIERDZENIA |
| 4 | § 12 ust. 1 | "kary umowne, o których mowa w § 9 ust. 3" | ✅ TAK | "Kara umowna za naruszenie poufności..." | ❌ NIE — § 9 ust. 3 reguluje karę za POUFNOŚĆ, a § 12 mówi o karze za ZWŁOKĘ | 🔴 BŁĄD ODESŁANIA |
| 5 | § 15 ust. 2 | "zgodnie z § 17" | ❌ NIE — ostatni paragraf to § 16 | — | — | 🔴 ODESŁANIE NIEISTNIEJĄCE |
| 6 | § 11 ust. 4 | "wskazane w §___" | — | — | — | 🔴 PUSTE POLE ODESŁANIA |
```

**Kategorie statusu:**

- ✅ **OK** — odesłanie poprawne, cel istnieje, treść celu odpowiada kontekstowi
- ⚠️ **DO POTWIERDZENIA** — cel istnieje, ale niejasna interpretacja (np. semantyczne odesłanie, lub załącznik nieobecny w pakiecie)
- 🔴 **BŁĄD ODESŁANIA** — cel istnieje, ale jego treść NIE pasuje do kontekstu odesłania
- 🔴 **ODESŁANIE NIEISTNIEJĄCE** — paragraf/ustęp/pkt, do którego się odsyła, nie istnieje w umowie
- 🔴 **PUSTE POLE** — autor zostawił niewypełniony placeholder (rzadkie, ale się zdarza)

### Krok 2.2: Weryfikacja odesłań semantycznych

Każde odesłanie semantyczne wymaga **rozszyfrowania kontekstowego** — co konkretnie ma być "powyższe", "niniejsze", "wskazane".

```
## WERYFIKACJA ODESŁAŃ SEMANTYCZNYCH

| # | Źródło | Odesłanie | Co konkretnie powinno być? | Co rzeczywiście jest w tym miejscu? | Status |
|---|--------|-----------|---------------------------|------------------------------------|--------|
| 1 | § 5 ust. 4 | "Powyższe nie wyłącza..." | Postanowienia § 5 ust. 1-3 (o obowiązkach) | § 5 ust. 1-3 mówią o obowiązkach Stron — pasuje | ✅ OK |
| 2 | § 9 ust. 2 | "z zastrzeżeniem ust. 3" | § 9 ust. 3 | § 9 ust. 3 istnieje i wprowadza wyjątek | ✅ OK |
| 3 | § 14 ust. 1 | "wskazane wyżej" | Niejasne — przed § 14 jest § 13 o poufności, ale § 14 mówi o wypowiedzeniu | Brak logicznego nawiązania | ⚠️ NIEJASNE |
```

### Krok 2.3: Weryfikacja definicji

```
## WERYFIKACJA DEFINICJI

### Definicje zdefiniowane, ale NIEUŻYWANE w treści ("zombie definitions")
- "Materiały Marketingowe" (§ 1 ust. 7) — definicja jest, ale w żadnym paragrafie nie znajduję użycia. **Do usunięcia lub do wykorzystania.**

### Terminy UŻYWANE z wielkiej litery, ale NIEZDEFINIOWANE
- "Konsultant" (używany w § 8 ust. 2) — brak definicji w § 1. **Domysł:** chodzi o Specjalistę, ale to wymaga ujednolicenia. 🔴
- "Punkt Kontroli" (używany w § 11 ust. 3) — brak definicji. ⚠️

### Niespójność pisowni (terminy używane raz z wielką, raz z małą literą)
- "Specjalista" / "specjalista" — w § 1, 4, 5 z wielkiej, w § 8 ust. 4 z małej. Sprawdzić czy świadome rozróżnienie. ⚠️

### Definicje powtórzone (ten sam termin zdefiniowany dwa razy z różnym znaczeniem)
- "Strona" — zdefiniowany w § 1 ust. 1 (Usługodawca/Usługobiorca) i ponownie w § 13 ust. 2 (w kontekście postępowania sądowego "Strona Postępowania"). Niespójność. 🔴
```

### Krok 2.4: Weryfikacja spójności kwotowej, datowej, terminologicznej

```
## WERYFIKACJA SPÓJNOŚCI

### Kwoty i procenty

| Wartość | Miejsca występowania | Spójność |
|---------|---------------------|----------|
| Stawka godzinowa | Preambuła: "250 PLN" / § 3 ust. 1: "250 zł netto" / Załącznik nr 1: "260 PLN" | 🔴 NIESPÓJNE |
| Cap odpowiedzialności | § 11 ust. 2: "100% rocznego wynagrodzenia" | OK (jedno miejsce) |
| Kara umowna za zwłokę | § 9 ust. 1: "0,5% za dzień" / § 12 ust. 3: "0,5% miesięcznego wynagrodzenia" | ⚠️ Różne podstawy obliczenia — sprawdzić zamierzenie |

### Daty i terminy

| Wartość | Miejsca występowania | Spójność |
|---------|---------------------|----------|
| Data zawarcia | Preambuła: "12-05-2026" | OK |
| Początek świadczenia | § 2 ust. 3: "od 1 czerwca 2026" / Harmonogram (Załącznik nr 1): "od 15 maja 2026" | 🔴 NIESPÓJNE |
| Okres wypowiedzenia | § 14 ust. 1: "3 miesiące" / § 14 ust. 2 (przy naruszeniu): "30 dni" | OK (różne podstawy wypowiedzenia) |

### Terminologia i nazwy stron

| Termin | Lokalizacje | Spójność |
|--------|-------------|----------|
| Nazwa strony pierwszej | Preambuła: "Usługodawca" / § 4 ust. 2: "Wykonawca" / § 8: "Spółka" | 🔴 NIESPÓJNE |
| Określenie usługi | "Usługi" / "Świadczenie" / "Czynności" | ⚠️ Wymaga ujednolicenia |
```

---

## RAPORT KOŃCOWY

```
## RAPORT KOŃCOWY WERYFIKACJI ODESŁAŃ I SPÓJNOŚCI

### Statystyki
- Paragrafów: N
- Załączników wymienionych: N (w pakiecie: M, niejasnych: K)
- Odesłań jednoznacznych: N (OK: X, błędów: Y, do potwierdzenia: Z)
- Odesłań semantycznych: N
- Terminów zdefiniowanych: N (używanych: X, "zombie": Y)
- Terminów używanych niezdefiniowanych: N

### KRYTYCZNE BŁĘDY (🔴) — wymagają natychmiastowej korekty
1. § 12 ust. 1 — Błąd odesłania "kary umowne, o których mowa w § 9 ust. 3" — § 9 ust. 3 mówi o INNEJ karze (poufność, nie zwłoka). **Korekta:** zmienić na "§ 9 ust. 1" (kara za zwłokę).
2. § 15 ust. 2 — Odesłanie do nieistniejącego § 17. **Korekta:** ustalić, do czego miało odsyłać — być może § 16 (zmiana ostatnia w trakcie edycji).
3. Stawka godzinowa — niespójność 250/260 PLN między preambułą, § 3 i Załącznikiem nr 1. **Korekta:** ujednolicić.
4. Nazwa strony — niespójność "Usługodawca" / "Wykonawca" / "Spółka". **Korekta:** wybrać jedną nazwę (przy art. 750 KC — "Usługodawca").

### OSTRZEŻENIA (⚠️) — do potwierdzenia z autorem
1. § 8 ust. 4 — Załącznik nr 2 "Wzór Timesheet" wymieniony, ale nie widzę go w pakiecie. Czy istnieje?
2. § 14 ust. 1 — Niejasne odesłanie "wskazane wyżej".
3. § 9 ust. 1 vs § 12 ust. 3 — kary umowne mają różne podstawy obliczenia (% za dzień vs % miesięcznego wynagrodzenia) — świadome rozróżnienie czy błąd?

### MAŁE NIESPÓJNOŚCI (do uporządkowania)
1. Pisownia "Specjalista" / "specjalista" — ujednolicić.
2. Definicja "Materiały Marketingowe" — zdefiniowana, ale nieużywana — usunąć lub wykorzystać.
```

**STOP. Zapytaj:** *"Raport gotowy. Idziemy do poprawiania klauzul z błędami krytycznymi (workflows/popraw-fragment.md), czy najpierw chcesz przedyskutować któreś ostrzeżenia?"*

---

## Tryb skrócony — dla krótkich umów (< 15 stron)

Jeśli umowa ma < 15 stron lub < 8 paragrafów, **nie uruchamiaj pełnej procedury dwuetapowej** — wykonaj weryfikację skróconą w jednym kroku:

1. Tabela odesłań (jednoznacznych) z 5 kolumnami: lokalizacja / odesłanie / cel istnieje? / pasuje? / status
2. Lista terminów zdefiniowanych vs używanych
3. Lista niespójności kwotowych/terminologicznych

Bez STOPów. Bez Pass 1 / Pass 2.

---

## Anti-patterns które ten workflow ma wykryć (typowe błędy umów edytowanych etapowo)

1. **Renumeracja po edycji** — autor dodał nowy ustęp, ale nie przeniumerował odesłań w innych paragrafach. Częste przy współpracy wielu osób.
2. **Usunięcie + zostawienie odesłania** — autor usunął § 7 (np. uznał go za zbędny), ale w § 12 nadal jest "zgodnie z § 7".
3. **Definicja zmieniła nazwę** — termin "Pracownik" przemianowany na "Specjalista" w § 1, ale w § 8 i 11 nadal jest "Pracownik".
4. **Wartość liczbowa zmieniona tylko w jednym miejscu** — wynagrodzenie zmienione w § 3 podczas negocjacji, ale w preambule i w załączniku została stara kwota.
5. **Załącznik wymieniony, ale nieobecny** — § 4 ust. 3 odsyła do "Załącznika nr 2 (Wzór Timesheet)", ale w wykazie załączników (na końcu umowy) jest tylko Załącznik nr 1.
6. **Załącznik dołączony, ale niewymieniony w treści** — odwrotnie: w pakiecie jest Załącznik nr 4, ale w treści umowy nikt do niego nie odsyła. Bezużyteczny załącznik.
7. **Puste pole odesłania** — "zgodnie z §___" — zapomniano uzupełnić po szablonie.
8. **Cykliczne odesłania** — "§ 5 ust. 2 stosuje się odpowiednio do § 12 ust. 3, z zastrzeżeniem § 5 ust. 2" — błąd logiczny.
9. **Odesłanie do "uchylonego" ustępu** — w trakcie edycji ustęp został oznaczony "(uchylony)" lub usunięty, ale w innym miejscu nadal się do niego odsyła.
10. **Niespójność daty wstecznej/przyszłej** — preambuła z datą bieżącą + § Termin z datą sprzed dwóch miesięcy (typowy błąd kopiowania szablonu).

## Zasada operacyjna — kiedy Claude SAM uruchamia ten workflow

Bez pytania użytkownika — jeśli wykryje **co najmniej dwie** z poniższych okoliczności:
- Umowa > 15 stron lub > 5 000 słów
- > 15 paragrafów
- > 10 odesłań międzyparagrafowych
- > 3 niespójności wstępnych
- Słowa kluczowe sygnalizujące złożoność: "Załącznik", "z zastrzeżeniem", "powyższe", "wskazane w", "stosuje się odpowiednio"

W takim razie po etapie 2 pełnej analizy (checklist) Claude komunikuje:

> *"Umowa jest długa i zawiera wiele odesłań międzyparagrafowych. Modele językowe mają znaną tendencję do gubienia powiązań w długich dokumentach (attention dilution). Sugeruję dedykowaną weryfikację odesłań przed audytem ryzyk — to dwuetapowa procedura (inwentaryzacja + weryfikacja). Zajmie 5-10 minut. Akceptujesz?"*

---

## Kiedy sam Claude nie wystarczy — NotebookLM jako uzupełnienie

Doświadczenie pokazuje, że dla umów **30+ stron z bardzo gęstą siecią odesłań** nawet dwuetapowy workflow weryfikacji w standardowym Claude może przepuścić niektóre błędy. W takich wypadkach **NotebookLM (Google)** daje wyraźnie lepsze wyniki — z konkretnego powodu architektonicznego.

### Dlaczego NotebookLM jest mocniejszy w długich dokumentach

**1. Architektura RAG zamiast czystego long context** — NotebookLM indeksuje dokument na chunki z embeddings i przy każdym pytaniu retrievuje konkretne fragmenty istotne dla zapytania. Dla pytania *"co konkretnie znajduje się w § 8 ust. 3"* model dostaje **skoncentrowany kontekst** wokół § 8 ust. 3, a nie 30 stron rozproszonej uwagi.

**2. Wymuszone cytowanie ze źródła** — przy każdej odpowiedzi NotebookLM pokazuje **konkretny fragment dokumentu**, na którym opiera odpowiedź. To zmusza model do faktycznego zaglądnięcia do dokumentu, nie wnioskowania z pamięci kontekstowej. Architekturalna wersja tego, co dwuetapowy workflow Claude'a próbuje wymusić proceduralnie.

**3. Mniejszy "miss rate" przy wielu pytaniach** — w jednej sesji można zadać 20-30 pytań, każde dostaje świeży retrieval. W standardowym Claude rozmowa rośnie i kontekst się "rozcieńcza".

### Kiedy zalecać klientowi/sobie przejście do NotebookLM

Claude powinien **sam zasugerować** przejście do NotebookLM, jeśli po przejściu workflow weryfikacji w Claude:

- Umowa ma > 30 stron (próg empiryczny — powyżej tego nawet dwuetapowy proces nie wystarcza)
- Pojawiło się **podejrzenie**, że workflow nie wykrył wszystkiego (np. niespójność, którą użytkownik zauważył ręcznie, mimo że nie była w raporcie)
- Umowa zawiera > 30 odesłań międzyparagrafowych
- Umowa ma > 5 załączników, do których w treści odsyłają liczne paragrafy
- Umowa była **wielokrotnie edytowana** (negocjacje, kilka rund poprawek) — ryzyko renumeracji jest tu wysokie

### Komunikat Claude'a do użytkownika

> *"Workflow weryfikacji w Claude wykrył X błędów, ale przy umowie tej długości (Y stron, Z odesłań) zalecam jeszcze sprawdzenie w NotebookLM (Google). NotebookLM działa na architekturze RAG — indeksuje dokument i retrievuje konkretne fragmenty — co daje wyższą trafność w bardzo długich umowach. Sugerowane pytania do NotebookLM (potrzeba 2-3 wywołań):*
> *1. „Wymień wszystkie odesłania międzyparagrafowe w umowie i zweryfikuj każde."*
> *2. „Wymień wszystkie terminy używane z wielkiej litery i sprawdź, czy każdy jest zdefiniowany w § Definicje."*
> *3. „Sprawdź spójność kwot, dat i terminologii pomiędzy preambułą, treścią umowy i załącznikami."*
> *Po sprawdzeniu w NotebookLM wróć z wynikami — porównamy z moim raportem i zsyntetyzujemy pełną listę poprawek."*

### Dlaczego 2-3 wywołania w NotebookLM

NotebookLM też nie jest idealny — z dwóch powodów:

**A. Chunking nie zawsze respektuje strukturę prawną** — NotebookLM dzieli dokument heurystycznie (~500-1000 tokenów na chunk). Może rozdzielić § 8 ust. 3 od reszty § 8, co psuje kontekst lokalny. Stąd różne sformułowania pytań trafiają w różne fragmenty.

**B. Pytania o spójność globalną są antytezą RAG** — *"czy ta umowa jest wewnętrznie spójna terminologicznie"* wymaga całościowego spojrzenia, a RAG retrievuje fragmenty. Stąd pytania trzeba **dekomponować** (osobno terminologia, osobno kwoty, osobno daty) — co daje wspomniane 2-3 wywołania.

### Workflow Claude → NotebookLM → Claude

Najsilniejsza ścieżka dla bardzo długich umów:

1. **Claude (ten skill)** — pełna analiza 5-etapowa + workflow weryfikacji w Pass 1/Pass 2
2. **NotebookLM** — 2-3 wywołania dedykowane sprawdzeniu odesłań, terminologii, kwot
3. **Powrót do Claude** — synteza obu raportów, rozwiązanie konfliktów, opracowanie listy poprawek z odpowiednimi klauzulami z `references/baza-klauzul/`

NotebookLM **nie zastępuje** skilla — uzupełnia go w wąskiej, ale ważnej warstwie weryfikacji wewnętrznej spójności bardzo długich umów. Cała warstwa doktrynalna (`references/baza-wiedzy/`), klauzulowa (`references/baza-klauzul/`), stylistyczna (`references/style-redakcyjny.md`) i workflow agentowy pozostaje w Claude.
