# Siła wyższa, podwykonawcy (art. 474 KC) i zmiana prawa — alokacja ryzyka zewnętrznego

**Źródło:** własne opracowanie KTZR na podstawie publicznych źródeł doktrynalnych oraz orzecznictwa SN i komentarzy do KC.
**Kategoria:** doktryna i orzecznictwo — alokacja ryzyka zewnętrznego w umowach IT (siła wyższa, odpowiedzialność za podwykonawców z art. 474 KC, klauzule zmiany prawa).

> **Uwaga operacyjna dla Claude'a:** treść tego pliku to **wiedza doktrynalna** — **nie tekst do kopiowania do umowy**. Odesłania do art. 471, 473, 474, 353¹ KC są tutaj kontekstem; w generowanej treści umowy stosuj **W6** (`style-redakcyjny.md`).

---

## TL;DR dla Claude'a (do zapamiętania operacyjnie)

1. **Siła wyższa nie jest pojęciem ustawowym** — w polskim prawie definiuje się ją kontraktowo. SN dopuszcza umowne rozszerzenie odpowiedzialności także na przypadki siły wyższej (art. 473 § 1 KC), o ile okoliczności są w umowie **wyraźnie określone**.
2. **A fortiori — wyłączenie odpowiedzialności za siłę wyższą jest dopuszczalne**, ale wymaga precyzyjnej definicji + procedury notyfikacji + obowiązku mitygacji.
3. **Art. 474 KC** — dłużnik odpowiada za osoby, którymi się posługuje, jak za własne działania. **Można umownie ograniczyć tę odpowiedzialność**, z zachowaniem granicy art. 473 § 2 KC (zakaz wyłączenia za winę umyślną).
4. **Kluczowe orzeczenie: SN II CSKP 1106/22 (15.03.2023)** — w umowie leasingu dopuszczalne jest wyłączenie odpowiedzialności finansującego za niewydanie rzeczy przez zbywcę wybranego przez korzystającego. Ryzyko wyboru ponosi ten, kto wybiera kontrahenta.
5. **Wniosek dla IT:** dopuszczalne jest ograniczenie odpowiedzialności dostawcy za **wybranych przez klienta** podwykonawców (integratorzy, operator chmury wskazany przez klienta). Wymaga wyraźnego postanowienia.
6. **Stanowisko klienta KTZR:** utrzymywać pełną odpowiedzialność dostawcy za **wszystkich** podwykonawców (włącznie z dostawcą chmury), nie zgadzać się na przerzucanie ryzyka, chyba że klient ma realny wpływ na wybór.
7. **Zmiana prawa** — brak szczegółowej analizy w źródłach; konstrukcja w ramach swobody umów (art. 353¹, art. 473 KC). Pożądany kierunek: ograniczenie do zmian nakładających dodatkowe obowiązki publicznoprawne + obowiązek renegocjacji SLA/wynagrodzenia, **nie** pełne wyłączenie odpowiedzialności.

---

## Doktryna — szczegółowo

### 1. Siła wyższa

#### Podstawa prawna

**Art. 471 KC** stanowi punkt wyjścia: dłużnik odpowiada za niewykonanie/nienależyte wykonanie, **chyba że wskaże okoliczności, za które odpowiedzialności nie ponosi** — w tym siłę wyższą.

**Art. 473 § 1 KC** — strony mogą umownie **rozszerzyć** odpowiedzialność dłużnika, także na przypadki siły wyższej, jeśli tak postanowią. A fortiori — mogą również wyłączyć odpowiedzialność za skutki siły wyższej.

#### Stanowisko SN

SN wymaga, aby okoliczności rozszerzenia / ograniczenia odpowiedzialności były w umowie **"wyraźnie określone"**. Z tego wynika, że klauzula siły wyższej musi być precyzyjna — generyczne "force majeure" bez definicji jest słabe i podatne na spór interpretacyjny.

#### Elementy praktycznej klauzuli siły wyższej

1. **Definicja siły wyższej** — zdarzenie:
   - Zewnętrzne (niezależne od stron)
   - Niemożliwe do przewidzenia w chwili zawarcia umowy
   - Niemożliwe do zapobieżenia przy zachowaniu należytej staranności
   - Przykładowe katalogi: klęski żywiołowe (powódź, trzęsienie ziemi), wojna, akty terroryzmu, epidemia (z lekcji COVID-19), strajk generalny, akty władzy publicznej (sankcje, embarga, decyzje administracyjne nadzwyczajne)

2. **Wyłączenia z definicji** — co NIE jest siłą wyższą:
   - Trudności finansowe strony
   - Brak personelu strony
   - Awarie sprzętu strony (z wyjątkiem cyberataków zewnętrznych)
   - Zmiana cen rynkowych
   - Zwykłe działanie kontrahentów strony (chyba że sami doznali siły wyższej)

3. **Obowiązek notyfikacji**:
   - Termin: niezwłocznie, nie później niż w terminie X dni (typowo 3-7 dni)
   - Forma: pisemna lub mailowa
   - Zakres informacji: opis zdarzenia, prognozowany czas trwania, dotknięte obowiązki

