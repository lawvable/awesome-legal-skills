---
type: Klauzula
title: Regulamin usług elektronicznych / AUP
tags: [regulamin, u.ś.u.d.e., AUP, hosting, SaaS, DSA, AI-Act, domeny, notice-action, konsument, ODR]
contract_types: [SaaS, hosting, platforma, regulamin]
risk_level: wysoki
mandatory_for: [SaaS, hosting, platforma]
requires: [03-definicje.md, 11-odpowiedzialnosc.md, 14-rodo.md]
timestamp: 2026-06-27
---

# Regulamin usług elektronicznych / AUP (hosting, serwery, domeny, AI)

## Kiedy stosować i na co uważać

Regulamin usług świadczonych drogą elektroniczną — hosting, VPS, serwery dedykowane, rejestracja i utrzymanie domen, SaaS, moduły AI. Obowiązkowy na podstawie art. 8 u.ś.u.d.e. Pełni podwójną funkcję: wzorca umowy (art. 384 k.c.) i wykonania obowiązku ustawowego. Postanowień nieudostępnionych klientowi przed zawarciem umowy nie można na niego powoływać.

### ⚠️ Red flags

Brak dostępnego publicznie regulaminu (obowiązek ustawowy). Regulamin bez procedury notice & action (wymóg DSA). Zakaz treści bezprawnych bez żadnego katalogu. Brak uzasadnienia decyzji o blokadzie treści (wymóg DSA art. 17). Wyłączenie odpowiedzialności za wady produktu bez wyłączenia winy umyślnej — nieskuteczne wobec konsumentów. Brak trybu zmiany regulaminu z prawem wypowiedzenia. Klauzula „usługodawca może wedle uznania" bez wskazania przesłanek. Ściana tekstu bez struktury — naruszenie standardu przejrzystości DSA.

### Klauzula wzorcowa — zakaz treści bezprawnych (generyczny)

> Usługobiorca jest zobowiązany do korzystania z usług zgodnie z obowiązującymi przepisami prawa, postanowieniami niniejszego Regulaminu oraz dobrymi obyczajami. Zakazane jest w szczególności: (a) przechowywanie lub transmisja treści naruszających prawa autorskie lub prawa pokrewne; (b) przechowywanie lub transmisja treści naruszających dobra osobiste osób trzecich; (c) rozsyłanie niezamówionej korespondencji elektronicznej (spam); (d) przeprowadzanie lub inicjowanie ataków na systemy informatyczne (DDoS, skanowanie portów, brute-force); (e) rozpowszechnianie złośliwego oprogramowania; (f) przechowywanie treści o charakterze karnoprawnym, w tym pornografii dziecięcej i treści nawołujących do nienawiści. W przypadku usług opartych na systemach AI: zakaz obejmuje wprowadzanie do systemu AI danych o charakterze bezprawnym oraz wykorzystywanie wyników systemu AI do generowania lub dystrybucji treści objętych powyższymi zakazami.

### Klauzula wzorcowa — wyłączenie odpowiedzialności hostingu (generyczny)

> Usługodawca nie ponosi odpowiedzialności za treści przechowywane przez usługobiorców na infrastrukturze usługodawcy, pod warunkiem że usługodawca nie posiada wiedzy o bezprawnym charakterze tych treści lub — po uzyskaniu wiarygodnej wiadomości o ich bezprawności — niezwłocznie uniemożliwi dostęp do tych treści. Usługodawca nie jest zobowiązany do ogólnego nadzoru nad przechowywanymi danymi ani do ich aktywnego poszukiwania. Usługodawca jest uprawniony do dobrowolnego monitorowania treści i podejmowania dobrowolnych czynności sprawdzających, przy zachowaniu wyłączenia odpowiedzialności, o którym mowa w zdaniu pierwszym.

## Klauzule KTZR — regulaminy usług IT

### Definicje — System AI i Usługi AI

⚠️ Definicja poniżej pochodzi z konkretnej umowy i ma charakter własny (nie odwołuje się do AI Act). Przy nowych umowach preferuj definicję z art. 3 pkt 1 AI Act — patrz sekcja „Definicja Systemu AI — odesłanie do AI Act" poniżej.

> „System AI" — funkcjonalność systemu teleinformatycznego Usługodawcy oparta na modelu obliczeniowym zdolnym do przetwarzania danych wejściowych i generowania wyników, w szczególności treści, klasyfikacji, prognoz lub rekomendacji, udostępniana Usługobiorcom w ramach Usług.

> „Usługi AI" — usługi świadczone drogą elektroniczną polegające na udostępnianiu Usługobiorcom Systemu AI lub wyników jego działania za pośrednictwem systemu teleinformatycznego Usługodawcy.

