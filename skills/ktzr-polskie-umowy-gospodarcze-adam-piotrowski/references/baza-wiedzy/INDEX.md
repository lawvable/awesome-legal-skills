# Baza wiedzy — INDEX

Doktryna prawnicza, orzecznictwo i strategia kontraktowa wspomagająca rozumienie typu prawnego umów IT i konstrukcji klauzul. Pliki są pogrupowane **po zagadnieniach prawnych**, nie po typach umów — bo jedno zagadnienie (np. lucrum cessans, prawa autorskie, RODO) pojawia się w wielu typach umów.

## Zasada nadrzędna — wiedza vs tekst umowy

Wszystkie pliki bazy wiedzy to **wiedza doktrynalna**, nie tekst do kopiowania do umowy. Liczne odesłania do art. KC/PrAut/RODO/KP są tutaj kontekstem doktrynalnym. W generowanej treści umowy stosuj zasadę **W6 — Oszczędne odsyłanie do przepisów** (`references/style-redakcyjny.md`).

## Mapa bazy

### Prawa autorskie i oprogramowanie

| Plik | Zagadnienie | Kiedy sięgnąć |
|---|---|---|
| `01-maintenance-art750-kc.md` | Maintenance IT i SLA — art. 750 KC | Umowa zawiera "maintenance", "utrzymanie", "wsparcie", "SLA", "managed services". Pytanie: dzieło czy zlecenie/usługi? |
| `02-przeniesienie-praw-oprogramowanie.md` | Pola eksploatacji, utwory przyszłe (art. 41, 74 PrAut) | Umowa zawiera "przeniesienie praw autorskich", "pola eksploatacji", "Utwór". Brak wymienienia pól = krytyczny błąd |
| `03-prawa-zalezne-osobiste-program.md` | Utwory zależne, autorskie prawa osobiste (art. 74, 77 PrAut) | W umowie z programem komputerowym i fazą rozwoju. Pytanie o modyfikacje, nadzór autorski, prawo do oznaczenia autorstwa |
| `04-open-source-copyleft.md` | Open source, copyleft, indemnifikacja (art. 75-76 PrAut) | Umowa wdrożeniowa IT. Klient chce zabezpieczenia przed copyleft. Pytania o GPL/AGPL/MIT, "zakaz open source" |
| `11-wizerunek-a-prawa-autorskie.md` | Wizerunek (art. 81 PrAut) vs. autorskie prawa majątkowe do utworu audiowizualnego — autonomia reżimów, cofnięcie zgody ex nunc, wyjątki z art. 81 ust. 2, ciężar dowodu zakresu zgody | Sprawy o nagrania z udziałem osób (instruktorzy, prelegenci, modele). Umowy o dzieło z klauzulą "wszystkie prawa autorskie" obejmujące materiały z wizerunkiem. Ugody i porozumienia wizerunkowe. Argumenty "mamy prawa autorskie, więc możemy puszczać" |

### Odpowiedzialność kontraktowa

| Plik | Zagadnienie | Kiedy sięgnąć |
|---|---|---|
| `05-cap-lucrum-wina-umyslna.md` | Cap odpowiedzialności, wyłączenie lucrum cessans, granica art. 473 § 2 KC | W umowie pojawia się "cap", "limit of liability", "lucrum cessans", "consequential damages", "wina umyślna". Generowanie § Odpowiedzialność |
| `06-sila-wyzsza-i-podwykonawcy.md` | Siła wyższa, odpowiedzialność za podwykonawców (art. 474 KC), zmiana prawa | W umowie pojawia się "force majeure", "podwykonawca", "operator chmury", "change of law". Pytania o odpowiedzialność za AWS/Azure/GCP |
| `07-indemnifikacja-kary-umowne.md` | Klauzule indemnifikacyjne (hold harmless), kary umowne (art. 484 § 1 KC), odszkodowanie uzupełniające | "Indemnity", "hold harmless", "kara umowna", "odszkodowanie uzupełniające", "exclusive remedy" |

### Regulaminy i usługi elektroniczne

| Plik | Zagadnienie | Kiedy sięgnąć |
|---|---|---|
| `13-regulamin-usdde-hosting-ai.md` | Regulamin u.ś.u.d.e. — obowiązkowe elementy (art. 8), wyłączenie odpowiedzialności hostingu (art. 14), DSA (notice & action, uzasadnianie decyzji), usługi AI jako wariant usługi elektronicznej | Tworzenie lub analiza regulaminu hostingu/SaaS/domen/AI. Pytania o zakres obowiązku ustawowego, wyłączenie odpowiedzialności, AUP, DSA |

### Compliance AI Act

| Plik | Zagadnienie | Kiedy sięgnąć |
|---|---|---|
| `14-polityka-ai-wdrozenie.md` | Polityka AI firmowa — komentarz prawnika: §-po-§, kluczowe luki (Rejestr, umowa powierzenia RODO, Opiekun), checklista wdrożeniowa, tabela terminów AI Act | Klient/firma chce wdrożyć politykę AI. Pytania o art. 4 AI Act, zakazy art. 5, obowiązki chatbot/deepfake art. 50, incydenty AI, rekrutacja AI — kiedy potrzebne odrębne procedury. |

