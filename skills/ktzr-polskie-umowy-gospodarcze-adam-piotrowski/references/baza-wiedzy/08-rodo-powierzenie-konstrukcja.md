# RODO — kwalifikacja stron, umowa powierzenia (art. 28 RODO), subprocesorzy

**Źródło:** własne opracowanie KTZR na podstawie publicznych źródeł doktrynalnych oraz orzecznictwa NSA (seria wyroków z 18.06.2025 i lutego 2026), WSA w Warszawie i komentarza pod red. P. Lipińskiego (Warszawa 2021).
**Kategoria:** doktryna i orzecznictwo — kwalifikacja administrator vs procesor vs współadministrator, konstrukcja umowy powierzenia (art. 28 RODO), łańcuch subprocesorów, zwrot/usunięcie danych po zakończeniu umowy.

> **Uwaga operacyjna dla Claude'a:** treść tego pliku to **wiedza doktrynalna** — **nie tekst do kopiowania do umowy**. Odesłania do art. 4, 5, 26, 28, 32 RODO są tutaj kontekstem; w generowanej umowie powierzenia stosuj **W6** (`style-redakcyjny.md`). Wyjątek: odesłanie do art. 28 ust. 3 RODO przy klauzulach obowiązkowych umowy powierzenia spełnia funkcję W6.2 (definicja pojęcia ustawowego) i W6.3 (wyraźne włączenie reżimu) — zostaje.

---

## TL;DR dla Claude'a (do zapamiętania operacyjnie)

1. **Rozliczalność administratora (art. 5 ust. 2 RODO) jest CENTRALNA** — administrator zawsze odpowiada za zgodność przetwarzania, także gdy angażuje procesora. Może przerzucić obowiązki wykonawcze, ale **nie rozliczalność**.
2. **Trzy role:** administrator (decyduje o celach i sposobach), procesor (przetwarza w imieniu administratora), współadministrator (wspólnie decydują z innym podmiotem o celach — art. 26 RODO).
3. **Ryzyko nieprawidłowej kwalifikacji:** błędne uznanie podmiotu współdecydującego o celach za "czystego procesora" → naruszenie zasad RODO, sankcje administracyjne dla administratora.
4. **Procesor poza UE bez umowy podlegającej prawu UE/PCz** → administrator ponosi **obiektywną odpowiedzialność za wszystkie czynności tego procesora**. Linia orzecznicza NSA z 18.06.2025 jest tu jednolita (III OSK 2100/22, 2289/22, 2001/22, 1958/22, 1957/22, 2192/22).
5. **Art. 28 ust. 3 RODO — elementy obowiązkowe umowy powierzenia:** przedmiot, czas trwania, charakter i cel przetwarzania, rodzaj danych, kategorie osób, obowiązki i prawa administratora.
6. **Art. 28 ust. 1 RODO — wystarczające gwarancje** — administrator może korzystać tylko z procesorów, którzy dają wystarczające gwarancje wdrożenia odpowiednich środków technicznych i organizacyjnych. **Sama klauzula nie wystarczy** — administrator musi faktycznie zweryfikować (audyt, ankiety, raporty zewnętrzne).
7. **Subprocesorzy (art. 28 ust. 2 i 4 RODO):** preferować **zgodę szczegółową (imienną)** na kluczowych subprocesorów (hyperscaler, dostawca chmury); zgoda ogólna z prawem sprzeciwu jako fallback dla mniej krytycznych.
8. **Zwrot/usunięcie danych (art. 28 ust. 3 lit. g RODO):** wybór administratora, format umożliwiający migrację, termin, **dowody usunięcia** (certyfikat, logi).

---

## Doktryna — szczegółowo

### 1. Kwalifikacja stron — administrator / procesor / współadministrator

#### Podstawy prawne

- **Art. 4 pkt 7 RODO** — administrator: podmiot, który *"samodzielnie lub wspólnie z innymi ustala cele i sposoby przetwarzania danych osobowych"*
- **Art. 4 pkt 8 RODO** — podmiot przetwarzający: podmiot, który *"przetwarza dane osobowe w imieniu administratora"*
- **Art. 26 RODO** — współadministrowanie: wymaga wspólnego ustalenia zakresów odpowiedzialności w przejrzysty sposób
- **Art. 5 ust. 2 RODO** — zasada rozliczalności

