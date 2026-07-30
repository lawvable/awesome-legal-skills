# Regulamin usług drogą elektroniczną — hosting, serwery, domeny, AI

**Źródło:** własne opracowanie KTZR na podstawie ustawy z dnia 18 lipca 2002 r. o świadczeniu usług drogą elektroniczną (u.ś.u.d.e.), Rozporządzenia DSA (UE) 2022/2065 oraz doktryny (Gumularz, Lubasz/Namysłowska, Susałko).
**Status:** zatwierdzono do bazy wiedzy KTZR.

## TL;DR — co Claude musi wiedzieć

1. Regulamin usług hostingowych/serwerowych/domenowych jest **ustawowo obowiązkowy** — wynika z art. 8 u.ś.u.d.e. i musi być udostępniony nieodpłatnie przed zawarciem umowy.
2. **Cztery minimalne elementy** (art. 8 ust. 3 u.ś.u.d.e.): rodzaje usług, warunki techniczne + zakaz treści bezprawnych, warunki zawarcia/rozwiązania, tryb reklamacji.
3. **Wyłączenie odpowiedzialności hostingu** — od 17.02.2024 r. podstawą jest **art. 6 DSA** (Rozp. 2022/2065), stosowany bezpośrednio. Art. 14 u.ś.u.d.e. (implementacja dyrektywy 2000/31/WE) jest uchylony w zakresie objętym DSA (art. 89 DSA) i zachowuje znaczenie wyłącznie pomocnicze poza tym zakresem. W powołaniach: wskazuj art. 6 DSA, nie art. 14 u.ś.u.d.e.
4. **DSA** nakłada dodatkowe wymogi dotyczące przejrzystości warunków, mechanizmu notice & action i uzasadniania decyzji wobec usługobiorców.
5. Usługi AI traktowane są jako szczególny wariant usługi świadczonej drogą elektroniczną — reżim u.ś.u.d.e. + DSA stosuje się do nich bez tworzenia odrębnego reżimu.
6. **Praktyczny wniosek:** regulamin pełni podwójną funkcję — wzorca umowy (art. 384 k.c.) i wykonania obowiązku ustawowego; postanowień nieudostępnionych klientowi przed zawarciem umowy nie można na niego powoływać.

---

## I. Obowiązek posiadania i udostępnienia regulaminu

Usługodawca świadczący usługi drogą elektroniczną (hosting, VPS, serwery dedykowane, domeny, SaaS, moduły AI dostępne przez sieć) ma obowiązek:
- sporządzić regulamin określający zasady świadczenia tych usług,
- udostępnić go nieodpłatnie usługobiorcy przed zawarciem umowy, w sposób pozwalający na jego pobranie, odtworzenie i utrwalenie (np. PDF w stopce strony, checkbox przy rejestracji).

Postanowień nieudostępnionych w wymagany sposób nie można skutecznie powoływać wobec usługobiorcy. Test: czy jesteś w stanie wykazać, że klient miał dostęp do regulaminu przed akceptacją?

---

## II. Minimalny zakres — cztery elementy obowiązkowe

### 1. Rodzaje i zakres usług

Wyczerpujące wyliczenie świadczonych usług: hosting współdzielony, VPS, serwery dedykowane, kolokacja, rejestracja i utrzymanie domen, certyfikaty SSL, poczta, backup, moduły AI, usługi dodatkowe. Wskazanie, które usługi są odpłatne, jaki mają charakter (ciągłe / jednorazowe) i cykl rozliczeniowy.

### 2. Warunki świadczenia — dwa składniki

**a) Wymagania techniczne:** minimalne po stronie usługobiorcy (sprzęt, łącze, konfiguracja DNS/API, protokoły). Dla modułów AI: obsługiwane formaty danych wejściowych, limity zapytań, interfejsy dostępu.

**b) Zakaz treści bezprawnych:** expressis verbis, rozwinięty do konkretnego katalogu zabronionych działań — naruszenia praw autorskich, dóbr osobistych, treści przestępcze, spam, ataki DDoS, malware, phishing, pornografia dziecięca, treści nawołujące do nienawiści. Dla usług AI: zakaz obejmuje wprost dane wejściowe przekazywane do systemu AI oraz treści generowane przy jego użyciu.

### 3. Warunki zawarcia i rozwiązania umowy

