# Workflow: Triage szybki (GREEN / YELLOW / RED)


> _Reguły globalne: `references/rdzen-ktzr.md` (R1 cytowania · R2 bramka · R3 role · R4 profil · R5 format)._

**Cel:** szybka kategoryzacja umowy / NDA / aneksu w ciągu 5-10 minut, pomagająca w decyzji *„podpisać", „przekazać do analizy", „odrzucić bez negocjacji"*. Komplementarny do `pelna-analiza.md` (która jest głębsza i czasochłonna).

**Inspiracja:** Anthropic Contract Review skill (`anthropics/claude-for-legal`), zaadaptowany do polskiego B2B IT.

**Triggery:** *„czy mogę to podpisać"*, *„szybki rzut oka"*, *„triage"*, *„jak złe to jest"*, *„daj się to zobaczyć w 5 minut"*, *„NDA do podpisania"*, *„prosta umowa, ocenisz?"*.

**Zastrzeżenie:** triage jest **pierwszym filtrem**, nie pełną analizą. Każda umowa z kategorii YELLOW lub RED powinna być przekazana do pełnej analizy (`pelna-analiza.md`) przed podpisaniem. GREEN oznacza brak czerwonych flag w typowych obszarach — *nie* oznacza, że umowa jest *idealna*.

## Trzy kategorie

### 🟢 GREEN — standardowa, podpisalna bez modyfikacji

Umowa odpowiada wzorcom KTZR lub typowemu rynkowi B2B IT. Brak czerwonych flag w typowych obszarach. Można podpisać po przekazaniu klientowi krótkiej notatki *„OK, można podpisać"*.

**Kryteria (wszystkie muszą być spełnione):**

- Strony jednoznacznie zidentyfikowane (KRS / NIP / reprezentacja)
- Przedmiot umowy konkretny, mieszczący się w zakresie działalności klienta
- Cap odpowiedzialności obecny i mieszczący się w typowym przedziale (zwykle 12-mies. wynagrodzenie × 1-3x)
- Wina umyślna i rażące niedbalstwo nie są wyłączone (zgodne z art. 473 § 2 KC)
- Terminy płatności w standardzie (30, 45 dni od FV)
- Forma rozwiązywania sporów obecna (sąd polski lub arbitraż uzgodniony)
- Klauzule poufności proporcjonalne (czas trwania, zakres)
- W razie umowy IT — pola eksploatacji wymienione i adekwatne do przedmiotu (art. 41 ust. 2 PrAut)

### 🟡 YELLOW — wymaga analizy przed podpisaniem

Umowa zawiera klauzule odbiegające od typowych wzorców KTZR lub rynkowych. Nie jest oczywiście „zła", ale wymaga świadomej decyzji klienta i potencjalnie negocjacji.

**Sygnały do YELLOW (jakikolwiek z poniższych):**

