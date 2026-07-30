# Open source i copyleft w umowach wdrożeniowych — zabezpieczenie zamawiającego

**Źródło:** własne opracowanie KTZR na podstawie publicznych źródeł doktrynalnych oraz komentarzy A. Niewęgłowskiego do PrAut, artykułu E. Molendy-Kropielnickiej o cloud computingu i komentarzy do PZP.
**Kategoria:** doktryna i strategia kontraktowa — jak realnie zabezpieczyć zamawiającego (klienta KTZR) przed niekontrolowanym "wciągnięciem" w obowiązki copyleft.

> **Uwaga operacyjna dla Claude'a:** treść tego pliku to **wiedza doktrynalna i strategiczna** — **nie tekst do kopiowania do umowy**. Odesłania do art. 74-76 PrAut i art. 433 PZP są tutaj kontekstem; w generowanej umowie stosuj **W6**. Wyjątek: odesłanie do art. 75 ust. 2-3 PrAut w klauzuli o dekompilacji spełnia funkcję W6.3 (wyłączenie ograniczeń bezwzględnie nieważnych) — zostaje.

---

## TL;DR dla Claude'a (do zapamiętania operacyjnie)

1. **"Zakaz open source" nie jest standardem rynkowym** — w literaturze nie ma jednoznacznej tezy. Praktyka kontraktowa idzie raczej w stronę **regulacji**, nie zakazu.
2. **Dwa modele do wyboru:**
   - **"Zero open source"** — całkowity zakaz w kodzie objętym przeniesieniem praw
   - **"Bezpieczne dopuszczenie"** — zakaz tylko **copyleft** (GPL, AGPL), dopuszczenie licencji permissive (MIT, Apache, BSD) pod warunkami
3. **Zabezpieczenie wymaga ROZDZIELENIA dwóch warstw w umowie:**
   - Przeniesienie praw do **kodu wytworzonego** przez wykonawcę (pola eksploatacji, pełen tytuł prawny zamawiającego)
   - Korzystanie z **komponentów open source / osób trzecich** (licencje, bez "iluzorycznego przeniesienia")
4. **Trzy warstwy ochrony, które muszą wystąpić łącznie:**
   - **Zapewnienia (oświadczenia) wykonawcy** — brak copyleft, lista komponentów, pełne prawa do przeniesienia
   - **Klauzula indemnifikacyjna** — zwolnienie zamawiającego z odpowiedzialności wobec licencjodawców open source
   - **Kary umowne i mechanizm naprawczy** — sankcja + obowiązek usunięcia/zastąpienia
5. **Granica nieprzekraczalna**: nie można umownie wyłączyć uprawnień zamawiającego jako legalnego użytkownika z art. 75 ust. 2-3 PrAut (kopia zapasowa, testowanie, dekompilacja dla interoperacyjności) — przepisy semiimperatywne.
6. **W zamówieniach publicznych** — kary umowne muszą pozostawać w związku z przedmiotem zamówienia (art. 433 pkt 2 PZP); zakaz copyleft w kodzie objętym przeniesieniem praw jest dopuszczalny.

---

## Doktryna — szczegółowo

### 1. Punkt wyjścia — co zabezpieczamy

W umowie wdrożeniowej z perspektywy zamawiającego kluczowe są dwie płaszczyzny:

**A. Prawa do finalnego rozwiązania** — przeniesienie autorskich praw majątkowych (lub udzielenie licencji) do programu jako całości, zgodnie z PrAut, z uwzględnieniem szczególnej ochrony programów komputerowych z art. 74–76 PrAut.

**B. Ryzyka z licencji open source** — przede wszystkim ryzyko, że:
- Część kodu objęta licencją copyleft "pociągnie" za sobą obowiązek udostępnienia kodu źródłowego całości lub części rozwiązania
- Na zamawiającego zostaną "przeniesione" ograniczenia lub obowiązki z licencji, których nie akceptuje

Swoboda umów (KC) pozwala kształtować kontrakt tak, by ułożyć te ryzyka (zapewnienia, gwarancje, odpowiedzialność) — z zastrzeżeniem nienaruszania bezwzględnie obowiązujących przepisów PrAut (art. 75 ust. 2-3, art. 76 PrAut).

### 2. Dwa modele strategiczne

**Wariant "zero open source"** — umowny zakaz używania jakichkolwiek komponentów open source w kodzie, który ma być przeniesiony/objęty licencją na rzecz zamawiającego.