4. **Obowiązek mitygacji** — strona dotknięta siłą wyższą ma obowiązek podejmować działania minimalizujące skutki (np. działania zastępcze, plan ciągłości biznesowej, BCP).

5. **Skutki prawne**:
   - Zawieszenie wykonywania obowiązków objętych siłą wyższą
   - Brak naliczania kar umownych w okresie zawieszenia
   - Prawo do rozwiązania umowy, jeśli siła wyższa trwa dłużej niż X dni (typowo 30-90)
   - Sposób rozliczenia w razie rozwiązania (pro rata)

### 2. Odpowiedzialność za podwykonawców — art. 474 KC

#### Podstawa prawna

**Art. 474 KC**: *"Dłużnik odpowiedzialny jest jak za własne działanie lub zaniechanie za działania i zaniechania osób, z których pomocą zobowiązanie wykonuje, jak również osób, którym wykonanie zobowiązania powierza."*

To zasada bezwzględna **z mocy ustawy** — nawet bez wyraźnej klauzuli umownej, dłużnik odpowiada za podwykonawców.

#### Stanowisko SN — możliwość umownego ograniczenia

**Wyrok SN z 15.03.2023 r., II CSKP 1106/22** (kluczowy):
- Co do zasady dłużnik (finansujący) odpowiada za zbywcę, któremu powierzył wydanie rzeczy (art. 474 KC)
- Strony mogą jednak **umownie ograniczyć tę odpowiedzialność**, w tym zawężając odpowiedzialność za działania osób trzecich
- Granica: art. 473 § 2 KC (zakaz wyłączenia za winę umyślną)
- W umowie leasingu **dopuszczalne jest wyłączenie odpowiedzialności finansującego za niewydanie rzeczy z przyczyn leżących po stronie zbywcy wybranego przez korzystającego** — gdy to korzystający ponosi ryzyko wyboru kontrahenta

#### Wniosek operacyjny dla umów IT

**Dopuszczalne jest ograniczenie odpowiedzialności dostawcy za podwykonawców**, w szczególności:
- Subcontractorzy wskazani przez klienta
- Operator chmury wybrany przez klienta
- Integratorzy systemów stron trzecich, którymi zarządza klient
- Telekomy, ISP klienta

Wymaga to:
1. **Wyraźnego postanowienia** w umowie (nie wynika z domniemania)
2. **Zachowania wyjątku dla winy umyślnej** (art. 473 § 2 KC)
3. **Precyzyjnego zdefiniowania kategorii** podwykonawców wyłączonych spod odpowiedzialności
4. **Mechanizmu kompensacyjnego** — np. cesja roszczeń dostawcy wobec tych podmiotów na rzecz klienta (jak w leasingu — cesja roszczeń finansującego wobec zbywcy)

#### Stanowisko klienta KTZR (zwykle zamawiający)

**Domyślnie — utrzymywać pełną odpowiedzialność dostawcy za podwykonawców**, "jak za własne działania". Konkretne klauzule do odrzucenia:

- ❌ "Wykonawca nie odpowiada za działania jakichkolwiek podwykonawców"
- ❌ "Wykonawca nie odpowiada za niedostępność infrastruktury chmurowej dostawców trzecich"
- ❌ "Odpowiedzialność za działania partnerów technologicznych Wykonawcy spoczywa wyłącznie na tych partnerach"

**Akceptowalne wyjątki** (gdy klient ma realny wpływ na wybór):
- ✅ "Wykonawca nie odpowiada za niedostępność dostawcy chmury wskazanego przez Zamawiającego w Załączniku nr X" — jeśli klient sam wybrał konkretnego hyperscalera
- ✅ "W przypadku korzystania z usług podwykonawcy wskazanego pisemnie przez Zamawiającego, odpowiedzialność Wykonawcy ogranicza się do staranności w doborze i nadzorze, nie obejmując samego działania podwykonawcy"

#### Cesja roszczeń jako mechanizm zabezpieczający

Jeśli wymuszone zostanie ograniczenie odpowiedzialności za podwykonawcę — zażądać **cesji roszczeń**:

> *W zakresie, w jakim Wykonawca ogranicza odpowiedzialność za działania [Podwykonawcy X], Wykonawca z chwilą zawarcia Umowy przenosi na Zamawiającego wszelkie roszczenia, jakie przysługują lub będą przysługiwać Wykonawcy wobec [Podwykonawcy X] z tytułu nienależytego wykonania umów łączących Wykonawcę z [Podwykonawcą X] w zakresie objętym niniejszą Umową.*

### 3. Zmiana prawa (change of law)

**Brak szczegółowej analizy** w dostępnych publicznych źródłach. Konstrukcja klauzuli wynika z ogólnej swobody umów:

- **Art. 353¹ KC** — strony mogą uregulować skutki zmiany prawa
- **Art. 473 KC** — mogą rozszerzyć lub ograniczyć odpowiedzialność

#### Dwie strategie konstrukcyjne

