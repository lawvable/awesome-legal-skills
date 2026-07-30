# Klauzule indemnifikacyjne (hold harmless) i kary umowne — mechanizmy reparacji

**Źródło:** własne opracowanie KTZR na podstawie publicznych źródeł doktrynalnych oraz orzecznictwa SN i komentarzy do KC.
**Kategoria:** doktryna i orzecznictwo — mechanizmy reparacji szkód w umowach IT: klauzule indemnifikacyjne (zwolnienie z odpowiedzialności wobec osób trzecich) oraz kary umowne (art. 483-484 KC) i ich relacja do odszkodowania uzupełniającego.

> **Uwaga operacyjna dla Claude'a:** treść tego pliku to **wiedza doktrynalna** — **nie tekst do kopiowania do umowy**. Odesłania do art. 353¹, 429, 471, 473, 474, 483-484 KC są tutaj kontekstem; w generowanej treści umowy stosuj **W6** (`style-redakcyjny.md`). Wyjątek: odesłanie do art. 484 § 1 KC w klauzuli o odszkodowaniu uzupełniającym spełnia funkcję W6.1 (modyfikacja reżimu ustawowego) — zostaje.

---

## TL;DR dla Claude'a (do zapamiętania operacyjnie)

1. **Klauzule indemnifikacyjne (hold harmless) — w polskim prawie nienazwane**, ale dopuszczalne na podstawie swobody umów (art. 353¹ KC). Konstrukcja: jedna strona zobowiązuje się **pokryć roszczenia osób trzecich** kierowane do drugiej strony w określonych okolicznościach.
2. **Indemnifikacja ≠ wyłączenie własnej odpowiedzialności** — to przyjęcie **dodatkowego ryzyka**, więc art. 473 § 2 KC nie ma tu bezpośredniego zastosowania.
3. **Art. 484 § 1 KC**: *"Żądanie odszkodowania przenoszącego wysokość zastrzeżonej kary nie jest dopuszczalne, chyba że strony inaczej postanowiły"*. To formuła **opt-in** — odszkodowanie uzupełniające trzeba wprost zastrzec.
4. **Kara umowna może być wyłącznym środkiem ochrony (exclusive remedy)** — strony mogą umówić się, że odszkodowanie przewyższające karę jest wyłączone. Nie narusza per se art. 473 § 2 KC, ale klauzula wyłączająca nie może obejmować szkody umyślnej.
5. **Rozróżnienie niewykonania / nienależytego wykonania nie ma znaczenia dla bytu kary umownej** — w utrwalonym orzecznictwie SN każda postać naruszenia może być objęta karą.
6. **Miarkowanie kary** — art. 484 § 2 KC, sąd może obniżyć karę, gdy: (a) zobowiązanie zostało w znacznej części wykonane, (b) kara jest rażąco wygórowana. Klient KTZR powinien stosować adekwatne, proporcjonalne kary — nie symboliczne ani zaporowe.
7. **Indemnifikacja w IT** — kluczowe obszary: roszczenia z naruszenia IP (open source, patenty), naruszenia danych osobowych, naruszenia obowiązków przez podwykonawców.

---

## Doktryna — szczegółowo

### 1. Klauzule indemnifikacyjne — charakter prawny w polskim prawie

#### Brak odrębnej regulacji ustawowej

Polskie prawo cywilne nie zna pojęcia "indemnity" / "hold harmless" jako odrębnej instytucji. Jednak na podstawie **art. 353¹ KC** (swoboda umów) wynika możliwość konstruowania zobowiązań polegających na:

- **Zwolnieniu kontrahenta od odpowiedzialności wobec osób trzecich**
- **Pokryciu szkody powstałej z roszczeń osób trzecich** kierowanych do kontrahenta
- **Przejęciu długu** (art. 519 KC) lub konstrukcji świadczenia regresowego

**Art. 429 KC** (odpowiedzialność za powierzenie czynności) i **art. 474 KC** stanowią ustawowe podstawy odpowiedzialności za działania osób trzecich. Indemnifikacja to **dodatkowa, kontraktowa warstwa** ponad to.

#### Granice prawne indemnifikacji

**Art. 473 § 2 KC** nie ma bezpośredniego zastosowania do klasycznej indemnifikacji, bo:
- Indemnifikacja **nie wyłącza** własnej odpowiedzialności indemnifikującego wobec drugiej strony
- Indemnifikacja to **przyjęcie dodatkowego ryzyka** za szkody wyrządzone osobie trzeciej przez indemnifikującego