**Wariant "bezpiecznego dopuszczenia"** — zakaz dotyczy jedynie określonych typów licencji (zwłaszcza copyleft), pozostałe mogą być stosowane po spełnieniu warunków:
- Lista licencji dopuszczonych (permissive: MIT, Apache 2.0, BSD)
- Obowiązek raportowania komponentów
- Compliance z warunkami licencji

Z punktu widzenia PrAut **oba warianty mieszczą się w granicach swobody umów** — jest to określenie sposobu wykonania świadczenia przez wykonawcę.

**Nie wolno** umownie wyłączyć uprawnień zamawiającego jako legalnego użytkownika z art. 75 ust. 2-3 PrAut (testowanie, dekompilacja dla interoperacyjności) — wyłączenie byłoby bezwzględnie nieważne.

### 3. Struktura umowy — rozdzielenie regulacji

**3.1. Postanowienia o przeniesieniu praw / licencji do wytworzonego oprogramowania**

- Precyzyjne określenie pól eksploatacji zgodnie z art. 50 PrAut, dostosowanych do programów komputerowych (zwielokrotnianie, rozpowszechnianie, udostępnianie w sieci, chmura)
- Wskazanie, że przeniesienie praw / licencja obejmuje **całość oprogramowania wytworzonego w wykonaniu umowy**, **z wyłączeniem** wyraźnie zidentyfikowanych elementów osób trzecich (w tym open source), do których zamawiający otrzymuje jedynie stosowne licencje
- Zaznaczenie, że **wykonawca ponosi pełne ryzyko i koszty uzyskania praw/licencji od podmiotów trzecich** — zamawiający nie musi negocjować osobno licencji do komponentów

**3.2. Osobny rozdział "Oprogramowanie osób trzecich / open source"**

Tu odseparowujemy:

**A. Definicja "Komponentów Open Source":**
> "Komponenty Open Source" — jakiekolwiek elementy objęte licencją, która:
> (a) dopuszcza nieodpłatne korzystanie i modyfikację programu, oraz
> (b) nakłada na użytkownika obowiązek udostępnienia modyfikacji lub całości programu na tej samej licencji (copyleft) albo inne obowiązki udostępnieniowe.

**B. Zakazy / ograniczenia:**
- Zakaz stosowania w kodzie objętym przeniesieniem praw licencji **copyleft** wymagających udostępnienia kodu źródłowego (GNU GPL, AGPL, SSPL i podobne)
- Lub całkowity zakaz jakiegokolwiek oprogramowania open source w tej części kodu, która ma być objęta pełnym tytułem prawnym zamawiającego (jeśli wariant "zero open source")

**C. Dopuszczone komponenty open source** (jeśli wariant bezpiecznego dopuszczenia):
- Wymóg pisemnej akceptacji zamawiającego przed użyciem
- Lista komponentów, licencja, link do treści licencji
- Wykonawca zapewnia zgodność wykorzystania z warunkami licencji open source

**D. Obowiązek ujawniania i dokumentowania:**
- Bill of materials — lista wszystkich komponentów osób trzecich, w tym open source, z oznaczeniem licencji i wersji
- Obowiązek aktualizacji przy każdej zmianie wersji systemu

**E. Wyraźne rozdzielenie własności i licencji:**
- Wprost wskazać, że do komponentów open source zamawiający **nie nabywa autorskich praw majątkowych**, lecz korzysta na zasadach wynikających z licencji open source
- Przeniesienie praw z umowy dotyczy **wyłącznie tej części kodu, którą wykonawca może swobodnie przenieść**
- "Przeniesienie kodu open source" na zamawiającego jako przeniesienie praw — wyłączone; zamawiający obejmuje jedynie uprawnienia licencyjne danej licencji

### 4. Trzy warstwy ochrony kontraktowej

**Warstwa 1 — Zapewnienia (oświadczenia) wykonawcy:**

> Wykonawca oświadcza i zapewnia, że:
> (a) w częściach oprogramowania, do których przenosi na zamawiającego autorskie prawa majątkowe, nie zostały użyte komponenty open source objęte licencją copyleft ani inne licencje nakładające obowiązek udostępnienia kodu źródłowego całości lub części rozwiązania
> (b) wszelkie użyte komponenty osób trzecich są wskazane w załączniku i są wykorzystywane zgodnie z warunkami odpowiednich licencji
> (c) wykonawca posiada pełne prawa do przeniesienia praw / udzielenia licencji w zakresie określonym w umowie — tj. brak jest praw osób trzecich, które ograniczałyby takie przeniesienie

