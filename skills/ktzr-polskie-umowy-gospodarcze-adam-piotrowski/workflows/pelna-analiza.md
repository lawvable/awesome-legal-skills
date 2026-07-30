# Workflow: Pełna analiza umowy (5 etapów)


> _Reguły globalne: `references/rdzen-ktzr.md` (R1 cytowania · R2 bramka · R3 role · R4 profil · R5 format)._

5-etapowy workflow analizy umowy. **Po każdym etapie zatrzymaj się i poczekaj na korekty użytkownika** zanim przejdziesz do następnego. To nie jest one-shot — to dialog.

## Tryb express (opcjonalny)

Jeśli użytkownik wyraźnie powie "zrób całość bez pytania", "tryb express", "wszystkie 5 etapów naraz" — wykonaj wszystkie etapy w jednej odpowiedzi, ale i tak każdy etap jako osobną sekcję z nagłówkiem. W przeciwnym razie postępuj po jednym etapie.

---

## ETAP 0/5: Pamięć kancelarii

Przed analizą sprawdź pamięć kancelarii — wcześniejsze wpisy o tej sprawie lub kontrahencie mogą zmienić priorytety analizy.

1. `list_categories()` — jeśli pamięć pusta: pomiń resztę etapu, przejdź do ETAP 1
2. Jeśli pamięć niepusta:
   - `recall("nazwa kontrahenta")` — jeśli widoczna w umowie
   - `recall("typ umowy")` — np. "body leasing", "NDA", "wdrożenie"
   - `recall("ryzyka negocjacje")` — pozycje negocjacyjne, ryzyka zaznaczone wcześniej

Wyświetl trafienia przed ETAP 1:

```
📋 Pamięć kancelarii — kontekst sprawy:
[podsumowanie trafień — max 5 wpisów, tylko co istotne dla tej analizy]
```

Jeśli brak trafień — **pomiń sekcję**. Przejdź do ETAP 1.

---

## ETAP 1/5: Essentialia negotii

**Otwórz:** `references/essentialia-mapowanie.md`

Zmapuj pięć elementów: typ umowy, strony, przedmiot, wynagrodzenie, czas. Następnie podaj **krytyczne elementy dla tego typu umowy** zgodnie z mapowaniem w pliku referencyjnym.

**Format wyjścia:**

```
## ETAP 1/5: ESSENTIALIA NEGOTII

- **Typ:** [...]
- **Strony:** [Strona A] (rola) / [Strona B] (rola)
- **Przedmiot:** [zwięźle, 1-2 zdania]
- **Wynagrodzenie:** [model + kwota/stawka + termin]
- **Czas:** [określony/nieokreślony + szczegóły]

### Krytyczne elementy dla tego typu umowy
- [...]
- [...]
```

**STOP. Zapytaj:** "Potwierdzasz to mapowanie? Czy coś dodać/poprawić przed checklistą kompletności?"

---

## ETAP 2/5: Checklist kompletności (15 punktów)

**Otwórz:** `references/checklist-15.md`

Przejdź przez wszystkie 15 punktów. Dla każdego oznacz status (✅ / ⚠️ / ❌ / ➖) z krótkim uzasadnieniem (1-2 zdania).

**Format wyjścia:**

```
## ETAP 2/5: CHECKLIST KOMPLETNOŚCI (15 punktów)

1. **Preambuła i data** — ✅ Data dd-mm-rrrr, Gdańsk, prawidłowa struktura.
2. **Strony i reprezentacja** — ⚠️ Brak numeru KRS po stronie Zamawiającego; reprezentacja przez prokurenta bez wskazania prokury.
3. **Definicje** — ❌ Brak definicji "Specjalista" mimo używania w treści.
[...]
15. **Postanowienia końcowe** — ✅ Wszystko OK.

### Wynik: X/15 punktów spełnionych
```

Wskaż na końcu **TOP 3 braki** wymagające naprawy.

**STOP. Zapytaj:** "Idziemy do logiki wewnętrznej, czy najpierw chcesz poprawić któryś z braków?"

---

## ETAP 3/5: Logika wewnętrzna i spójność

Sprawdź spójność wewnętrzną umowy:

1. **Niezdefiniowane pojęcia** — każde słowo pisane Wielką Literą musi mieć definicję
2. **Niespójność nazewnictwa stron** — np. "Wykonawca" w jednym paragrafie i "Zleceniobiorca" w innym
3. **Błędne odesłania wewnętrzne** — "zgodnie z § 5 ust. 3" tam, gdzie § 5 nie ma ust. 3
4. **Osierocone załączniki** — wymienione w preambule ale nie przywołane / przywołane ale brakujące
5. **Niespójność terminów** — np. "30 dni" w jednym miejscu i "miesiąc" w drugim dla tej samej rzeczy
6. **Powtórzenia regulacji** — ta sama klauzula w dwóch miejscach

### ⚠️ AUTOMATYCZNY TRIGGER dla długich umów

**Modele językowe mają znaną tendencję do gubienia powiązań w długich dokumentach** (attention dilution — uwaga modelu nie jest jednolita w długim kontekście, szczególnie dla relacji między odległymi fragmentami).

**Sprawdź czy spełnione co najmniej dwa z poniższych:**
- Umowa > 15 stron lub > 5 000 słów
- > 15 paragrafów
- > 10 odesłań międzyparagrafowych ("§ X ust. Y") w treści
- Wstępna analiza (kroki 1-6 powyżej) wykazała > 3 niespójności
- Słowa kluczowe sygnalizujące złożoność: "Załącznik", "z zastrzeżeniem", "powyższe", "stosuje się odpowiednio"