#### Klasyczne rozróżnienie w orzecznictwie

WSA w Warszawie (II SA/Wa 1226/24) potwierdza:

- **Administrator** — np. archiwum korzystające z usług zewnętrznego dostawcy chmury pozostaje administratorem wobec swoich klientów
- **Procesor** — realizuje operacje przetwarzania "w imieniu administratora" i na podstawie umowy o powierzenie, podlegającej prawu UE lub PCz, określającej elementy z art. 28 ust. 3 RODO

#### Kluczowa teza NSA (seria wyroków z 18.06.2025 r.)

NSA w serii wyroków z 18.06.2025 r. (III OSK 2100/22, III OSK 2289/22, III OSK 2192/22) konsekwentnie przyjmuje:

> *Administrator zawsze pozostaje odpowiedzialny za zgodność przetwarzania z RODO, także gdy angażuje procesora. Może "przerzucić" część obowiązków wykonawczych, ale nie rozliczalność — ta z mocy art. 5 ust. 2 RODO obciąża administratora.*

#### Procesor spoza UE — odpowiedzialność obiektywna administratora

Jeden z najbardziej praktycznych wniosków z orzecznictwa NSA:

- Jeżeli administrator zawiera umowę powierzenia z **podmiotem spoza jurysdykcji UE** lub umowa **nie podlega prawu UE/PCz**, administrator **ponosi obiektywną odpowiedzialność za wszystkie czynności przetwarzania takiego podmiotu**
- Odpowiedzialność procesora może być oceniana **odrębnie tylko wtedy**, gdy podlega on RODO i jest realna możliwość wyegzekwowania odpowiedzialności administracyjnej

**Konsekwencja praktyczna:** umowa powierzenia z dostawcą spoza EOG bez prawa UE/PCz = pełna odpowiedzialność klienta KTZR (jako administratora) za działania tego dostawcy. Krytyczne dla SaaS amerykańskich.

#### Kwalifikacja w praktyce IT (brak kazuistyki w źródłach)

Dostępne źródła publiczne nie zawierają konkretnej kazuistyki SaaS/body leasing/hosting, ale na tle definicji można wskazać kryteria:

| Sytuacja | Rola | Uwaga |
|---|---|---|
| Dostawca SaaS przetwarza dane klienta wyłącznie do świadczenia usługi (np. hosting CRM) | **Procesor** | Standardowo |
| Dostawca chmury archiwizujący dokumenty klienta | **Procesor** | Potwierdzone w orzecznictwie WSA |
| Dostawca usług analitycznych korzystający z danych klienta do **własnej analityki/profilowania** | **Administrator (równoległy)** | Wymaga osobnej podstawy prawnej + obowiązków informacyjnych |
| Body leasing IT — specjaliści mają dostęp do danych klientów Zamawiającego, działają w imieniu Zamawiającego | **Procesor** (typowo Usługodawca) | Wymaga umowy powierzenia |
| Platforma marketplace, gdzie obie strony decydują o celach (np. portal pracy) | **Współadministratorzy** | Art. 26 RODO + porozumienie |

#### Ryzyko nieprawidłowej kwalifikacji

NSA wskazuje: w każdym przypadku naruszenia zasad przetwarzania:
- Odpowiada administrator, **chyba że** możliwe jest przypisanie odpowiedzialności innemu podmiotowi zaangażowanemu i skuteczne jej wyegzekwowanie
- Zawarcie powierzenia z podmiotem spoza UE bez instrumentu prawnego podlegającego prawu UE/PCz = **pełna odpowiedzialność administratora**

**Wniosek dla klienta KTZR:** w umowie SaaS/hosting **konkretnie opisać cele i sposoby** przetwarzania, np. zastrzec brak prawa dostawcy do wykorzystywania danych do własnych celów marketingowych/analitycznych. To **zamyka dostawcę w roli procesora**.

### 2. Umowa powierzenia — art. 28 ust. 3 RODO

#### Elementy obowiązkowe

WSA w Warszawie w sprawie cyfrowego archiwum (II SA/Wa 1226/24) szczegółowo przywołuje z art. 28 ust. 3 RODO **elementy obligatoryjne**:

