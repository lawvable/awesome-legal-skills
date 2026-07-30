import importlib.util
import unittest
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT_DIR / "scripts" / "legal_date_extractor.py"


spec = importlib.util.spec_from_file_location("legal_date_extractor", MODULE_PATH)
legal_date_extractor = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(legal_date_extractor)


class TestLegalDateExtractor(unittest.TestCase):
    def test_entry_into_force_with_polish_textual_date(self) -> None:
        text = "Niniejsze rozporzadzenie wchodzi w zycie z dniem 12 maja 2026 r."
        rows = legal_date_extractor.extract(text)
        self.assertEqual(1, len(rows))
        self.assertIn("entry_into_force", rows[0]["event_types"])
        self.assertIn("2026-05-12", rows[0]["normalized_dates"])

    def test_application_start_english_iso_date(self) -> None:
        text = "This Regulation shall apply from 2027-01-01."
        rows = legal_date_extractor.extract(text)
        self.assertEqual(1, len(rows))
        self.assertIn("application_start", rows[0]["event_types"])
        self.assertIn("2027-01-01", rows[0]["normalized_dates"])

    def test_deadline_and_relative_timeframe(self) -> None:
        text = "Panstwa czlonkowskie przyjmuja przepisy najpozniej do dnia 31.12.2028, w terminie 6 miesiecy od dnia publikacji."
        rows = legal_date_extractor.extract(text)
        self.assertEqual(1, len(rows))
        self.assertIn("deadline_general", rows[0]["event_types"])
        self.assertIn("transposition_deadline", rows[0]["event_types"])
        self.assertIn("2028-12-31", rows[0]["normalized_dates"])
        self.assertTrue(rows[0]["relative_timeframes"])

    def test_repeal_effective_and_publication_reference(self) -> None:
        text = "Act shall be repealed with effect from 01/02/2030 and published in the Official Journal of the European Union."
        rows = legal_date_extractor.extract(text)
        self.assertEqual(1, len(rows))
        self.assertIn("repeal_effective", rows[0]["event_types"])
        self.assertIn("publication_reference", rows[0]["event_types"])
        self.assertIn("2030-02-01", rows[0]["normalized_dates"])

    def test_summary_contains_event_counts(self) -> None:
        text = """\
This Regulation shall enter into force on 2026-01-01.
This Regulation shall apply from 2026-06-01.
By 01.01.2027 the Commission shall review this Regulation.
"""
        rows = legal_date_extractor.extract(text)
        summary = legal_date_extractor.summarize(rows)
        self.assertEqual(3, summary["total_matches"])
        self.assertEqual(3, summary["lines_with_dates"])
        self.assertEqual(1, summary["event_type_counts"].get("entry_into_force"))
        self.assertEqual(1, summary["event_type_counts"].get("application_start"))
        self.assertEqual(1, summary["event_type_counts"].get("review_clause"))


if __name__ == "__main__":
    unittest.main()
