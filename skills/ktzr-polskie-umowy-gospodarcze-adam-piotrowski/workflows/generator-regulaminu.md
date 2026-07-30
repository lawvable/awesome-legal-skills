# Workflow: Generator regulaminu (cold start → wywiad → szkielet → treść)


> _Reguły globalne: `references/rdzen-ktzr.md` (R1 cytowania · R2 bramka · R3 role · R4 profil · R5 format)._

> **R3 — LAIK:** dodatkowe sygnały dla regulaminów: „muszę opublikować regulamin", „jestem właścicielem sklepu", „chcę uruchomić sklep".

Interaktywny generator regulaminów usług elektronicznych (u.ś.u.d.e., DSA). Workflow **zawsze zaczyna od 3 pytań diagnostycznych** — by wybrać właściwą ścieżkę. Następnie prowadzi wywiad jedno pytanie po drugim, pokazuje szkielet struktury do akceptacji, a dopiero potem generuje pełną treść.

## Trzy ścieżki

| Ścieżka | Kiedy | Paragrafy | Pytania wywiadu |
|---|---|---|---|
| **Ogólny** | B2B, usługa profesjonalna, brak sklepu i SaaS | ~10 | 4 |
| **SaaS** | B2B/B2C, platforma / aplikacja, subskrypcja, SLA | ~18 | 7 |
| **E-commerce** | B2C / mieszany, sklep, towary lub treści cyfrowe | ~22 | 9 |

---

## ETAP 0: Cold start (diagnoza — 3 pytania)

**Nie pytaj wszystkiego naraz.** Zadaj każde pytanie osobno, poczekaj na odpowiedź.

### Pytanie diagnostyczne 1/3

> Zanim zaczniemy — kilka pytań żebym wybrał właściwą ścieżkę.
>
> **Kim będą główni użytkownicy Twojego regulaminu?**
> a) Wyłącznie firmy / przedsiębiorcy (B2B)
> b) Konsumenci — osoby fizyczne (B2C)
> c) Mieszani — i firmy, i konsumenci

### Pytanie diagnostyczne 2/3

Po odpowiedzi zapytaj:

> **Czego głównie dotyczy usługa objęta regulaminem?**
> a) Sprzedaż produktów / towarów przez internet (sklep online)
> b) Dostęp do platformy lub aplikacji webowej / mobilnej (SaaS, marketplace, portal)
> c) Hosting, serwery, domeny, e-mail
> d) Usługi profesjonalne / pośrednictwo / doradztwo online
> e) Inne (opisz)

### Pytanie diagnostyczne 3/3

Po odpowiedzi zapytaj:

> **Jaki model odpłatności?**
> a) Subskrypcja (miesięczna / roczna)
> b) Jednorazowy zakup / opłata za transakcję
> c) Model prowizyjny / success fee
> d) Bezpłatna lub freemium

### Wybór ścieżki

Po 3 odpowiedziach ogłoś ścieżkę:

```
Na podstawie Twoich odpowiedzi wybieram ścieżkę [NAZWA]:
— [jedno zdanie uzasadnienia]

Zaraz zadam Ci [N] pytań szczegółowych. Lecimy?
```

**Reguły wyboru:**
- B2C + sklep / towary / treści cyfrowe → **E-commerce**
- B2C + platforma / aplikacja → **E-commerce** (u.p.k. stosuje się do platform)
- Mieszani + sklep → **E-commerce** (konsument = słabsza strona, stosuj wyższy standard)
- Mieszani + platforma / aplikacja (nie sklep) → **SaaS** ⚠️ Platforma ma użytkowników będących konsumentami — dodaj do SaaS §Prawo Odstąpienia (art. 27 u.p.k. od zawarcia umowy online) i sekcję ODR w §Postanowienia Końcowe
- B2B + sklep / sprzedaż towarów → **E-commerce** ⚠️ Pomiń §10 Prawo Odstąpienia i §11 Wyjątki — nie stosują się w obrocie B2B; zachowaj rękojmię KC (art. 556 i n.) bez klauzul konsumenckich
- B2B + platforma / SaaS / hosting / domeny → **SaaS**
- B2B + usługi profesjonalne / pośrednictwo / inne → **Ogólny**
- B2C + hosting / domeny / e-mail → **SaaS** ⚠️ Dodaj §Prawo Odstąpienia (art. 27 u.p.k.) i sekcję ODR w §Postanowienia Końcowe — konsument kupujący hosting podlega pełnej ochronie u.p.k.
- Mieszani + hosting / domeny → **SaaS** ⚠️ Jak wyżej
- Wątpliwości → zapytaj wprost zamiast zgadywać

