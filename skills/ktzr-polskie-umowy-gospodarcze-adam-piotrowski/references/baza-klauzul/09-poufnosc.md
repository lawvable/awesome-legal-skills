---
type: Klauzula
title: Poufność
tags: [poufność, NDA, informacje-poufne, tajemnica-przedsiębiorstwa, breach-notification, wykluczenia, 72h]
contract_types: [NDA, body-leasing, licencyjna, ramowa, B2B-IT]
risk_level: wysoki
mandatory_for: [NDA]
requires: [03-definicje.md, 18-zwrot-materialow.md]
timestamp: 2026-06-27
---

# Poufność

## Kiedy stosować i na co uważać

Ochrona informacji poufnych obu stron. W IT obejmuje kod źródłowy, architekturę systemów, dane klientów, know-how technologiczny. Może być w umowie głównej lub jako osobne NDA.

### ⚠️ Red flags

Brak definicji informacji poufnych. Brak okresu obowiązywania po zakończeniu umowy. Obowiązek poufności tylko jednostronny. Brak wyłączeń (informacje publiczne, uzyskane niezależnie, wymagane prawem). Brak kary umownej — trudna egzekucja.

### Klauzula wzorcowa (generyczny IT)

> Strona Otrzymująca zobowiązuje się do: (a) zachowania Informacji Poufnych w ścisłej tajemnicy; (b) wykorzystywania ich wyłącznie w celu realizacji Umowy; (c) ujawniania ich wyłącznie osobom, których udział jest niezbędny, pod warunkiem zobowiązania ich do poufności. Obowiązek poufności obowiązuje przez okres trwania Umowy oraz 3 lata po jej wygaśnięciu. Kara umowna za naruszenie: [kwota] PLN za każdy przypadek.

## Klauzule z umów KTZR

### NDA IT (KTZR)

> Strona Otrzymująca zobowiązuje się do: zachowania Informacji Poufnych w ścisłej tajemnicy; wykorzystywania ich wyłącznie w celu realizacji Projektu; zastosowania co najmniej takiej samej staranności przy ochronie, z jaką chroni własne informacje poufne — jednak nie mniejszej niż należyta staranność wymagana od profesjonalisty.

> Zobowiązanie do zachowania poufności obowiązuje przez 5 (pięć) lat od dnia zakończenia Projektu lub rozmów między Stronami — niezależnie od przyczyny zakończenia współpracy.

> Za Informacje Poufne nie uznaje się informacji, które: (a) są publicznie dostępne w sposób inny niż w wyniku naruszenia Umowy; (b) były w posiadaniu Strony Otrzymującej przed ich ujawnieniem; (c) zostały niezależnie opracowane; (d) uzyskane od osoby trzeciej bez obowiązku poufności; (e) muszą być ujawnione na podstawie przepisów prawa. Ciężar dowodu wyłączeń spoczywa na Stronie Otrzymującej.

> Niezwłoczne — nie później niż w ciągu 72 godzin — pisemne powiadomienie Strony Ujawniającej o każdym przypadku nieuprawnionego ujawnienia, utraty, kradzieży lub uzasadnionym podejrzeniu naruszenia poufności.

> ⚠️ **Przy łączeniu z klauzulą Poufność techniczna** (sekcja poniżej): stosuj termin 24-godzinny jako lex specialis — usuń termin 72-godzinny z wersji końcowej, aby uniknąć sprzeczności.

### Body Leasing IT (KTZR)

> Usługodawca zobowiązuje się do zawarcia ze Specjalistami odrębnych umów o zachowaniu poufności (NDA) w zakresie co najmniej równoważnym z niniejszym paragrafem, przed przystąpieniem Specjalisty do świadczenia Usług.

### Umowa ramowa współpracy prowizyjnej

> Wszelkie informacje przekazane przez Zleceniodawcę w jakiejkolwiek formie, niezależnie od opatrzenia ich klauzulą „Informacje poufne”, stanowią informacje poufne i nie będą (również po okresie obowiązywania Umowy) użyte przez Partnera do innego celu niż należyta realizacja Umowy.

### Umowa licencyjno-doradcza

> Licencjobiorca zobowiązuje się do zachowania w ścisłej tajemnicy wszelkich Informacji Poufnych zarówno w trakcie trwania Umowy, jak i bezterminowo po jej zakończeniu.

### Poufność techniczna (IT — kod źródłowy, dane dostępowe, infrastruktura)

> Informacje Poufne obejmują w szczególności: (a) dane techniczne — kod źródłowy, architekturę systemów, loginy, hasła, certyfikaty SSL, klucze API, parametry środowiskowe; (b) dane operacyjne — bazy danych, warunki handlowe, know-how procesowe; (c) dane finansowe — obroty, marże, koszty operacyjne; (d) plany biznesowe — projekty nowych modułów, strategie rozwoju. W razie wątpliwości co do charakteru danej informacji domniemywa się, że stanowi Informację Poufną.

> Strona Otrzymująca nie jest uprawniona do kopiowania, eksportowania, pobierania ani przechowywania poza infrastrukturą Strony Ujawniającej żadnych danych, kodu źródłowego ani innych Informacji Poufnych. Zakaz obejmuje wszelkie formy i nośniki, w tym pliki lokalne, nośniki zewnętrzne, usługi chmurowe i prywatne repozytoria. Dozwolone są wyłącznie zatwierdzone kopie zapasowe.

> W przypadku powzięcia podejrzenia o nieuprawnionym dostępie do Informacji Poufnych, ich utraty lub ujawnienia, Strona Otrzymująca zobowiązuje się powiadomić Stronę Ujawniającą w formie dokumentowej nie później niż w ciągu 24 godzin od powzięcia informacji. Brak terminowego poinformowania traktowany jest jako odrębne naruszenie poufności.

> Strona Ujawniająca ma prawo do bieżącego monitorowania aktywności Strony Otrzymującej w zakresie korzystania z udostępnionych zasobów, w tym przeglądania logów i przeprowadzania audytów bezpieczeństwa.

> Obowiązki z niniejszego paragrafu wiążą przez cały okres obowiązywania Umowy oraz przez 10 lat od daty jej zakończenia, niezależnie od przyczyny. Dla informacji stanowiących tajemnicę przedsiębiorstwa w rozumieniu art. 11 ust. 2 u.z.n.k. obowiązek poufności jest bezterminowy.
