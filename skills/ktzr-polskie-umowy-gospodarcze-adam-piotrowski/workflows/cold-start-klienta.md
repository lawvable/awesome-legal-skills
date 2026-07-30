# Workflow: Cold-start klienta (onboarding nowego klienta)


> _Reguły globalne: `references/rdzen-ktzr.md` (R1 cytowania · R2 bramka · R3 role · R4 profil · R5 format)._

**Cel:** szybki, ustrukturyzowany wywiad z nowym klientem (10-15 min), który pozwala wypracować *profil klienta* używany w dalszej pracy Claude'a nad jego sprawami. Profil pomaga kontekstualizować rekomendacje — bez niego Claude pracuje na *„generycznym B2B"*, co zwykle daje gorszy efekt niż praca na rzeczywistym profilu klienta.

**Inspiracja:** *„cold-start interview"* z Anthropic `claude-for-legal` (commercial-legal, employment-legal). Zaadaptowane do polskiego rynku B2B IT i SME.

**Triggery:** nowy klient kancelarii, *„onboarding"*, *„profil klienta"*, *„pierwsza rozmowa z klientem"*, *„skonfigurować Claude pod konkretnego klienta"*, *„zapisać preferencje klienta"*.

**Output:** plik `profile/klient-[nazwa-roboczej-nazwy].md` w prywatnej strukturze użytkownika (folder gitignored, nie commitowany do publicznego repo). Profil jest *living document* — aktualizowany w toku współpracy.

**Zastrzeżenie:** wywiad ma charakter informacyjny i operacyjny dla pracy kancelarii. Nie zastępuje porady prawnej co do konkretnych spraw klienta. Profil służy do kontekstualizacji rekomendacji, nie do automatycznego generowania decyzji prawnych.

## Struktura wywiadu (10-15 min)

Wywiad ma 6 sekcji, każda zajmuje 1-3 min. Pytania można zadawać w dowolnej kolejności — istotne jest, żeby na końcu mieć materiał do uzupełnienia każdej sekcji profilu.

### Sekcja 1: Profil biznesowy klienta (2-3 min)

Pytania:

1. *„Czym Państwo zajmują się komercyjnie?"* (sektor, model biznesowy)
2. *„Jaki jest etap rozwoju firmy?"* (startup pre-seed / seed / series A+ / mature / korporacja)
3. *„Jaka jest skala?"* (liczba osób, obrót roczny, liczba kontrahentów)
4. *„Czy działają Państwo lokalnie, regionalnie, krajowo, międzynarodowo?"*
5. *„Czy są ograniczenia regulacyjne wynikające z branży?"* (KSC/NIS2, RODO szczególne, MIFID, MAR, sektor zdrowia, sektor energetyczny, sektor edukacyjny)

**Co wynika dla pracy Claude'a:** sektor i etap rozwoju determinują domyślny tone-of-voice (formalny vs partnerski), poziom szczegółowości (startup chce krótko, korporacja chce dokumentację), oraz kontekst regulacyjny.

### Sekcja 2: Typowe sprawy i kontrahenci (2-3 min)

Pytania:

1. *„Z jakimi typami umów spotykają się Państwo najczęściej?"* (NDA, body leasing, wdrożenia, licencje, SaaS, dystrybucja, agencyjne, employment, B2B)
2. *„Kim są typowi kontrahenci?"* (sektor, skala — duzi enterprise, średni B2B, mali, konsumenci)
3. *„Czy są kontrahenci, z którymi Państwo regularnie pracują?"* (i ich charakterystyka — *„zwykle agresywni"*, *„zwykle reasonable"*, *„zawsze próbują dorzucić X"*)
4. *„Czy mają Państwo własny wzór umowy, którego używają, czy zwykle pracują na wzorze drugiej strony?"*

**Co wynika dla pracy Claude'a:** Claude może proaktywnie sugerować typy klauzul typowe dla branży klienta. Wiedza o tym, *kto jest po drugiej stronie stołu*, pomaga w doborze tonalności umowy (agresywna vs koncesyjna).

### Sekcja 3: Preferencje co do ryzyka (2-3 min)

Pytania:

1. *„Jak Państwo definiują tolerancję na ryzyko prawne?"* (konserwatywna / wyważona / agresywna)
2. *„Czy zdarzyły się Państwu spory sądowe lub arbitrażowe?"* (jakie, jaki rezultat)
3. *„Czy mają Państwo politykę co do typowych klauzul ryzyka?"* — cap odpowiedzialności, indemnifikacja, kary umowne, zakaz konkurencji
4. *„Czy są klauzule, których Państwo nigdy nie akceptują?"* (deal breakers)
5. *„Czy są klauzule, na które Państwo zawsze nalegają w swoich umowach?"* (must-have)

**Co wynika dla pracy Claude'a:** ryzykofilność klienta wpływa na rekomendacje. Klient *konserwatywny* dostaje surowsze klauzule ochronne; klient *agresywny* dostaje umowy z elementami presji negocjacyjnej.

### Sekcja 4: Eskalacja i decyzje (1-2 min)

Pytania:

1. *„Kto po Państwa stronie jest osobą decyzyjną co do umów?"* (CEO / CFO / Head of Legal / Founder)
2. *„Jaki jest próg, powyżej którego sprawa wymaga zaangażowania osoby decyzyjnej?"* (kwotowy, wpływ na działalność, czasowy)
3. *„Kogo loopować w sprawach dotyczących Państwa firmy?"* (oprócz głównej osoby kontaktowej — np. księgowa przy kwestiach podatkowych, IT manager przy wdrożeniach)
4. *„Z jakimi kancelariami / doradcami Państwo współpracują w innych obszarach?"* (jeśli relewantne — np. notariusz przy nieruchomościach, doradca podatkowy)

**Co wynika dla pracy Claude'a:** Claude może wskazywać, że dana sprawa wymaga eskalacji do decydenta lub konsultacji z innym doradcą; wie też, kogo cytować jako *„zgodnie z osobą X"*.

### Sekcja 5: Styl komunikacji i format (1-2 min)

Pytania:

1. *„Jakiego stylu komunikacji Państwo oczekują od kancelarii?"* (formalny, partnerski, partnerski z elementami formalnymi przy ważnych sprawach)
2. *„Czy preferują Państwo komunikację pisemną (email, DMS) czy ustną (telefon, video)?"* w sprawach roboczych
3. *„Jakiej formy oczekują Państwo dla dokumentów?"* — Word (.docx), PDF, oba; klasyczna grafika (Times New Roman) czy bardziej współczesna (Arial); preferencje co do typografii umów
4. *„Czy używają Państwo legal designu (tabele kluczowych warunków, spis treści, schematy)?"* — patrz `references/legal-design.md`
5. *„Czy oczekują Państwo wyjaśnień technicznych (klauzule z komentarzem), czy wolą czyste umowy bez metakomentarza?"*

**Co wynika dla pracy Claude'a:** Claude dostosowuje generowane dokumenty do preferencji typograficznych i stylu komunikacji klienta. Klient *„old-school"* dostaje Times 12, klient *„nowoczesny"* dostaje Arial 11,5 z legal design.

### Sekcja 6: Specyficzne klauzule i konteksty (1-2 min)

Pytania:

1. *„Czy mają Państwo własne wzory klauzul, których chcą używać?"* (np. własna klauzula poufności, własna klauzula RODO, własna klauzula odpowiedzialności)
2. *„Czy są obszary, w których macie Państwo wewnętrzną politykę nie do negocjacji?"* (np. *„nasza klauzula MFN zawsze obowiązuje"*)
3. *„Czy są obszary technologiczne / branżowe, których Claude powinien być świadomy?"* (np. *„zawsze pracujemy z open-source, więc klauzule IP muszą uwzględniać licencje copyleft"*)
4. *„Czy są obszary, w których Państwo nigdy się nie angażują?"* (np. *„nigdy nie podejmujemy umów z sektorem hazardowym / militarnym / kryptowalut"*)

**Co wynika dla pracy Claude'a:** *„hard rules"* klienta są niepodważalne — Claude nie powinien ich kwestionować, tylko stosować. *„Soft preferences"* mogą być negocjowane w konkretnych sprawach.

