# Format Checklist KTZR

10 punktów do sprawdzenia przed wygenerowaniem lub zwróceniem każdego dokumentu.
Szybki filtr — czytelnia dla `legal-design.md` i `style-redakcyjny.md`.

---

## Checklist

| # | Reguła | Test |
|---|--------|------|
| 1 | **Cudzysłowy** | Wyłącznie „polskie" — nie "angielskie" ani «żadne inne» |
| 2 | **Pauza** | Długa pauza —  (U+2014) przy wtrąceniach i wyliczeniach, nie półpauza - ani myślnik - |
| 3 | **Kwoty i kary** | Cyframi i słownie: `18.000,00 zł (słownie: osiemnaście tysięcy złotych)` |
| 4 | **Numeracja** | §/ust./pkt spójne przez cały dokument; listy klauzul: a) b) c); listy punktów: 1) 2) 3) |
| 5 | **Definicje** | Każde pojęcie pisane Wielką Literą ma definicję w § Definicje lub przy pierwszym wystąpieniu |
| 6 | **Odesłania wewnętrzne** | Każde „§ X ust. Y" prowadzi do istniejącego przepisu — sprawdź po skończeniu numeracji |
| 7 | **Brak łaciny w klauzulach** | `lucrum cessans`, `dolus`, `ex contractu` — tylko w analizie, nigdy w treści klauzul |
| 8 | **Terminy** | Daty: `dd.mm.rrrr`; okresy: `7 dni` / `7 Dni Roboczych` — nie „tydzień", „niezwłocznie" |
| 9 | **Spójność stron** | Jedna nazwa przez cały dokument: „Wykonawca" wszędzie, nie raz „Zleceniobiorca" |
| 10 | **Cytaty przepisów** | Każdy art. N ustawy X → najpierw `verify_article()` (jeśli MCP aktywny) lub `[NIEZWERYFIKOWANE]` |

---

## Kiedy uruchamiać

- Przed każdym outputem z `generator-umow.md` (KROK 5 QA)
- Przed każdym outputem z `generator-regulaminu.md`
- Po `popraw-fragment.md` — przed zwróceniem poprawionego fragmentu
- Opcjonalnie: po `audyt-ryzyk.md` — sprawdź cytowane przepisy (punkt 10)

## Czerwone flagi — natychmiast popraw przed outputem

```
❌ "niezwłocznie"                     → zastąp: "w terminie 3 dni roboczych" (lub inny)
❌ cudzysłów "..."                    → zastąp: „..."
❌ półpauza - lub myślnik -            → zastąp: —
❌ Wielka Litera bez definicji         → dodaj definicję lub zmień na małą
❌ § 5 ust. 3 (nieistniejący)         → popraw odesłanie
❌ art. X ustawy Y bez verify_article → dodaj [NIEZWERYFIKOWANE] lub wywołaj MCP
```