Opis momentu zawarcia umowy (rejestracja + akceptacja regulaminu / złożenie zamówienia / opłacenie faktury proforma), forma i termin wypowiedzenia przez każdą ze stron, przesłanki rozwiązania natychmiastowego (naruszenie AUP, brak płatności, zagrożenie bezpieczeństwa systemu), skutki wygaśnięcia usługi domenowej (procedura wygaśnięcia/skreślenia domeny).

### 4. Tryb postępowania reklamacyjnego

Kanały zgłoszeń (panel klienta, e-mail, formularz), zakres wymaganych danych, terminy rozpatrzenia, katalog możliwych rozstrzygnięć (usunięcie usterki, rabat, częściowy zwrot). Dla usług AI: reklamacje dotyczą parametrów technicznych (niedostępność modułu, brak API), nie merytorycznej oceny poprawności wyników modelu.

---

## III. Wyłączenie odpowiedzialności hostingu — art. 6 DSA (Rozp. 2022/2065)

> ⚠️ Podstawa prawna: od 17.02.2024 r. wyłączenie odpowiedzialności hostingu opiera się na **art. 6 DSA** (Rozp. 2022/2065), stosowanym bezpośrednio jako lex posterior do art. 14 u.ś.u.d.e. (art. 89 DSA). W powołaniach regulaminowych wskazuj art. 6 DSA; art. 14 u.ś.u.d.e. — tylko pomocniczo poza zakresem DSA.

Usługodawca nie ponosi odpowiedzialności za przechowywane przez usługobiorcę dane, jeżeli:
- nie wie o ich bezprawnym charakterze,
- po uzyskaniu wiarygodnej wiadomości lub urzędowego zawiadomienia niezwłocznie uniemożliwi do nich dostęp.

**Jak to prawidłowo realizować w regulaminie:**
- Wpisz wprost, że usługodawca nie sprawuje ogólnego nadzoru nad treściami klienta.
- Zastrzeż prawo do dobrowolnego monitorowania i moderacji — korzystanie z tego prawa nie znosi wyłączenia odpowiedzialności.
- Zaprojektuj procedurę notice & action: kanał zgłoszeń, wymagane informacje, terminy reakcji, obowiązek powiadomienia usługobiorcy przed blokowaniem treści (chyba że pilność na to nie pozwala).
- Dla AI: wyłączenie obejmuje treści generowane z użyciem AI przechowywane na infrastrukturze usługodawcy.

**⚠️ Pułapka:** regulamin, który deklaruje brak nadzoru, a jednocześnie zawiera mechanizmy aktywnego filtrowania, może skutkować utratą przywileju wyłączenia — spójność jest kluczowa.

---

## IV. Wymagania DSA — co i jak dodać

Rozporządzenie DSA (2022/2065) nakłada na dostawców usług hostingu dodatkowe wymogi, uzupełniające u.ś.u.d.e.:

### Przejrzyste warunki korzystania

Wszelkie ograniczenia dotyczące informacji przekazywanych przez odbiorców (limity, zakazy, moderacja) muszą być opisane w regulaminie w sposób jasny, konkretny i zrozumiały dla przeciętnego odbiorcy. Bez żargonu. Wymóg ten jest szczególnie istotny przy klauzulach moderacyjnych i AUP dla AI.

### Mechanizm notice & action

Regulamin musi określać:
- sposób składania zgłoszeń o treściach nielegalnych (adres e-mail / formularz),
- minimalną zawartość zgłoszenia (opis treści, podstawa prawna bezprawności, dane zgłaszającego),
- terminy i sposób reakcji usługodawcy.

### Uzasadnianie decyzji ograniczających

Przy usuwaniu treści, zawieszaniu konta lub ograniczaniu usługi z powodu naruszenia regulaminu, DSA wymaga przekazania usługobiorcy zrozumiałego uzasadnienia — jakie postanowienie naruszył, na czym polega naruszenie, co usługodawca zrobił i dlaczego. Decyzja powinna wskazywać tryb odwoławczy lub reklamacyjny.

### Aktualizacja warunków

Istotne zmiany warunków korzystania muszą być komunikowane usługobiorcom z odpowiednim wyprzedzeniem, w sposób umożliwiający rezygnację z usługi przed wejściem zmian w życie.

---

## V. Usługi AI jako komponent usług elektronicznych

### Jak traktować AI w regulaminie

