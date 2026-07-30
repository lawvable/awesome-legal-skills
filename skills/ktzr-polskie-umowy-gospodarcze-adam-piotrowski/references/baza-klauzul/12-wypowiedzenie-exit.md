---
type: Klauzula
title: Wypowiedzenie i exit plan
tags: [wypowiedzenie, exit-plan, vendor-lock-in, kod-źródłowy, przekazanie-danych, wsparcie-przejściowe, commit-history]
contract_types: [B2B-IT, body-leasing, usługi-księgowe, maintenance, platforma]
risk_level: wysoki
mandatory_for: [maintenance]
requires: [04-przedmiot-umowy.md, 09-poufnosc.md]
timestamp: 2026-06-27
---

# Wypowiedzenie i exit plan

## Kiedy stosować i na co uważać

Warunki zakończenia współpracy i obowiązki przy wyjściu. W IT krytyczny jest exit plan — przekazanie kodu, dokumentacji, danych, haseł, migracja — bez tego zamawiający zostaje z „vendor lock-in”.

### ⚠️ Red flags

Brak możliwości wypowiedzenia (umowa na czas nieokreślony bez klauzuli exit). Asymetryczne okresy wypowiedzenia. Brak exit planu — vendor lock-in. Brak obowiązku przekazania kodu źródłowego. Brak przesłanek rozwiązania natychmiastowego.

### Klauzula wzorcowa (generyczny IT)

> Każda ze Stron może wypowiedzieć Umowę z zachowaniem [___]-dniowego okresu wypowiedzenia. Rozwiązanie natychmiastowe przysługuje w przypadku: (a) istotnego naruszenia Umowy nieusuniętego w terminie [___] dni od wezwania; (b) złożenia wniosku o upadłość; (c) zaprzestania działalności. W terminie [___] dni od zakończenia Umowy Wykonawca przekaże Zamawiającemu: całość kodu źródłowego, dokumentację techniczną, dane dostępowe, kopie danych oraz udzieli wsparcia migracyjnego w wymiarze do [___] godzin.

## Klauzule z umów KTZR

### Body Leasing IT (KTZR)

> Każda ze Stron może wypowiedzieć Umowę z zachowaniem [___]-dniowego okresu wypowiedzenia. Rozwiązanie natychmiastowe w przypadku: istotnego naruszenia nieusuniętego w [___] dni od wezwania, złożenia wniosku o upadłość, zaprzestania działalności.

> W terminie [___] dni od zakończenia Umowy Usługodawca przekaże całość kodu źródłowego, dokumentację techniczną, dane dostępowe i kopie danych.

### Umowa ramowa przewozu

> Umowa zostaje zawarta na czas nieokreślony, z możliwością jej wypowiedzenia przez każdą ze Stron z zachowaniem jednomiesięcznego okresu wypowiedzenia, ze skutkiem na koniec miesiąca kalendarzowego.

### Umowa o usługi księgowe

> Po rozwiązaniu umowy Zleceniobiorca zobowiązany jest do wydania Zleceniodawcy wszystkich oryginałów dokumentów, ksiąg, ewidencji zarówno w formie papierowej, jak i w formie edytowalnych plików elektronicznych, w terminie 14 dni. Zleceniobiorcy nie przysługuje prawo zatrzymania dokumentacji z żadnego tytułu.

### Porozumienie o rozwiązaniu umowy zlecenia

> Strony zgodnie oświadczają, że łącząca je umowa zlecenia zostaje rozwiązana za porozumieniem stron ze skutkiem na dzień [___]. Zleceniobiorca oświadcza, że wyraża zgodę działając dobrowolnie i świadomie, z pełną świadomością konsekwencji rozwiązania umowy.