- Cap odpowiedzialności **niestandardowy** (np. tylko 50% wynagrodzenia rocznego — niski; albo 5x roczne — wysoki, ale akceptowalny w przemyśle)
- **Wyłączenia odpowiedzialności szeroko określone** (*„za szkody pośrednie, lucrum cessans"*) — wymaga sprawdzenia kontekstu (zwykle akceptowalne przy umowach komercyjnych)
- Klauzula **zakazu konkurencji** lub **non-solicitation** — wymaga sprawdzenia ekwiwalentu, czasu trwania, zakresu (w PL trudno egzekwowalne bez ekwiwalentu, art. 101¹ KP analogiczne dla B2B sporne)
- **Przeniesienie praw autorskich** *„do wszystkich utworów powstałych w toku współpracy"* bez sprecyzowania pól eksploatacji — bez konkretu klauzula nieskuteczna (art. 41 ust. 2 PrAut), ale klient może o tym nie wiedzieć
- **Forma rozwiązywania sporów obca** (np. sąd zagraniczny, arbitraż w obcej jurysdykcji) — wymaga konsensusu klienta
- **Klauzula audytu** lub *„prawo do inspekcji"* po stronie drugiej strony — wymaga sprawdzenia zakresu
- **RODO**: brak umowy powierzenia, mimo że umowa zakłada przetwarzanie danych osobowych (art. 28 RODO) — sygnał do uzupełnienia
- Wynagrodzenie **uzależnione od czynników zewnętrznych** (KPI, wynik finansowy klienta, success fee) — wymaga zdefiniowania metryk
- Klauzule **zmiany umowy** (np. *„Zamawiający może jednostronnie zmienić zakres Usług"*) — typowa nierównowaga, warto negocjować

### 🔴 RED — nie podpisywać bez głębokiej negocjacji

Umowa zawiera klauzule blokujące lub stwarzające istotne ryzyko. Bez negocjacji nie powinna być podpisana.

**Sygnały do RED (jakikolwiek z poniższych):**

- **Brak cap odpowiedzialności** lub cap rażąco niski (np. *„do kwoty 1 PLN"*) — strona bez ochrony przed konsekwencjami
- **Wyłączenie odpowiedzialności za winę umyślną** — nieważne z mocy art. 473 § 2 KC, ale wskazuje, że druga strona pisała umowę agresywnie
- **Indemnifikacja jednostronna** (*„Wykonawca zwolni Zamawiającego z wszelkich roszczeń osób trzecich"*) bez wzajemności, bez ograniczeń kwotowych i czasowych
- **Cesja umowy** bez zgody jednej ze stron (zwykle bez zgody Wykonawcy — niekorzystne dla naszego klienta)
- **Klauzula MFN (most-favoured nation)** lub **klauzula najtańszej oferty** — zobowiązują do udzielania drugiej stronie najlepszych warunków na rynku; często niemożliwa do egzekwowania w praktyce
- **Zakaz konkurencji** bez ekwiwalentu i z szerokim zakresem czasowo-przestrzennym (np. *„5 lat, na terenie EU, w branży IT"*)
- **Pełne przeniesienie praw autorskich** *„do wszystkich utworów, które kiedykolwiek powstaną"* w umowie typu open-ended — wymaga konkretyzacji
- **Brak klauzuli wypowiedzenia** lub wypowiedzenie tylko po jednej stronie
- **Forma rozwiązywania sporów wyłączająca prawo polskie** w sytuacji, gdy nie ma uzasadnienia gospodarczego
- **RODO**: druga strona żąda dostępu do danych osobowych pracowników naszego klienta bez podstawy prawnej
- **Kary umowne** rażąco wysokie w stosunku do wartości umowy (np. *„kara umowna 500% wynagrodzenia za każde naruszenie"* — możliwa do miarkowania z art. 484 § 2 KC, ale wskazuje na agresywność)
- **Klauzula automatycznego przedłużenia** umowy bez wyraźnej zgody (*„umowa przedłuża się o kolejny rok, chyba że strona złoży wypowiedzenie 6 miesięcy przed terminem"*)

## Procedura triage

### Krok 1: Sprawdzenie kompletności (1-2 min)

- Czy umowa zawiera datę, miejsce, strony, sposób reprezentacji?
- Czy zawiera wszystkie *essentialia negotii* (typ stosunku, przedmiot, wynagrodzenie, czas)?
- Czy załączniki są w zestawie?

Brak któregoś z elementów = **automatycznie YELLOW** (uzupełnij, potem powtórz triage).

### Krok 2: Skan obszarów ryzyka (3-5 min)

Przejdź kolejno przez listy kryteriów dla GREEN / YELLOW / RED. Pierwsza znaleziona flaga RED → kategoria RED. Brak RED, jakikolwiek YELLOW → kategoria YELLOW. Brak ani RED ani YELLOW → kategoria GREEN.

**Obszary do skanu (kolejność):**

1. Odpowiedzialność (cap, wyłączenia, wina umyślna)
2. Prawa autorskie (przeniesienie, pola eksploatacji)
3. Poufność i NDA (czas trwania, zakres)
4. Wypowiedzenie i exit
5. Kary umowne
6. RODO (umowa powierzenia, transfery do państw trzecich)
7. Cesja umowy
8. Forma rozwiązywania sporów
9. Klauzule zmian umowy (asymetria)
10. Wynagrodzenie i terminy płatności

### Krok 3: Notatka triage (1-2 min)

**Format wynikowy:**

```
TRIAGE: 🟢/🟡/🔴

Kategoria: [GREEN / YELLOW / RED]

Klauzule znaczące:
- § X — [krótki opis sygnału]
- § Y — [krótki opis sygnału]
- ...

Rekomendacja:
[GREEN] Można podpisać. Notatka opcjonalna: [krótka uwaga].
[YELLOW] Wymaga analizy przed podpisaniem. Punkty do omówienia: [lista].
[RED] Nie podpisywać bez negocjacji. Punkty blokujące: [lista].
```

### Krok 4 (tylko dla YELLOW i RED): przekazanie do pełnej analizy

YELLOW i RED zostawiają sprawę otwartą. Następny krok = workflow `pelna-analiza.md` lub `audyt-ryzyk.md`. Triage nie zastępuje pełnej analizy — jest pierwszym filtrem.

## Reguła operacyjna: kiedy używać triage

- ✅ NDA standardowe (mutual lub one-way) od typowych kontrahentów
- ✅ Aneksy techniczne (rozliczenia, zmiany SLA, dodanie modułu)
- ✅ Proste umowy o usługi do 50 tys. zł rocznie
- ✅ Pierwszy filtr przy dużej liczbie umów wpływających do oceny
- ✅ Decyzja klienta *„czy w ogóle to czytać dalej, czy odrzucić"*

**Kiedy NIE używać triage (od razu pełna analiza):**

- Umowy o wartości > 250 tys. zł rocznie
- Umowy z elementem fuzji / przejęcia / inwestycji
- Umowy o pracę i jej analogi B2B z elementami kontroli (ryzyko reklasyfikacji)
- Umowy zawierające elementy wpływające na strukturę kapitałową klienta
- Wszystkie przypadki, w których klient sygnalizuje *„to jest dla nas ważne, sprawdź dokładnie"*

## Powiązania w skill

- `workflows/pelna-analiza.md` — następny krok dla YELLOW i RED
- `workflows/audyt-ryzyk.md` — głębsza analiza ryzyk dla YELLOW
- `references/zlote-reguly.md` — Złote Reguły jako filtr dla GREEN/YELLOW/RED
- `references/baza-klauzul/INDEX.md` — referencja do typowych klauzul KTZR (do porównania)

## Zastrzeżenie końcowe

Triage jest narzędziem operacyjnym dla pracy prawniczej, nie produktem rynkowym ani usługą doradczą. Wynik triage nie zastępuje pełnej analizy prawnej. W każdej sprawie ostateczna decyzja co do podpisania umowy należy do klienta i powinna być podjęta po konsultacji z prawnikiem prowadzącym.
