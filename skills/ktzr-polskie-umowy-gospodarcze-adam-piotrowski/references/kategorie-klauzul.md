# Kategorie klauzul umownych — taksonomia analityczna

**Status:** wzorzec analityczny KTZR, pomocny w redakcji i diagnozie klauzul. Inspiracja: *Adams, A Manual of Style for Contract Drafting* (5. wyd., ABA 2023) — *„categories of contract language"*. Adaptacja do polskiego systemu prawnego.

**Cel pliku:** dostarczyć Claude'owi i prawnikowi KTZR taksonomię 7 kategorii głównych klauzul (plus 2 pomocnicze: Intencja i Rekomendacja), tak by każda klauzula umowy mogła być świadomie zaklasyfikowana do jednej z nich. Mieszanie kategorii w jednej klauzuli jest typowym źródłem niejednoznaczności.

**Zastrzeżenie:** taksonomia ma charakter analityczny, nie normatywny. Nie zastępuje doktryny ani orzecznictwa. W konkretnej sprawie kategoria klauzuli może być przedmiotem sporu — taksonomia służy autorowi umowy, nie sądowi.

## TL;DR

1. **Każda klauzula = jedna kategoria.** Jeżeli klauzula próbuje robić więcej niż jedno (np. zobowiązuje i jednocześnie zezwala), prawdopodobnie powinna zostać podzielona na dwie.
2. **Niedopasowanie kategorii do treści = niejednoznaczność.** Klauzula *„Strony zobowiązują się, że termin biegnie od dnia zawarcia"* miesza zobowiązanie z polityką — termin nie jest „zobowiązaniem", tylko regułą obliczeniową.
3. **Wybór kategorii zaczyna się od pytania:** *czy chodzi mi o (a) obowiązek wykonania czegoś, (b) prawo do czegoś, (c) zakaz czegoś, (d) zasadę/regułę bez podmiotu zobowiązanego, (e) stwierdzenie faktu, (f) czynność konwencjonalną dokonywaną przez umowę, czy (g) warunek?*
4. **Polska składnia zobowiązaniowa** ma swoją specyfikę — patrz reguła 2 w `style-redakcyjny.md` (warstwa 2): *„[Strona] zobowiązuje się do [czynności w bezokoliczniku]"*. Taksonomia tę regułę uzupełnia o inne kategorie.

## Siedem kategorii klauzul

### 1. Zobowiązanie (obowiązek wykonania świadczenia)

**Konstrukcja:** *„[Strona] zobowiązuje się do [czynności]"* / *„[Strona] [czyni X]"*

**Przykład:**
> *„Wykonawca zobowiązuje się do wystawienia faktury w terminie 7 dni od dnia uznania rachunku."*

**Cechy:**
- Identyfikowalna strona zobowiązana (kto?)
- Konkretna czynność do wykonania (co?)
- Najczęściej z terminem (kiedy?)
- Niewykonanie = naruszenie umowy → odpowiedzialność (art. 471 KC) lub kara umowna

**Anti-pattern:** użycie zobowiązania tam, gdzie wystarczy polityka. Klauzula *„Strony zobowiązują się, że umowa wchodzi w życie z dniem podpisania"* — to nie jest zobowiązanie, tylko polityka (data wejścia w życie nie wymaga „zobowiązywania się"; to fakt obliczeniowy).

### 2. Uprawnienie (prawo do czynienia czegoś)

**Konstrukcja:** *„[Strona] ma prawo do [X]"* / *„[Strona] może [X]"*

**Przykład:**
> *„Wykonawca ma prawo do wstrzymania świadczenia Usług w razie opóźnienia w zapłacie wynagrodzenia powyżej 30 dni."*

**Cechy:**
- Identyfikowalna strona uprawniona
- Konkretne uprawnienie
- Skorzystanie z uprawnienia zazwyczaj nie jest naruszeniem umowy
- Często powiązane z warunkiem aktywującym uprawnienie

**Anti-pattern:** *„Wykonawca może zobowiązać się do [X]"* — miesza uprawnienie ze zobowiązaniem; albo Wykonawca zobowiązuje się (zobowiązanie), albo ma prawo (uprawnienie); nie obie naraz.

### 3. Zakaz (powstrzymanie się od czynienia)

**Konstrukcja:** *„[Stronie] nie wolno [X]"* / *„[Strona] zobowiązuje się nie czynić [X]"* / *„[Strona] zobowiązuje się powstrzymać od [X]"*

**Przykład:**
> *„Zamawiający zobowiązuje się powstrzymać od jakichkolwiek wypowiedzi mogących naruszyć dobre imię Wykonawcy."*

**Cechy:**
- Negatywne zobowiązanie (obowiązek niedziałania)
- Naruszenie = wykonanie czynności wbrew zakazowi
- Często zabezpieczony karą umowną (art. 483 KC)

