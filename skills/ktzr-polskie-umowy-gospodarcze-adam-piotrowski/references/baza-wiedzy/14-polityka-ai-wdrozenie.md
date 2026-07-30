# Polityka AI w firmie — komentarz prawnika (jak nie wdrożyć wzoru „w ciemno")

**Źródło:** opracowanie KTZR — Kancelaria Radców Prawnych Żurawska Piotrowski i Wspólnicy, Gdańsk (ktzr.pl).  
**Wzór:** `references/baza-klauzul/21-polityka-ai.md`  
**Status:** zatwierdzone do bazy wiedzy KTZR — lipiec 2026.

## TL;DR — co Claude musi wiedzieć

1. Polityka AI to narzędzie zarządzania, nie tylko compliance — jej wartość polega na tym, że w razie wycieku lub błędu „halucynującego" modelu firma ma **jasne reguły i się czym bronić**.
2. Od **2 lutego 2025 r.** obowiązuje art. 4 AI Act (obowiązek zapewnienia kompetencji w zakresie AI) — polityka + szkolenie + oświadczenie to minimalne wypełnienie tego przepisu.
3. Wzór dotyczy wyłącznie roli **deployera (podmiotu stosującego)** — tworzenie własnego systemu AI przenosi firmę do znacznie cięższego reżimu dostawcy.
4. **Trzy krytyczne luki**, przez które polityki zawodzą w praktyce: brak imiennego Opiekuna (martwy dokument), pusta tabela Rejestru (fikcja kontroli), brak umowy powierzenia RODO z dostawcą narzędzia AI (naruszenie art. 28 RODO).
5. Polityka „ożywa" dopiero z **wypełnionym Rejestrem narzędzi AI** (Zał. 1) — bez niego każde użycie ChatGPT jest poza kontrolą.

---

## Przewodnik paragraf po paragrafie

### §1. Cel i zakres — kogo obowiązuje

**Co robi:** rozciąga politykę na wszystkich pracujących na rzecz firmy, niezależnie od podstawy współpracy, i zawęża ją do roli podmiotu stosującego (deployera) w rozumieniu AI Act.

**Na co uważać:** rozdzielenie ról jest kluczowe — tworzenie własnego narzędzia AI przenosi firmę do dużo cięższego reżimu dostawcy. Dobrze, że zakres obejmuje też współpracowników B2B i funkcje AI wbudowane w inne oprogramowanie — to oni najczęściej wypadają poza „oczywisty" obraz AI.

---

### §2. Definicje — tu przesądza się szczelność

**Co robi:** definiuje System AI (przez art. 3 pkt 1 AI Act), szeroko ujęte Narzędzie AI, Cele służbowe oraz Dane chronione.

**Na co uważać:** dwie definicje robią najwięcej roboty.

**„Narzędzie AI"** łapie też użycie pośrednie (osadzony model, cudze API) — ucina wykręt „to zwykły program".

**„Cele służbowe"** zawierają twardą regułę: jeśli wrzucasz do narzędzia informacje o firmie lub kliencie, to zawsze użycie służbowe — niezależnie od urządzenia i pory. To zamyka lukę „robiłem to prywatnie z domowego laptopa".

---

### §3. Narzędzia dopuszczone i zakazane

**Co robi:** dopuszcza wyłącznie narzędzia z Rejestru, zakazuje praktyk z art. 5 AI Act i używania AI do decyzji o osobach (rekrutacja, ocena pracowników — systemy wysokiego ryzyka z zał. III AI Act).

**Na co uważać:**

Przy „rozpoznawaniu emocji w miejscu pracy" art. 5 ust. 1 lit. f ma wyjątek — względy medyczne lub bezpieczeństwa. Wzór podaje to jako zakaz bez wyjątku; to dopuszczalne (firma może być surowsza), ale rób to świadomie.

Zastosowania HR słusznie wymagają odrębnych procedur — sama polityka nie wystarczy dla systemów wysokiego ryzyka.

---

### §4. Bezpieczeństwo danych — czego nie wolno wrzucać

**Co robi:** zakazuje wprowadzania Danych chronionych do narzędzi AI; wyjątek wymaga łącznie: narzędzie w Rejestrze + podstawa prawna + zgoda Opiekuna + umowa powierzenia (art. 28 RODO). Nakazuje anonimizację i ocenę potrzeby DPIA.

**Na co uważać:** tu firmy potykają się najczęściej.

Wrzucenie danych osobowych do zewnętrznego narzędzia to **powierzenie** — art. 28 RODO wymaga odrębnej umowy (forma pisemna lub elektroniczna). Kliknięcie „akceptuję regulamin" tego **nie zastępuje**.

Pseudonimizacja to wciąż dane osobowe — wzór trafnie o tym przypomina.

---

### §5. Weryfikacja przez człowieka — kto odpowiada za błąd AI

**Co robi:** nakłada obowiązek sprawdzenia wyniku (prawdziwość, aktualność, prawa osób trzecich) przed użyciem i przesądza, że „halucynacja" nie zwalnia z odpowiedzialności.

**Na co uważać:**

Dwa niuanse prawnoautorskie:
- Wytwór **w całości wygenerowany przez AI** może nie być utworem (brak ochrony prawnoautorskiej).
- Wynik AI **nie jest domyślnie „czysty"** od praw osób trzecich (przy kodzie: licencje open source).