Jednak gdy indemnifikacja przewiduje pokrycie roszczeń **wynikających z umyślnego działania** drugiej strony (indemnifikowanego), klauzula ta może być uznana za sprzeczną z naturą zobowiązania lub zasadami współżycia społecznego (art. 353¹ KC). Praktyka: zastrzeż wyjątek dla winy umyślnej **indemnifikowanego**.

#### Konstrukcja klauzuli indemnifikacyjnej

Elementy obowiązkowe:

1. **Zakres roszczeń objętych zwolnieniem:**
   - Roszczenia osób trzecich (np. licencjodawców, właścicieli praw, autorów, użytkowników, organów administracji)
   - Wyroki sądowe, ugody zawarte z osobami trzecimi
   - Koszty obrony prawnej (adwokat / radca, ekspertyzy)
   - Kary administracyjne (jeśli prawo dopuszcza ich przerzucenie — w PL temat sporny, ale praktycznie tak)

2. **Trigger indemnifikacji** — okoliczność wywołująca:
   - Naruszenie praw autorskich osób trzecich przez software dostarczony przez wykonawcę
   - Naruszenie warunków licencji open source
   - Naruszenie obowiązków RODO przez wykonawcę skutkujące roszczeniami osób, których dane dotyczą
   - Działania podwykonawców wykonawcy

3. **Procedura prowadzenia sporu (defense control)** — kto kontroluje obronę:
   - **Wariant A — kontrola po stronie indemnifikującego:** indemnifikujący przejmuje obronę, sam wybiera prawnika i strategię procesową; indemnifikowany ma obowiązek współpracy. Korzystne dla indemnifikującego (kontrola kosztów).
   - **Wariant B — kontrola po stronie indemnifikowanego:** indemnifikowany prowadzi obronę, indemnifikujący zwraca koszty. Korzystne dla indemnifikowanego (autonomia procesowa).
   - **Wariant C — wspólna kontrola:** wymaga uzgodnień co do strategii. W praktyce trudna.

4. **Obowiązki informacyjne** — indemnifikowany ma obowiązek niezwłocznie poinformować indemnifikującego o roszczeniu osób trzecich (typowo 7-14 dni), pod rygorem utraty prawa do indemnifikacji w zakresie szkód powstałych z opóźnienia.

5. **Limity:**
   - **W ramach ogólnego cap'u** — korzystne dla indemnifikującego (suma roszczeń, w tym indemnifikacji, nie przekracza cap'u)
   - **Poza cap'em** — korzystne dla indemnifikowanego (indemnifikacja działa pełnoetatowo, niezależnie od cap'u; standardowo dla IP i danych osobowych w umowach IT)

#### Wzorzec klauzuli indemnifikacyjnej IP (korzystny dla klienta KTZR)

> *Wykonawca zwalnia Zamawiającego z odpowiedzialności oraz zobowiązuje się pokryć wszelkie szkody, koszty (w tym koszty pomocy prawnej) i wydatki, jakie Zamawiający poniesie wskutek roszczeń osób trzecich zarzucających naruszenie praw autorskich, patentów, znaków towarowych lub innych praw własności intelektualnej w związku z wykorzystaniem Systemu dostarczonego przez Wykonawcę. Indemnifikacja nie podlega ograniczeniu wynikającemu z § [Cap]. Zamawiający niezwłocznie, nie później niż w terminie 14 dni od otrzymania roszczenia, poinformuje Wykonawcę. Wykonawca przejmuje obronę przed roszczeniem na własny koszt, w porozumieniu z Zamawiającym.*

### 2. Kary umowne — art. 483-484 KC

#### Podstawa prawna

- **Art. 483 § 1 KC** — możliwość zastrzeżenia kary umownej za niewykonanie lub nienależyte wykonanie zobowiązania niepieniężnego
- **Art. 484 § 1 KC** — *"W razie niewykonania lub nienależytego wykonania zobowiązania kara umowna należy się wierzycielowi w zastrzeżonej na ten wypadek wysokości bez względu na wysokość poniesionej szkody. Żądanie odszkodowania przenoszącego wysokość zastrzeżonej kary nie jest dopuszczalne, chyba że strony inaczej postanowiły."*
- **Art. 484 § 2 KC** — miarkowanie kary przez sąd

