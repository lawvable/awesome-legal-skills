# Materiały testowe

Fikcyjne dokumenty do testowania skilla bez angażowania danych klientów.

## Testowe akta (`testowe-akta/`)

| Plik | Typ umowy | Kluczowe ryzyka do wykrycia |
|------|-----------|----------------------------|
| `01-nda-b2b.md` | NDA wzajemne | Brak kary umownej, „niezwłocznie", wąska definicja inf. poufnych, brak poufności po zakończeniu |
| `02-body-leasing-it.md` | Body leasing IT | Ryzyko stosunku pracy, brak pól eksploatacji (PrAut), wyłączenie lucrum cessans bez zastrzeżenia winy umyślnej (art. 473 §2 KC), brak non-solicitation |
| `03-saas-z-dpa.md` | SaaS + DPA/RODO | Brak twardego SLA, auto-renewal bez okna wypowiedzenia, niekompletna UPD (brak audytu, naruszenia, podpodmiotów wg art. 28 ust. 3 RODO) |

## Jak używać

1. Wklej zawartość pliku (bez bloku ostrzeżenia) do sesji z Claude ze skillem.
2. Poproś o: triage, pełną analizę, audyt ryzyk lub konkretny workflow.
3. Porównaj wynik z listą ryzyk w stopce pliku — to twój benchmark.

Dokumenty celowo zawierają luki typowe dla umów „z internetu" lub pierwszych szkiców bez nadzoru prawnego. Skill powinien je wychwycić.

## Zasady

- Wszystkie dane (nazwy, KRS, NIP, osoby) są **zmyślone** — nie używaj ich w prawdziwych dokumentach.
- Numery KRS zaczynają się od `0000999` — poza zakresem prawdziwych wpisów.
- Plik możesz edytować aby testować skill na konkretnych konfiguracjach klauzul.
