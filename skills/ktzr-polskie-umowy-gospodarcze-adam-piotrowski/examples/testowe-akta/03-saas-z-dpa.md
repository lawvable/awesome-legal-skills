> ⚠️ **DOKUMENT TESTOWY — DANE FIKCYJNE**
> Spółki, numery KRS/NIP/REGON, adresy i osoby są zmyślone.
> Plik służy do testowania skilla bez angażowania danych klientów.
> Celowo zawiera kilka błędów i luk — skill powinien je wykryć.

---

# UMOWA O ŚWIADCZENIE USŁUG OPROGRAMOWANIA JAKO USŁUGI (SaaS)
## wraz z Umową Powierzenia Przetwarzania Danych Osobowych

zawarta w Gdańsku, dnia 1 maja 2026 r., pomiędzy:

**ALFA SOLUTIONS SPÓŁKA Z OGRANICZONĄ ODPOWIEDZIALNOŚCIĄ** z siedzibą w Gdańsku, ul. Długa 14/3, 80-827 Gdańsk, KRS: **0000999001**, NIP: **5833399001**, reprezentowaną przez Annę Kowalską — Prezesa Zarządu,

zwaną dalej „**Dostawcą**" lub „**Podmiotem Przetwarzającym**",

a

**DELTA RETAIL SPÓŁKA Z OGRANICZONĄ ODPOWIEDZIALNOŚCIĄ** z siedzibą w Krakowie, ul. Floriańska 8/2, 31-019 Kraków, KRS: **0000999004**, NIP: **6762399004**, REGON: **389004004**, reprezentowaną przez Monikę Zając — Prezesa Zarządu,

zwaną dalej „**Klientem**" lub „**Administratorem**".

---

## CZĘŚĆ I — UMOWA SaaS

### §1. Przedmiot

1. Dostawca zobowiązuje się świadczyć Klientowi dostęp do platformy zarządzania sprzedażą „AlfaSales" (dalej: „**Platforma**") za pośrednictwem sieci Internet, w modelu SaaS.
2. Platforma umożliwia zarządzanie zamówieniami, stanami magazynowymi i raportowanie sprzedaży.

### §2. Dostęp i licencja

1. Dostawca udziela Klientowi niewyłącznej, niezbywalnej licencji na korzystanie z Platformy na czas trwania Umowy.
2. Klient może tworzyć konta dla maksymalnie 25 (dwudziestu pięciu) użytkowników.
3. Klient nie jest uprawniony do sublicencjonowania, modyfikowania ani dekompilowania Platformy.

### §3. Poziom usług (SLA)

1. Dostawca dołoży wszelkich starań, aby Platforma była dostępna przez 24 godziny na dobę, 7 dni w tygodniu.
2. Planowane przerwy techniczne będą ogłaszane z wyprzedzeniem.

### §4. Wynagrodzenie i subskrypcja

1. Klient zobowiązuje się do zapłaty miesięcznego abonamentu w wysokości **2.400,00 zł netto** + VAT.
2. Abonament płatny z góry za każdy miesiąc, na podstawie faktury wystawianej pierwszego dnia miesiąca.
3. Umowa zawarta jest na czas określony 12 miesięcy, a następnie ulega automatycznemu przedłużeniu na kolejne okresy 12-miesięczne.
4. Płatność: 14 dni od daty faktury.

### §5. Odpowiedzialność Dostawcy

1. Dostawca nie ponosi odpowiedzialności za przerwy w dostępie do Platformy wynikające z awarii infrastruktury zewnętrznej.
2. Strony wyłączają odpowiedzialność za utracone korzyści oraz szkody pośrednie.
3. Odpowiedzialność Dostawcy ograniczona jest do wartości abonamentu zapłaconego przez Klienta w miesiącu, w którym powstała szkoda.

### §6. Wypowiedzenie

Klient może wypowiedzieć Umowę z zachowaniem 30-dniowego okresu wypowiedzenia, ze skutkiem na koniec okresu abonamentowego.

---

## CZĘŚĆ II — UMOWA POWIERZENIA PRZETWARZANIA DANYCH OSOBOWYCH

### §7. Podstawa i cel powierzenia

Na podstawie art. 28 Rozporządzenia Parlamentu Europejskiego i Rady (UE) 2016/679 (RODO), Administrator powierza Podmiotowi Przetwarzającemu przetwarzanie danych osobowych w związku ze świadczeniem usług opisanych w Części I.

### §8. Zakres i cel przetwarzania

1. Podmiot Przetwarzający przetwarza dane osobowe wyłącznie na udokumentowane polecenie Administratora.
2. Kategorie danych: dane identyfikacyjne i kontaktowe klientów Administratora (imię, nazwisko, adres e-mail, numer telefonu, adres dostawy).
3. Cel przetwarzania: obsługa zamówień za pośrednictwem Platformy.

### §9. Obowiązki Podmiotu Przetwarzającego

1. Podmiot Przetwarzający zobowiązuje się do wdrożenia odpowiednich środków technicznych i organizacyjnych zapewniających bezpieczeństwo przetwarzanych danych.
2. Podmiot Przetwarzający może korzystać z usług podpodmiotów przetwarzających po poinformowaniu Administratora.
3. Po zakończeniu Umowy Podmiot Przetwarzający usunie lub zwróci dane osobowe.

### §10. Postanowienia końcowe

1. Wszelkie zmiany Umowy wymagają formy pisemnej pod rygorem nieważności.
2. Prawo właściwe: prawo polskie.
3. Sąd właściwy: sąd siedziby Dostawcy.

---

*Alfa Solutions Sp. z o.o.* &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; *Delta Retail Sp. z o.o.*

Anna Kowalska — Prezes Zarządu &emsp;&emsp;&emsp; Monika Zając — Prezes Zarządu

---

> **Wskazówka dla testera:** Skill powinien wykryć m.in.:
> - §3: brak twardego SLA — „dołoży wszelkich starań" to nie jest mierzalny poziom usług; brak: dostępność %, RTO, RPO, kary za niedotrzymanie
> - §4 ust. 3: auto-renewal bez możliwości wypowiedzenia przed odnowieniem — §6 daje 30 dni, ale tylko „na koniec okresu abonamentowego"; jeśli klient nie wypowie do dnia X, jest związany kolejnym rokiem
> - §5 ust. 3: cap = 1 miesięczny abonament (2.400 zł netto) = prawdopodobnie za niski jak na zobowiązania RODO
> - §9 ust. 1: brak enumeracji środków bezpieczeństwa (art. 28 ust. 3 lit. c RODO wymaga konkretnych środków)
> - §9 ust. 2: podpodmioty przetwarzające — brak uprzedniej zgody Administratora (art. 28 ust. 2 RODO wymaga zgody szczegółowej lub ogólnej z prawem sprzeciwu); sama „informacja" to za mało
> - brak obowiązku powiadomienia o naruszeniu ochrony danych (art. 33 ust. 2 RODO — bezpośredni obowiązek procesora wobec administratora; art. 28 ust. 3 lit. f to obowiązek pomocy w spełnieniu art. 32–36, nie sam obowiązek powiadomienia)
> - brak klauzuli audytu (art. 28 ust. 3 lit. h RODO)
> - brak wskazania państw, do których dane mogą być transferowane
> - §2 ust. 1: licencja „na czas trwania Umowy" — brak: co z danymi przetworzonymi po zakończeniu (backup, retencja)