> „AUP" (Acceptable Use Policy / Zasady dopuszczalnego korzystania) — zasady prawidłowego korzystania z Usług, stanowiące integralną część niniejszego Regulaminu.

> „SLA" (Service Level Agreement) — deklarowany poziom świadczenia Usług w zakresie dostępności, czasów reakcji na zgłoszenia i parametrów technicznych, określony w § [___].

### Zawarcie umowy i moment związania regulaminem

> Umowa o świadczenie Usług zostaje zawarta z chwilą rejestracji Konta przez Usługobiorcę i akceptacji niniejszego Regulaminu, co jest równoznaczne z zapoznaniem się z jego treścią i wyrażeniem zgody na jego postanowienia. Usługodawca potwierdza zawarcie umowy wiadomością e-mail na adres wskazany przez Usługobiorcę przy rejestracji.

> Regulamin jest udostępniony nieodpłatnie pod adresem [___] w wersji umożliwiającej jego pobranie, odtworzenie i utrwalenie. Usługobiorca niebędący konsumentem potwierdza fakt zapoznania się z Regulaminem przez złożenie oświadczenia przy rejestracji lub złożeniu zamówienia.

### Parametry SLA dla usług hostingowych

> Usługodawca gwarantuje dostępność infrastruktury hostingowej (Uptime) na poziomie nie niższym niż [___]% w skali miesiąca kalendarzowego, mierzoną przez zewnętrzny system monitorujący. Do czasu niedostępności nie wlicza się: (a) zaplanowanych okien serwisowych uzgodnionych z co najmniej 48-godzinnym wyprzedzeniem, łącznie nie więcej niż [___] godziny miesięcznie, planowanych poza godzinami szczytu; (b) niedostępności wynikającej z działania siły wyższej; (c) przerw spowodowanych działaniami Usługobiorcy lub osób, za które ponosi on odpowiedzialność.

### Parametry SLA dla usług AI

> Usługodawca deklaruje dostępność Systemu AI na poziomie określonym w Cenniku dla danego planu usług. Parametry techniczne (dostępność interfejsu, czas odpowiedzi, limity zapytań miesięcznych) mają charakter wiążący w zakresie wynikającym z SLA. Usługodawca nie gwarantuje osiągnięcia określonego poziomu merytorycznej poprawności lub trafności wyników generowanych przez System AI — wyniki mają charakter pomocniczy i wymagają weryfikacji przez Usługobiorcę.

### Zasady korzystania z systemów AI — AUP (blok szczegółowy)

> Usługobiorca korzystający z Usług AI zobowiązuje się do:
> 1. nieprzekazywania do Systemu AI danych lub treści o charakterze bezprawnym;
> 2. niekorzystania z Systemu AI w celu generowania lub dystrybucji spamu, phishingu, złośliwego oprogramowania ani treści bezprawnych;
> 3. niestosowania Systemu AI do masowego generowania treści wprowadzających w błąd co do tożsamości autora lub podszywania się pod osoby lub podmioty trzecie;
> 4. weryfikowania wyników Systemu AI przed ich zastosowaniem w procesach decyzyjnych mających istotne skutki prawne, finansowe lub medyczne;
> 5. niepodejmowania prób obejścia technicznych zabezpieczeń Systemu AI.

> Usługobiorca ponosi wyłączną odpowiedzialność za treści przekazywane do Systemu AI jako dane wejściowe oraz za sposób i skutki zastosowania wyników Systemu AI wobec osób trzecich.

### Procedura notice & action — zgłaszanie treści nielegalnych

> Każda osoba, której prawa zostały naruszone przez treści przechowywane przez Usługobiorców w ramach Usług, może zgłosić ten fakt Usługodawcy na adres: [___] lub przez formularz dostępny pod adresem [___]. Zgłoszenie powinno zawierać: (a) dane umożliwiające identyfikację zgłaszającego; (b) wskazanie treści objętej zgłoszeniem; (c) wskazanie przepisu prawa lub prawa, które zostało naruszone; (d) oświadczenie zgłaszającego o działaniu w dobrej wierze.

> Usługodawca rozpatruje zgłoszenie bez zbędnej zwłoki. W przypadku podjęcia decyzji o ograniczeniu dostępu do treści, Usługodawca informuje Usługobiorcę, którego treści dotyczą zgłoszenie, o powodach decyzji, jej zakresie i trybie odwoławczym — chyba że poinformowanie groziłoby ujawnieniem informacji objętych tajemnicą służbową lub zagroziłoby czynnościom organów ścigania.

### Zawieszenie i rozwiązanie umowy ze skutkiem natychmiastowym