**STOP. Poczekaj na potwierdzenie ("lecimy" / "tak" / korekta ścieżki).**

---

## ETAP 1A: Wywiad — ścieżka Ogólna (4 pytania)

Pytaj jedno po drugim, czekaj na odpowiedź.

**P1.** Pełna nazwa Twojej firmy / działalności i siedziba?

**P2.** Jak nazywa się usługa lub serwis objęty regulaminem? Czego dotyczy — opisz w jednym zdaniu.

**P3.** Jakie są główne obowiązki i zakazy po stronie użytkownika? (np. zakaz spamowania, zakaz odsprzedaży, zakaz zakładania fikcyjnych kont)

**P4.** Jak obsługujesz płatności — kiedy użytkownik płaci i jaką metodą? Czy abonament, jednorazowo, czy usługa bezpłatna?

Po ostatniej odpowiedzi → **ETAP 2A**.

---

## ETAP 1B: Wywiad — ścieżka SaaS (7 pytań)

Pytaj jedno po drugim, czekaj na odpowiedź.

**P1.** Pełna nazwa firmy i nazwa platformy / aplikacji?

**P2.** Jaki model subskrypcji? Jakie plany są dostępne — nazwy i co obejmują? Czy jest bezpłatny plan próbny?

**P3.** Czy oferujesz SLA — gwarantowany czas dostępności (uptime)? Jeśli tak: jaki % i co się dzieje przy niedotrzymaniu?

**P4.** Lista zakazów AUP — jakich działań użytkownicy nie mogą robić na platformie? (typowe: spam, scraping, nielegalne treści, nadużycie API)

**P5.** Czy przetwarzasz dane osobowe użytkowników — dane konta, logi, dane klientów uploadowane przez użytkownika? Czy potrzebujesz umowy powierzenia przetwarzania (DPA, art. 28 RODO)?

**P6.** Czy platforma zawiera funkcje AI — generatywne lub analityczne? Jeśli tak: opisz krótko.

**P7.** Czy użytkownicy mogą wrzucać treści na platformę (UGC: posty, pliki, obrazy, dane)? Czy platforma jest moderowana?

Po ostatniej odpowiedzi → **ETAP 2B**.

---

## ETAP 1C: Wywiad — ścieżka E-commerce (9 pytań)

Pytaj jedno po drugim, czekaj na odpowiedź.

**P1.** Pełna nazwa sklepu / serwisu i siedziba sprzedawcy?

**P2.** Co sprzedajesz — produkty fizyczne, treści cyfrowe (pliki, dostęp online), usługi, czy mix?

**P3.** Jakie formy płatności akceptujesz? (karta, BLIK, przelew, PayPal, inne)

**P4.** Jakie formy dostawy i orientacyjny czas realizacji? (kurier, paczkomat, e-mail dla treści cyfrowych)

**P5.** Polityka zwrotów — stosujesz ustawowe 14 dni na odstąpienie (art. 27 u.p.k.), czy oferujesz wydłużony termin?

**P6.** Czy sprzedajesz treści cyfrowe niedostarczane na nośniku — np. pliki PDF, kursy online, dostęp do aplikacji? (wpływa na art. 38 pkt 13 u.p.k. — wyłączenie prawa odstąpienia po spełnieniu świadczenia za zgodą konsumenta)

**P7.** Czy wśród produktów są towary z wyłączeniami prawa odstąpienia — np. produkty nagrywane, szybko psujące się, dopasowywane do konsumenta?

**P8.** Czy obsługujesz zamówienia z krajów UE poza Polską? (wpływa na VAT OSS i regulacje transgraniczne)

**P9.** Preferowana ścieżka reklamacji — e-mail, formularz, czy inaczej? Jaki chcesz zadeklarować termin odpowiedzi?

> ⚠️ **Walidacja P9:** W relacji B2C deklarowany termin odpowiedzi na reklamację nie powinien przekraczać 14 dni kalendarzowych — dłuższy skutkuje uznaniem reklamacji z mocy prawa (art. 7a u.p.k.); dla roszczeń z tytułu braku zgodności towaru z umową — art. 43d ust. 1 u.p.k. W przypadku gdy użytkownik wskaże termin dłuższy niż 14 dni — poinformuj o ryzyku i zaproponuj termin 14 dni. Przeliczaj terminy podane w dniach roboczych lub tygodniach na dni kalendarzowe przed porównaniem (tydzień = 7 dni kal.; 1 dzień roboczy ≈ 1,4 dnia kal.).