### Wykładnia i interpretacja

| Plik | Zagadnienie | Kiedy sięgnąć |
|---|---|---|
| `12-wykladnia-oswiadczen-woli.md` | Wykładnia kombinowana (art. 65 k.c.), prymat wykładni językowej, metoda derywacyjna, zakaz prawotwórczej — z tezami SN 2024–2025 | Sporna klauzula umowna — jakie znaczenie nada jej sąd? Analiza ryzyka wieloznaczności. Spór o rozumienie pojęcia. Akty zakładowego prawa pracy (regulamin, ZUZP). |

### RODO w umowach IT

| Plik | Zagadnienie | Kiedy sięgnąć |
|---|---|---|
| `08-rodo-powierzenie-konstrukcja.md` | Kwalifikacja administrator/procesor/współadministrator, art. 28 ust. 3 RODO, subprocesorzy, zwrot/usunięcie danych | "Powierzenie przetwarzania", "DPA", "procesor", "administrator", "subprocesor". Generowanie umowy powierzenia |
| `09-rodo-bezpieczenstwo-i-naruszenia.md` | Środki techniczne i organizacyjne (art. 32 RODO), incydenty bezpieczeństwa (art. 33-34 RODO) | "Środki TOMs", "ISO 27001", "SOC 2", "data breach", "incydent", "72 godziny" |
| `10-rodo-audyt-i-odpowiedzialnosc-administracyjna.md` | Prawo audytu (art. 28 ust. 3 lit. h), kary administracyjne (art. 82-83 RODO), regres A → P | "Prawo audytu", "kontrola procesora", "kary RODO", "regres", "PUODO" |

## Powiązania z klauzulami i stylem

Baza wiedzy łączy się z trzema innymi miejscami w skillu:

1. **Klauzule praktyczne** (`baza-klauzul/`) — wiedza doktrynalna wyjaśnia, **dlaczego** klauzule są napisane tak a nie inaczej
2. **Złote Reguły** (`references/zlote-reguly.md`) — wiedza doktrynalna nie zastępuje reguł nadrzędnych
3. **Styl redakcyjny** (`references/style-redakcyjny.md`) — wiedza doktrynalna nie zmienia zasady oszczędnego odsyłania (W6)

## Typowe ścieżki użycia

**Analiza umowy maintenance IT z SLA:**
1. `references/essentialia-mapowanie.md` → kwalifikacja prawna
2. `baza-wiedzy/01-maintenance-art750-kc.md` → potwierdzenie/uściślenie art. 750 KC, charakter starannego działania
3. `baza-klauzul/04-przedmiot-umowy.md` → klauzule

**Generowanie umowy przeniesienia praw do programu z open source:**
1. `references/essentialia-mapowanie.md` → wymagania konstrukcyjne
2. `baza-wiedzy/02-przeniesienie-praw-oprogramowanie.md` → katalog pól eksploatacji
3. `baza-wiedzy/03-prawa-zalezne-osobiste-program.md` → konstrukcja praw zależnych/osobistych
4. `baza-wiedzy/04-open-source-copyleft.md` → trzy warstwy ochrony
5. `baza-klauzul/08-prawa-autorskie-ip.md` → klauzule

**Analiza ryzyka spornej klauzuli — co powie sąd:**
1. `baza-wiedzy/12-wykladnia-oswiadczen-woli.md` → metoda kombinowana, obiektywna, prymat językowej
2. `workflows/ocena-2-strony.md` → Kategoria 2 (Niejednoznaczności interpretacyjne) — operacyjne zastosowanie

**Negocjowanie ograniczeń odpowiedzialności w umowie SaaS:**
1. `baza-wiedzy/05-cap-lucrum-wina-umyslna.md` → ramy cap'u, granica art. 473 § 2 KC
2. `baza-wiedzy/06-sila-wyzsza-i-podwykonawcy.md` → siła wyższa, AWS/Azure jako podwykonawca
3. `baza-wiedzy/07-indemnifikacja-kary-umowne.md` → indemnifikacja IP poza cap'em
4. `baza-klauzul/11-odpowiedzialnosc.md` → klauzule

**Konstrukcja umowy powierzenia danych osobowych:**
1. `baza-wiedzy/08-rodo-powierzenie-konstrukcja.md` → kwalifikacja, elementy obowiązkowe art. 28 ust. 3, subprocesorzy
2. `baza-wiedzy/09-rodo-bezpieczenstwo-i-naruszenia.md` → środki techniczne, klauzula incydentów
3. `baza-wiedzy/10-rodo-audyt-i-odpowiedzialnosc-administracyjna.md` → audyt, regres kar
4. `baza-klauzul/14-rodo.md` → klauzule praktyczne

