# RODO — bezpieczeństwo danych (art. 32 RODO) i obsługa naruszeń (art. 33-34 RODO)

**Źródło:** własne opracowanie KTZR na podstawie publicznych źródeł doktrynalnych oraz orzecznictwa NSA (seria wyroków z 18.06.2025) i WSA.
**Kategoria:** doktryna i orzecznictwo — środki techniczne i organizacyjne wymagane art. 32 RODO, łańcuch notyfikacji naruszeń (art. 33-34 RODO) i odpowiedzialność za incydenty bezpieczeństwa.

> **Uwaga operacyjna dla Claude'a:** treść tego pliku to **wiedza doktrynalna** — **nie tekst do kopiowania do umowy**. Odesłania do art. 5, 32, 33, 34 RODO są tutaj kontekstem; w generowanej treści umowy/załączniku bezpieczeństwa stosuj **W6** (`style-redakcyjny.md`). Wyjątek: odesłanie do art. 32 ust. 1 lit. a-d RODO w klauzuli o konkretnych środkach spełnia funkcję W6.2 (definicja pojęć ustawowych) — zostaje.

---

## TL;DR dla Claude'a (do zapamiętania operacyjnie)

1. **Art. 32 RODO + art. 5 ust. 1 lit. f RODO** — kluczowy duet. NSA łączy naruszenie art. 32 z naruszeniem zasady integralności i poufności (art. 5 ust. 1 lit. f). Brak właściwych środków technicznych = naruszenie obu jednocześnie.
2. **NSA: środki techniczne i organizacyjne NIE są działaniem jednorazowym** — wymagają **okresowego przeglądu i aktualizacji** (wyrok NSA III OSK 455/25 z 27.02.2026 r.). Klauzula umowy musi to przewidywać.
3. **Wycieki danych = w pierwszej kolejności odpowiedzialność administratora** — nawet jeśli wystąpiły na poziomie procesora/subprocesora (orzecznictwo NSA w sprawach III OSK 2100/22, 2289/22, 2192/22).
4. **Konkretne uchybienia, które prowadziły do sankcji RODO** (z orzecznictwa NSA i WSA): brak hasła na porcie bazy indeksów, brak weryfikacji miejsca przechowywania kopii bazy, brak procedur przy migracji, brak okresowych przeglądów.
5. **Art. 32 ust. 1 lit. a-d RODO — katalog środków:** pseudonimizacja, zdolność zapewnienia poufności/integralności/dostępności/odporności, zdolność do szybkiego przywrócenia, regularne testowanie.
6. **Naruszenia (art. 33-34 RODO)** — administrator zgłasza UODO w 72h od stwierdzenia naruszenia; procesor zgłasza administratorowi **niezwłocznie** (umownie typowo 24-48h, by administrator zdążył w 72h ustawowych).
7. **ISO 27001 / SOC 2 nie są wymagane przez RODO**, ale orzecznictwo akcentuje **ciągły proces weryfikacji i doskonalenia** środków — co spójne z tymi standardami.

---

## Doktryna — szczegółowo

### 1. Art. 32 RODO — środki techniczne i organizacyjne

#### Podstawa prawna

**Art. 32 ust. 1 RODO** wskazuje obowiązek wdrożenia **odpowiednich środków technicznych i organizacyjnych**, uwzględniając:
- Stan wiedzy technicznej
- Koszt wdrożenia
- Charakter, zakres, kontekst i cele przetwarzania
- Ryzyko naruszenia praw i wolności osób fizycznych (różnego prawdopodobieństwa i wagi)

**Katalog środków z art. 32 ust. 1 lit. a-d RODO:**
- **lit. a** — pseudonimizacja i szyfrowanie danych osobowych
- **lit. b** — zdolność do ciągłego zapewnienia poufności, integralności, dostępności i odporności systemów i usług przetwarzania
- **lit. c** — zdolność do szybkiego przywrócenia dostępności danych osobowych i dostępu do nich w razie incydentu fizycznego lub technicznego
- **lit. d** — regularne testowanie, mierzenie i ocenianie skuteczności środków technicznych i organizacyjnych

**Art. 5 ust. 1 lit. f RODO** — zasada integralności i poufności. Łączy się z art. 32 — naruszenie środków = naruszenie zasady = naruszenie RODO.

#### Stanowisko orzecznicze — NSA i WSA łączą art. 32 z art. 5 ust. 1 lit. f

