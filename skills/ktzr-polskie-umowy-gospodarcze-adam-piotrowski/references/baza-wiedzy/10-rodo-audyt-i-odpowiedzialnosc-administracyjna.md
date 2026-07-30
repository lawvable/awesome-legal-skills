# RODO — audyt procesora (art. 28 ust. 3 lit. h) i odpowiedzialność administracyjna (art. 82-83 RODO)

**Źródło:** własne opracowanie KTZR na podstawie publicznych źródeł doktrynalnych oraz orzecznictwa NSA (seria wyroków z 18.06.2025 i lutego 2026), WSA i komentarza pod red. P. Lipińskiego.
**Kategoria:** doktryna i orzecznictwo — prawo audytu i kontroli procesora (art. 28 ust. 3 lit. h RODO), kary administracyjne (art. 82-83 RODO), regres między administratorem a procesorem.

> **Uwaga operacyjna dla Claude'a:** treść tego pliku to **wiedza doktrynalna** — **nie tekst do kopiowania do umowy**. Odesłania do art. 5 ust. 2, 28 ust. 3, 82-83 RODO są tutaj kontekstem; w generowanej treści umowy stosuj **W6** (`style-redakcyjny.md`). Wyjątek: odesłanie do art. 28 ust. 3 lit. h RODO przy klauzuli audytu spełnia funkcję W6.2 (definicja uprawnienia ustawowego) — zostaje.

---

## TL;DR dla Claude'a (do zapamiętania operacyjnie)

1. **Art. 28 ust. 3 lit. h RODO** — procesor *"udostępnia administratorowi wszelkie informacje niezbędne do wykazania spełnienia obowiązków oraz umożliwia przeprowadzanie audytów, w tym inspekcji"*.
2. **NSA wyraźnie: samo prawo audytu na papierze nie wystarcza** (wyrok III OSK 455/25 z 27.02.2026). Administrator musi z niego **faktycznie korzystać** lub udokumentować weryfikację w inny sposób (kwestionariusze, raporty zewnętrzne).
3. **Audyt on-site można zastąpić raportami zewnętrznych audytorów** (SOC 2, ISO 27001), o ile zapewniają realną możliwość oceny środków.
4. **Art. 5 ust. 2 RODO — rozliczalność jest centralna** — administrator zawsze odpowiada za zgodność przetwarzania, NSA potwierdza to w serii wyroków z 18.06.2025.
5. **Procesor spoza UE bez instrumentu prawa UE/PCz = administrator ponosi obiektywną odpowiedzialność** za wszystkie działania (brak realnego rozdzielenia odpowiedzialności administracyjnej).
6. **Art. 82 RODO — odpowiedzialność cywilna**: administrator i procesor są **solidarnie odpowiedzialni** wobec osób, których dane dotyczą, gdy oboje uczestniczyli w przetwarzaniu z naruszeniem RODO.
7. **Art. 83 RODO — kary administracyjne**: do 20 mln EUR lub 4% rocznego światowego obrotu (whichever is higher). Administrator i procesor mogą być karani odrębnie, ale **w pierwszej kolejności rozliczany jest administrator**.
8. **Regres A → P** — niezbędny mechanizm umowy powierzenia. Klient KTZR jako administrator musi zabezpieczyć możliwość dochodzenia od procesora zwrotu kar zapłaconych z naruszeń procesora.

---

## Doktryna — szczegółowo

### 1. Audyt procesora — art. 28 ust. 3 lit. h RODO

#### Podstawa prawna

**Art. 28 ust. 3 lit. h RODO** wymaga, by umowa powierzenia zobowiązywała procesora do:

> *Udostępniania administratorowi wszelkich informacji niezbędnych do wykazania spełnienia obowiązków określonych w niniejszym artykule oraz umożliwiania administratorowi lub audytorowi upoważnionemu przez administratora przeprowadzania audytów, w tym inspekcji, i przyczyniania się do nich.*

Procesor ma obowiązek niezwłocznie poinformować administratora, jeśli jego zdaniem instrukcja administratora narusza RODO lub inne przepisy o ochronie danych.

#### Stanowisko NSA — kluczowa teza

**Wyrok NSA z 27.02.2026 r., III OSK 455/25**:

> *Administrator nie realizował prawa kontroli, o którym mowa w art. 28 ust. 3 lit. h RODO; dopiero po incydencie wysłał ankietę do procesora. Organ (PUODO) wskazał, że było to naruszenie art. 28 ust. 1 w zw. z art. 32 RODO — administrator ma obowiązek realnego weryfikowania procesora, a nie jedynie posiadania "na papierze" klauzuli kontrolnej.*