Systemy AI udostępniane w ramach hostingu/SaaS są szczególnym typem usługi świadczonej drogą elektroniczną — nie wymagają odrębnego reżimu, lecz uzupełnień w ramach istniejącej struktury regulaminu.

**W definicjach:** wprowadź pojęcia „System AI" / „Moduł AI" i „Usługi AI" jako funkcjonalności systemu teleinformatycznego opartą na modelach zdolnych do przetwarzania danych wejściowych i generowania wyników.

**W zakresie usług:** wylicz moduły AI obok innych usług cyfrowych — z oznaczeniem, czy są odpłatne i w jakim pakiecie.

**W warunkach technicznych:** wskaż obsługiwane formaty danych wejściowych, limity zapytań, dostępne interfejsy (API, panel).

**W AUP (zasadach dopuszczalnego korzystania):** zakazy obejmują wprost:
- wprowadzanie do systemu AI danych bezprawnych,
- korzystanie z AI do generowania treści bezprawnych,
- masowe generowanie spamu, phishingu lub złośliwego oprogramowania,
- podszywanie się pod inne osoby lub wprowadzanie w błąd.

**W SLA:** parametry AI (dostępność modułu, czas odpowiedzi, limity zapytań) mają charakter techniczny. Jakość wyników AI (trafność, poprawność merytoryczna) ma charakter orientacyjny — odchylenia od oczekiwań nie stanowią co do zasady nienależytego wykonania usługi, o ile parametry techniczne są dotrzymane.

**W odpowiedzialności:** usługodawca odpowiada za dostępność i sprawność modułu AI, nie za merytoryczne skutki zastosowania wyników AI przez usługobiorcę. Usługobiorca jest zobowiązany weryfikować wyniki AI przed ich wykorzystaniem w istotnych procesach decyzyjnych.

**W danych osobowych:** dane wprowadzane do systemu AI mogą być przetwarzane w sposób obejmujący analizę, generowanie danych pochodnych i wywnioskowanych. Regulamin odsyła do polityki prywatności, która precyzuje te kwestie.

---

## VI. Zakres danych osobowych przetwarzanych przez usługodawcę

W ramach świadczenia usług drogą elektroniczną usługodawca może przetwarzać:
- dane identyfikacyjne i kontaktowe niezbędne do nawiązania i realizacji stosunku usługowego,
- dane eksploatacyjne charakteryzujące korzystanie z usługi (identyfikatory sesji, znaczniki czasu dostępu, zakres korzystania),
- dane niezbędne ze względu na charakter usługi lub sposób jej rozliczenia.

Dane zbierane na potrzeby marketingu lub badań rynku wymagają odrębnej, wyraźnej zgody usługobiorcy — nie mogą być wbudowane w akceptację regulaminu.

---

## VII. Zasady sporządzania regulaminu — metodologia

### Kolejność konstruowania

1. **Spełnij minimum z art. 8 ust. 3 u.ś.u.d.e.** — cztery obowiązkowe elementy.
2. **Wbuduj mechanizm wyłączenia odpowiedzialności hostingu** (art. 14 u.ś.u.d.e.) — procedura notice & action, spójność z deklaracją braku ogólnego nadzoru.
3. **Nałóż wymogi DSA** — przejrzystość warunków, uzasadnianie decyzji, mechanizm zgłaszania.
4. **Uzupełnij specyfiką AI** — definicje, AUP, SLA, odpowiedzialność.
5. **Sprawdź spójność z prawem konsumenckim** (jeśli klientami są konsumenci) — prawo odstąpienia, informacje przedumowne, ADR/ODR.

### Dobre praktyki redakcyjne

| Zasada | Dlaczego ważna |
|---|---|
| Jasny, precyzyjny język (bez żargonu) | Wymóg DSA; niejasność = ryzyko klauzuli abuzywnej |
| Definicje w § 1, konsekwentnie stosowane | Spójność wewnętrzna, zmniejsza ryzyko sporów interpretacyjnych |
| Wersjonowanie (data i numer wersji) | Możliwość wykazania, jaki regulamin obowiązywał w danym momencie |
| Checkbox przy akceptacji + archiwizacja | Dowód udostępnienia i akceptacji — standard weryfikowalny |
| Tryb zmiany regulaminu z prawem wypowiedzenia | Standard przejrzystości DSA + ochrona konsumenta |
| AUP jako osobny blok (nie rozrzucony) | Przejrzystość; ułatwia stosowanie mechanizmu notice & action |
| Spójność deklaracji braku nadzoru z mechanizmem moderacji | Utrata wyłączenia odpowiedzialności, jeśli deklaracja i praktyka są sprzeczne |

