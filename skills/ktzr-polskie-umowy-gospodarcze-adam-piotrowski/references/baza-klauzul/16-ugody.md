---
type: Klauzula
title: Ugody i porozumienia
tags: [ugoda, art-917-KC, VAT, zadośćuczynienie, odszkodowanie, wizerunek, roszczenia, cofnięcie-zgody, warunek-zawieszający]
contract_types: [ugoda, porozumienie]
risk_level: wysoki
mandatory_for: [ugoda]
requires: [02-preambuly.md, 17-postanowienia-koncowe.md]
timestamp: 2026-06-27
---

# Ugody i porozumienia

## Klauzule z umów KTZR

### Porozumienie (ugoda — wady lokalu)

> Zapłata następuje wyłącznie w celu uniknięcia dalszego sporu i nie stanowi uznania przez Sprzedających jakichkolwiek roszczeń Kupujących — ani wprost, ani w sposób dorozumiany — w tym w szczególności nie stanowi uznania długu w rozumieniu przepisów prawa cywilnego.

> Z chwilą dokonania zapłaty wszelkie roszczenia Kupujących wynikające ze zdarzeń opisanych w § 1 zostają w całości zaspokojone i wyczerpane. Spór uznaje się za całkowicie i polubownie zakończony.

> Porozumienie stanowi ugodę w rozumieniu art. 917 Kodeksu cywilnego. Każda ze Stron ponosi własne koszty jego zawarcia.

### Porozumienie o rozwiązaniu umowy zlecenia

> Strony oświadczają, że nie mają wobec siebie żadnych dalszych roszczeń wynikających z rozwiązanej umowy zlecenia.

## VAT w ugodach o mieszanych tytułach płatności

Gdy ugoda zawiera **dwa lub więcej tytułów płatności o różnym reżimie podatkowym** (typowo: odszkodowanie / zadośćuczynienie + wynagrodzenie za korzystanie z dobra niematerialnego), wymaga to świadomej decyzji co do alokacji VAT i jej zapisania w treści.

### Typowe tytuły i ich reżim VAT

| Tytuł | VAT |
|---|---|
| Odszkodowanie za szkodę majątkową (lucrum cessans, damnum emergens) | **Nie podlega** — nie jest wynagrodzeniem za świadczenie (interpr. ogólna MF + linia orzecznicza NSA) |
| Zadośćuczynienie za naruszenie dobra osobistego (wizerunek, dobre imię) | **Nie podlega** — szkoda niemajątkowa, brak ekwiwalentności świadczeń |
| Wynagrodzenie za korzystanie z wizerunku / praw autorskich / licencji w okresie objętym ugodą | **Podlega** — usługa w rozumieniu art. 8 ustawy o VAT |
| Wynagrodzenie za zrzeczenie się roszczeń / „odstępne" | **Podlega** — świadczenie usługi (zaniechania) |
| Zwrot kosztów postępowania / Pokrycie kosztów pełnomocnika | **Nie podlega** — zwrot kosztów, nie wynagrodzenie |

### Wariant redakcyjny: jednolita kwota „brutto"

> ✅ *„Zamawiający zobowiązuje się zapłacić Wykonawcy łączną kwotę [X] zł (słownie: [X słownie]) brutto, łącznie ze wszystkimi należnościami podatkowymi."*

— Zamyka furtkę interpretacyjną *„a może to było netto"*. Ryzyko VAT po stronie odbiorcy (Wykonawca dolicza sobie VAT z kwoty *brutto*, czyli liczy VAT *„w stu"*).

**Stosuj gdy:** klient (wystawca dokumentu księgowego) godzi się ponieść ryzyko, że część kwoty objętej VAT „skonsumuje" VAT należny.

### Wariant redakcyjny: rozdzielenie tytułów z alokacją

> ✅ *„Z kwoty [X] zł:
>   1) [Y] zł stanowi wynagrodzenie za korzystanie z wizerunku Wykonawcy w Okresie Przejściowym (do tej kwoty Wykonawca doliczy VAT zgodnie z obowiązującą stawką);
>   2) [Z] zł stanowi zadośćuczynienie i odszkodowanie, nie podlegające VAT."*

— Czyste, ale wymaga decyzji co do podziału (do uzgodnienia z księgowym klienta).

**Stosuj gdy:** klient chce mieć jasność i kontrolę nad reżimem VAT lub gdy stawka VAT dla części świadczenia jest niestandardowa.

### Wariant redakcyjny: odroczenie decyzji

> ✅ *„Strony uzgodnią alokację należności na poszczególne tytuły przed wystawieniem pierwszego dokumentu księgowego. Brak osobnego uzgodnienia oznacza, że pełna kwota traktowana jest jako [tytuł nie podlegający VAT / podlegający VAT]."*

**Stosuj gdy:** podpisanie ugody jest pilne, a kwestia VAT wymaga konsultacji z księgowym, której nie można przeprowadzić przed podpisaniem.