**Konsekwencje praktyczne:**
- Sama klauzula prawa audytu w umowie **nie chroni** administratora przed sankcjami
- Administrator musi faktycznie z prawa korzystać LUB dokumentować weryfikację w inny sposób
- Procesor musi być zobowiązany do **aktywnych działań** (udostępniania informacji, raportów, wyników testów, usuwania niezgodności)

#### Audyt on-site vs raporty zewnętrznych audytorów

W relacjach B2B (SaaS, hosting, body leasing, maintenance), w praktyce dopuszczalne jest **zastąpienie części audytów on-site przez raporty zewnętrznych audytorów**:
- SOC 2 Type II — raport audytu kontroli (Trust Services Criteria)
- ISO 27001 — certyfikat + raport audytu zewnętrznego
- ISAE 3402 — raport zaufania (analog SOC 2 w jurysdykcjach europejskich)

**Warunek**: raporty muszą zapewniać **realną możliwość oceny** środków technicznych i organizacyjnych. Procesor musi je **faktycznie udostępniać administratorowi** (nie tylko twierdzić, że je posiada).

#### Praktyczne elementy klauzuli audytu

**1. Częstotliwość:**
- Standardowo: nie rzadziej niż raz w roku
- Plus każdorazowo przy **istotnej zmianie usług** lub po incydencie bezpieczeństwa
- Z możliwością audytu nadzwyczajnego przy uzasadnionym podejrzeniu naruszenia

**2. Zasady organizacyjne:**
- Zapowiedź audytu (typowo 14-30 dni)
- Godziny robocze procesora
- Zachowanie tajemnicy przedsiębiorstwa procesora (klauzula NDA dla audytora)
- Lista zakresu audytu z góry

**3. Forma audytu (do wyboru administratora):**
- Audyt on-site przez administratora lub jego pracowników
- Audyt przez **upoważnionego niezależnego audytora** wybranego przez administratora
- Raporty zewnętrznych audytów (SOC 2, ISO 27001) — z warunkiem ich aktualności (max 12 miesięcy)
- Kwestionariusze samooceny procesora (uzupełniająco)

**4. Koszty:**
- **Wariant standardowy**: standardowe audyty roczne wliczone w usługę procesora
- **Audyty nadzwyczajne**: na koszt administratora, **chyba że** ujawnią naruszenia — wówczas koszt procesora
- **Wariant alternatywny** (mniej korzystny dla administratora): wszystkie audyty na koszt administratora

**5. Obowiązki procesora po audycie:**
- Usunięcie wykrytych niezgodności w określonym terminie
- Plan naprawczy
- Raportowanie postępów

#### Wzorzec klauzuli audytu

> *§ X Prawo audytu i kontroli*
>
> *1. Administrator ma prawo, zgodnie z art. 28 ust. 3 lit. h RODO, do weryfikacji wykonywania przez Procesora obowiązków wynikających z niniejszej umowy oraz z RODO.*
>
> *2. Procesor udostępnia Administratorowi wszelkie informacje niezbędne do wykazania spełnienia obowiązków, w szczególności:*
>   *(a) aktualne raporty audytów zewnętrznych (SOC 2 Type II, ISO 27001 audit reports) — raz w roku oraz na żądanie Administratora;*
>   *(b) wyniki testów penetracyjnych — raz w roku oraz po istotnych zmianach;*
>   *(c) listę incydentów bezpieczeństwa, które miały miejsce w roku poprzedzającym, wraz z opisem reakcji.*
>
> *3. Administrator może przeprowadzić audyt on-site nie częściej niż raz w roku, w godzinach pracy Procesora, po zawiadomieniu z [14] dniowym wyprzedzeniem.*
>
> *4. Niezależnie od ust. 3, Administrator może przeprowadzić audyt nadzwyczajny w razie uzasadnionego podejrzenia naruszenia RODO przez Procesora, po zawiadomieniu z [3] dniowym wyprzedzeniem.*
>
> *5. Audyt może przeprowadzić Administrator lub upoważniony przez niego niezależny audytor. Audytor zewnętrzny zobowiązany jest do zachowania poufności na zasadach określonych w § [Poufność].*
>
> *6. Koszty audytów rocznych ponosi Procesor w ramach Wynagrodzenia. Koszty audytów nadzwyczajnych ponosi Administrator, chyba że audyt ujawni naruszenie RODO lub niniejszej umowy przez Procesora — wówczas koszty audytu ponosi Procesor.*
>
> *7. Procesor zobowiązuje się do usunięcia niezgodności wykrytych w trakcie audytu w terminie [30] dni od otrzymania raportu, chyba że Strony uzgodnią inny termin uwzględniający charakter naruszenia.*

