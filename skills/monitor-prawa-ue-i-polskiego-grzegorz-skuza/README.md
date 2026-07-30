# EU/PL Law Tracker

Skill do analizy statusu regulacji UE i powiązanych aktów/projektów w Polsce.

## Struktura

- `SKILL.md` — instrukcja operacyjna.
- `references/` — źródła, wzorce identyfikatorów, wiarygodność, szablony raportu.
- `scripts/` — pomocnicze skrypty CLI do identyfikacji i ekstrakcji danych.

## Szybkie użycie skryptów

```bash
python scripts/eu_law_identify.py --query "CBAM" --aliases references/regulation-aliases.yaml
python scripts/eu_law_parse.py --input-file path/to/act.txt
python scripts/legal_date_extractor.py --input-file path/to/act.txt
python scripts/relation_extractor.py --input-file path/to/act.txt
```

Wyniki skryptów traktuj jako pomocnicze i zawsze waliduj w źródłach urzędowych.

## Instalacja skilla z ZIP w VS Code

Archiwum skilla znajduje się tutaj:

- `D:\eu-pl-law-tracker\.vscode\eu-pl-law-tracker.zip`

Skrócone kroki instalacji:

1. Zamknij VS Code (zalecane).
2. Rozpakuj ZIP do folderu:
	- `C:\Users\grzeg\AppData\Roaming\Code\User\prompts\skills\eu-pl-law-tracker`
3. Sprawdź, czy istnieje plik:
	- `C:\Users\grzeg\AppData\Roaming\Code\User\prompts\skills\eu-pl-law-tracker\SKILL.md`
4. Uruchom ponownie VS Code i rozpocznij nową rozmowę w Copilot Chat.

Pełna instrukcja jest dostępna w pliku [.vscode/README.MD](.vscode/README.MD).

