---
type: Klauzula
title: Odpowiedzialność i limity
tags: [odpowiedzialność, cap, szkody-pośrednie, SLA, uptime, maintenance, DSA, hosting, art-14-usdde]
contract_types: [B2B-IT, body-leasing, usługi-księgowe, maintenance, platforma, hosting]
risk_level: krytyczny
mandatory_for: [B2B-IT]
requires: [10-kary-umowne.md, 07-terminy-kamienie-milowe.md]
timestamp: 2026-06-27
---

# Odpowiedzialność i limity

## Kiedy stosować i na co uważać

Cap odpowiedzialności, wyłączenia, ubezpieczenie. Bez tego punktu odpowiedzialność jest nieograniczona — co przy projektach IT może oznaczać wielokrotność wartości umowy.

### ⚠️ Red flags

Brak limitu odpowiedzialności (= nieograniczona). Asymetryczny cap (tylko jedna strona chroniona). Brak wyłączenia szkód pośrednich. Wyłączenie rękojmi bez podstawy. Cap zbyt niski względem ryzyka projektu.

### Klauzula wzorcowa (generyczny IT)

> Całkowita odpowiedzialność Wykonawcy z tytułu Umowy jest ograniczona do kwoty równej wynagrodzeniu netto wypłaconemu Wykonawcy w okresie ostatnich 12 miesięcy. Ograniczenie nie dotyczy szkód wyrządzonych umyślnie, naruszenia poufności oraz naruszenia praw własności intelektualnej. Żadna ze Stron nie ponosi odpowiedzialności za szkody pośrednie, utracone korzyści ani utratę danych — chyba że szkoda wynikła z działania umyślnego Strony (art. 473 § 2 KC).

## Klauzule z umów KTZR

### Umowa o usługi księgowe

> Zleceniobiorca ponosi pełną odpowiedzialność odszkodowawczą za wszelkie szkody poniesione przez Zleceniodawcę, w tym zapłacone odsetki za zwłokę, nałożone kary, grzywny, sankcje oraz koszty postępowań. Odpowiedzialność nie jest w żaden sposób ograniczona.

> Zleceniobiorca oświadcza, że posiada ubezpieczenie OC z tytułu wykonywania usług księgowych na sumę gwarancyjną nie niższą niż [___] PLN. Zobowiązuje się do utrzymywania nieprzerwanego ubezpieczenia przez cały okres obowiązywania umowy.

### Umowa ramowa przewozu

> Zamawiający nie ponosi odpowiedzialności za ewentualną szkodę, którą może wyrządzić Pasażer Przewoźnikowi w zw. z realizacją umowy.

### Przydział kwaterunkowy

> Zleceniobiorca ponosi pełną odpowiedzialność za wszelkie szkody powstałe w lokalu z jego winy, winy osób, którym umożliwił przebywanie w lokalu. Zleceniodawca nie ponosi żadnej odpowiedzialności za rzeczy Zleceniobiorcy wniesione do lokalu.

### Umowa współpracy operacyjnej (B2B)

> Zleceniobiorca ponosi pełną odpowiedzialność względem Zleceniodawcy oraz osób trzecich za prawidłowe i terminowe wykonywanie obowiązków. Usługi Zleceniobiorca może wykonać przy pomocy osób trzecich — w takiej sytuacji ponosi odpowiedzialność za ich działania jak za własne.

### SLA — gwarantowana dostępność systemu i czasy reakcji (maintenance IT)

> Wykonawca gwarantuje dostępność Systemu (Uptime) na poziomie nie niższym niż [___]% w skali miesiąca kalendarzowego, mierzoną przez zewnętrzny system monitorujący, z interwałami nie dłuższymi niż 5 minut. Do czasu niedostępności nie wlicza się: (a) zaplanowanych okien serwisowych uzgodnionych z co najmniej 48-godzinnym wyprzedzeniem, łącznie nie więcej niż [___] godziny miesięcznie; (b) zdarzeń stanowiących siłę wyższą; (c) awarii infrastruktury niezwiązanych z działaniem ani zaniechaniem Wykonawcy — przy czym ciężar wykazania braku związku spoczywa na Wykonawcy.

> Wykonawca zobowiązuje się do obsługi zgłoszeń zgodnie z poniższą kategoryzacją:
> - **Wada Krytyczna** (całkowita niedostępność lub kluczowych modułów): czas reakcji do [___] h (24/7/365), czas naprawy do [___] h;
> - **Wada Istotna** (błąd ograniczający funkcjonalność, niepowodujący zatrzymania procesów): czas reakcji do [___] h (Dni Robocze), czas naprawy do [___] h (Dni Robocze);
> - **Wada Kosmetyczna** (drobny błąd nieistotny dla logiki biznesowej): czas reakcji do [___] h (Dni Robocze), czas naprawy do [___] Dni Roboczych.

> W przypadku niedotrzymania parametrów SLA Zamawiający ma prawo do proporcjonalnego obniżenia wynagrodzenia za dany miesiąc o wartość odpowiadającą procentowemu udziałowi czasu niedostępności przekraczającego dopuszczalny próg — niezależnie od kar umownych.

> Wykonawca ponosi odpowiedzialność za działania i zaniechania osób, którymi posługuje się przy realizacji Umowy (w tym podwykonawców i współpracowników), jak za działania i zaniechania własne.

### Platforma aukcyjna — wyłączenie odpowiedzialności pośrednika (art. 14 u.ś.u.d.e.)

> Administrator Portalu nie ponosi odpowiedzialności za zachowania Użytkowników w ramach Portalu ani za niewykonanie lub nienależyte wykonanie przez nich umów zawartych za pośrednictwem Portalu. Administrator nie ponosi w szczególności odpowiedzialności za: jakość, bezpieczeństwo lub legalność usług oferowanych w Aukcjach; zdolność Sprzedających do zawarcia i wykonania umowy; wypłacalność Kupujących; prawdziwość i rzetelność informacji podawanych przez Użytkowników. Portal nie jest stroną umów zawieranych między Użytkownikami i nie gwarantuje, że są oni uprawnieni do zawarcia i wykonania umowy.

⚠️ Podstawa: art. 6 DSA (Rozp. 2022/2065, hosting safe harbour) — bezpośrednio stosowany od 17.02.2024 r. DSA uchyla art. 14 u.ś.u.d.e. w zakresie przez siebie objętym (art. 89 DSA); art. 14 u.ś.u.d.e. zachowuje znaczenie pomocnicze wyłącznie poza zakresem przedmiotowym DSA. W powołaniach: wskazuj DSA jako lex posterior i lex specialis; art. 14 u.ś.u.d.e. — ewentualnie pomocniczo. Wyłączenie skuteczne pod warunkiem, że Administrator: (a) nie ma rzeczywistej wiedzy o bezprawności działań Użytkownika; (b) po uzyskaniu takiej wiedzy niezwłocznie usuwa lub blokuje dostęp do treści (termin ustawowy — nie dookreślać w klauzuli; praktyka: do 24–48 h od potwierdzenia zgłoszenia). Nie obejmuje sytuacji, gdy Portal sam aktywnie uczestniczy w transakcji lub sprawuje redakcyjną kontrolę nad treścią Aukcji.