Po ostatniej odpowiedzi → **ETAP 2C**.

---

## ETAP 2A: Szkielet — ścieżka Ogólna

**Otwórz:** `references/baza-klauzul/20-regulamin-usdde-aup.md`, `references/baza-klauzul/INDEX.md`

Pokaż proponowaną strukturę:

```
SZKIELET REGULAMINU — ścieżka Ogólna (~10 §)

§ 1.  Definicje          — pojęcia kluczowe, nazwy stron
§ 2.  Postanowienia ogólne — charakter regulaminu, akceptacja, wymagania techniczne
§ 3.  Zakres usługi      — co obejmuje, czego nie obejmuje
§ 4.  Obowiązki i zakazy użytkownika — lista z P3
§ 5.  Wynagrodzenie i płatności — [model z P4]
§ 6.  Odpowiedzialność usługodawcy — limit, wyłączenia
§ 7.  Reklamacje         — procedura (forma, dane, termin)
§ 8.  Wypowiedzenie i zawieszenie konta
§ 9.  Ochrona danych osobowych — art. 13 RODO, podstawa przetwarzania
§ 10. Postanowienia końcowe — prawo właściwe, sąd, zmiana regulaminu
```

**STOP. Zapytaj:** "Akceptujesz tę strukturę? Coś dodać lub wyrzucić?"

---

## ETAP 2B: Szkielet — ścieżka SaaS

**Otwórz:** `references/baza-klauzul/20-regulamin-usdde-aup.md`, `references/baza-wiedzy/13-regulamin-usdde-hosting-ai.md`, `references/baza-klauzul/INDEX.md`

Pokaż proponowaną strukturę. Paragrafy z [jeśli...] aktywuj tylko gdy dotyczy:

```
SZKIELET REGULAMINU — ścieżka SaaS (~18 §)

§ 1.  Definicje          — Platforma, Plan Abonamentowy, SLA, AUP, Konto, Użytkownik
§ 2.  Zawarcie umowy     — moment rejestracji, e-mail aktywacyjny, wiek / status prawny
§ 3.  Zakres usługi      — opis Platformy, moduły, środowisko produkcyjne vs. testowe
§ 4.  Plany abonamentowe — [nazwy z P2], zakres, upgrades / downgrades
§ 5.  AUP               — zakazy użytkowania [lista z P4]
§ 6.  Konto użytkownika  — hasło, bezpieczeństwo, odpowiedzialność za konto
§ 7.  Wynagrodzenie i płatności — pre-paid, faktury VAT, skutki braku płatności
§ 8.  SLA               — dostępność [% z P3], czasy reakcji, Wada Krytyczna / Istotna / Kosmetyczna [jeśli P3 podano]
§ 9.  Dane osobowe i powierzenie — art. 13 RODO + DPA art. 28 [jeśli P5 = tak]
§ 10. Prawa własności intelektualnej — platforma = własność usługodawcy; dane użytkownika = własność użytkownika
§ 11. Treści użytkownika (UGC) — licencja, moderacja, notice & action [jeśli P7 = tak]
§ 12. Moduły AI          — zakres, wyłączenia odpowiedzialności za output [jeśli P6 = tak]
§ 13. Odpowiedzialność   — cap (ostatnie 12 mies. abonamentu), wyłączenie szkód pośrednich
§ 14. Zawieszenie i usunięcie konta — przesłanki, wind-down, eksport danych
§ 15. Wypowiedzenie      — przez każdą ze stron, okresy
§ 16. Zmiana regulaminu  — tryb, okres wyprzedzenia, brak akceptacji
§ 17. Reklamacje         — procedura, [___] dni roboczych
§ 18. Postanowienia końcowe — prawo polskie, sąd, klauzula salwatoryjna
```

**STOP. Zapytaj:** "Akceptujesz tę strukturę? Które §§ oznaczone [jeśli...] dotyczą Twojej platformy? Coś dodać lub wyrzucić?"

---

## ETAP 2C: Szkielet — ścieżka E-commerce

**Otwórz:** `references/baza-klauzul/20-regulamin-usdde-aup.md`, `references/baza-klauzul/INDEX.md`