W sprawach dotyczących wycieków danych z chmury lub systemów informatycznych NSA i WSA konsekwentnie wskazują:

> *Brak właściwego zabezpieczenia (np. brak hasła na porcie bazy indeksów, brak weryfikacji usunięcia kopii, brak procedur przy migracji) stanowi naruszenie art. 32 i art. 5 ust. 1 lit. f RODO.*

**Wyrok NSA z 27.02.2026 r., III OSK 455/25** — kluczowa teza:

> *Odpowiednie środki techniczne i organizacyjne nie mogą być działaniem jednorazowym — wymagają okresowego przeglądu i aktualizacji.*

To bardzo istotne dla konstrukcji klauzul w umowach powierzenia: **zobowiązanie do "wdrożenia" środków raz nie wystarcza** — musi być obowiązek ciągłego utrzymywania i aktualizowania.

#### Praktyczne elementy klauzul art. 32 RODO w umowie powierzenia

Na podstawie orzecznictwa można rekomendować w umowie IT/SaaS:

**1. Konkretne środki techniczne** (z art. 32 ust. 1 lit. a-d RODO):
- Szyfrowanie danych **w spoczynku** (at rest) i **w tranzycie** (in transit)
- Silne uwierzytelnianie (MFA dla dostępu administracyjnego)
- Segmentacja sieci
- Testy penetracyjne (frequency: roczne lub po istotnych zmianach)
- Backup i disaster recovery (z testami odtwarzania)
- Pseudonimizacja gdzie zasadne
- Logi dostępu i operacji (retencja minimum 90 dni)

**2. Obowiązek ciągłego przeglądu** (kluczowa konsekwencja wyroku NSA III OSK 455/25):

> *Procesor zobowiązuje się do regularnego (nie rzadziej niż raz w roku) przeglądu i aktualizacji środków technicznych i organizacyjnych, dostosowywania ich do aktualnego stanu wiedzy technicznej oraz informowania Administratora o istotnych zmianach z [30] dniowym wyprzedzeniem.*

**3. Powiązanie z mechanizmem audytu/raportowania:**
- Raporty z zewnętrznych audytów (SOC 2 Type II, ISO 27001 audit reports)
- Wyniki testów penetracyjnych
- Raporty incident response

#### ISO 27001 / SOC 2 — niewymagane przez RODO, ale spójne

Orzecznictwo nie odwołuje się wprost do ISO 27001 ani SOC 2, ale **nacisk na ciągły proces weryfikacji** jest z tymi standardami spójny. W praktyce:

- Posiadanie SOC 2 Type II lub ISO 27001 = **mocny argument** za spełnieniem art. 28 ust. 1 RODO ("wystarczające gwarancje")
- Klient KTZR może w umowie wymagać posiadania certyfikatu i jego utrzymywania
- Brak certyfikatu nie wyłącza obowiązków — wymagana wówczas konkretna lista środków + raporty audytów

#### Wzorzec klauzuli załącznika bezpieczeństwa

> *Załącznik nr [X] — Środki Techniczne i Organizacyjne*
>
> *Procesor wdraża i utrzymuje następujące środki:*
>
> *1. Środki organizacyjne:*
>   *(a) polityka bezpieczeństwa informacji aktualizowana nie rzadziej niż raz w roku;*
>   *(b) szkolenia personelu z zakresu ochrony danych nie rzadziej niż raz w roku;*
>   *(c) procedury reagowania na incydenty bezpieczeństwa;*
>   *(d) klauzule poufności w umowach z personelem mającym dostęp do danych;*
>   *(e) Inspektor Ochrony Danych (jeśli wymaga prawo) z aktualnym kontaktem.*
>
> *2. Środki techniczne:*
>   *(a) szyfrowanie danych w tranzycie (TLS 1.2+) i spoczynku (AES-256 lub równoważne);*
>   *(b) silne uwierzytelnianie (MFA) dla dostępu administracyjnego;*
>   *(c) segmentacja sieci i firewalling;*
>   *(d) logi dostępu i operacji z retencją [90] dni, zabezpieczone przed modyfikacją;*
>   *(e) backup danych z testami odtwarzania nie rzadziej niż raz na kwartał;*
>   *(f) testy penetracyjne raz w roku oraz po istotnych zmianach w systemie;*
>   *(g) skanowanie podatności co najmniej raz w miesiącu.*
>
> *3. Certyfikaty (jeśli Procesor je posiada):*
>   *(a) ISO 27001 — aktualny certyfikat;*
>   *(b) SOC 2 Type II — aktualny raport, udostępniany Administratorowi raz w roku;*
>
> *4. Procesor zobowiązuje się do okresowego przeglądu i aktualizacji środków nie rzadziej niż raz w roku oraz każdorazowo w razie istotnej zmiany ryzyka. O istotnych zmianach Procesor informuje Administratora z [30] dniowym wyprzedzeniem.*