1. **Przedmiot i czas trwania przetwarzania**
2. **Charakter i cel przetwarzania**
3. **Rodzaj danych osobowych**
4. **Kategorie osób, których dane dotyczą**
5. **Obowiązki i prawa administratora**

Te pięć elementów MUSI być w umowie. Brak któregokolwiek = nieprawidłowa umowa powierzenia, ryzyko sankcji.

Obok elementów wstępnych art. 28 ust. 3 RODO wymaga ujęcia **8 obligatoryjnych zobowiązań procesora** (lit. a–h): (a) przetwarzanie wyłącznie na udokumentowane polecenie ADO; (b) zapewnienie obowiązku poufności osób upoważnionych; (c) stosowanie środków z art. 32 RODO; (d) warunki angażowania podprocesorów (pisemna zgoda ADO, flow-down obowiązków); (e) pomoc ADO przy realizacji praw podmiotów danych (art. 15–22 RODO); (f) pomoc ADO przy bezpieczeństwie, zgłaszaniu naruszeń i DPIA (art. 32–36 RODO); (g) usunięcie lub zwrot danych po zakończeniu usługi (wybór ADO); (h) udostępnianie informacji na potrzeby weryfikacji + prawo audytu. **Łącznie: 5 elementów wstępnych + lit. a–h = kompletna umowa powierzenia z art. 28 ust. 3 RODO.**

#### Wystarczające gwarancje — art. 28 ust. 1 RODO

> *Administrator może korzystać wyłącznie z usług takich podmiotów przetwarzających, które zapewniają wystarczające gwarancje wdrożenia odpowiednich środków technicznych i organizacyjnych, aby przetwarzanie spełniało wymogi rozporządzenia i chroniło prawa osób, których dane dotyczą.*

**Kluczowa teza NSA z wyroku III OSK 455/25 (27.02.2026):**
- Samo posiadanie prawa audytu **nie wystarcza** — środki techniczne i organizacyjne nie mogą być działaniem jednorazowym
- Administrator musi z niego **faktycznie korzystać** lub **w inny sposób dokumentować weryfikację** (kwestionariusze, raporty zewnętrznych audytorów)
- Środki podlegają **okresowemu przeglądowi i aktualizacji**
- Brak realnej weryfikacji = naruszenie art. 28 ust. 1 w zw. z art. 32 RODO

#### Praktyczne klauzule konstrukcji umowy powierzenia

Na tle przywołanych spraw można wyprowadzić następujące wnioski co do treści:

1. **Bardzo precyzyjny opis przedmiotu i celu**:
   - Konkretnie: "przechowywanie/hosting danych klientów", "świadczenie usługi systemu kadrowego"
   - **Bez prawa procesora do rozszerzania celów poza instrukcje administratora**

2. **Wskazanie rodzajów danych i kategorii osób**:
   - Np. dane klientów końcowych, pracowników, użytkowników systemu
   - Kategorie szczególne (art. 9 RODO) — wyraźnie, jeśli dotyczą

3. **Opis środków technicznych i organizacyjnych** lub odwołanie do załącznika bezpieczeństwa (szczegóły: `09-rodo-bezpieczenstwo-i-naruszenia.md`)

4. **Klauzule współdziałania z administratorem** przy realizacji art. 32-36 RODO:
   - Bezpieczeństwo
   - DPIA (art. 35-36 RODO)
   - Zgłaszanie naruszeń (art. 33-34 RODO)
   - Kontakt z UODO

5. **Prawo do kontroli i audytu** (art. 28 ust. 3 lit. h RODO) — szczegóły w `10-rodo-audyt-i-odpowiedzialnosc-administracyjna.md`

### 3. Subprocesorzy — art. 28 ust. 2 i 4 RODO

#### Podstawa prawna

- **Art. 28 ust. 2 RODO** — procesor nie korzysta z usług innego procesora bez uprzedniej **szczegółowej lub ogólnej pisemnej zgody** administratora
- **Art. 28 ust. 4 RODO** — procesor obciążony tymi samymi obowiązkami umownymi wobec subprocesora, co administrator wobec niego

#### Stanowisko orzecznicze (pośrednie)

