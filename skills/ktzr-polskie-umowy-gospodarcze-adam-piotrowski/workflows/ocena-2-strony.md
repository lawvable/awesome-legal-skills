# Workflow: Ocena umowy z perspektywy drugiej strony (devil's advocate)


> _Reguły globalne: `references/rdzen-ktzr.md` (R1 cytowania · R2 bramka · R3 role · R4 profil · R5 format)._

Workflow symulujący czytanie projektu umowy / ugody przez **pełnomocnika drugiej strony**. Cel: znaleźć wszystko, co druga strona mogłaby wykorzystać przeciwko naszemu klientowi — *zanim* dokument zostanie wysłany.

**Triggery (kiedy uruchamiać):**
- "ocena drugiej strony"
- "co mogą zarzucić"
- "jak druga strona to przeczyta"
- "perspektywa kontrahenta"
- "red team"
- "devil's advocate"
- "audyt z perspektywy oponenta"
- "ataki na umowę"
- "sprawdź jak druga strona to wykorzysta"

**Kiedy uruchamiać proaktywnie:** zawsze przed wysłaniem ugody, wezwania do zapłaty, kontrpropozycji, lub umowy w wysokostawkowej negocjacji. To jest finalna kontrola przed wyjściem dokumentu z kancelarii.

---

## Krok 0: Pamięć kancelarii

Przed oceną z perspektywy drugiej strony — sprawdź czy kancelaria ma wcześniejsze informacje o kontrahencie lub jego stylu negocjacyjnym.

1. `list_categories()` — jeśli pamięć pusta: pomiń resztę kroku, przejdź do Kroku 1
2. Jeśli pamięć niepusta:
   - `recall("nazwa kontrahenta")` — historia współpracy, wcześniejsze pozycje
   - `recall("negocjacje")` — udokumentowane taktyki drugiej strony
   - `recall("precedensy")` — jak podobne sprawy się zakończyły

Wyświetl trafienia jako kontekst dla persony oponenta:

```
📋 Pamięć kancelarii — historia kontrahenta:
[wpisy o kontrahencie i historii negocjacji — wpływają na ocenę persony oponenta w Kroku 1]
```

Jeśli brak trafień — **pomiń sekcję**. Przejdź do Kroku 1.

---

## Krok 1: Określ stronę i kontekst

Zanim zaczniesz czytanie "z drugiej strony":

