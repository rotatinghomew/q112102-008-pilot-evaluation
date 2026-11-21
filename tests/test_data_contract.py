import csv
import io
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIELDS = {'regimes': ['region', 'at', 'cutoff', 'rubric'], 'profile': ['resident', 'region', 'applied_at', 'freeze_on', 'prior_failed', 'mobility', 'exception'], 'score_revisions': ['revision', 'resident', 'score', 'state', 'recorded_at'], 'results': ['resident', 'took_ride', 'abandoned', 'observed_at'], 'analytic_policy': ['rubric', 'windows', 'min_distinct_per_side', 'max_adjacent_ratio', 'max_prior_gap', 'min_uptake_jump', 'maturity_days'], 'plan_policy': ['week', 'budget', 'minimum_gain', 'pilot_slots'], 'planning_requests': ['request', 'region', 'score', 'vehicle', 'start', 'end'], 'trips': ['trip', 'region', 'vehicle', 'start', 'end', 'pool', 'link', 'leg', 'cost'], 'prior_promises': ['id', 'request', 'trips', 'notified_at'], 'planning_changes': ['id', 'kind', 'subject', 'at'], 'proposals': ['id', 'region', 'candidate_cutoff', 'week']}


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
