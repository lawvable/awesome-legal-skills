import importlib.util
import unittest
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT_DIR / "scripts" / "eu_law_parse.py"


spec = importlib.util.spec_from_file_location("eu_law_parse", MODULE_PATH)
eu_law_parse = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(eu_law_parse)


class TestEuLawParse(unittest.TestCase):
    def test_entry_into_force_with_article_and_date(self) -> None:
        text = "Art. 36 Niniejsze rozporzadzenie wchodzi w zycie z dniem 1 stycznia 2027 r."
        rows = eu_law_parse.extract_final_provisions(text)
        self.assertEqual(1, len(rows))
        self.assertIn("entry_into_force", rows[0]["event_types"])
        self.assertIn("Art. 36", rows[0]["article_refs"])
        self.assertIn("2027-01-01", rows[0]["normalized_dates"])

    def test_member_states_deadline_and_relative_timeframe(self) -> None:
        text = "Panstwa czlonkowskie wyznaczaja wlasciwy organ najpozniej do dnia 31.12.2028, w terminie 6 miesiecy od dnia publikacji."
        rows = eu_law_parse.extract_final_provisions(text)
        self.assertEqual(1, len(rows))
        self.assertIn("member_state_obligation", rows[0]["event_types"])
        self.assertIn("competent_authority", rows[0]["event_types"])
        self.assertIn("deadline", rows[0]["event_types"])
        self.assertIn("member_states", rows[0]["actors"])
        self.assertIn("competent_authority", rows[0]["actors"])
        self.assertIn("2028-12-31", rows[0]["normalized_dates"])
        self.assertTrue(rows[0]["relative_timeframes"])

    def test_commission_amendment_repeal(self) -> None:
        text = "Article 12 is amended and Article 15 shall be repealed; the Commission shall adopt implementing acts by 1 January 2030."
        rows = eu_law_parse.extract_final_provisions(text)
        self.assertEqual(1, len(rows))
        self.assertIn("amendment", rows[0]["event_types"])
        self.assertIn("repeal", rows[0]["event_types"])
        self.assertIn("commission_implementing", rows[0]["event_types"])
        self.assertIn("deadline", rows[0]["event_types"])
        self.assertIn("commission", rows[0]["actors"])
        self.assertIn("2030-01-01", rows[0]["normalized_dates"])

    def test_summary_counts_events_and_actors(self) -> None:
        text = """\
Article 1 shall enter into force on 2026-01-01.
Member States shall designate competent authorities by 01/06/2026.
Transitional provisions apply from 1 July 2026.
"""
        rows = eu_law_parse.extract_final_provisions(text)
        summary = eu_law_parse.summarize(rows)
        self.assertEqual(3, summary["total_lines_matched"])
        self.assertEqual(3, summary["lines_with_dates"])
        self.assertEqual(1, summary["event_type_counts"].get("entry_into_force"))
        self.assertEqual(1, summary["event_type_counts"].get("member_state_obligation"))
        self.assertEqual(1, summary["event_type_counts"].get("transitional_provisions"))
        self.assertGreaterEqual(summary["actor_counts"].get("member_states", 0), 1)


if __name__ == "__main__":
    unittest.main()