## Output: struktura profilu klienta

Po wywiadzie Claude generuje plik `profile/klient-[nazwa].md` (tylko prywatny — nie do publikacji) w następującej strukturze:

```markdown
# Profil klienta: [Nazwa]

**Status:** robocza wersja po cold-start z dnia [data]
**Aktualizacja:** [data ostatniej aktualizacji]

## Sekcja 1: Profil biznesowy
- Sektor: [...]
- Skala: [...]
- Etap rozwoju: [...]
- Zasięg: [...]
- Ograniczenia regulacyjne: [...]

## Sekcja 2: Typowe sprawy i kontrahenci
- Najczęstsze typy umów: [...]
- Typowi kontrahenci: [...]
- Stałe relacje (i charakterystyka): [...]
- Wzór własny vs cudzy: [...]

## Sekcja 3: Profil ryzyka
- Tolerancja: [konserwatywny / wyważony / agresywny]
- Historia sporów: [...]
- Polityki co do typowych klauzul:
  - Cap odpowiedzialności: [...]
  - Indemnifikacja: [...]
  - Kary umowne: [...]
  - Zakaz konkurencji: [...]
- Deal breakers: [...]
- Must-haves: [...]

## Sekcja 4: Eskalacja
- Osoba decyzyjna: [...]
- Próg eskalacji: [...]
- Stakeholders do informowania: [...]
- Inni doradcy: [...]

## Sekcja 5: Komunikacja i format
- Styl: [...]
- Forma komunikacji roboczej: [...]
- Format dokumentów: [...]
- Legal design: [tak / nie / tylko dla X]
- Komentarze w dokumentach: [tak / nie]

## Sekcja 6: Specyficzne klauzule i konteksty
- Wzory własne: [...]
- Hard rules: [...]
- Konteksty technologiczne / branżowe: [...]
- Branże wykluczone: [...]

## Historia spraw (uzupełniana w toku)
- [data] — [krótki opis sprawy] — [wynik / status]

## Notatki dodatkowe
[notatki ad-hoc po rozmowach]
```

## Reguła operacyjna: jak używać profilu

1. **Przed każdą nową sprawą** Claude czyta profil klienta — kontekstualizuje rekomendacje.
2. **Po każdej znaczącej sprawie** Claude lub prawnik prowadzący aktualizuje sekcję *„Historia spraw"* — z czasem profil staje się bogatszy.
3. **Co 6-12 miesięcy** profil powinien być przejrzany razem z klientem (krótki check-in, 15-20 min) — preferencje mogą się zmienić wraz z rozwojem firmy.

## Reguła operacyjna: kiedy uruchamiać cold-start

- ✅ Nowy klient kancelarii (pierwsze 1-2 sprawy)
- ✅ Klient istniejący, ale Claude nie był wcześniej używany w jego sprawach
- ✅ Istotna zmiana u klienta (nowy management, nowa runda finansowania, zmiana modelu biznesowego)
- ❌ Klient regularny, dla którego profil już istnieje i jest aktualny (poniżej 12 miesięcy od ostatniej aktualizacji)

## Powiązania w skill

- `references/zlote-reguly.md` — kontekst złotych reguł KTZR, niezmienny niezależnie od profilu klienta
- `references/style-redakcyjny.md` — styl KTZR, niezmienny; profil klienta dostosowuje *intensywność* (np. czy stosujemy legal design)
- `references/legal-design.md` — wybór trybu *„classic-clean"* vs *„light legal design"* zależy od profilu klienta (sekcja 5)
- `workflows/triage-szybki.md` — triage może uwzględniać profil klienta (sygnały RED dla klienta konserwatywnego mogą być YELLOW dla agresywnego)
- `workflows/pelna-analiza.md` — pełna analiza zawsze uwzględnia profil klienta

## Zastrzeżenie końcowe

Profil klienta jest *narzędziem roboczym kancelarii*, nie zobowiązaniem wobec klienta. Decyzje co do konkretnych spraw zawsze podejmowane są w kontekście aktualnej sytuacji, niezależnie od ogólnych preferencji wpisanych w profil. Profil ułatwia pracę, ale jej nie zastępuje.
