# Workflow: Popraw fragment


> _Reguły globalne: `references/rdzen-ktzr.md` (R1 cytowania · R2 bramka · R3 role · R4 profil · R5 format)._

Workflow do edycji **konkretnego fragmentu umowy** — gdy użytkownik wkleja klauzulę i prosi o poprawienie, lub gdy przerywa szerszy workflow analizy, żeby naprawić jeden paragraf.

Używaj, gdy:
- Użytkownik wkleja fragment + prosi o korektę
- Użytkownik pisze "popraw § X w tej umowie"
- W trakcie pełnej analizy/audytu użytkownik zatrzymuje workflow, żeby naprawić jedno miejsce

---

## Krok 1: Zrozum, co poprawiamy

**Otwórz teraz:** `references/style-redakcyjny.md` — zawsze przed edycją klauzuli. Reguły stylu KTZR są wymagane także przy drobnych poprawkach.

Wyjaśnij sobie:
- **Co konkretnie ma być poprawione?** Cały paragraf, jeden ustęp, jedno zdanie?
- **Dlaczego?** Ujednolicić styl, dodać brakujący element, naprawić błąd prawny, dostosować do innych klauzul, doprecyzować
- **W jakim kontekście?** Czy fragment funkcjonuje samodzielnie czy odsyła do innych części umowy?

Jeśli instrukcja użytkownika jest niejasna ("popraw to") — **dopytaj raz**: "Co konkretnie chcesz zmienić? Np. dodać limit kar, ujednolicić z § 4, doprecyzować termin?"

---

## Krok 2: Wybór klauzuli z bazy lub przeróbka

### Scenariusz A: Dodanie/zastąpienie klauzulą z bazy

Jeśli użytkownik chce dodać element, którego brakuje (np. "dodaj klauzulę anty-copyleft", "dorzuć limit odpowiedzialności"):

1. Otwórz `references/baza-klauzul/INDEX.md`
2. Znajdź odpowiednią kategorię i otwórz plik
3. Wybierz najlepszą klauzulę dla kontekstu (zwykle z umowy KTZR najbliższej typowi)
4. Dopasuj do kontekstu fragmentu — nazwy stron, terminy, odesłania

### Scenariusz B: Przeróbka istniejącego fragmentu

Jeśli użytkownik chce naprawić istniejący tekst (np. "ujednolicaj z resztą umowy", "uprość język"):

1. Przeczytaj fragment i zrozum jego cel prawny
2. Sprawdź `references/zlote-reguly.md` — czy fragment narusza którąś regułę
3. Zastosuj reguły stylistyczne KTZR
4. Zachowaj sens prawny — zmieniasz formę, nie treść (chyba że treść jest błędna)

### Scenariusz C: Pełna wymiana

Jeśli fragment jest "do śmieci" (np. nieważna klauzula próbująca wyłączyć winę umyślną — art. 473 § 2 KC):

> _(R1): `verify_article()` przed każdym cytowanym artykułem — lub `[NIEZWERYFIKOWANE]` przy braku MCP._

1. Wyjaśnij krótko, dlaczego fragment jest problematyczny
2. Zaproponuj zastępczą klauzulę z bazy
3. Pokaż "przed i po"

---

## Krok 3: Format wyjścia

**Zwięzły, zorientowany na działanie.** Nie pisz długich wyjaśnień, chyba że użytkownik prosi.

### Wariant domyślny (wystarczy poprawiony tekst)

> ⛔ Jeśli poprawiony fragment jest gotowy do wklejenia w podpisywaną umowę — najpierw zapytaj: „Czy prawnik prowadzący sprawę widział tę zmianę?" Bez potwierdzenia: dodaj `[DRAFT — DO WERYFIKACJI]` nad fragmentem.

```
[gotowy poprawiony fragment, do wklejenia w dokument]
```

Po tym **jedno-dwie linijki** uzasadnienia, co zmieniłeś i dlaczego (jeśli zmiana wymaga wyjaśnienia).

### Wariant rozbudowany (gdy zmiana jest istotna)

```
## ZMIANA

**Przed:**
[fragment oryginalny]

**Po:**
[fragment poprawiony]

**Co zmieniłem:**
- [1-3 punkty, każdy 1 zdanie]

**Klauzula z bazy:** `references/baza-klauzul/XX-yyy.md`
```

---

## Zasady poprawiania

1. **Zachowuj sens prawny** — chyba że jego zmiana jest świadomym celem
2. **Stosuj Złote Reguły KTZR** (zwłaszcza: spójność terminologii, definicje, brak powtórzeń)
3. **Dopasuj do kontekstu** — jeśli umowa używa "Wykonawca", w poprawionym fragmencie też "Wykonawca", nie "Zleceniobiorca"
4. **Nie wymyślaj klauzul od zera** — bierz z bazy KTZR
5. **Brak komentarzy w tekście** — gotowa klauzula ma być wklejalna w dokument bez sprzątania po Tobie. Komentarze osobno.

---

## Anty-pattern — czego NIE robić

- ❌ Nie zmieniaj fragmentu, którego użytkownik nie prosił o zmianę (np. ktoś prosi o poprawkę § 5, a ty przy okazji "ulepszasz" § 6)
- ❌ Nie dodawaj treści prawnej, której użytkownik nie zlecił (np. ktoś prosi o ujednolicenie stylu, a ty dorzucasz kary umowne "bo brakuje")
- ❌ Nie pisz długiego wprowadzenia ("Zrozumiałem polecenie, oto poprawiony fragment z uwzględnieniem...") — przejdź od razu do efektu
- ❌ Nie zostawiaj placeholderów [tutaj wstaw kwotę] — jeśli czegoś nie wiesz, **zapytaj** zamiast wstawiać placeholdery
