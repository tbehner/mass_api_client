import json

from mass_api_client.resources import ScheduledAnalysis
from tests.serialization_test_case import SerializationTestCase


class ScheduledAnalysisTestCase(SerializationTestCase):
    def test_is_data_correct_after_serialization(self):
        with open('tests/data/scheduled_analysis.json') as data_file:
            data = json.load(data_file)

        self.assertEqualAfterSerialization(ScheduledAnalysis(), data)