### 2. Odpowiedzialność administracyjna — art. 82-83 RODO

#### Podstawa prawna

**Art. 5 ust. 2 RODO** — zasada rozliczalności: administrator jest odpowiedzialny za przestrzeganie zasad i musi móc to wykazać.

**Art. 82 RODO** — odpowiedzialność cywilna:
- Każda osoba, która poniosła szkodę z naruszenia RODO, ma prawo do odszkodowania od administratora lub procesora
- Administrator i procesor są **solidarnie odpowiedzialni** wobec osoby, gdy oboje uczestniczyli w przetwarzaniu z naruszeniem (art. 82 ust. 4)
- Możliwy regres między administratorem a procesorem (art. 82 ust. 5)

**Art. 83 RODO** — administracyjne kary pieniężne:
- Do **10 mln EUR** lub **2% rocznego światowego obrotu** za naruszenia z art. 83 ust. 4 (m.in. obowiązki procesora, naruszenia art. 25-39 RODO)
- Do **20 mln EUR** lub **4% rocznego światowego obrotu** za najpoważniejsze naruszenia z art. 83 ust. 5 (zasady przetwarzania, prawa osób, transfer poza EOG)

#### Stanowisko NSA — kluczowe orzeczenia z 18.06.2025

NSA w serii wyroków (III OSK 2100/22, 2289/22, 2192/22, 1958/22, 1957/22, 2001/22) szczegółowo analizuje odpowiedzialność administracyjną. Kluczowe tezy:

**1. Punkt wyjścia — art. 5 ust. 2 RODO:**
- Administrator jest odpowiedzialny za przestrzeganie zasad i musi móc to wykazać

**2. Domniemanie odpowiedzialności administratora:**
- W przypadku naruszenia zasad przetwarzania odpowiedzialność ponosi administrator
- **Wyjątek**: gdy możliwe jest przypisanie odpowiedzialności innemu podmiotowi (np. procesor, który sam narusza art. 32) i **skuteczne jej wyegzekwowanie**

**3. Procesor spoza UE:**
- Jeśli procesor nie podlega RODO/przepisom państwa członkowskiego, administrator ponosi **odpowiedzialność obiektywną** za wszystkie jego działania
- Nie ma wtedy mowy o realnym rozdzieleniu odpowiedzialności administracyjnej

**4. Skuteczność, proporcjonalność, odstraszający charakter (art. 83 ust. 2 lit. d RODO):**
- NSA akcentuje cel kary
- Przemawia to **przeciwko "fikcyjnemu" przerzucaniu** całości ryzyk administracyjnych na podmiot, którego odpowiedzialności nie da się wyegzekwować

#### Komentarz Lipińskiego

NSA odwołuje się do komentarza:

> *Ogólne rozporządzenie o ochronie danych osobowych. Ustawa o ochronie danych osobowych. Wybrane przepisy sektorowe. Komentarz*, pod red. P. Lipińskiego, Warszawa 2021.

Wskazuje, że **obowiązek wdrożenia odpowiednich środków technicznych i organizacyjnych w celu zapewnienia bezpieczeństwa spoczywa na procesorze**, ale **rozliczalność administratora z wyboru i nadzoru pozostaje**.

### 3. Regres administrator → procesor

#### Niezbędność mechanizmu w umowie powierzenia

Dostępne źródła publiczne nie zawierają szczegółowej analizy cywilnoprawnego regresu, ale wnioski są jednoznaczne:

- **Administracyjnie PUODO/NSA rozlicza przede wszystkim administratora** (a czasem również procesora)
- W konsekwencji w umowie powierzenia trzeba zbudować mechanizm regresowy:

**Klauzula regresu — elementy:**

1. **Odpowiedzialność procesora za naruszenia RODO powstałe na jego poziomie:**
   - Brak środków z art. 32
   - Brak współpracy z administratorem
   - Brak notyfikacji naruszeń
   - Naruszenie art. 28 (np. niedopuszczone wykorzystanie danych do innych celów)

2. **Obowiązek zwrotu administratorowi zapłaconych kar administracyjnych:**
   - W części odpowiadającej naruszeniom procesora
   - Z zachowaniem zakazu wyłączania odpowiedzialności za działanie umyślne (art. 473 § 2 KC — odesłanie do `05-cap-lucrum-wina-umyslna.md`)