**Strategia dostawcy (pełne wyłączenie):**
> *Strony zgodnie postanawiają, że brak wykonania lub opóźnienie spowodowane zmianą prawa, której nie można było rozsądnie przewidzieć w chwili zawarcia Umowy, nie stanowi nienależytego wykonania.*

**Strategia klienta (ograniczone wyłączenie + renegocjacja):**
> *W przypadku zmiany powszechnie obowiązujących przepisów prawa, która nakłada na Wykonawcę dodatkowe obowiązki publicznoprawne wpływające na koszt świadczenia Usług, Strony przystąpią w dobrej wierze do renegocjacji odpowiednio Wynagrodzenia lub Harmonogramu. Brak osiągnięcia porozumienia w terminie 60 dni od dnia złożenia wniosku przez Wykonawcę uprawnia każdą ze Stron do wypowiedzenia Umowy z zachowaniem [okresu wypowiedzenia].*

#### Stanowisko klienta KTZR

**Domyślnie odrzucać pełne wyłączenia.** Dopuścić tylko **mechanizm renegocjacji** z obowiązkiem prowadzenia dobrej wierze + ostatecznością prawa wypowiedzenia, **nie** pełne uchylenie odpowiedzialności.

---

## Implikacje dla pracy nad umową

### Kiedy Claude ma sięgnąć po ten plik

- W umowie pojawia się: "siła wyższa", "force majeure", "podwykonawca", "subcontractor", "operator chmury", "partner technologiczny", "zmiana prawa", "change of law"
- W trakcie analizy lub generowania klauzul o odpowiedzialności — sekcja "wyłączenia"
- Klient pyta: "co jeśli dostawca powie, że to wina dostawcy chmury?"
- Klient pyta: "jak zabezpieczyć się przed COVID/wojną/atakiem hakerskim?"

### Co Claude robi z tą wiedzą

1. **Przy generowaniu klauzul z `baza-klauzul/15-sila-wyzsza.md`:**
   - Zawsze pełna definicja siły wyższej + wyłączenia katalogowe (co NIE jest siłą wyższą)
   - Zawsze obowiązek notyfikacji + mitygacji
   - Prawo wypowiedzenia po X dniach (po stronie klienta)

2. **Przy generowaniu klauzul o podwykonawcach (`baza-klauzul/11-odpowiedzialnosc.md`):**
   - Domyślnie pełna odpowiedzialność dostawcy za podwykonawców (art. 474 KC, bez modyfikacji)
   - Jeśli klient godzi się na wyjątki — wymagać cesji roszczeń + zachowania art. 473 § 2 KC

3. **Przy analizie umowy:**
   - "Wykonawca nie odpowiada za działania podwykonawców" bez ograniczenia → 🟠 RYZYKO WYSOKIE (klient bez ochrony przy łańcuchu dostaw)
   - Klauzula siły wyższej bez definicji ("force majeure events") → 🟡 RYZYKO ŚREDNIE (niepewność interpretacyjna)
   - Klauzula siły wyższej bez obowiązku notyfikacji i mitygacji → 🟡 RYZYKO ŚREDNIE
   - Pełne wyłączenie odpowiedzialności za "zmianę prawa" → 🟠 RYZYKO WYSOKIE
   - Ograniczenie odpowiedzialności za podwykonawcę bez wyjątku winy umyślnej → 🔴 RYZYKO KRYTYCZNE (sprzeczne z art. 473 § 2 KC w tej części)
   - Brak mechanizmu cesji roszczeń przy ograniczeniu odpowiedzialności za podwykonawcę → 🟡 RYZYKO ŚREDNIE

4. **Anti-pattern do natychmiastowego skorygowania:**
   - "Force majeure" bez katalogu zdarzeń → uzupełnij definicję i wyłączenia
   - "Wykonawca nie odpowiada za AWS / Azure / GCP" → zażądaj cesji roszczeń + wyjątku dla winy umyślnej + ograniczenia do wyboru klienta
   - "Strony nie odpowiadają za niewykonanie spowodowane zmianą prawa" → przepisz na mechanizm renegocjacji
   - "Siła wyższa obejmuje wszelkie zdarzenia niezależne od stron" — zbyt szerokie → ogranicz do katalogu

### Powiązania z innymi plikami

- Cap i lucrum cessans → `05-cap-lucrum-wina-umyslna.md`
- Kary umowne i odszkodowanie → `07-indemnifikacja-kary-umowne.md`
- Klauzule praktyczne → `baza-klauzul/15-sila-wyzsza.md`, `baza-klauzul/11-odpowiedzialnosc.md`

---

## Źródła doktrynalne i orzecznicze

**Orzecznictwo SN (kluczowe):**
- Wyrok SN z 15.03.2023 r., **II CSKP 1106/22**, OSNC 2023/11/111 — dopuszczalność umownego ograniczenia odpowiedzialności za osoby trzecie z art. 474 KC

**Przepisy podstawowe:**
- Art. 353¹ KC (swoboda umów)
- Art. 471 KC (odpowiedzialność za nienależyte wykonanie)
- Art. 473 § 1-2 KC (modyfikacja odpowiedzialności, granica winy umyślnej)
- Art. 474 KC (odpowiedzialność za osoby, którymi się posługuje)