**Jeśli spełnione co najmniej dwa z powyższych** — zamiast skróconej analizy w 1-2 zdaniach, **otwórz `workflows/weryfikacja-spojnosci-odeslan.md`** i wykonaj jego dwuetapową procedurę (inwentaryzacja → weryfikacja). To zajmie 5-10 min, ale wykrywa błędy, których pojedynczy przebieg nie złapie.

Zakomunikuj użytkownikowi:

> *"Umowa jest długa i zawiera wiele odesłań między paragrafami. Modele językowe gubią powiązania w długich dokumentach — sugeruję dedykowaną weryfikację odesłań (dwuetapowy workflow: inwentaryzacja + sprawdzanie). Zajmie 5-10 minut. Akceptujesz?"*

Jeśli użytkownik się zgadza — uruchom `weryfikacja-spojnosci-odeslan.md` w pełnej postaci (Pass 1 → STOP → Pass 2 → Raport). Wynik z raportu wkomponuj do ETAP 3 zamiast standardowego formatu poniżej.

Jeśli użytkownik się nie zgadza lub umowa jest krótka — wykonaj standardową analizę poniżej.

### Standardowy format wyjścia (krótkie umowy)

```
## ETAP 3/5: LOGIKA WEWNĘTRZNA

### Niezdefiniowane pojęcia
- "Timesheet" (§ 5 ust. 2) — używane bez definicji
- "Wada Krytyczna" (§ 8) — definicja brakuje

### Niespójność nazewnictwa
- ✅ Spójne ("Usługodawca" w całej umowie)

### Odesłania wewnętrzne
- ❌ § 6 ust. 4 odsyła do "§ 4 ust. 5" — § 4 ma tylko 3 ustępy

### Załączniki
- ⚠️ Załącznik nr 2 (wzór Timesheet) wymieniony w treści, nie wymieniony w wykazie załączników

### Powtórzenia
- ⚠️ Kara umowna za zwłokę w § 9 ust. 2 i § 13 ust. 1 — sprawdzić czy świadome rozróżnienie czy duplikat
```

**STOP. Zapytaj:** "Idziemy do audytu ryzyk, czy najpierw naprawiamy logikę?"

---

## ETAP 4/5: Audyt ryzyk

Zidentyfikuj wszystkie ryzyka prawne i biznesowe. Każde z poziomem i lokalizacją.

**Poziomy:**
- 🔴 **KRYTYCZNY** — może prowadzić do nieważności umowy, nieograniczonej odpowiedzialności, utraty praw lub egzekucji przez drugą stronę
- 🟠 **WYSOKI** — istotne ryzyko finansowe lub operacyjne, wymaga natychmiastowej negocjacji
- 🟡 **ŚREDNI** — warto poprawić, ale nie deal-breaker
- 🟢 **NISKI** — drobne nieścisłości, ulepszenie stylu

**Format wyjścia (każde ryzyko):**

```
🔴 KRYTYCZNY | § 11 ust. 2 — Nieograniczona odpowiedzialność
Brak limitu odpowiedzialności Wykonawcy. W razie szkody z winy zwykłej Wykonawca odpowiada w pełnym zakresie, łącznie z lucrum cessans.
**Rekomendacja:** Dodać cap (np. 12 mies. wynagrodzenia), wyłączyć lucrum cessans, zastrzec wyjątek winy umyślnej (art. 473 § 2 KC). Klauzule do użycia: `references/baza-klauzul/11-odpowiedzialnosc.md`.
```

Na końcu **ocena bezpieczeństwa (0–100)** + uzasadnienie.

**STOP. Zapytaj:** "Idziemy do rekomendacji, czy chcesz najpierw obgadać któreś z ryzyk?"

---

## ETAP 5/5: Podsumowanie i rekomendacje

**Format wyjścia:**

```
## ETAP 5/5: PODSUMOWANIE I REKOMENDACJE

### TOP 3 do naprawy
1. **[Problem]** — `[paragraph]` — rekomendowana klauzula z: `[plik z bazy]`
2. [...]
3. [...]

### Sugerowane zmiany terminologiczne
- "Zleceniobiorca" → "Wykonawca" (spójność z § 1)
- [...]

### Ogólna ocena umowy
[2-3 zdania: czy umowa jest do podpisania, do negocjacji, do gruntownej przeróbki]
```

**Na końcu (tylko tutaj):**

> *Analiza ma charakter pomocniczy i nie zastępuje oceny radcy prawnego prowadzącego sprawę.*

---

## Zachowanie agentowe — co robić, gdy użytkownik przerywa workflow

- Jeśli użytkownik po etapie 2 pisze "popraw § 5 ust. 3" — przerwij workflow, wykonaj `workflows/popraw-fragment.md`, potem zapytaj "wracamy do analizy od etapu 3?"
- Jeśli użytkownik pisze "wystarczy" / "dziękuję" po jakimś etapie — kończ, nie naciskaj
- Jeśli użytkownik wkleja inną umowę — to nowe zadanie, startujesz workflow od nowa
- Jeśli użytkownik prosi o klauzulę z bazy — odsyłaj do odpowiedniego pliku w `references/baza-klauzul/` i wracaj do workflowu