3. **Powiązanie z indemnifikacją RODO** (`07-indemnifikacja-kary-umowne.md`):
   - Klauzula indemnifikacji **poza cap'em** odpowiedzialności
   - Zwrot kar UODO + kosztów obrony przed UODO + kosztów postępowania sądowego

#### Wzorzec klauzuli regresu

> *§ X Odpowiedzialność i regres w przypadku kar RODO*
>
> *1. Procesor odpowiada wobec Administratora za szkody i koszty (w tym koszty obrony prawnej i kosztów postępowania) wynikające z naruszenia przez Procesora obowiązków z RODO lub niniejszej umowy.*
>
> *2. W szczególności, jeśli Administrator zostanie obciążony karą administracyjną nałożoną przez organ nadzorczy (Prezesa UODO lub odpowiedni organ w innym państwie członkowskim) lub odszkodowaniem na rzecz osoby, której dane dotyczą, na podstawie art. 82-83 RODO, Procesor zwraca Administratorowi tę kwotę w zakresie, w jakim naruszenie zostało spowodowane działaniem lub zaniechaniem Procesora.*
>
> *3. Procesor zwraca również Administratorowi koszty postępowania przed organem nadzorczym oraz koszty obrony prawnej, jakie Administrator poniósł w związku z naruszeniem przez Procesora.*
>
> *4. Postanowienia ust. 1-3 nie podlegają ograniczeniu wynikającemu z § [Cap odpowiedzialności].*
>
> *5. Procesor zachowuje prawo do udziału w obronie przed organem nadzorczym lub w postępowaniu sądowym. Strony współdziałają w obronie w dobrej wierze.*

### 4. Tajemnica zawodowa radców prawnych a powierzenie

Obszar wymagający szczególnej ostrożności — kancelaria radców prawnych może być zarówno **procesorem** (jeśli klient powierza jej dane swoich klientów do obsługi prawnej), jak i **administratorem** (typowo — wtedy gdy korzysta z procesorów typu Anthropic, Google Workspace, FOTC).

Kolizja: prawo audytu wymaga ujawnienia informacji o sposobie przetwarzania, ale tajemnica zawodowa radców prawnych (art. 3 ust. 3–5 u.r.p., art. 6 KERP — ogólny obowiązek zawodowy + art. 15 KERP — tajemnica zawodowa) ogranicza ujawnienie informacji uzyskanych w związku z prowadzeniem sprawy klienta.

#### Stanowisko Claude'a przy generowaniu umów powierzenia z kancelarią prawną

- **Sygnalizuj klientowi temat jako "obszar wymagający osobnej analizy prawnej"**
- Proponuj klauzule kompromisowe (anonimizacja materiałów audytowych, audyt przez niezależnego audytora związanego tajemnicą, raporty zewnętrzne zamiast on-site)
- Sugeruj uzyskanie opinii ORA / KIRP w razie wątpliwości

---

## Implikacje dla pracy nad umową

### Kiedy Claude ma sięgnąć po ten plik

- W umowie pojawia się: "audyt", "kontrola", "inspekcja", "weryfikacja procesora", "right to audit"
- W umowie pojawia się: "kary administracyjne", "art. 82", "art. 83", "regres", "indemnifikacja RODO", "PUODO"
- W trakcie analizy lub generowania klauzul kontrolnych i odpowiedzialnościowych w umowie powierzenia
- Klient pyta: "co się stanie, jeśli UODO nałoży na nas karę z powodu wycieku u dostawcy?"
- Klient pyta: "ile razy mogę audytować dostawcę?"

### Co Claude robi z tą wiedzą

1. **Przy generowaniu klauzuli audytu:**
   - Zawsze prawo do audytu **rocznego** + **nadzwyczajnego** po incydencie
   - Akceptowalna alternatywa: raporty SOC 2 / ISO 27001 + audyt on-site rzadziej (co 2-3 lata)
   - Klauzula obowiązku procesora do usuwania niezgodności (30 dni standardowo)
   - Koszty: audyty roczne na koszt procesora w ramach wynagrodzenia; audyty nadzwyczajne na koszt administratora z warunkiem zwrotu w razie naruszeń

2. **Przy generowaniu klauzuli odpowiedzialności RODO:**
   - **Zawsze** klauzula regresu A → P
   - **Zawsze** indemnifikacja z kar UODO **poza cap'em** ogólnym (kluczowe — kary mogą być wysokie)
   - Klauzula obowiązku współdziałania w obronie przed UODO
   - Wyjątek dla winy umyślnej administratora (art. 473 § 2 KC)