> Usługodawca jest uprawniony do zawieszenia świadczenia Usług ze skutkiem natychmiastowym, bez konieczności uprzedniego wezwania, w przypadku: (a) rażącego lub powtarzającego się naruszenia AUP; (b) zaległości w opłacie wymagalnej przez więcej niż [___] dni; (c) prowadzenia przez Usługobiorcę działalności zagrażającej bezpieczeństwu systemów Usługodawcy lub systemów osób trzecich; (d) urzędowego nakazu lub zabezpieczenia sądowego zobowiązującego do usunięcia lub zablokowania dostępu do treści.

> Usługodawca informuje Usługobiorcę o zawieszeniu Usług i jego przyczynie wiadomością e-mail na adres wskazany przy rejestracji lub komunikatem w Panelu klienta, z jednoczesnym podaniem terminu, w którym Usługobiorca może usunąć naruszenie. Bezskuteczny upływ terminu uprawnia Usługodawcę do rozwiązania umowy.

### Zasady świadczenia usług domenowych — rola pośrednika

> Usługodawca rejestruje i utrzymuje domeny jako akredytowany rejestrator lub partner rejestratora uprawnionego przez właściwy rejestr. W zakresie rejestracji i utrzymania domen zastosowanie mają regulaminy właściwych rejestrów (wskazane w Cenniku lub Panelu klienta), które mają pierwszeństwo przed postanowieniami niniejszego Regulaminu w zakresie warunków rejestracji i utrzymania nazwy domeny.

> W przypadku braku opłaty za przedłużenie domeny w terminie wskazanym w Cenniku, Usługodawca podejmuje próbę powiadomienia Usługobiorcy na co najmniej [___] dni przed datą wygaśnięcia. Po wygaśnięciu domeny jej odzyskanie może być niemożliwe lub wiązać się z dodatkowymi kosztami, za co Usługodawca nie ponosi odpowiedzialności.

### Zmiana Regulaminu

> Usługodawca jest uprawniony do zmiany Regulaminu w przypadku: (a) zmian obowiązujących przepisów prawa; (b) zmian w ofercie usług lub infrastrukturze technicznej; (c) modyfikacji lub aktualizacji Systemów AI; (d) zmian w regulaminach rejestrów domenowych; (e) decyzji organów regulacyjnych.

> O każdej zmianie Regulaminu Usługodawca informuje Usługobiorców nie później niż [___] dni przed datą wejścia zmiany w życie — wiadomością e-mail na adres wskazany przy rejestracji lub komunikatem w Panelu klienta. Usługobiorca, który nie akceptuje zmian, ma prawo wypowiedzieć umowę ze skutkiem na dzień wejścia zmian w życie.

### Uprawnienia konsumenta — prawo odstąpienia

> Usługobiorca będący konsumentem ma prawo odstąpić od umowy zawartej na odległość w terminie 14 dni od jej zawarcia, bez podawania przyczyny, składając jednoznaczne oświadczenie na adres e-mail [___]. Prawo odstąpienia nie przysługuje, w przypadku gdy Usługodawca — za wyraźną uprzednią zgodą konsumenta, z jednoczesnym poinformowaniem o utracie prawa odstąpienia — wykonał usługę w pełni przed upływem terminu do odstąpienia.

### Postanowienia końcowe