1. **Identyfikuj naszego klienta** — kogo reprezentujemy w tej umowie? (Wykonawca? Zamawiający? Wynajmujący? Beneficjent?)
2. **Identyfikuj drugą stronę** — kto czyta naszą umowę z drugiej strony stołu?
3. **Określ kontekst sporu/relacji** — czy jest spór otwarty? Czy negocjacja nowej współpracy? Czy umowa wykonawcza w trakcie współpracy?
4. **Określ profil pełnomocnika drugiej strony** — kancelaria duża korporacyjna (szuka literek)? Kancelaria mała ogólna (szuka oczywistego)? In-house o nastawieniu obronnym? Sam przedsiębiorca bez prawnika (szuka „dlaczego mam tyle zapłacić")?

Wynik tego kroku to **persona oponenta** — w jego buty wchodzisz w kroku 2.

---

## Krok 2: Sześć kategorii ataków

Czytaj umowę punkt po punkcie, z perspektywy oponenta, szukając w każdej z **sześciu kategorii**.

### Kategoria 1: Niekorzystne potwierdzenia (concessions)

Fragmenty, w których **nasza strona niechcąco przyznaje** fakt lub stanowisko prawne korzystne dla drugiej strony.

**Pytania kontrolne:**
- Czy umowa zawiera oświadczenie, które potwierdza zakres roszczeń lub praw drugiej strony szerzej, niż musimy?
- Czy preambuła zawiera ustalenia faktyczne, które drugą stronę mogą uzbroić w argument w przyszłym sporze?
- Czy odesłania do wcześniejszych umów / regulacji "włączają" klauzule niekorzystne dla naszego klienta?
- Czy używamy słów typu "potwierdzają", "uznają", "zgodnie z" wobec kwestii spornych?

**Sygnały ostrzegawcze:**
- *„Strony zgodnie potwierdzają, że…"* przy spornym fakcie
- *„kierując się treścią [poprzedniej umowy]"* — włącza klauzule poprzedniej umowy backdoor'em
- *„Strony nie mają wobec siebie żadnych roszczeń"* — może być wykorzystane przeciwko nam, jeśli o jakimś nie wiemy
- *„Wszystko, co przekazane do dnia podpisania, stanowi własność…"* — szeroki transfer

**Mechanizm anti-patternu:**
Klauzula preambuły zawierająca odesłanie typu *„kierując się treścią [wcześniejszej umowy]"* daje drugiej stronie argument, że konkretne klauzule wygasłej umowy (np. dotyczące przejścia praw autorskich) nadal obowiązywały w okresie po wygaśnięciu umowy pisemnej. Klasyczna poprawka: usunięcie odniesienia do całej treści lub zawężenie do *„operacyjnych zasad wykonywania świadczeń"*, bez wchodzenia w merytoryczne klauzule.

### Kategoria 2: Niejednoznaczności interpretacyjne

Słowa lub konstrukcje pozwalające oponentowi na **alternatywną interpretację** klauzuli na jego korzyść.

**Pytania kontrolne:**
- Czy używamy słów typu "odpowiednio", "stosownie", "w miarę możliwości", "rozsądny", "uzasadniony" bez doprecyzowania?
- Czy daty graniczne są jednoznaczne ("do dnia X włącznie / wyłącznie")?
- Czy zaimki referencyjne ("ten", "te", "powyższy") odsyłają jednoznacznie do jednego źródła?
- Czy kwoty są opisane jako "brutto", "netto", "z VAT", "bez VAT" — i czy jest spójność w całej umowie?
- Czy zdarzenia warunkowe są opisane konkretnie ("jeśli X" vs "w przypadku zaistnienia okoliczności")?

**Sygnały ostrzegawcze:**
- *„w terminie odpowiednim do okoliczności"* — zawsze sporne
- *„koszty zostaną pokryte"* — przez kogo, w jakim zakresie, na podstawie czego?
- *„świadczenie zostanie wykonane"* — w stronie biernej bez wskazania podmiotu

### Kategoria 3: Luki dowodowe

Brakujące zapisy, które druga strona może wykorzystać w sporze procesowym.

**Pytania kontrolne:**
- Czy moment zapłaty jest jednoznacznie ustalony? (uznanie rachunku vs obciążenie?)
- Czy mechanizm doręczeń jest opisany? (e-mail vs pismo, na jaki adres?)
- Czy są klauzule dowodowe ("oświadczenia stron stanowią pełny dowód")?
- Czy umowa wymaga konkretnych form (pisemna, dokumentowa) i czy spełniają one funkcję dowodową?
- Czy są zachowane mechanizmy potwierdzania wykonania (raporty, oświadczenia)?

**Sygnały ostrzegawcze:**
- Brak terminu na zgłoszenie zastrzeżeń (przyjmuje się że milczenie = akceptacja)
- Brak mechanizmu odbiorczego (przy umowach wdrożeniowych — bez tego nie ma podstawy do zapłaty)
- Brak adresów do doręczeń (domyślnie z komparycji, ale może się różnić)

### Kategoria 4: Sprzeczności wewnętrzne

Logiczne dziury umożliwiające drugiej stronie **wybiórczą interpretację**.

**Pytania kontrolne:**
- Czy każdy paragraf jest spójny z preambułą?
- Czy klauzule warunkujące się nawzajem (zgoda warunkowa + wygaśnięcie + zaspokojenie) tworzą zamknięty obwód?
- Czy "wyczerpanie roszczeń" w jednej klauzuli nie koliduje z "obowiązkiem zapłaty" w innej?
- Czy odesłania wewnętrzne ("§ X ust. Y") są aktualne po wszystkich edycjach?

**Sygnał ostrzegawczy (klasyczny):** klauzula wygaśnięcia umowy "w całości" + jednoczesne pozostawienie obowiązków po wygaśnięciu (klasyczny przykład — wymaga przebudowy na "wygaśnięcie w części niewykonanej").

### Kategoria 5: Błędy obliczeniowe i terminowe

Konkrety: liczby, terminy, daty.

**Pytania kontrolne:**
- Czy suma rat zgadza się z kwotą łączną?
- Czy daty terminów płatności są kompatybilne (np. III rata 31.07 + termin wygaśnięcia zgody 31.07 — kolizja!)?
- Czy liczbowo-słowne zapisy kwot się zgadzają (*„50 000 zł (słownie: pięćdziesiąt tysięcy złotych)"*)?
- Czy "do dnia X" oznacza X włącznie czy wyłącznie?
- Czy odsetki są liczone od jakiej daty (data Wezwania? wymagalność?)?

**Sygnały ostrzegawcze:**
- Suma składowych ≠ suma deklarowana
- Daty graniczne kolidujące ze sobą bez wyjaśnienia
- Brak słownego zapisu kwoty głównej

### Kategoria 6: Mechanizmy wyjścia (exit ramps)

Klauzule, które druga strona może wykorzystać do **wycofania się** z umowy lub spowolnienia wykonania.

**Pytania kontrolne:**
- Czy są klauzule typu "siła wyższa" zbyt szerokie?
- Czy "ważne powody" wypowiedzenia są skonkretyzowane czy otwarte?
- Czy mechanizmy uchylenia (np. art. 918 KC dla ugód) są ograniczone tam, gdzie mogą szkodzić?
- Czy klauzule rozwiązujące są symetryczne — i czy chcemy, by były?
- Czy są zapisy typu "do czasu spełnienia warunku", które dają drugiej stronie nieograniczoną zwłokę?

**Sygnały ostrzegawcze:**
- "Strony mogą rozwiązać umowę z ważnych powodów" bez listy zamkniętej
- Brak terminów na rozpoznanie zastrzeżeń
- Możliwość niepublicznego odstąpienia bez kar

---

## Krok 3: Generowanie raportu

Po przejściu wszystkich sześciu kategorii, wygeneruj **raport perspektywy 2. strony** w następującej strukturze:

```
## Persona oponenta
[Krótko: kto czyta, jakie jest jego motywacje, jakie ma narzędzia]

## Zidentyfikowane słabości

### P1 — krytyczne (muszą być naprawione przed wysłaniem)
1. [Lokalizacja: § X ust. Y] [Słabość] → [Atak drugiej strony] → [Rekomendacja]
2. ...

### P2 — istotne (rekomenduje się poprawić)
1. ...

### P3 — drobne (do rozważenia)
1. ...

## Pytania do klienta przed wysłaniem
[Jeśli niektóre kwestie wymagają decyzji biznesowej klienta przed naprawą]

## Ogólna ocena ryzyka
[1-3 zdania: jak ocena 2. strony wpłynie na pozycję negocjacyjną]
```

**Priorytety:**
- **P1** — słabość, którą oponent z dużym prawdopodobieństwem wykorzysta. Może to znacząco osłabić naszą pozycję w sporze. Naprawiamy zawsze.
- **P2** — słabość możliwa do wykorzystania w agresywnej negocjacji, ale wymagająca specjalisty. Rekomenduje się naprawę, choć nie blokująca.
- **P3** — słabość teoretyczna; mało prawdopodobne, że zostanie wykorzystana, ale "miło mieć" naprawione.

---

## Krok 4: Iteracja z klientem

Niektóre P1/P2 mogą wymagać **decyzji biznesowej klienta**, nie tylko prawnej (np. *„czy chcesz zaakceptować ryzyko symetryczności klauzuli niedyskredytowania w zamian za szybsze podpisanie?"*).

Po naprawach — **ponownie uruchom workflow** (krok 1–3). Iteruj do momentu, gdy zostaną tylko akceptowane P2/P3 i klient świadomie je przyjmuje.

## Krok 5: Final check przed wysłaniem

**Lekcja z praktyki:** po kilku iteracjach poprawek klient może **zapomnieć wprowadzić** ostateczne decyzje (np. zmianę „brutto" → „netto", korektę literówki w odesłaniu). Workflow nie jest ukończony, dopóki nie zweryfikujesz, że wszystkie uzgodnienia faktycznie znalazły się w dokumencie.

**Final checklist** (do przejścia tuż przed wysłaniem):

1. **Czy wszystkie uzgodnione zmiany są w dokumencie?**
   - Porównaj z listą uzgodnień (P1/P2 zatwierdzonych w iteracji)
   - Szczególnie czujnie podchodź do **drobnych zmian wartościowych** (brutto/netto, kwoty, daty) — są łatwe do przeoczenia
2. **Czy odesłania wewnętrzne są aktualne po wszystkich edycjach?**
   - Każde *„zgodnie z § X ust. Y pkt Z)"* — sprawdź, czy faktycznie wskazuje na właściwy fragment po renumeracji
   - Szczególnie po dodaniu / usunięciu ustępów: późniejsze odesłania mogą wskazywać na zły numer
3. **Czy nazewnictwo wyliczeń jest spójne?**
   - Po reformie z `(a)(b)(c)` na `1)2)3)` — sprawdź, czy odesłania używają *„pkt"* a nie *„podpunkt"* / *„lit."* (zob. `style-redakcyjny.md` warstwa 2, reguła 5)
4. **Czy nie ma duplikatów mechanizmów?**
   - Zob. `references/baza-klauzul/16-ugody.md`, anti-pattern „dublowanie mechanizmów sankcji"
   - Każdy mechanizm = jeden paragraf; jeśli dwa różne paragrafy regulują ten sam skutek, jeden jest do wycięcia
5. **Czy spójność przypadków gramatycznych przy łączeniu list?**
   - *„wraz z X oraz Y"* — X i Y muszą być w tym samym przypadku (narzędnik), nie mieszać z dopełniaczem
   - *„dochodzenia X, Y oraz Z"* — wszystkie w dopełniaczu
6. **Czy literówki w bolding / placeholderach?**
   - Rozbite pogrubienie (*„**5 000** **zł**"* zamiast *„**5 000 zł**"*) — efekt wielokrotnych edycji w Wordzie, do scalenia
   - Placeholdery dat / miejsc: spójne (5 kropek czy 4? jeden styl w całym dokumencie)
7. **Czy nazwy stron w klauzulach są zgodne z komparycją?**
   - Po wielu iteracjach mogą się pojawić warianty (*„Wykonawca"* / *„Zleceniobiorca"* / *„Strona"*) — wszystko powinno być spójne z definicją z komparycji

**Reguła operacyjna:** final check zawsze robi **osoba inna** niż autor finalnej redakcji (lub Claude, jeśli klient pracuje solo). Świeże oko wyłapuje to, czego autor już nie widzi.

---

## Anti-patterns workflowu

- **Nie myl tego z audytem ryzyk** (`audyt-ryzyk.md`). Audyt ryzyk patrzy *z naszej perspektywy* — co nam grozi w wykonaniu umowy. Ocena 2. strony patrzy *z perspektywy oponenta* — co oponent może w niej znaleźć przeciwko nam. Komplementarne, nie zamienne.
- **Nie ograniczaj się do języka prawniczego**. Pełnomocnik drugiej strony może mieć inne specjalizacje (cywilista, podatkowiec, IP) — myśl szeroko.
- **Nie traktuj klauzuli jako "bezpiecznej" tylko dlatego, że jest standardowa**. Standardowe klauzule mają najwięcej orzecznictwa = najwięcej znanych ataków.
- **Nie zapominaj o tonie**. Czasem słabość to ton (np. agresywne sformułowanie w ugodzie zaprasza do twardej kontry zamiast szybkiego podpisu).

---

## Powiązania w skill

- `workflows/audyt-ryzyk.md` — komplementarny workflow (perspektywa naszego klienta)
- `workflows/pelna-analiza.md` — szersza analiza (essentialia + spójność + ryzyka + 2. strona)
- `references/zlote-reguly.md` — Złote Reguły KTZR (kontekst nadrzędny)
- `references/baza-wiedzy/` — wiedza doktrynalna do uzasadniania ataków/obron

---

## Przykład zastosowania (schematyczny)

Przykład pokazuje strukturę procesu, nie konkretną sprawę — każdy kontekst (typ umowy, branża, role stron) generuje inny zestaw słabości i ataków, ale logika kroków pozostaje ta sama.

**Schemat typowej sekwencji:**

1. **Wejście:** projekt umowy / ugody, świeżo zredagowany przez pełnomocnika jednej ze stron, gotowy do wysłania.
2. **Persona drugiej strony:** pełnomocnik o jasnej motywacji (minimalizacja zobowiązań, maksymalizacja zatrzymanych praw, ekstrakcja informacji z preambuły).
3. **Mapowanie słabości:** dla każdej klauzuli zadaj pytania z kategorii 1-6 (concessions, niejednoznaczności, luki dowodowe, sprzeczności wewnętrzne, błędy obliczeniowe/terminowe, mechanizmy wyjścia).
4. **Klasyfikacja:** każdą słabość oznacz priorytetem **P1** (musi być poprawione przed wysłaniem) / **P2** (zalecane) / **P3** (świadomie akceptujemy).
5. **Tabela wyników:** lokalizacja → słabość → potencjalny atak → rekomendacja → priorytet.

**Co warto trzymać w głowie:**

- Czasem słabość P3 jest świadomym kompromisem (np. asymetryczna klauzula niedyskredytowania w ugodzie, gdy klient prowadzący ma mniejszą ekspozycję komunikacyjną).
- Czasem słabość P1 wynika z prostego niedopatrzenia językowego (*„brutto"* przy dwóch tytułach płatności z różnymi reżimami VAT).
- Czasem słabość P1 wynika z faktycznej luki w konstrukcji (logiczna sprzeczność: cofnięcie zgody, która formalnie nie została udzielona).

Workflow działa identycznie w ugodach kończących spory, umowach wdrożeniowych IT, body leasingach, NDA i porozumieniach exit. Zmienia się merytoryka pytań kontrolnych; struktura procesu nie.
