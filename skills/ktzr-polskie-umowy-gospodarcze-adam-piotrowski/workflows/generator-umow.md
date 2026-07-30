# Workflow: Generator umów (5 kroków, z kontekstem)


> _Reguły globalne: `references/rdzen-ktzr.md` (R1 cytowania · R2 bramka · R3 role · R4 profil · R5 format)._

> **R3 — LAIK:** dodatkowe sygnały dla umów: „muszę podpisać umowę", „jestem klientem [firmy X]", „sprawdź czy mogę to podpisać".

5-krokowy workflow generowania nowej umowy w stylu KTZR. **Każdy krok wymaga akceptacji użytkownika** przed przejściem dalej. Generator może działać z dodatkowym **kontekstem** (emaile klienta, notatki, brief, dokumenty referencyjne).

## Przyjmowanie briefu i kontekstu

Brief minimalny od użytkownika:
- **Typ umowy** (z listy: body leasing IT, NDA, usługowa IT, wdrożenie, SaaS, przeniesienie praw autorskich, współpraca, zlecenie, księgowa, ugoda, cesja, inna)
- **Strona A** (klient — nazwa, forma prawna, KRS/NIP, adres)
- **Strona B** (kontrahent — nazwa, forma prawna, KRS/NIP, adres)
- **Kluczowe ustalenia** (przedmiot, wynagrodzenie, czas, specjalne wymagania)

**Kontekst dodatkowy (opcjonalny):** emaile, notatki ze spotkań, draft kontrahenta, dokumenty referencyjne. Jeśli użytkownik dostarcza kontekst — traktuj go jako **źródło faktów o sprawie**, ale nie jako wiążące dla treści umowy. Z kontekstu wyciągasz: rzeczywiste ustalenia stron, intencje, ryzyka biznesowe, terminologię preferowaną przez strony.

**Ważne — generator jest odcięty od ewentualnej "bieżącej umowy":** w odróżnieniu od workflowu analizy, generator nie czyta żadnej obecnej umowy jako podstawy. Wyjątek: jeśli użytkownik wyraźnie powie "wzoruj się na tej umowie", "weź to jako szablon".

---

## KROK 0/5: Pamięć kancelarii

Po otrzymaniu briefu — przed analizą — sprawdź pamięć kancelarii pod kątem tej sprawy.

1. `list_categories()` — jeśli pamięć pusta: pomiń resztę kroku, przejdź do KROKU 1
2. Jeśli pamięć niepusta:
   - `recall("nazwa kontrahenta")` — Strona B z briefu
   - `recall("typ umowy")` — np. "body leasing", "NDA", "SaaS"
   - `recall("negocjacje pozycja")` — wcześniejsze ustalenia negocjacyjne

Wyświetl trafienia w sekcji kroku 1 jako:

```
### 📋 Pamięć kancelarii — kontekst sprawy
[podsumowanie trafień — co istotne dla tej umowy]
```

Jeśli brak trafień — **pomiń sekcję**. Przejdź do KROKU 1.

---

## KROK 1/5: Analiza briefu

**Otwórz:** `references/essentialia-mapowanie.md`

Przeanalizuj brief + kontekst. Odpowiedz **zwięźle** (max 1 strona):

1. **Typ stosunku prawnego** (z podstawą: art. 750 KC dla usług, 627 KC dla dzieła, 41 PrAut dla licencji, etc.)
2. **Strony i ich role** (kto co dostarcza, kto za co płaci)
3. **Kluczowe ryzyka** — top 3 ryzyka prawne typowe dla tego typu umowy + ewentualne dodatkowe wynikające z kontekstu
4. **Brakujące informacje** — czego brakuje w briefie, żeby napisać kompletną umowę (kwoty, terminy, pola eksploatacji, etc.)
5. **Rekomendacja** — czy idziemy dalej z tym co jest, czy najpierw uzupełniamy brief

Wymień również **obowiązkowe elementy** zgodnie z `essentialia-mapowanie.md` dla tego typu umowy.

**STOP. Zapytaj:** "Możemy planować strukturę, czy najpierw uzupełniasz brief?"

---

## KROK 2/5: Planowanie struktury

**Otwórz:** `references/baza-klauzul/INDEX.md`

Zaplanuj **strukturę umowy paragraf po paragrafie**. Format:

```
## STRUKTURA UMOWY

§ 1. Przedmiot Umowy
   → klauzule z: `04-przedmiot-umowy.md` (Body Leasing IT)

§ 2. Definicje
   → klauzule z: `03-definicje.md` (Body Leasing IT)
   → definicje do dodania: Specjalista, Timesheet, Utwór, Informacje Poufne

§ 3. Obowiązki Stron
   → klauzule z: `05-obowiazki-stron.md`

§ 4. Wynagrodzenie
   → klauzule z: `06-wynagrodzenie.md`

§ 5. Prawa autorskie
   → klauzule z: `08-prawa-autorskie-ip.md`

[...]

§ N. Postanowienia końcowe
   → klauzule z: `17-postanowienia-koncowe.md`

### Załączniki
- Załącznik nr 1: Wzór Zamówienia
- Załącznik nr 2: Wzór Timesheet
- Załącznik nr 3: Lista Specjalistów
```

**Zasady planowania:**
- Korzystasz **wyłącznie z klauzul w bazie KTZR** (`references/baza-klauzul/`). Nie wymyślasz nowych.
- Wybierasz źródło najbliższe typowi umowy (np. dla body leasing — klauzule specyficzne dla Body Leasing IT, nie generyczne wzorce).
- Wymieniasz **definicje do dodania** w § 1.
- Wymieniasz **załączniki** z konkretnymi nazwami.

**STOP. Zapytaj:** "Akceptujesz tę strukturę? Coś dodać/zmienić przed pisaniem draftu?"

Jeśli użytkownik zgłasza korekty — uwzględnij je i przedstaw ZAKTUALIZOWANĄ strukturę przed przejściem do KROKU 3.

---

## KROK 3/5: Pisanie draftu

**Otwórz teraz (jeśli jeszcze nie otwarto):** `references/style-redakcyjny.md` — masz w tym pliku konkretne wzorce składniowe KTZR (konstrukcje warunkowe, definicje, wyliczenia, nazewnictwo stron). Pisz draft **zgodnie z tym stylem**, nie z generycznymi konwencjami pisania umów.

Na podstawie zatwierdzonej struktury napisz **pełną umowę**.

### Zasady pisania

1. **Wyłącznie klauzule z bazy KTZR** — żadnej improwizacji. Jeśli baza nie ma odpowiedniej klauzuli na coś, co struktura przewiduje — **przerwij i zapytaj użytkownika** zamiast wymyślać.

2. **Dopasowanie do kontekstu:**
   - Konkretne nazwy stron (z briefu, nie placeholdery "[Strona A]")
   - Konkretne kwoty/stawki/terminy (z briefu)
   - Spójne nazewnictwo (jeśli "Usługodawca" w § 1, to "Usługodawca" w całej umowie)
   - Odesłania działające (po napisaniu draftu sprawdź każde "§ X ust. Y")

3. **Definicje w § Definicje:**
   - Każdy termin pisany Wielką Literą w treści musi mieć definicję tutaj
   - Definicje w kolejności alfabetycznej
   - Definicja w formacie: „Termin" — opis (...).

4. **Złote Reguły KTZR** mają pierwszeństwo nad bazą klauzul — np. jeśli klauzula z bazy ma odesłanie "zgodnie z § 5", a w Twojej strukturze § 5 to co innego — popraw odesłanie.

5. **Cytaty przepisów — obowiązek weryfikacji:** każdy artykuł przywołany w klauzuli (np. „art. 473 § 2 KC", „art. 28 RODO") → wywołaj `verify_article()` przed wpisaniem brzmienia. Jeśli MCP niedostępny → dopisz `[NIEZWERYFIKOWANE]` przy cytacie. Halucynacja treści przepisu dyskwalifikuje draft.

### Format wyjścia

```
UMOWA [TYP]

zawarta w dniu [data] w [miejscu], pomiędzy:

[Strona A z pełnymi danymi i reprezentacją]
— zwaną dalej "[Rola]"

a

[Strona B z pełnymi danymi i reprezentacją]
— zwaną dalej "[Rola]"

Strony postanawiają, co następuje:

§ 1. Przedmiot Umowy

[Treść klauzuli z bazy, dopasowana]

§ 2. Definicje

W rozumieniu niniejszej Umowy:
1. „Termin1" — opis (...);
2. „Termin2" — opis (...);
[...]

[Treść klauzuli z bazy, dopasowana]

[...]

§ N. Postanowienia końcowe

1. [Klauzula salwatoryjna]
2. [Forma zmian]
3. [Załączniki]
4. [Egzemplarze]
5. [Wejście w życie]

___________________            ___________________
[Strona A]                     [Strona B]

Załączniki:
1. [Nazwa załącznika]
2. [...]
```

**STOP. Zapytaj:** "Idziemy do weryfikacji kompletności, czy chcesz najpierw coś poprawić w drafcie?"

---

## KROK 4/5: Weryfikacja kompletności

**Otwórz:** `references/checklist-15.md`

Sprawdź draft przez **checklistę 15 punktów**. Dla każdego: ✅ / ⚠️ / ❌ / ➖ (N/D — nie dotyczy). Następnie:

1. **Brakujące elementy** — co powinno być a nie ma
2. **Komentarz do typu umowy** — czy są elementy specyficzne dla tego typu (z `essentialia-mapowanie.md`), których brakuje
3. **Nadmiarowe elementy** — co jest zbędne, można usunąć
4. **Rekomendacje** — co dopisać przed kontrolą jakości

Następnie **dopisz brakujące paragrafy** (pełny tekst, z bazy klauzul) i zwróć **CAŁY draft z poprawkami** (nie tylko changesy — pełny tekst, gotowy do dalszej obróbki).

**STOP. Zapytaj:** "Idziemy do kontroli jakości, czy chcesz coś jeszcze dodać/zmienić?"

---

## KROK 5/5: Kontrola jakości (QA)

Wykonaj końcową kontrolę:

1. **Spójność definicji** — każde użycie wielką literą = definicja w § 1
2. **Odesłania wewnętrzne** — każde "§ X ust. Y" prowadzi do istniejącego przepisu
3. **Terminologia** — jedno pojęcie = jeden termin
4. **Załączniki** — każdy załącznik wymieniony w preambule/końcu jest też przywołany w treści
5. **Numeracja** — paragrafy, ustępy, punkty numerowane spójnie
6. **Dane stron** — KRS, NIP, REGON, adresy kompletne i prawidłowo sformatowane
7. **Daty i terminy** — daty pełne (dd-mm-rrrr), terminy w jednostkach jednorodnych (dni / Dni Robocze)
8. **Złote Reguły KTZR** — sprawdź każdą z 12 reguł

Zwróć **FINALNĄ WERSJĘ** umowy — sam tekst umowy, **bez komentarzy w treści**. Komentarze QA osobno PRZED finalną wersją w formacie:

```
## KONTROLA JAKOŚCI

✅ Wszystkie definicje spójne (sprawdzono 12 terminów)
✅ Odesłania wewnętrzne — 8/8 prowadzą do istniejących przepisów
⚠️ Termin "Dni Robocze" w § 5 ust. 3 — w § 1 zdefiniowano jako "dni od pn. do pt. z wyłączeniem dni ustawowo wolnych"; sprawdź zgodność
[...]
```

---

## BRAMKA FINALNA

Wyświetl użytkownikowi poniższe pytania i **zaczekaj na odpowiedź** przed generowaniem:

```
⛔ Przed finalną wersją — potwierdź:
1. Dane stron (KRS/NIP/adresy) zweryfikowane źródłowo?
2. Cytowane przepisy sprawdzone (verify_article lub ręcznie)?
3. Prawnik prowadzący sprawę widział ten draft?

→ „tak, generuj finalną wersję" / lub wskaż co poprawić
```

Dopiero po potwierdzeniu — generuj. Bez potwierdzenia — zwróć `[DRAFT — DO WERYFIKACJI]` nad dokumentem i zatrzymaj się.

Wyjątek: jeśli użytkownik powiedział „tryb express" lub „zrób bez pytania" — generuj, ale dodaj `[DRAFT — DO WERYFIKACJI]` na początku i końcu dokumentu.

---

## FINALNA UMOWA

[czysty tekst gotowy do wklejenia w dokument, bez komentarzy w treści]

---

## Iteracja: REDRAFT

Jeśli po kroku 5 użytkownik chce poprawić draft ("zmień § 4 — dodaj waloryzację", "usuń klauzulę X", "dodaj non-solicitation"):

1. Otwórz odpowiedni plik z bazy klauzul, weź klauzulę
2. Wprowadź zmianę w finalnym tekście
3. Przebiegnij KROK 5 (QA) ponownie — sprawdź czy zmiana nie zepsuła odesłań, definicji, numeracji
4. Zwróć ponownie cały draft

---

## Specjalny tryb: generowanie z kontekstem

Jeśli użytkownik dostarczył **kontekst** (emaile, notatki, draft kontrahenta, brief biznesowy) — w **KROKU 1** dodaj sekcję:

```
### Z kontekstu wyciągnąłem
- Ustalenie 1: [...]
- Ustalenie 2: [...]
- Preferowana terminologia stron: "Klient" zamiast "Zamawiający"
- Ryzyko zidentyfikowane przez Twojego klienta: [...]
```

To pomaga użytkownikowi sprawdzić, czy dobrze zrozumiałeś kontekst, zanim zaczniesz pisać. W kolejnych krokach uwzględniaj ustalenia z kontekstu (kwoty, terminologia, ryzyka), ale nie kopiuj treści z kontekstu do umowy — umowa zawsze składana jest z klauzul KTZR.