⚠️ Zdanie drugie („działając dobrowolnie i świadomie...") jest klauzulą pustą (W7) — nie zamyka zarzutów z art. 82–86 KC (wady oświadczenia woli). W nowych porozumieniach pomijaj.

### Udostępnienie lokalu — cofnięcie ze skutkiem natychmiastowym

> [Udostępniający] jest uprawniony do cofnięcia udostępnienia w każdym czasie, ze skutkiem natychmiastowym, bez podania przyczyny. [Korzystający] zobowiązany jest do opróżnienia i wydania lokalu w terminie [___] dni od doręczenia oświadczenia o cofnięciu.

### Udostępnienie lokalu — wygaśnięcie z mocy prawa (dwie przyczyny)

> Udostępnienie wygasa automatycznie z dniem rozwiązania lub wygaśnięcia Umowy głównej — bez konieczności składania odrębnego oświadczenia. [Korzystający] zobowiązany jest do opróżnienia i wydania lokalu najpóźniej w ostatnim dniu obowiązywania Umowy głównej.

> Udostępnienie wygasa automatycznie w przypadku nieobecności [Korzystającego] w lokalu trwającej nieprzerwanie dłużej niż [___] dni — bez konieczności składania odrębnych oświadczeń przez żadną ze Stron.

### Platforma aukcyjna — zawieszenie i usunięcie konta

> Administrator Portalu jest uprawniony do zawieszenia konta Użytkownika w przypadku: braku płatności abonamentu w terminie lub naruszenia postanowień Regulaminu bądź przepisów prawa.

> Administrator Portalu jest uprawniony do usunięcia konta Użytkownika w przypadku: (a) odmowy zawarcia umowy ze zwycięzcą Aukcji lub niewykonania umowy zawartej w ramach Aukcji; (b) naruszenia Regulaminu lub przepisów prawa.

> W przypadku gdy Użytkownik nie zaakceptuje zmienionego Regulaminu i złoży oświadczenie o braku akceptacji — umowa wygasa, Aukcje Użytkownika zostają automatycznie zakończone po [___] dniach od złożenia oświadczenia, a konto usunięte po [___] dniach od tego dnia.

### Kompleksowy exit plan (maintenance IT / SaaS)

> Po złożeniu oświadczenia o wypowiedzeniu lub rozwiązaniu Umowy Wykonawca jest zobowiązany do:
> 1. przekazania Zamawiającemu — w terminie 3 Dni Roboczych — pełnego dostępu do infrastruktury, w tym wszystkich danych dostępowych, certyfikatów, kluczy szyfrujących, tokenów API i haseł, z pisemnym potwierdzeniem kompletności;
> 2. przekazania — w tym samym terminie — pełnego kodu źródłowego w aktualnym stanie wraz z historią zatwierdzeń (commit history), do repozytorium wskazanego przez Zamawiającego;
> 3. przekazania kompletnej dokumentacji technicznej niezbędnej do dalszego utrzymania przez osobę trzecią — w terminie [___] Dni Roboczych.

> W okresie [___] dni od daty zakończenia Umowy Wykonawca świadczy wsparcie przejściowe na rzecz Zamawiającego lub wskazanego przez niego podmiotu, obejmujące udzielanie odpowiedzi na pytania techniczne, udział w spotkaniach roboczych i pomoc przy wdrożeniu u nowego dostawcy. Wynagrodzenie za wsparcie przejściowe jest objęte ostatnią fakturą za utrzymanie i nie stanowi podstawy do odrębnych roszczeń Wykonawcy.

> Po upływie okresu wsparcia przejściowego Wykonawca trwale i nieodwracalnie usuwa wszelkie dane, kody źródłowe i dokumentację Zamawiającego ze wszystkich urządzeń, nośników i systemów Wykonawcy oraz podmiotów powiązanych — z zastosowaniem metod uniemożliwiających odtworzenie. W terminie [___] Dni Roboczych od trwałego usunięcia danych Wykonawca przekazuje Zamawiającemu pisemne oświadczenie potwierdzające wykonanie tego obowiązku, ze wskazaniem metody usunięcia.

> Zamawiający jest uprawniony do przeprowadzenia niezależnego audytu systemów Wykonawcy w celu weryfikacji wykonania obowiązku trwałego usunięcia danych, na co Wykonawca wyraża bezwarunkową zgodę.