**Anti-pattern:** *„Zamawiający nie powinien udostępniać Materiałów"* — *„nie powinien"* nie jest zakazem, to rekomendacja. Egzekwowanie niejasne. Lepiej: *„Zamawiający zobowiązuje się nie udostępniać Materiałów"*.

### 4. Polityka / zasada (reguła bez podmiotu zobowiązanego)

**Konstrukcja:** *„[X] wynosi [Y]"* / *„[X] biegnie od [Y]"* / *„[X] stanowi [Y]"* / *„[X] jest [Y]"*

**Przykład:**
> *„Termin płatności wynosi 30 dni od dnia doręczenia faktury."*  
> *„Okres Przejściowy biegnie od dnia zawarcia Porozumienia do dnia 31 grudnia [roku] r."*

**Cechy:**
- Brak identyfikowalnej strony zobowiązanej
- Stwierdzenie reguły obliczeniowej, faktycznej lub definicyjnej
- Stosuje się do całej umowy lub konkretnego paragrafu

**Anti-pattern:** politykę formułować jako zobowiązanie. *„Strony zobowiązują się, że termin płatności wynosi 30 dni"* — niezgrabne, bo „wynoszenie 30 dni" nie wymaga zobowiązania. Po prostu *„Termin płatności wynosi 30 dni"*.

### 5. Oświadczenie / deklaracja (stwierdzenie faktu)

**Konstrukcja:** *„[Strona] oświadcza, że [X]"* / *„Strony zgodnie oświadczają, że [X]"* / *„[Strona] potwierdza, że [X]"*

**Przykład:**
> *„Wykonawca oświadcza, że posiada pełne prawa autorskie majątkowe do Utworów oraz że ich przeniesienie na Zamawiającego nie narusza praw osób trzecich."*

**Cechy:**
- Stwierdzenie stanu faktycznego lub prawnego
- Konsekwencja nieprawdziwości oświadczenia = odpowiedzialność za zapewnienie (art. 471 KC + ewentualnie art. 84-86 KC — uchylenie od skutków oświadczenia woli pod wpływem błędu)
- Często powiązane z indemnifikacją (zob. `baza-klauzul/10-kary-umowne.md` i `baza-wiedzy/07-indemnifikacja-kary-umowne.md`)

**Anti-pattern:** mieszanie oświadczenia z zobowiązaniem. *„Wykonawca oświadcza, że będzie wystawiał faktury"* — przyszłe działanie nie jest „faktem" do oświadczenia; powinno być zobowiązanie *„Wykonawca zobowiązuje się do wystawiania faktur"*.

### 6. Czynność konwencjonalna (skutek prawny przez samą umowę)

**Konstrukcja:** *„[Strona] niniejszym [przenosi / udziela / zwalnia / wyraża zgodę / wypowiada]"*

**Przykład:**
> *„Wykonawca niniejszym przenosi na Zamawiającego autorskie prawa majątkowe do Utworów na polach eksploatacji wymienionych w § 5."*  
> *„Wykonawca niniejszym wyraża zgodę na rozpowszechnianie jego wizerunku w Okresie Przejściowym."*

**Cechy:**
- Skutek prawny powstaje przez samą umowę (przeniesienie praw, udzielenie zgody, zwolnienie z długu)
- Słowo-klucz: *„niniejszym"* (lub bez, gdy kontekst jest jasny)
- Po podpisaniu umowy czynność jest dokonana — nie wymaga osobnego wykonania
- Adams nazywa to *„language of performance"*

**Anti-pattern:** użycie zobowiązania tam, gdzie wystarczy czynność. *„Wykonawca zobowiązuje się do przeniesienia praw autorskich"* — wymaga osobnego, późniejszego aktu przeniesienia; lepiej *„Wykonawca niniejszym przenosi prawa autorskie"* — skutek od razu.

### 7. Warunek (zdarzenie aktywujące)