Pokaż proponowaną strukturę. Paragrafy z [jeśli...] aktywuj tylko gdy dotyczy:

```
SZKIELET REGULAMINU — ścieżka E-commerce (~22 §)

§ 1.  Dane sprzedawcy    — art. 8 ust. 3 u.ś.u.d.e.: firma, adres, NIP, e-mail, telefon
§ 2.  Definicje          — Sklep, Towar, Treść Cyfrowa, Konsument, Konto, Zamówienie
§ 3.  Zasady korzystania ze Sklepu — wymagania techniczne, zakazy
§ 4.  Rejestracja i Konto [jeśli sklep ma konta]
§ 5.  Składanie Zamówień — procedura, moment zawarcia umowy sprzedaży
§ 6.  Ceny i Płatności   — metody [z P3], waluta, termin
§ 7.  Dostawa            — metody [z P4], koszty, termin, ryzyko utraty towaru
§ 8.  Realizacja         — potwierdzenie, anulowanie, niedostępność towaru
§ 9.  Treści Cyfrowe     — dostarczenie, moment wykonania, zgoda konsumenta na natychmiastowe spełnienie [jeśli P2/P6]
§ 10. Prawo Odstąpienia  — 14 dni (art. 27 u.p.k.), formularz, zwrot płatności
§ 11. Wyjątki od Prawa Odstąpienia — [lista z P7 + art. 38 u.p.k.] [jeśli dotyczy]
§ 12. Rękojmia           — odpowiedzialność za wady towaru (art. 43a–43g u.p.k. dla B2C; art. 556 i n. KC dla B2B)
§ 13. Reklamacje         — procedura [z P9], termin, co zawierać zgłoszenie
§ 14. Gwarancja          — kto udziela, czas, zakres [jeśli dotyczy]
§ 15. Oceny i Komentarze [jeśli sklep ma system opinii]
§ 16. Ochrona Danych Osobowych — art. 13 RODO, cel i podstawa przetwarzania
§ 17. Pliki Cookies i śledzenie
§ 18. Odpowiedzialność   — ograniczenia po stronie sprzedawcy (nie dot. roszczeń konsumenta z rękojmi)
§ 19. Zamówienia transgraniczne — VAT, prawo właściwe dla konsumentów UE [jeśli P8 = tak]
§ 20. Pozasądowe Rozwiązywanie Sporów — ODR (https://commission.europa.eu/consumers/odr), UOKIK
§ 21. Zmiana Regulaminu  — tryb, skuteczność wobec zamówień złożonych przed zmianą
§ 22. Postanowienia Końcowe — prawo polskie, sąd, klauzula salwatoryjna
```

**STOP. Zapytaj:** "Akceptujesz tę strukturę? Które §§ oznaczone [jeśli...] dotyczą Twojego sklepu? Coś dodać lub wyrzucić?"

---

## ETAP 3: Generowanie regulaminu

**Otwórz:** `references/style-redakcyjny.md`, `references/baza-klauzul/20-regulamin-usdde-aup.md`, potrzebne pliki z `references/baza-klauzul/` wg `INDEX.md`

Na podstawie zatwierdzonego szkieletu generuj regulamin paragraf po paragrafie.

### Zasady pisania

1. **Klauzule z bazy KTZR** — główne źródło: `20-regulamin-usdde-aup.md`. Uzupełniaj z innych plików wg `INDEX.md`. Nie wymyślaj klauzul spoza bazy.

2. **Dopasowanie do wywiadu** — konkretna nazwa usługodawcy i usługi, nie placeholdery. Konkretne plany, terminy, metody płatności z odpowiedzi. Pola `[___]` pozostawiaj **tylko tam gdzie użytkownik nie podał danych**.

3. **Styl KTZR** — zgodnie z `style-redakcyjny.md`. Definicje z wielką literą. Ustępy numerowane. Odesłania w formacie "§ X ust. Y". Język formalno-prawny, nie marketingowy.

4. **Minimum art. 8 u.ś.u.d.e.** — każdy regulamin musi zawierać:
   - dane usługodawcy (firma, adres, NIP, e-mail, telefon)
   - rodzaje i zakres usług elektronicznych
   - warunki świadczenia (wymagania techniczne)
   - warunki zawarcia i rozwiązania umowy
   - tryb postępowania reklamacyjnego