### 2. Naruszenia ochrony danych — art. 33-34 RODO

#### Podstawa prawna

**Art. 33 ust. 1 RODO** — w razie naruszenia ochrony danych osobowych administrator **bez zbędnej zwłoki — w miarę możliwości, nie później niż w terminie 72 godzin** — zgłasza je organowi nadzorczemu (UODO).

**Art. 33 ust. 2 RODO** — **procesor** zgłasza administratorowi **bez zbędnej zwłoki** (RODO nie wskazuje konkretnego terminu, ale praktycznie krócej niż 72h, by administrator zdążył w swoim terminie).

**Art. 33 ust. 3 RODO** — zakres informacji w zgłoszeniu administratora do UODO:
- Charakter naruszenia, w tym kategorie i przybliżona liczba osób i wpisów
- Imię i nazwisko + kontakt IOD lub osoby kontaktowej
- Możliwe konsekwencje naruszenia
- Środki zastosowane lub proponowane

**Art. 34 RODO** — zawiadomienie osób, których dane dotyczą, jeśli naruszenie powoduje **wysokie ryzyko** dla ich praw i wolności.

#### Stanowisko orzecznicze

Analizowane źródła wskazują **koncentrują się na odpowiedzialności administratora** za naruszenie, ale wyraźnie:

- Istotą spraw dotyczących wycieków jest **odpowiedzialność administratora za zgodność przetwarzania z RODO** — fakt, że naruszenie powstało na poziomie procesora, **nie zwalnia administratora**
- Administrator odpowiada również za wdrożenie i nadzór nad środkami procesora (art. 32 w zw. z art. 28)

#### Łańcuch notyfikacji — kluczowy element umowy powierzenia

Klient KTZR jako administrator ma **72h na zgłoszenie do UODO**. Jeśli incydent powstał u procesora, klient potrzebuje czasu na:
1. Analizę incydentu i jego zakresu (12-24h)
2. Przygotowanie zgłoszenia do UODO (12h)
3. Reakcję na ewentualne pytania UODO

Stąd **procesor musi zgłosić administratorowi znacznie szybciej** niż 72h — typowo 24-48h.

#### Praktyczne klauzule

**1. Termin zgłoszenia procesor → administrator:**
- **Wariant rygorystyczny**: niezwłocznie, nie później niż w 24h od stwierdzenia naruszenia
- **Wariant standardowy**: niezwłocznie, nie później niż w 48h
- **Niedopuszczalne**: "bez zbędnej zwłoki" bez konkretnego terminu (zostawia furtkę interpretacyjną)

**2. Zakres informacji w zgłoszeniu** (zbieżny z art. 33 ust. 3 RODO):
- Opis naruszenia
- Kategorie i przybliżona liczba osób / wpisów dotkniętych
- Możliwe konsekwencje
- Środki zaradcze już zastosowane lub proponowane
- Dane kontaktowe odpowiedzialnej osoby po stronie procesora

**3. Obowiązek pomocy w realizacji art. 33-34 RODO:**
- Procesor pomaga administratorowi w przygotowaniu zgłoszeń (do UODO i osób)
- Procesor pomaga w komunikacji z osobami, których dane dotyczą (jeśli administrator tego wymaga)

**4. Odpowiedzialność za opóźnienie:**
- **Kontraktowa odpowiedzialność procesora za opóźnienie lub nieprawidłowość zgłoszenia** — kluczowe, bo administrator jest rozliczany administracyjnie
- Można zastrzec karę umowną za każdą godzinę opóźnienia ponad termin umowny
- Lub indemnifikację za kary administracyjne nałożone na administratora w związku z opóźnieniem procesora

#### Wzorzec klauzuli naruszeń