#### Stanowisko SN — kluczowe orzeczenia

**Utrwalona linia orzecznicza SN (kary umownej)** — kluczowe tezy:
- **Zapłata kary umownej nie jest uzależniona od wykazania szkody** — wierzyciel nie musi udowodnić poniesionej straty
- Strony mogą **dowolnie kształtować relację kary do odszkodowania** w ramach art. 484 § 1 KC
- W orzecznictwie SN utrwalony jest pogląd, że **rozróżnienie niewykonania / nienależytego wykonania nie ma znaczenia dla bytu kary umownej** — każda postać naruszenia może być objęta karą, jeśli umowa nie stanowi inaczej

#### Cztery konstrukcje relacji kary do odszkodowania

1. **Kara wyłączna (exclusive remedy)** — *"Strony wyłączają prawo do dochodzenia odszkodowania przewyższającego wysokość kary umownej."* — domyślny reżim z art. 484 § 1 KC zdanie drugie.

2. **Kara z odszkodowaniem uzupełniającym** — *"Zapłata kary umownej nie wyłącza prawa do dochodzenia odszkodowania przewyższającego jej wysokość na zasadach ogólnych."* — opt-in z art. 484 § 1 KC zdanie drugie.

3. **Kara alternatywna** — wierzyciel wybiera albo karę umowną (bez dowodu szkody), albo odszkodowanie na zasadach ogólnych (z dowodem szkody). Rzadkie w praktyce.

4. **Kara zaliczalna** — kara umowna zalicza się na poczet odszkodowania (różnica między odszkodowaniem a karą jest dochodzona dodatkowo). Wymaga wyraźnego postanowienia.

#### Wybór konstrukcji — stanowisko klienta KTZR

**Domyślne stanowisko: kara z odszkodowaniem uzupełniającym** (konstrukcja 2). Klauzula:

> *Zapłata kary umownej, o której mowa w ust. 1, nie wyłącza prawa Zamawiającego do dochodzenia odszkodowania przewyższającego jej wysokość na zasadach ogólnych Kodeksu cywilnego (art. 484 § 1 KC).*

**Alternatywa — kara wyłączna z wysokimi stawkami** — gdy klient akceptuje wymianę "niskich kar przewyższalnych" na "wysokie kary wyłączne". Wówczas zadbać o:
- Wysoki poziom kar (realnie kompensujący potencjalne szkody)
- Wyłączenie spod kary wyłącznej szkód kluczowych (IP, dane, poufność, winę umyślną)

#### Miarkowanie kary — art. 484 § 2 KC

Sąd może obniżyć karę umowną, gdy:
- **Zobowiązanie zostało w znacznej części wykonane**
- **Kara jest rażąco wygórowana**

Stanowisko praktyczne: konstruować kary **proporcjonalne** — np. % miesięcznego wynagrodzenia za dzień zwłoki, kara katalogowa za naruszenie poufności w wysokości ekonomicznie uzasadnionej. **Unikać kar typu "100% wartości umowy za każde naruszenie poufności"** — sąd je zmiarkuje, klauzula będzie podatna na ataki.

#### Granica art. 473 § 2 KC

Klauzula wyłączająca odszkodowanie uzupełniające (kara wyłączna) **nie może obejmować szkody wyrządzonej umyślnie** — w tej części byłaby nieważna. Praktyczne ujęcie:

> *Postanowienia ust. 2 [wyłączające odszkodowanie uzupełniające] nie stosują się do szkód wyrządzonych przez Stronę umyślnie. W zakresie szkód umyślnych Zamawiający dochodzi odszkodowania na zasadach ogólnych.*

---

## Implikacje dla pracy nad umową

### Kiedy Claude ma sięgnąć po ten plik

- W umowie pojawia się: "indemnity", "indemnifikacja", "hold harmless", "zwolnienie z odpowiedzialności wobec osób trzecich"
- W umowie pojawia się: "kara umowna", "kara konwencjonalna", "penalty"
- W umowie pojawia się: "odszkodowanie uzupełniające", "exclusive remedy", "odszkodowanie przewyższające"
- Klient pyta: "jak zabezpieczyć się przed roszczeniami autorów / licencjodawców open source?"
- Klient pyta: "czy wystarczą same kary umowne, czy potrzeba też odszkodowania?"