5. **Ścieżka E-commerce — konsument** — każda klauzula dotycząca konsumenta musi być zgodna z ustawą z 30 maja 2014 r. o prawach konsumenta. Klauzule ograniczające prawa konsumenta są z mocy prawa bezskuteczne — nie wpisuj ich.

### Format wyjścia

```
REGULAMIN [NAZWA USŁUGI / SKLEPU]
Obowiązuje od: [data — zostaw puste jeśli nie podano]
Wersja: 1.0

§ 1. [TYTUŁ]

1. [Treść ustępu pierwszego]
2. [Treść ustępu drugiego]

§ 2. [TYTUŁ]

1. [Treść]
[...]

---
Kontakt: [dane z wywiadu]
```

Po wygenerowaniu całości → **ETAP 4 (QA)**.

**STOP. Zapytaj:** „Chcesz żebym teraz przeprowadził QA regulaminu?"

---

## ETAP 4: Weryfikacja (QA)

Sprawdź regulamin pod kątem:

1. **Minimum u.ś.u.d.e.** — czy art. 8 ust. 3 pkt 1–4 są spełnione: (a) dane usługodawcy (firma, adres, NIP, e-mail, telefon); (b) wymagania techniczne; (c) zakaz dostarczania treści bezprawnych; (d) warunki zawarcia i rozwiązania umowy; (e) tryb reklamacyjny
2. **Definicje** — każde pojęcie pisane Wielką Literą ma definicję w § Definicje
3. **Odesłania** — każde "§ X ust. Y" prowadzi do istniejącego przepisu
4. **Pola `[___]`** — czy nie zostało żadne niezamierzone puste pole
5. **Konsument (E-commerce i SaaS z B2C)** — czy nie ma klauzul sprzecznych z u.p.k. i art. 385¹ KC
6. **Terminologia** — jedna nazwa strony przez cały regulamin
7. **Formularz odstąpienia (E-commerce B2C)** — czy §Prawo Odstąpienia zawiera wzór formularza lub odesłanie do formularza z Załącznika nr 2 u.p.k. (art. 30 u.p.k.)
8. **Obowiązki informacyjne (E-commerce i SaaS B2C)** — czy regulamin lub wskazane miejsce na stronie pokrywa minimum art. 12 u.p.k. (dane sprzedawcy, łączna cena, czas trwania, prawo odstąpienia, interoperacyjność treści cyfrowych)
9. **Reklamacje B2C (SaaS z B2C / E-commerce)** — termin w § Reklamacje musi być w dniach **kalendarzowych**, nie roboczych; art. 7a u.p.k. limituje do 14 dni kal. (dłuższy termin = reklamacja uznana z mocy prawa). Przelicz: 1 tydzień = 7 dni kal.; 1 dzień roboczy ≠ 1 dzień kalendarzowy.

Przed finalną wersją — bramka. Wyświetl pytania i **zaczekaj na odpowiedź**:

```
⛔ Przed finalnym regulaminem — potwierdź:
1. Dane podmiotu (nazwa, NIP, adres, KRS) zweryfikowane źródłowo?
2. Cytaty przepisów sprawdzone (verify_article lub ręcznie)?
3. Platforma/sklep B2C czy wyłącznie B2B? (zmienia zakres obowiązków u.p.k.)
4. Prawnik widział draft?
→ „tak, generuj" / lub wskaż co poprawić
```

Dopiero po potwierdzeniu — generuj. Bez potwierdzenia — zwróć `[DRAFT — DO WERYFIKACJI]` nad regulaminem.

Wyjątek: „tryb express" lub „zrób bez pytania" → generuj z `[DRAFT — DO WERYFIKACJI]` na początku i końcu.

Zwróć QA jako listę ✅ / ⚠️ / ❌, a następnie finalny regulamin:

```
## WERYFIKACJA REGULAMINU

✅ Minimum art. 8 u.ś.u.d.e. — spełnione (§ 1, § 7, § 17)
⚠️ [ew. uwaga]
❌ [ew. błąd — opisz co poprawiono]

---

## FINALNY REGULAMIN

[czysty tekst, bez komentarzy w treści]
```

---

## Iteracja: REDRAFT

Jeśli użytkownik chce zmienić fragment po wygenerowaniu:

1. Wskaż paragraf i zmianę
2. Pobierz odpowiednią klauzulę z bazy (jeśli potrzeba)
3. Wprowadź zmianę; sprawdź czy nie zepsuła odesłań, definicji, numeracji
4. Zwróć **CAŁY regulamin ponownie** — nie tylko zmieniony fragment
