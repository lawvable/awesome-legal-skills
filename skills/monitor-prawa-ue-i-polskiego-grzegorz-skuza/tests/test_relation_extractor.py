import importlib.util
import unittest
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT_DIR / "scripts" / "relation_extractor.py"


spec = importlib.util.spec_from_file_location("relation_extractor", MODULE_PATH)
relation_extractor = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(relation_extractor)


class TestRelationExtractor(unittest.TestCase):
    def test_classify_polish_repeal(self) -> None:
        line = "Niniejsze rozporzadzenie uchyla rozporzadzenie (UE) 2020/123."
        self.assertIn("repeals", relation_extractor.classify_line(line))

    def test_classify_english_amend(self) -> None:
        line = "Article 3 is amended as follows."
        self.assertIn("amends", relation_extractor.classify_line(line))

    def test_classify_polish_authority_and_sanctions(self) -> None:
        line = "Organ wlasciwy naklada sankcje pieniezne."
        result = relation_extractor.classify_line(line)
        self.assertIn("competent_authority", result)
        self.assertIn("national_sanctions", result)

    def test_extract_detailed_includes_evidence(self) -> None:
        text = "This delegated act supplements Regulation (EU) 2023/956."
        rows = relation_extractor.extract(text, detailed=True)
        self.assertEqual(1, len(rows))
        self.assertIn("supplements", rows[0]["relations"])
        self.assertIn("evidence", rows[0])
        self.assertIn("supplements", rows[0]["evidence"])

    def test_summary_counts_relations(self) -> None:
        text = """\
This Regulation shall be repealed.
Article 3 is amended.
Article 4 is amended.
"""
        rows = relation_extractor.extract(text)
        summary = relation_extractor.summarize(rows)
        self.assertEqual(1, summary.get("repeals"))
        self.assertEqual(2, summary.get("amends"))


if __name__ == "__main__":
    unittest.main()