**Konstrukcja:** *„W przypadku [zdarzenia], [strona] [czyni X]"* / *„Jeżeli [zdarzenie], [skutek]"* (W2 stylu KTZR preferuje *„W przypadku"*)

**Przykład:**
> *„W przypadku opóźnienia w zapłacie którejkolwiek z rat o więcej niż 7 dni od terminu jej wymagalności Porozumienie wygasa w części, w jakiej nie zostało wykonane do dnia upływu tego terminu."*

**Cechy:**
- Warunek zawieszający (skutek powstaje, gdy się ziści) lub rozwiązujący (skutek ustaje, gdy się ziści) — art. 89-94 KC
- Powiązany z inną kategorią — warunek aktywuje zobowiązanie, uprawnienie, zakaz lub politykę
- Z natury złożona konstrukcja — łatwo o niespójność (zob. `baza-klauzul/16-ugody.md`, anti-pattern „dublowanie mechanizmów sankcji")

**Anti-pattern:** ukrywanie warunku w konstrukcji zobowiązaniowej. *„Wykonawca zobowiązuje się do wstrzymania Usług, jeżeli Zamawiający opóźni się z zapłatą o 30 dni"* — to faktycznie warunek + uprawnienie (Wykonawca *może* wstrzymać, nie *musi*); lepiej *„W przypadku opóźnienia w zapłacie powyżej 30 dni Wykonawca ma prawo wstrzymać świadczenie Usług"*.

## Kategorie pomocnicze (rzadziej używane)

### Intencja

**Konstrukcja:** *„Strony zamierzają, że [X]"* / *„Intencją Stron jest, aby [X]"*

Używane głównie w preambule lub przy klauzulach o niepewnym skutku prawnym (np. *„Strony zamierzają, aby Wykonawca pozostawał niezależnym przedsiębiorcą, a nie pracownikiem Zamawiającego"* — przy umowie B2B; treść intencji nie wiąże, ale pomaga w wykładni).

### Rekomendacja

**Konstrukcja:** *„[Strona] powinna [X]"* / *„zalecane jest [X]"*

Rzadko używana w KTZR — wewnętrzna sprzeczność (jeżeli coś jest tylko zalecane, to z mocy umowy nie wynika żadne uprawnienie do egzekwowania). Może występować w załącznikach technicznych jako *„best practices"*.

## Reguła operacyjna: jak używać taksonomii przy redakcji

Przed napisaniem klauzuli zadaj sobie cztery pytania:

1. **Co chcę osiągnąć w tej klauzuli?** (skutek docelowy)
2. **Jaka kategoria najlepiej oddaje ten skutek?** (zobowiązanie, uprawnienie, zakaz, polityka, oświadczenie, czynność, warunek)
3. **Czy w jednej klauzuli próbuję zrobić więcej niż jedno?** Jeżeli tak — rozbij na dwie lub więcej.
4. **Czy konstrukcja składniowa odpowiada kategorii?** (wzorzec wprowadzający — *„zobowiązuje się"* dla zobowiązania, *„ma prawo"* dla uprawnienia, *„niniejszym"* dla czynności konwencjonalnej, *„W przypadku"* dla warunku — patrz tabela poniżej).

| Kategoria | Wzorzec wprowadzający |
|---|---|
| Zobowiązanie | *Strona zobowiązuje się do…* |
| Uprawnienie | *Strona ma prawo do… / może…* |
| Zakaz | *Stronie nie wolno… / Strona zobowiązuje się nie czynić…* |
| Polityka | *X wynosi / biegnie / stanowi / jest…* |
| Oświadczenie | *Strona oświadcza, że…* |
| Czynność konwencjonalna | *Strona niniejszym przenosi / udziela / wyraża zgodę…* |
| Warunek | *W przypadku [X]… / W razie [X]…* |

## Reguła operacyjna: diagnoza niejednoznaczności

Gdy klauzula brzmi *„dziwnie"* lub gdy druga strona zgłasza zastrzeżenia interpretacyjne, taksonomia pomaga zdiagnozować *czemu*:

- **Mieszanie kategorii** w jednym zdaniu — najczęstsze źródło problemu
- **Kategoria niewłaściwa dla skutku** (np. zobowiązanie tam, gdzie powinna być polityka) — sąd interpretuje z trudem
- **Brak kategorii** — klauzula jest tylko obserwacją, nie wynika z niej skutek prawny

## Powiązania w skill

- `references/style-redakcyjny.md` — W2 stylu KTZR opisuje wzorce składniowe dla zobowiązań (rozszerzenie tej taksonomii)
- `references/style-redakcyjny.md` — reguła 1 warstwa 2 (konstrukcje warunkowe — *„W przypadku"*)
- `references/zlote-reguly.md` — Złota Reguła #12 (§ 1 = Przedmiot Umowy, mapa kategorii klauzul w dalszych paragrafach)
- `workflows/audyt-ryzyk.md` — kategoria klauzuli jako filtr przy audycie
- `workflows/popraw-fragment.md` — diagnoza przez taksonomię przy poprawkach

## Źródła doktrynalne

- **Adams, Kenneth A.**, *A Manual of Style for Contract Drafting*, 5. wyd., American Bar Association 2023 — koncepcja *„categories of contract language"* (chap. 2-3)
- **Garner, Bryan A.**, *Guidelines for Drafting and Editing Contracts*, West Academic Publishing 2019 — komplementarne podejście, nacisk na plain language
- **Wronkowska, Sławomira; Zieliński, Maciej**, *Komentarz do Zasad techniki prawodawczej*, Wydawnictwo Sejmowe 2004 — polskie standardy redakcji aktów normatywnych (stosowane analogicznie do umów)
- *Rozporządzenie Prezesa Rady Ministrów z 20 czerwca 2002 r. w sprawie „Zasad techniki prawodawczej"* (Dz.U. 2016 poz. 283 t.j.) — polski formalny wzorzec redakcji