**Warstwa 2 — Klauzula indemnifikacyjna:**

> Wykonawca zobowiązuje się zwolnić zamawiającego z odpowiedzialności i pokryć wszelkie szkody, koszty (w tym koszty pomocy prawnej), jakie zamawiający poniesie wskutek roszczeń osób trzecich (w tym licencjodawców open source), zarzucających naruszenie licencji lub praw autorskich, wynikających z wykorzystania komponentów zastosowanych przez wykonawcę niezgodnie z umową lub warunkami danej licencji.

**Warstwa 3 — Kary umowne i mechanizm naprawczy:**

- **Kara umowna** za zastosowanie wbrew zakazowi komponentu copyleft w części kodu objętej przeniesieniem praw — co do zasady dopuszczalna, bezpośrednio związana z prawidłowym wykonaniem przedmiotu umowy (dostarczenie kodu wolnego od obciążeń)
- **W zamówieniach publicznych** — kary muszą pozostawać w związku z przedmiotem zamówienia (art. 433 pkt 2 PZP). Kara za naruszenie zakazu copyleft jest w tym związku
- **Mechanizm naprawczy** — zobowiązanie wykonawcy do usunięcia komponentu open source użytego sprzecznie z umową i zastąpienia go komponentem spełniającym wymogi, w określonym terminie, na własny koszt, bez przerwy w korzystaniu lub z minimalną przerwą uzgodnioną z zamawiającym

### 5. Związek z przepisami semiimperatywnymi PrAut

Projektując klauzule zabezpieczające nie wolno naruszyć przepisów PrAut o charakterze bezwzględnie obowiązującym/semiimperatywnym:

**Art. 75 ust. 2-3 PrAut** — nie można umownie odebrać zamawiającemu:
- Prawa do sporządzenia kopii zapasowej
- Prawa do testowania programu
- Prawa do dekompilacji w granicach wskazanych w przepisie

Próba "sprzedania" lub ograniczenia tych praw może prowadzić do nieważności postanowień (jako umowy o świadczenie niemożliwe lub klauzule abuzywne w relacjach konsumenckich).

**Art. 76 PrAut** — niektóre ograniczenia w zakresie modyfikacji/korzystania z programu są niedopuszczalne; próby umownego wyłączenia mogą być uznane za nieważne.

**Wniosek:** zakaz open source musi dotyczyć **sposobu przygotowania rozwiązania przez wykonawcę** i **struktury prawnej przeniesienia praw/licencji**, nie zaś prób ograniczania ustawowych uprawnień zamawiającego do korzystania z programu jako legalnego użytkownika.

### 6. Open source w chmurze — przykład ryzyka copyleft

Dostawcy chmury często korzystają z komponentów open source, w tym copyleft. Licencje copyleft wymagają udostępniania kodu źródłowego modyfikacji na tych samych warunkach.

To istotne ryzyko kontraktowe dla modeli SaaS/PaaS — wymaga uregulowania w umowach przez klauzule:
- Dot. stosowanych licencji
- Informowania o komponentach
- Zapewnień, że prawa klienta nie zostaną "zarażone" obowiązkami copyleft

Kierunek — **świadome ukształtowanie postanowień o open source**, nie bezwzględny zakaz.

---

## Implikacje dla pracy nad umową

### Kiedy Claude ma sięgnąć po ten plik

- Umowa dotyczy oprogramowania wytwarzanego na zamówienie (wdrożenie, prace rozwojowe)
- W umowie pojawia się termin: "open source", "copyleft", "GPL", "MIT", "permissive", "licencje osób trzecich"
- Klient (zamawiający) chce zabezpieczenia przed "wciągnięciem" w obowiązki copyleft
- Klient pyta "czy zakazać open source w umowie?"

### Co Claude robi z tą wiedzą

1. **Pierwszy ruch — wybór wariantu z klientem:**
   - "Zero open source" — pełen zakaz w kodzie objętym przeniesieniem praw
   - "Bezpieczne dopuszczenie" — zakaz copyleft, dopuszczenie permissive
   - **Zapytaj klienta** który wariant preferuje przed pisaniem klauzul