> *§ X Naruszenia ochrony danych osobowych*
>
> *1. Procesor zgłasza Administratorowi każde naruszenie ochrony danych osobowych w rozumieniu art. 4 pkt 12 RODO niezwłocznie, nie później niż w terminie 24 godzin od stwierdzenia naruszenia.*
>
> *2. Zgłoszenie zawiera co najmniej:*
>   *(a) opis charakteru naruszenia, w tym — w miarę możliwości — kategorie i przybliżoną liczbę osób, których dane dotyczą, oraz kategorie i przybliżoną liczbę wpisów danych osobowych dotkniętych naruszeniem;*
>   *(b) imię i nazwisko oraz dane kontaktowe Inspektora Ochrony Danych lub innej osoby kontaktowej po stronie Procesora;*
>   *(c) opis możliwych konsekwencji naruszenia ochrony danych osobowych;*
>   *(d) opis środków zastosowanych lub proponowanych przez Procesora w celu zaradzenia naruszeniu, w tym — w stosownych przypadkach — środków w celu zminimalizowania jego ewentualnych negatywnych skutków.*
>
> *3. Jeśli przekazanie wszystkich informacji w terminie z ust. 1 nie jest możliwe, Procesor przekazuje informacje sukcesywnie, w miarę ich uzyskiwania, bez zbędnej zwłoki.*
>
> *4. Procesor współdziała z Administratorem w celu wypełnienia obowiązków administratora z art. 33-34 RODO, w tym w przygotowaniu zgłoszeń do organu nadzorczego oraz informacji do osób, których dane dotyczą.*
>
> *5. Procesor ponosi odpowiedzialność za szkody i kary administracyjne nałożone na Administratora w związku z opóźnieniem lub nieprawidłowością zgłoszenia, o którym mowa w niniejszym paragrafie, na zasadach określonych w § [Indemnifikacja RODO].*

### 3. Wnioski praktyczne z orzecznictwa wycieków danych

#### Konkretne uchybienia, które prowadziły do sankcji

Orzecznictwo wymienia konkretne naruszenia z orzecznictwa NSA i WSA, które mogą się przekładać na anti-pattern dla Claude'a przy analizie umów:

- **Brak hasła na porcie bazy indeksów** — klasyczny brak elementarnego zabezpieczenia
- **Brak weryfikacji usunięcia kopii bazy danych** — administrator nie sprawdził, czy procesor faktycznie usunął kopie
- **Brak procedur przy migracji systemów** — incydenty wycieków powstawały podczas operacji migracyjnych
- **Brak okresowych przeglądów środków bezpieczeństwa** — środki "wdrożone i zapomniane"
- **Brak weryfikacji miejsca przechowywania kopii bezpieczeństwa**

Wszystkie te uchybienia spowodowały sankcje **dla administratora**, mimo że techniczne przyczyny były po stronie procesora/subprocesora.

#### Co to znaczy dla klauzul umowy

Klauzula powinna **wprost adresować** te ryzyka:

- Obowiązek dokumentowania procesu usuwania danych (kto, kiedy, jakie wolumeny)
- Procedura przy migracji systemów (zgłaszanie administratorowi, plan, mitygacja)
- Okresowy raport stanu środków bezpieczeństwa (np. kwartalny)
- Lista lokalizacji przechowywania danych (w tym backupów) w załączniku

---

## Implikacje dla pracy nad umową

### Kiedy Claude ma sięgnąć po ten plik

- W umowie pojawia się: "środki techniczne i organizacyjne", "TOMs", "ISO 27001", "SOC 2", "bezpieczeństwo informacji", "incident response"
- W umowie pojawia się: "naruszenie ochrony danych", "data breach", "incydent bezpieczeństwa", "72 godziny", "zgłoszenie UODO"
- W trakcie analizy lub generowania załącznika bezpieczeństwa
- Klient pyta: "co dostawca musi zapewnić w zakresie bezpieczeństwa?"
- Klient pyta: "ile dostawca ma czasu na poinformowanie o wycieku?"

### Co Claude robi z tą wiedzą

1. **Przy generowaniu załącznika bezpieczeństwa:**
   - **Zawsze** wskazać konkretne środki (nie ogólniki) — pełny katalog z art. 32 ust. 1 lit. a-d RODO
   - **Zawsze** obowiązek ciągłego przeglądu i aktualizacji (kluczowe po wyroku NSA III OSK 455/25)
   - Powiązanie z certyfikatami (SOC 2, ISO 27001) jako "wystarczające gwarancje" z art. 28 ust. 1 RODO

