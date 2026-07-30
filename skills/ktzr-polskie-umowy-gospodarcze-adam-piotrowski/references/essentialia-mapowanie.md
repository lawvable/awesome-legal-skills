# Essentialia negotii — mapowanie typów umów

Przed jakąkolwiek pracą z umową **zawsze najpierw zmapuj essentialia**. Bez tego nie wolno generować ani jednego paragrafu.

## Pięć elementów obowiązkowych dla każdej umowy

1. **TYP UMOWY** — jaki stosunek prawny reguluje? (B2B, NDA, wdrożenie, przeniesienie praw, najem, dostawa, etc.)
2. **STRONY** — kto z kim (nazwy pełne, formy prawne, role: Zleceniodawca/Wykonawca, Zamawiający/Dostawca, etc.)
3. **PRZEDMIOT** — co dokładnie jest przedmiotem (usługa, licencja, przeniesienie praw, dzieło, towar)
4. **WYNAGRODZENIE** — ile, jak, kiedy (kwota/stawka, model, termin, waluta, faktura)
5. **CZAS** — na jak długo (czas określony/nieokreślony, daty, okresy wypowiedzenia)

---

## Mapowanie po typach — co musi być

### Body Leasing IT (B2B)

**Typ prawny:** umowa o świadczenie usług (art. 750 KC w zw. z 734 i nast.) między przedsiębiorcami.

**Krytyczne elementy:**
- **Wyraźne wyłączenie stosunku pracy** (art. 22 § 1 KP): "Umowa nie kreuje stosunku pracy"
- **Specjalista jako niezależny przedsiębiorca** (B2B) lub osoba na umowie cywilnoprawnej
- **Autonomia Specjalisty** w doborze metod i narzędzi (kluczowe dla obrony przed przekwalifikowaniem)
- **Model rozliczenia:** T&M na podstawie Timesheet, zatwierdzanego (z domniemaniem akceptacji po np. 5 DR)
- **NDA dla Specjalistów** — obowiązek zawarcia odrębnych NDA przed przystąpieniem
- **Przeniesienie praw autorskich** — Utwory tworzone w ramach Usług (z określeniem momentu i pól)

**Czas:** zwykle nieokreślony, wypowiedzenie 1–3 mies. Ramowa + Zamówienia.

---

### NDA (umowa o zachowaniu poufności)

**Typ prawny:** umowa nienazwana (autonomia woli, art. 353¹ KC), zwykle jednostronna lub wzajemna.

**Krytyczne elementy:**
- **Definicja Informacji Poufnych** — szeroka, z domniemaniem poufności w razie wątpliwości
- **Cel ujawnienia** — wyraźnie wskazany (Projekt, negocjacje, współpraca)
- **Okres obowiązywania** — w trakcie + po (typowo 3–10 lat; tajemnica przedsiębiorstwa bezterminowo)
- **Wyłączenia** — informacje publicznie dostępne, znane wcześniej, niezależnie opracowane, ujawnione na żądanie organów
- **Procedura naruszenia** — notyfikacja 24–72h, współpraca przy ograniczaniu skutków
- **Kara umowna** — konkretna kwota za każdy przypadek + odszkodowanie uzupełniające
- **Zastrzeżenie:** zawarcie NDA nie zobowiązuje do zawarcia umowy głównej

**Czas:** określony okresem od daty zawarcia + okres po zakończeniu.

---

### Umowa wdrożeniowa IT (fixed price)

**Typ prawny:** umowa o dzieło (art. 627 KC) z elementami usług / mieszana.

**Krytyczne elementy:**
- **Specyfikacja** jako załącznik (najlepiej szczegółowy SOW)
- **Kamienie milowe** z protokołami odbiorów (częściowych i końcowego)
- **Procedura odbioru** — terminy zgłaszania wad, klasyfikacja wad (krytyczna/istotna/kosmetyczna)
- **Gwarancja** — okres, zakres, wyłączenia (zmiany konfiguracji, zmiany środowiska)
- **Przeniesienie praw autorskich** — z momentem przejścia (zwykle po zapłacie wynagrodzenia)
- **Klauzula anty-copyleft** — Wykonawca gwarantuje brak elementów GPL/AGPL
- **Repository handover** — procedura wydania kodu źródłowego i dokumentacji

