import csv
import io
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIELDS = {'grids': ['grid', 'block', 'ready_on'], 'relations': ['left', 'right', 'kind', 'registered_on'], 'wave_plan': ['wave', 'invite_on', 'freeze_on', 'max_global', 'seed'], 'quotas': ['wave', 'block', 'quota'], 'assignments': ['wave', 'grid', 'status', 'notified_on'], 'study': ['primary', 'days', 'min_direct_units', 'min_unexposed_units', 'signal'], 'contacts': ['person', 'grid', 'kind', 'at'], 'registrants': ['person', 'grid', 'eligible', 'registered_on'], 'outcomes': ['person', 'status', 'stable', 'observed_on', 'available_on']}


class DataContractTests(unittest.TestCase):
    def test_readable_source_tables(self):
        for name, fields in FIELDS.items():
            with self.subTest(table=name):
                text = (ROOT / 'data' / (name + '.csv')).read_text(encoding='utf-8')
                with io.StringIO(text, newline='') as stream:
                    reader = csv.reader(stream, strict=True)
                    self.assertEqual(next(reader), fields)
                    rows = list(reader)
                self.assertTrue(rows)
                self.assertTrue(all(len(row) == len(fields) for row in rows))