### Anti-patterns — czego unikać

- Ogólne klauzule „usługodawca może wedle uznania" bez wskazania przesłanek — abuzywne, nieskuteczne w DSA.
- Brak procedury notice & action lub procedura bez terminu reakcji.
- Zakaz treści bezprawnych bez żadnego katalogu — zbyt nieprecyzyjne dla potrzeb AUP.
- Regulamin jako jedna ściana tekstu bez struktury — naruszenie standardu przejrzystości DSA.
- Postanowienia ograniczające odpowiedzialność usługodawcy bez wyraźnego wyłączenia winy umyślnej.
- Klauzula ogólna „wyniki AI mogą być błędne" bez wskazania, co usługobiorca powinien z tym zrobić (obowiązek weryfikacji).

---

## VIII. Mapa struktury regulaminu — szkielet paragrafów

| Paragraf | Treść | Podstawa prawna |
|---|---|---|
| § 1 | Postanowienia ogólne i definicje (System AI, Usługi AI, AUP, SLA…) | art. 8 u.ś.u.d.e. |
| § 2 | Dane usługodawcy (firma, KRS/CEIDG, NIP, kontakt) | art. 8 u.ś.u.d.e. |
| § 3 | Rodzaje i zakres usług (hosting, VPS, domeny, AI, SSL…) | art. 8 ust. 3 pkt 1 |
| § 4 | Warunki techniczne korzystania | art. 8 ust. 3 pkt 2 lit. a |
| § 5 | Zakaz treści bezprawnych + katalog AUP (w tym AI) | art. 8 ust. 3 pkt 2 lit. b |
| § 6 | Zawarcie umowy i moment akceptacji regulaminu | art. 8 ust. 3 pkt 3 |
| § 7 | Czas trwania i przedłużanie usług (w tym domeny) | art. 8 ust. 3 pkt 3 |
| § 8 | Zasady płatności i rozliczeń | KC + u.p.k. (konsumenci) |
| § 9 | Parametry usług i SLA (uptime, backup, limity AI) | art. 8 ust. 3 pkt 1 |
| § 10 | Zasady prawidłowego korzystania / AUP (w tym AI) | art. 8 ust. 3 pkt 2 |
| § 11 | Odpowiedzialność usługodawcy i wyłączenia (hosting safe harbour) | art. 14 u.ś.u.d.e. |
| § 12 | Odpowiedzialność usługobiorcy (za treści, naruszenia IP, AI) | KC |
| § 13 | Usługi domenowe (rola pośrednika, regulaminy rejestrów) | — |
| § 14 | Tryb reklamacyjny (w tym dla AI) | art. 8 ust. 3 pkt 4 |
| § 15 | Dane osobowe i bezpieczeństwo | art. 18 u.ś.u.d.e. + RODO |
| § 16 | Moderacja treści i procedura notice & action (w tym AI) | art. 14 u.ś.u.d.e. + DSA |
| § 17 | Uprawnienia konsumenta (odstąpienie, ADR/ODR) | u.p.k. |
| § 18 | Zmiana regulaminu | art. 8 + DSA |
| § 19 | Rozwiązanie umowy i zawieszenie usług | art. 8 ust. 3 pkt 3 |
| § 20 | Postanowienia końcowe (prawo właściwe, klauzula salwatoryjna) | KC |

---

## Powiązania z innymi plikami skilla

- `baza-klauzul/20-regulamin-usdde-aup.md` — klauzule do wklejenia do regulaminu
- `baza-wiedzy/08-rodo-powierzenie-konstrukcja.md` — gdy hosting = powierzenie danych osobowych (art. 28 RODO)
- `baza-wiedzy/09-rodo-bezpieczenstwo-i-naruszenia.md` — środki TOMs, klauzula incydentów
- `baza-wiedzy/07-indemnifikacja-kary-umowne.md` — kary umowne za naruszenia AUP
- `baza-klauzul/11-odpowiedzialnosc.md` — SLA, cap odpowiedzialności
- `baza-klauzul/12-wypowiedzenie-exit.md` — rozwiązanie umowy, exit plan