2. **Przy generowaniu klauzul gwarancji czystości IP (anti-copyleft):**
   - ZAWSZE rozdziel umowę na dwa rozdziały (kod wytworzony / komponenty osób trzecich)
   - ZAWSZE załącz wszystkie trzy warstwy ochrony (zapewnienia + indemnifikacja + kary)
   - Klauzula bill of materials jako załącznik
   - Gotowe klauzule: `baza-klauzul/08-prawa-autorskie-ip.md` § Zakaz komponentów copyleft

3. **Przy analizie umowy:**
   - "Zakaz open source" bez rozdzielenia warstw → 🟠 RYZYKO WYSOKIE (klauzula iluzoryczna, nie chroni przed copyleft w komponentach)
   - Brak klauzuli indemnifikacyjnej w umowie zabezpieczającej przed copyleft → 🟠 RYZYKO WYSOKIE (sankcja bez egzekucji)
   - Brak listy komponentów / bill of materials → 🟡 RYZYKO ŚREDNIE (trudność wykrycia naruszeń)
   - Próba ograniczenia dekompilacji "dla interoperacyjności" → 🔴 RYZYKO KRYTYCZNE (art. 75 ust. 2-3 PrAut, semiimperatywne, nieważność)
   - W zamówieniach publicznych: kara umowna za "ogólne naruszenie zasad jakości" bez związku z konkretnym przedmiotem → 🟠 RYZYKO WYSOKIE (art. 433 pkt 2 PZP)

4. **Anti-pattern do natychmiastowego skorygowania:**
   - "Wykonawca zobowiązuje się nie używać open source" — zbyt ogólne, nieoperacyjne → rozbij na rozdziały, dodaj definicje, listę, sankcje
   - "Zamawiający nabywa pełne prawa do całości oprogramowania, włącznie z komponentami open source" → konstrukcja iluzoryczna, nie da się przenieść tego, czego wykonawca sam nie ma; zmień na "uzyskuje uprawnienia licencyjne zgodne z licencją open source"
   - Brak zapewnień wykonawcy o czystości IP w umowie z przeniesieniem praw → dodaj warstwę 1 (oświadczenia)

### Powiązania z innymi plikami

- Pola eksploatacji, przeniesienie praw → `02-przeniesienie-praw-oprogramowanie.md`
- Prawa zależne i osobiste → `03-prawa-zalezne-osobiste-program.md`
- Klauzule praktyczne — gwarancje czystości IP (anty-copyleft), indemnifikacja: zob. `baza-klauzul/08-prawa-autorskie-ip.md`
- Procedura wydania kodu (Repository Handover) — element konstrukcyjny umów wdrożeniowych IT (`baza-klauzul/12-wypowiedzenie-exit.md` jako punkt wyjścia)

---

## Źródła doktrynalne

**Komentarze do PrAut (Niewęgłowski Adrian, WKP 2025):**
- *Prawo autorskie. Komentarz*, wyd. II, Art. 41 (zakres umowy, pola eksploatacji)
- *Prawo autorskie. Komentarz*, wyd. II, Art. 67 (licencja, charakter prawny)
- *Prawo autorskie. Komentarz*, wyd. II, Art. 75 (uprawnienia legalnego użytkownika programu — semiimperatywne)
- *Prawo autorskie. Komentarz*, wyd. II, Art. 76 (ograniczenia korzystania z programu — semiimperatywne)

**Artykuły naukowe:**
- Molenda-Kropielnicka Ewa, *Cloud Computing — zagadnienia prawne*, ZNUJ. PPWI 2013/1/109-149 (open source w chmurze, ryzyko copyleft w SaaS/PaaS)

**Prawo zamówień publicznych:**
- Wiktorowska Ewa [w:] Gawrońska-Baran A., Wiktorowska E., Wiktorowski A., Wójcik P., *Prawo zamówień publicznych. Komentarz aktualizowany*, Art. 433 (kary umowne w PZP)

**Przepisy podstawowe:**
- Art. 50, 74-76 ustawy z dnia 4 lutego 1994 r. o prawie autorskim i prawach pokrewnych
- Art. 471 i nast. KC (odpowiedzialność za nienależyte wykonanie zobowiązania)
- Art. 433 pkt 2 ustawy z dnia 11 września 2019 r. — Prawo zamówień publicznych