Analizowane źródła wskazują nie zawierają szczegółowej kazuistyki subprocesorów, ale kilka tez ma znaczenie:

- Administrator odpowiada za wybór procesora i za to, by procesor zapewniał odpowiednie środki techniczne i organizacyjne (art. 28 ust. 1, art. 32) — **pośrednio obejmuje cały łańcuch subprocesorów**
- W sprawach o wycieki danych: brak weryfikacji jednego z podmiotów w łańcuchu = naruszenie zasady poufności i sankcja **dla administratora**
- WSA i NSA kwalifikują ujawnienie danych podczas operacji na serwerach zewnętrznego dostawcy jako **naruszenie art. 5 ust. 1 lit. f RODO po stronie administratora** — mimo że de facto doszło na poziomie procesora/subprocesora

#### Konstrukcja klauzul subprocesorów

**Preferowane stanowisko klienta KTZR (jako administrator):**

1. **Zgoda szczegółowa (imienna)** na kluczowych subprocesorów:
   - Hyperscaler (AWS, Azure, GCP)
   - Dostawca chmury
   - Lista w załączniku do umowy

2. **Zgoda ogólna z prawem sprzeciwu** dla mniej krytycznych:
   - Obowiązek **uprzedniego informowania** procesora o zamiarze dodania/zmiany subprocesora
   - Termin na sprzeciw (typowo 30 dni)
   - Prawo wypowiedzenia umowy w razie sprzeciwu

3. **Łańcuch obowiązków:**
   - Procesor narzuca subprocesorom **co najmniej te same obowiązki**, co z umowy powierzenia (art. 28 ust. 4 RODO)
   - W zakresie środków bezpieczeństwa i audytu

4. **Odpowiedzialność procesora za subprocesorów:**
   - Procesor kontraktowo gwarantuje **pełną odpowiedzialność** za działania subprocesorów (w relacji A–P)
   - Bo na gruncie administracyjnym i tak odpowiedzialność spoczywa w pierwszym rzędzie na administratorze

#### Wzorzec klauzuli subprocesorów (umowa powierzenia)

> *§ X Korzystanie z dalszych podmiotów przetwarzających*
>
> *1. Procesor korzysta z dalszych podmiotów przetwarzających (Subprocesorów) wymienionych w Załączniku nr [X] (Lista Subprocesorów) za zgodą Administratora wyrażoną w niniejszej umowie.*
>
> *2. Procesor poinformuje Administratora o zamiarze zaangażowania nowego Subprocesora lub zmianie istniejącego z [30] dniowym wyprzedzeniem. Administrator może w tym terminie zgłosić uzasadniony sprzeciw.*
>
> *3. W razie zgłoszenia sprzeciwu Strony przystąpią do negocjacji rozwiązania. Brak porozumienia w terminie [30] dni uprawnia Administratora do wypowiedzenia umowy ze skutkiem na koniec miesiąca kalendarzowego, bez prawa Procesora do dochodzenia odszkodowania.*
>
> *4. Procesor zapewnia, że wszyscy Subprocesorzy zostali zobowiązani do tych samych obowiązków co Procesor na podstawie niniejszej umowy w zakresie ochrony danych osobowych.*
>
> *5. Procesor ponosi pełną odpowiedzialność wobec Administratora za działania i zaniechania Subprocesorów, jak za własne.*

### 4. Zwrot/usunięcie danych po zakończeniu umowy — art. 28 ust. 3 lit. g RODO

#### Podstawa prawna

Po zakończeniu świadczenia usług, procesor — **według wyboru administratora** — usuwa lub zwraca wszystkie dane osobowe, **chyba że** dalsze przechowywanie wymagane jest przez prawo UE/PCz.

#### Stanowisko orzecznicze (kontekstowe)

W sprawach o wycieki danych podkreślano **obowiązek administratora w zakresie weryfikacji wykonania czynności usuwania** — brak weryfikacji miejsca przechowywania kopii bazy danych = naruszenie art. 32 i art. 5 ust. 1 lit. f RODO.

#### Konstrukcja klauzuli zwrotu/usunięcia

Elementy:

1. **Wybór administratora** — usunięcie LUB zwrot (klauzula bez wyboru, narzucająca tylko usunięcie, narusza art. 28 ust. 3 lit. g RODO)
2. **Format danych** — ustrukturyzowany, powszechnie używany, czytelny maszynowo (np. CSV, JSON, XML); umożliwiający migrację (analogicznie do art. 20 RODO — prawo do przenoszenia)
3. **Termin usuwania** — typowo 30-90 dni od zakończenia umowy
4. **Los kopii bezpieczeństwa i logów** — kluczowy! Procesor zwykle ma kopie w backupach; klauzula musi przewidywać:
   - Termin usunięcia z backupów (typowo 30-180 dni; zależne od cyklu rotacji backupów)
   - Zakaz wykorzystywania danych w backupach do innych celów
5. **Dowody usunięcia**:
   - **Certyfikat usunięcia** (oświadczenie procesora)
   - **Logi systemowe** potwierdzające usunięcie
   - Prawo administratora do żądania audytu po usunięciu

#### Wzorzec klauzuli

> *§ X Zakończenie świadczenia usług*
>
> *1. Po zakończeniu świadczenia usług, Procesor — według wyboru Administratora wyrażonego w terminie [30] dni od zakończenia umowy:*
> *  (a) zwraca Administratorowi wszystkie dane osobowe w ustrukturyzowanym, powszechnie używanym formacie nadającym się do odczytu maszynowego, lub*
> *  (b) usuwa wszystkie dane osobowe.*
>
> *2. Procesor usuwa również wszystkie kopie danych (w tym kopie zapasowe) w terminie [90] dni od zakończenia umowy lub zwrotu danych, chyba że dalsze przechowywanie wymagane jest przez prawo Unii lub państwa członkowskiego. W okresie tym Procesor nie wykorzystuje danych w żadnym celu.*
>
> *3. Procesor potwierdza usunięcie pisemnym oświadczeniem ("Certyfikat Usunięcia") w terminie [7] dni od zakończenia procesu usuwania. Administrator ma prawo żądać przeprowadzenia audytu potwierdzającego usunięcie na koszt Administratora.*

---

## Implikacje dla pracy nad umową

### Kiedy Claude ma sięgnąć po ten plik

- W umowie pojawia się: "powierzenie przetwarzania", "art. 28 RODO", "data processing agreement", "DPA", "procesor", "administrator"
- W umowie pojawia się: "subprocesor", "dalszy podmiot przetwarzający", "sub-processor"
- W trakcie analizy lub generowania umowy SaaS, hosting, maintenance IT z dostępem do danych klienta
- Klient pyta: "kto jest administratorem, a kto procesorem?"
- Klient pyta: "czy dostawca może podpowierzyć dane Google'owi?"

### Co Claude robi z tą wiedzą

1. **Pierwszy ruch — kwalifikacja stron:**
   - Zapytaj klienta: czy dostawca przetwarza dane **wyłącznie w imieniu klienta**, czy ma **własne cele** (analityka, marketing, profilowanie)?
   - Jeśli wyłącznie w imieniu klienta → procesor → umowa powierzenia z art. 28 ust. 3 RODO
   - Jeśli ma własne cele → administrator równoległy lub współadministrator (art. 26 RODO)
   - Jeśli niejasne → wymagać klauzuli zamykającej dostawcę w roli procesora ("Procesor nie wykorzystuje danych do własnych celów")

2. **Drugi ruch — sprawdzenie jurysdykcji:**
   - Jeśli dostawca **poza EOG** → ostrzeż klienta o obiektywnej odpowiedzialności
   - Wymagaj klauzuli prawa UE/PCz, zastrzeżenia jurysdykcji, mechanizmu transferu (SCC, DPF)

3. **Przy generowaniu umowy powierzenia (`baza-klauzul/14-rodo.md`):**
   - **Zawsze** wszystkie 5 elementów art. 28 ust. 3 RODO (przedmiot, czas, charakter/cel, rodzaj danych, kategorie osób, obowiązki/prawa administratora)
   - Klauzule subprocesorów: zgoda szczegółowa + ogólna z prawem sprzeciwu
   - Klauzula zwrotu/usunięcia z dowodami (certyfikat, logi)
   - Klauzula odpowiedzialności procesora za subprocesorów