> Regulamin podlega prawu polskiemu. Wszelkie spory wynikające z niniejszego Regulaminu rozstrzygane są przez sąd właściwy dla siedziby Usługodawcy, z uwzględnieniem przepisów ochronnych dla konsumentów w zakresie właściwości miejscowej sądu. Konsument może skorzystać z pozasądowych metod rozwiązywania sporów (ODR: https://commission.europa.eu/consumers/odr).

> W przypadku gdy którekolwiek z postanowień Regulaminu zostanie uznane za nieważne lub bezskuteczne, pozostałe postanowienia zachowują moc (klauzula salwatoryjna). W sprawach nieuregulowanych zastosowanie mają przepisy Kodeksu cywilnego i ustawy o świadczeniu usług drogą elektroniczną.

---

## Zasady redakcji regulaminów — wnioski z praktyki KTZR

### Struktura umowna w serwisach z rejestracją i planami (SaaS)

W serwisach oferujących rejestrację Konta i Plany Abonamentowe stosuj dwupoziomową strukturę umowną — zdefiniowaną w § Definicje i opisaną hierarchicznie w § Zawarcie umowy:

**§ Definicje:**
> „Umowa ramowa" — umowa o świadczenie Usług zawarta z chwilą rejestracji Konta i akceptacji Regulaminu; określa ogólne warunki korzystania z Platformy i stanowi podstawę dla Umów Planowych.

> „Umowa Planowa" — umowa szczegółowa zawierana w ramach Umowy ramowej z chwilą aktywacji wybranego Planu Abonamentowego; określa zakres Usług i wynagrodzenie odpowiadające danemu Planowi.

**§ Zawarcie umowy:**
> 1. Umowa ramowa zostaje zawarta z chwilą rejestracji Konta i akceptacji Regulaminu. Usługodawca potwierdza zawarcie wiadomością e-mail na adres wskazany przy rejestracji w terminie nie dłuższym niż [___] dzień roboczy.
> 2. Zakres Usług w każdym okresie rozliczeniowym określa Umowa Planowa, zawierana z chwilą aktywacji wybranego Planu przez Usługodawcę. W przypadku zmiany Planu nowa Umowa Planowa zastępuje poprzednią ze skutkiem od początku kolejnego okresu rozliczeniowego.

❌ Anti-pattern: jedno zdanie scalające rejestrację i wybór Planu w jedną "chwilę zawarcia umowy" — miesza dwie odrębne czynności prawne.

### Definicja Systemu AI — odesłanie do AI Act (Rozp. 2024/1689)

Nie definiuj Systemu AI własną definicją ogólną — użyj definicji z art. 3 pkt 1 AI Act i wskaż role stron:

> „System AI" — system sztucznej inteligencji w rozumieniu art. 3 pkt 1 Rozporządzenia Parlamentu Europejskiego i Rady (UE) 2024/1689 z dnia 13 czerwca 2024 r. w sprawie sztucznej inteligencji (AI Act), zintegrowany z Platformą, służący do [opis funkcjonalności]; dostępny wyłącznie w [Planach X].
> Usługodawca pełni rolę dostawcy w rozumieniu art. 3 pkt 3 AI Act; Usługobiorca korzystający z Systemu AI pełni rolę podmiotu wdrażającego w rozumieniu art. 3 pkt 4 AI Act.

⚠️ Klasyfikację ryzyka (niskie / wysokie) weryfikuj każdorazowo pod kątem Załącznika III AI Act dla konkretnego przypadku użycia — nie stosuj domyślnie "niskie ryzyko". Wysokie ryzyko (np. zastosowanie w procesach kadrowych, kredytowych, sądowych) uruchamia obowiązki z art. 9–16 AI Act po stronie dostawcy.

### AUP dla Systemu AI — klauzula obowiązków podmiotu wdrażającego

> Usługobiorca jako podmiot wdrażający System AI w rozumieniu art. 3 pkt 4 AI Act zobowiązuje się do:
> 1) niestosowania Systemu AI do celów zabronionych na podstawie art. 5 AI Act — w szczególności do manipulacji behawioralnej, biometrycznej kategoryzacji osób ani systemów oceny społecznej;
> 2) nieprzekazywania do Systemu AI danych szczególnych kategorii w rozumieniu art. 9 RODO, chyba że dokumentacja techniczna Platformy wyraźnie to dopuszcza;
> 3) weryfikacji wyników Systemu AI przed ich zastosowaniem w procesach wywołujących skutki prawne, finansowe lub organizacyjne wobec osób fizycznych — wymóg nadzoru ludzkiego (human oversight); uwaga: art. 26 ust. 1 lit. d AI Act dotyczy wyłącznie systemów wysokiego ryzyka (Załącznik III AI Act) — dla systemów niskiego ryzyka nadzór ludzki jest dobrą praktyką, nie obowiązkiem ustawowym;
> 4) niepodejmowania prób inżynierii odwrotnej ani obchodzenia technicznych zabezpieczeń Systemu AI;
> 5) niezwłocznego powiadomienia Usługodawcy [kanał + termin] o każdym działaniu Systemu AI niezgodnym z jego deklarowanym przeznaczeniem lub mogącym stanowić poważny incydent w rozumieniu art. 3 pkt 49 AI Act.

### Treści wprowadzane do platformy — oświadczenie o uprawnieniach (nie licencja)

❌ Anti-pattern — "licencja na przetwarzanie danych": miesza dwa różne reżimy prawne:
- dane osobowe → podstawa przetwarzania wynika z DPA (art. 28 RODO) — nie potrzeba licencji
- treści chronione prawem autorskim → tu jest podstawa dla odrębnej klauzuli, ale nie "licencja na przetwarzanie"

✅ Prawidłowa konstrukcja — oświadczenie o uprawnieniach do treści:
> Usługobiorca oświadcza, że dysponuje prawami lub uprawnieniami do treści wprowadzanych do Platformy w zakresie umożliwiającym ich przetwarzanie przez Usługodawcę — w tym utrwalanie, zwielokrotnianie i analizę przez System AI — wyłącznie w celu świadczenia Usług. Usługodawca nie nabywa żadnych praw do tych treści ponad zakres niezbędny do świadczenia Usług.

Zamiana z licencji (przyznanie praw) na gwarancję (zapewnienie, że Usługobiorca sam ma uprawnienia) — poprawna konstrukcja, bo to Usługobiorca odpowiada za legalność wprowadzanych treści.
