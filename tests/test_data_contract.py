import csv
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class FixtureContractTests(unittest.TestCase):
    def test_fixture_headers_and_rows_match_documented_contract(self):
        for path in sorted((ROOT / 'data').glob('*.csv')):
            with path.open(encoding='utf-8', newline='') as stream:
                rows = list(csv.reader(stream))
            self.assertGreaterEqual(len(rows), 2, path.name)
            self.assertTrue(all(len(row) == len(rows[0]) for row in rows), path.name)
            self.assertTrue(all(rows[0]), path.name)

if __name__ == '__main__':
    unittest.main()
