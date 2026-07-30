# Legal design dla KTZR

**Źródło:** standardy stosowania legal design opracowane przez naszą kancelarię, w oparciu o literaturę (Hagan, Haapio, Passera) i WorldCC Contract Design Pattern Library — dostosowane do profilu kancelarii (B2B IT, nie consumer / nie startup).

**Cel:** ustalić, **które elementy legal design adoptujemy w KTZR**, a które są poza profilem (B2B IT, nie consumer / nie startup). Nie chodzi o "malowanie umów" — chodzi o wybrane techniki poprawiające czytelność, z zachowaniem profesjonalnego tonu dokumentu prawnego.

## TL;DR

1. **Legal design ≠ ozdabianie**. To metoda projektowania dokumentów pod kątem rzeczywistego użytkownika (klienta biznesowego), a nie drugiego prawnika.
2. **WorldCC Pattern Library** (https://contract-design.worldcc.foundation) — open-source, 10 rodzin wzorców. Główne źródło operacyjne.
3. **KTZR adoptuje 5 rodzin w pełni** (Layout, Navigation, Emphasis, Organizing, Tone of voice), **3 selektywnie** (Summarizing, Layering, Visuals — tylko gdy realnie służą), **2 odpada lub robi wewnętrznie** (Reviewing, Explainers w treści normatywnej).
4. **Domyślna typografia KTZR:** Arial 11,5 pt dla treści głównej, lekkie obramowania pod tytułami paragrafów, justyfikacja treści. Times New Roman tylko gdy klient wprost prosi o "klasyczny" wygląd.
5. **5 pytań do zadania przy każdej umowie** decyduje, czy warto dodać tabelę kluczowych warunków, spis treści, timeline lub explainer box.
6. **Antywzorce zawsze odpadają:** comic contracts, kolorowe schematy w treści normatywnej, ikony zastępujące tekst, emojis.
7. **Standard KTZR „light legal design"** = klasyczna struktura prawnicza + selektywne elementy wizualne podnoszące czytelność, bez naruszania profesjonalnego tonu.

## Domyślna typografia KTZR

Te ustawienia stosujemy **w każdym dokumencie wychodzącym z kancelarii**, chyba że klient prosi o inny standard.

### Czcionka

| Element | Czcionka | Rozmiar | Waga |
|---|---|---|---|
| Treść główna | Arial | 11,5 pt | Regular |
| Tytuł dokumentu (POROZUMIENIE, UMOWA itd.) | Arial | 16–18 pt | Bold |
| Podtytuł (kwalifikacja prawna) | Arial | 12 pt | Bold |
| Tytuły paragrafów (§ X. Nazwa) | Arial | 12 pt | Bold |
| Numeracja list literowych / numerycznych | Arial | 11,5 pt | Regular |

**Wyjątek:** jeśli klient wprost prosi o "klasyczny" wygląd (Times New Roman), używamy Times New Roman 12 pt. Stosujemy tę samą strukturę i obramowania.

### Obramowania

| Element | Border | Kolor | Rozmiar |
|---|---|---|---|
| Pod tytułem paragrafu (§ X. Nazwa) | bottom | `808080` (mid gray) | 0,75–1 pt |
| Pod tytułem dokumentu | bottom | `808080` | 1 pt |
| Tabele („Kluczowe warunki", podsumowania) | wszystkie | `CCCCCC` (light gray) | 0,5 pt |

Zasada: **subtelne, monochromatyczne**. Nigdy kolory poza skalą szarości w korpusie umowy. Kolory tylko w tabelach pomocniczych (i tylko jeśli klient wprost zlecił pełniejszy legal design).

### Układ

- Marginesy: 2,5 cm wszystkie strony (1 cal jest też akceptowalne).
- Justyfikacja treści: tak, dla większości akapitów. Centerowane tylko dla tytułów i nagłówków sekcji.
- Spacing: 6 pt po każdym akapicie. Interlinia 1,25.
- Listy: hangujące wcięcie dla (a)(b)(c), numerycznych 1./2./3..

## 10 rodzin wzorców WorldCC — z filtrem KTZR

Mapa wszystkich rodzin z biblioteki Passery / Haapio + decyzja KTZR co do każdej z nich.

| Rodzina | Co robi | Decyzja KTZR | Konkret dla nas |
|---|---|---|---|
| **Emphasis** | Wyróżnia kluczowe informacje | ✅ adoptujemy | Bold dla kwot, dat, terminów, numerów rachunków. **Border-bottom** pod tytułami paragrafów. Kursywa dla definicji w cudzysłowach typograficznych „..." |
| **Layout** | Układa treść by była czytelna | ✅ adoptujemy | Białe światło, krótkie akapity, hangujące wcięcia. Arial 11,5 pt, marginesy 2,5 cm |
| **Navigation** | Pomaga znaleźć w dokumencie | ✅ adoptujemy | Spis treści dla umów >5 stron (auto-generowany). **Aktywne cross-refs** zamiast wpisywanych ręcznie |
| **Organizing** | Strukturyzuje logicznie | ✅ adoptujemy | Kolejność klauzul wg chronologii stosunku, nie alfabetycznie. Definicje na początku, postanowienia końcowe na końcu |
| **Tone of voice** | Słowa, ton, postrzeganie | ✅ adoptujemy | Plain Polish, aktywna strona, krótkie zdania (W1/W2 stylu KTZR) |
| **Summarizing** | Streszcza | ⚖️ selektywnie | Tabela „Kluczowe warunki" na początku — tylko dla umów >3 stron lub gdy klient biznesowy ją czyta |
| **Layering** | Hierarchizuje, kluczowe na wierzchu | ⚖️ selektywnie | Klauzule techniczne / operacyjne przenosimy do załączników; korpus zostaje czytelny |
| **Visuals** | Obrazy wspomagające zrozumienie | ⚖️ selektywnie | Timeline dla projektów z fazami (wdrożenie IT, milestones). Tabela RACI dla podziału odpowiedzialności. Swimlane dla procesów multi-strony. **Tylko gdy realnie tłumaczą strukturę** |
| **Explainers** | Wyjaśnia znaczenie klauzul | ⚠️ z ostrożnością | Boxy „Wyjaśnienie" tylko dla wyjątkowo nieintuicyjnych klauzul (cap odpowiedzialności, wina umyślna, indemnifikacja), gdy klient sygnalizuje że nie rozumie |
| **Reviewing** | Sprawdza kompletność | 🏠 wewnętrznie | Checklisty dla naszego zespołu (`workflows/`), nie wprowadzamy do dokumentu wychodzącego |

## 5 pytań do zadania przy każdej umowie

Przed wysłaniem umowy do klienta / kontrahenta:

1. **Czy umowa ma >3 strony?** Tak → dodaj spis treści (Word: `Wstaw → Spis treści`).
2. **Czy umowa zawiera kluczowe parametry, które klient biznesowy chciałby widzieć od razu?** Tak → tabela „Kluczowe warunki" na początku (Strony, Przedmiot, Wynagrodzenie, Czas trwania, Najważniejsze zobowiązania).
3. **Czy umowa opisuje proces wieloetapowy?** Tak → rozważ timeline (faza 1 → 2 → 3) lub swimlane (kto, kiedy, co robi).
4. **Czy umowa zawiera klauzule technicznie złożone, których odbiorca prawdopodobnie nie zrozumie?** Tak → krótki explainer box obok (max 2-3 zdania plain Polish).
5. **Czy cross-referencje są aktywne (klikalne) w Wordzie?** Nie → popraw na hiperłącza, bo statyczny tekst „§ 5 ust. 2" przy późniejszej renumeracji staje się błędem.

Jeśli odpowiedź na pyt. 1-4 to „nie", umowa zostaje w **stylu klasycznym KTZR** (Arial 11,5, border-bottom pod §, bez dodatkowych elementów wizualnych).

## Konkretne techniki krok po kroku

### A. Tabela „Kluczowe warunki" (Summarizing)

**Kiedy:** umowy >3 stron, każda ugoda, umowy wdrożeniowe IT, umowy ramowe z wieloma zamówieniami.

**Lokalizacja:** zaraz pod tytułem dokumentu, przed komparycją lub pod nią — zależy od konwencji.

**Struktura (minimalna, 2-kolumnowa):**

```
| Strony                  | Wykonawca: [Nazwa] / Zamawiający: [Nazwa]   |
| Przedmiot               | [Krótko, 1 zdanie]                          |
| Wynagrodzenie           | [Kwota / mechanizm rozliczenia]             |
| Czas trwania            | [Daty lub okres]                            |
| Najważniejsze terminy   | [Np. terminy płatności, data wygaśnięcia]   |
| Sąd właściwy            | [Miejscowość]                               |
```

**Charakter:** informacyjny, nie normatywny. Wiążąca jest treść paragrafów. Jeśli ktoś o to pyta — możemy dopisać klauzulę „Tabela ma charakter wyłącznie informacyjny" w postanowieniach końcowych, ale domyślnie nie wpisujemy (zbędne, oczywiste).

### B. Spis treści (Navigation)

**Kiedy:** umowy >5 stron.

**Jak:** Word → `Wstaw → Spis treści` → wybierz wzorzec automatyczny, dostosuj font do Arial 11,5. Wymaga, by tytuły paragrafów były oznaczone jako *Heading 2* (lub odpowiedni styl).

### C. Timeline procesu (Visuals)

**Kiedy:** umowy opisujące projekt wielofazowy (wdrożenie IT, projekt budowlany, migracja). Dla ugody z 3 ratami — *nie warto*, tabela rat wystarcza.

**Jak:**
- Word: `Wstaw → SmartArt → Proces` → wzór poziomy z 3–7 etapami.
- Każdy etap = krótka nazwa (1-3 słowa) + data / milestone.
- Bez ikon, monochromatycznie (szarości lub jeden kolor accentowy nawiązujący do brandingu klienta).

### D. Swimlane (Visuals)

**Kiedy:** wieloetapowe procesy z udziałem >2 podmiotów (np. body leasing IT — Zamawiający / Usługodawca / Specjalista).

**Jak:** SmartArt → diagram z wierszami reprezentującymi strony, kolumnami reprezentującymi fazy. Strzałki przepływu między wierszami.

### E. Explainer box (Explainers)

**Kiedy:** rzadko, tylko gdy klauzula technicznie złożona i klient wprost sygnalizuje że nie rozumie.

**Struktura:**
```
┌─────────────────────────────────────────────┐
│ Wyjaśnienie (charakter informacyjny):       │
│ [2-3 zdania plain Polish, co klauzula       │
│ oznacza w praktyce]                         │
└─────────────────────────────────────────────┘
```

**Charakter:** informacyjny, nie normatywny. Box ma być wizualnie oddzielony od klauzuli (np. tabela 1×1 z lekkim border'em, fontem 10,5 pt italic).

### F. Border-bottom pod tytułami paragrafów (Emphasis + Layout)

**Cel:** subtelne oddzielenie tytułu od treści, ułatwia skanowanie dokumentu.

**Implementacja (Word):**
- Zaznaczamy paragraf z tytułem (§ X. Nazwa).
- `Akapit → Obramowanie → Dolne obramowanie` → kolor `808080`, grubość 0,75 pt.
- Alternatywnie w style definition: `pBdr → bottom`.

**Implementacja (docx-js):**
```javascript
new Paragraph({
  border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: "808080", space: 4 } },
  children: [new TextRun({ text: "§ X. Tytuł", bold: true })]
})
```

## Antywzorce — czego unikamy

- **Comic contracts** (ilustracje komiksowe zastępujące treść). Stanford robił z RPA dla pracowników niepiśmiennych — nie nasz profil.
- **Kolorowe schematy w treści normatywnej**. Wygląda jak prezentacja, nie dokument prawny.
- **Ikony zamiast tekstu w klauzulach**. Ikona może być akcentem w tabeli kluczowych warunków (jeśli klient wymaga); nigdy nie zastępuje treści normatywnej.
- **Emojis** — w żadnym dokumencie wychodzącym z kancelarii.
- **Zbyt dużo bold'a** — jeśli wszystko jest podkreślone, nic nie jest podkreślone. Bold rezerwujemy dla kwot, dat, kluczowych zobowiązań.
- **Dwa różne fonty w jednym dokumencie** (poza wyjątkami typu Arial dla treści + Courier dla kodu w załączniku technicznym). Trzymamy się jednego.
- **Granice komórek tabeli ciemniejsze niż treść** — wygląda jak kratka zeszytu. Zawsze jasny gray (`CCCCCC` lub jaśniejsze).

## Decyzja użycia — kiedy idziemy „light legal design"

KTZR domyślnie pracuje w trybie **„classic-clean"** — bez tabeli kluczowych warunków, bez timeline'ów, ale z naszą domyślną typografią (Arial 11,5 + border-bottom + plain Polish).

Tryb **„light legal design"** uruchamiamy gdy spełniony jest **co najmniej jeden** z warunków:

- Umowa >5 stron i adresatem jest osoba biznesowa (nie prawnik drugiej strony).
- Umowa opisuje proces wieloetapowy z milestone'ami.
- Klient wprost prosi o legal design / „user-friendly" dokument.
- Umowa będzie używana operacyjnie przez zespoły (nie tylko podpisana i schowana do segregatora).

Tryb **„full legal design"** (kolory, ikony, infografiki) — **nie robimy w KTZR**. Jeśli klient tego potrzebuje, kierujemy do wyspecjalizowanych kancelarii projektowych.

## Źródła doktrynalne i operacyjne

### Operacyjne (biblioteki wzorców)

- **WorldCC Contract Design Pattern Library** — https://contract-design.worldcc.foundation (Stefania Passera, Helena Haapio). Open-source, 10 rodzin wzorców z przykładami od Shell, Airbus, Juro i in.
- **Open Law Lab** — https://www.openlawlab.com (Margaret Hagan). Blog + zasoby.
- **Stanford Legal Design Lab** — https://www.legaltechdesign.com.

### Doktrynalne (publikacje)

- **Hagan, M.** (2020), "Legal Design as a Thing: A Theory of Change and a Set of Methods to Craft a Human-Centered Legal System", *Design Issues* 36(3).
- **Hagan, M.**, *Law by Design* — https://www.lawbydesign.co (online, open).
- **Haapio, H. & Passera, S.** (2021), "Contracts as interfaces: Exploring visual representation patterns in contract design", w: *Legal Informatics*, Cambridge University Press, s. 213–238.
- **Haapio, H. & Hagan, M.** (2016), "Design Patterns for Contracts", *Proceedings of the 19th International Legal Informatics Symposium IRIS 2016*. SSRN: 2747280.
- **Corrales Compagnucci, M., Haapio, H., Hagan, M. & Doherty, M.** (red.) (2021), *Legal Design*, Edward Elgar Publishing.

## Powiązania w skill

- `style-redakcyjny.md` — W1–W7 (warsztat prawnika + styl KTZR). Domyślna typografia KTZR (Arial 11,5 + bordery) jest tu rozszerzeniem warstwy 2.
- `zlote-reguly.md` — Złote Reguły KTZR (#1–#12). Legal design nie zmienia tych reguł.
- `baza-klauzul/` — wzorce klauzul. Visual layer jest *niezależny* od treści klauzul — to jest jak je *prezentujemy*, nie *co* w nich piszemy.