Wzór zastrzega, że nie rozszerza odpowiedzialności ponad przepisy bezwzględnie obowiązujące — to ważne dla stosunków z pracownikami.

---

### §6. Oznaczanie treści tworzonych z AI

**Co robi:** wprowadza obowiązek oznaczania treści z AI udostępnianych na zewnątrz oraz zasady dla chatbotów i deepfake'ów (art. 50 AI Act).

**Na co uważać:** obowiązki z art. 50 są rozdzielone rolowo:
- chatbot (ust. 1) — obowiązek informowania o interakcji z AI,
- deepfake (ust. 4) — obowiązek ujawnienia manipulacji.

Rozsądny jest wyjątek dla użycia pomocniczego (korekta językowa) — odpowiada wyjątkowi „standardowej edycji" z art. 50 ust. 2.

---

### §7. Incydenty — co zrobić, gdy coś wycieknie

**Co robi:** nakazuje zgłoszenie incydentu Opiekunowi w wyznaczonym terminie, chroni zgłaszającego w dobrej wierze, wstrzymuje użycie narzędzia i każe zabezpieczyć dowody.

**Na co uważać:**

Wpisz **konkretny termin** zgłoszenia (we wzorze pole `[……..] dni`) — „niezwłocznie" bez liczby dni bywa źródłem sporu.

Powiązanie z reżimem AI Act (poważny incydent → obowiązki wobec dostawcy i organów nadzoru) i z RODO (inspektor ochrony danych) jest tu na miejscu — ale wymaga, żeby Opiekun wiedział, co sprawdzić.

---

### §8–§9. Opiekun Polityki i szkolenia

**Co robi:** wskazuje właściciela procesu (Opiekun/AI Owner) — prowadzi Rejestr, przyjmuje zgłoszenia, robi przeglądy — oraz przewiduje szkolenia wstępne i okresowe z oświadczeniem (art. 4 AI Act).

**Na co uważać:**

Bez **imiennie wskazanego Opiekuna** i realnego cyklu przeglądów polityka staje się martwym dokumentem. Zalecane: przegląd co 6–12 miesięcy i po każdej istotnej zmianie przepisów (Digital Omnibus może przesunąć terminy AI Act).

Szkolenie odwzorowuje przesłanki art. 4 (rola, wiedza, kontekst) — to dobrze i wystarczające jako minimum.

---

### §10 i załączniki

**Co robi:** wiąże naruszenie z odpowiedzialnością pracowniczą/kontraktową, reguluje zmiany i wejście w życie; sercem operacyjnym jest Rejestr narzędzi AI (Zał. 1) i oświadczenie (Zał. 2).

**Na co uważać:**

Polityka „ożywa" dopiero z **wypełnionym Rejestrem**. Sam wzór (§10 bez uzupełnionego Zał. 1) to szkielet bez mięśni.

Pamiętaj o zastrzeżeniu stanu prawnego — terminy stosowania AI Act mogą się zmienić w związku z pakietem Digital Omnibus.

---

## Checklista przed przyjęciem polityki (5 minut)

| # | Co sprawdzić | OK? |
|---|---|---|
| 1 | Uzupełniono wszystkie pola `[…]` (nazwa firmy, data, Opiekun, termin incydentu, okres przeglądu) | ☐ |
| 2 | Rejestr narzędzi AI (Zał. 1) zawiera faktycznie używane narzędzia z oceną ryzyka i zatwierdzonym celem | ☐ |
| 3 | Dla każdego narzędzia z Rejestru: sprawdzono, czy dostawca oferuje umowę powierzenia (art. 28 RODO) | ☐ |
| 4 | Zidentyfikowano Opiekuna Polityki i przekazano mu zakres obowiązków | ☐ |
| 5 | Zaplanowano szkolenie wstępne dla wszystkich objętych Polityką i zbieranie oświadczeń (Zał. 2) | ☐ |
| 6 | Określono tryb aktualizacji (kto, kiedy, jak informuje o zmianach) | ☐ |
| 7 | Zastosowania HR (rekrutacja, ocena pracowników) — jeśli planowane — mają odrębne procedury AI Act | ☐ |
| 8 | Zaplanowano datę pierwszego przeglądu Polityki | ☐ |

---

## Przepisy kluczowe

| Przepis | Treść | Obowiązuje od |
|---|---|---|
| Art. 4 AI Act | Kompetencje w zakresie AI — obowiązek zapewnienia szkolenia | 2 lutego 2025 r. |
| Art. 5 AI Act | Praktyki zakazane (manipulacja, scoring społeczny, rozpoznawanie emocji w miejscu pracy) | 2 lutego 2025 r. |
| Zał. III AI Act | Systemy wysokiego ryzyka (rekrutacja, zarządzanie pracownikami, ocena) | 2 sierpnia 2026 r. |
| Art. 50 AI Act | Przejrzystość: oznaczanie AI, chatboty, deepfake | 2 sierpnia 2026 r. |
| Art. 28 RODO | Umowa powierzenia danych osobowych z podmiotem przetwarzającym | Obowiązuje |

*Stan prawny: lipiec 2026. Terminy AI Act mogą ulec zmianie (Digital Omnibus) — przed wdrożeniem zweryfikuj aktualny stan przez `mcp__aiakt-kb__przepis()` lub bezpośrednio w EUR-Lex CELEX:32024R1689.*
