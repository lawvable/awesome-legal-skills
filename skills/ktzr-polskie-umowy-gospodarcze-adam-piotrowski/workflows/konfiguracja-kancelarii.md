# Workflow: Konfiguracja kancelarii

Jednorazowy wywiad, który generuje plik `practice-profile.md` — trwałą konfigurację kancelarii czytaną przez wszystkie workflow. Uruchamia administrator (partner/właściciel kancelarii lub asystent przez niego upoważniony).

**Kiedy uruchamiać:**
- Przy pierwszym wdrożeniu skilla w kancelarii
- Po zmianie profilu praktyki, specjalizacji lub standardów
- Gdy kilka osób w organizacji korzysta ze skilla i potrzebna jest spójna konfiguracja

**Czas:** 15–20 minut. Odpowiadaj konkretnie — im precyzyjniej, tym lepiej skill dopasuje się do Twojej kancelarii.

**Output:** gotowy plik `practice-profile.md` do skopiowania do katalogu głównego skilla. Plik jest gitignorowany — nie trafi do repozytorium publicznego.

---

## Zasady przeprowadzania wywiadu

- Zadawaj sekcjami — po każdej czekaj na odpowiedzi, potem idź dalej
- Nie pytaj o dane klientów, sygnatur spraw ani żadnych danych osobowych
- Jeśli administrator odpowiada „standardowo" lub „typowo" — zastosuj domyślne wartości rynkowe dla polskiej kancelarii B2B IT
- Używaj odpowiedzi do skonstruowania `practice-profile.md` — nie przechowuj ich w pamięci sesji

---

## SEKCJA 1/5 — Profil praktyki

**Pytania:**

1. **Główne typy umów:** jakie rodzaje umów stanowią >80% pracy kancelarii? (np. body leasing IT, NDA, SaaS, wdrożenia ERP, przeniesienie praw autorskich, ugody, umowy o pracę B2B)

2. **Reprezentacja:** kogo kancelaria reprezentuje najczęściej?
   - Zamawiającego / Klienta (nabywca usług)
   - Wykonawcę / Dostawcę (świadczący usługi)
   - Obustronnie (zależy od sprawy)

3. **Rynek:** profil klientów kancelarii:
   - B2B / B2C / mieszany
   - Krajowy / międzynarodowy (jeśli INT — jakie jurysdykcje?)
   - Wielkość klientów: MŚP / korporacje / startup / mieszane

4. **Branże specjalizacji:** poza IT — jakieś dodatkowe branże? (np. fintech, medtech, e-commerce, nieruchomości)

**STOP — poczekaj na odpowiedzi do Sekcji 1.**

---

## SEKCJA 2/5 — Progi ryzyka

**Pytania:**

1. **Styl kancelarii:** jak opisałbyś podejście kancelarii do ryzyka?
   - **Konserwatywny** — zawsze wychodzi z maksymalnych zabezpieczeń, negocjuje każde odchylenie od standardu
   - **Umiarkowany** — standardowy rynek B2B; negocjuje ryzyka powyżej progu
   - **Agresywny** — orientacja na zamknięcie transakcji; akceptuje wyższe ryzyka gdy klient świadomie decyduje

2. **RED bezwzględne:** co zawsze blokuje umowę bez negocjacji? Przykłady (zaznacz i uzupełnij):
   - [ ] Brak cap odpowiedzialności lub cap < X miesięcy wynagrodzenia
   - [ ] Próba wyłączenia winy umyślnej (art. 473 §2 KC)
   - [ ] Brak pól eksploatacji przy przeniesieniu praw autorskich
   - [ ] Jurysdykcja zagraniczna bez uzasadnienia
   - [ ] Inne: ___

3. **Próg pełnej analizy vs triage:** od jakiej wartości umowy zawsze robisz pełną analizę (nie triage)?

**STOP — poczekaj na odpowiedzi do Sekcji 2.**

---

## SEKCJA 3/5 — Domyślne pozycje negocjacyjne

**Pytania:**

1. **Cap odpowiedzialności:** jaki cap rekomenduje kancelaria jako punkt wyjścia negocjacji?
   - Np. „12 miesięcy wynagrodzenia netto" / „wartość kontraktu" / „zależy od wartości umowy"

2. **Poufność:** standardowy okres poufności po zakończeniu umowy w kancelarii?
   - Np. „3 lata dla informacji zwykłych, bezterminowo dla tajemnicy przedsiębiorstwa"

3. **RODO:** domyślna pozycja kancelarii:
   - Reprezentujemy administratora (strona zlecająca przetwarzanie)
   - Reprezentujemy podmiot przetwarzający (strona przyjmująca dane)
   - Obustronnie

4. **Rozstrzyganie sporów:** preferowane forum?
   - Sąd powszechny (siedziba której strony?)
   - Arbitraż (jaki sąd arbitrażowy?)
   - Zależy od wartości i stron

5. **Kary umowne:** czy kancelaria standardowo proponuje kary umowne w każdej umowie, czy tylko gdy klient prosi?

**STOP — poczekaj na odpowiedzi do Sekcji 3.**

