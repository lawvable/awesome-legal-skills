---
type: Klauzula
title: Preambuły i oświadczenia stron
tags: [preambuła, oświadczenia, ugoda, charakter-umowy, zważywszy-że, definicja-zamknięta]
contract_types: [ugoda, body-leasing, NDA, licencyjna, usługi-księgowe]
risk_level: średni
mandatory_for: [ugoda]
requires: [03-definicje.md]
timestamp: 2026-06-27
---

# Preambuły i oświadczenia stron

## Zasada długości preambuły

**Co do zasady preambuła ma być zwięzła.** W prostych B2B, NDA, cesji, umowach o świadczenie usług — preambuła nie jest konieczna albo ogranicza się do oświadczenia o charakterze umowy (par. 1 ust. 1) bez bloku „ZWAŻYWSZY, ŻE".

**Wyjątek — historia stron rozpisana:** w **ugodach (art. 917 KC) i porozumieniach kończących spór** preambuła może (i często powinna) być rozpisana — bo czyni zrozumiałym **przedmiot wzajemnych ustępstw**. W bloku „ZWAŻYWSZY, ŻE: A. … G." osadzasz:
- chronologię stosunku stron (od kiedy, na jakiej podstawie),
- zdarzenie wywołujące spór (pismo, data, treść roszczenia),
- stanowiska stron co do podstawy prawnej sporu (neutralnie — „Strony przyjęły rozbieżne stanowiska co do…"),
- intencję polubownego zakończenia.

**Reguła operacyjna dla ugód:** dokumentujesz fakty (daty, numery przesyłek, wysokość roszczeń) — **nie ocenę**. „Zamawiający kontynuował publikację" zamiast „Zamawiający bezprawnie naruszał wizerunek". Druga strona musi to podpisać — preambuła nie może czytać się jak pozew.

**Test redakcyjny dla preambuły ugody:**
- czy każdy punkt A./B./C. wnosi fakt potrzebny do zrozumienia ustępstw w klauzulach merytorycznych? Jeśli nie — usuń;
- czy język jest neutralny (do podpisania przez obie strony), a nie polemiczny (jak w wezwaniu do zapłaty)?
- czy odesłania do przepisów ograniczyłeś do tych z funkcją prawną (np. art. 81 ust. 1 PrAut przy odwołaniu zgody na wizerunek)? Odesłanie do art. 917 KC daj w klauzule końcowej, nie w preambule.

## Anti-patterns w preambułach (do unikania)

### 1. Backdoor'em aktywujące klauzule poprzedniej umowy

> ❌ *„…po jej wygaśnięciu Strony kontynuowały współpracę bez zachowania formy pisemnej, **jednak kierując się treścią w zakresie praw i obowiązków Stron**;"*

W ugodzie kończącej spór, fraza *„kierując się treścią"* dawałaby drugiej stronie argument, że konkretna klauzula wygasłej umowy (np. dotycząca przejścia praw autorskich) obowiązywała także w spornym okresie — czyli odwrotnie do intencji klienta wnoszącego ugodę.

**Poprawka — wariant najczystszy:**
> ✅ *„…po jej wygaśnięciu Strony kontynuowały współpracę bez zachowania formy pisemnej."*

Patrz: `style-redakcyjny.md` → W8 (Nie aktywuj backdoor'em klauzul z wygasłych umów).

### 2. „Cofnięcie zgody" bez wcześniejszego potwierdzenia, że zgoda była

W preambule ugody dotyczącej dóbr osobistych (np. wizerunku) pkt w formie *„[Strona] cofnęła zgodę"* zakłada, że zgoda była wcześniej udzielona. Jeśli wcześniejszy pkt potwierdzający udzielenie zgody został usunięty — kolejny pkt staje się logicznie zawieszony i daje drugiej stronie argument, że *„skoro nie było formalnej zgody, to nie ma czego cofać → wszystkie wcześniejsze działania były bez podstawy → ugoda jest ich zalegalizowaniem."*

**Dwie ścieżki naprawy:**

1. **Wrócić pkt potwierdzający w wersji łagodnej:**
> ✅ *„C. w okresie współpracy Materiały były rozpowszechniane za wiedzą [Strony];"*

Słowo *„zgoda"* zastąpione *„wiedzą"* — neutralne, nie potwierdza formalnej zgody, a zachowuje logikę kolejnego punktu.

2. **Przeformułować pkt na oświadczenie braku zgody:**
> ✅ *„D. pismem z dnia [data] [Strona] **oświadczyła brak zgody** na dalsze rozpowszechnianie swojego wizerunku przez [Drugą Stronę] po dniu [data];"*

Eliminuje słowo *„cofnęła"* (nie wymaga wcześniejszej formalnej zgody) i jest spójne z autonomią reżimu wizerunku (art. 81 ust. 1 PrAut — oświadczenie woli na przyszłość, ex nunc).

### 3. Przyznanie faktów spornych w preambule

Preambuła ma dokumentować *fakty bezsporne* (chronologia, pisma, daty, kwoty), nie *oceny prawne* czy *interpretacje*. Każdy element typu *„Strony zgodnie potwierdzają, że…"* przy kwestii spornej — to potencjalne źródło problemu w przyszłym sporze. Przed wysłaniem stosuj filtr: *„czy każdy fakt z preambuły wnosi do logiki ugody, czy może być wykorzystany przeciwko klientowi w przyszłości?"*

## Technika: definicja jako zbiór zamknięty

Gdy preambuła wprowadza definicję pojęcia używanego później w klauzulach (*„Materiały"*, *„Projekt"*, *„Usługi"*, *„Roszczenia"*), warto **zawężać zakres na poziomie definicji**, a nie powtarzać zawężenia w każdej klauzule.

**Anti-pattern (zbiór otwarty czasowo):**
> ❌ *„…nagrania wykładów zawierające wizerunek [Strony] są udostępniane słuchaczom kursów odpłatnie… (dalej: „Materiały");"*

*„Materiały"* obejmują też nagrania powstające PO zawarciu ugody — czyli druga strona może argumentować, że ugoda dotyczy także nowych utrwaleń.

**Pattern (zbiór zamknięty):**
> ✅ *„…**nagrania utrwalone w toku tej współpracy**, zawierające wizerunek [Strony], są udostępniane słuchaczom kursów odpłatnie… (dalej: „Materiały");"*

Fraza *„utrwalone w toku tej współpracy"* (lub równoważne: *„utrwalone do dnia [X]"*, *„powstałe w okresie [Y]"*) **zamyka kalendarz**. Definicja staje się zbiorem zamkniętym, niezależnie od dalszego biegu zdarzeń.

**Korzyść:** wszystkie późniejsze klauzule używające zdefiniowanego pojęcia (np. § zgoda na korzystanie, § obowiązek usunięcia, § wynagrodzenie za korzystanie poza okresem przejściowym, § wygaśnięcie, § RODO) **automatycznie dziedziczą zawężenie**. Nie trzeba powtarzać w każdej z nich, że dotyczą *„tylko istniejących"*.

**Komplement:** dla pełnej szczelności warto dodatkowo wprowadzić w klauzulach materialnych **klauzulę autonomii zakresowej** (typowo w § 2 dla ugód wizerunkowych), wykluczającą rozszerzanie zakresu zgody na nowe wykorzystania:

> *„Porozumienie nie obejmuje zgody na utrwalanie ani wykorzystywanie wizerunku Wykonawcy w jakichkolwiek nowych materiałach powstających po dniu zawarcia Porozumienia."*

Razem (zawężenie definicji + klauzula autonomii) zamykają zarówno kalendarz, jak i zakres przedmiotowy.

## Klauzule z umów KTZR

### Body Leasing IT (KTZR)

> Strony zgodnie oświadczają, że: (i) Umowa jest umową o świadczenie usług zawartą między przedsiębiorcami, której przedmiotem jest wyłącznie wykonanie określonych czynności prawnych oraz faktycznych na rzecz Usługobiorcy przez Specjalistów; (ii) Umowa nie kreuje stosunku pracy w rozumieniu art. 22 § 1 Kodeksu pracy; (iii) Specjaliści są niezależnymi przedsiębiorcami (B2B) lub osobami współpracującymi z Usługodawcą na podstawie umów cywilnoprawnych i żadne z postanowień Umowy nie wyłącza ich samodzielności zawodowej.

> Umowa ma charakter ramowy. Prawa i obowiązki Stron w odniesieniu do konkretnych Usług określają Zamówienia, które po obustronnym podpisaniu stają się integralną częścią Umowy.

### Umowa licencyjno-doradcza

> ZWAŻYWSZY, ŻE: A. Licencjodawca jest organizacją posiadającą specjalistyczną wiedzę, doświadczenie oraz sprawdzone metody działania w zakresie tworzenia i prowadzenia jednostek biznesowych w [___] sektorze. [...] D. Licencjobiorca jest zainteresowany uzyskaniem licencji na korzystanie z Know-how Licencjodawcy oraz otrzymywaniem wsparcia doradczego.

### Umowa o usługi księgowe

> Strony oświadczają, że Zleceniobiorca posiada uprawnienia niezbędne do usługowego prowadzenia ksiąg rachunkowych oraz posiada ważne ubezpieczenie od odpowiedzialności cywilnej za szkody wyrządzone w związku z prowadzoną działalnością.

### NDA IT (KTZR)

> Zawarcie niniejszej Umowy nie stanowi zobowiązania żadnej ze Stron do zawarcia umowy głównej dotyczącej Projektu ani do kontynuowania rozmów oraz negocjacji.

### Udostępnienie lokalu

> Udostępnienie lokalu [Korzystającemu] na mocy niniejszej Umowy nie jest umową najmu ani dzierżawy w rozumieniu przepisów Kodeksu cywilnego ani nie podlega przepisom ustawy z dnia 21 czerwca 2001 r. o ochronie praw lokatorów.