3. **Przy analizie umowy:**
   - Brak klauzuli audytu → 🔴 RYZYKO KRYTYCZNE (naruszenie art. 28 ust. 3 lit. h RODO, niedopuszczalność umowy powierzenia)
   - Klauzula audytu **tylko "na papierze"** bez konkretnej procedury → 🟠 RYZYKO WYSOKIE (wyrok NSA III OSK 455/25 — nie chroni administratora)
   - Brak regresu A → P w razie kar RODO → 🟠 RYZYKO WYSOKIE (administrator zapłaci, procesor uniknie)
   - Indemnifikacja RODO w ramach ogólnego cap'u → 🟡 RYZYKO ŚREDNIE (kary mogą wielokrotnie przekroczyć cap)
   - Brak obowiązku usuwania niezgodności po audycie → 🟡 RYZYKO ŚREDNIE (audyt bez egzekwowania)
   - Procesor zachowuje wyłączne prawo decyzji o obronie przed UODO → 🟡 RYZYKO ŚREDNIE
   - Procesor spoza UE bez prawa UE/PCz → 🟠 RYZYKO WYSOKIE (obiektywna odpowiedzialność administratora)

4. **Anti-pattern do natychmiastowego skorygowania:**
   - "Administrator ma prawo audytu" bez procedury (częstotliwość, zakres, koszty) → uzupełnij
   - "Audyt na koszt administratora" bez warunku zwrotu w razie naruszeń → dodaj warunek
   - Brak terminu na usuwanie niezgodności po audycie → dodaj 30 dni
   - "Procesor odpowiada za naruszenia RODO" bez konkretnego mechanizmu regresu kar → dorzuć klauzulę regresu i indemnifikacji
   - Indemnifikacja RODO "w ramach cap'u" → przepisz na "niezależnie od cap'u"

### Powiązania z innymi plikami

- Konstrukcja umowy powierzenia, kwalifikacja stron, subprocesorzy → `08-rodo-powierzenie-konstrukcja.md`
- Bezpieczeństwo i naruszenia (art. 32, 33-34 RODO) → `09-rodo-bezpieczenstwo-i-naruszenia.md`
- Indemnifikacja i kary umowne (mechanizmy reparacji) → `07-indemnifikacja-kary-umowne.md`
- Cap odpowiedzialności (i wyłączenia spod niego dla RODO) → `05-cap-lucrum-wina-umyslna.md`
- Klauzule praktyczne → `baza-klauzul/14-rodo.md`

---

## Źródła doktrynalne i orzecznicze

**Orzecznictwo NSA (seria wyroków z 18.06.2025 r. — kluczowe dla odpowiedzialności administracyjnej):**
- Wyrok NSA z 18.06.2025 r., **III OSK 2100/22** — konieczność jednego postępowania w przypadku naruszenia ochrony danych objętego tym samym stanem faktycznym
- Wyrok NSA z 18.06.2025 r., **III OSK 2289/22** — konieczność ujednolicenia postępowania ws. naruszeń RODO — rozproszone postępowania PUODO niezgodne z prawem
- Wyrok NSA z 18.06.2025 r., **III OSK 2192/22** — odpowiedzialność administratora w kontekście procesora spoza UE; konieczność jednego, kompleksowego postępowania

**Orzecznictwo NSA (luty 2026):**
- Wyrok NSA z 27.02.2026 r., **III OSK 455/25** — środki techniczne i organizacyjne wymagają okresowego przeglądu i aktualizacji; samo prawo audytu nie wystarcza, wymaga realnej realizacji

**Postanowienia NSA:**
- Postanowienie NSA z 16.10.2025 r., **III OSK 2192/22** — orzeczenie uzupełniające do wyroku z 18.06.2025 r. w tej samej sprawie

**Komentarze:**
- *Ogólne rozporządzenie o ochronie danych osobowych. Ustawa o ochronie danych osobowych. Wybrane przepisy sektorowe. Komentarz*, pod red. P. Lipińskiego, Warszawa 2021

**Przepisy podstawowe:**
- Art. 5 ust. 2 RODO (rozliczalność)
- Art. 28 ust. 3 lit. h RODO (prawo audytu)
- Art. 82 RODO (odpowiedzialność cywilna)
- Art. 83 ust. 2-5 RODO (administracyjne kary pieniężne)