---

## SEKCJA 4/5 — Styl i format

**Pytania:**

1. **Legal design:** jaki format wyjścia preferujesz?
   - **Classic** — tradycyjny format prawniczy, bez tabel i boxów (Times New Roman)
   - **Light legal design** — Arial, tabele kluczowych warunków, subtelne wyróżnienia (standard KTZR)

2. **Poziom formalności odpowiedzi skilla:** jak skill ma się do Ciebie zwracać?
   - Formal — „Kancelaria" / „Zamawiający" / bez bezpośrednich zwrotów
   - Semi-formal — „Państwa kancelaria" / „Państwo"
   - Operacyjny — bezpośrednio, jak kolega-prawnik

3. **Język roboczy:**
   - Wyłącznie PL
   - PL z angielskim termsheet / summaries dla klientów zagranicznych
   - EN i PL równorzędnie

4. **Format raportów z analizy:** co ma być zawsze w raporcie, czego nie chcesz?

**STOP — poczekaj na odpowiedzi do Sekcji 4.**

---

## SEKCJA 5/5 — Wykluczenia

**Pytania:**

1. **Typy spraw których kancelaria NIE prowadzi:** np. prawo pracy, postępowania sądowe, sprawy karne, startupy pre-seed

2. **Typy klientów których kancelaria NIE obsługuje:** np. konsumenci, klienci spoza PL bez polskiej struktury, branże regulowane (banki, ubezpieczenia)

3. **Cokolwiek jeszcze** co skill powinien wiedzieć o kancelarii, a nie pytaliśmy?

**STOP — poczekaj na odpowiedzi do Sekcji 5.**

---

## Generowanie practice-profile.md

Po zebraniu odpowiedzi ze wszystkich 5 sekcji — wygeneruj plik w poniższym formacie. Uzupełnij wartości na podstawie odpowiedzi; brak odpowiedzi → stosuj wartość domyślną podaną w nawiasach.

Przy generowaniu zastąp: `[DZISIAJ]` → datą dzisiejszą w formacie DD.MM.RRRR; `[lista z odpowiedzi]` → konkretną listą z udzielonych odpowiedzi; `[odpowiedź]` → wybraną wartością z opcji lub tekstem użytkownika.

```markdown
# practice-profile.md
# Konfiguracja kancelarii — plik prywatny (gitignored)
# Wygenerowany przez: workflows/konfiguracja-kancelarii.md
# Data: [DZISIAJ]

## Profil praktyki

Główne typy umów: [lista z odpowiedzi / domyślnie: body leasing IT, NDA, SaaS, wdrożenia]
Reprezentacja: [Zamawiający / Wykonawca / Obustronnie]
Rynek: [B2B krajowy / B2B międzynarodowy / mieszany]
Wielkość klientów: [MŚP / korporacje / mieszane]
Branże specjalizacji: [lista]

## Progi ryzyka

Styl: [Konserwatywny / Umiarkowany / Agresywny / domyślnie: Umiarkowany]
Próg pełnej analizy: [kwota PLN / domyślnie: 100.000 PLN rocznie]

RED bezwzględne (zawsze blokuj bez negocjacji):
- [lista z odpowiedzi]
- [domyślnie: brak cap, wyłączenie winy umyślnej, brak pól eksploatacji przy IP]

## Domyślne pozycje negocjacyjne

Cap odpowiedzialności (punkt wyjścia): [odpowiedź / domyślnie: 12 miesięcy wynagrodzenia netto]
Okres poufności po zakończeniu: [odpowiedź / domyślnie: 3 lata dla informacji zwykłych, bezterminowo dla tajemnicy przedsiębiorstwa]
Pozycja RODO: [Administrator / Podmiot przetwarzający / Obustronnie]
Forum sporów: [odpowiedź / domyślnie: sąd właściwy dla siedziby naszego klienta]
Kary umowne: [standardowo / na żądanie klienta]

## Styl i format

Legal design: [Classic / Light legal design / domyślnie: Light legal design]
Formalność odpowiedzi: [Formal / Semi-formal / Operacyjny / domyślnie: Operacyjny]
Język roboczy: [PL / EN+PL / domyślnie: PL]
Format raportów: [uwagi z odpowiedzi]

## Wykluczenia

Typy spraw poza profilem: [lista z odpowiedzi]
Typy klientów poza profilem: [lista z odpowiedzi]
Uwagi dodatkowe: [odpowiedź do Sekcji 5 pyt. 3]
```

---

## Po wygenerowaniu — instrukcja dla administratora

```
1. Skopiuj wygenerowany blok powyżej do pliku: practice-profile.md
   (w katalogu głównym skilla — tym samym co SKILL.md)

2. Plik jest gitignorowany — nie trafi do repozytorium publicznego.

3. Od tej pory wszystkie workflow czytają practice-profile.md na starcie sesji
   i dostosowują zachowanie do Twojego profilu kancelarii.

4. Aktualizacja profilu: uruchom ponownie ten workflow lub edytuj
   practice-profile.md ręcznie.
```