### Co Claude robi z tą wiedzą

1. **Przy generowaniu klauzul indemnifikacyjnych:**
   - W umowach IT z przeniesieniem praw: **zawsze** klauzula indemnifikacji IP (poza cap'em)
   - W umowach z przetwarzaniem danych: klauzula indemnifikacji RODO (poza cap'em)
   - Procedura defense control: domyślnie wariant A (kontrola po stronie indemnifikującego) z obowiązkiem porozumienia
   - Obowiązek informacyjny ze strony indemnifikowanego: 14 dni, forma pisemna

2. **Przy generowaniu klauzul kar umownych (`baza-klauzul/10-kary-umowne.md`):**
   - Domyślnie konstrukcja "kara z odszkodowaniem uzupełniającym" (klauzula opt-in z art. 484 § 1 KC)
   - Kary proporcjonalne do naruszenia (% wynagrodzenia, nie zaporowe)
   - Wyjątek dla winy umyślnej (art. 473 § 2 KC zgodnie z W6.1)
   - Katalog naruszeń jako załącznik (jeśli umowa rozbudowana, np. NDA z dostępem administracyjnym)

3. **Przy analizie umowy:**
   - Kara umowna jako exclusive remedy bez wyłączenia szkody umyślnej → 🔴 RYZYKO KRYTYCZNE (nieważność w zakresie umyślności)
   - Kara umowna bez klauzuli odszkodowania uzupełniającego → 🟡 RYZYKO ŚREDNIE (klient ograniczony do wysokości kary, art. 484 § 1 KC)
   - Kary umowne zaporowe ("100% wartości umowy") → 🟠 RYZYKO WYSOKIE (podatne na miarkowanie z art. 484 § 2 KC)
   - Brak klauzuli indemnifikacyjnej IP w umowie z przeniesieniem praw → 🟠 RYZYKO WYSOKIE (klient odpowiada wobec osób trzecich za ewentualne naruszenia wykonawcy)
   - Indemnifikacja w ramach ogólnego cap'u (a nie poza nim) → 🟡 RYZYKO ŚREDNIE (ochrona iluzoryczna przy dużych roszczeniach)
   - Brak procedury defense control w klauzuli indemnifikacyjnej → 🟡 RYZYKO ŚREDNIE (niepewność co do prowadzenia sporu)

4. **Anti-pattern do natychmiastowego skorygowania:**
   - "Wykonawca zapłaci karę umowną; powyższe wyłącza dochodzenie odszkodowania uzupełniającego" + brak wyjątku winy umyślnej → dodaj wyjątek
   - "Wykonawca pokryje wszelkie szkody powstałe z naruszenia umowy" jako jedyna klauzula indemnifikacji → uzupełnij o procedurę defense control, obowiązek informacyjny, zakres
   - Kara umowna w wysokości 50% wartości umowy za każdy dzień zwłoki → 🔴 zaporowa, niemal pewne miarkowanie
   - Indemnifikacja "bez ograniczenia kwotowego" bez wyraźnego wyłączenia spod cap'u → doprecyzuj "niezależnie od § [Cap]"

### Powiązania z innymi plikami

- Cap odpowiedzialności i lucrum cessans → `05-cap-lucrum-wina-umyslna.md`
- Siła wyższa i podwykonawcy → `06-sila-wyzsza-i-podwykonawcy.md`
- Klauzule praktyczne: `baza-klauzul/10-kary-umowne.md`

---

## Źródła doktrynalne i orzecznicze

**Orzecznictwo SN (kluczowe):**
- Wyrok SN z 15.03.2023 r., **II CSKP 1106/22**, OSNC 2023/11/111 — granice ograniczenia odpowiedzialności (powiązanie z indemnifikacją)

**Przepisy podstawowe:**
- Art. 353¹ KC (swoboda umów)
- Art. 429 KC (odpowiedzialność za powierzenie czynności)
- Art. 471 KC (odpowiedzialność za nienależyte wykonanie)
- Art. 473 § 2 KC (zakaz wyłączenia za winę umyślną)
- Art. 474 KC (odpowiedzialność za osoby, którymi się posługuje)
- Art. 483 § 1 KC (kara umowna)
- Art. 484 § 1-2 KC (zasady kary umownej, miarkowanie, odszkodowanie uzupełniające)
- Art. 519 KC (przejęcie długu jako element konstrukcji indemnifikacji)