### Reguła operacyjna

Przy każdej ugodzie o płatnościach przekraczających 5 000 zł i obejmującej co najmniej jeden tytuł podlegający VAT — **zawsze konsultuj alokację z księgowym klienta** przed finalizacją tekstu. Nie ma „bezpiecznego defaultu" — wybór wariantu zależy od profilu klienta, charakteru świadczeń i relacji stron.

## Redakcyjny dylemat: „cofnięcie zgody" vs „oświadczenie braku zgody"

Przy ugodach kończących spór o naruszenie dóbr osobistych (zwłaszcza wizerunek — art. 81 PrAut) konstrukcja preambuły musi być spójna z konstrukcją prawną podstawy cofnięcia.

**„Cofnięcie zgody"** zakłada, że zgoda **była wcześniej udzielona** (formalnie lub dorozumianie). W preambule wymaga punktu potwierdzającego udzielenie zgody (lub neutralnego: *„Materiały były rozpowszechniane za wiedzą Wykonawcy"*).

**„Oświadczenie braku zgody na dalsze rozpowszechnianie"** to oświadczenie woli na przyszłość, ex nunc — nie wymaga uprzedniej zgody. Spójne z autonomią reżimu wizerunku.

### Kiedy stosować który wariant

- **„Cofnięcie zgody":** gdy mamy pisemną zgodę z poprzedniego okresu lub fakt udzielenia zgody jest bezsporny i opisany w preambule.
- **„Oświadczenie braku zgody":** gdy formalnej zgody nie było (była dorozumiana), lub gdy preambuła nie potwierdza wprost udzielenia zgody.

Patrz: `references/baza-wiedzy/11-wizerunek-a-prawa-autorskie.md` (punkt o redakcji odwołania zgody).

## Anti-pattern: dublowanie mechanizmów sankcji

W ugodach z elementem zgody warunkowej (np. zgoda na korzystanie z wizerunku/utworu) + osobnym paragrafem o wygaśnięciu — łatwo zduplikować mechanizm sankcji za niewykonanie obowiązków pieniężnych.

**Anti-pattern:**

§ 2 ust. 1 zd. 2:
> ❌ *„Zgoda jest skuteczna pod warunkiem terminowego wykonania przez Zamawiającego obowiązków z § 3, na zasadach z § 6."*

§ 6 ust. 2 pkt 1):
> *„zgoda udzielona w § 2 wygasa z dniem wygaśnięcia Porozumienia"*

**Problem:** dwa różne mechanizmy prawne robią to samo („nie zapłacisz → zgoda przepada"), ale **konstrukcyjnie niespójnie**:
- § 2: warunek zawieszający (art. 89 KC) — *„zgoda staje się skuteczna gdy warunek się ziści"*
- § 6: wygaśnięcie — *„zgoda była skuteczna, ale przestała być"*

Druga strona w sporze może wybrać tę interpretację, która jest dla niej korzystna: *„skoro zgoda jest pod warunkiem zawieszającym, to do dnia pełnej zapłaty zgody w ogóle nie ma — czyli cały okres przejściowy jest bez zgody."*

**Reguła operacyjna:**

- **Jeden mechanizm sankcji = jeden paragraf.**
- Jeśli mechanizm wygaśnięcia jest osadzony w osobnym paragrafie (§ 6) — w klauzuli zgody (§ 2) pisz ją **bez warunku**, jako czystą zgodę ograniczoną czasowo.
- Wygaśnięcie reguluje § 6, który aktywuje się przy niewykonaniu obowiązków pieniężnych — automatycznie pociąga za sobą wygaśnięcie zgody (jeśli § 6 to wprost stanowi).

**Pattern (po naprawie):**

§ 2 ust. 1:
> ✅ *„[Strona] wyraża zgodę na dalsze udostępnianie… w okresie od dnia zawarcia Porozumienia do dnia [data graniczna] włącznie (dalej: „Okres Przejściowy")."*

§ 6 ust. 2 pkt 1) (bez zmian):
> *„zgoda udzielona w § 2 wygasa z dniem wygaśnięcia Porozumienia, a [Druga Strona] zobowiązana jest do natychmiastowego zaprzestania korzystania z Materiałów"*

**Korzyść poboczna (strategiczna):** dla klienta, którego głównym celem jest **otrzymać należne świadczenie pieniężne** (a nie utrzymywać retoryczną kontrolę nad zgodą), prostsza konstrukcja bez warunku ułatwia podpisanie przez drugą stronę. Mniej powodów dla niej do oporu = szybsze podpisanie = szybsze rozliczenie.

**Reguła generalizująca:** dla każdego mechanizmu w ugodzie zadaj sobie pytanie *„czy ten sam efekt nie jest już osiągnięty w innym paragrafie?"* — jeśli tak, jeden z dwóch zapisów jest do wycięcia.