4. **Przy analizie umowy:**
   - Umowa powierzenia bez któregokolwiek z 5 elementów art. 28 ust. 3 → 🔴 RYZYKO KRYTYCZNE (nieprawidłowa umowa, ryzyko sankcji)
   - Brak klauzuli wyboru (zwrot LUB usunięcie) → 🟠 RYZYKO WYSOKIE (naruszenie art. 28 ust. 3 lit. g RODO)
   - "Procesor może wykorzystywać dane do własnej analityki" → 🔴 KRYTYCZNE (procesor staje się administratorem; ryzyko reklasyfikacji ról)
   - Brak listy subprocesorów + zgoda ogólna bez prawa sprzeciwu → 🟠 RYZYKO WYSOKIE (brak kontroli administratora nad łańcuchem)
   - Dostawca spoza EOG bez prawa UE/PCz → 🟠 RYZYKO WYSOKIE (obiektywna odpowiedzialność klienta)
   - Brak mechanizmu zwrotu/usunięcia danych z backupów → 🟡 RYZYKO ŚREDNIE
   - Brak certyfikatu usunięcia / dowodów → 🟡 RYZYKO ŚREDNIE
   - Procesor nie odpowiada za subprocesorów → 🟠 RYZYKO WYSOKIE (brak gwarancji łańcucha)

5. **Anti-pattern do natychmiastowego skorygowania:**
   - "Procesor może wykorzystywać Dane Osobowe do celów świadczenia usług" — zbyt ogólne, otwiera furtkę → zawęź do "wyłącznie w celu i zakresie określonych w niniejszej umowie"
   - Brak terminu usunięcia danych z backupów → dodaj termin + zakaz innych celów
   - "Subprocesorzy zgodnie z polityką procesora" — brak kontroli → dodaj listę imienną + mechanizm sprzeciwu
   - Procesor "zachowuje prawo korzystania ze zanonimizowanych danych" → sprawdź czy faktyczna anonimizacja, czy tylko pseudonimizacja (różnica zasadnicza dla RODO)

### Powiązania z innymi plikami

- Bezpieczeństwo i naruszenia (art. 32, 33-34 RODO) → `09-rodo-bezpieczenstwo-i-naruszenia.md`
- Audyt i odpowiedzialność administracyjna → `10-rodo-audyt-i-odpowiedzialnosc-administracyjna.md`
- Klauzule praktyczne → `baza-klauzul/14-rodo.md`
- Cap odpowiedzialności w kontekście RODO → `05-cap-lucrum-wina-umyslna.md`

---

## Źródła doktrynalne i orzecznicze

**Orzecznictwo NSA (seria wyroków z 18.06.2025 r. — kluczowe):**
- Wyrok NSA z 18.06.2025 r., **III OSK 2100/22**
- Wyrok NSA z 18.06.2025 r., **III OSK 2289/22**
- Wyrok NSA z 18.06.2025 r., **III OSK 2192/22**

**Orzecznictwo NSA (luty 2026):**
- Wyrok NSA z 27.02.2026 r., **III OSK 455/25**

**Orzecznictwo WSA w Warszawie:**
- Wyrok WSA w Warszawie z 20.11.2024 r., **II SA/Wa 1226/24** — środki techniczne i organizacyjne w praktyce; odpowiedzialność administratora za incydenty u procesora (cyfrowe archiwum)

**Postanowienia NSA:**
- Postanowienie NSA z 16.10.2025 r., **III OSK 2192/22** — orzeczenie uzupełniające w sprawie wyroku z 18.06.2025 r.

**Komentarze:**
- *Ogólne rozporządzenie o ochronie danych osobowych. Ustawa o ochronie danych osobowych. Wybrane przepisy sektorowe. Komentarz*, pod red. P. Lipińskiego, Warszawa 2021 — obowiązki procesora i administratora

**Przepisy podstawowe:**
- Art. 4 pkt 7-8 RODO (administrator, procesor)
- Art. 5 ust. 2 RODO (rozliczalność)
- Art. 26 RODO (współadministrowanie)
- Art. 28 RODO (powierzenie — kompletna regulacja)
- Art. 32 RODO (środki techniczne i organizacyjne)
- Ustawa z dnia 10 maja 2018 r. o ochronie danych osobowych