2. **Przy generowaniu klauzuli naruszeń:**
   - Termin zgłoszenia procesor → administrator: 24h (rygorystyczny) lub 48h (standardowy), **nigdy** "bez zbędnej zwłoki" bez liczby
   - Pełen zakres informacji zbieżny z art. 33 ust. 3 RODO
   - Obowiązek współdziałania w realizacji art. 33-34 RODO
   - Klauzula odpowiedzialności za opóźnienie (link do indemnifikacji RODO)

3. **Przy analizie umowy:**
   - "Procesor wdroży odpowiednie środki bezpieczeństwa" bez konkretnej listy → 🟠 RYZYKO WYSOKIE (klauzula niewykonalna, nie spełnia art. 32 RODO operacyjnie)
   - Brak obowiązku okresowego przeglądu środków → 🟠 RYZYKO WYSOKIE (sprzeczne z wyrokiem NSA III OSK 455/25)
   - "Procesor zawiadomi Administratora o naruszeniu bez zbędnej zwłoki" bez konkretnego terminu → 🟠 RYZYKO WYSOKIE (administrator nie zdąży w 72h)
   - Termin zgłoszenia procesor → administrator dłuższy niż 48h → 🟠 RYZYKO WYSOKIE
   - Brak obowiązku procesora pomagania w przygotowaniu zgłoszenia UODO → 🟡 RYZYKO ŚREDNIE
   - Brak odpowiedzialności procesora za opóźnienie zgłoszenia → 🟡 RYZYKO ŚREDNIE
   - Brak listy lokalizacji przechowywania danych i backupów → 🟡 RYZYKO ŚREDNIE
   - "Procesor stosuje środki adekwatne do ryzyka" jako jedyna klauzula art. 32 → 🟠 RYZYKO WYSOKIE (cyrkularnie odsyła do RODO, nie konkretyzuje)

4. **Anti-pattern do natychmiastowego skorygowania:**
   - "Procesor zapewni bezpieczeństwo zgodnie z RODO" — pusta klauzula → wymień konkretne środki + obowiązek przeglądu
   - "Naruszenie zgłaszane bez zbędnej zwłoki" — dodaj konkretne 24h lub 48h
   - "Procesor stosuje ISO 27001" bez wymogu **aktualnego certyfikatu** + udostępniania → wymaga: "posiada i utrzymuje aktualny certyfikat", "udostępnia raport raz w roku"
   - Klauzula naruszeń bez obowiązku pomocy w przygotowaniu zgłoszenia do UODO → dodaj
   - Brak wskazania kategorii informacji w zgłoszeniu procesor → administrator → wymień (zgodnie z art. 33 ust. 3 RODO)

### Powiązania z innymi plikami

- Konstrukcja umowy powierzenia, kwalifikacja stron → `08-rodo-powierzenie-konstrukcja.md`
- Audyt, odpowiedzialność administracyjna (kary, regres) → `10-rodo-audyt-i-odpowiedzialnosc-administracyjna.md`
- Indemnifikacja w kontekście RODO → `07-indemnifikacja-kary-umowne.md`
- Klauzule praktyczne → `baza-klauzul/14-rodo.md`

---

## Źródła doktrynalne i orzecznicze

**Orzecznictwo NSA (kluczowe dla art. 32 RODO):**
- Wyrok NSA z 27.02.2026 r., **III OSK 455/25** — środki techniczne nie mogą być działaniem jednorazowym; obowiązek okresowego przeglądu i aktualizacji
- Seria wyroków NSA z 18.06.2025 r. (III OSK 2100/22, III OSK 2289/22, III OSK 2192/22) — odpowiedzialność administratora za środki procesora; konieczność jednego postępowania przez Prezesa UODO w razie incydentu

**Orzecznictwo WSA w Warszawie:**
- Wyrok WSA z 20.11.2024 r., **II SA/Wa 1226/24** — środki techniczne i organizacyjne w praktyce; odpowiedzialność administratora za incydenty u procesora (cyfrowe archiwum)

**Przepisy podstawowe:**
- Art. 5 ust. 1 lit. f RODO (zasada integralności i poufności)
- Art. 32 ust. 1 i 2 RODO (środki techniczne i organizacyjne, katalog z lit. a-d)
- Art. 33 RODO (zgłaszanie naruszeń organowi nadzorczemu)
- Art. 34 RODO (zawiadamianie osób, których dane dotyczą)

**Standardy spójne z orzecznictwem (niewymagane przez RODO):**
- ISO/IEC 27001:2022 — System Zarządzania Bezpieczeństwem Informacji
- SOC 2 Type II — Trust Services Criteria
- NIST Cybersecurity Framework
