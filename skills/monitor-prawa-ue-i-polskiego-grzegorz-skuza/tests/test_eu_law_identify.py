import importlib.util
import unittest
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT_DIR / "scripts" / "eu_law_identify.py"
ALIASES_PATH = ROOT_DIR / "references" / "regulation-aliases.yaml"


spec = importlib.util.spec_from_file_location("eu_law_identify", MODULE_PATH)
eu_law_identify = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(eu_law_identify)


class TestEuLawIdentify(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.aliases = eu_law_identify.parse_aliases_minimal_yaml(ALIASES_PATH)

    def test_detects_full_celex(self) -> None:
        result = eu_law_identify.identify("Sprawdz CELEX 32023R0956", self.aliases)
        self.assertEqual("celex", result["match_type"])
        self.assertEqual("32023R0956", result["primary"]["celex"])

    def test_normalizes_short_celex(self) -> None:
        result = eu_law_identify.identify("Czy to 2023R0956?", self.aliases)
        self.assertEqual("celex", result["match_type"])
        self.assertEqual("32023R0956", result["primary"]["celex"])

    def test_prefers_alias_for_cbam_phrase(self) -> None:
        query = "CBAM rozporzadzenie 2023/956 i import cementu spoza UE"
        result = eu_law_identify.identify(query, self.aliases)
        self.assertEqual("alias", result["match_type"])
        self.assertEqual("cbam", result["primary"]["alias"])
        self.assertIn("2023/956", result["identifiers"]["act_numbers"])

    def test_detects_eli(self) -> None:
        query = "https://eur-lex.europa.eu/eli/reg/2023/956/oj"
        result = eu_law_identify.identify(query, self.aliases)
        self.assertEqual("eli", result["match_type"])
        self.assertIn("/eli/reg/2023/956", result["primary"]["eli"])

    def test_returns_topic_for_unknown_query(self) -> None:
        result = eu_law_identify.identify("przepisy o lodach i turystyce kosmicznej", self.aliases)
        self.assertEqual("topic", result["match_type"])
        self.assertEqual("low", result["confidence"])


if __name__ == "__main__":
    unittest.main()