**Czas:** określony datą końcową lub osiągnięciem ostatniego kamienia milowego.

---

### SaaS / licencja oprogramowania

**Typ prawny:** umowa licencyjna (art. 41 i nast. PrAut) + umowa o świadczenie usług (utrzymanie).

**Krytyczne elementy:**
- **Pola eksploatacji** licencji — wymienione wprost
- **Charakter licencji** — niewyłączna/wyłączna, terytorialna/światowa, sublicensable czy nie
- **SLA** — dostępność (uptime %), czasy reakcji, czasy naprawy
- **Maintenance & support** — co obejmuje, co dodatkowo płatne
- **Dane klienta** — własność, miejsce przetwarzania, RODO, eksport po zakończeniu
- **Wypowiedzenie i exit** — okres, procedura migracji danych

---

### Umowa o świadczenie usług księgowych

**Typ prawny:** umowa o świadczenie usług (art. 750 KC), regulowana ustawą o rachunkowości.

**Krytyczne elementy:**
- **Uprawnienia Zleceniobiorcy** — wpis na listę / certyfikat, ważne OC
- **Zakres usług** — księgowość pełna/uproszczona, kadry, płace, doradztwo podatkowe (osobno)
- **Obowiązki Zleceniodawcy** — terminowe i kompletne dostarczanie dokumentów
- **Odpowiedzialność za szkody** — z odesłaniem do polisy OC
- **Tajemnica zawodowa** — odesłanie do art. 4a ustawy o doradztwie podatkowym / ustawy o rachunkowości

---

### Umowa przeniesienia praw autorskich

**Typ prawny:** umowa rozporządzająca (art. 41 i nast. PrAut).

**Krytyczne elementy:**
- **Pola eksploatacji** — wymienione wprost (art. 41 ust. 2 PrAut — brak wymienienia = brak przeniesienia)
- **Wynagrodzenie** — wyraźnie wskazane (nieodpłatność wymaga jasnego oświadczenia)
- **Moment przejścia praw** — wskazany wprost (data zawarcia / data zapłaty / data odbioru)
- **Prawa zależne** — czy nabywca może przerabiać, modyfikować, tworzyć utwory zależne
- **Prawa osobiste** — zobowiązanie autora do niewykonywania (nie da się przenieść, tylko zobowiązać do niewykonywania)
- **Gwarancje czystości IP** — Zbywca gwarantuje wyłączną pełnię praw
- **Klauzula anty-copyleft** — dla oprogramowania

---

### Ugoda

**Typ prawny:** ugoda (art. 917 KC).

**Krytyczne elementy:**
- **Stan sporny** — opis sytuacji, do której się odnosi (z konkretami: numery faktur, daty, kwoty)
- **Wzajemne ustępstwa** — wyraźnie po obu stronach (bez tego nie jest to ugoda)
- **Zrzeczenie roszczeń** — w jakim zakresie, czego
- **Termin i sposób wykonania** zobowiązań z ugody
- **Klauzula salwatoryjna** specyficzna dla ugody — co jeśli któraś strona nie wykona

---

### Cesja wierzytelności

**Typ prawny:** przelew wierzytelności (art. 509 i nast. KC).

**Krytyczne elementy:**
- **Wierzytelność precyzyjnie określona** — podstawa prawna, dłużnik, kwota, wymagalność
- **Cena za cesję** lub jej brak (cesja nieodpłatna)
- **Oświadczenie cedenta o przysługującej wierzytelności** — istnienie, brak obciążeń, brak zakazu cesji
- **Notyfikacja dłużnika** — kto, kiedy, w jakiej formie (od momentu notyfikacji dłużnik nie może płacić cedentowi)
- **Odpowiedzialność cedenta** — za istnienie wierzytelności (zawsze), za wypłacalność dłużnika (tylko jeśli wyraźnie zastrzeżona — art. 516 KC)

---

## Po zmapowaniu essentialia

Pokaż użytkownikowi mapowanie w przejrzystym formacie:

```
ESSENTIALIA NEGOTII
- Typ: [...]
- Strony: [...]
- Przedmiot: [...]
- Wynagrodzenie: [...]
- Czas: [...]

KRYTYCZNE ELEMENTY DLA TEGO TYPU UMOWY:
- [...]
- [...]
```

I **zapytaj o potwierdzenie lub korekty**, zanim przejdziesz dalej.
